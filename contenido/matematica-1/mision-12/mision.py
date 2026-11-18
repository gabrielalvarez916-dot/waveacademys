# -*- coding: utf-8 -*-
"""Matemática I · Misión 12 · Números enteros: suma y resta. Genera mision-12.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
neg=lambda n:["-%s"%n,"−%s"%n]
N1={
"objetivo":"Vas a poder sumar números enteros, primero con la recta numérica y después con las reglas de los signos.",
"vas_a_ver":["Sumar con la recta numérica","Sumar enteros de igual signo","Sumar enteros de distinto signo","Propiedades de la suma"],
"secciones":[
 S(1,"Sumar en la recta",[
  D("Suma en la recta","Se parte del primer número y se avanza el segundo: si es <b>positivo</b>, hacia la <b>derecha</b>; si es <b>negativo</b>, hacia la <b>izquierda</b>."),
  P("Ejemplo: 3 + (−5): parto del 3 y me muevo 5 lugares a la izquierda; llego a −2. Los negativos se escriben entre paréntesis cuando van después de un signo: 3 + (−5)."),
 ]),
 S(1,"Las reglas",[
  D("Reglas de la suma","<b>Igual signo:</b> se suman los valores absolutos y se deja el signo. <b>Distinto signo:</b> se restan los valores absolutos (mayor menos menor) y se pone el signo del que tiene mayor valor absoluto."),
  T("Ejemplos",["Suma","Signos","Cuenta","Resultado"],[["(−4) + (−6)","iguales","4 + 6 = 10","−10"],["(−9) + 4","distintos","9 − 4 = 5","−5"],["9 + (−4)","distintos","9 − 4 = 5","5"]]),
 ]),
 S(2,"Propiedades",[
  P("La suma de enteros es <b>conmutativa</b> y <b>asociativa</b>, el <b>0</b> no cambia nada (a + 0 = a) y un número más su <b>opuesto</b> da 0: 7 + (−7) = 0."),
 ]),
 S(2,"Varios sumandos",[
  P("Con varios sumandos, podés sumar de a dos o agrupar los positivos por un lado y los negativos por otro."),
  E("Sumar (−12) + 7 + (−5) + 10","Agrupamos por signo.",["Positivos: 7 + 10 = 17.","Negativos: (−12) + (−5) = −17.","17 + (−17) = 0."]),
 ]),
],
"ejemplo_completo":{"titulo":"(−15) + (−7) + 20","planteo":"Calculá (−15) + (−7) + 20.","pasos":["(−15) + (−7): igual signo. 15 + 7 = 22, signo −: −22.","(−22) + 20: distinto signo. 22 − 20 = 2.","Gana el signo del 22, que es negativo: −2.","En la recta: desde −22 avanzo 20 a la derecha y llego a −2."]},
"ejemplo_incompleto":{"titulo":"(−8) + 3","planteo":"Completá los espacios.","pasos":["Los signos son distintos.","8 − 3 = ___ .","El de mayor valor absoluto es −8: el signo es ___ .","Resultado: ___ ."]},
"ejemplo_solo":{"titulo":"(−6) + 14 + (−3)","planteo":"Calculá (−6) + 14 + (−3)."},
"tip":{"titulo":"¿Quién gana?","texto":"Con signos distintos, imaginá una pulseada: gana el que tiene más fuerza (mayor valor absoluto), y la diferencia es lo que le sobra."},
"ojo":["Sumar siempre los valores absolutos: (−7) + 3 no es −10; es −4.","Poner el signo del menor: en 9 + (−4) gana el 9, el resultado es positivo."],
"resumen":[{"titulo":"Recta","texto":"Positivo a la derecha, negativo a la izquierda."},{"titulo":"Igual signo","texto":"Se suman y se deja el signo. Ej.: (−4) + (−6) = −10."},{"titulo":"Distinto signo","texto":"Se restan; signo del mayor. Ej.: (−9) + 4 = −5."},{"titulo":"Opuestos","texto":"7 + (−7) = 0."}],
"glosario":[{"palabra":"Sumando","significado":"Cada número que se suma."},{"palabra":"Valor absoluto","significado":"Distancia al cero, sin signo."},{"palabra":"Opuesto","significado":"El número que sumado da 0."}],
"carpeta":["Calculá (−6) + (−9).","Calculá (−11) + 4.","Calculá 13 + (−8).","Un compañero hizo (−7) + 3 = −10. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[neg(15),neg(7),["5"],neg(4)],
"soluciones":{"incompleto":"5. Signo −. Resultado: −5.","solo":"(−6) + 14 = 8; 8 + (−3) = 5.","carpeta":["−15: igual signo, 6 + 9.","−7: 11 − 4, gana el negativo.","5: 13 − 8, gana el positivo.","−4: signos distintos, se restan: 7 − 3 = 4, con el signo del 7."]}
}
N2={
"objetivo":"Vas a poder restar números enteros transformando la resta en una suma del opuesto, y calcular diferencias de temperatura o de altura.",
"vas_a_ver":["Restar es sumar el opuesto","Por qué restar un negativo suma","Resta de negativos","Diferencias de temperaturas y alturas"],
"secciones":[
 S(1,"Restar es sumar el opuesto",[
  D("Resta de enteros","Para restar, se <b>suma el opuesto</b> del número que se resta: a − b = a + (−b)."),
  T("Ejemplos",["Resta","Como suma","Resultado"],[["5 − 8","5 + (−8)","−3"],["4 − (−6)","4 + 6","10"],["(−3) − (−7)","(−3) + 7","4"],["(−2) − 5","(−2) + (−5)","−7"]]),
 ]),
 S(1,"Por qué restar un negativo suma",[
  P("Mirá el patrón: 4 − 2 = 2; 4 − 1 = 3; 4 − 0 = 4; 4 − (−1) = 5. Cada vez que lo que restás baja 1, el resultado sube 1. Por eso <b>restar un negativo agranda</b> el resultado."),
 ]),
 S(2,"La resta no es conmutativa",[
  P("3 − 5 = −2, pero 5 − 3 = 2. El orden importa: dan opuestos."),
 ]),
 S(2,"Diferencias",[
  P("La <b>diferencia</b> entre dos valores es el mayor menos el menor. Con negativos, aparece el doble signo."),
  E("Temperaturas","La máxima fue 6 °C y la mínima −4 °C.",["Diferencia: 6 − (−4).","6 + 4 = 10.","Hubo 10 grados de diferencia."]),
 ]),
],
"ejemplo_completo":{"titulo":"(−8) − (−3) − 6","planteo":"Calculá (−8) − (−3) − 6.","pasos":["Cada resta pasa a suma del opuesto: (−8) + 3 + (−6).","(−8) + 3 = −5.","(−5) + (−6) = −11.","Resultado: −11."]},
"ejemplo_incompleto":{"titulo":"dos restas","planteo":"Completá los espacios.","pasos":["7 − (−5) = 7 + ___ = ___ .","(−4) − 9 = (−4) + (−9) = ___ ."]},
"ejemplo_solo":{"titulo":"el avión y el submarino","planteo":"Un avión vuela a 2.500 m de altura y un submarino navega a −300 m. ¿Qué diferencia de altura hay entre los dos?"},
"tip":{"titulo":"Dos signos menos juntos","texto":"Cuando ves − (−…), se convierten en un +: 4 − (−6) = 4 + 6."},
"ojo":["Restar un negativo y achicar: 2 − (−3) no es −1; es 2 + 3 = 5.","Perder el doble signo: en 6 − (−4) hay que cambiar el signo del 4."],
"resumen":[{"titulo":"Regla","texto":"a − b = a + (−b)."},{"titulo":"Doble signo","texto":"4 − (−6) = 4 + 6 = 10."},{"titulo":"No conmutativa","texto":"3 − 5 = −2 y 5 − 3 = 2."},{"titulo":"Diferencia","texto":"Mayor menos menor. Ej.: 6 − (−4) = 10."}],
"glosario":[{"palabra":"Diferencia","significado":"El resultado de una resta."},{"palabra":"Opuesto","significado":"El mismo número con el otro signo."},{"palabra":"Desnivel","significado":"Diferencia de altura entre dos lugares."}],
"carpeta":["Calculá 3 − 10.","Calculá 6 − (−4).","Calculá (−5) − (−8).","Un compañero dice que 2 − (−3) = −1. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[neg(7),["10"],["3"],["5"]],
"soluciones":{"incompleto":"7 + 5 = 12. −13.","solo":"2.500 − (−300) = 2.500 + 300 = 2.800 m.","carpeta":["−7: 3 + (−10).","10: 6 + 4.","3: (−5) + 8.","5: 2 + 3. Restar un negativo es sumar."]}
}
N3={
"objetivo":"Vas a poder resolver sumas algebraicas con varios términos y suprimir paréntesis precedidos por + o por −.",
"vas_a_ver":["Qué es una suma algebraica","Términos con su signo","Suprimir paréntesis con + y con −","Paréntesis y corchetes"],
"secciones":[
 S(1,"Suma algebraica",[
  D("Suma algebraica","Es un cálculo con sumas y restas de enteros. Cada número con el signo que tiene adelante es un <b>término</b>: en 5 − 8 + 3 − 2 los términos son +5, −8, +3 y −2."),
  P("Se resuelve sumando todos los términos. Lo más cómodo es juntar los positivos (5 + 3 = 8) y los negativos (−8 − 2 = −10) y después sumar: 8 + (−10) = −2."),
 ]),
 S(1,"Suprimir paréntesis",[
  D("Reglas","Si el paréntesis tiene un <b>+</b> adelante, se saca y los signos de adentro <b>quedan igual</b>. Si tiene un <b>−</b> adelante, se saca y se <b>cambian todos</b> los signos de adentro."),
  P("Ejemplo: 10 − (4 − 7 + 2) = 10 − 4 + 7 − 2 = 11. Comprobación: adentro da −1, y 10 − (−1) = 11."),
 ]),
 S(2,"Paréntesis y corchetes",[
  P("Se suprimen de adentro hacia afuera, o se resuelve primero lo de adentro. Las dos formas dan lo mismo."),
  E("8 − [3 − (5 − 9)]","Dos caminos.",["Resolviendo adentro: 5 − 9 = −4; 3 − (−4) = 7; 8 − 7 = 1.","Suprimiendo: 8 − [3 − 5 + 9] = 8 − 3 + 5 − 9 = 1."]),
 ]),
 S(2,"Agrupar por signo",[
  P("En cálculos largos, después de sacar los paréntesis, sumá todos los positivos, después todos los negativos, y al final hacé una sola cuenta."),
 ]),
],
"ejemplo_completo":{"titulo":"−6 + (2 − 9) − (−4 + 1 − 3)","planteo":"Resolvé suprimiendo paréntesis.","pasos":["El primer paréntesis tiene +: queda 2 − 9.","El segundo tiene −: se cambian los signos: + 4 − 1 + 3.","−6 + 2 − 9 + 4 − 1 + 3.","Positivos: 2 + 4 + 3 = 9. Negativos: −6 − 9 − 1 = −16.","9 + (−16) = −7."]},
"ejemplo_incompleto":{"titulo":"15 − (6 − 10)","planteo":"Completá los espacios.","pasos":["Hay un − adelante: se cambian los signos de adentro.","15 − 6 + ___ .","Resultado: ___ ."]},
"ejemplo_solo":{"titulo":"20 − (8 + 5 − 3) + (−4 + 7)","planteo":"Resolvé suprimiendo paréntesis."},
"tip":{"titulo":"Cambiá todos","texto":"Un − delante del paréntesis cambia el signo de cada término de adentro, no solo del primero."},
"ojo":["Mantener los signos al sacar un paréntesis con −: 12 − (4 + 6) es 12 − 4 − 6 = 2, no 14.","Cambiar solo el primer signo: en −(5 − 2 + 1) todos cambian: −5 + 2 − 1."],
"resumen":[{"titulo":"Términos","texto":"Cada número con su signo."},{"titulo":"+( )","texto":"Los signos quedan igual."},{"titulo":"−( )","texto":"Se cambian todos los signos de adentro."},{"titulo":"Agrupar","texto":"Positivos por un lado, negativos por otro."}],
"glosario":[{"palabra":"Suma algebraica","significado":"Cálculo con sumas y restas de enteros."},{"palabra":"Término","significado":"Cada número con su signo."},{"palabra":"Suprimir","significado":"Sacar los paréntesis."}],
"carpeta":["Calculá 4 − 9 + 6 − 3.","Calculá 10 − (3 − 8).","Calculá −(−5 + 2).","Un compañero escribió 12 − (4 + 6) = 12 − 4 + 6 = 14. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[neg(2),["15"],["3"],["2"]],
"soluciones":{"incompleto":"15 − 6 + 10. Resultado: 19.","solo":"20 − 8 − 5 + 3 − 4 + 7 = 13.","carpeta":["−2: positivos 10, negativos −12.","15: 10 − 3 + 8.","3: +5 − 2.","2: 12 − 4 − 6. Con un − adelante cambian todos los signos."]}
}
N4={
"objetivo":"Vas a poder resolver problemas de temperaturas, saldos y alturas armando el cálculo con enteros e interpretando el resultado.",
"vas_a_ver":["Pasar una situación a un cálculo con enteros","Saldos y deudas","Temperaturas y desniveles","Qué significa un resultado negativo"],
"secciones":[
 S(1,"Del enunciado al cálculo",[
  D("Modelizar","Se elige el cero de la situación y se traduce: <b>subir, ganar, cobrar o depositar</b> suman; <b>bajar, perder, pagar o gastar</b> restan."),
  T("Traducir",["Situación","Cálculo"],[["Hacía −5 °C y subió 12 grados","−5 + 12 = 7"],["Estaba en el piso 2 y bajó 5","2 − 5 = −3"]]),
 ]),
 S(1,"Saldos y deudas",[
  D("Saldo","El <b>saldo</b> es lo que hay en una cuenta. Si es negativo, es una <b>deuda</b>: −$1.500 significa que se deben $1.500."),
  P("Ejemplo: con $2.000 se pagan $3.500: 2.000 − 3.500 = −1.500. Después se depositan $4.000: −1.500 + 4.000 = 2.500."),
 ]),
 S(2,"Temperaturas y desniveles",[
  P("Para saber <b>cuánto cambió</b> algo, se hace valor final menos valor inicial. Si da positivo, subió; si da negativo, bajó."),
  E("La temperatura","A las 6 h hacía −7 °C y al mediodía 9 °C.",["Cambio: 9 − (−7).","9 + 7 = 16.","Subió 16 grados."]),
 ]),
 S(2,"Interpretar el resultado",[
  P("Un resultado negativo no es un error: puede ser una deuda, una temperatura bajo cero o un subsuelo. Respondé siempre con la unidad: °C, pesos, metros, pisos."),
 ]),
],
"ejemplo_completo":{"titulo":"la cuenta","planteo":"Una cuenta tiene $1.200. Se paga una factura de $3.000, después se cobran $5.000 y se pagan $1.700. ¿Cuál es el saldo final?","pasos":["1.200 − 3.000 = −1.800 (queda en deuda).","−1.800 + 5.000 = 3.200.","3.200 − 1.700 = 1.500.","El saldo final es $1.500."]},
"ejemplo_incompleto":{"titulo":"el día frío","planteo":"A las 6 h hacía −7 °C y a las 15 h, 9 °C. ¿Cuánto subió la temperatura? Completá los espacios.","pasos":["9 − (−7) = 9 + ___ .","Subió ___ grados."]},
"ejemplo_solo":{"titulo":"el buzo","planteo":"Un buzo está a −18 m. Sube 7 m y después baja 12 m. ¿A qué profundidad queda?"},
"tip":{"titulo":"Final menos inicial","texto":"Para saber cuánto cambió algo, restá el valor del final menos el del principio. El signo te dice si subió o bajó."},
"ojo":["Creer que un resultado negativo es imposible: −$700 es una deuda.","Armar mal el cálculo: de −10 °C a 5 °C se sube 15 grados, no 5."],
"resumen":[{"titulo":"Traducir","texto":"Subir y ganar suman; bajar y gastar restan."},{"titulo":"Saldo negativo","texto":"Es una deuda."},{"titulo":"Cambio","texto":"Final − inicial. Ej.: 9 − (−7) = 16."},{"titulo":"Respuesta","texto":"Siempre con unidad."}],
"glosario":[{"palabra":"Saldo","significado":"Lo que queda en una cuenta."},{"palabra":"Deuda","significado":"Dinero que se debe; saldo negativo."},{"palabra":"Desnivel","significado":"Diferencia de altura."},{"palabra":"Modelizar","significado":"Pasar una situación a un cálculo."}],
"carpeta":["Hacía −3 °C y la temperatura subió 8 grados. ¿Qué temperatura hace ahora?","Un ascensor está en el piso 4 y baja 6 pisos. ¿En qué piso queda?","Tenías $500 y gastaste $1.200 con la tarjeta. ¿Cuál es tu saldo?","Un compañero dice que de −10 °C a 5 °C la temperatura subió 5 grados. ¿Cuántos grados subió?"],
"respuestas_carpeta":[["5"],neg(2),neg(700),["15"]],
"soluciones":{"incompleto":"9 + 7. Subió 16 grados.","solo":"−18 + 7 − 12 = −23. Queda a 23 m de profundidad (−23 m).","carpeta":["5 °C: −3 + 8.","−2: 4 − 6, el segundo subsuelo.","−$700: 500 − 1.200, es una deuda.","15: 5 − (−10) = 15."]}
}
ACT={
"1":[N("Calculá ({a}) + {b}.",{"formula":"b-x"},"Signos distintos: se restan los valores absolutos y gana el signo del mayor.",{"vars":{"x":{"min":2,"max":20},"b":{"min":1,"max":20}},"calculadas":{"a":"0-x"}}),
     MC("¿Qué signo tiene el resultado de (−15) + 9?",["Positivo","Negativo"],"Negativo","15 tiene mayor valor absoluto que 9.")],
"2":[N("Calculá {a} − ({c}).",{"formula":"a+y"},"Restar un negativo es sumar su opuesto.",{"vars":{"a":{"min":1,"max":20},"y":{"min":1,"max":15}},"calculadas":{"c":"0-y"}}),
     VF("Restar un número es lo mismo que sumar su opuesto.","Verdadero","a − b = a + (−b).")],
"3":[N("Calculá 7 − (2 − 9).",{"acepta":[14]},"Se cambian los signos: 7 − 2 + 9 = 14."),
     {"t":"tap_text","p":"Detective del error: tocá el paso que está mal y escribí el resultado correcto.","o":{"modo":"palabras","segmentos":["8 − (3 − 5)","=","8 − 3 − 5","=","0"],"pide_correccion":"Escribí el resultado correcto"},"r":{"tocar":[2],"correccion":["10"]},"e":"Con un − adelante cambian todos los signos: 8 − 3 + 5 = 10."}],
"4":[N("Hacía −6 °C y la temperatura subió 11 grados. ¿Qué temperatura hace?",{"acepta":[5]},"−6 + 11 = 5 °C."),
     N("Tenías $800 y pagaste $2.000. ¿Cuál es tu saldo? Escribilo con signo.",{"acepta":[-1200]},"800 − 2.000 = −1.200: es una deuda.")],
"5":[N("Relámpago. Calculá (−4) + (−5).",{"acepta":[-9]},"Igual signo: 4 + 5 con signo −.",tiempo=25),
     N("Relámpago. Calculá 3 − 8.",{"acepta":[-5]},"3 + (−8) = −5.",tiempo=25),
     N("Relámpago. Calculá (−2) − (−6).",{"acepta":[4]},"(−2) + 6 = 4.",tiempo=30),
     N("Relámpago. Calculá |−15|.",{"acepta":[15]},"Repaso de la misión 11.",tiempo=20)],
}
EXAMEN=[
 [1,N("Calculá (−13) + 8.",{"acepta":[-5]},"13 − 8 = 5, gana el negativo.")],
 [1,N("Calculá (−7) + (−11).",{"acepta":[-18]},"Igual signo: 7 + 11 con signo −.")],
 [1,VF("Para cualquier entero a, a + (−a) = 0.","Verdadero","Un número más su opuesto da 0.")],
 [2,N("Calculá (−9) − 4.",{"acepta":[-13]},"(−9) + (−4) = −13.")],
 [2,N("Calculá 5 − (−12).",{"acepta":[17]},"5 + 12 = 17.")],
 [2,N("La temperatura máxima fue 8 °C y la mínima −5 °C. ¿Cuántos grados de diferencia hubo?",{"acepta":[13]},"8 − (−5) = 13.")],
 [3,N("Calculá −3 + 8 − 10 + 4.",{"acepta":[-1]},"Positivos 12, negativos −13: −1.")],
 [3,N("Calculá 6 − (−2 + 7 − 1).",{"acepta":[2]},"6 + 2 − 7 + 1 = 2.")],
 [3,MC("Al suprimir el paréntesis en 9 − (4 − 3 + 2), queda…",["9 − 4 − 3 + 2","9 − 4 + 3 − 2","9 + 4 − 3 + 2","9 − 4 + 3 + 2"],"9 − 4 + 3 − 2","Con un − adelante cambian todos los signos de adentro.")],
 [4,N("Un submarino está a −150 m y sube 60 m. ¿A qué altura queda? Escribila con signo.",{"acepta":[-90]},"−150 + 60 = −90 m.")],
 [4,N("Una cuenta tiene un saldo de −$400 y se depositan $1.000. ¿Cuál es el nuevo saldo?",{"acepta":[600]},"−400 + 1.000 = 600.")],
 [4,N("Un ascensor sube del subsuelo −3 al piso 8. ¿Cuántos pisos subió?",{"acepta":[11]},"8 − (−3) = 11.")],
 [4,MC("Un saldo de −$300 significa…",["Que hay $300 disponibles","Que se deben $300","Que hay un error en la cuenta","Que no hubo movimientos"],"Que se deben $300","Un saldo negativo es una deuda.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":12,"practica":"Práctica general: suma y resta de enteros","examen_titulo":"Nivel jefe: suma y resta de enteros",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-12.json"),"w"),ensure_ascii=False)
print("ok")
