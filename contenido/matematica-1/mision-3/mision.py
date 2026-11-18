# -*- coding: utf-8 -*-
"""Matemática I · Misión 3 · Potenciación y radicación. Genera mision-3.json (se carga con cargar_mision)."""
import json, os
D=lambda t,x:{"tipo":"definicion","titulo":t,"texto":x}
P=lambda x:{"tipo":"parrafo","texto":x}
IM=lambda t,x:{"tipo":"importante","titulo":t,"texto":x}
T=lambda t,c,f,x=None:{"tipo":"tabla","titulo":t,"columnas":c,"filas":f,"iguales":True,**({"texto":x} if x else {})}
E=lambda t,x,i:{"tipo":"ejemplo","titulo":t,"texto":x,"items":i}
S=lambda e,t,b:{"etapa":e,"titulo":t,"bloques":b}
MC=lambda p,o,ok,e,**k:{"t":"multiple_choice","p":p,"o":o,"r":{"correcta":ok},"e":e,**k}
VF=lambda p,ok,e,**k:{"t":"true_false","p":p,"o":["Verdadero","Falso"],"r":{"correcta":ok},"e":e,**k}
N=lambda p,r,e,o=None,**k:{"t":"numeric","p":p,"o":o or {},"r":r,"e":e,**k}
N1={
"objetivo":"Vas a poder explicar qué es una potencia, reconocer la base y el exponente y calcular potencias de números naturales.",
"vas_a_ver":["Qué es una potencia: base y exponente","La potencia como producto de factores iguales","Cuadrados y cubos","El exponente 1 y el exponente 0","Potencias que crecen rápido"],
"secciones":[
 S(1,"Qué es una potencia",[
  D("Potencia","Una <b>potencia</b> es una multiplicación de <b>factores iguales</b>. El número que se repite es la <b>base</b> y la cantidad de veces que se repite es el <b>exponente</b>: 2³ = 2 × 2 × 2 = 8."),
  T("Base, exponente y resultado",["Potencia","Base","Exponente","Producto","Resultado"],[["5²","5","2","5 × 5","25"],["2⁵","2","5","2 × 2 × 2 × 2 × 2","32"],["3⁴","3","4","3 × 3 × 3 × 3","81"]],"El exponente no multiplica a la base: dice cuántas veces se escribe la base como factor."),
 ]),
 S(1,"Cuadrados y cubos",[
  D("Cuadrado y cubo","Con exponente 2 se dice <b>al cuadrado</b> y con exponente 3, <b>al cubo</b>. Un cuadrado de lado 4 tiene 4² = 16 cuadraditos; un cubo de arista 3 tiene 3³ = 27 cubitos."),
  P("Por eso 5² se lee \"cinco al cuadrado\" y 5³, \"cinco al cubo\". Para los demás exponentes se dice \"elevado a\": 2⁵ es \"dos elevado a la quinta\"."),
 ]),
 S(2,"Exponente 1 y exponente 0",[
  P("Mirá qué pasa al bajar el exponente de a uno: cada vez se divide por la base."),
  T("Bajando el exponente",["2³","2²","2¹","2⁰"],[["8","4","2","1"]],"Cada resultado es la mitad del anterior."),
  IM("Dos reglas","Todo número elevado a 1 da el mismo número: 7¹ = 7. Todo número distinto de 0 elevado a 0 da <b>1</b>: 7⁰ = 1."),
 ]),
 S(2,"Potencias que crecen rápido",[
  P("Las potencias sirven para contar cosas que se duplican, se triplican o se multiplican siempre por el mismo número."),
  E("Una bacteria que se duplica","Cada hora, cada bacteria se divide en 2.",["Después de 1 hora hay 2¹ = 2.","Después de 3 horas hay 2³ = 8.","Después de 5 horas hay 2⁵ = 32."]),
 ]),
],
"ejemplo_completo":{"titulo":"4³ y 3⁴","planteo":"Calculá 4³ y 3⁴ y decí cuál es mayor.","pasos":["4³ = 4 × 4 × 4.","4 × 4 = 16 y 16 × 4 = 64.","3⁴ = 3 × 3 × 3 × 3.","3 × 3 = 9; 9 × 3 = 27; 27 × 3 = 81.","81 es mayor que 64: 3⁴ es mayor, aunque tenga la base más chica."]},
"ejemplo_incompleto":{"titulo":"6² y 2⁶","planteo":"Calculá 6² y 2⁶. Completá los espacios.","pasos":["6² = 6 × ___ = 36.","2⁶ = 2 × 2 × 2 × 2 × 2 × 2 = ___ .","La mayor es ___ ."]},
"ejemplo_solo":{"titulo":"5³ y 3⁵","planteo":"Calculá 5³ y 3⁵ y decí cuál es mayor."},
"tip":{"titulo":"Multiplicá de a dos","texto":"Para calcular una potencia, multiplicá el primer par y seguí multiplicando el resultado por la base: 3⁴ es 9, después 27, después 81."},
"ojo":["Multiplicar base por exponente: 2³ no es 2 × 3 = 6; es 2 × 2 × 2 = 8.","Pensar que un número elevado a 0 da 0: 5⁰ = 1."],
"resumen":[{"titulo":"Potencia","texto":"Producto de factores iguales. Ej.: 2³ = 2 × 2 × 2 = 8."},{"titulo":"Base y exponente","texto":"La base se repite tantas veces como dice el exponente."},{"titulo":"Cuadrado y cubo","texto":"Exponente 2 y 3. Ej.: 4² = 16 y 3³ = 27."},{"titulo":"Exponente 1","texto":"Da la base. Ej.: 7¹ = 7."},{"titulo":"Exponente 0","texto":"Da 1. Ej.: 7⁰ = 1."}],
"glosario":[{"palabra":"Potencia","significado":"Multiplicación de factores iguales."},{"palabra":"Base","significado":"El número que se repite como factor."},{"palabra":"Exponente","significado":"El número chico de arriba que dice cuántas veces se repite la base."},{"palabra":"Al cuadrado","significado":"Elevado a 2."},{"palabra":"Al cubo","significado":"Elevado a 3."}],
"carpeta":["Calculá 2⁵.","Calculá 7⁰ + 7¹.","Una caja tiene forma de cubo y en cada arista entran 4 cubitos. ¿Cuántos cubitos hay en total?","Un compañero dice que 3⁴ = 12. ¿Cuánto vale 3⁴?"],
"respuestas_carpeta":[["32"],["8"],["64"],["81"]],
"soluciones":{"incompleto":"6² = 6 × 6 = 36. 2⁶ = 64. La mayor es 2⁶.","solo":"5³ = 125 y 3⁵ = 243. La mayor es 3⁵.","carpeta":["32: 2 × 2 × 2 × 2 × 2.","8: 7⁰ = 1 y 7¹ = 7; 1 + 7 = 8.","64: 4³ = 4 × 4 × 4.","81: 3 × 3 × 3 × 3. Multiplicó la base por el exponente."]}
}
N2={
"objetivo":"Vas a poder usar las propiedades de las potencias para calcular y simplificar, y reconocer cuándo no se pueden aplicar.",
"vas_a_ver":["Producto de potencias de igual base","Cociente de potencias de igual base","Potencia de una potencia","Distributiva respecto del producto y del cociente","Cuándo NO se distribuye: suma y resta"],
"secciones":[
 S(1,"Producto y cociente de igual base",[
  D("Producto de igual base","Para multiplicar potencias de <b>igual base</b>, se deja la base y se <b>suman los exponentes</b>: aᵐ × aⁿ = aᵐ⁺ⁿ."),
  P("Ejemplo: 2³ × 2² = (2 × 2 × 2) × (2 × 2) = 2⁵ = 32. Hay 3 + 2 = 5 factores 2."),
  D("Cociente de igual base","Para dividir potencias de <b>igual base</b>, se deja la base y se <b>restan los exponentes</b>: aᵐ ÷ aⁿ = aᵐ⁻ⁿ."),
  P("Ejemplo: 3⁵ ÷ 3² = 3³ = 27. Comprobación: 243 ÷ 9 = 27."),
 ]),
 S(1,"Potencia de una potencia",[
  D("Potencia de potencia","Para elevar una potencia a otro exponente, se <b>multiplican los exponentes</b>: (aᵐ)ⁿ = aᵐ×ⁿ."),
  P("Ejemplo: (2²)³ = 2² × 2² × 2² = 2⁶ = 64. Comprobación: 2² = 4 y 4³ = 64."),
 ]),
 S(2,"Distributiva con producto y cociente",[
  P("La potencia se puede repartir entre los factores de un producto o de un cociente: (a × b)ⁿ = aⁿ × bⁿ y (a ÷ b)ⁿ = aⁿ ÷ bⁿ."),
  E("Distribuir la potencia","Calculamos de dos formas.",["(2 × 5)³ = 10³ = 1.000. Distribuyendo: 2³ × 5³ = 8 × 125 = 1.000.","(12 ÷ 3)² = 4² = 16. Distribuyendo: 12² ÷ 3² = 144 ÷ 9 = 16."]),
 ]),
 S(2,"Cuándo NO se puede",[
  P("La potencia <b>no se distribuye</b> sobre una suma ni sobre una resta. Y al sumar potencias de igual base <b>no se suman los exponentes</b>."),
  E("Contraejemplos","Las dos formas dan distinto.",["(2 + 3)² = 5² = 25, pero 2² + 3² = 4 + 9 = 13.","(5 − 3)² = 2² = 4, pero 5² − 3² = 25 − 9 = 16.","2³ + 2² = 8 + 4 = 12, que no es 2⁵ = 32."]),
 ]),
],
"ejemplo_completo":{"titulo":"2⁴ × 2³ ÷ 2⁵","planteo":"Escribí como una sola potencia y calculá.","pasos":["Producto de igual base: 2⁴ × 2³ = 2⁴⁺³ = 2⁷.","Cociente de igual base: 2⁷ ÷ 2⁵ = 2⁷⁻⁵ = 2².","2² = 4.","Comprobación: 16 × 8 = 128 y 128 ÷ 32 = 4."]},
"ejemplo_incompleto":{"titulo":"(3²)² × 3","planteo":"Escribí como una sola potencia. Completá los espacios.","pasos":["(3²)² = 3 elevado a ___ (se multiplican los exponentes).","3 = 3¹, entonces 3⁴ × 3¹ = 3 elevado a ___ .","3⁵ = ___ ."]},
"ejemplo_solo":{"titulo":"5⁶ ÷ 5⁴","planteo":"Escribí 5⁶ ÷ 5⁴ como una sola potencia y calculá."},
"tip":{"titulo":"Primero mirá la base","texto":"Las reglas de sumar y restar exponentes solo valen si la base es la misma y la operación es producto o cociente."},
"ojo":["Distribuir sobre una suma: (a + b)² no es a² + b². Ej.: (2 + 3)² = 25, no 13.","Multiplicar las bases: 2³ × 2² es 2⁵, no 4⁵."],
"resumen":[{"titulo":"Producto","texto":"Igual base: se suman exponentes. Ej.: 2³ × 2² = 2⁵."},{"titulo":"Cociente","texto":"Igual base: se restan exponentes. Ej.: 3⁵ ÷ 3² = 3³."},{"titulo":"Potencia de potencia","texto":"Se multiplican exponentes. Ej.: (2²)³ = 2⁶."},{"titulo":"Distributiva","texto":"Vale con × y ÷. Ej.: (2 × 5)³ = 2³ × 5³."},{"titulo":"No vale","texto":"Con + y −. Ej.: (2 + 3)² = 25 y 2² + 3² = 13."}],
"glosario":[{"palabra":"Igual base","significado":"Potencias que tienen el mismo número abajo."},{"palabra":"Propiedad","significado":"Regla que se cumple siempre en una operación."},{"palabra":"Distribuir","significado":"Aplicar la potencia a cada factor por separado."},{"palabra":"Contraejemplo","significado":"Un caso que muestra que una regla no se cumple."},{"palabra":"Simplificar","significado":"Escribir una cuenta de forma más corta."}],
"carpeta":["Escribí 2⁴ × 2² como una sola potencia y calculá el resultado.","Calculá 10⁷ ÷ 10⁴.","Calculá (2 × 3)².","Un compañero dice que (3 + 1)² = 3² + 1² = 10. ¿Cuánto vale realmente (3 + 1)²?"],
"respuestas_carpeta":[["64"],["1000"],["36"],["16"]],
"soluciones":{"incompleto":"(3²)² = 3⁴. 3⁴ × 3¹ = 3⁵. 3⁵ = 243.","solo":"5⁶ ÷ 5⁴ = 5² = 25.","carpeta":["64: 2⁴ × 2² = 2⁶ = 64.","1.000: 10⁷ ÷ 10⁴ = 10³ = 1.000.","36: (2 × 3)² = 6² = 36 (o 2² × 3² = 4 × 9).","16: primero la suma: 4² = 16. No se distribuye sobre la suma."]}
}
N3={
"objetivo":"Vas a poder calcular raíces cuadradas y cúbicas exactas, entendiéndolas como la operación inversa de la potencia, y estimar raíces que no son exactas.",
"vas_a_ver":["Qué es la raíz cuadrada","Qué es la raíz cúbica","Cuadrados y cubos perfectos","Estimar una raíz que no es exacta","Raíces de números grandes"],
"secciones":[
 S(1,"La raíz cuadrada",[
  D("Raíz cuadrada","La <b>raíz cuadrada</b> de un número es el número que, <b>elevado al cuadrado</b>, da ese número. Se escribe √. El número de adentro se llama <b>radicando</b>. √49 = 7 porque 7² = 49."),
  T("Cuadrados perfectos",["n","1","2","3","4","5","6","7","8","9","10"],[["n²","1","4","9","16","25","36","49","64","81","100"]],"Los números de la fila de abajo tienen raíz cuadrada exacta: son <b>cuadrados perfectos</b>."),
 ]),
 S(1,"La raíz cúbica",[
  D("Raíz cúbica","La <b>raíz cúbica</b> de un número es el número que, <b>elevado al cubo</b>, da ese número. Se escribe ∛. ∛64 = 4 porque 4³ = 64."),
  T("Cubos perfectos",["n","1","2","3","4","5","6"],[["n³","1","8","27","64","125","216"]],"La raíz es la operación inversa de la potencia: deshace lo que hizo la potencia."),
 ]),
 S(2,"Estimar una raíz no exacta",[
  P("Si el número no es un cuadrado perfecto, su raíz no es un número natural. Pero podés decir <b>entre qué dos naturales está</b>, buscando los cuadrados perfectos de al lado."),
  E("¿Entre qué números está √50?","Buscamos los cuadrados vecinos.",["49 = 7² y 64 = 8².","50 está entre 49 y 64.","Entonces √50 está entre 7 y 8 (muy cerca de 7)."]),
 ]),
 S(2,"Raíces de números grandes",[
  P("Para un número grande, lo partís en un producto de números con raíz conocida y sacás la raíz de cada factor. La raíz sí se reparte en un producto, pero <b>no en una suma</b>: √(9 + 16) = √25 = 5, y no 3 + 4 = 7."),
  E("Descomponer y sacar la raíz","Dos ejemplos.",["√3.600 = √(36 × 100) = 6 × 10 = 60. Comprobación: 60² = 3.600.","∛8.000 = ∛(8 × 1.000) = 2 × 10 = 20. Comprobación: 20³ = 8.000."]),
 ]),
],
"ejemplo_completo":{"titulo":"√1.600","planteo":"Calculá √1.600 descomponiendo y comprobá el resultado.","pasos":["1.600 = 16 × 100.","√16 = 4 porque 4² = 16.","√100 = 10 porque 10² = 100.","√1.600 = 4 × 10 = 40.","Comprobación: 40² = 40 × 40 = 1.600."]},
"ejemplo_incompleto":{"titulo":"∛27.000","planteo":"Calculá ∛27.000 descomponiendo. Completá los espacios.","pasos":["27.000 = 27 × ___ .","∛27 = ___ porque 3³ = 27.","∛1.000 = 10.","∛27.000 = 3 × 10 = ___ ."]},
"ejemplo_solo":{"titulo":"estimar √90","planteo":"¿Entre qué dos números naturales está √90?"},
"tip":{"titulo":"Comprobá elevando","texto":"Para saber si una raíz está bien, elevá el resultado: al cuadrado si es raíz cuadrada, al cubo si es cúbica. Tiene que darte el radicando."},
"ojo":["Dividir por 2: √36 no es 18; es 6, porque 6² = 36.","Repartir la raíz en una suma: √(9 + 16) es 5, no 3 + 4."],
"resumen":[{"titulo":"Raíz cuadrada","texto":"El número que al cuadrado da el radicando. Ej.: √49 = 7."},{"titulo":"Raíz cúbica","texto":"El número que al cubo da el radicando. Ej.: ∛64 = 4."},{"titulo":"Operación inversa","texto":"La raíz deshace la potencia."},{"titulo":"Estimar","texto":"√50 está entre 7 y 8, porque 49 < 50 < 64."},{"titulo":"Números grandes","texto":"Se descompone. Ej.: √3.600 = 6 × 10 = 60."}],
"glosario":[{"palabra":"Raíz","significado":"Operación inversa de la potencia."},{"palabra":"Radicando","significado":"El número que está adentro de la raíz."},{"palabra":"Cuadrado perfecto","significado":"Número que tiene raíz cuadrada exacta, como 49."},{"palabra":"Cubo perfecto","significado":"Número que tiene raíz cúbica exacta, como 64."},{"palabra":"Estimar","significado":"Decir aproximadamente cuánto da, sin el valor exacto."}],
"carpeta":["Calculá √121.","Calculá ∛125.","Calculá √4.900.","Un compañero dice que √36 = 18 porque dividió por 2. ¿Cuánto vale √36?"],
"respuestas_carpeta":[["11"],["5"],["70"],["6"]],
"soluciones":{"incompleto":"27.000 = 27 × 1.000. ∛27 = 3. Resultado: 30.","solo":"81 = 9² y 100 = 10². 90 está entre 81 y 100, así que √90 está entre 9 y 10.","carpeta":["11: 11² = 121.","5: 5³ = 125.","70: √(49 × 100) = 7 × 10 = 70.","6: 6² = 36. Dividir por 2 no es sacar la raíz."]}
}
N4={
"objetivo":"Vas a poder resolver problemas con cuadrados y cubos: pasar de lado a área, de arista a volumen, y al revés.",
"vas_a_ver":["Lado y área de un cuadrado","Arista y volumen de un cubo","Cómo volver del área al lado y del volumen a la arista","Reconocer cuadrados y cubos perfectos","Problemas de baldosas y cajas"],
"secciones":[
 S(1,"Cuadrado: lado y área",[
  D("Área del cuadrado","El <b>área</b> de un cuadrado es lo que ocupa adentro: <b>lado²</b>. Se mide en unidades cuadradas (cm², m²). El <b>perímetro</b>, en cambio, es el borde: 4 × lado."),
  P("Ejemplo: un cuadrado de lado 7 cm tiene área 7² = 49 cm² y perímetro 4 × 7 = 28 cm. Al revés: si el área es 81 m², el lado es √81 = 9 m."),
 ]),
 S(1,"Cubo: arista y volumen",[
  D("Volumen del cubo","El <b>volumen</b> de un cubo es lo que ocupa: <b>arista³</b>. Se mide en unidades cúbicas (cm³, m³)."),
  P("Ejemplo: un cubo de arista 5 cm tiene volumen 5³ = 125 cm³. Al revés: si el volumen es 216 cm³, la arista es ∛216 = 6 cm."),
 ]),
 S(2,"Reconocer cuadrados y cubos perfectos",[
  P("Un número es <b>cuadrado perfecto</b> si es el área de un cuadrado de lado natural, y <b>cubo perfecto</b> si es el volumen de un cubo de arista natural. Algunos son las dos cosas."),
  T("¿Cuadrado, cubo o los dos?",["Número","Cuadrado perfecto","Cubo perfecto"],[["36","Sí (6²)","No"],["27","No","Sí (3³)"],["64","Sí (8²)","Sí (4³)"],["50","No","No"]]),
 ]),
 S(2,"Problemas de baldosas y cajas",[
  P("Primero fijate qué te dan (lado, área, arista o volumen) y qué te piden. Si te dan el área y piden el lado, sacás raíz cuadrada; si te dan el volumen y piden la arista, raíz cúbica."),
  E("El patio","Un patio cuadrado tiene 36 m² y se cubre con baldosas de 1 m de lado.",["Lado del patio: √36 = 6 m.","Baldosas: cada una ocupa 1 m², así que hacen falta 36.","Borde para poner zócalo: perímetro = 4 × 6 = 24 m."]),
 ]),
],
"ejemplo_completo":{"titulo":"la caja cúbica","planteo":"Una caja con forma de cubo tiene un volumen de 343 cm³. ¿Cuánto mide la arista? ¿Cuál es el área de una de sus caras?","pasos":["Dan el volumen y piden la arista: raíz cúbica.","∛343 = 7, porque 7³ = 7 × 7 × 7 = 343. La arista mide 7 cm.","Cada cara es un cuadrado de lado 7 cm.","Área de una cara: 7² = 49 cm²."]},
"ejemplo_incompleto":{"titulo":"el terreno cuadrado","planteo":"Un terreno cuadrado tiene 144 m² de área. ¿Cuánto mide el lado? ¿Cuánto alambre hace falta para rodearlo? Completá los espacios.","pasos":["Lado: √144 = ___ m.","Perímetro: 4 × 12 = ___ m.","Hacen falta 48 m de alambre."]},
"ejemplo_solo":{"titulo":"el cubo de 9 cm","planteo":"Un cubo tiene 9 cm de arista. ¿Cuál es su volumen?"},
"tip":{"titulo":"Mirá la unidad","texto":"cm es largo (lado, arista, perímetro), cm² es área y cm³ es volumen. La unidad te dice qué estás calculando."},
"ojo":["Confundir perímetro y área: un cuadrado de lado 6 cm tiene área 36 cm², no 24 (eso es el perímetro).","Confundir lado con área: si el área es 49 m², el lado es 7 m, no 49 m."],
"resumen":[{"titulo":"Área del cuadrado","texto":"lado². Ej.: lado 7 cm → 49 cm²."},{"titulo":"Volumen del cubo","texto":"arista³. Ej.: arista 5 cm → 125 cm³."},{"titulo":"Al revés","texto":"Lado = √área; arista = ∛volumen."},{"titulo":"Perímetro","texto":"4 × lado: es el borde, no el área."},{"titulo":"Perfectos","texto":"64 es cuadrado (8²) y cubo (4³)."}],
"glosario":[{"palabra":"Área","significado":"Lo que ocupa una figura plana por dentro."},{"palabra":"Perímetro","significado":"La medida del borde de una figura."},{"palabra":"Volumen","significado":"Lo que ocupa un cuerpo en el espacio."},{"palabra":"Arista","significado":"Cada borde de un cubo."},{"palabra":"Cara","significado":"Cada uno de los 6 cuadrados que forman un cubo."}],
"carpeta":["Un cuadrado tiene 15 cm de lado. ¿Cuál es su área en cm²?","Una habitación cuadrada tiene 64 m² de piso. ¿Cuánto mide el lado en metros?","Un cubo tiene un volumen de 1.000 cm³. ¿Cuánto mide la arista en cm?","Un compañero dice que un cuadrado de 6 cm de lado tiene un área de 24 cm². ¿Cuál es el área correcta en cm²?"],
"respuestas_carpeta":[["225","225cm2","225cm²"],["8","8m"],["10","10cm"],["36","36cm2","36cm²"]],
"soluciones":{"incompleto":"Lado: 12 m. Perímetro: 48 m.","solo":"9³ = 9 × 9 × 9 = 729 cm³.","carpeta":["225 cm²: 15² = 225.","8 m: √64 = 8.","10 cm: ∛1.000 = 10.","36 cm²: 6² = 36. El 24 es el perímetro."]}
}
ACT={
"1":[N("Calculá {b} elevado a {e}.",{"formula":"b^e"},"Se multiplica la base por sí misma tantas veces como dice el exponente.",{"vars":{"b":{"min":2,"max":5},"e":{"min":2,"max":4}}}),
     VF("Cualquier número distinto de 0 elevado a 0 da 0.","Falso","Da 1. Por ejemplo, 7 elevado a 0 = 1.")],
"2":[{"t":"fill_blank","p":"2 elevado a 3 × 2 elevado a 4 = 2 elevado a ___.","o":[],"r":{"huecos":[["7"]]},"e":"Igual base: se suman los exponentes, 3 + 4 = 7."},
     {"t":"multi_select","p":"¿Cuáles de estas igualdades son verdaderas?","o":["(2 × 5) elevado a 2 = 2 elevado a 2 × 5 elevado a 2","(2 + 5) elevado a 2 = 2 elevado a 2 + 5 elevado a 2","3 elevado a 6 ÷ 3 elevado a 2 = 3 elevado a 4","(4 elevado a 2) elevado a 3 = 4 elevado a 5","10 elevado a 2 × 10 elevado a 3 = 10 elevado a 5"],"r":{"correctas":["(2 × 5) elevado a 2 = 2 elevado a 2 × 5 elevado a 2","3 elevado a 6 ÷ 3 elevado a 2 = 3 elevado a 4","10 elevado a 2 × 10 elevado a 3 = 10 elevado a 5"]},"e":"No se distribuye sobre la suma, y en la potencia de potencia los exponentes se multiplican (da 4 elevado a 6)."}],
"3":[N("Calculá la raíz cuadrada de {c}.",{"formula":"n"},"Buscá el número que elevado al cuadrado da el radicando.",{"vars":{"n":{"min":2,"max":15}},"calculadas":{"c":"n*n"}}),
     MC("¿Entre qué dos números naturales está la raíz cuadrada de 30?",["4 y 5","5 y 6","6 y 7","15 y 16"],"5 y 6","25 = 5 al cuadrado y 36 = 6 al cuadrado; 30 está entre 25 y 36.")],
"4":[N("Un cuadrado tiene {a} cm² de área. ¿Cuánto mide su lado en cm?",{"formula":"n"},"El lado es la raíz cuadrada del área.",{"vars":{"n":{"min":3,"max":20}},"calculadas":{"a":"n*n"}}),
     {"t":"matching","p":"Uní cada dato con lo que se calcula a partir de él.","o":{"izquierda":["Lado 4 cm","Arista 4 cm","Área 49 cm²","Volumen 27 cm³"],"derecha":["Área 16 cm²","Volumen 64 cm³","Lado 7 cm","Arista 3 cm"]},"r":{"pares":{"Lado 4 cm":"Área 16 cm²","Arista 4 cm":"Volumen 64 cm³","Área 49 cm²":"Lado 7 cm","Volumen 27 cm³":"Arista 3 cm"}},"e":"Lado al cuadrado da el área; arista al cubo da el volumen; las raíces hacen el camino inverso."}],
"5":[MC("Relámpago. ¿Cuánto es 2 elevado a 0?",["0","1","2","20"],"1","Todo número distinto de 0 elevado a 0 da 1.",tiempo=20),
     N("Relámpago. Calculá la raíz cúbica de 8.000.",{"acepta":[20]},"8.000 = 8 × 1.000; raíz cúbica: 2 × 10 = 20.",tiempo=40),
     VF("Relámpago. (3 + 4) elevado a 2 = 9 + 16.","Falso","(3 + 4) elevado a 2 = 7 elevado a 2 = 49. No se distribuye sobre la suma.",tiempo=25),
     N("Relámpago. Calculá 25 × 19 con la distributiva.",{"acepta":[475]},"25 × 20 − 25 = 500 − 25 = 475 (repaso de la misión 2).",tiempo=40)],
}
EXAMEN=[
 [1,N("Calculá {b} elevado a {e}.",{"formula":"b^e"},"Producto de factores iguales.",{"vars":{"b":{"min":2,"max":9},"e":{"min":2,"max":3}}})],
 [1,MC("En 7 elevado a 4, ¿cuál es la base?",["7","4","28","2.401"],"7","La base es el número que se repite como factor.")],
 [1,{"t":"table_fill","p":"Completá la tabla.","o":{"columnas":["Potencia","Producto","Resultado"],"filas":[["3 elevado a 2","3 × 3","9"],["2 elevado a 4","2 × 2 × 2 × 2",""],["5 elevado a 3","5 × 5 × 5",""]]},"r":{"celdas":{"2|Resultado":["16"],"3|Resultado":["125"]}},"e":"2 × 2 × 2 × 2 = 16 y 5 × 5 × 5 = 125."}],
 [2,{"t":"fill_blank","p":"5 elevado a 8 ÷ 5 elevado a 3 = 5 elevado a ___.","o":[],"r":{"huecos":[["5"]]},"e":"Igual base en un cociente: se restan los exponentes, 8 − 3 = 5."}],
 [2,VF("(4 + 2) elevado a 2 es igual a 4 elevado a 2 + 2 elevado a 2.","Falso","(4 + 2) elevado a 2 = 36, pero 16 + 4 = 20.")],
 [2,N("Calculá (2 elevado a 3) elevado a 2.",{"acepta":[64]},"Se multiplican los exponentes: 2 elevado a 6 = 64.")],
 [3,N("Calculá la raíz cuadrada de {c}.",{"formula":"n"},"El número que elevado al cuadrado da el radicando.",{"vars":{"n":{"min":11,"max":20}},"calculadas":{"c":"n*n"}})],
 [3,N("Calculá la raíz cúbica de 216.",{"acepta":[6]},"6 × 6 × 6 = 216.")],
 [3,MC("Un compañero dice que la raíz cuadrada de 64 es 32. ¿Qué error cometió?",["Dividió por 2","Multiplicó por 2","Restó 2","No cometió ningún error"],"Dividió por 2","La raíz cuadrada de 64 es 8, porque 8 × 8 = 64.")],
 [4,N("Un cubo tiene 5 cm de arista. ¿Cuál es su volumen en cm³?",{"acepta":[125]},"5 × 5 × 5 = 125 cm³.")],
 [4,N("Un terreno cuadrado tiene 400 m² de área. ¿Cuánto mide cada lado en metros?",{"acepta":[20]},"La raíz cuadrada de 400 es 20.")],
 [4,{"t":"classify","p":"Clasificá cada número.","o":{"elementos":["16","27","36","64","125","49"],"categorias":["Solo cuadrado perfecto","Solo cubo perfecto","Cuadrado y cubo perfecto"]},"r":{"categorias":{"16":"Solo cuadrado perfecto","27":"Solo cubo perfecto","36":"Solo cuadrado perfecto","64":"Cuadrado y cubo perfecto","125":"Solo cubo perfecto","49":"Solo cuadrado perfecto"}},"e":"64 = 8 al cuadrado = 4 al cubo."}],
 [4,N("Un patio cuadrado de 9 m de lado se cubre con baldosas cuadradas de 1 m de lado. ¿Cuántas baldosas hacen falta?",{"acepta":[81]},"El área es 9 al cuadrado = 81 m², y cada baldosa ocupa 1 m².")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":3,"practica":"Práctica general: potenciación y radicación","examen_titulo":"Nivel jefe: potenciación y radicación",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-3.json"),"w"),ensure_ascii=False)
print("ok")
