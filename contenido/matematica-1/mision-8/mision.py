# -*- coding: utf-8 -*-
"""Matemática I · Misión 8 · Fracciones: equivalencia y orden. Genera mision-8.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
SI=["si","sí"]
N1={
"objetivo":"Vas a poder explicar qué es una fracción, representarla con distintos modelos y pasar de fracción impropia a número mixto y al revés.",
"vas_a_ver":["La fracción como parte de un todo","Numerador y denominador","La fracción como cociente","Fracciones propias, impropias y números mixtos","Fracción de una cantidad"],
"secciones":[
 S(1,"Parte de un todo",[
  D("Fracción","Una <b>fracción</b> a/b indica que un entero se divide en <b>b partes iguales</b> (el <b>denominador</b>) y se toman <b>a</b> de esas partes (el <b>numerador</b>)."),
  P("En 3/4 de pizza, la pizza se corta en 4 porciones iguales y se toman 3. Las partes tienen que ser iguales: si no, no es una fracción del entero."),
 ]),
 S(1,"La fracción como cociente",[
  D("Fracción y división","La fracción a/b también es la división <b>a ÷ b</b>. Si repartís 3 pizzas entre 4 personas, a cada una le toca 3/4 de pizza."),
  P("Por eso 6/3 = 6 ÷ 3 = 2 y 4/4 = 1."),
 ]),
 S(2,"Propias, impropias y mixtos",[
  P("Una fracción es <b>propia</b> si el numerador es menor que el denominador (vale menos que 1) e <b>impropia</b> si es mayor o igual (vale 1 o más). Una impropia se puede escribir como <b>número mixto</b>: enteros más una fracción propia."),
  E("Ir y volver","Usamos la división.",["7/4: 7 ÷ 4 = 1, resto 3. Entonces 7/4 = 1 3/4 (un entero y tres cuartos).","2 1/3: 2 enteros son 6 tercios; más 1 tercio: (2 × 3 + 1)/3 = 7/3."]),
 ]),
 S(2,"Fracción de una cantidad",[
  P("Para calcular una fracción de una cantidad, se divide por el denominador y se multiplica por el numerador."),
  E("2/3 de 12 caramelos","Repartimos en 3 grupos y tomamos 2.",["12 ÷ 3 = 4 caramelos por grupo.","2 grupos: 2 × 4 = 8.","2/3 de 12 son 8 caramelos."]),
 ]),
],
"ejemplo_completo":{"titulo":"17/5","planteo":"Escribí 17/5 como número mixto y explicá qué significa.","pasos":["Es impropia: 17 es mayor que 5.","17 ÷ 5 = 3, resto 2.","17/5 = 3 2/5.","Son 3 enteros completos y 2 quintos de otro.","Comprobación: (3 × 5 + 2)/5 = 17/5."]},
"ejemplo_incompleto":{"titulo":"11/4","planteo":"Completá los espacios.","pasos":["11 ÷ 4 = ___ , resto ___ .","11/4 = 2 3/4.","Para volver: (2 × 4 + 3)/4 = ___ /4."]},
"ejemplo_solo":{"titulo":"3 2/5","planteo":"Escribí 3 2/5 como fracción impropia."},
"tip":{"titulo":"Abajo, en cuántas; arriba, cuántas","texto":"El denominador dice en cuántas partes iguales se corta; el numerador, cuántas se toman."},
"ojo":["Dibujar partes que no son iguales: así no se representa una fracción.","Confundir numerador y denominador: en 5/8 el denominador es 8."],
"resumen":[{"titulo":"Fracción","texto":"a/b: b partes iguales, se toman a."},{"titulo":"Cociente","texto":"a/b = a ÷ b. Ej.: 3 pizzas entre 4 → 3/4."},{"titulo":"Propia e impropia","texto":"Menor que 1; 1 o más."},{"titulo":"Número mixto","texto":"7/4 = 1 3/4."},{"titulo":"De una cantidad","texto":"2/3 de 12 = 8."}],
"glosario":[{"palabra":"Numerador","significado":"El número de arriba: cuántas partes se toman."},{"palabra":"Denominador","significado":"El número de abajo: en cuántas partes iguales se divide el entero."},{"palabra":"Fracción impropia","significado":"La que vale 1 o más."},{"palabra":"Número mixto","significado":"Enteros más una fracción propia."}],
"carpeta":["¿Cuántos caramelos son 3/4 de 20 caramelos?","Escribí 9/2 como número mixto. ¿Cuántos enteros tiene?","Escribí 2 1/6 como fracción impropia. ¿Cuál es el numerador?","Un compañero dice que en 5/8 el denominador es 5. ¿Cuál es el denominador?"],
"respuestas_carpeta":[["15"],["4"],["13"],["8"]],
"soluciones":{"incompleto":"11 ÷ 4 = 2, resto 3. Para volver: 11/4.","solo":"(3 × 5 + 2)/5 = 17/5.","carpeta":["15: 20 ÷ 4 = 5 y 3 × 5 = 15.","4: 9 ÷ 2 = 4, resto 1; 9/2 = 4 1/2.","13: (2 × 6 + 1)/6 = 13/6.","8: el denominador es el de abajo, en cuántas partes se divide el entero."]}
}
N2={
"objetivo":"Vas a poder encontrar fracciones equivalentes, simplificar hasta la fracción irreducible usando el MCD y comprobar equivalencias con productos cruzados.",
"vas_a_ver":["Qué son las fracciones equivalentes","Amplificar y simplificar","La fracción irreducible con el MCD","Comprobar con productos cruzados"],
"secciones":[
 S(1,"Fracciones equivalentes",[
  D("Fracciones equivalentes","Dos fracciones son <b>equivalentes</b> si representan la <b>misma cantidad</b>, aunque se escriban distinto: 1/2 = 2/4 = 3/6."),
  P("Media pizza es lo mismo que 2 porciones de una pizza cortada en 4, o 3 de una cortada en 6."),
 ]),
 S(1,"Amplificar y simplificar",[
  D("Amplificar y simplificar","<b>Amplificar</b> es multiplicar numerador y denominador por el mismo número. <b>Simplificar</b> es dividirlos por el mismo número. En los dos casos se obtiene una fracción equivalente."),
  T("Desde 2/3",["Operación","Resultado"],[["Amplificar por 4","8/12"],["Simplificar 8/12 por 4","2/3"]],"Hay que hacer lo mismo arriba y abajo, y siempre multiplicando o dividiendo."),
 ]),
 S(2,"Irreducible con el MCD",[
  P("Una fracción es <b>irreducible</b> si ya no se puede simplificar: el MCD del numerador y el denominador es 1. Para llegar de una vez, se divide por el MCD."),
  E("Simplificar 18/24","Usamos el MCD.",["MCD(18, 24) = 6.","18 ÷ 6 = 3 y 24 ÷ 6 = 4.","18/24 = 3/4, que es irreducible."]),
 ]),
 S(2,"Productos cruzados",[
  P("a/b y c/d son equivalentes si <b>a × d = b × c</b>. Por ejemplo, 3/4 y 9/12: 3 × 12 = 36 y 4 × 9 = 36. Son equivalentes."),
 ]),
],
"ejemplo_completo":{"titulo":"36/48","planteo":"Simplificá 36/48 hasta la irreducible y comprobá.","pasos":["MCD(36, 48) = 12.","36 ÷ 12 = 3 y 48 ÷ 12 = 4.","36/48 = 3/4.","Comprobación cruzada: 36 × 4 = 144 y 48 × 3 = 144."]},
"ejemplo_incompleto":{"titulo":"amplificar y simplificar","planteo":"Completá los espacios.","pasos":["2/5 amplificada por 3 = ___ /15.","Para 20/30, el MCD es ___ .","20/30 = 2/3."]},
"ejemplo_solo":{"titulo":"45/60","planteo":"Escribí 45/60 como fracción irreducible."},
"tip":{"titulo":"Con el MCD, de una","texto":"Si dividís por el MCD llegás directo a la irreducible, sin simplificar varias veces."},
"ojo":["Sumar el mismo número arriba y abajo: 1/2 y 2/3 no son equivalentes. Solo se multiplica o divide.","Parar antes de tiempo: 12/18 = 6/9 todavía se simplifica a 2/3."],
"resumen":[{"titulo":"Equivalentes","texto":"Misma cantidad. Ej.: 1/2 = 2/4."},{"titulo":"Amplificar","texto":"Multiplicar arriba y abajo por lo mismo."},{"titulo":"Simplificar","texto":"Dividir arriba y abajo por lo mismo."},{"titulo":"Irreducible","texto":"Dividir por el MCD. Ej.: 18/24 = 3/4."},{"titulo":"Cruzados","texto":"a × d = b × c."}],
"glosario":[{"palabra":"Equivalente","significado":"Que vale lo mismo."},{"palabra":"Amplificar","significado":"Multiplicar numerador y denominador por el mismo número."},{"palabra":"Simplificar","significado":"Dividir numerador y denominador por el mismo número."},{"palabra":"Irreducible","significado":"Que ya no se puede simplificar."}],
"carpeta":["Completá 3/7 = __/21. ¿Qué numerador va?","Escribí 24/36 como fracción irreducible.","¿Son equivalentes 4/6 y 10/15? Respondé sí o no.","Un compañero sumó 1 arriba y abajo a 3/4 para buscar una equivalente. ¿Cuál es la fracción equivalente a 3/4 con denominador 8?"],
"respuestas_carpeta":[["9"],["2/3"],SI,["6/8"]],
"soluciones":{"incompleto":"6/15. MCD 10.","solo":"MCD(45, 60) = 15. 45/60 = 3/4.","carpeta":["9: se multiplicó por 3 abajo, entonces 3 × 3 = 9.","2/3: MCD(24, 36) = 12.","Sí: 4 × 15 = 60 y 6 × 10 = 60.","6/8: se amplifica por 2. Sumar no da equivalentes."]}
}
N3={
"objetivo":"Vas a poder ubicar fracciones, propias e impropias, en la recta numérica y encontrar fracciones entre otras dos.",
"vas_a_ver":["La recta numérica y la unidad","Ubicar fracciones propias","Ubicar fracciones impropias","Fracciones entre dos fracciones","Subdividir intervalos"],
"secciones":[
 S(1,"La recta y la unidad",[
  D("Ubicar una fracción","Se marca el 0 y el 1 (la <b>unidad</b>). Para ubicar a/b, se divide cada unidad en <b>b partes iguales</b> y se cuentan <b>a partes</b> desde el 0."),
  P("Para 3/4: dividís el tramo de 0 a 1 en 4 partes iguales y contás 3. Si dividís mal la unidad, todas las fracciones quedan mal ubicadas."),
 ]),
 S(1,"Fracciones impropias",[
  D("Impropias en la recta","Una fracción impropia queda <b>después del 1</b>. Conviene pasarla a número mixto: 5/4 = 1 1/4 está un cuarto después del 1."),
  P("Ejemplo: 7/3 = 2 1/3 está entre 2 y 3, a un tercio del 2."),
 ]),
 S(2,"Fracciones entre fracciones",[
  P("Entre dos fracciones <b>siempre hay otras</b>. Para encontrarlas, se amplifican las dos para tener más partes y aparecen fracciones en el medio."),
  E("Entre 1/4 y 2/4","Amplificamos por 2.",["1/4 = 2/8 y 2/4 = 4/8.","Entre 2/8 y 4/8 está 3/8.","3/8 está entre 1/4 y 2/4."]),
 ]),
 S(2,"Subdividir con denominador común",[
  E("Entre 1/3 y 1/2","Buscamos un denominador común y subdividimos.",["Con sextos: 1/3 = 2/6 y 1/2 = 3/6. No hay sextos en el medio.","Amplificamos por 2: 4/12 y 6/12.","5/12 está entre 1/3 y 1/2."]),
 ]),
],
"ejemplo_completo":{"titulo":"2/3 y 5/6","planteo":"Ubicá 2/3 y 5/6 en la misma recta numérica.","pasos":["Los denominadores son 3 y 6: conviene dividir la unidad en 6 partes.","2/3 = 4/6.","Contamos 4 sextos desde 0 para 2/3 y 5 sextos para 5/6.","5/6 queda a la derecha de 2/3, un sexto más adelante."]},
"ejemplo_incompleto":{"titulo":"entre 2/5 y 3/5","planteo":"Encontrá una fracción entre 2/5 y 3/5. Completá los espacios.","pasos":["Amplificamos por 2: 2/5 = 4/10 y 3/5 = ___ .","Entre 4/10 y 6/10 está ___ ."]},
"ejemplo_solo":{"titulo":"entre 1/3 y 1/2","planteo":"Encontrá una fracción que esté entre 1/3 y 1/2."},
"tip":{"titulo":"Elegí bien la división","texto":"Si vas a ubicar varias fracciones, dividí la unidad según un denominador común: todas caben en la misma división."},
"ojo":["Ubicar una impropia antes del 1: 5/3 está entre 1 y 2.","Creer que entre dos fracciones no hay otras: siempre se puede amplificar y encontrar más."],
"resumen":[{"titulo":"Ubicar","texto":"Dividir la unidad en b partes y contar a."},{"titulo":"Impropias","texto":"Después del 1. Ej.: 7/3 entre 2 y 3."},{"titulo":"Entre dos","texto":"Siempre hay otras. Ej.: entre 1/4 y 2/4 está 3/8."},{"titulo":"Común","texto":"Un denominador común ubica todo en la misma recta."}],
"glosario":[{"palabra":"Recta numérica","significado":"Línea donde cada punto representa un número."},{"palabra":"Unidad","significado":"El tramo entre 0 y 1."},{"palabra":"Intervalo","significado":"El tramo entre dos números."},{"palabra":"Subdividir","significado":"Partir cada parte en partes más chicas."}],
"carpeta":["Si la unidad se divide en 6 partes iguales, ¿cuántas partes hay que contar desde 0 para ubicar 7/6?","¿Entre qué dos números enteros está 11/4? Escribí el menor.","Escribí una fracción con denominador 10 que esté entre 2/5 y 3/5.","Un compañero ubicó 5/3 entre 0 y 1. ¿Entre qué dos enteros está en realidad? Escribí el mayor."],
"respuestas_carpeta":[["7"],["2"],["5/10"],["2"]],
"soluciones":{"incompleto":"3/5 = 6/10. Entre ellas está 5/10.","solo":"Con doceavos: 1/3 = 4/12 y 1/2 = 6/12. Entre ellas está 5/12.","carpeta":["7: se cuentan 7 sextos, uno más que la unidad.","2: 11/4 = 2 3/4, está entre 2 y 3.","5/10: 2/5 = 4/10 y 3/5 = 6/10.","2: 5/3 = 1 2/3, está entre 1 y 2."]}
}
N4={
"objetivo":"Vas a poder comparar y ordenar fracciones eligiendo el método más conveniente: mismo denominador, mismo numerador, denominador común o referentes.",
"vas_a_ver":["Comparar con el mismo denominador","Comparar con el mismo numerador","Comparar con denominador común","Comparar con referentes: 1/2 y 1","Ordenar varias fracciones"],
"secciones":[
 S(1,"Mismo denominador o mismo numerador",[
  D("Casos fáciles","Con el <b>mismo denominador</b>, es mayor la de <b>mayor numerador</b>: 5/8 > 3/8. Con el <b>mismo numerador</b>, es mayor la de <b>menor denominador</b>: 3/4 > 3/5, porque los cuartos son más grandes que los quintos."),
 ]),
 S(1,"Denominador común",[
  D("Comparar con denominador común","Si no comparten nada, se pasan a fracciones equivalentes con el <b>mismo denominador</b> y se comparan los numeradores."),
  E("2/3 y 3/5","Usamos quinceavos.",["2/3 = 10/15 y 3/5 = 9/15.","10 > 9, entonces 2/3 > 3/5."]),
 ]),
 S(2,"Referentes: 1/2 y 1",[
  P("A veces alcanza con comparar con 1/2 o con 1. Una fracción es mayor que 1/2 si el numerador es más de la mitad del denominador: 5/8 > 1/2 (5 > 4) y 3/7 < 1/2. Y es mayor que 1 si es impropia: 7/6 > 1 > 9/10."),
 ]),
 S(2,"Ordenar varias",[
  E("Ordenar 1/2, 3/4, 2/3 y 5/12","Denominador común 12.",["1/2 = 6/12; 3/4 = 9/12; 2/3 = 8/12; 5/12.","Ordenamos los numeradores: 5, 6, 8, 9.","5/12 < 1/2 < 2/3 < 3/4."]),
 ]),
],
"ejemplo_completo":{"titulo":"3/4, 5/6 y 2/3","planteo":"Ordená de menor a mayor: 3/4, 5/6 y 2/3.","pasos":["Denominador común: 12.","3/4 = 9/12; 5/6 = 10/12; 2/3 = 8/12.","Numeradores en orden: 8, 9, 10.","2/3 < 3/4 < 5/6."]},
"ejemplo_incompleto":{"titulo":"4/9 y 5/12","planteo":"Compará 4/9 y 5/12. Completá los espacios.","pasos":["Denominador común: 36.","4/9 = ___ /36.","5/12 = ___ /36.","La mayor es ___ ."]},
"ejemplo_solo":{"titulo":"1/2, 3/8 y 5/6","planteo":"Ordená de menor a mayor: 1/2, 3/8 y 5/6."},
"tip":{"titulo":"Elegí el método","texto":"Antes de buscar denominador común, fijate si comparten numerador o denominador, o si alcanza con compararlas con 1/2."},
"ojo":["Mirar solo los numeradores: 3/4 no es menor que 4/5 por tener 3; hay que comparar bien (15/20 < 16/20).","Mirar solo los denominadores: 2/5 no es mayor que 3/4 porque 5 > 4."],
"resumen":[{"titulo":"Mismo denominador","texto":"Mayor numerador, mayor fracción."},{"titulo":"Mismo numerador","texto":"Menor denominador, mayor fracción."},{"titulo":"Denominador común","texto":"Se igualan y se comparan numeradores."},{"titulo":"Referentes","texto":"Comparar con 1/2 o con 1."}],
"glosario":[{"palabra":"Comparar","significado":"Decidir cuál es mayor."},{"palabra":"Denominador común","significado":"Mismo denominador para varias fracciones."},{"palabra":"Referente","significado":"Número conocido con el que se compara, como 1/2 o 1."}],
"carpeta":["¿Cuál es mayor: 5/7 o 5/9?","¿Cuál es mayor: 3/4 o 4/5?","¿Cuál de estas fracciones es menor que 1/2: 4/7, 3/8 o 5/9?","Un compañero dice que 2/5 es mayor que 3/4 porque 5 es mayor que 4. Escribí la mayor de las dos."],
"respuestas_carpeta":[["5/7"],["4/5"],["3/8"],["3/4"]],
"soluciones":{"incompleto":"16/36 y 15/36. La mayor es 4/9.","solo":"Con 24: 12/24, 9/24 y 20/24. 3/8 < 1/2 < 5/6.","carpeta":["5/7: mismo numerador, menor denominador.","4/5: 3/4 = 15/20 y 4/5 = 16/20.","3/8: 3 es menos que la mitad de 8.","3/4: 2/5 es menor que 1/2 y 3/4 es mayor."]}
}
ACT={
"1":[N("¿Cuántos caramelos son 2/3 de {n} caramelos?",{"formula":"2*k"},"Se divide por 3 y se multiplica por 2.",{"vars":{"k":{"min":3,"max":15}},"calculadas":{"n":"3*k"}}),
     MC("¿Qué tipo de fracción es 7/4?",["Propia","Impropia"],"Impropia","El numerador es mayor que el denominador: vale más que 1.")],
"2":[{"t":"fill_blank","p":"4/5 = ___/20","o":[],"r":{"huecos":[["16"]]},"e":"Se amplificó por 4: 4 × 4 = 16."},
     MC("¿Cuál es la fracción irreducible de 18/24?",["9/12","6/8","3/4","2/3"],"3/4","Se divide por el MCD, que es 6.")],
"3":[MC("¿Entre qué dos números enteros está 9/4?",["0 y 1","1 y 2","2 y 3","3 y 4"],"2 y 3","9/4 = 2 1/4."),
     VF("Entre 1/4 y 2/4 no hay ninguna fracción.","Falso","Por ejemplo, 3/8 está entre 2/8 y 4/8.")],
"4":[MC("¿Cuál es mayor?",["3/8","3/5"],"3/5","Mismo numerador: los quintos son más grandes que los octavos."),
     {"t":"ordering","p":"Ordená de menor a mayor.","o":["3/4","1/3","5/6","1/2"],"r":{"orden":["1/3","1/2","3/4","5/6"]},"e":"Con 12: 4/12, 6/12, 9/12 y 10/12."}],
"5":[VF("Relámpago. 2/4 y 3/6 son equivalentes.","Verdadero","Las dos valen 1/2.",tiempo=20),
     N("Relámpago. ¿Cuántos son 3/4 de 40?",{"acepta":[30]},"40 ÷ 4 = 10 y 3 × 10 = 30.",tiempo=30),
     MC("Relámpago. ¿Cuál es mayor?",["5/8","1/2"],"5/8","1/2 = 4/8.",tiempo=20),
     N("Relámpago. ¿Cuál es el MCM de 4 y 6?",{"acepta":[12]},"Repaso de la misión 7.",tiempo=30)],
}
EXAMEN=[
 [1,N("¿Cuántos son 3/5 de 35?",{"acepta":[21]},"35 ÷ 5 = 7 y 3 × 7 = 21.")],
 [1,MC("¿Cómo se escribe 13/4 como número mixto?",["3 1/4","4 1/3","3 3/4","1 3/4"],"3 1/4","13 ÷ 4 = 3, resto 1.")],
 [1,{"t":"matching","p":"Uní cada palabra con su significado.","o":{"izquierda":["Numerador","Denominador","Fracción propia","Fracción impropia"],"derecha":["Cuántas partes se toman","En cuántas partes iguales se divide el entero","Vale menos que 1","Vale 1 o más"]},"r":{"pares":{"Numerador":"Cuántas partes se toman","Denominador":"En cuántas partes iguales se divide el entero","Fracción propia":"Vale menos que 1","Fracción impropia":"Vale 1 o más"}},"e":"El denominador divide; el numerador cuenta."}],
 [2,{"t":"fill_blank","p":"2/7 = 6/___","o":[],"r":{"huecos":[["21"]]},"e":"Se amplificó por 3: 7 × 3 = 21."}],
 [2,MC("¿Cuál de estas fracciones NO es equivalente a 2/3?",["4/6","6/9","8/12","5/6"],"5/6","Las demás se obtienen amplificando 2/3.")],
 [2,VF("Para simplificar 30/45 de una vez, se dividen numerador y denominador por 15.","Verdadero","MCD(30, 45) = 15. Queda 2/3.")],
 [3,N("Si la unidad de la recta se divide en 8 partes iguales, ¿cuántas partes se cuentan desde 0 para ubicar 11/8?",{"acepta":[11]},"Se cuentan 11 octavos: un entero y 3 octavos.")],
 [3,MC("¿Qué fracción está entre 1/3 y 2/3?",["1/6","1/2","5/6","3/2"],"1/2","Con sextos: 2/6 < 3/6 < 4/6.")],
 [3,VF("7/5 se ubica entre 0 y 1 en la recta numérica.","Falso","7/5 = 1 2/5: está entre 1 y 2.")],
 [4,MC("¿Cuál es mayor?",["7/12","2/3"],"2/3","2/3 = 8/12.")],
 [4,MC("¿Cuál de estas fracciones es mayor que 1?",["5/6","6/6","7/6","1/6"],"7/6","Es impropia: el numerador supera al denominador.")],
 [4,{"t":"ordering","p":"Ordená de menor a mayor.","o":["5/8","1/4","7/8","1/2"],"r":{"orden":["1/4","1/2","5/8","7/8"]},"e":"Con 8: 2/8, 4/8, 5/8 y 7/8."}],
 [4,MC("Para comparar 3/4 y 4/5, un compañero miró solo los numeradores. ¿Cuál es la mayor?",["3/4","4/5","Son iguales"],"4/5","3/4 = 15/20 y 4/5 = 16/20.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":8,"practica":"Práctica general: fracciones, equivalencia y orden","examen_titulo":"Nivel jefe: fracciones, equivalencia y orden",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-8.json"),"w"),ensure_ascii=False)
print("ok")
