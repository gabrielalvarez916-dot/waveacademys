# Arreglos de Matemática I M1-M8 y M10 (26/11/2026): textos copiados, relleno y pantallas que repetían práctica.
import sys, json; sys.path.insert(0, 'tools/interactiva'); from armar import *
def T_(M,n,i): return M['niveles'][n]['leccion']['temas'][i]
def put(M,n,i,defi=None,par=None,lista=None,ej=None,ex=None,tit=None):
  t=T_(M,n,i); E=t['explicacion']
  for b in E:
    if b['tipo']=='definicion' and defi: b['texto']=defi
    if b['tipo']=='parrafo' and par: b['texto']=par
    if b['tipo']=='lista' and lista: b['items']=lista
  if ej: t['ejemplo']=ej
  if ex: t['ejercicio']=ex
  if tit: t['titulo']=tit
def quitar(M,n,i,a_lista=None,destino=0):
  t=M['niveles'][n]['leccion']['temas'].pop(i)
  if a_lista:
    for b in M['niveles'][n]['leccion']['temas'][destino]['explicacion']:
      if b['tipo']=='lista': b['items'].append(a_lista)
def m1(M):
  put(M,'1',1,defi="Un número largo se lee partiéndolo en grupos de tres cifras, contando de derecha a izquierda. Cada grupo tiene un nombre: unidades, miles, millones y miles de millones.",par="Partido así, el número largo se vuelve una serie de números cortos: cada grupo se dice como un número de hasta tres cifras, seguido del nombre de su grupo. Por ejemplo, 3.040.500 se lee «tres millones cuarenta mil quinientos». Para escribirlo con cifras se hace al revés, poniendo ceros en los lugares que no se nombran.")
  put(M,'4',0,defi="En el sistema sexagesimal las unidades se juntan de a 60: 60 segundos hacen un minuto y 60 minutos hacen una hora. Con él medimos el tiempo y también los ángulos.",par="Se usa 60 porque se reparte en partes iguales de muchas maneras: la mitad, la tercera, la cuarta o la sexta parte de una hora son siempre una cantidad entera de minutos. Para cambiar de unidad se multiplica por 60 al bajar a una unidad más chica y se divide por 60 al subir a una más grande.")
guardar('contenido/matematica-1/mision-1/mision-1.json',ajustes=m1)
def m2(M):
  put(M,'1',0,defi="La suma tiene dos propiedades muy útiles: se pueden cambiar de lugar los sumandos (conmutativa) y se pueden agrupar como uno quiera (asociativa), sin que cambie el resultado.",par="Gracias a ellas se puede sumar en el orden que más convenga. En 37 + 48 + 63, juntar primero 37 y 63 da 100, y después sumar 48 es muy fácil. La resta, en cambio, no las cumple: 9 − 4 da 5, pero 4 − 9 no da lo mismo.")
  put(M,'1',1,defi="Sumar y restar son operaciones inversas: una deshace lo que hace la otra. Si 25 + 17 = 42, entonces 42 − 17 = 25 y 42 − 25 = 17.",par="Por eso, para controlar una resta se suma el resultado con lo que se restó y tiene que dar el número del principio. Y para encontrar un número que falta en una suma, como en 25 + ▢ = 42, se resta: 42 − 25 = 17.")
  put(M,'3',0,defi="Dividir es repartir en partes iguales o averiguar cuántas veces entra un número en otro. En una división hay cuatro números: el dividendo, el divisor, el cociente y el resto.",par="Si 47 caramelos se reparten entre 5 chicos, a cada uno le tocan 9 y sobran 2: 47 es el dividendo, 5 el divisor, 9 el cociente y 2 el resto. El resto tiene que ser más chico que el divisor, porque si sobraran 5 o más, todavía alcanzaría para darle uno más a cada uno.")
  T_(M,'3',1)['ejercicio']={"motor":"naturales_x","p":{"modo":"relacion"}}; T_(M,'3',2)['ejercicio']={"motor":"naturales_x","p":{"modo":"falta"}}
guardar('contenido/matematica-1/mision-2/mision-2.json',ajustes=m2)
def m4(M):
  put(M,'1',2,defi="Un término es cada parte del cálculo que queda separada por un signo + o − que no está dentro de un paréntesis. Cada término se resuelve aparte y al final se suman o restan los resultados.",par="Marcar los términos antes de empezar ordena el trabajo: en 4 × 3 + 12 ÷ 2 − 5 hay tres términos, que dan 12, 6 y 5, y el resultado es 12 + 6 − 5 = 13. Un término formado por un solo número queda como está hasta el final.")
  put(M,'2',0,defi="Los paréntesis marcan qué parte del cálculo se resuelve primero, aunque adentro haya una suma o una resta. Lo que está entre paréntesis se trata como una cuenta separada que se hace antes que todo lo demás.")
  quitar(M,'3',2,"Al terminar, conviene verificar rehaciendo el cálculo o estimando el resultado.",0)
guardar('contenido/matematica-1/mision-4/mision-4.json',ajustes=m4)
def m5(M):
  quitar(M,'1',1)
  put(M,'1',1,tit="Cuándo vuelven a coincidir",defi="Cuando un mismo número aparece a la vez en la tabla de uno y en la tabla de otro, se lo llama múltiplo común de los dos. Sirve para saber cuándo vuelven a coincidir dos cosas que se repiten cada cierto tiempo.",par="Imaginá dos luces de un árbol de Navidad: una se prende cada 4 segundos y la otra cada 6, y arrancan juntas. Vuelven a encenderse a la vez a los 12 segundos, después a los 24 y a los 36, que son los números que están en la tabla del 4 y también en la del 6. Escribir las dos listas una debajo de la otra hace fácil ver dónde coinciden.",lista=["Las luces coinciden a los 12, 24 y 36 segundos.","Con 3 y 5 coincidirían a los 15, 30 y 45."])
guardar('contenido/matematica-1/mision-5/mision-5.json',ajustes=m5)
def m6(M):
  put(M,'1',1,defi="Para saber si un número se puede dividir por 3 o por 9 sin hacer la división, se suman sus cifras: si la suma es múltiplo de 3, el número es divisible por 3; si es múltiplo de 9, por 9.",par="Funciona porque 10, 100 y 1.000 dejan siempre resto 1 al dividirlos por 3 o por 9, así que cada cifra aporta solo su propio valor. Con 4.572, las cifras suman 18, y como 18 es múltiplo de 9, el número es divisible por 3 y por 9. Si la suma queda grande, se vuelven a sumar sus cifras.")
  put(M,'2',1,defi="Un número es divisible por 6 cuando es divisible por 2 y por 3 a la vez. Se puede combinar así porque 6 = 2 × 3 y el 2 y el 3 no tienen divisores en común.",par="La misma idea sirve para otros divisores compuestos: para el 15 se usan los criterios del 3 y del 5, y para el 10, los del 2 y del 5. Hay que usar factores que no tengan divisores comunes: que un número sea divisible por 2 y por 4 no asegura que lo sea por 8, como pasa con el 12.")
  put(M,'3',0,defi="La criba de Eratóstenes es una forma de encontrar todos los números primos hasta cierto número: se van tachando los múltiplos de cada primo y los que quedan sin tachar son primos.",par="Primero se arma una tabla con los números a partir del 2. Se deja el 2 y se borran todos los que están en su tabla de multiplicar; el primer número que sobrevive es el 3, y se borran los de su tabla; después se sigue con el 5 y con el 7. Lleva el nombre de un matemático griego que vivió hace más de dos mil años, y sigue siendo útil.")
  T_(M,'3',1)['ejercicio']={"motor":"factores_x","p":{"modo":"cuantos"}} if False else T_(M,'3',1)['ejercicio']
  quitar(M,'3',1,"Para saber si un número es primo alcanza con probar dividirlo por los primos cuyo cuadrado no lo supere.",0)
  quitar(M,'4',1,"La descomposición en factores primos de un número es siempre la misma, sin importar por qué divisor se empiece.",0)
guardar('contenido/matematica-1/mision-6/mision-6.json',ajustes=m6)
def m7(M):
  for n in ('1','2'):
    for b in T_(M,n,0)['explicacion']:
      if b['tipo'] in ('definicion','parrafo'): b['texto']=b['texto'].replace(' Se escribe MCD(a, b).',' Se escribe MCD(a, b), por ejemplo MCD(12, 18) = 6.').replace(' Se escribe MCM(a, b).',' Se escribe MCM(a, b), por ejemplo MCM(4, 6) = 12.')
  T_(M,'1',1)['ejercicio']={"motor":"mcd_guiado","p":{}}
  T_(M,'2',1)['ejercicio']={"motor":"factores_x","p":{"modo":"producto"}}
  T_(M,'2',2)['ejercicio']={"motor":"mcd_mcm_problemas","p":{}}
  quitar(M,'4',1,"En los problemas mixtos, primero se decide si se busca algo más chico que los datos (MCD) o más grande (MCM).",0)
guardar('contenido/matematica-1/mision-7/mision-7.json',ajustes=m7)
def m8(M):
  put(M,'1',2,defi="Si el numerador es más chico que el denominador, la fracción es propia y vale menos que un entero. Si es igual o más grande, es impropia y vale un entero o más, y se puede escribir como número mixto.",par="Para escribir 11/4 como número mixto se piensa cuántos enteros de cuatro cuartos se pueden armar con once cuartos: se arman dos, que usan ocho, y sobran tres cuartos. Por eso 11/4 = 2 3/4. Es lo mismo que dividir 11 por 4: el cociente son los enteros y el resto, los cuartos que sobran.")
  quitar(M,'4',2,"Para ordenar varias fracciones, primero se separan con los referentes 1/2 y 1, y después se comparan con un denominador común.",0)
guardar('contenido/matematica-1/mision-8/mision-8.json',ajustes=m8)
def m10(M):
  for b in T_(M,'2',2)['explicacion']:
    if b['tipo']=='parrafo': b['texto']=b['texto'].replace(' Al final se simplifica.',' Al final la fracción se simplifica hasta que quede irreducible.')
guardar('contenido/matematica-1/mision-10/mision-10.json',ajustes=m10)
