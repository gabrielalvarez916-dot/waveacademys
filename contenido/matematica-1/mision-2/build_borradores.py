# -*- coding: utf-8 -*-
"""Matemática I · Misión 2 · Operaciones con naturales. Arma los 4 borradores (nivel-N.json)."""
import json, base64, os
AQUI = os.path.dirname(os.path.abspath(__file__))
D=lambda t,x:{"tipo":"definicion","titulo":t,"texto":x}
P=lambda x:{"tipo":"parrafo","texto":x}
IM=lambda t,x:{"tipo":"importante","titulo":t,"texto":x}
T=lambda t,c,f,x=None:{"tipo":"tabla","titulo":t,"columnas":c,"filas":f,"iguales":True,**({"texto":x} if x else {})}
E=lambda t,x,i:{"tipo":"ejemplo","titulo":t,"texto":x,"items":i}
S=lambda e,t,b:{"etapa":e,"titulo":t,"bloques":b}
OUT={}

# ---------------- NIVEL 1: suma y resta ----------------
OUT[1]={
"objetivo":"Vas a poder usar las propiedades de la suma y estrategias de cálculo mental para sumar y restar rápido y sin errores.",
"vas_a_ver":["La propiedad conmutativa de la suma","La propiedad asociativa de la suma","La resta como operación inversa de la suma","Cálculo mental por descomposición","Cálculo mental por compensación"],
"secciones":[
 S(1,"Las propiedades de la suma",[
  D("Propiedad conmutativa","En una suma, <b>el orden de los sumandos no cambia el resultado</b>: a + b = b + a."),
  P("Ejemplo: 27 + 48 = 75 y 48 + 27 = 75. Sirve para empezar por el número más cómodo."),
  D("Propiedad asociativa","Cuando sumás tres o más números, <b>podés agruparlos como quieras</b> y el resultado es el mismo: (a + b) + c = a + (b + c)."),
  P("Ejemplo: 36 + 25 + 75 = 36 + (25 + 75) = 36 + 100 = 136. Agrupar los que juntos dan un número redondo hace la cuenta más fácil."),
  IM("La resta no cumple estas propiedades","9 − 4 = 5, pero 4 − 9 no da 5 (con números naturales ni siquiera se puede resolver). En la resta el orden importa."),
 ]),
 S(1,"Suma y resta van juntas",[
  D("Operación inversa","La resta es la <b>operación inversa</b> de la suma: deshace lo que hizo la suma. Si a + b = c, entonces c − b = a y c − a = b."),
  T("Una suma y sus dos restas",["Suma","Primera resta","Segunda resta"],[["45 + 30 = 75","75 − 30 = 45","75 − 45 = 30"]],"Con una sola suma ya sabés el resultado de dos restas. También sirve para comprobar: si restás y después sumás, volvés al número del principio."),
  P("Por eso una resta se puede pensar de dos formas: como una <b>diferencia</b> (cuánto más tiene uno que otro) o como un <b>complemento</b> (cuánto le falta a un número para llegar a otro). Para 1.000 − 637 contás hacia arriba: 637 + 3 = 640; 640 + 60 = 700; 700 + 300 = 1.000. Faltaron 3 + 60 + 300 = 363."),
 ]),
 S(2,"Cálculo mental por descomposición",[
  P("Descomponer es partir los números en unidades de mil, centenas, decenas y unidades, operar cada parte y juntar. Gracias a la conmutativa y la asociativa, las partes se pueden sumar en cualquier orden."),
  E("Sumar y restar descomponiendo","Resolvemos dos cuentas.",["346 + 238 = (300 + 200) + (40 + 30) + (6 + 8) = 500 + 70 + 14 = 584.","485 − 132: restamos por partes. 485 − 100 = 385; 385 − 30 = 355; 355 − 2 = 353."]),
 ]),
 S(2,"Cálculo mental por compensación",[
  P("<b>Compensar</b> es cambiar un número por uno redondo cercano y después corregir lo que cambiaste. En la suma, si sumaste de más, restás lo que te pasaste. En la resta, si restaste de más, lo <b>devolvés sumando</b>."),
  E("Compensar en una suma y en una resta","Usamos 200 en lugar de 198 y 100 en lugar de 99.",["198 + 357: 198 es 200 − 2. 200 + 357 = 557; 557 − 2 = 555.","523 − 99: 99 es 100 − 1. 523 − 100 = 423; restamos 1 de más, así que sumamos 1: 423 + 1 = 424."]),
 ]),
],
"ejemplo_completo":{"titulo":"1.250 − 398 con compensación","planteo":"Calculá 1.250 − 398 con compensación y comprobá el resultado con una suma.","pasos":["398 está cerca de 400: 398 = 400 − 2.","1.250 − 400 = 850.","Restamos 2 de más, así que los devolvemos: 850 + 2 = 852.","Comprobación con la operación inversa: 852 + 398 = 1.250.","Resultado: 1.250 − 398 = 852."]},
"ejemplo_incompleto":{"titulo":"735 − 197","planteo":"Calculá 735 − 197 con compensación. Completá los espacios.","pasos":["197 = 200 − ___ .","735 − 200 = ___ .","Restamos 3 de más: 535 + 3 = ___ .","Comprobación: 538 + 197 = 735."]},
"ejemplo_solo":{"titulo":"2.460 − 999","planteo":"Calculá 2.460 − 999 con compensación y comprobalo con una suma."},
"tip":{"titulo":"Mirá los números antes de calcular","texto":"Si un número está cerca de uno redondo (99, 198, 1.001), compensá. Si hay dos que juntos dan redondo (25 y 75, 36 y 64), asocialos primero."},
"ojo":["Cambiar el orden en una resta: 15 − 8 no es lo mismo que 8 − 15. La conmutativa es solo de la suma.","Olvidar la compensación: en 523 − 99 restás 100 y tenés que sumar 1; si no, te da 423 en lugar de 424."],
"resumen":[{"titulo":"Conmutativa","texto":"El orden de los sumandos no cambia la suma. Ej.: 27 + 48 = 48 + 27."},{"titulo":"Asociativa","texto":"Se agrupa como convenga. Ej.: 36 + (25 + 75) = 136."},{"titulo":"Operación inversa","texto":"Si 45 + 30 = 75, entonces 75 − 30 = 45."},{"titulo":"Descomposición","texto":"Se opera por partes. Ej.: 346 + 238 = 500 + 70 + 14."},{"titulo":"Compensación","texto":"Se redondea y se corrige. Ej.: 523 − 99 = 523 − 100 + 1."}],
"glosario":[{"palabra":"Sumando","significado":"Cada número que se suma."},{"palabra":"Diferencia","significado":"El resultado de una resta."},{"palabra":"Propiedad","significado":"Una regla que se cumple siempre en una operación."},{"palabra":"Operación inversa","significado":"La que deshace lo que hizo otra: la resta deshace la suma."},{"palabra":"Compensar","significado":"Cambiar un número por uno redondo y corregir después."},{"palabra":"Complemento","significado":"Lo que le falta a un número para llegar a otro."}],
"carpeta":["Calculá usando la propiedad asociativa: 47 + 64 + 36.","Calculá con compensación: 645 + 298.","Sabiendo que 358 + 247 = 605, ¿cuánto es 605 − 247?","Un compañero calculó 812 − 99 restando 100 y escribió 712. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["147"],["943"],["358"],["713"]],
"soluciones":{"incompleto":"197 = 200 − 3. 735 − 200 = 535. 535 + 3 = 538.","solo":"999 = 1.000 − 1. 2.460 − 1.000 = 1.460. Restamos 1 de más: 1.460 + 1 = 1.461. Comprobación: 1.461 + 999 = 2.460.","carpeta":["147: 47 + (64 + 36) = 47 + 100 = 147.","943: 298 = 300 − 2. 645 + 300 = 945; 945 − 2 = 943.","358: la resta es la inversa de la suma, así que 605 − 247 = 358.","713: 812 − 100 = 712, pero restó 1 de más; hay que devolverlo: 712 + 1 = 713."]}
}

# ---------------- NIVEL 2: multiplicación y distributiva ----------------
png = base64.b64encode(open(os.path.join(AQUI, "distributiva.png"), "rb").read()).decode()
OUT[2]={
"objetivo":"Vas a poder usar las propiedades de la multiplicación, sobre todo la distributiva, para calcular rápido y para escribir una cuenta de otra forma.",
"vas_a_ver":["La multiplicación como suma repetida y como área","Las propiedades conmutativa y asociativa del producto","La propiedad distributiva respecto de la suma","La distributiva respecto de la resta","Cálculo mental con la distributiva"],
"secciones":[
 S(1,"Qué es multiplicar",[
  D("Multiplicación","Multiplicar es <b>sumar un mismo número varias veces</b>. Los números que se multiplican son los <b>factores</b> y el resultado es el <b>producto</b>."),
  P("Ejemplo: 4 × 6 = 6 + 6 + 6 + 6 = 24. También es el área de un rectángulo: 4 filas de 6 cuadraditos forman 24 cuadraditos."),
  P("Igual que la suma, el producto cumple la <b>conmutativa</b> (4 × 6 = 6 × 4) y la <b>asociativa</b>: 25 × 7 × 4 = (25 × 4) × 7 = 100 × 7 = 700."),
 ]),
 S(1,"La propiedad distributiva",[
  D("Propiedad distributiva","Multiplicar un número por una suma es lo mismo que <b>multiplicarlo por cada sumando y sumar los resultados</b>: a × (b + c) = a × b + a × c."),
  {"tipo":"imagen","imagen_tipo":"diagrama","titulo":"12 × 17 partido en dos rectángulos","texto":"El rectángulo de 12 por 17 se parte en uno de 12 por 10 y otro de 12 por 7: 120 + 84 = 204.","imagen_descripcion":"Rectángulo cuadriculado de 12 filas por 17 columnas, partido por una línea vertical en una parte de 10 columnas (12 × 10 = 120) y otra de 7 columnas (12 × 7 = 84).","imagen_fuente":"Dibujo propio (matplotlib).","png_base64":png},
  P("La figura lo muestra: 12 × 17 = 12 × (10 + 7) = 12 × 10 + 12 × 7 = 120 + 84 = 204. Partir el 17 en 10 + 7 parte el rectángulo en dos, y las dos áreas suman el área total."),
 ]),
 S(2,"Distributiva con la resta",[
  P("La distributiva también vale con una resta: a × (b − c) = a × b − a × c. Multiplicás por cada número y restás."),
  E("Distribuir sobre una resta","Calculamos 6 × (10 − 2) de dos formas.",["Primero la resta: 6 × 8 = 48.","Con distributiva: 6 × 10 − 6 × 2 = 60 − 12 = 48.","Las dos formas dan 48."]),
 ]),
 S(2,"Cálculo mental con la distributiva",[
  P("Para multiplicar mentalmente, partí un factor en un número redondo más (o menos) un número chico, y distribuí."),
  E("Multiplicar mentalmente","Partimos un factor.",["14 × 11 = 14 × (10 + 1) = 140 + 14 = 154.","25 × 19 = 25 × (20 − 1) = 500 − 25 = 475.","8 × 99 = 8 × (100 − 1) = 800 − 8 = 792."]),
 ]),
],
"ejemplo_completo":{"titulo":"24 × 99 con la distributiva","planteo":"Calculá 24 × 99 con la distributiva y comprobá el resultado de otra forma.","pasos":["99 está cerca de 100: 99 = 100 − 1.","24 × 99 = 24 × (100 − 1) = 24 × 100 − 24 × 1.","24 × 100 = 2.400 y 24 × 1 = 24.","2.400 − 24 = 2.376.","Comprobación partiendo el 24: 20 × 99 = 1.980 y 4 × 99 = 396; 1.980 + 396 = 2.376."]},
"ejemplo_incompleto":{"titulo":"13 × 21","planteo":"Calculá 13 × 21 con la distributiva. Completá los espacios.","pasos":["21 = 20 + ___ .","13 × 21 = 13 × 20 + 13 × 1.","13 × 20 = ___ .","260 + 13 = ___ ."]},
"ejemplo_solo":{"titulo":"35 × 98","planteo":"Calculá 35 × 98 partiendo el 98 en un número redondo menos un número chico."},
"tip":{"titulo":"Partí el factor que está cerca de uno redondo","texto":"99 = 100 − 1, 21 = 20 + 1, 48 = 50 − 2. Si dudás, dibujá el rectángulo partido: cada parte es una multiplicación más fácil."},
"ojo":["Distribuir solo sobre un sumando: 2 × (3 + 4) no es 6 + 4; es 2 × 3 + 2 × 4 = 6 + 8 = 14.","Usar la distributiva en un producto: 2 × (3 × 4) no es (2 × 3) × (2 × 4). Ahí va la asociativa: 2 × 3 × 4 = 24."],
"resumen":[{"titulo":"Multiplicación","texto":"Suma repetida. Ej.: 4 × 6 = 6 + 6 + 6 + 6 = 24."},{"titulo":"Conmutativa y asociativa","texto":"Se cambia el orden y se agrupa. Ej.: 25 × 7 × 4 = 100 × 7."},{"titulo":"Distributiva","texto":"a × (b + c) = a × b + a × c. Ej.: 12 × 17 = 120 + 84."},{"titulo":"Con la resta","texto":"a × (b − c) = a × b − a × c. Ej.: 6 × (10 − 2) = 60 − 12."},{"titulo":"Cálculo mental","texto":"Se parte un factor. Ej.: 25 × 19 = 500 − 25 = 475."}],
"glosario":[{"palabra":"Factor","significado":"Cada número que se multiplica."},{"palabra":"Producto","significado":"El resultado de una multiplicación."},{"palabra":"Distribuir","significado":"Repartir la multiplicación entre cada número de una suma o una resta."},{"palabra":"Área","significado":"Cuántos cuadraditos ocupa una figura."},{"palabra":"Factor redondo","significado":"Un número terminado en ceros, fácil de multiplicar."}],
"carpeta":["Calculá con la distributiva: 15 × 12.","Calculá 8 × (10 − 3) aplicando la distributiva.","Completá: 7 × (20 + 6) = 140 + ___ .","Un compañero escribió 5 × (8 + 2) = 40 + 2 = 42. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["180"],["56"],["42"],["50"]],
"soluciones":{"incompleto":"21 = 20 + 1. 13 × 20 = 260. 260 + 13 = 273.","solo":"98 = 100 − 2. 35 × 100 = 3.500 y 35 × 2 = 70. 3.500 − 70 = 3.430.","carpeta":["180: 15 × (10 + 2) = 150 + 30 = 180.","56: 8 × 10 − 8 × 3 = 80 − 24 = 56.","42: 7 × 6 = 42.","50: el 5 multiplica a los dos sumandos: 5 × 8 + 5 × 2 = 40 + 10 = 50."]}
}

# ---------------- NIVEL 3: división ----------------
OUT[3]={
"objetivo":"Vas a poder resolver divisiones con resto, entender qué significa el resto y usar la relación fundamental para comprobar y para hallar datos que faltan.",
"vas_a_ver":["Las partes de la división: dividendo, divisor, cociente y resto","Qué significa el resto y por qué es menor que el divisor","La relación fundamental de la división","Cómo comprobar una división","Problemas con un dato que falta"],
"secciones":[
 S(1,"Las partes de la división",[
  D("División","Dividir es <b>repartir en partes iguales</b> o ver cuántas veces entra un número en otro. El número que se reparte es el <b>dividendo</b>, el que reparte es el <b>divisor</b>, el resultado entero es el <b>cociente</b> y lo que sobra es el <b>resto</b>."),
  T("La división 47 ÷ 5",["Dividendo","Divisor","Cociente","Resto"],[["47","5","9","2"]],"El 5 entra 9 veces en 47 (5 × 9 = 45) y sobran 2. El resto siempre es menor que el divisor: si sobrara 5 o más, entraría una vez más."),
  IM("Dos casos especiales","Si el resto es 0, la división es <b>exacta</b>: 45 ÷ 5 = 9. Y <b>nunca se divide por 0</b>: no hay ningún número que multiplicado por 0 dé 47."),
 ]),
 S(1,"La relación fundamental",[
  D("Relación fundamental de la división","En toda división: <b>dividendo = divisor × cociente + resto</b>, con el resto menor que el divisor."),
  P("En 47 ÷ 5: 5 × 9 + 2 = 45 + 2 = 47. Se vuelve al dividendo. Esta relación une la división con la multiplicación y la suma."),
 ]),
 S(2,"Comprobar una división",[
  P("Para comprobar, aplicás la relación fundamental: multiplicás el divisor por el cociente y sumás el resto. Si te da el dividendo, está bien."),
  E("Dividir y comprobar","Resolvemos 365 ÷ 7 y 824 ÷ 4.",["365 ÷ 7 = 52, resto 1. Comprobación: 7 × 52 = 364; 364 + 1 = 365.","824 ÷ 4: 8 ÷ 4 = 2; el 2 no alcanza para dividir por 4, así que va un 0 en el cociente; 24 ÷ 4 = 6.","824 ÷ 4 = 206, resto 0. Comprobación: 4 × 206 = 824."]),
 ]),
 S(2,"Problemas con un dato que falta",[
  P("Con la relación fundamental podés hallar el dividendo si conocés los otros tres datos. Y en un problema, el resto te dice algo: a veces sobra, a veces obliga a sumar 1."),
  E("Usar la relación y el resto","Dos situaciones.",["Divisor 6, cociente 15 y resto 4: dividendo = 6 × 15 + 4 = 90 + 4 = 94.","50 chicos van de excursión en micros de 12 lugares: 50 ÷ 12 = 4, resto 2. Con 4 micros quedan 2 chicos afuera: hacen falta 5 micros."]),
 ]),
],
"ejemplo_completo":{"titulo":"1.537 ÷ 12","planteo":"Resolvé 1.537 ÷ 12 y comprobá con la relación fundamental.","pasos":["15 ÷ 12 = 1, y 12 × 1 = 12: resto 3.","Bajamos el 3: 33 ÷ 12 = 2, y 12 × 2 = 24: resto 9.","Bajamos el 7: 97 ÷ 12 = 8, y 12 × 8 = 96: resto 1.","Cociente 128 y resto 1 (1 es menor que 12).","Comprobación: 12 × 128 = 1.536; 1.536 + 1 = 1.537."]},
"ejemplo_incompleto":{"titulo":"253 ÷ 8","planteo":"Resolvé 253 ÷ 8. Completá los espacios.","pasos":["25 ÷ 8 = 3, y 8 × 3 = 24: resto ___ .","Bajamos el 3: 13 ÷ 8 = 1, y 8 × 1 = 8: resto ___ .","Cociente 31 y resto 5.","Comprobación: 8 × 31 + 5 = ___ ."]},
"ejemplo_solo":{"titulo":"hallar el dividendo","planteo":"En una división, el divisor es 9, el cociente es 27 y el resto es 5. ¿Cuál es el dividendo?"},
"tip":{"titulo":"Cerrá siempre con la comprobación","texto":"Divisor por cociente, más el resto: tiene que darte el dividendo. Y mirá que el resto sea menor que el divisor."},
"ojo":["Dejar un resto igual o mayor que el divisor: en 47 ÷ 5, un resto de 7 no puede ser; el 5 todavía entra una vez más.","Olvidar el cero del cociente: 824 ÷ 4 es 206, no 26. Comprobá: 4 × 26 = 104."],
"resumen":[{"titulo":"Partes","texto":"Dividendo ÷ divisor = cociente, con un resto. Ej.: 47 ÷ 5 = 9, resto 2."},{"titulo":"Resto","texto":"Lo que sobra; siempre es menor que el divisor."},{"titulo":"Exacta","texto":"Resto 0. Ej.: 45 ÷ 5 = 9."},{"titulo":"Relación fundamental","texto":"Dividendo = divisor × cociente + resto. Ej.: 47 = 5 × 9 + 2."},{"titulo":"Dato que falta","texto":"Divisor 6, cociente 15, resto 4: dividendo 94."}],
"glosario":[{"palabra":"Dividendo","significado":"El número que se reparte."},{"palabra":"Divisor","significado":"El número por el que se divide."},{"palabra":"Cociente","significado":"Cuántas veces entra el divisor en el dividendo."},{"palabra":"Resto","significado":"Lo que sobra al dividir."},{"palabra":"División exacta","significado":"La que tiene resto 0."},{"palabra":"Comprobar","significado":"Revisar con otra cuenta que el resultado está bien."}],
"carpeta":["Calculá 735 ÷ 7.","¿Cuál es el resto de 158 ÷ 6?","En una división, el divisor es 8, el cociente es 14 y el resto es 3. ¿Cuál es el dividendo?","Un compañero resolvió 65 ÷ 7 y escribió cociente 8 y resto 9. ¿Cuál es el cociente correcto?"],
"respuestas_carpeta":[["105"],["2"],["115"],["9"]],
"soluciones":{"incompleto":"Resto 1 (25 − 24). Resto 5 (13 − 8). Comprobación: 8 × 31 + 5 = 248 + 5 = 253.","solo":"Dividendo = 9 × 27 + 5 = 243 + 5 = 248.","carpeta":["105: 7 ÷ 7 = 1; 3 no alcanza para 7, va un 0; 35 ÷ 7 = 5. Comprobación: 7 × 105 = 735.","2: 6 × 26 = 156 y 158 − 156 = 2.","115: 8 × 14 + 3 = 112 + 3 = 115.","9: el resto 9 es mayor que 7, así que el 7 entra una vez más. 7 × 9 = 63 y sobran 2."]}
}

# ---------------- NIVEL 4: estimación y problemas ----------------
OUT[4]={
"objetivo":"Vas a poder estimar resultados, controlar si una respuesta tiene sentido y resolver problemas de varios pasos eligiendo bien cada operación.",
"vas_a_ver":["Cómo redondear un número","Cómo estimar el resultado de una cuenta","Cómo controlar si un resultado es razonable","Cómo elegir la operación según lo que pasa en el problema","Problemas de varios pasos con datos de más"],
"secciones":[
 S(1,"Redondear",[
  D("Redondear","Redondear es <b>reemplazar un número por otro redondo cercano</b>. Mirás la cifra que está a la derecha del lugar al que redondeás: si es 0, 1, 2, 3 o 4, el lugar queda igual; si es 5, 6, 7, 8 o 9, sube 1. Lo que sigue pasa a ser 0."),
  T("Redondear 4.372",["A la","Cifra que mirás","Resultado"],[["decena","2 (queda)","4.370"],["centena","7 (sube)","4.400"],["unidad de mil","3 (queda)","4.000"]],"Según a qué lugar redondees, el número redondo cambia."),
 ]),
 S(1,"Estimar",[
  D("Estimar","Estimar es <b>calcular de forma aproximada</b> con números redondeados. No da el resultado exacto, pero dice más o menos cuánto tiene que dar."),
  P("Ejemplo: 389 + 512 es parecido a 400 + 500 = 900. El resultado exacto es 901, muy cerca de la estimación."),
 ]),
 S(2,"¿Es razonable el resultado?",[
  P("Comparar el resultado exacto con la estimación sirve para detectar errores. Si están muy lejos, algo falló."),
  E("Controlar una cuenta","Un compañero calculó 48 × 21 = 1.808.",["Estimamos: 48 es casi 50 y 21 es casi 20. 50 × 20 = 1.000.","1.808 está muy lejos de 1.000: algo falló.","Calculamos bien: 48 × 21 = 48 × 20 + 48 = 960 + 48 = 1.008. Ahora sí está cerca de 1.000."]),
 ]),
 S(2,"Problemas de varios pasos",[
  P("Para elegir la operación, pensá qué pasa en la situación: si se juntan cantidades, se suma; si se quita o se compara, se resta; si se repite una cantidad, se multiplica; si se reparte, se divide. Algunos problemas traen <b>datos de más</b> que no se usan."),
  E("Las entradas del cine","Una familia compra 3 entradas de $4.500 y paga con $20.000. El cine está a 12 cuadras. ¿Cuánto vuelto recibe?",["Las 12 cuadras son un dato de más: no cambian el vuelto.","Se repite el precio 3 veces: 3 × 4.500 = 13.500.","Se quita lo que pagó del billete: 20.000 − 13.500 = 6.500.","Control: 3 × 5.000 = 15.000, vuelto cerca de 5.000. Recibe $6.500."]),
 ]),
],
"ejemplo_completo":{"titulo":"las pelotas del club","planteo":"Un club quiere comprar 18 pelotas de $7.850 cada una y tiene $150.000. ¿Le alcanza? ¿Cuánto le sobra o le falta?","pasos":["Estimamos: 20 × 8.000 = 160.000. Está cerca de 150.000, así que hay que hacer la cuenta exacta.","Se repite el precio 18 veces: 7.850 × 18 = 7.850 × 10 + 7.850 × 8 = 78.500 + 62.800 = 141.300.","Comparamos con lo que tiene: 150.000 − 141.300 = 8.700.","Control: 141.300 es un poco menos que 160.000 porque al estimar redondeamos los dos números hacia arriba.","Le alcanza y le sobran $8.700."]},
"ejemplo_incompleto":{"titulo":"los viajes del micro","planteo":"Un micro lleva 45 pasajeros por viaje y hace 4 viajes por día durante 6 días. ¿Cuántos pasajeros lleva en total? Completá los espacios.","pasos":["Viajes en total: 4 × 6 = ___ .","Pasajeros: 45 × 24 = ___ .","Estimación: 50 × 20 = ___ . Está cerca: el resultado es razonable."]},
"ejemplo_solo":{"titulo":"la compra de Juana","planteo":"Juana tiene $5.000. Compra 3 cuadernos de $1.180 y una birome de $650. ¿Cuánto le queda?"},
"tip":{"titulo":"Estimá antes de calcular","texto":"Así ya sabés qué resultado esperar y detectás un error en el momento, no después."},
"ojo":["Elegir la operación por una palabra suelta: \"más\" no siempre es sumar. Leé qué pasa en la situación.","Aceptar un resultado sin controlarlo: si 48 × 21 te da 1.808, la estimación (1.000) te avisa que algo falló."],
"resumen":[{"titulo":"Redondear","texto":"Se mira la cifra de la derecha: de 0 a 4 queda, de 5 a 9 sube. Ej.: 4.372 ≈ 4.400."},{"titulo":"Estimar","texto":"Calcular con números redondos. Ej.: 389 + 512 ≈ 900."},{"titulo":"Controlar","texto":"Si el resultado está lejos de la estimación, algo falló."},{"titulo":"Elegir la operación","texto":"Juntar, quitar, repetir o repartir: según lo que pasa."},{"titulo":"Datos de más","texto":"Algunos datos no se usan. Ej.: las 12 cuadras del cine."}],
"glosario":[{"palabra":"Redondear","significado":"Cambiar un número por uno redondo cercano."},{"palabra":"Estimar","significado":"Calcular aproximadamente, sin la cuenta exacta."},{"palabra":"Razonable","significado":"Que tiene sentido para la situación."},{"palabra":"Dato de más","significado":"Información del problema que no hace falta para resolverlo."},{"palabra":"Vuelto","significado":"Lo que te devuelven cuando pagás con más dinero del necesario."}],
"carpeta":["Redondeá 6.749 a la centena.","Estimá 298 × 21 redondeando 298 a 300 y 21 a 20.","Un kiosco vende 125 alfajores por día durante 6 días, a $900 cada uno. ¿Cuánto recauda en total?","Un compañero dice que 52 × 19 = 9.880. Estimá para ver si tiene sentido y escribí el resultado correcto."],
"respuestas_carpeta":[["6700"],["6000"],["675000","$675000"],["988"]],
"soluciones":{"incompleto":"Viajes: 24. Pasajeros: 45 × 24 = 1.080. Estimación: 1.000.","solo":"3 × 1.180 = 3.540. 3.540 + 650 = 4.190. 5.000 − 4.190 = 810. Le quedan $810.","carpeta":["6.700: la cifra de las decenas es 4, así que la centena queda igual.","6.000: 300 × 20 = 6.000.","$675.000: 125 × 6 = 750 alfajores; 750 × 900 = 675.000.","988: estimando, 50 × 20 = 1.000, así que 9.880 no tiene sentido. 52 × 19 = 52 × 20 − 52 = 1.040 − 52 = 988."]}
}

metas={1:"Suma y resta: propiedades y cálculo mental",2:"Multiplicación y propiedad distributiva",3:"División, resto y relación fundamental",4:"Estimación y problemas de cálculo"}
for k,v in OUT.items():
    json.dump(v,open(os.path.join(AQUI,f'nivel-{k}.json'),'w'),ensure_ascii=False)
    json.dump({"meta":{"materia":"Matemática I","anio":1,"tema_num":2,"tema":"Operaciones con naturales: propiedades y cálculo","leccion_num":4+k,"titulo":metas[k]},"contenido":v},open(f'/tmp/m2_{k}.json','w'),ensure_ascii=False)
print("ok")
