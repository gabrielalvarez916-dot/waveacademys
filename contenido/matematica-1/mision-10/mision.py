# -*- coding: utf-8 -*-
"""Matemática I · Misión 10 · Expresiones decimales y racionales positivos. Genera mision-10.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
dec=lambda *s:[x for v in s for x in (v, v.replace(",", "."))]  # acepta coma o punto decimal
N1={
"objetivo":"Vas a poder pasar una fracción a número decimal y un decimal a fracción, y comparar números decimales.",
"vas_a_ver":["De fracción a decimal: dividir","Fracciones decimales","De decimal a fracción","Comparar decimales"],
"secciones":[
 S(1,"De fracción a decimal",[
  D("Dividir","Como a/b = a ÷ b, para pasar una fracción a decimal se <b>divide el numerador por el denominador</b>."),
  P("Ejemplos: 3/4 = 3 ÷ 4 = 0,75. 1/8 = 1 ÷ 8 = 0,125. Ojo: 3/4 no es 3,4."),
 ]),
 S(1,"Fracciones decimales",[
  D("Fracción decimal","Es una fracción con denominador <b>10, 100, 1.000…</b> Cada lugar después de la coma es un décimo, un centésimo, un milésimo."),
  T("Decimal y fracción decimal",["Decimal","Se lee","Fracción decimal","Irreducible"],[["0,7","siete décimos","7/10","7/10"],["0,25","veinticinco centésimos","25/100","1/4"],["0,125","ciento veinticinco milésimos","125/1.000","1/8"]]),
 ]),
 S(2,"De decimal a fracción",[
  P("Se escribe el número sin coma arriba y, abajo, un 1 seguido de tantos ceros como cifras decimales. Después se simplifica. Los ceros después de la coma cuentan: 0,06 = 6/100 = 3/50, no 6/10."),
 ]),
 S(2,"Comparar decimales",[
  P("Se comparan primero los enteros y después las cifras decimales de a una, de izquierda a derecha. Conviene <b>completar con ceros</b> para que tengan la misma cantidad de decimales."),
  E("Comparar","Completamos con ceros.",["0,5 y 0,25: 0,50 > 0,25. Tener más cifras no lo hace más grande.","2,3 y 2,28: 2,30 > 2,28."]),
 ]),
],
"ejemplo_completo":{"titulo":"7/8","planteo":"Pasá 7/8 a decimal y comprobá volviendo a fracción.","pasos":["7 ÷ 8 = 0,875.","0,875 tiene tres decimales: 875/1.000.","MCD(875, 1.000) = 125.","875/1.000 = 7/8."]},
"ejemplo_incompleto":{"titulo":"3/5","planteo":"Completá los espacios.","pasos":["3/5 = 3 ÷ 5 = ___ .","0,6 = 6/ ___ .","6/10 simplificado = 3/5."]},
"ejemplo_solo":{"titulo":"ordenar decimales","planteo":"Ordená de menor a mayor: 0,4; 0,35; 0,402."},
"tip":{"titulo":"Completá con ceros","texto":"Para comparar, escribí todos con la misma cantidad de decimales: 0,4 = 0,400. Así se compara como si fueran naturales."},
"ojo":["Creer que más cifras es más grande: 0,25 es menor que 0,5.","Perder ceros: 0,06 son seis centésimos, 6/100."],
"resumen":[{"titulo":"Fracción a decimal","texto":"Se divide. Ej.: 3/4 = 0,75."},{"titulo":"Fracción decimal","texto":"Denominador 10, 100, 1.000."},{"titulo":"Decimal a fracción","texto":"0,25 = 25/100 = 1/4."},{"titulo":"Comparar","texto":"Completar con ceros. Ej.: 0,50 > 0,25."}],
"glosario":[{"palabra":"Décimo","significado":"Una de las 10 partes iguales del entero: 0,1."},{"palabra":"Centésimo","significado":"Una de las 100 partes iguales: 0,01."},{"palabra":"Milésimo","significado":"Una de las 1.000 partes iguales: 0,001."},{"palabra":"Fracción decimal","significado":"Fracción con denominador 10, 100, 1.000…"}],
"carpeta":["Escribí 1/4 como número decimal.","Escribí 0,8 como fracción irreducible.","¿Cuál es mayor: 0,7 o 0,65?","Un compañero escribió que 3/4 = 3,4. ¿Cuál es el decimal correcto?"],
"respuestas_carpeta":[dec("0,25"),["4/5"],dec("0,7"),dec("0,75")],
"soluciones":{"incompleto":"0,6. 6/10.","solo":"0,350 < 0,400 < 0,402. Orden: 0,35; 0,4; 0,402.","carpeta":["0,25: 1 ÷ 4.","4/5: 8/10 simplificado por 2.","0,7: 0,70 > 0,65.","0,75: 3 ÷ 4. La raya de fracción no es una coma."]}
}
N2={
"objetivo":"Vas a poder distinguir decimales exactos y periódicos, saber de antemano cuál va a dar una fracción y pasar un periódico simple a fracción.",
"vas_a_ver":["Decimales exactos","Decimales periódicos puros y mixtos","Cómo saber si una fracción da exacto o periódico","La fracción de un periódico puro"],
"secciones":[
 S(1,"Exactos y periódicos",[
  D("Decimal exacto y periódico","Un decimal es <b>exacto</b> si la división termina: 3/4 = 0,75. Es <b>periódico</b> si una cifra o grupo de cifras se repite sin fin: 1/3 = 0,333… El grupo que se repite es el <b>período</b>."),
  P("Con la calculadora, 1 ÷ 3 muestra 0,3333333: la pantalla se corta, pero el 3 sigue para siempre. Por eso 0,333 (con tres cifras) <b>no es</b> lo mismo que 0,333…"),
 ]),
 S(1,"Puros y mixtos",[
  D("Puro y mixto","Un periódico es <b>puro</b> si el período empieza justo después de la coma: 0,2727… (período 27). Es <b>mixto</b> si antes hay cifras que no se repiten, el <b>anteperíodo</b>: 0,1666… (anteperíodo 1, período 6)."),
 ]),
 S(2,"¿Exacto o periódico?",[
  P("Se mira el denominador de la fracción <b>irreducible</b>: si al descomponerlo solo tiene factores <b>2 y 5</b>, el decimal es exacto; si tiene otro primo, es periódico."),
  E("Dos casos","Descomponemos el denominador.",["3/40: 40 = 2³ × 5. Exacto: 0,075.","5/12: 12 = 2² × 3. Tiene un 3: periódico, 0,41666…"]),
 ]),
 S(2,"De periódico puro a fracción",[
  P("Para un periódico puro: arriba va el período y abajo tantos <b>9</b> como cifras tiene el período. Después se simplifica."),
  E("Fracción generatriz","Tres ejemplos.",["0,333… = 3/9 = 1/3.","0,2727… = 27/99 = 3/11.","1,555… = 1 + 5/9 = 14/9."]),
 ]),
],
"ejemplo_completo":{"titulo":"0,4545…","planteo":"Escribí 0,4545… como fracción irreducible y comprobá.","pasos":["Es periódico puro, período 45 (dos cifras).","0,4545… = 45/99.","MCD(45, 99) = 9: 45/99 = 5/11.","Comprobación: 5 ÷ 11 = 0,4545…"]},
"ejemplo_incompleto":{"titulo":"ida y vuelta","planteo":"Completá los espacios.","pasos":["0,777… = 7/ ___ .","2/9 = 0, ___ (se repite)."]},
"ejemplo_solo":{"titulo":"7/20","planteo":"¿7/20 da un decimal exacto o periódico? Justificá con el denominador y calculalo."},
"tip":{"titulo":"Mirá el denominador","texto":"Simplificá primero y descomponé el denominador: solo 2 y 5 → exacto; cualquier otro primo → periódico."},
"ojo":["Redondear un periódico y creerlo exacto: 0,33 no es 1/3.","Confundir período con anteperíodo: en 0,1666… el período es 6."],
"resumen":[{"titulo":"Exacto","texto":"La división termina. Ej.: 3/4 = 0,75."},{"titulo":"Periódico","texto":"Se repite sin fin. Ej.: 1/3 = 0,333…"},{"titulo":"Puro y mixto","texto":"0,2727… puro; 0,1666… mixto."},{"titulo":"Criterio","texto":"Denominador con solo 2 y 5: exacto."},{"titulo":"Generatriz","texto":"0,2727… = 27/99 = 3/11."}],
"glosario":[{"palabra":"Período","significado":"Cifra o grupo de cifras que se repite sin fin."},{"palabra":"Anteperíodo","significado":"Cifras después de la coma que no se repiten."},{"palabra":"Fracción generatriz","significado":"La fracción que da ese decimal."}],
"carpeta":["¿Qué fracción irreducible es 0,666…?","¿Cuál es el período de 0,1818…?","7/25 da un decimal exacto. ¿Cuál es?","Un compañero dice que 1/3 = 0,33. ¿Cuánto da 0,33 × 3?"],
"respuestas_carpeta":[["2/3"],["18"],dec("0,28"),dec("0,99")],
"soluciones":{"incompleto":"7/9. 0,222…","solo":"20 = 2² × 5: solo 2 y 5, es exacto. 7 ÷ 20 = 0,35.","carpeta":["2/3: 6/9 simplificado.","18: se repite el grupo 18.","0,28: 7 ÷ 25 (25 = 5²).","0,99: no da 1, así que 0,33 no es exactamente 1/3."]}
}
N3={
"objetivo":"Vas a poder sumar, restar, multiplicar y dividir números decimales ubicando bien la coma, y controlar el resultado con una estimación.",
"vas_a_ver":["Suma y resta: alinear las comas","Multiplicación: contar las cifras decimales","División: correr la coma","Estimar para ubicar la coma"],
"secciones":[
 S(1,"Suma y resta",[
  D("Alinear las comas","Para sumar o restar decimales se encolumnan <b>coma con coma</b> (décimos con décimos, centésimos con centésimos). Si falta alguna cifra, se completa con ceros."),
  P("Ejemplos: 3,5 + 12,48 = 3,50 + 12,48 = 15,98. 10 − 4,37 = 10,00 − 4,37 = 5,63."),
 ]),
 S(1,"Multiplicación",[
  D("Contar decimales","Se multiplica como si no hubiera coma y, al resultado, se le ponen <b>tantas cifras decimales como tienen entre los dos factores</b>."),
  P("2,4 × 0,3: 24 × 3 = 72; hay 1 + 1 = 2 decimales: 0,72. Y 1,25 × 4 = 5,00 = 5."),
 ]),
 S(2,"División",[
  P("Si el divisor tiene coma, se <b>corre la coma</b> el mismo número de lugares en el dividendo y en el divisor, hasta que el divisor quede entero (es amplificar). Después se divide."),
  E("Dividir decimales","Dos casos.",["7,5 ÷ 0,25: corremos dos lugares: 750 ÷ 25 = 30.","4,8 ÷ 6: el divisor ya es entero: 0,8."]),
 ]),
 S(2,"Estimar para controlar",[
  P("Antes de calcular, redondeá: 3,9 × 2,1 es casi 4 × 2 = 8. Si te da 81,9 o 0,819, la coma quedó mal; el resultado correcto es 8,19."),
 ]),
],
"ejemplo_completo":{"titulo":"12,6 × 0,15","planteo":"Calculá 12,6 × 0,15 y controlá con una estimación.","pasos":["Sin comas: 126 × 15 = 1.890.","Decimales: 1 + 2 = 3. Queda 1,890 = 1,89.","Estimación: 12 × 0,15 es un poco menos que 12 × 0,2 = 2,4, y bastante más que 1.","1,89 es razonable."]},
"ejemplo_incompleto":{"titulo":"6,3 ÷ 0,7","planteo":"Completá los espacios.","pasos":["Corremos la coma un lugar en los dos: 63 ÷ ___ .","63 ÷ 7 = ___ ."]},
"ejemplo_solo":{"titulo":"15 − 7,48","planteo":"Calculá 15 − 7,48."},
"tip":{"titulo":"La coma, al final","texto":"En la multiplicación, hacé la cuenta sin comas y recién al final ubicá la coma contando decimales."},
"ojo":["Alinear a la derecha: al sumar 3,5 + 12,48 hay que alinear las comas, no las últimas cifras.","Contar mal los decimales: 2,5 × 1,2 = 3,00, no 30."],
"resumen":[{"titulo":"Sumar y restar","texto":"Coma debajo de coma. Ej.: 3,5 + 12,48 = 15,98."},{"titulo":"Multiplicar","texto":"Se suman las cifras decimales. Ej.: 2,4 × 0,3 = 0,72."},{"titulo":"Dividir","texto":"Correr la coma. Ej.: 7,5 ÷ 0,25 = 750 ÷ 25 = 30."},{"titulo":"Estimar","texto":"3,9 × 2,1 ≈ 8."}],
"glosario":[{"palabra":"Cifra decimal","significado":"Cada cifra que está después de la coma."},{"palabra":"Encolumnar","significado":"Escribir los números uno debajo del otro, alineados."},{"palabra":"Correr la coma","significado":"Moverla lugares a la derecha o a la izquierda."}],
"carpeta":["Calculá 4,25 + 3,8.","Calculá 0,6 × 0,4.","Calculá 9 ÷ 0,3.","Un compañero hizo 2,5 × 1,2 y le dio 30. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[dec("8,05"),dec("0,24"),["30"],["3"]+dec("3,0","3,00")],
"soluciones":{"incompleto":"63 ÷ 7. Resultado: 9.","solo":"15,00 − 7,48 = 7,52.","carpeta":["8,05: 4,25 + 3,80.","0,24: 6 × 4 = 24, dos decimales.","30: 90 ÷ 3.","3: 25 × 12 = 300, con dos decimales: 3,00."]}
}
N4={
"objetivo":"Vas a poder resolver problemas de compras, recetas y medidas con fracciones y decimales, elegir la forma más cómoda de escribir los números y redondear cuando corresponde.",
"vas_a_ver":["Fracción o decimal: cuál conviene","Problemas de dinero y medidas","Redondear en contexto","Estimar y controlar"],
"secciones":[
 S(1,"Fracción o decimal",[
  D("Elegir la representación","Un mismo número se puede escribir como fracción o como decimal. Conviene el <b>decimal</b> para dinero y medidas; la <b>fracción</b> cuando el decimal es periódico (1/3 es exacto; 0,33 no)."),
  T("Mismo número, dos formas",["Fracción","Decimal","Conviene"],[["1/4 kg","0,25 kg","cualquiera"],["1/3 de la torta","0,333…","fracción"],["$15/2","$7,50","decimal"]]),
 ]),
 S(1,"Dinero y medidas",[
  D("Precio por cantidad","Si algo cuesta un precio por kilo o por metro, el total es <b>precio × cantidad</b>, aunque la cantidad sea un decimal o una fracción."),
  E("En el almacén","Dos compras.",["2,5 kg de pan a $1.840 el kg: 1.840 × 2,5 = 4.600.","3/4 kg de queso a $9.200 el kg: 9.200 × 3/4 = 6.900."]),
 ]),
 S(2,"Redondear en contexto",[
  P("El dinero se redondea a <b>centavos</b> (dos decimales), y siempre <b>al final</b> del cálculo. Si redondeás en el medio, el error se acumula. Repartir $1.000 entre 3 da 333,333…; cada uno recibe $333,33 y queda 1 centavo."),
 ]),
 S(2,"Recetas y control",[
  E("La receta","Una receta para 4 personas lleva 1 1/2 tazas de leche. ¿Cuánta para 6?",["6 personas es 1,5 veces 4.","1,5 × 1,5 = 2,25 tazas, o sea 2 1/4.","Control: para 8 serían 3 tazas, así que 2 1/4 para 6 es razonable."]),
 ]),
],
"ejemplo_completo":{"titulo":"la compra","planteo":"Comprás 1,5 kg de tomates a $1.200 el kg y 3/4 kg de queso a $8.400 el kg. Pagás con $10.000. ¿Cuánto vuelto recibís?","pasos":["Tomates: 1.200 × 1,5 = 1.800.","Queso: 8.400 × 3/4 = 8.400 ÷ 4 × 3 = 6.300.","Total: 1.800 + 6.300 = 8.100.","Vuelto: 10.000 − 8.100 = 1.900.","Control: unos 2.000 de tomates y 6.000 de queso, cerca de 8.000. Es razonable."]},
"ejemplo_incompleto":{"titulo":"el reparto","planteo":"Tres amigos se reparten $2.500 en partes iguales. Completá los espacios.","pasos":["2.500 ÷ 3 = ___ (sigue con 3 periódico).","Redondeado a centavos, cada uno recibe $833,33.","3 × 833,33 = ___ : falta 1 centavo por el redondeo."]},
"ejemplo_solo":{"titulo":"la tela","planteo":"Una tela cuesta $3.600 el metro. ¿Cuánto cuestan 2,75 m?"},
"tip":{"titulo":"Redondeá al final","texto":"Hacé todas las cuentas con los números completos y redondeá solo el resultado."},
"ojo":["Redondear antes de terminar: el error se acumula en cada paso.","Aceptar un resultado absurdo: 2,4 kg a $1.500 no pueden costar $360; la estimación da unos $3.000."],
"resumen":[{"titulo":"Representación","texto":"Decimal para dinero; fracción si el decimal es periódico."},{"titulo":"Precio","texto":"Precio × cantidad. Ej.: 2,5 kg × $1.840 = $4.600."},{"titulo":"Redondeo","texto":"A centavos y al final."},{"titulo":"Control","texto":"Estimar con números redondos."}],
"glosario":[{"palabra":"Centavo","significado":"Una centésima parte de un peso: $0,01."},{"palabra":"Redondear","significado":"Cambiar un número por uno cercano más simple."},{"palabra":"Representación","significado":"Forma de escribir un número."}],
"carpeta":["¿Cuánto cuesta medio kilo (0,5 kg) de queso a $8.000 el kg?","Una receta para 4 personas lleva 0,75 kg de harina. ¿Cuántos kg hacen falta para 8 personas?","Repartí $100 entre 3 personas en partes iguales y redondeá a centavos. ¿Cuánto recibe cada una?","Un compañero dice que 2,4 kg a $1.500 el kg cuestan $360. ¿Cuánto cuestan en realidad?"],
"respuestas_carpeta":[["4000"],dec("1,5"),dec("33,33"),["3600"]],
"soluciones":{"incompleto":"833,333… 2.499,99.","solo":"3.600 × 2,75 = 9.900. Cuestan $9.900.","carpeta":["$4.000: la mitad de 8.000.","1,5 kg: el doble de 0,75.","$33,33: 100 ÷ 3 = 33,333…","$3.600: 1.500 × 2,4. Corrió mal la coma."]}
}
ACT={
"1":[MC("¿Cuál es el decimal de 3/8?",["0,38","0,375","3,8","0,83"],"0,375","3 ÷ 8 = 0,375."),
     MC("¿Cuál es mayor?",["0,5","0,25"],"0,5","0,50 > 0,25: tener más cifras no lo hace mayor.")],
"2":[MC("¿Qué fracción es 0,333… (el 3 se repite sin fin)?",["3/10","1/3","33/100","3/100"],"1/3","Período 3, una cifra: 3/9 = 1/3."),
     {"t":"classify","p":"Clasificá cada fracción según el decimal que da.","o":{"elementos":["1/4","1/3","3/20","5/6","7/8","2/9"],"categorias":["Decimal exacto","Decimal periódico"]},"r":{"categorias":{"1/4":"Decimal exacto","1/3":"Decimal periódico","3/20":"Decimal exacto","5/6":"Decimal periódico","7/8":"Decimal exacto","2/9":"Decimal periódico"}},"e":"Denominadores con solo 2 y 5 (4, 20, 8) dan exacto; con 3 (3, 6, 9), periódico."}],
"3":[N("Calculá {a},5 + {b},25.",{"formula":"a+b+0.75"},"Se alinean las comas: los décimos y centésimos se suman aparte.",{"vars":{"a":{"min":1,"max":20},"b":{"min":1,"max":20}}}),
     N("Calculá 3,6 ÷ 0,4.",{"acepta":[9]},"Corremos la coma: 36 ÷ 4 = 9.")],
"4":[N("¿Cuánto cuestan 1,5 kg de manzanas a $2.200 el kg?",{"acepta":[3300]},"2.200 × 1,5 = 3.300."),
     MC("Para repartir 1 kg de dulce en 3 frascos iguales, ¿qué forma de escribir lo que va en cada frasco es exacta?",["0,33 kg","0,333 kg","1/3 kg"],"1/3 kg","El decimal es periódico: 0,33 y 0,333 son aproximaciones.")],
"5":[N("Relámpago. Escribí 1/2 como número decimal.",{"acepta":[0.5]},"1 ÷ 2 = 0,5.",tiempo=20),
     N("Relámpago. Calculá 0,2 × 0,3.",{"acepta":[0.06]},"2 × 3 = 6, con dos decimales: 0,06.",tiempo=30),
     VF("Relámpago. 0,50 y 0,5 son el mismo número.","Verdadero","Agregar ceros al final de los decimales no cambia el número.",tiempo=20),
     MC("Relámpago. 1/2 + 1/3 =",["2/5","5/6","1/6","2/6"],"5/6","3/6 + 2/6 (repaso de la misión 9).",tiempo=30)],
}
EXAMEN=[
 [1,N("Escribí 7/20 como número decimal.",{"acepta":[0.35]},"7 ÷ 20 = 0,35.")],
 [1,MC("¿Cuál es la fracción irreducible de 0,25?",["25/10","1/4","2/5","1/25"],"1/4","25/100 simplificado por 25.")],
 [1,{"t":"ordering","p":"Ordená de menor a mayor.","o":["0,4","0,35","0,402","0,04"],"r":{"orden":["0,04","0,35","0,4","0,402"]},"e":"Con tres decimales: 0,040; 0,350; 0,400; 0,402."}],
 [2,MC("¿Cuál de estas fracciones da un decimal periódico?",["3/8","7/20","5/12","9/25"],"5/12","12 = 2² × 3 tiene un factor 3.")],
 [2,MC("¿Qué fracción es 0,2727… (el 27 se repite sin fin)?",["27/100","3/11","27/10","2/7"],"3/11","27/99 simplificado por 9.")],
 [2,VF("0,333 es lo mismo que 0,333… con el 3 repitiéndose sin fin.","Falso","0,333 termina; el periódico sigue para siempre.")],
 [3,N("Calculá 10 − 4,37.",{"acepta":[5.63]},"10,00 − 4,37 = 5,63.")],
 [3,N("Calculá 1,25 × 0,8.",{"acepta":[1]},"125 × 8 = 1.000, con tres decimales: 1,000.")],
 [3,N("Calculá 7,5 ÷ 0,25.",{"acepta":[30]},"750 ÷ 25 = 30.")],
 [4,N("Una tela cuesta $3.600 el metro. ¿Cuánto cuestan 2,75 m?",{"acepta":[9900]},"3.600 × 2,75 = 9.900.")],
 [4,N("Tres amigos compran una pizza de $9.450 y pagan en partes iguales. ¿Cuánto paga cada uno?",{"acepta":[3150]},"9.450 ÷ 3 = 3.150.")],
 [4,VF("En un cálculo largo conviene redondear en cada paso.","Falso","Se redondea al final, para que el error no se acumule.")],
 [4,MC("¿Cuál es la mejor estimación de 4,9 × 3,1?",["1,5","15","150","0,15"],"15","5 × 3 = 15.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":10,"practica":"Práctica general: decimales y racionales positivos","examen_titulo":"Nivel jefe: decimales y racionales positivos",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-10.json"),"w"),ensure_ascii=False)
print("ok")
