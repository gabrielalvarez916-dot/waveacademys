# -*- coding: utf-8 -*-
"""Matemática I · Misión 13 · Enteros: producto, cociente y potencias. Genera mision-13.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
neg=lambda n:["-%s"%n,"−%s"%n]
N1={
"objetivo":"Vas a poder multiplicar números enteros aplicando la regla de los signos y entender por qué funciona.",
"vas_a_ver":["La multiplicación como suma repetida","La regla de los signos","Por qué menos por menos da más","Productos de varios factores"],
"secciones":[
 S(1,"Suma repetida",[
  D("Multiplicar por un positivo","Multiplicar por un número positivo es sumar varias veces: 3 × (−4) = (−4) + (−4) + (−4) = −12."),
 ]),
 S(1,"La regla de los signos",[
  D("Regla de los signos","Se multiplican los valores absolutos y el signo es: <b>signos iguales, resultado positivo</b>; <b>signos distintos, resultado negativo</b>."),
  T("La regla",["Factores","Signo del producto","Ejemplo"],[["+ × +","+","3 × 4 = 12"],["− × −","+","(−3) × (−4) = 12"],["+ × −","−","3 × (−4) = −12"],["− × +","−","(−3) × 4 = −12"]]),
 ]),
 S(2,"Por qué menos por menos da más",[
  P("Mirá el patrón: (−3) × 2 = −6; (−3) × 1 = −3; (−3) × 0 = 0. Cada vez que el segundo factor baja 1, el resultado sube 3. Siguiendo: (−3) × (−1) = 3 y (−3) × (−2) = 6."),
 ]),
 S(2,"Varios factores",[
  P("Se cuentan los factores negativos: si son una cantidad <b>par</b>, el resultado es positivo; si son <b>impar</b>, negativo."),
  E("Contar negativos","Dos productos.",["(−2) × 3 × (−5): dos negativos, positivo. 2 × 3 × 5 = 30. Resultado 30.","(−1) × (−2) × (−3): tres negativos, negativo. 1 × 2 × 3 = 6. Resultado −6."]),
 ]),
],
"ejemplo_completo":{"titulo":"(−4) × 5 × (−2) × (−1)","planteo":"Calculá (−4) × 5 × (−2) × (−1).","pasos":["Factores negativos: −4, −2 y −1. Son tres: impar.","El resultado es negativo.","Valores absolutos: 4 × 5 × 2 × 1 = 40.","Resultado: −40."]},
"ejemplo_incompleto":{"titulo":"(−6) × (−7)","planteo":"Completá los espacios.","pasos":["Los signos son iguales: el resultado es ___ .","6 × 7 = ___ .","(−6) × (−7) = 42."]},
"ejemplo_solo":{"titulo":"2 × (−3) × (−4) × (−5)","planteo":"Calculá 2 × (−3) × (−4) × (−5)."},
"tip":{"titulo":"Primero el signo","texto":"Decidí el signo contando negativos y después multiplicá los números sin signo. Así no se te pierde."},
"ojo":["Creer que menos por menos es menos: (−5) × (−2) = 10.","Sumar en vez de multiplicar: (−3) × (−4) no es −7."],
"resumen":[{"titulo":"Iguales","texto":"Signos iguales: positivo. Ej.: (−3) × (−4) = 12."},{"titulo":"Distintos","texto":"Signos distintos: negativo. Ej.: 3 × (−4) = −12."},{"titulo":"Varios","texto":"Cantidad par de negativos: +; impar: −."}],
"glosario":[{"palabra":"Factor","significado":"Cada número que se multiplica."},{"palabra":"Producto","significado":"El resultado de una multiplicación."},{"palabra":"Regla de los signos","significado":"Indica el signo de un producto o cociente."}],
"carpeta":["Calculá (−8) × 3.","Calculá (−9) × (−4).","Calculá (−1) × (−1) × (−1) × (−1).","Un compañero dice que (−5) × (−2) = −10. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[neg(24),["36"],["1"],["10"]],
"soluciones":{"incompleto":"Positivo. 42.","solo":"Tres negativos: negativo. 2 × 3 × 4 × 5 = 120. Resultado −120.","carpeta":["−24: signos distintos.","36: signos iguales.","1: cuatro negativos, cantidad par.","10: menos por menos da más."]}
}
N2={
"objetivo":"Vas a poder dividir números enteros con la regla de los signos, resolver divisiones con resto y saber qué pasa con el cero.",
"vas_a_ver":["La regla de los signos en la división","Comprobar con la multiplicación","Casos con cero","División con resto"],
"secciones":[
 S(1,"Regla de los signos",[
  D("División de enteros","Se dividen los valores absolutos y el signo sigue la <b>misma regla que la multiplicación</b>: iguales, positivo; distintos, negativo."),
  P("Ejemplos: (−20) ÷ 4 = −5. (−18) ÷ (−3) = 6. 15 ÷ (−5) = −3. Se comprueba multiplicando: 4 × (−5) = −20."),
 ]),
 S(1,"El cero",[
  D("Casos con cero","0 dividido cualquier número (distinto de 0) da <b>0</b>: 0 ÷ (−7) = 0. Pero <b>no se puede dividir por 0</b>: ningún número multiplicado por 0 da −7."),
 ]),
 S(2,"División con resto",[
  P("Se mantiene la relación de siempre, dividendo = divisor × cociente + resto, con el resto <b>positivo o cero</b> y menor que el valor absoluto del divisor."),
  E("(−17) ÷ 5","Buscamos un resto entre 0 y 4.",["5 × (−3) = −15, pero de −15 a −17 habría que restar: no sirve.","5 × (−4) = −20, y de −20 a −17 hay que sumar 3.","Cociente −4 y resto 3: −17 = 5 × (−4) + 3."]),
 ]),
 S(2,"Comprobar",[
  P("Siempre podés comprobar: divisor × cociente + resto tiene que dar el dividendo, con el signo correcto."),
 ]),
],
"ejemplo_completo":{"titulo":"(−84) ÷ (−7)","planteo":"Calculá (−84) ÷ (−7) y comprobá.","pasos":["Signos iguales: positivo.","84 ÷ 7 = 12.","Resultado: 12.","Comprobación: (−7) × 12 = −84."]},
"ejemplo_incompleto":{"titulo":"(−56) ÷ 8","planteo":"Completá los espacios.","pasos":["Signos distintos: el resultado es ___ .","56 ÷ 8 = ___ .","Comprobación: 8 × (−7) = ___ ."]},
"ejemplo_solo":{"titulo":"(−23) ÷ 4","planteo":"Calculá el cociente y el resto de (−23) ÷ 4, con el resto positivo o cero."},
"tip":{"titulo":"La misma regla","texto":"Si ya sabés la regla de la multiplicación, ya sabés la de la división: es la misma."},
"ojo":["Dividir por cero: no tiene resultado.","Dar un resto negativo: el resto siempre es positivo o cero."],
"resumen":[{"titulo":"Signos","texto":"Iguales: +; distintos: −."},{"titulo":"Ejemplo","texto":"(−18) ÷ (−3) = 6."},{"titulo":"Cero","texto":"0 ÷ a = 0; a ÷ 0 no existe."},{"titulo":"Resto","texto":"−17 = 5 × (−4) + 3."}],
"glosario":[{"palabra":"Cociente","significado":"El resultado de la división."},{"palabra":"Resto","significado":"Lo que sobra; positivo o cero."},{"palabra":"Comprobar","significado":"Verificar multiplicando."}],
"carpeta":["Calculá (−45) ÷ 9.","Calculá (−36) ÷ (−6).","Calculá 0 ÷ (−8).","Un compañero dice que (−30) ÷ (−5) = −6. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[neg(5),["6"],["0"],["6"]],
"soluciones":{"incompleto":"Negativo. 7. −56.","solo":"4 × (−6) = −24, y −24 + 1 = −23. Cociente −6, resto 1.","carpeta":["−5: signos distintos.","6: signos iguales.","0: cero dividido cualquier número da cero.","6: signos iguales, resultado positivo."]}
}
N3={
"objetivo":"Vas a poder resolver cálculos combinados con enteros respetando la jerarquía y los signos, y aplicar la distributiva con negativos.",
"vas_a_ver":["La jerarquía con enteros","La distributiva con negativos","Paréntesis y signos","La diferencia entre −3² y (−3)²"],
"secciones":[
 S(1,"Jerarquía con signos",[
  D("El orden de siempre","Primero <b>paréntesis</b>, después <b>potencias</b>, después <b>× y ÷</b> (con la regla de los signos) y al final <b>sumas y restas</b>."),
  P("Ejemplo: (−3) + 4 × (−2) = (−3) + (−8) = −11. Primero la multiplicación."),
 ]),
 S(1,"Distributiva con negativos",[
  D("Distribuir un negativo","El factor multiplica a <b>cada término</b>, con su signo: −2 × (5 − 3) = −2 × 5 − 2 × (−3) = −10 + 6 = −4."),
  P("Comprobación: −2 × (5 − 3) = −2 × 2 = −4."),
 ]),
 S(2,"−3² y (−3)²",[
  P("La potencia afecta solo a lo que tiene pegado. En <b>(−3)²</b> la base es −3: (−3) × (−3) = 9. En <b>−3²</b> la base es 3 y el signo queda afuera: −(3 × 3) = −9."),
 ]),
 S(2,"Cálculos largos",[
  E("(−12) ÷ (−4) − 2 × (−5)","Términos y signos.",["(−12) ÷ (−4) = 3.","2 × (−5) = −10, y restar −10 es sumar 10.","3 + 10 = 13."]),
 ]),
],
"ejemplo_completo":{"titulo":"5 − 3 × (−4) + (−20) ÷ 5","planteo":"Resolvé con una igualdad por línea.","pasos":["Multiplicación y división: 3 × (−4) = −12 y (−20) ÷ 5 = −4.","= 5 − (−12) + (−4).","= 5 + 12 − 4.","= 13."]},
"ejemplo_incompleto":{"titulo":"(−2) × (7 − 10)","planteo":"Completá los espacios.","pasos":["Paréntesis: 7 − 10 = ___ .","(−2) × (−3) = ___ ."]},
"ejemplo_solo":{"titulo":"18 ÷ (−6) − (−4) × 3","planteo":"Resolvé respetando la jerarquía."},
"tip":{"titulo":"Escribí el signo del resultado","texto":"Después de cada multiplicación o división, escribí el resultado entre paréntesis si es negativo: así ves bien qué signo queda adelante."},
"ojo":["Perder el signo al distribuir: −4 × (3 − 5) = −12 + 20 = 8.","Confundir −3² con (−3)²: valen −9 y 9."],
"resumen":[{"titulo":"Jerarquía","texto":"Paréntesis, potencias, × y ÷, + y −."},{"titulo":"Distributiva","texto":"−2 × (5 − 3) = −10 + 6 = −4."},{"titulo":"Potencia","texto":"(−3)² = 9; −3² = −9."}],
"glosario":[{"palabra":"Jerarquía","significado":"Orden en que se resuelven las operaciones."},{"palabra":"Distribuir","significado":"Multiplicar un factor por cada término."},{"palabra":"Base","significado":"El número que se multiplica en una potencia."}],
"carpeta":["Calculá (−2) + 3 × (−4).","Calculá −3 × (2 − 6).","Calculá (−20) ÷ (−5) − 7.","Un compañero distribuyó −4 × (3 − 5) y escribió −12 − 20. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[neg(14),["12"],neg(3),["8"]],
"soluciones":{"incompleto":"−3. 6.","solo":"18 ÷ (−6) = −3 y (−4) × 3 = −12. −3 − (−12) = −3 + 12 = 9.","carpeta":["−14: 3 × (−4) = −12; −2 − 12.","12: −3 × (−4).","−3: 4 − 7.","8: −4 × 3 = −12 y −4 × (−5) = 20. −12 + 20 = 8."]}
}
N4={
"objetivo":"Vas a poder calcular potencias de base negativa, saber su signo según el exponente y calcular raíces de enteros cuando existen.",
"vas_a_ver":["Potencias de base negativa","El signo según el exponente","−2² no es (−2)²","Raíces cuadradas y cúbicas de enteros","Propiedades con enteros"],
"secciones":[
 S(1,"Base negativa",[
  D("Signo de la potencia","Si la base es negativa: con <b>exponente par</b> el resultado es <b>positivo</b>; con <b>exponente impar</b>, <b>negativo</b>."),
  T("Potencias de −2",["Potencia","Producto","Resultado"],[["(−2)²","(−2) × (−2)","4"],["(−2)³","(−2) × (−2) × (−2)","−8"],["(−2)⁴","(−2) × (−2) × (−2) × (−2)","16"]],"Es la regla de contar negativos: cada factor es un negativo."),
 ]),
 S(1,"Ojo con los paréntesis",[
  D("−2² y (−2)²","Sin paréntesis, la potencia es solo del número: −2² = −(2 × 2) = −4. Con paréntesis, es del negativo: (−2)² = 4."),
 ]),
 S(2,"Raíces de enteros",[
  P("<b>Raíz cúbica</b> de un negativo: existe y es negativa. ∛(−8) = −2, porque (−2)³ = −8. <b>Raíz cuadrada</b> de un negativo: <b>no existe</b> en los enteros, porque ningún número al cuadrado da negativo. La raíz cuadrada de un positivo se toma positiva: √25 = 5."),
 ]),
 S(2,"Propiedades",[
  P("Las propiedades de las potencias valen igual con base negativa: (−2)³ × (−2)² = (−2)⁵ = −32. Y (−1) elevado a cualquier par da 1; a cualquier impar, −1."),
 ]),
],
"ejemplo_completo":{"titulo":"(−3)³ + (−2)⁴ − ∛(−64)","planteo":"Resolvé.","pasos":["(−3)³ = −27 (exponente impar).","(−2)⁴ = 16 (exponente par).","∛(−64) = −4, porque (−4)³ = −64.","−27 + 16 − (−4) = −27 + 16 + 4 = −7."]},
"ejemplo_incompleto":{"titulo":"con y sin paréntesis","planteo":"Completá los espacios.","pasos":["(−5)² = ___ .","−5² = ___ .","∛(−125) = ___ ."]},
"ejemplo_solo":{"titulo":"(−1)⁵ + (−2)³ − √49","planteo":"Resolvé."},
"tip":{"titulo":"Par o impar","texto":"Antes de calcular una potencia de base negativa, mirá el exponente: par, positivo; impar, negativo."},
"ojo":["Creer que (−2)⁴ es negativo: es 16, exponente par.","Pensar que −2² = 4: sin paréntesis da −4."],
"resumen":[{"titulo":"Exponente par","texto":"Positivo. Ej.: (−2)⁴ = 16."},{"titulo":"Exponente impar","texto":"Negativo. Ej.: (−2)³ = −8."},{"titulo":"Paréntesis","texto":"−2² = −4; (−2)² = 4."},{"titulo":"Raíces","texto":"∛(−8) = −2; √(−9) no existe en los enteros."}],
"glosario":[{"palabra":"Exponente par","significado":"2, 4, 6…"},{"palabra":"Exponente impar","significado":"1, 3, 5…"},{"palabra":"Raíz cúbica","significado":"Número que elevado al cubo da el radicando."}],
"carpeta":["Calculá (−4)³.","Calculá (−3)⁴.","Calculá ∛(−1.000).","Un compañero dice que −6² = 36. ¿Cuánto vale −6²?"],
"respuestas_carpeta":[neg(64),["81"],neg(10),neg(36)],
"soluciones":{"incompleto":"25. −25. −5.","solo":"−1 + (−8) − 7 = −16.","carpeta":["−64: exponente impar.","81: exponente par.","−10: (−10)³ = −1.000.","−36: sin paréntesis, la potencia es solo del 6."]}
}
ACT={
"1":[N("Calculá ({a}) × ({c}).",{"formula":"x*y"},"Signos iguales: resultado positivo.",{"vars":{"x":{"min":2,"max":12},"y":{"min":2,"max":12}},"calculadas":{"a":"0-x","c":"0-y"}}),
     MC("¿Qué signo tiene (−2) × (−3) × (−4)?",["Positivo","Negativo"],"Negativo","Tres factores negativos: cantidad impar.")],
"2":[N("Calculá ({d}) ÷ {b}.",{"formula":"0-q"},"Signos distintos: resultado negativo.",{"vars":{"b":{"min":2,"max":9},"q":{"min":2,"max":12}},"calculadas":{"d":"0-b*q"}}),
     VF("Se puede dividir cualquier entero por 0.","Falso","Dividir por 0 no tiene resultado.")],
"3":[N("Calculá (−3) × 4 + (−18) ÷ 3.",{"acepta":[-18]},"−12 + (−6) = −18."),
     MC("¿Cuánto vale −3 elevado a 2, si el exponente afecta solo al 3 (sin paréntesis)?",["9","−9","6","−6"],"−9","−(3 × 3) = −9.")],
"4":[N("Calculá (−2) elevado a 5.",{"acepta":[-32]},"Exponente impar: negativo. 2⁵ = 32."),
     {"t":"classify","p":"Clasificá cada potencia según el signo del resultado.","o":{"elementos":["(−2) elevado a 2","(−2) elevado a 3","(−1) elevado a 10","(−5) elevado a 3"],"categorias":["Positivo","Negativo"]},"r":{"categorias":{"(−2) elevado a 2":"Positivo","(−2) elevado a 3":"Negativo","(−1) elevado a 10":"Positivo","(−5) elevado a 3":"Negativo"}},"e":"Exponente par: positivo; impar: negativo."}],
"5":[N("Relámpago. Calculá (−6) × 5.",{"acepta":[-30]},"Signos distintos.",tiempo=20),
     N("Relámpago. Calculá (−42) ÷ (−7).",{"acepta":[6]},"Signos iguales.",tiempo=25),
     N("Relámpago. Calculá (−3) elevado a 2.",{"acepta":[9]},"Exponente par.",tiempo=20),
     N("Relámpago. Calculá (−8) + 3.",{"acepta":[-5]},"Repaso de la misión 12.",tiempo=25)],
}
EXAMEN=[
 [1,N("Calculá (−7) × (−8).",{"acepta":[56]},"Signos iguales: positivo.")],
 [1,N("Calculá (−1) × 2 × (−3) × (−4).",{"acepta":[-24]},"Tres negativos: negativo. 1 × 2 × 3 × 4 = 24.")],
 [1,MC("Si un producto tiene 4 factores negativos, el resultado es…",["Positivo","Negativo","Cero"],"Positivo","Cantidad par de negativos.")],
 [2,N("Calculá (−63) ÷ 9.",{"acepta":[-7]},"Signos distintos.")],
 [2,N("Calculá (−48) ÷ (−6).",{"acepta":[8]},"Signos iguales.")],
 [2,MC("En la división (−17) ÷ 5, con resto positivo y menor que 5, ¿cuál es el cociente?",["−3","−4","3","4"],"−4","5 × (−4) = −20 y −20 + 3 = −17: resto 3.")],
 [3,N("Calculá 10 − 2 × (−6).",{"acepta":[22]},"2 × (−6) = −12; 10 − (−12) = 22.")],
 [3,N("Calculá (−5) × (3 − 7).",{"acepta":[20]},"(−5) × (−4) = 20.")],
 [3,VF("(−4) elevado a 2 y −4 elevado a 2 (sin paréntesis) tienen el mismo valor.","Falso","(−4)² = 16 y −4² = −16.")],
 [4,N("Calculá (−3) elevado a 3.",{"acepta":[-27]},"Exponente impar: negativo.")],
 [4,N("Calculá la raíz cúbica de −8.",{"acepta":[-2]},"(−2)³ = −8.")],
 [4,MC("¿Cuánto vale la raíz cuadrada de −16 en los números enteros?",["4","−4","No existe","16"],"No existe","Ningún entero al cuadrado da un número negativo.")],
 [4,N("Calculá (−1) elevado a 7 + (−1) elevado a 8.",{"acepta":[0]},"−1 + 1 = 0.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":13,"practica":"Práctica general: producto, cociente y potencias de enteros","examen_titulo":"Nivel jefe: producto, cociente y potencias de enteros",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-13.json"),"w"),ensure_ascii=False)
print("ok")
