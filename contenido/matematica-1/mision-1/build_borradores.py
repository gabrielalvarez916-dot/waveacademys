# -*- coding: utf-8 -*-
import json, copy, base64
n1 = json.load(open('/home/claude/prueba/n1.json'))['contenido']
D=lambda t,x:{"tipo":"definicion","titulo":t,"texto":x}
P=lambda x:{"tipo":"parrafo","texto":x}
IM=lambda t,x:{"tipo":"importante","titulo":t,"texto":x}
T=lambda t,c,f,x=None:{"tipo":"tabla","titulo":t,"columnas":c,"filas":f,"iguales":True,**({"texto":x} if x else {})}
E=lambda t,x,i:{"tipo":"ejemplo","titulo":t,"texto":x,"items":i}
S=lambda e,t,b:{"etapa":e,"titulo":t,"bloques":b}
OUT={}

# ---------------- NIVEL 1: decimal (recortado del borrador anterior) ----------------
c=copy.deepcopy(n1)
sec=c['secciones']
img=[b for b in sec[1]['bloques'] if b['tipo']=='imagen'][0]; img['png_base64']=base64.b64encode(open('/home/claude/mision1/base10_small.png','rb').read()).decode()
sec[1]['bloques']=[b for b in sec[1]['bloques'] if b['tipo'] in ('definicion','tabla')]+[img]
sec[0]['bloques']=[sec[0]['bloques'][0], P("Hay muchas formas de escribir un mismo número: los romanos escribían 2026 como MMXXVI y nosotros 2.026. El número es el mismo; cambia el sistema.")]
sec[2]['bloques']=[b for b in sec[2]['bloques'] if b['tipo']!='ejemplo']
sec[5]['bloques']=[P('Un <b>canje</b> es cambiar 1 grupo por 10 del orden anterior (o al revés). Por eso un mismo número se escribe de varias formas: 4.205 = 4.000 + 200 + 5 = 3.000 + 1.200 + 5, porque 1 unidad de mil se canjea por 10 centenas.')]
m=sec[3]; m['titulo']='Descomposición aditiva y multiplicativa'; m['bloques']=[sec[3]['bloques'][0],sec[3]['bloques'][1],sec[4]['bloques'][0],sec[4]['bloques'][1]]
c['secciones']=[sec[0],sec[1],sec[2],m,sec[5]]
OUT[1]=c

# ---------------- NIVEL 2: binario ----------------
OUT[2]={
"objetivo":"Vas a poder explicar cómo funciona el sistema binario y pasar números de binario a decimal y de decimal a binario.",
"vas_a_ver":["Qué es el sistema binario y para qué se usa","Las dos cifras: 0 y 1","Cuánto vale cada lugar: 1, 2, 4, 8, 16…","Cómo pasar de binario a decimal","Cómo pasar de decimal a binario con divisiones por 2"],
"secciones":[
 S(1,"El sistema binario",[
  D("Sistema binario","El <b>sistema binario</b> usa solo <b>2 cifras</b>: el 0 y el 1. Se <b>agrupa de a 2</b>: cuando juntás 2 de algo, lo cambiás por 1 del lugar siguiente."),
  P("Se usa en las computadoras y los celulares, porque un circuito solo puede estar en dos estados: apagado (0) o encendido (1). Cada cifra binaria se llama <b>bit</b>."),
  T("Contar en binario",["Decimal","0","1","2","3","4","5","6","7","8"],[["Binario","0","1","10","11","100","101","110","111","1000"]],"Al llegar a 2 no hay una cifra nueva: se agrupa y se escribe 10 (un grupo de 2 y cero unidades)."),
 ]),
 S(1,"El valor de cada lugar",[
  D("Valor posicional en binario","En binario, cada lugar vale <b>el doble</b> del lugar que tiene a su derecha. Empezando por la derecha, los lugares valen 1, 2, 4, 8, 16, 32…"),
  T("El número 1011₂ en la tabla de lugares",["Lugar de 8","Lugar de 4","Lugar de 2","Lugar de 1"],[["1","0","1","1"],["vale 8","vale 0","vale 2","vale 1"]],"Un 1 cuenta el valor de su lugar; un 0 no cuenta nada. El subíndice ₂ avisa que el número está en binario."),
 ]),
 S(2,"De binario a decimal",[
  P("Para pasar un número binario a decimal, sumás los valores de los lugares donde hay un 1."),
  E("Pasar 1011₂ y 11001₂ a decimal","Sumamos solo los lugares con 1.",["1011₂: lugares de 8, 2 y 1. 8 + 2 + 1 = 11.","11001₂: lugares de 16, 8 y 1. 16 + 8 + 1 = 25.","Entonces 1011₂ = 11 y 11001₂ = 25."]),
 ]),
 S(2,"De decimal a binario",[
  P("Para pasar un número decimal a binario, lo dividís por 2 una y otra vez, anotando cada resto, hasta llegar a cociente 0. El binario se lee con los restos <b>de abajo hacia arriba</b>."),
  E("Pasar 13 a binario","Dividimos por 2 hasta llegar a 0.",["13 ÷ 2 = 6, resto 1.","6 ÷ 2 = 3, resto 0.","3 ÷ 2 = 1, resto 1.","1 ÷ 2 = 0, resto 1.","Leemos los restos de abajo hacia arriba: 1101₂. Comprobación: 8 + 4 + 1 = 13."]),
 ]),
],
"ejemplo_completo":{"titulo":"pasar 45 a binario","planteo":"Escribí el número 45 en el sistema binario y comprobá el resultado.","pasos":["45 ÷ 2 = 22, resto 1.","22 ÷ 2 = 11, resto 0.","11 ÷ 2 = 5, resto 1.","5 ÷ 2 = 2, resto 1.","2 ÷ 2 = 1, resto 0.","1 ÷ 2 = 0, resto 1.","Restos de abajo hacia arriba: 101101₂.","Comprobación: 32 + 8 + 4 + 1 = 45."]},
"ejemplo_incompleto":{"titulo":"pasar 26 a binario","planteo":"Escribí 26 en binario. Completá los espacios.","pasos":["26 ÷ 2 = 13, resto ___.","13 ÷ 2 = 6, resto 1.","6 ÷ 2 = 3, resto ___.","3 ÷ 2 = 1, resto 1.","1 ÷ 2 = 0, resto 1.","Restos de abajo hacia arriba: ___ ."]},
"ejemplo_solo":{"titulo":"pasar 37 a binario","planteo":"Escribí 37 en binario y comprobalo sumando los valores de los lugares."},
"tip":{"titulo":"Comprobá sumando","texto":"Después de pasar a binario, sumá los valores de los lugares con 1: tiene que darte el número original. Te acordás de los lugares si recitás 1, 2, 4, 8, 16, 32."},
"ojo":["Leer los restos de arriba hacia abajo: da el número al revés (13 daría 1011 en vez de 1101).","Usar la cifra 2 en binario: no existe; el 2 se escribe 10."],
"resumen":[{"titulo":"Sistema binario","texto":"2 cifras (0 y 1) y agrupamientos de a 2. Ej.: el 2 se escribe 10."},{"titulo":"Bit","texto":"Cada cifra binaria. Ej.: 101 tiene 3 bits."},{"titulo":"Valor de los lugares","texto":"Cada lugar vale el doble del anterior: 1, 2, 4, 8, 16…"},{"titulo":"Binario a decimal","texto":"Se suman los lugares con 1. Ej.: 1011₂ = 8 + 2 + 1 = 11."},{"titulo":"Decimal a binario","texto":"Dividir por 2 y leer los restos de abajo hacia arriba. Ej.: 13 = 1101₂."}],
"glosario":[{"palabra":"Binario","significado":"Sistema que usa solo las cifras 0 y 1."},{"palabra":"Bit","significado":"Cada cifra de un número binario."},{"palabra":"Resto","significado":"Lo que sobra al dividir y no alcanza para otro grupo."},{"palabra":"Cociente","significado":"El resultado entero de una división."},{"palabra":"Subíndice","significado":"El numerito chico (₂) que indica en qué sistema está escrito el número."}],
"carpeta":["Pasá 1001₂ a decimal.","¿Cuánto vale el lugar de la 5.ª cifra contando desde la derecha en un número binario?","Pasá 20 a binario.","Un compañero escribió el 6 en binario como 101. ¿Cuál es el número binario correcto de 6?"],
"respuestas_carpeta":[["9"],["16"],["10100"],["110"]],
"soluciones":{"incompleto":"26 ÷ 2: resto 0. 6 ÷ 2: resto 0. Resultado: 11010₂.","solo":"37 ÷ 2 = 18 r1; 18 ÷ 2 = 9 r0; 9 ÷ 2 = 4 r1; 4 ÷ 2 = 2 r0; 2 ÷ 2 = 1 r0; 1 ÷ 2 = 0 r1. Resultado: 100101₂. Comprobación: 32 + 4 + 1 = 37.","carpeta":["9: 8 + 1.","16: los lugares valen 1, 2, 4, 8, 16.","10100: 20 ÷ 2 = 10 r0; 10 ÷ 2 = 5 r0; 5 ÷ 2 = 2 r1; 2 ÷ 2 = 1 r0; 1 ÷ 2 = 0 r1. Comprobación: 16 + 4 = 20.","110: 6 = 4 + 2. El 101 es el 5 (4 + 1)."]}
}

# ---------------- NIVEL 3: sexagesimal ----------------
OUT[3]={
"objetivo":"Vas a poder explicar cómo funciona el sistema sexagesimal y operar con horas, minutos y segundos, y con ángulos en grados.",
"vas_a_ver":["Qué es el sistema sexagesimal y dónde lo usamos","Cómo se agrupa de a 60: segundos, minutos y horas","Los grados, minutos y segundos de un ángulo","Cómo pasar de horas a minutos y de minutos a horas","Cómo sumar tiempos haciendo canjes"],
"secciones":[
 S(1,"El sistema sexagesimal",[
  D("Sistema sexagesimal","El <b>sistema sexagesimal</b> se <b>agrupa de a 60</b>: cada vez que juntás 60 de una unidad, la cambiás por 1 de la unidad siguiente. Lo usamos para medir el tiempo y los ángulos."),
  T("Cómo se agrupa el tiempo",["Si juntás","Formás","Se escribe"],[["60 segundos","1 minuto","60 s = 1 min"],["60 minutos","1 hora","60 min = 1 h"]],"Un tiempo se escribe con las unidades en orden: 3 h 25 min 40 s significa 3 horas, 25 minutos y 40 segundos."),
  P("Es distinto del decimal: en el decimal agrupás de a 10; acá, de a 60. Por eso 75 minutos no se pueden dejar así: son 1 hora y 15 minutos."),
 ]),
 S(1,"Ángulos: grados, minutos y segundos",[
  D("Medida de ángulos","Los ángulos también se miden en sexagesimal: <b>1 grado (1°) = 60 minutos (60′)</b> y <b>1 minuto = 60 segundos (60″)</b>."),
  E("Leer un ángulo","Interpretamos 35° 20′ 10″.",["35° son 35 grados.","20′ son 20 minutos de grado (no minutos de tiempo).","10″ son 10 segundos de grado.","Se agrupa igual que el tiempo: 60″ forman 1′ y 60′ forman 1°."]),
 ]),
 S(2,"Pasar de una unidad a otra",[
  P("<b>De horas a minutos:</b> multiplicás las horas por 60 y sumás los minutos. <b>De minutos a horas:</b> dividís por 60; el cociente son las horas y el resto, los minutos."),
  E("Pasajes de horas y minutos","Resolvemos dos pasajes.",["2 h 15 min = 2 × 60 + 15 = 120 + 15 = 135 min.","170 min ÷ 60 = 2, resto 50. Entonces 170 min = 2 h 50 min."]),
 ]),
 S(2,"Sumar tiempos con canje",[
  P("Se suma cada unidad por separado. Si los minutos (o los segundos) llegan a 60 o más, <b>canjeás</b>: cada 60 forma 1 de la unidad siguiente."),
  E("Sumar 1 h 45 min + 2 h 30 min","Sumamos columna por columna.",["Horas: 1 + 2 = 3 h.","Minutos: 45 + 30 = 75 min.","75 min es más que 60: 75 = 60 + 15, o sea 1 h 15 min.","Total: 3 h + 1 h 15 min = 4 h 15 min."]),
 ]),
],
"ejemplo_completo":{"titulo":"sumar 3 h 50 min + 2 h 40 min","planteo":"Sumá los dos tiempos y escribí el resultado con minutos menores que 60.","pasos":["Horas: 3 + 2 = 5 h.","Minutos: 50 + 40 = 90 min.","90 min = 60 min + 30 min = 1 h 30 min.","Total: 5 h + 1 h 30 min = 6 h 30 min.","Comprobación en minutos: 230 min + 160 min = 390 min = 6 × 60 + 30 = 6 h 30 min."]},
"ejemplo_incompleto":{"titulo":"1 h 45 min + 2 h 35 min","planteo":"Sumá los tiempos. Completá los espacios.","pasos":["Horas: 1 + 2 = ___ h.","Minutos: 45 + 35 = ___ min.","80 min = 1 h 20 min.","Total: 3 h + 1 h 20 min = ___ h 20 min."]},
"ejemplo_solo":{"titulo":"4 h 25 min 50 s + 1 h 40 min 30 s","planteo":"Sumá los dos tiempos. Empezá por los segundos y canjeá cuando haga falta."},
"tip":{"titulo":"Empezá por la unidad más chica","texto":"Al sumar tiempos, arrancá por los segundos, después los minutos y al final las horas: los canjes se van pasando de a una unidad hacia la izquierda."},
"ojo":["Dejar 75 minutos sin canjear: hay que escribir 1 h 15 min.","Usar 100 como si fuera el grupo: acá el grupo es de 60, no de 10."],
"resumen":[{"titulo":"Sistema sexagesimal","texto":"Se agrupa de a 60. Ej.: 60 min = 1 h."},{"titulo":"Tiempo","texto":"Horas, minutos y segundos. Ej.: 3 h 25 min 40 s."},{"titulo":"Ángulos","texto":"Grados, minutos y segundos: 1° = 60′ y 1′ = 60″."},{"titulo":"Horas a minutos","texto":"Se multiplica por 60. Ej.: 2 h 15 min = 135 min."},{"titulo":"Canje","texto":"60 minutos pasan a 1 hora. Ej.: 75 min = 1 h 15 min."}],
"glosario":[{"palabra":"Sexagesimal","significado":"Sistema que se agrupa de a 60."},{"palabra":"Canje","significado":"Cambiar un grupo completo por 1 unidad del orden siguiente."},{"palabra":"Grado","significado":"Unidad con la que se mide un ángulo (°)."},{"palabra":"Minuto de grado","significado":"La sesenta parte de un grado (′)."},{"palabra":"Segundo","significado":"La sesenta parte de un minuto (s o ″)."}],
"carpeta":["¿Cuántos minutos son 3 h?","Escribí 135 min en horas y minutos.","Sumá 2 h 50 min + 1 h 20 min.","Un compañero sumó 1 h 45 min + 30 min y escribió 1 h 75 min. Escribí el resultado correcto."],
"respuestas_carpeta":[["180"],["2 h 15 min","2h15min","2 h 15 minutos","2:15"],["4 h 10 min","4h10min","4 h 10 minutos","4:10"],["2 h 15 min","2h15min","2 h 15 minutos","2:15"]],
"soluciones":{"incompleto":"Horas: 3. Minutos: 80. Total: 4 h 20 min.","solo":"Segundos: 50 + 30 = 80 s = 1 min 20 s. Minutos: 25 + 40 + 1 = 66 min = 1 h 6 min. Horas: 4 + 1 + 1 = 6 h. Total: 6 h 6 min 20 s.","carpeta":["180 min: 3 × 60.","2 h 15 min: 135 ÷ 60 = 2, resto 15.","4 h 10 min: horas 3 y minutos 70 = 1 h 10 min.","2 h 15 min: 45 + 30 = 75 min = 1 h 15 min."]}
}

# ---------------- NIVEL 4: potencias de 10 ----------------
OUT[4]={
"objetivo":"Vas a poder escribir y leer potencias de 10, y usarlas para escribir números grandes de forma corta.",
"vas_a_ver":["Qué es una potencia: base y exponente","Las potencias de 10: un 1 seguido de ceros","Los nombres de los números grandes","Multiplicar un número por una potencia de 10","Escribir un número grande con potencias de 10"],
"secciones":[
 S(1,"Qué es una potencia",[
  D("Potencia","Una <b>potencia</b> es una multiplicación de un mismo número por sí mismo varias veces. El número que se repite es la <b>base</b> y las veces que se repite es el <b>exponente</b>, que se escribe arriba y chiquito."),
  E("Leer una potencia","Interpretamos 10³.",["La base es 10 y el exponente es 3.","10³ = 10 × 10 × 10.","10 × 10 = 100 y 100 × 10 = 1.000. Entonces 10³ = 1.000."]),
 ]),
 S(1,"Las potencias de 10",[
  D("Potencia de 10","Una <b>potencia de 10</b> es un 10 elevado a un exponente. El resultado es un <b>1 seguido de tantos ceros como indica el exponente</b>."),
  T("Potencias de 10",["Potencia","Cuenta","Número","Se lee"],[["10¹","10","10","diez"],["10²","10 × 10","100","cien"],["10³","10 × 10 × 10","1.000","mil"],["10⁴","10 × 10 × 10 × 10","10.000","diez mil"],["10⁵","10 × 10 × 10 × 10 × 10","100.000","cien mil"],["10⁶","10 × 10 × 10 × 10 × 10 × 10","1.000.000","un millón"]],"Mirá la columna del medio: el exponente es la cantidad de ceros del número."),
 ]),
 S(2,"Multiplicar por una potencia de 10",[
  P("Para multiplicar un número por 10ⁿ, le agregás <b>n ceros</b> a la derecha: es lo mismo que pasar cada cifra n lugares hacia la izquierda."),
  E("Multiplicar por potencias de 10","Resolvemos tres cuentas.",["35 × 10² = 35 × 100 = 3.500 (dos ceros).","8 × 10⁴ = 8 × 10.000 = 80.000 (cuatro ceros).","27 × 10⁶ = 27.000.000 (seis ceros)."]),
 ]),
 S(2,"Números grandes con potencias",[
  P("Con potencias de 10 podés escribir un número grande de forma corta, y también <b>descomponerlo</b> como en el sistema decimal, pero con potencias."),
  E("Escribir 4.205 y 7.000.000","Usamos potencias de 10.",["4.205 = 4 × 10³ + 2 × 10² + 0 × 10¹ + 5 = 4.000 + 200 + 0 + 5.","7.000.000 = 7 × 1.000.000 = 7 × 10⁶."]),
 ]),
],
"ejemplo_completo":{"titulo":"escribir 6.300.000 con potencias de 10","planteo":"Escribí 6.300.000 de dos formas: con una sola potencia y descompuesto.","pasos":["6.300.000 es 63 seguido de cinco ceros: 63 × 100.000.","100.000 = 10⁵. Entonces 6.300.000 = 63 × 10⁵.","Descompuesto: 6.300.000 = 6.000.000 + 300.000.","6.000.000 = 6 × 10⁶ y 300.000 = 3 × 10⁵.","Entonces 6.300.000 = 6 × 10⁶ + 3 × 10⁵.","Comprobación: 63 × 100.000 = 6.300.000."]},
"ejemplo_incompleto":{"titulo":"2.400.000","planteo":"Escribí 2.400.000 con potencias de 10. Completá los espacios.","pasos":["2.400.000 es 24 seguido de ___ ceros.","Entonces 2.400.000 = 24 × 10⁵.","Descompuesto: 2.000.000 + 400.000.","2.000.000 = 2 × 10 con exponente ___ y 400.000 = 4 × 10⁵.","Entonces 2.400.000 = 2 × 10⁶ + 4 × 10⁵."]},
"ejemplo_solo":{"titulo":"40.800.000","planteo":"Escribí 40.800.000 de dos formas: con una sola potencia y descompuesto en dos sumandos."},
"tip":{"titulo":"Contá los ceros","texto":"Para saber el exponente de una potencia de 10, contá los ceros que tiene el número. Para escribir una potencia, hacé el camino inverso: escribí un 1 y agregá tantos ceros como diga el exponente."},
"ojo":["Pensar que 10³ es 10 × 3 = 30: el exponente cuenta cuántos 10 se multiplican entre sí.","Contar mal los ceros: 100.000 tiene cinco ceros, o sea 10⁵ (no 10⁶)."],
"resumen":[{"titulo":"Potencia","texto":"Base multiplicada por sí misma tantas veces como diga el exponente. Ej.: 10³ = 10 × 10 × 10."},{"titulo":"Potencia de 10","texto":"Un 1 seguido de tantos ceros como el exponente. Ej.: 10⁵ = 100.000."},{"titulo":"Por 10ⁿ","texto":"Se agregan n ceros. Ej.: 35 × 10² = 3.500."},{"titulo":"Números grandes","texto":"Se escriben cortos con potencias. Ej.: 7.000.000 = 7 × 10⁶."},{"titulo":"Un millón","texto":"Equivale a 10⁶ = 1.000.000."}],
"glosario":[{"palabra":"Potencia","significado":"Multiplicación de un mismo número por sí mismo varias veces."},{"palabra":"Base","significado":"El número que se multiplica por sí mismo."},{"palabra":"Exponente","significado":"El numerito chico que dice cuántas veces se multiplica la base."},{"palabra":"Millón","significado":"Mil veces mil: 1.000.000."},{"palabra":"Descomponer","significado":"Escribir un número como suma de partes."}],
"carpeta":["Escribí 10⁵ como número.","Calculá 9 × 10⁴.","Escribí como número: 3 × 10⁶ + 5 × 10³.","Un compañero dice que 10³ = 30. ¿Cuánto vale realmente 10³?"],
"respuestas_carpeta":[["100000"],["90000"],["3005000"],["1000"]],
"soluciones":{"incompleto":"24 seguido de 5 ceros. 2.000.000 = 2 × 10⁶. Resultado: 2.400.000 = 24 × 10⁵ = 2 × 10⁶ + 4 × 10⁵.","solo":"40.800.000 = 408 × 10⁵ (408 seguido de cinco ceros). Descompuesto: 40.000.000 + 800.000 = 4 × 10⁷ + 8 × 10⁵.","carpeta":["100.000: un 1 con cinco ceros.","90.000: 9 × 10.000.","3.005.000: 3.000.000 + 5.000.","1.000: 10 × 10 × 10. Con 10 × 3 = 30 se confunde el exponente con una multiplicación."]}
}

# respuestas del nivel 1 (la carpeta ya trae soluciones)
OUT[1]['respuestas_carpeta']=[["40382"],["6000"],["800000+400+9","3"],["60"]]
OUT[1]['soluciones']['carpeta'][2]="800.000 + 400 + 9: tiene 3 sumandos. Respuesta: 3."
OUT[1]['carpeta'][2]="Descomponé 800.409 de forma aditiva y contá cuántos sumandos tiene. ¿Cuántos son?"

for k,v in OUT.items(): json.dump(v,open(f'c{k}.json','w'),ensure_ascii=False)
metas={1:"Sistema decimal y descomposición",2:"El sistema binario",3:"El sistema sexagesimal: horas y ángulos",4:"Potencias de 10 y números grandes"}
for k,v in OUT.items():
    json.dump({"meta":{"materia":"Matemática I","anio":1,"tema_num":1,"tema":"Sistemas numéricos","leccion_num":k,"titulo":metas[k]},"contenido":v},open(f'm{k}.json','w'),ensure_ascii=False)
