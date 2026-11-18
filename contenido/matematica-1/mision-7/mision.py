# -*- coding: utf-8 -*-
"""Matemática I · Misión 7 · MCD y MCM. Genera mision-7.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
N1={
"objetivo":"Vas a poder calcular el máximo común divisor (MCD) de dos o tres números usando la descomposición en factores primos, y reconocer números coprimos.",
"vas_a_ver":["Qué es el máximo común divisor","Cómo calcularlo por descomposición","Números coprimos","MCD de tres números"],
"secciones":[
 S(1,"El máximo común divisor",[
  D("MCD","El <b>máximo común divisor (MCD)</b> de dos números es el <b>mayor</b> de sus divisores comunes."),
  P("Ejemplo: divisores de 12: 1, 2, 3, 4, 6, 12. Divisores de 18: 1, 2, 3, 6, 9, 18. Comunes: 1, 2, 3, 6. El MCD es 6."),
 ]),
 S(1,"MCD por descomposición",[
  D("Regla del MCD","Se descomponen los números en factores primos y se multiplican <b>solo los factores comunes</b>, cada uno con su <b>menor exponente</b>."),
  T("MCD de 72 y 60",["Número","Descomposición"],[["72","2³ × 3²"],["60","2² × 3 × 5"],["MCD","2² × 3 = 12"]],"El 5 no es común, así que no entra. Del 2 se toma 2² (el menor) y del 3, 3¹."),
 ]),
 S(2,"Números coprimos",[
  P("Dos números son <b>coprimos</b> si su MCD es 1: no tienen ningún factor primo en común. No hace falta que sean primos: 8 = 2³ y 15 = 3 × 5 son coprimos."),
 ]),
 S(2,"MCD de tres números",[
  E("MCD de 24, 36 y 60","El factor tiene que estar en los tres.",["24 = 2³ × 3; 36 = 2² × 3²; 60 = 2² × 3 × 5.","Comunes a los tres: 2 y 3. Menores exponentes: 2² y 3¹.","MCD = 2² × 3 = 12."]),
 ]),
],
"ejemplo_completo":{"titulo":"MCD de 84 y 126","planteo":"Calculá el MCD de 84 y 126 por descomposición y comprobá.","pasos":["84 = 2² × 3 × 7.","126 = 2 × 3² × 7.","Comunes con menor exponente: 2, 3 y 7.","MCD = 2 × 3 × 7 = 42.","Comprobación: 84 ÷ 42 = 2 y 126 ÷ 42 = 3."]},
"ejemplo_incompleto":{"titulo":"MCD de 40 y 100","planteo":"Completá los espacios.","pasos":["40 = 2³ × 5.","100 = 2² × 5².","MCD = 2 elevado a ___ × 5 = ___ ."]},
"ejemplo_solo":{"titulo":"MCD de 45 y 75","planteo":"Calculá el MCD de 45 y 75 por descomposición."},
"tip":{"titulo":"El MCD no supera al menor","texto":"El MCD divide a los dos números, así que nunca puede ser mayor que el más chico. Si te da más, revisá."},
"ojo":["Tomar todos los factores: en el MCD van solo los comunes.","Tomar el mayor exponente: en el MCD va el menor."],
"resumen":[{"titulo":"MCD","texto":"El mayor divisor común. Ej.: 12 y 18 → 6."},{"titulo":"Regla","texto":"Factores comunes con el menor exponente."},{"titulo":"Ejemplo","texto":"72 y 60 → 2² × 3 = 12."},{"titulo":"Coprimos","texto":"MCD = 1. Ej.: 8 y 15."}],
"glosario":[{"palabra":"MCD","significado":"Máximo común divisor: el mayor divisor que comparten."},{"palabra":"Factor común","significado":"Primo que aparece en las dos descomposiciones."},{"palabra":"Coprimos","significado":"Números cuyo MCD es 1."},{"palabra":"Exponente","significado":"Cuántas veces se repite el factor."}],
"carpeta":["Calculá el MCD de 36 y 54.","¿Cuál es el MCD de 14 y 25?","Calculá el MCD de 12, 18 y 30.","Un compañero calculó el MCD de 2³ × 3 y 2² × 3² tomando 2³ × 3² = 72. ¿Cuál es el MCD correcto?"],
"respuestas_carpeta":[["18"],["1"],["6"],["12"]],
"soluciones":{"incompleto":"MCD = 2² × 5 = 20.","solo":"45 = 3² × 5 y 75 = 3 × 5². MCD = 3 × 5 = 15.","carpeta":["18: 36 = 2² × 3² y 54 = 2 × 3³; MCD = 2 × 3² = 18.","1: 14 = 2 × 7 y 25 = 5²: no tienen factores comunes. Son coprimos.","6: 12 = 2² × 3, 18 = 2 × 3², 30 = 2 × 3 × 5; MCD = 2 × 3.","12: hay que tomar el menor exponente: 2² × 3 = 12."]}
}
N2={
"objetivo":"Vas a poder calcular el mínimo común múltiplo (MCM) de dos o tres números por descomposición y comprobarlo con la relación entre MCD, MCM y el producto.",
"vas_a_ver":["Qué es el mínimo común múltiplo","Cómo calcularlo por descomposición","La relación MCD × MCM = a × b","MCM de tres números"],
"secciones":[
 S(1,"El mínimo común múltiplo",[
  D("MCM","El <b>mínimo común múltiplo (MCM)</b> de dos números es el <b>menor</b> de sus múltiplos comunes, sin contar el 0."),
  P("Ejemplo: múltiplos de 4: 4, 8, 12, 16, 20, 24… Múltiplos de 6: 6, 12, 18, 24… El menor común es 12."),
 ]),
 S(1,"MCM por descomposición",[
  D("Regla del MCM","Se descomponen los números y se multiplican <b>todos los factores</b>, comunes y no comunes, cada uno con su <b>mayor exponente</b>."),
  T("MCM de 12 y 18",["Número","Descomposición"],[["12","2² × 3"],["18","2 × 3²"],["MCM","2² × 3² = 36"]],"Del 2 se toma 2² y del 3, 3²: los mayores."),
 ]),
 S(2,"MCD, MCM y el producto",[
  P("Para dos números siempre vale: <b>a × b = MCD × MCM</b>. Sirve para comprobar o para calcular uno de los dos si conocés el otro."),
  P("Con 12 y 18: 12 × 18 = 216, y MCD × MCM = 6 × 36 = 216."),
 ]),
 S(2,"MCM de tres números",[
  E("MCM de 4, 6 y 10","Todos los factores con el mayor exponente.",["4 = 2²; 6 = 2 × 3; 10 = 2 × 5.","Factores: 2², 3 y 5.","MCM = 2² × 3 × 5 = 60."]),
 ]),
],
"ejemplo_completo":{"titulo":"MCM de 24 y 90","planteo":"Calculá el MCM de 24 y 90 y comprobalo con el producto.","pasos":["24 = 2³ × 3 y 90 = 2 × 3² × 5.","Todos los factores con mayor exponente: 2³, 3² y 5.","MCM = 8 × 9 × 5 = 360.","MCD = 2 × 3 = 6.","Comprobación: 24 × 90 = 2.160 y 6 × 360 = 2.160."]},
"ejemplo_incompleto":{"titulo":"MCM de 8 y 12","planteo":"Completá los espacios.","pasos":["8 = 2³ y 12 = 2² × 3.","MCM = 2³ × 3 = ___ .","MCD = ___ .","Comprobación: 8 × 12 = 96 y 4 × 24 = 96."]},
"ejemplo_solo":{"titulo":"MCM de 15, 20 y 30","planteo":"Calculá el MCM de 15, 20 y 30 por descomposición."},
"tip":{"titulo":"El MCM no es menor que el mayor","texto":"El MCM es múltiplo de los dos, así que nunca es más chico que el mayor de ellos. Multiplicarlos siempre da un múltiplo común, pero no siempre el menor."},
"ojo":["Tomar el menor exponente: en el MCM va el mayor.","Multiplicar los números sin más: 6 × 9 = 54 es múltiplo común, pero el MCM es 18."],
"resumen":[{"titulo":"MCM","texto":"El menor múltiplo común. Ej.: 4 y 6 → 12."},{"titulo":"Regla","texto":"Todos los factores con el mayor exponente."},{"titulo":"Ejemplo","texto":"12 y 18 → 2² × 3² = 36."},{"titulo":"Relación","texto":"a × b = MCD × MCM."}],
"glosario":[{"palabra":"MCM","significado":"Mínimo común múltiplo: el menor múltiplo que comparten, sin el 0."},{"palabra":"Factor no común","significado":"Primo que aparece en una sola descomposición."},{"palabra":"Comprobar","significado":"Verificar con otra cuenta."}],
"carpeta":["Calculá el MCM de 6 y 8.","Calculá el MCM de 9 y 12.","Calculá el MCM de 2, 3 y 5.","Un compañero dice que el MCM de 6 y 9 es 54 porque los multiplicó. ¿Cuál es el MCM?"],
"respuestas_carpeta":[["24"],["36"],["30"],["18"]],
"soluciones":{"incompleto":"MCM = 24. MCD = 4.","solo":"15 = 3 × 5, 20 = 2² × 5, 30 = 2 × 3 × 5. MCM = 2² × 3 × 5 = 60.","carpeta":["24: 6 = 2 × 3 y 8 = 2³; MCM = 2³ × 3.","36: 9 = 3² y 12 = 2² × 3; MCM = 2² × 3².","30: no tienen factores comunes; MCM = 2 × 3 × 5.","18: 6 = 2 × 3 y 9 = 3²; MCM = 2 × 3² = 18."]}
}
N3={
"objetivo":"Vas a poder resolver problemas de repartos, coincidencias, cortes y embaldosados usando el MCD o el MCM.",
"vas_a_ver":["Repartir en partes iguales sin resto: MCD","Cosas que coinciden cada cierto tiempo: MCM","Cortar y embaldosar sin desperdicio","Problemas con tres cantidades"],
"secciones":[
 S(1,"Repartos sin resto: MCD",[
  D("Repartir con el MCD","Para repartir varias cantidades en la <b>mayor cantidad posible</b> de grupos iguales sin que sobre nada, se calcula el <b>MCD</b>."),
  E("Lápices y gomas","Hay 24 lápices y 36 gomas para armar cajas iguales, la mayor cantidad posible.",["MCD de 24 y 36 = 12.","Se arman 12 cajas.","Cada una lleva 24 ÷ 12 = 2 lápices y 36 ÷ 12 = 3 gomas."]),
 ]),
 S(1,"Coincidencias: MCM",[
  D("Coincidir con el MCM","Si dos cosas pasan cada cierto tiempo y empiezan juntas, <b>vuelven a coincidir</b> cada <b>MCM</b> de esos tiempos."),
  P("Ejemplo: una luz titila cada 6 segundos y otra cada 8. Si titilan juntas, vuelven a hacerlo cada MCM(6, 8) = 24 segundos."),
 ]),
 S(2,"Cortar y embaldosar",[
  P("Para cortar en <b>trozos iguales lo más largos posible</b> sin sobrante, se usa el MCD. Para armar el <b>cuadrado más chico</b> juntando baldosas rectangulares, se usa el MCM."),
  E("Tablas y baldosas","Dos situaciones.",["Tablas de 90 cm y 120 cm en trozos iguales lo más largos posible: MCD = 30 cm. Salen 3 + 4 = 7 trozos.","Baldosas de 12 cm × 18 cm para formar el menor cuadrado: MCM(12, 18) = 36 cm de lado."]),
 ]),
 S(2,"Tres cantidades",[
  P("Con tres o más cantidades se hace igual: el MCD o el MCM de todas. Ejemplo: tres colectivos salen cada 10, 15 y 20 minutos; coinciden cada MCM(10, 15, 20) = 60 minutos."),
 ]),
],
"ejemplo_completo":{"titulo":"los faros","planteo":"Tres faros se encienden cada 12, 18 y 30 segundos. Ahora se encendieron juntos. ¿En cuántos segundos vuelven a coincidir?","pasos":["Es una coincidencia: se busca el MCM.","12 = 2² × 3; 18 = 2 × 3²; 30 = 2 × 3 × 5.","MCM = 2² × 3² × 5 = 180.","Vuelven a coincidir dentro de 180 segundos, o sea 3 minutos."]},
"ejemplo_incompleto":{"titulo":"las bolsitas","planteo":"Hay 60 alfajores y 84 caramelos para armar la mayor cantidad posible de bolsitas iguales. Completá los espacios.","pasos":["60 = 2² × 3 × 5 y 84 = 2² × 3 × 7.","MCD = 2² × 3 = ___ bolsitas.","Cada una lleva ___ alfajores y ___ caramelos."]},
"ejemplo_solo":{"titulo":"las parcelas","planteo":"Un terreno de 48 m por 72 m se divide en parcelas cuadradas iguales, lo más grandes posible. ¿Cuánto mide el lado de cada parcela? ¿Cuántas parcelas hay?"},
"tip":{"titulo":"Mirá el tamaño de la respuesta","texto":"Si lo que buscás tiene que caber dentro de los datos (repartir, cortar), es el MCD. Si tiene que contener a los datos (coincidir, juntar), es el MCM."},
"ojo":["Elegir el MCM para repartir: repartir siempre da un número más chico que los datos.","Responder sin comprobar: verificá que el reparto no deje resto."],
"resumen":[{"titulo":"Repartir","texto":"Mayor cantidad de grupos iguales: MCD."},{"titulo":"Coincidir","texto":"Cuándo vuelven a coincidir: MCM."},{"titulo":"Cortar","texto":"Trozos iguales lo más largos posible: MCD."},{"titulo":"Embaldosar","texto":"Menor cuadrado con baldosas: MCM."}],
"glosario":[{"palabra":"Coincidir","significado":"Pasar al mismo tiempo."},{"palabra":"Desperdicio","significado":"Lo que sobra y no se usa."},{"palabra":"Embaldosar","significado":"Cubrir una superficie con baldosas."},{"palabra":"Parcela","significado":"Cada parte en que se divide un terreno."}],
"carpeta":["Dos colectivos salen juntos de la terminal; uno sale cada 20 minutos y el otro cada 30. ¿En cuántos minutos vuelven a salir juntos?","Hay 45 rosas y 60 claveles para armar la mayor cantidad posible de ramos iguales. ¿Cuántos ramos se arman?","En esos ramos, ¿cuántas rosas lleva cada uno?","Un compañero, para cortar cintas de 18 cm y 24 cm en trozos iguales lo más largos posible, calculó el MCM. ¿Cuánto tiene que medir cada trozo en cm?"],
"respuestas_carpeta":[["60"],["15"],["3"],["6"]],
"soluciones":{"incompleto":"12 bolsitas. 5 alfajores y 7 caramelos.","solo":"MCD(48, 72) = 24: parcelas de 24 m de lado. Hay 2 × 3 = 6 parcelas.","carpeta":["60: MCM(20, 30).","15: MCD(45, 60).","3: 45 ÷ 15.","6: es un corte, se usa el MCD(18, 24) = 6."]}
}
N4={
"objetivo":"Vas a poder decidir si un problema se resuelve con el MCD o con el MCM, sin guiarte solo por las palabras, y verificar que la respuesta cumpla las condiciones.",
"vas_a_ver":["¿La respuesta es más chica o más grande que los datos?","El límite de las palabras clave","Problemas mixtos","Verificar las condiciones","Armar tus propios problemas"],
"secciones":[
 S(1,"¿Más chica o más grande?",[
  D("Cómo decidir","Si la respuesta tiene que <b>dividir</b> a los datos (es más chica o igual), se usa el <b>MCD</b>. Si tiene que ser <b>múltiplo</b> de los datos (es más grande o igual), se usa el <b>MCM</b>."),
  T("Dos preguntas con los mismos números",["Pregunta","Respuesta","Se usa"],[["Mayor largo de trozos para cortar cintas de 8 y 12 cm","4 cm","MCD"],["Menor largo de una cinta que se pueda cortar en trozos de 8 y de 12 cm","24 cm","MCM"]]),
 ]),
 S(1,"El límite de las palabras",[
  P("\"Mayor\" no siempre es MCD ni \"menor\" siempre es MCM. En la tabla, la pregunta con \"menor\" se resuelve con el MCM. Lo que decide es qué pasa en la situación: ¿se reparte o se junta?"),
 ]),
 S(2,"Problemas mixtos",[
  E("El club","Juan va al club cada 6 días y Sofía cada 8. Un día que coinciden llevan 18 gaseosas y 24 sándwiches para repartir en bandejas iguales, la mayor cantidad posible.",["Coincidir: MCM(6, 8) = 24. Coinciden cada 24 días.","Repartir: MCD(18, 24) = 6. Arman 6 bandejas.","Cada bandeja: 3 gaseosas y 4 sándwiches."]),
 ]),
 S(2,"Verificar y armar",[
  P("Al terminar, comprobá la respuesta: un MCD tiene que dividir a todos los datos; un MCM tiene que ser múltiplo de todos. Y para practicar, inventá un problema de reparto y uno de coincidencia con los mismos números."),
 ]),
],
"ejemplo_completo":{"titulo":"la florista","planteo":"Una florista tiene 36 rosas y 48 tulipanes. Quiere armar la mayor cantidad posible de ramos iguales sin que sobre nada. ¿Cuántos ramos arma y qué lleva cada uno?","pasos":["Se reparte: la respuesta tiene que dividir a 36 y a 48. Es el MCD.","36 = 2² × 3² y 48 = 2⁴ × 3. MCD = 2² × 3 = 12.","Arma 12 ramos, cada uno con 3 rosas y 4 tulipanes.","Verificación: 12 × 3 = 36 y 12 × 4 = 48."]},
"ejemplo_incompleto":{"titulo":"los semáforos","planteo":"Un semáforo cambia cada 40 segundos y otro cada 60. Acaban de cambiar juntos. ¿Cuándo vuelven a coincidir? Completá los espacios.","pasos":["La respuesta tiene que ser ___ que 60: es el MCM.","40 = 2³ × 5 y 60 = 2² × 3 × 5.","MCM = 2³ × 3 × 5 = ___ segundos, o sea ___ minutos."]},
"ejemplo_solo":{"titulo":"los postes","planteo":"Dos lados de un terreno miden 54 m y 42 m. Se ponen postes a la misma distancia, con uno en cada esquina y la mayor distancia posible entre postes. ¿Cada cuántos metros va un poste?"},
"tip":{"titulo":"Imaginá la situación","texto":"Antes de calcular, preguntate: ¿estoy partiendo algo en pedazos (MCD) o esperando a que algo se junte (MCM)?"},
"ojo":["Decidir solo por una palabra: \"menor\" puede pedir un MCM.","No distinguir el mayor del menor valor posible: hay muchos múltiplos comunes, el MCM es el menor."],
"resumen":[{"titulo":"MCD","texto":"La respuesta divide a los datos: repartir, cortar."},{"titulo":"MCM","texto":"La respuesta es múltiplo de los datos: coincidir, juntar."},{"titulo":"Palabras","texto":"Ayudan, pero no deciden."},{"titulo":"Verificar","texto":"El MCD divide a todos; el MCM es múltiplo de todos."}],
"glosario":[{"palabra":"Condición","significado":"Lo que la respuesta tiene que cumplir."},{"palabra":"Verificar","significado":"Comprobar que la respuesta cumple todo."},{"palabra":"Palabra clave","significado":"Palabra del enunciado que da una pista."}],
"carpeta":["Si la respuesta de un problema tiene que dividir a todos los datos, ¿se calcula el MCD o el MCM?","Cintas de 30 cm y 45 cm se cortan en trozos iguales lo más largos posible, sin sobrante. ¿Cuánto mide cada trozo en cm?","Lucas riega una planta cada 4 días y otra cada 10. Hoy regó las dos. ¿Dentro de cuántos días vuelve a regarlas el mismo día?","Para \"¿cuál es la menor cantidad de caramelos que se puede repartir en bolsas de 6 y también en bolsas de 9 sin que sobre?\", un compañero leyó \"menor\" y calculó el MCD. ¿Cuál es la respuesta correcta?"],
"respuestas_carpeta":[["MCD"],["15"],["20"],["18"]],
"soluciones":{"incompleto":"Mayor que 60. MCM = 120 segundos, o sea 2 minutos.","solo":"La distancia tiene que dividir a 54 y a 42: MCD(54, 42) = 6. Un poste cada 6 m.","carpeta":["MCD: el MCD divide a todos los datos.","15: MCD(30, 45).","20: MCM(4, 10).","18: la cantidad tiene que ser múltiplo de 6 y de 9: MCM = 18."]}
}
ACT={
"1":[N("Calculá el MCD de 48 y 80.",{"acepta":[16]},"48 = 2⁴ × 3 y 80 = 2⁴ × 5. MCD = 2⁴ = 16."),
     VF("15 y 28 son coprimos.","Verdadero","15 = 3 × 5 y 28 = 2² × 7: no tienen factores comunes.")],
"2":[N("Calculá el MCM de 10 y 15.",{"acepta":[30]},"10 = 2 × 5 y 15 = 3 × 5. MCM = 2 × 3 × 5 = 30."),
     {"t":"fill_blank","p":"Si el MCD de dos números es 4 y su producto es 96, su MCM es ___.","o":[],"r":{"huecos":[["24"]]},"e":"a × b = MCD × MCM, así que MCM = 96 ÷ 4 = 24."}],
"3":[N("Dos alarmas suenan cada 15 y cada 25 minutos. Sonaron juntas. ¿En cuántos minutos vuelven a sonar juntas?",{"acepta":[75]},"Coincidencia: MCM(15, 25) = 3 × 5² = 75."),
     N("Se reparten 54 figuritas y 72 stickers en la mayor cantidad posible de sobres iguales, sin que sobre nada. ¿Cuántos sobres se arman?",{"acepta":[18]},"Reparto: MCD(54, 72) = 2 × 3² = 18.")],
"4":[{"t":"classify","p":"Clasificá cada problema según lo que hay que calcular.","o":{"elementos":["Cada cuánto coinciden dos colectivos","Mayor tamaño de baldosa cuadrada para cubrir un piso sin cortar","Menor cantidad de alumnos que se pueden agrupar de a 4 y de a 6","Mayor cantidad de bolsitas iguales con 20 y 30 caramelos"],"categorias":["MCD","MCM"]},"r":{"categorias":{"Cada cuánto coinciden dos colectivos":"MCM","Mayor tamaño de baldosa cuadrada para cubrir un piso sin cortar":"MCD","Menor cantidad de alumnos que se pueden agrupar de a 4 y de a 6":"MCM","Mayor cantidad de bolsitas iguales con 20 y 30 caramelos":"MCD"}},"e":"Repartir o cortar: MCD. Coincidir o juntar: MCM."},
     MC("La respuesta de un problema tiene que ser múltiplo de todos los datos. ¿Qué calculás?",["MCD","MCM"],"MCM","Un múltiplo común es más grande o igual que los datos.")],
"5":[N("Relámpago. ¿Cuál es el MCD de 12 y 20?",{"acepta":[4]},"12 = 2² × 3 y 20 = 2² × 5.",tiempo=30),
     N("Relámpago. ¿Cuál es el MCM de 3 y 7?",{"acepta":[21]},"Son coprimos: el MCM es su producto.",tiempo=25),
     VF("Relámpago. El MCM de dos números nunca es menor que el mayor de ellos.","Verdadero","Es múltiplo de los dos.",tiempo=20),
     N("Relámpago. ¿Cuántos divisores tiene 2 elevado a 3 × 3 elevado a 2?",{"acepta":[12]},"(3 + 1) × (2 + 1) = 12 (repaso de la misión 6).",tiempo=40)],
}
EXAMEN=[
 [1,N("Calculá el MCD de 2 elevado a 3 × 3 × 5 y 2 × 3 elevado a 2 × 7.",{"acepta":[6]},"Comunes con menor exponente: 2 y 3.")],
 [1,MC("¿Cuál de estos pares de números son coprimos?",["6 y 9","8 y 12","9 y 16","10 y 15"],"9 y 16","9 = 3² y 16 = 2⁴ no comparten factores.")],
 [1,N("Calculá el MCD de 30, 45 y 60.",{"acepta":[15]},"30 = 2 × 3 × 5, 45 = 3² × 5, 60 = 2² × 3 × 5. MCD = 3 × 5.")],
 [2,N("Calculá el MCM de 12 y 30.",{"acepta":[60]},"12 = 2² × 3 y 30 = 2 × 3 × 5. MCM = 2² × 3 × 5.")],
 [2,MC("Para calcular el MCM por descomposición se toman…",["Solo los factores comunes, con el menor exponente","Todos los factores, con el mayor exponente","Solo los factores comunes, con el mayor exponente","Todos los factores, con el menor exponente"],"Todos los factores, con el mayor exponente","La primera opción es la regla del MCD.")],
 [2,N("El MCD de 8 y 20 es 4. Usando el producto de los dos números, ¿cuál es su MCM?",{"acepta":[40]},"8 × 20 = 160 y 160 ÷ 4 = 40.")],
 [3,N("Tres corredores dan una vuelta a la pista en 4, 6 y 9 minutos. Salieron juntos. ¿En cuántos minutos vuelven a pasar juntos por la largada?",{"acepta":[36]},"MCM(4, 6, 9) = 2² × 3² = 36.")],
 [3,N("Un piso de 360 cm por 450 cm se cubre con baldosas cuadradas iguales, lo más grandes posible, sin cortar ninguna. ¿Cuánto mide el lado de cada baldosa en cm?",{"acepta":[90]},"MCD(360, 450) = 2 × 3² × 5 = 90.")],
 [3,N("Un piso de 360 cm por 450 cm se cubre con baldosas cuadradas de 90 cm de lado. ¿Cuántas baldosas hacen falta?",{"acepta":[20]},"360 ÷ 90 = 4 y 450 ÷ 90 = 5: 4 × 5 = 20.")],
 [4,MC("Problema: \"¿Cuál es la menor cantidad de bombones que se puede repartir en cajas de 12 y también en cajas de 15 sin que sobre?\". ¿Qué se calcula?",["MCD","MCM"],"MCM","La cantidad tiene que ser múltiplo de 12 y de 15.")],
 [4,N("¿Cuál es la menor cantidad de bombones que se puede repartir en cajas de 12 y también en cajas de 15 sin que sobre ninguno?",{"acepta":[60]},"MCM(12, 15) = 2² × 3 × 5 = 60.")],
 [4,VF("Si un problema dice \"mayor\", siempre se calcula el MCD.","Falso","Lo que decide es la situación, no la palabra.")],
 [4,N("Hay 42 varones y 56 mujeres para formar la mayor cantidad posible de equipos mixtos iguales. ¿Cuántos equipos se forman?",{"acepta":[14]},"MCD(42, 56) = 2 × 7 = 14.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":7,"practica":"Práctica general: MCD y MCM","examen_titulo":"Nivel jefe: MCD y MCM",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-7.json"),"w"),ensure_ascii=False)
print("ok")
