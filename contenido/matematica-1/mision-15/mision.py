# -*- coding: utf-8 -*-
"""Matemática I · Misión 15 · Lenguaje algebraico y patrones. Genera mision-15.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
N1={
"objetivo":"Vas a poder pasar enunciados del lenguaje común al lenguaje algebraico, usando letras para representar números que pueden cambiar.",
"vas_a_ver":["Variables y constantes","Traducir enunciados a expresiones","Leer expresiones algebraicas","Usar letras para generalizar"],
"secciones":[
 S(1,"Variables y constantes",[
  D("Variable y constante","Una <b>variable</b> es una letra que representa un número que puede cambiar. Una <b>constante</b> es un número fijo. En 3n + 5, n es la variable y 3 y 5 son constantes."),
  P("Se puede usar cualquier letra: n, a, t, m… Entre un número y una letra no se escribe el signo ×: 3n significa 3 × n."),
 ]),
 S(1,"Traducir",[
  D("Del lenguaje común al algebraico","Cada frase se pasa a una operación con la letra."),
  T("Traducciones",["Lenguaje común","Lenguaje algebraico"],[["El doble de un número","2n"],["Un número aumentado en 5","n + 5"],["El triple de un número menos 1","3n − 1"],["La mitad de un número","n/2"],["El consecutivo de un número","n + 1"],["El cuadrado de un número","n²"]],"Ojo: \"el doble\" es multiplicar por 2 (2n), no sumar 2 (n + 2)."),
 ]),
 S(2,"Leer expresiones",[
  P("También se lee al revés: 4t + 1 es \"el cuádruple de un número más uno\"; (a + b)/2 es \"la mitad de la suma de dos números\"."),
 ]),
 S(2,"Generalizar",[
  P("Las letras sirven para decir algo que vale para <b>todos</b> los números. \"La suma de un número y su consecutivo\" es n + (n + 1), para cualquier n: con n = 4 da 4 + 5 = 9; con n = 10 da 10 + 11 = 21."),
 ]),
],
"ejemplo_completo":{"titulo":"las edades","planteo":"Ana tiene a años. Su hermano tiene 3 años más que ella y su papá tiene el triple de la edad de Ana. Escribí las edades con letras y calculalas si Ana tiene 12 años.","pasos":["Hermano: a + 3.","Papá: 3a (3 × a).","Con a = 12: hermano 12 + 3 = 15 años.","Papá: 3 × 12 = 36 años."]},
"ejemplo_incompleto":{"titulo":"traducir con m","planteo":"Completá los espacios.","pasos":["El doble de m: ___ .","m disminuido en 4: ___ .","El cuadrado de m: m²."]},
"ejemplo_solo":{"titulo":"cuadrado y bicicletas","planteo":"Escribí con letras: el perímetro de un cuadrado de lado l y la cantidad de ruedas de b bicicletas."},
"tip":{"titulo":"Probá con un número","texto":"Si dudás de una traducción, reemplazá la letra por un número: si n = 5, el doble tiene que dar 10. Con 2n da 10; con n + 2 da 7."},
"ojo":["Traducir \"el doble\" como n + 2: es 2n.","Creer que la letra es una etiqueta fija: n puede valer cualquier número."],
"resumen":[{"titulo":"Variable","texto":"Letra que puede tomar distintos valores."},{"titulo":"Doble y triple","texto":"2n y 3n."},{"titulo":"Aumentado en","texto":"n + 5."},{"titulo":"Consecutivo","texto":"n + 1."},{"titulo":"Generalizar","texto":"Una fórmula sirve para todos los números."}],
"glosario":[{"palabra":"Variable","significado":"Letra que representa un número que puede cambiar."},{"palabra":"Constante","significado":"Número que no cambia."},{"palabra":"Expresión algebraica","significado":"Cálculo con números y letras."},{"palabra":"Consecutivo","significado":"El número que sigue: n + 1."}],
"carpeta":["Si n vale 7, ¿cuánto vale el doble de n más 3?","Escribí con lenguaje algebraico \"el triple de un número t\".","El número k y su consecutivo: si k = 12, ¿cuánto vale el consecutivo?","Un compañero escribió el doble de n como n + 2. Si n = 10, ¿cuánto vale realmente el doble de n?"],
"respuestas_carpeta":[["17"],["3t","3×t","3*t","3·t"],["13"],["20"]],
"soluciones":{"incompleto":"2m. m − 4.","solo":"Perímetro: 4l. Ruedas: 2b.","carpeta":["17: 2 × 7 + 3.","3t: 3 × t.","13: k + 1.","20: 2 × 10. Con n + 2 daría 12."]}
}
N2={
"objetivo":"Vas a poder descubrir la regla de un patrón, escribir su fórmula y usarla para calcular términos lejanos.",
"vas_a_ver":["Patrones numéricos y con figuras","Regla recursiva: cómo se pasa de un término al siguiente","Fórmula explícita: el término según su posición","Predecir términos lejanos","Posición y valor"],
"secciones":[
 S(1,"Patrones",[
  D("Patrón","Un <b>patrón</b> es una secuencia que sigue una regla. Cada número es un <b>término</b> y tiene una <b>posición</b> (1.º, 2.º, 3.º…)."),
  T("Cuadrados con fósforos en fila",["Cuadrados (posición n)","1","2","3","4"],[["Fósforos","4","7","10","13"]],"Cada cuadrado nuevo agrega 3 fósforos, porque comparte un lado con el anterior."),
 ]),
 S(1,"Recursiva y explícita",[
  D("Dos formas de la regla","La regla <b>recursiva</b> dice cómo pasar de un término al siguiente: \"se suman 3\". La fórmula <b>explícita</b> da el término directamente según su posición n: fósforos = 3n + 1."),
  P("Comprobación de la fórmula: n = 1 da 4; n = 2 da 7; n = 3 da 10. Funciona con todos los de la tabla."),
 ]),
 S(2,"Términos lejanos",[
  P("Con la recursiva, para saber el término 50 habría que calcular los 49 anteriores. Con la explícita, se reemplaza: 3 × 50 + 1 = 151 fósforos."),
 ]),
 S(2,"Posición y valor",[
  P("No hay que confundir la posición con el valor: en 4, 7, 10, 13, el término en la posición 3 vale 10. La n de la fórmula es la posición."),
 ]),
],
"ejemplo_completo":{"titulo":"5, 9, 13, 17, …","planteo":"Encontrá la fórmula de la secuencia 5, 9, 13, 17, … y calculá el término 20.","pasos":["De un término al siguiente se suman 4: la fórmula empieza con 4n.","Con n = 1, 4n da 4, pero el término es 5: hay que sumar 1.","Fórmula: 4n + 1. Comprobación: n = 2 da 9; n = 3 da 13.","Término 20: 4 × 20 + 1 = 81."]},
"ejemplo_incompleto":{"titulo":"2, 4, 6, 8, …","planteo":"Completá los espacios.","pasos":["El término en la posición n es ___ .","El término 30 es ___ ."]},
"ejemplo_solo":{"titulo":"las baldosas","planteo":"La figura 1 tiene 3 baldosas, la figura 2 tiene 5 y la figura 3 tiene 7. Escribí la fórmula y calculá cuántas baldosas tiene la figura 10."},
"tip":{"titulo":"Lo que se suma va con la n","texto":"Si de un término al siguiente se suma siempre lo mismo, ese número multiplica a la n. Después ajustás con el primer término."},
"ojo":["Dar la regla solo con palabras: hace falta la fórmula para llegar lejos.","Armar una fórmula que sirve para un solo término: comprobala con varios."],
"resumen":[{"titulo":"Patrón","texto":"Secuencia con una regla."},{"titulo":"Recursiva","texto":"Del anterior al siguiente: +3."},{"titulo":"Explícita","texto":"Según la posición: 3n + 1."},{"titulo":"Lejanos","texto":"Término 50: 3 × 50 + 1 = 151."}],
"glosario":[{"palabra":"Término","significado":"Cada número de una secuencia."},{"palabra":"Posición","significado":"El lugar que ocupa el término: 1.º, 2.º…"},{"palabra":"Término general","significado":"Fórmula que da cualquier término según su posición."}],
"carpeta":["¿Cuál es el término 6 de la secuencia 3, 7, 11, 15, …?","En la secuencia de término general 5n − 2, ¿cuál es el término 10?","¿Qué número sigue en 1, 4, 9, 16, …?","En 2, 5, 8, 11, … la fórmula es 3n − 1. Un compañero dijo que el término 10 es 14. ¿Cuál es el término 10?"],
"respuestas_carpeta":[["23"],["48"],["25"],["29"]],
"soluciones":{"incompleto":"2n. 60.","solo":"Se suman 2: 2n + 1. Figura 10: 2 × 10 + 1 = 21 baldosas.","carpeta":["23: fórmula 4n − 1; 4 × 6 − 1.","48: 5 × 10 − 2.","25: son los cuadrados 1², 2², 3², 4²; sigue 5².","29: 3 × 10 − 1. Confundió el término siguiente con el término 10."]}
}
N3={
"objetivo":"Vas a poder calcular el valor numérico de una expresión reemplazando las letras, incluso con números negativos, y usar fórmulas.",
"vas_a_ver":["Qué es el valor numérico","Reemplazar respetando la jerarquía","Reemplazar con negativos","Fórmulas de geometría y movimiento","Tablas de valores"],
"secciones":[
 S(1,"Valor numérico",[
  D("Valor numérico","El <b>valor numérico</b> de una expresión es lo que da al <b>reemplazar las letras por números</b> y hacer las cuentas respetando la jerarquía."),
  P("3a + 2 con a = 5: 3 × 5 + 2 = 17. 2x² con x = 3: primero la potencia, 2 × 9 = 18 (no 6² = 36)."),
 ]),
 S(1,"Con negativos",[
  D("Paréntesis al reemplazar","Si la letra vale un número negativo, al reemplazar se pone <b>entre paréntesis</b>."),
  P("Con a = −4: 3a + 2 = 3 × (−4) + 2 = −12 + 2 = −10. Y a² = (−4)² = 16."),
 ]),
 S(2,"Fórmulas",[
  T("Fórmulas conocidas",["Qué calcula","Fórmula"],[["Perímetro de un rectángulo","P = 2b + 2h"],["Área de un rectángulo","A = b × h"],["Distancia recorrida","d = v × t"]],"b es la base, h la altura, v la velocidad y t el tiempo."),
 ]),
 S(2,"Tablas de valores",[
  T("Valores de y = 2x + 1",["x","0","1","2","3"],[["y","1","3","5","7"]],"Para cada x se calcula el valor numérico."),
 ]),
],
"ejemplo_completo":{"titulo":"el viaje","planteo":"Usá la fórmula d = v × t para calcular cuántos kilómetros recorre un auto a 80 km/h durante 2,5 horas.","pasos":["v = 80 y t = 2,5.","d = 80 × 2,5.","80 × 2,5 = 200.","Recorre 200 km."]},
"ejemplo_incompleto":{"titulo":"5 − 2x con x = −3","planteo":"Completá los espacios.","pasos":["5 − 2 × (___).","2 × (−3) = −6, entonces 5 − (−6).","5 + 6 = ___ ."]},
"ejemplo_solo":{"titulo":"x² − 3x","planteo":"Calculá el valor numérico de x² − 3x para x = 4."},
"tip":{"titulo":"Paréntesis siempre","texto":"Al reemplazar, poné cada número entre paréntesis. Así no se pierden signos y la potencia afecta al número completo."},
"ojo":["Sustituir sin respetar la jerarquía: 2x² con x = 3 es 18, no 36.","Olvidar paréntesis con un negativo: con a = −4, a² es (−4)² = 16."],
"resumen":[{"titulo":"Valor numérico","texto":"Reemplazar y calcular. Ej.: 3a + 2 con a = 5 → 17."},{"titulo":"Negativos","texto":"Entre paréntesis. Ej.: a = −4 → 3 × (−4) + 2."},{"titulo":"Fórmulas","texto":"A = b × h; d = v × t."},{"titulo":"Tablas","texto":"Un valor para cada x."}],
"glosario":[{"palabra":"Valor numérico","significado":"Resultado de reemplazar las letras por números."},{"palabra":"Sustituir","significado":"Reemplazar la letra por un número."},{"palabra":"Fórmula","significado":"Expresión con letras que sirve para calcular algo."}],
"carpeta":["Calculá 4m − 1 para m = 6.","Calculá a² + 1 para a = −3.","Calculá el área de un rectángulo con la fórmula A = b × h, si b = 12 y h = 5.","Un compañero calculó 2x² con x = 3 haciendo 6² = 36. ¿Cuál es el valor correcto?"],
"respuestas_carpeta":[["23"],["10"],["60"],["18"]],
"soluciones":{"incompleto":"−3. 11.","solo":"4² − 3 × 4 = 16 − 12 = 4.","carpeta":["23: 4 × 6 − 1.","10: (−3)² + 1 = 9 + 1.","60: 12 × 5.","18: la potencia va primero: 2 × 9."]}
}
N4={
"objetivo":"Vas a poder reconocer expresiones equivalentes, comprobarlas con valores y simplificar expresiones sencillas usando la distributiva.",
"vas_a_ver":["Qué son las expresiones equivalentes","Por qué un solo valor no alcanza","Términos semejantes","Simplificar con la distributiva"],
"secciones":[
 S(1,"Expresiones equivalentes",[
  D("Equivalentes","Dos expresiones son <b>equivalentes</b> si dan el <b>mismo valor para cualquier número</b> que reemplace a la letra."),
  T("2(x + 3) y 2x + 6",["x","2(x + 3)","2x + 6"],[["1","8","8"],["5","16","16"],["10","26","26"]],"Son equivalentes por la distributiva: 2(x + 3) = 2x + 2 × 3."),
 ]),
 S(1,"Un valor no alcanza",[
  P("x + x y x · x dan lo mismo con x = 2 (las dos dan 4), pero con x = 3 dan 6 y 9. No son equivalentes. <b>Un solo valor no alcanza</b> para asegurar que son equivalentes; para mostrar que <b>no</b> lo son, sí alcanza un valor que dé distinto."),
 ]),
 S(2,"Términos semejantes",[
  P("Son términos con la <b>misma parte de letras</b>. Se pueden sumar: 3a + 5a = 8a. Pero 3a + 5 no se puede juntar: son términos distintos."),
 ]),
 S(2,"Simplificar",[
  E("Dos simplificaciones","Distributiva y términos semejantes.",["4n + 2n − n = 5n.","2(a + 4) + a = 2a + 8 + a = 3a + 8."]),
 ]),
],
"ejemplo_completo":{"titulo":"3(n − 2) + n","planteo":"¿Son equivalentes 3(n − 2) + n y 4n − 6?","pasos":["Distributiva: 3(n − 2) = 3n − 6.","3n − 6 + n = 4n − 6.","Son equivalentes.","Comprobación con n = 5: 3 × 3 + 5 = 14 y 4 × 5 − 6 = 14."]},
"ejemplo_incompleto":{"titulo":"5(x + 2)","planteo":"Completá los espacios.","pasos":["5(x + 2) = 5x + ___ .","Con x = 1: 5 × 3 = 15 y 5 × 1 + 10 = ___ ."]},
"ejemplo_solo":{"titulo":"2(a + 3) + 4a","planteo":"Simplificá 2(a + 3) + 4a."},
"tip":{"titulo":"Distribuí a todos","texto":"El número de afuera multiplica a cada término del paréntesis, no solo al primero."},
"ojo":["Probar un solo valor: puede coincidir de casualidad.","Distribuir solo el primer término: 4(y + 5) es 4y + 20, no 4y + 5."],
"resumen":[{"titulo":"Equivalentes","texto":"Mismo valor para todo número."},{"titulo":"Un valor no alcanza","texto":"x + x y x · x coinciden con x = 2."},{"titulo":"Semejantes","texto":"3a + 5a = 8a; 3a + 5 no se junta."},{"titulo":"Simplificar","texto":"2(a + 4) + a = 3a + 8."}],
"glosario":[{"palabra":"Equivalente","significado":"Que da siempre el mismo valor."},{"palabra":"Términos semejantes","significado":"Términos con la misma parte de letras."},{"palabra":"Simplificar","significado":"Escribir más corto sin cambiar el valor."}],
"carpeta":["Simplificá 7b − 2b y calculá su valor para b = 4.","Si 3(x + 2) = 3x + c para cualquier x, ¿cuánto vale c?","¿Cuánto da x · x para x = 3?","Un compañero escribió 4(y + 5) = 4y + 5. Para y = 1, ¿cuánto vale 4(y + 5)?"],
"respuestas_carpeta":[["20"],["6"],["9"],["24"]],
"soluciones":{"incompleto":"10. 15.","solo":"2a + 6 + 4a = 6a + 6.","carpeta":["20: 7b − 2b = 5b; 5 × 4.","6: 3 × 2.","9: 3 × 3. Con x + x daría 6: no son equivalentes.","24: 4 × 6. Distribuyendo bien: 4y + 20."]}
}
ACT={
"1":[MC("¿Qué expresión es \"el doble de un número n\"?",["n + 2","2n","n²","n/2"],"2n","El doble es multiplicar por 2."),
     {"t":"matching","p":"Uní cada frase con su expresión.","o":{"izquierda":["El triple de a","a aumentado en 3","El cuadrado de a","La mitad de a"],"derecha":["3a","a + 3","a²","a/2"]},"r":{"pares":{"El triple de a":"3a","a aumentado en 3":"a + 3","El cuadrado de a":"a²","La mitad de a":"a/2"}},"e":"Triple: × 3. Aumentado: + 3. Cuadrado: potencia 2. Mitad: ÷ 2."}],
"2":[N("En la secuencia de término general 3n + 2, ¿cuál es el término {n}?",{"formula":"3*n+2"},"Se reemplaza n por la posición.",{"vars":{"n":{"min":5,"max":40}}}),
     MC("En la secuencia 4, 7, 10, 13, …, ¿cuál es la fórmula del término general?",["n + 3","3n + 1","3n","4n"],"3n + 1","Se suma 3 cada vez; con n = 1, 3 + 1 = 4.")],
"3":[N("Calculá 2a + {b} para a = {a}.",{"formula":"2*a+b"},"Se reemplaza y se respeta la jerarquía.",{"vars":{"a":{"min":2,"max":12},"b":{"min":1,"max":9}}}),
     N("Calculá 3x² para x = 2.",{"acepta":[12]},"Primero la potencia: 3 × 4 = 12.")],
"4":[MC("¿Qué expresión es equivalente a 2(m + 4)?",["2m + 4","2m + 8","m + 8","2m + 6"],"2m + 8","El 2 multiplica a los dos términos."),
     VF("Si dos expresiones dan el mismo resultado para un valor, siempre son equivalentes.","Falso","x + x y x · x coinciden con x = 2, pero no con x = 3.")],
"5":[N("Relámpago. Si n = 5, ¿cuánto vale 3n?",{"acepta":[15]},"3 × 5.",tiempo=20),
     MC("Relámpago. ¿Qué número sigue: 2, 4, 6, 8, …?",["9","10","12","16"],"10","Se suma 2.",tiempo=20),
     MC("Relámpago. 3a + 2a =",["5a","6a","5a²","5"],"5a","Términos semejantes.",tiempo=20),
     N("Relámpago. ¿Cuánto es el 10% de 250?",{"acepta":[25]},"Repaso de la misión 14.",tiempo=25)],
}
EXAMEN=[
 [1,MC("¿Qué expresión es \"un número aumentado en 7\"?",["7n","n + 7","n − 7","n/7"],"n + 7","Aumentado en es sumar.")],
 [1,MC("En la expresión 5k − 3, ¿qué es k?",["Una constante","Una variable","Un exponente","Un resultado"],"Una variable","Puede tomar distintos valores.")],
 [1,N("Si p = 9, ¿cuánto vale el triple de p menos 4?",{"acepta":[23]},"3 × 9 − 4.")],
 [2,N("¿Cuál es el término 8 de la secuencia 6, 11, 16, 21, …?",{"acepta":[41]},"Fórmula 5n + 1: 5 × 8 + 1.")],
 [2,MC("En una secuencia con fórmula 2n + 5, ¿qué representa n?",["El valor del término","La posición del término","Lo que se suma cada vez","El primer término"],"La posición del término","n es el lugar que ocupa.")],
 [2,N("Con fósforos se arman cuadrados en fila: para n cuadrados se usan 3n + 1 fósforos. ¿Cuántos fósforos hacen falta para 20 cuadrados?",{"acepta":[61]},"3 × 20 + 1.")],
 [3,N("Calculá 5 − 2x para x = −4.",{"acepta":[13]},"5 − 2 × (−4) = 5 + 8.")],
 [3,N("Calculá x² − 2x para x = 5.",{"acepta":[15]},"25 − 10.")],
 [3,N("Con la fórmula d = v × t, ¿cuántos km recorre un auto a 90 km/h durante 3 horas?",{"acepta":[270]},"90 × 3.")],
 [4,MC("¿Qué expresión es equivalente a 3(a − 2)?",["3a − 2","3a − 6","a − 6","3a + 6"],"3a − 6","El 3 multiplica a los dos términos.")],
 [4,MC("¿Cuál es la forma simplificada de 6n − 2n + n?",["5n","3n","4n","9n"],"5n","6 − 2 + 1 = 5.")],
 [4,N("Calculá 2(y + 3) + y para y = 4.",{"acepta":[18]},"2 × 7 + 4.")],
 [4,VF("3a + 5 se puede simplificar a 8a.","Falso","No son términos semejantes.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":15,"practica":"Práctica general: lenguaje algebraico y patrones","examen_titulo":"Nivel jefe: lenguaje algebraico y patrones",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-15.json"),"w"),ensure_ascii=False)
print("ok")
