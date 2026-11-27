# -*- coding: utf-8 -*-
"""Ciencias Sociales Integradas I · Lengua y Literatura I · Misión 6 (El fantasma de Canterville, primera parte) y Misión 7 (Ortografía en uso)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}
SID = "e1b0726d-08aa-4d9e-9060-18489f529da2"

# ================= MISIÓN 6: EL FANTASMA DE CANTERVILLE (primera parte) =================
A1=NV("Vas a reconocer el escenario, los personajes y el conflicto de los primeros capítulos de «El fantasma de Canterville», de Oscar Wilde.",["Un castillo con historia","Los personajes","El narrador","El conflicto inicial"],[
 S(1,"El cuento",[P("«El fantasma de Canterville» es un relato de Oscar Wilde (1887). Una familia estadounidense, los Otis, compra un castillo inglés, Canterville Chase, aunque su dueño les advierte que está embrujado."),D("Relato gótico","Historia de misterio y terror que suele ocurrir en castillos antiguos, con fantasmas y secretos. Wilde usa sus elementos para jugar con ellos.")]),
 S(1,"Los personajes",[T("Quiénes son",["Personaje","Cómo es"],[["Lord Canterville","El dueño; avisa del fantasma y no quiere comprometerse"],["Los Otis","Familia práctica y moderna: no creen en fantasmas"],["Sir Simon","El fantasma del castillo; quiere asustar y se toma muy en serio"],["Virginia","La hija de los Otis; sensible y amable"]])]),
 S(2,"El narrador",[D("Narrador omnisciente","Narra en tercera persona y conoce los pensamientos y sentimientos de todos los personajes."),P("Por eso sabemos lo que siente el fantasma aunque los demás no lo vean.")]),
 S(2,"El conflicto",[P("El conflicto surge del choque entre dos mundos: un fantasma que representa la <b>tradición antigua</b> y una familia que representa la <b>mentalidad práctica y moderna</b>. Se dice que Sir Simon cometió un crimen hace siglos y que una mancha de sangre del suelo no se borra.")])],
 {"titulo":"identificar","planteo":"¿Por qué es un problema para el fantasma que los Otis no crean en fantasmas?","pasos":["El fantasma vive de asustar.","Si nadie se asusta, no logra su objetivo.","Ese es el conflicto central."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El autor del cuento es Oscar ___ .","El narrador que cuenta en tercera persona y sabe todo es ___ ."]},
 {"titulo":"tu turno","planteo":"Describí en tu carpeta en dos oraciones cómo es la familia Otis y cómo es el fantasma."},
 {"titulo":"Dos mundos","texto":"Para entender el conflicto, preguntate qué quiere cada personaje y qué lo frena."},
 ["Pensar que es un cuento de terror común.","Confundir al narrador con un personaje."],
 RS(("Autor","Oscar Wilde."),("Escenario","Un castillo inglés."),("Personajes","Los Otis y Sir Simon."),("Conflicto","Tradición contra practicidad.")),
 G(("Gótico","Género de misterio con castillos y fantasmas."),("Omnisciente","Que lo sabe todo."),("Embrujado","Que tiene un fantasma."),("Tradición","Costumbres del pasado.")),
 ["¿Cómo se llama el fantasma?","¿Qué familia compra el castillo?","¿De qué nacionalidad es la familia Otis?","¿El narrador cuenta en primera o en tercera persona?"],
 [["sir simon","simon","simón","sir simón","sir simon de canterville"],["los otis","otis","la familia otis"],["estadounidense","americana","norteamericana","de estados unidos"],["tercera","tercera persona","en tercera"]],
 {"incompleto":"Wilde. Omnisciente.","solo":"Los Otis son prácticos y no creen en fantasmas; Sir Simon es tradicional y quiere asustar.","carpeta":["Sir Simon.","Los Otis.","Estadounidense.","En tercera persona."]})
A2=NV("Vas a ordenar las escenas, reconocer causas y consecuencias y explicar cómo se siente el fantasma.",["Una secuencia de intentos","Causa y consecuencia","Cómo se siente el fantasma"],[
 S(1,"Intentos y respuestas",[T("Lo que intenta el fantasma y cómo responde la familia",["El fantasma...","La familia..."],[["Hace sonar sus cadenas","El señor Otis le ofrece aceite para engrasarlas"],["Deja una mancha de sangre en el suelo","Washington la limpia con un quitamanchas"],["Aparece de noche con un aspecto horrible","Los gemelos le tiran almohadas"]])]),
 S(1,"Causa y consecuencia",[D("Causa","Lo que provoca que algo pase."),D("Consecuencia","Lo que pasa a raíz de una causa."),E("Un ejemplo","La mancha vuelve a aparecer y Washington vuelve a borrarla.",["Causa: el fantasma renueva la mancha.","Consecuencia: la familia la limpia otra vez.","Efecto: el fantasma queda cada vez más desesperado."])]),
 S(2,"Sentimientos",[P("Aunque es un fantasma, Sir Simon se siente <b>humillado</b>, cansado y herido en su orgullo: lleva siglos asustando y ahora nadie le tiene miedo. Eso lo vuelve un personaje gracioso y a la vez un poco triste.")])],
 {"titulo":"encadenar","planteo":"Ordená: a) La familia limpia la mancha. b) El fantasma deja una mancha. c) El fantasma se siente humillado.","pasos":["b: primero ocurre el intento del fantasma.","a: la familia responde limpiando.","c: por eso el fantasma queda humillado."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Lo que provoca que algo pase es la ___ .","El fantasma se siente ___ porque nadie le tiene miedo."]},
 {"titulo":"tu turno","planteo":"Escribí una causa y una consecuencia de lo que le pasa al fantasma."},
 {"titulo":"Porque... entonces","texto":"Para encontrar causas y consecuencias, probá unir las oraciones con \"porque\" y \"entonces\"."},
 ["Confundir la causa con la consecuencia.","Creer que el fantasma no siente nada."],
 RS(("Secuencia","Intento y respuesta."),("Causa","Lo que provoca."),("Consecuencia","Lo que ocurre después."),("Fantasma","Humillado.")),
 G(("Causa","Motivo por el que pasa algo."),("Consecuencia","Resultado de lo que pasó antes."),("Humillado","Que siente que lo ridiculizaron.")),
 ["¿Con qué limpia Washington la mancha de sangre?","¿Qué le ofrece el señor Otis al fantasma para sus cadenas ruidosas?","¿Quiénes le arrojan almohadas?","El fantasma, ¿se siente orgulloso o humillado?"],
 [["quitamanchas","con un quitamanchas","un quitamanchas","limpiador","con un limpiador"],["aceite","lubricante","aceite para las cadenas"],["los gemelos","gemelos","los hermanos gemelos"],["humillado","humillado."]],
 {"incompleto":"Causa. Humillado.","solo":"Causa: nadie le tiene miedo. Consecuencia: se siente humillado.","carpeta":["Con un quitamanchas.","Aceite.","Los gemelos.","Humillado."]})
A3=NV("Vas a reconocer el humor y la ironía en el cuento y explicar cómo se logran.",["Qué es la ironía","El humor por contraste","La exageración","Una parodia"],[
 S(1,"Ironía",[D("Ironía","Decir o mostrar algo que significa lo contrario de lo que se espera o de lo que se dice, generalmente para burlarse o para señalar algo."),P("En el cuento, la ironía aparece cuando la familia trata al fantasma con una calma práctica, como si fuera un problema doméstico más.")]),
 S(1,"Contraste",[T("Qué se espera y qué ocurre",["Se espera...","Ocurre..."],[["Que la familia huya aterrada","Le ofrecen aceite para las cadenas"],["Que el fantasma sea imponente","Se siente ridículo y cansado"],["Que la mancha sea un misterio","La limpian con un producto de limpieza"]])]),
 S(2,"Exageración y parodia",[P("Wilde <b>exagera</b> los hechos para hacernos reír: un fantasma que se preocupa por su actuación, como un actor. El cuento es una <b>parodia</b> del género gótico: imita sus elementos (castillo, fantasma, mancha de sangre) pero para burlarse de ellos.")]),
 S(2,"Dos culturas",[P("El humor también viene del choque entre la tradición europea del fantasma y la mentalidad práctica de la familia estadounidense.")])],
 {"titulo":"explicar","planteo":"¿Por qué resulta gracioso que el señor Otis ofrezca aceite al fantasma?","pasos":["Se espera miedo y reacciona con practicidad.","Trata el terror como un problema común.","Esa distancia entre lo esperado y lo que pasa produce humor e ironía."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Imitar un género para burlarse de él es una ___ .","Exagerar los hechos sirve para generar ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un momento del cuento que te parezca gracioso y explicá cómo se logra el humor."},
 {"titulo":"Esperado contra real","texto":"Para encontrar la ironía, compará lo que se espera con lo que ocurre."},
 ["Pensar que la ironía es mentir.","Creer que el humor del cuento es solo burla."],
 RS(("Ironía","Lo contrario de lo esperado."),("Contraste","Choque entre dos cosas."),("Exageración","Hace reír."),("Parodia","Imita para burlarse.")),
 G(("Ironía","Expresar lo contrario de lo esperado."),("Parodia","Imitación que se burla."),("Contraste","Diferencia entre dos cosas.")),
 ["Imitar un género para burlarse de él es una…","Cuando lo que ocurre es lo contrario de lo esperado, hay…","¿Qué género de historias parodia el cuento: el gótico o el policial?","Exagerar los hechos, ¿sirve para generar humor? Respondé sí o no."],
 [["parodia","una parodia"],["ironia","ironía","hay ironia","hay ironía"],["gotico","gótico","el gótico","el gotico"],["si","sí"]],
 {"incompleto":"Parodia. Humor.","solo":"El fantasma se esfuerza por asustar y se toma tan en serio su actuación que resulta gracioso.","carpeta":["Parodia.","Ironía.","El gótico.","Sí."]})
A4=NV("Vas a distinguir hechos de opiniones y armar una opinión fundamentada sobre lo leído.",["Hecho y opinión","La estructura de una opinión","Argumentos con ejemplos","Conectores"],[
 S(1,"Hecho y opinión",[T("No son lo mismo",["","Hecho","Opinión"],[["Qué es","Algo que ocurre en el texto","Lo que yo pienso del texto"],["Ejemplo","El fantasma deja una mancha de sangre","El fantasma es un personaje simpático"]])]),
 S(1,"La estructura",[T("Partes de una opinión",["Parte","Qué hace"],[["Tesis","Dice lo que pienso"],["Argumentos","Explican por qué lo pienso"],["Ejemplos del texto","Prueban mis argumentos"],["Cierre","Resume y vuelve a la tesis"]])]),
 S(2,"Argumentar con el texto",[P("Una opinión vale más si se apoya en lo que dice el cuento. En lugar de \"es gracioso\", decí <b>por qué</b>: \"es gracioso porque la familia trata al fantasma como a un vecino ruidoso\".")]),
 S(2,"Conectores",[T("Para opinar",["Función","Conectores"],[["Opinar","en mi opinión, creo que, me parece que"],["Explicar","porque, ya que"],["Ejemplificar","por ejemplo, como cuando"],["Cerrar","por eso, en conclusión"]])])],
 {"titulo":"armar una opinión","planteo":"Opinión: «El fantasma es más gracioso que terrorífico».","pasos":["Tesis: me parece que el fantasma es más gracioso que terrorífico.","Argumento: porque se toma muy en serio y nadie le tiene miedo.","Ejemplo: como cuando le ofrecen aceite para sus cadenas.","Cierre: por eso el cuento hace reír en lugar de asustar."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Lo que pienso sobre un texto es mi ___ .","Para dar un ejemplo uso el conector ___ ejemplo."]},
 {"titulo":"tu turno","planteo":"Escribí tu opinión sobre el fantasma con una tesis, un argumento y un ejemplo del cuento."},
 {"titulo":"Opinión con prueba","texto":"Después de decir qué pensás, buscá una escena que lo pruebe."},
 ["Dar la opinión sin explicarla.","Mezclar un hecho con una opinión."],
 RS(("Hecho","Ocurre en el texto."),("Opinión","Lo que pienso."),("Estructura","Tesis, argumentos, ejemplos."),("Cierre","Vuelve a la tesis.")),
 G(("Tesis","Idea principal que se defiende."),("Argumento","Razón que apoya una opinión."),("Fundamentar","Apoyar con razones y ejemplos.")),
 ["\"El fantasma es simpático\", ¿es un hecho o una opinión?","¿Cómo se llama la idea principal que defendés en un texto de opinión?","¿Qué conector uso para dar un ejemplo?","¿Qué prueban mis argumentos: los ejemplos del texto o mis gustos?"],
 [["opinion","opinión","una opinion","una opinión"],["tesis","la tesis"],["por ejemplo"],["los ejemplos del texto","ejemplos del texto","los ejemplos","ejemplos"]],
 {"incompleto":"Opinión. Ejemplo.","solo":"Respuesta personal: me parece que..., porque..., por ejemplo..., por eso...","carpeta":["Una opinión.","La tesis.","Por ejemplo.","Los ejemplos del texto."]})
ACT6={"1":[{"t":"matching","p":"Uní cada personaje con su descripción.","o":{"izquierda":["Lord Canterville","Los Otis","Sir Simon","Virginia"],"derecha":["Dueño que avisa del fantasma","Familia práctica y moderna","Fantasma del castillo","Hija sensible y amable"]},"r":{"pares":{"Lord Canterville":"Dueño que avisa del fantasma","Los Otis":"Familia práctica y moderna","Sir Simon":"Fantasma del castillo","Virginia":"Hija sensible y amable"}},"e":"Cada personaje tiene su rol."},MC("Un narrador que cuenta en tercera persona y conoce los pensamientos de todos es…",["Omnisciente","Protagonista","Testigo","Ninguno"],"Omnisciente","Lo sabe todo.")],
 "2":[{"t":"ordering","p":"Ordená la secuencia.","o":["El fantasma se siente humillado","La familia limpia la mancha","El fantasma deja una mancha de sangre"],"r":{"orden":["El fantasma deja una mancha de sangre","La familia limpia la mancha","El fantasma se siente humillado"]},"e":"Intento, respuesta y consecuencia."},MC("¿Cómo se siente el fantasma ante la actitud de la familia?",["Humillado","Orgulloso","Aliviado","Indiferente"],"Humillado","Nadie le tiene miedo.")],
 "3":[{"t":"classify","p":"¿Qué se espera y qué ocurre?","o":{"elementos":["La familia huye aterrada","Le ofrecen aceite para las cadenas","El fantasma es imponente","El fantasma se siente ridículo"],"categorias":["Lo esperado","Lo que ocurre"]},"r":{"categorias":{"La familia huye aterrada":"Lo esperado","Le ofrecen aceite para las cadenas":"Lo que ocurre","El fantasma es imponente":"Lo esperado","El fantasma se siente ridículo":"Lo que ocurre"}},"e":"La ironía nace del contraste."},MC("El cuento imita elementos del género gótico para burlarse de ellos. Es una…",["Parodia","Biografía","Noticia","Fábula"],"Parodia","Imita para reírse.")],
 "4":[{"t":"classify","p":"¿Hecho u opinión?","o":{"elementos":["La familia compra el castillo","El fantasma es simpático","El fantasma deja una mancha","El cuento es muy divertido"],"categorias":["Hecho","Opinión"]},"r":{"categorias":{"La familia compra el castillo":"Hecho","El fantasma es simpático":"Opinión","El fantasma deja una mancha":"Hecho","El cuento es muy divertido":"Opinión"}},"e":"El hecho ocurre en el texto; la opinión es lo que pienso."},MC("¿Qué conector sirve para dar un ejemplo?",["Por ejemplo","En conclusión","Porque","Además"],"Por ejemplo","Introduce el ejemplo.")],
 "5":[MC("Relámpago. El autor del cuento es…",["Oscar Wilde","Edgar Allan Poe","Conan Doyle"],"Oscar Wilde","1887.",tiempo=20),MC("Relámpago. La ironía muestra algo…",["Contrario a lo esperado","Igual a lo esperado","Sin sentido"],"Contrario a lo esperado","Crea humor.",tiempo=20),MC("Relámpago. Una opinión necesita…",["Argumentos","Solo gritos","Nada"],"Argumentos","Y ejemplos.",tiempo=20),MC("Relámpago. En \"Mis primos llegaron tarde\", el sujeto es…",["Mis primos","llegaron","tarde"],"Mis primos","Se pregunta ¿quién?",tiempo=20)]}
EX6=[[1,MC("¿Cómo se llama el fantasma del cuento?",["Sir Simon","Lord Canterville","Washington","Virginia"],"Sir Simon","Es el fantasma de Canterville Chase.")],
 [1,MC("¿Quién es el autor?",["Oscar Wilde","Conan Doyle","Edgar Allan Poe","Julio Verne"],"Oscar Wilde","Lo escribió en 1887.")],
 [1,VF("El narrador cuenta en primera persona.","Falso","Narra en tercera persona omnisciente.")],
 [2,MC("¿Con qué limpia Washington la mancha?",["Un quitamanchas","Agua bendita","Fuego","Un hechizo"],"Un quitamanchas","Una solución práctica.")],
 [2,MC("La causa de la humillación del fantasma es…",["Que nadie le tiene miedo","Que lo atraparon","Que se perdió","Que se enfermó"],"Que nadie le tiene miedo","Eso hiere su orgullo.")],
 [2,VF("El fantasma se siente orgulloso de cómo reacciona la familia.","Falso","Se siente humillado.")],
 [3,MC("La ironía consiste en…",["Mostrar lo contrario de lo esperado","Decir siempre la verdad","Repetir una idea","Describir un paisaje"],"Mostrar lo contrario de lo esperado","Se usa para burlarse o señalar algo.")],
 [3,MC("El cuento es una parodia de…",["El género gótico","El género policial","La poesía épica","La noticia"],"El género gótico","Imita castillos, fantasmas y manchas.")],
 [3,VF("Exagerar los hechos puede generar humor.","Verdadero","Como el fantasma que se toma muy en serio.")],
 [4,MC("Una opinión se apoya en…",["Argumentos y ejemplos","Solo gustos","Nada","Una orden"],"Argumentos y ejemplos","Para convencer.")],
 [4,MC("\"El cuento es divertido\" es…",["Una opinión","Un hecho","Un título","Un diálogo"],"Una opinión","Depende de quien lee.")],
 [4,MC("Para dar un ejemplo uso…",["Por ejemplo","En conclusión","Entonces","Pero"],"Por ejemplo","Ejemplifica.")],
 [4,VF("Una opinión no necesita ninguna razón.","Falso","Se fundamenta con argumentos.")]]
M6={"subject_id":SID,"tema":6,"practica":"Práctica general: El fantasma de Canterville","examen_titulo":"Nivel jefe: El fantasma de Canterville","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT6,"examen":EX6}

# ================= MISIÓN 7: ORTOGRAFÍA EN USO =================
B1=NV("Vas a clasificar las palabras según su sílaba tónica y aplicar las reglas de tilde.",["Sílaba tónica","Agudas, graves y esdrújulas","Cuándo llevan tilde","Practicar"],[
 S(1,"La sílaba tónica",[D("Sílaba tónica","La que se pronuncia con más fuerza en una palabra."),P("En <b>ca-nción</b> la fuerte es <b>ción</b>; en <b>ár-bol</b>, <b>ár</b>; en <b>te-lé-fo-no</b>, <b>lé</b>.")]),
 S(1,"Tres clases",[T("Según dónde cae la fuerza",["Clase","Sílaba tónica","Ejemplo"],[["Aguda","La última","canción, papel, café"],["Grave","La penúltima","árbol, casa, lápiz"],["Esdrújula","La antepenúltima","teléfono, música, pájaro"]])]),
 S(2,"Reglas de tilde",[T("Cuándo llevan tilde",["Clase","Regla"],[["Aguda","Si termina en n, s o vocal: canción, compás, café"],["Grave","Si NO termina en n, s o vocal: árbol, lápiz, cárcel"],["Esdrújula","Siempre: teléfono, música"]]),P("Por eso <b>papel</b> (aguda terminada en l) no lleva tilde, y <b>casa</b> (grave terminada en vocal) tampoco.")])],
 {"titulo":"aplicar la regla","planteo":"¿Lleva tilde «arbol»?","pasos":["Se pronuncia ár-bol: la fuerza cae en la penúltima: es grave.","Termina en l, no en n, s ni vocal.","Entonces lleva tilde: árbol."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Las palabras con la fuerza en la última sílaba son ___ .","Las esdrújulas llevan tilde ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres palabras de cada clase (aguda, grave y esdrújula) y marcá la sílaba tónica."},
 {"titulo":"Primero la fuerza","texto":"Antes de poner tilde, decí la palabra en voz alta y buscá dónde cae la fuerza."},
 ["Poner tilde a todas las palabras que suenan fuerte.","Olvidar que las esdrújulas siempre llevan tilde."],
 RS(("Aguda","Última sílaba."),("Grave","Penúltima."),("Esdrújula","Antepenúltima."),("Tilde","Según la clase y la terminación.")),
 G(("Tilde","Signo que marca la sílaba tónica."),("Sílaba tónica","La que se pronuncia con más fuerza."),("Aguda","Palabra con fuerza en la última sílaba."),("Esdrújula","Palabra con fuerza en la antepenúltima sílaba.")),
 ["¿Cuál es la sílaba tónica de «canción»?","«Árbol», ¿es aguda, grave o esdrújula?","«Teléfono», ¿es aguda, grave o esdrújula?","«Papel», ¿lleva tilde? Respondé sí o no."],
 [["cion","ción","la ultima","la última"],["grave","es grave"],["esdrujula","esdrújula","es esdrujula","es esdrújula"],["no"]],
 {"incompleto":"Agudas. Siempre.","solo":"Aguda: café. Grave: árbol. Esdrújula: música.","carpeta":["Ción.","Grave.","Esdrújula.","No."]})
B2=NV("Vas a distinguir diptongos de hiatos y decidir cuándo llevan tilde.",["Vocales abiertas y cerradas","Diptongo","Hiato","Tilde en el hiato"],[
 S(1,"Vocales abiertas y cerradas",[T("Clases de vocales",["Clase","Vocales"],[["Abiertas (fuertes)","a, e, o"],["Cerradas (débiles)","i, u"]])]),
 S(1,"Diptongo",[D("Diptongo","Dos vocales juntas que se pronuncian en una sola sílaba."),P("Se forma con una abierta y una cerrada (<b>cuo-ta</b>, <b>pei-ne</b>) o con dos cerradas distintas (<b>ciu-dad</b>).")]),
 S(2,"Hiato",[D("Hiato","Dos vocales juntas que se pronuncian en sílabas distintas."),T("Casos",["Caso","Ejemplo"],[["Dos abiertas","le-er, ca-er, po-e-ta"],["Cerrada tónica + abierta","pa-ís, dí-a, rí-o"]])]),
 S(2,"Tilde",[P("El hiato con una vocal cerrada tónica <b>siempre lleva tilde</b> en la cerrada: país, día, río, baúl, reír. Los demás casos siguen las reglas generales.")])],
 {"titulo":"decidir","planteo":"¿«río» lleva tilde?","pasos":["Se separa en rí-o: dos sílabas.","Es hiato: i tónica y o abierta.","Lleva tilde en la i: río."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Dos vocales en la misma sílaba forman un ___ .","Una cerrada tónica con una abierta forma un ___ con tilde."]},
 {"titulo":"tu turno","planteo":"Escribí tres palabras con diptongo y tres con hiato."},
 {"titulo":"Separá en sílabas","texto":"Para saber si es diptongo o hiato, separá la palabra en sílabas y contá."},
 ["Poner tilde en un diptongo por costumbre.","Olvidar la tilde en país, día o río."],
 RS(("Abiertas","a, e, o."),("Cerradas","i, u."),("Diptongo","Una sílaba."),("Hiato","Dos sílabas.")),
 G(("Diptongo","Dos vocales en una sílaba."),("Hiato","Dos vocales en sílabas distintas."),("Vocal abierta","a, e, o."),("Vocal cerrada","i, u.")),
 ["«País», ¿tiene diptongo o hiato?","«Ciudad», ¿tiene diptongo o hiato?","«Río», ¿tiene diptongo o hiato?","«Reír», ¿lleva tilde? Respondé sí o no."],
 [["hiato","tiene hiato"],["diptongo","tiene diptongo"],["hiato","tiene hiato"],["si","sí"]],
 {"incompleto":"Diptongo. Hiato.","solo":"Diptongos: cuota, peine, ciudad. Hiatos: país, día, leer.","carpeta":["Hiato.","Diptongo.","Hiato.","Sí."]})
B3=NV("Vas a escribir con la letra correcta en los casos que más confunden.",["B y V","G y J","H","Palabras que se confunden"],[
 S(1,"B y V",[T("Reglas",["Regla","Ejemplo"],[["Se escriben con b los pretéritos en -aba","cantaba, jugaba"],["Con b antes de l y r","blanco, brazo"],["Con v el presente de ir","voy, vas, va"]])]),
 S(1,"G y J",[T("Reglas",["Regla","Ejemplo"],[["Verbos terminados en -ger y -gir llevan g","coger, elegir"],["Excepciones: tejer, crujir","tejer, crujir"]])]),
 S(2,"La H",[P("La <b>h</b> no suena, pero se escribe. <b>Hecho</b> (de hacer) lleva h; <b>echo</b> (de echar) no. <b>Haber</b> lleva h; <b>a ver</b> (mirar) no.")]),
 S(2,"Parejas que se confunden",[T("Distinguilas",["Palabra","Cuándo"],[["hay / ahí / ay","Hay: existir; ahí: lugar; ay: queja"],["porque / por qué","Porque: respuesta; por qué: pregunta"],["tuvo / tubo","Tuvo: del verbo tener; tubo: un caño"]])])],
 {"titulo":"elegir","planteo":"¿«Ayer ___ a mi abuela»: visite o visité? ¿Y cantaba o cantava?","pasos":["Pasado de cantar: cantaba, con b.","El verbo visitar lleva v: visité.","Cada regla resuelve una duda."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los pretéritos en -aba se escriben con ___ .","Los verbos terminados en -ger se escriben con ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres oraciones con hay, ahí y ay."},
 {"titulo":"Una regla por vez","texto":"No memorices todo: aprendé una regla por vez y usala en tus textos."},
 ["Escribir cantava en lugar de cantaba.","Confundir porque con por qué."],
 RS(("B","-aba y bl, br."),("G","-ger, -gir."),("H","Hecho, haber."),("Parejas","Hay, ahí, ay.")),
 G(("Pretérito","Tiempo verbal que expresa el pasado."),("Homófono","Palabra que suena igual a otra pero se escribe distinto.")),
 ["«Cantaba», ¿lleva b o v?","«Coger», ¿lleva g o j?","«Hecho», de hacer, ¿lleva h? Respondé sí o no.","¿Se escribe «porque» o «por qué» en «¿___ llegaste tarde?»"],
 [["b","con b"],["g","con g"],["si","sí"],["por que","por qué"]],
 {"incompleto":"B. G.","solo":"Hay un libro. Ahí está. ¡Ay, me duele!","carpeta":["B.","G.","Sí.","Por qué."]})
B4=NV("Vas a revisar un texto en varias pasadas y a escribir un dictado con atención a la ortografía.",["Revisar es releer","Las pasadas","El dictado","Cómo se corrige"],[
 S(1,"Revisar es releer",[P("Nadie escribe bien de una sola vez: <b>revisar</b> es leer de nuevo el texto buscando errores. Conviene leerlo en <b>voz alta</b>, porque así se escuchan las faltas.")]),
 S(1,"Las pasadas",[T("Una cosa por vez",["Pasada","Qué busco"],[["1","Que se entienda"],["2","Tildes"],["3","Letras que confunden (b/v, g/j, h)"],["4","Mayúsculas y puntuación"]])]),
 S(2,"El dictado",[P("En un dictado se escribe lo que alguien dice. Para hacerlo bien: escuchá toda la frase, escribila y <b>releé</b> al final con las reglas en la cabeza.")]),
 S(2,"Corregir",[P("Si dudás de una palabra, usá el <b>diccionario</b>. Anotá tus errores más frecuentes: son los que más tenés que revisar.")])],
 {"titulo":"revisar","planteo":"Corregí: «el avion aterrizo temprano».","pasos":["Mayúscula inicial: El.","Avión: aguda terminada en n, lleva tilde.","Aterrizó: aguda terminada en vocal, lleva tilde.","Versión: El avión aterrizó temprano."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Para escuchar las faltas conviene leer en ___ alta.","Para una duda de escritura uso el ___ ."]},
 {"titulo":"tu turno","planteo":"Pedile a alguien que te dicte cuatro oraciones y revisalas en cuatro pasadas."},
 {"titulo":"Una pasada, una cosa","texto":"No intentes corregir todo a la vez: una pasada para cada tipo de error."},
 ["Revisar una sola vez.","No usar el diccionario por pereza."],
 RS(("Revisar","Releer varias veces."),("Voz alta","Se escuchan las faltas."),("Pasadas","Una por tipo de error."),("Diccionario","Para dudas.")),
 G(("Revisar","Leer de nuevo para corregir."),("Dictado","Escritura de lo que se oye."),("Diccionario","Libro que explica palabras.")),
 ["¿Conviene revisar un texto una vez o varias veces?","¿Qué se usa para resolver una duda de escritura?","Corregí: «el avion aterrizo temprano». ¿Cuántas tildes faltan? Respondé solo el número.","¿Se escribe «a ver» o «haber» en «___ qué pasa»?"],
 [["varias","varias veces"],["diccionario","el diccionario"],["2","dos"],["a ver"]],
 {"incompleto":"Voz. Diccionario.","solo":"Cuatro oraciones revisadas con las cuatro pasadas.","carpeta":["Varias veces.","El diccionario.","2.","A ver."]})
ACT7={"1":[{"t":"classify","p":"¿Aguda, grave o esdrújula?","o":{"elementos":["canción","árbol","teléfono","papel"],"categorias":["Aguda","Grave","Esdrújula"]},"r":{"categorias":{"canción":"Aguda","árbol":"Grave","teléfono":"Esdrújula","papel":"Aguda"}},"e":"Se mira dónde cae la fuerza."},MC("¿Cuál lleva tilde?",["lápiz","papel","casa","reloj"],"lápiz","Grave terminada en z.")],
 "2":[{"t":"classify","p":"¿Diptongo o hiato?","o":{"elementos":["ciudad","país","cuota","día"],"categorias":["Diptongo","Hiato"]},"r":{"categorias":{"ciudad":"Diptongo","país":"Hiato","cuota":"Diptongo","día":"Hiato"}},"e":"Cuenta las sílabas."},MC("¿Cuál lleva tilde en el hiato?",["río","peine","cuota","ciudad"],"río","Cerrada tónica más abierta.")],
 "3":[{"t":"matching","p":"Uní cada palabra con su uso.","o":{"izquierda":["hay","ahí","ay","por qué"],"derecha":["Existir","Lugar","Queja","Pregunta"]},"r":{"pares":{"hay":"Existir","ahí":"Lugar","ay":"Queja","por qué":"Pregunta"}},"e":"Cada una tiene su función."},MC("¿Cuál está bien escrita?",["cantaba","cantava","kantaba","cantabba"],"cantaba","Pretérito en -aba.")],
 "4":[{"t":"ordering","p":"Ordená las pasadas de revisión.","o":["Mayúsculas y puntuación","Que se entienda","Letras que confunden","Tildes"],"r":{"orden":["Que se entienda","Tildes","Letras que confunden","Mayúsculas y puntuación"]},"e":"De lo general a lo detallado."},MC("¿Qué conviene hacer para escuchar las faltas?",["Leer en voz alta","Leer mirando el techo","No leer","Copiar"],"Leer en voz alta","Así se oyen.")],
 "5":[MC("Relámpago. La esdrújula…",["Siempre lleva tilde","Nunca lleva tilde","A veces"],"Siempre lleva tilde","Teléfono.",tiempo=20),MC("Relámpago. «País» tiene…",["Hiato","Diptongo","Nada"],"Hiato","Rí-o, pa-ís.",tiempo=20),MC("Relámpago. «Hecho» (de hacer) lleva…",["H","J","Nada"],"H","Participio de hacer.",tiempo=20),MC("Relámpago. Revisar conviene hacerlo…",["Varias veces","Una sola vez","Nunca"],"Varias veces","Una pasada por error.",tiempo=20)]}
EX7=[[1,MC("¿Cuál es una palabra aguda?",["canción","árbol","teléfono","casa"],"canción","Fuerza en la última sílaba.")],
 [1,MC("¿Cuál lleva tilde?",["árbol","casa","papel","reloj"],"árbol","Grave terminada en l.")],
 [1,VF("Las esdrújulas llevan tilde siempre.","Verdadero","Teléfono, música.")],
 [2,MC("¿Cuál es un diptongo?",["ciudad","país","río","día"],"ciudad","Dos vocales en una sílaba.")],
 [2,MC("¿Cuál es un hiato con tilde?",["país","ciudad","cuota","peine"],"país","Cerrada tónica y abierta.")],
 [2,VF("«Reír» lleva tilde.","Verdadero","Hiato con i tónica.")],
 [3,MC("¿Cuál es el pretérito de cantar?",["cantaba","cantava","cantaua","cantab"],"cantaba","Pretérito en -aba.")],
 [3,MC("¿Cuál está bien escrita?",["coger","cojer","kojer","coguer"],"coger","Verbos en -ger con g.")],
 [3,VF("«Hecho» (de hacer) se escribe sin h.","Falso","Lleva h.")],
 [4,MC("Revisar un texto conviene hacerlo…",["En varias pasadas","Una sola vez","Sin releer","Al final del año"],"En varias pasadas","Una por tipo de error.")],
 [4,MC("Para una duda de escritura se usa…",["El diccionario","El azar","Nada","La televisión"],"El diccionario","Resuelve la duda.")],
 [4,MC("¿Cuál está bien: «a ver» o «haber» en «___ si llega»?",["A ver","Haber","Aver","Ha ver"],"A ver","Es mirar.")],
 [4,VF("En un dictado no hace falta releer.","Falso","Conviene releer al final.")]]
M7={"subject_id":SID,"tema":7,"practica":"Práctica general: ortografía en uso","examen_titulo":"Nivel jefe: ortografía en uso","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT7,"examen":EX7}
for n,m in ((6,M6),(7,M7)):
    os.makedirs(os.path.join(AQUI,f"mision-{n}"),exist_ok=True); json.dump(m,open(os.path.join(AQUI,f"mision-{n}",f"mision-{n}.json"),"w"),ensure_ascii=False)

# ================= CLASES ANIMADAS =================
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={(5,1):"3029e488-5ba8-4032-b5fd-dd5a3a00cfa3",(5,2):"e6acbef3-5c27-474d-bb7c-54247c97bec1",(5,3):"dd05e528-5f20-4e8f-9a40-107f5b9ebd8a",(5,4):"06577aa6-32ec-469f-b28d-f43f2316036a",(6,1):"5e1454b9-74fb-43f0-9f22-19c1bf1a9c6f",(6,2):"0ef71248-d8a1-4e6a-9c78-7f8eacf2bcde",(6,3):"2a1555cb-959d-402a-aa6c-e7e544072c25",(6,4):"fed71c24-110e-4701-9ac7-ce1834d85f60"}
TIT={(5,1):"Recursos que se renuevan y recursos que se agotan",(5,2):"Petróleo, gas y carbón: recursos estratégicos",(5,3):"El agua: un recurso que no se reparte parejo",(5,4):"Minerales y cultivos que mueven la economía mundial",(6,1):"Suelos que se degradan: erosión y expansión agrícola",(6,2):"Contaminación del aire, el agua y la tierra",(6,3):"Cambio climático y fenómenos extremos",(6,4):"Políticas ambientales: de las cumbres a la comunidad"}
RES=lambda v,items:{"t":"resumen","voz":v,"items":items,"fin":{"titulo":"¡CLASE TERMINADA!","sub":"Ahora, a practicar 🚀"}}
Q=lambda p,o,c,v:{"t":"pregunta","pregunta":p,"opciones":o,"correcta":c,"voz":v}
ER=lambda it,v:{"t":"errores","items":[{"mal":a,"bien":b} for a,b in it],"voz":v}
DEF=lambda w,t,e,v:{"t":"definicion","palabra":w,"texto":t,"emoji":e,"voz":v}
CMP=lambda a,b,s,v:{"t":"comparar","a":{"cab":a[0],"texto":a[1],"emoji":a[2]},"b":{"cab":b[0],"texto":b[1],"emoji":b[2]},"signo":s,"voz":v}
TB=lambda t,c,f,v:{"t":"tabla","titulo":t,"columnas":c,"filas":f,"voz":v}
CAU=lambda c,it,v:{"t":"causas","causa":{"txt":c[0],"emoji":c[1]},"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
AD=lambda a,d,v:{"t":"antesdespues","antes":{"cab":a[0],"emoji":a[1],"texto":a[2]},"despues":{"cab":d[0],"emoji":d[1],"texto":d[2]},"voz":v}
DA=lambda n,a,d,t,e,v:{"t":"dato","numero":n,"antes":a,"despues":d,"texto":t,"emoji":e,"voz":v}
CL=lambda cj,fi,v:{"t":"clasificar","cajas":[{"cab":a,"emoji":b} for a,b in cj],"fichas":[{"txt":a,"caja":b} for a,b in fi],"voz":v}
PA=lambda t,it,v:{"t":"pasos","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
def NEU(e,**k): e=dict(e); e["neutro"]=k; return e
STEPS={(6,1):"037ca438-4ffc-4546-bac5-2d85e92fa42b",(6,2):"7c8e4668-4fda-412e-96a7-7706c24e7ec7",(6,3):"0505a6fd-24ea-4323-9560-fc64e1ae3d6e",(6,4):"5498e671-fda5-4d3e-af28-4376a962cc96",(7,1):"f492a440-2ac6-48da-9346-9cd82a20a00d",(7,2):"6e7f05eb-33db-4fab-b65a-771c877d32cc",(7,3):"10596e7f-6040-4341-a907-b2adaa0e0b9c",(7,4):"dedf15cb-0aa4-4e52-9ff0-e7dc27e290b1"}
TIT={(6,1):"Un castillo con historia",(6,2):"Un fantasma en apuros",(6,3):"Humor e ironía",(6,4):"Opino sobre lo leído",(7,1):"Agudas, graves y esdrújulas",(7,2):"Diptongo, hiato y tilde",(7,3):"Letras que confunden",(7,4):"Dictado y revisión"}
RES=lambda v,items:{"t":"resumen","voz":v,"items":items,"fin":{"titulo":"¡CLASE TERMINADA!","sub":"Ahora, a practicar 🚀"}}
Q=lambda p,o,c,v:{"t":"pregunta","pregunta":p,"opciones":o,"correcta":c,"voz":v}
ER=lambda it,v:{"t":"errores","items":[{"mal":a,"bien":b} for a,b in it],"voz":v}
DEF=lambda w,t,e,v:{"t":"definicion","palabra":w,"texto":t,"emoji":e,"voz":v}
CMP=lambda a,b,s,v:{"t":"comparar","a":{"cab":a[0],"texto":a[1],"emoji":a[2]},"b":{"cab":b[0],"texto":b[1],"emoji":b[2]},"signo":s,"voz":v}
TB=lambda t,c,f,v:{"t":"tabla","titulo":t,"columnas":c,"filas":f,"voz":v}
CAU=lambda c,it,v:{"t":"causas","causa":{"txt":c[0],"emoji":c[1]},"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
DA=lambda n,a,d,t,e,v:{"t":"dato","numero":n,"antes":a,"despues":d,"texto":t,"emoji":e,"voz":v}
CL=lambda cj,fi,v:{"t":"clasificar","cajas":[{"cab":a,"emoji":b} for a,b in cj],"fichas":[{"txt":a,"caja":b} for a,b in fi],"voz":v}
PA=lambda t,it,v:{"t":"pasos","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
AD=lambda a,d,v:{"t":"antesdespues","antes":{"cab":a[0],"emoji":a[1],"texto":a[2]},"despues":{"cab":d[0],"emoji":d[1],"texto":d[2]},"voz":v}
LN=lambda t,ev,v:{"t":"linea","titulo":t,"eventos":[{"fecha":a,"txt":b,"emoji":c} for a,b,c in ev],"voz":v}
CLS={(6,1):[
 {"t":"noticia","cinta":"EXTRA","titular":"Familia compra un castillo embrujado","bajada":"Y no cree en fantasmas","emoji":"🏰","titulo":"EL FANTASMA DE CANTERVILLE","sub":"un castillo con historia","voz":["Extra: una familia compra un castillo embrujado.","Y no cree en fantasmas.","Hoy: *El fantasma de Canterville*, de Oscar Wilde."]},
 TB("PERSONAJES",["Personaje","Cómo es"],[["Lord Canterville","El dueño"],["Los Otis","Prácticos y modernos"],["Sir Simon","El fantasma"],["Virginia","Sensible y amable"]],["Los personajes.","*Lord Canterville* es el dueño y avisa del fantasma.","Los *Otis* son una familia práctica y moderna.","*Sir Simon* es el fantasma.","Y *Virginia* es la hija, sensible y amable."]),
 DEF("Relato gótico","Misterio y terror en castillos antiguos","🏰",["Es un *relato gótico*: misterio y terror en un castillo antiguo.","Wilde juega con esos elementos."]),
 DEF("Narrador omnisciente","Cuenta en tercera persona y lo sabe todo","👁️",["El narrador es *omnisciente*.","Cuenta en tercera persona y conoce lo que sienten todos."]),
 CMP(("TRADICIÓN","El fantasma, siglos de historia","👻"),("PRACTICIDAD","La familia, moderna y sin miedo","🧼"),"vs",["El conflicto es un choque.","El fantasma representa la *tradición*.","La familia representa la *practicidad*."]),
 CL([("FANTASMA","👻"),("FAMILIA","🏠")],[("Quiere asustar",0),("No cree en ellos",1),("Siglos de historia",0)],["¿Del fantasma o de la familia?","*Quiere asustar* y *siglos de historia*: el fantasma.","*No cree en ellos*: la familia."]),
 Q("¿Cómo se llama el fantasma?",["Sir Simon","Lord Canterville","Washington"],0,["Te toca: ¿cómo se llama el fantasma?","¿Sir Simon, Lord Canterville o Washington?","*Sir Simon*."]),
 ER([("Es un cuento de terror común","Es una parodia gótica"),("El narrador es un personaje","Narra en tercera persona")],["Errores típicos.","Creer que es *terror común*.","Y confundir al *narrador* con un personaje."]),
 RES(["Repasemos.","El autor es *Oscar Wilde*.","El escenario es un *castillo inglés*.","Los personajes son los *Otis* y *Sir Simon*.","Y el conflicto enfrenta *tradición* y *practicidad*.","¡Clase terminada! Ahora, *a practicar*."],[["AUTOR","Wilde"],["ESCENARIO","castillo"],["PERSONAJES","Otis y Simon"],["CONFLICTO","tradición y práctica"]])],
(6,2):[
 {"t":"reto","texto":"¿Qué le ofrece el señor Otis al fantasma para sus cadenas?","segundos":6,"respuesta":"Aceite","emoji":"⛓️","titulo":"UN FANTASMA EN APUROS","sub":"intentos y respuestas","voz":["Desafío: ¿qué le ofrece el señor Otis al fantasma para sus cadenas? Seis segundos.","Aceite.","Hoy: *un fantasma en apuros*."]},
 TB("INTENTO Y RESPUESTA",["Fantasma","Familia"],[["Cadenas ruidosas","Le ofrecen aceite"],["Mancha de sangre","La limpian"],["Aparece de noche","Le tiran almohadas"]],["Cada intento tiene su respuesta.","Hace sonar *cadenas*: le ofrecen *aceite*.","Deja una *mancha*: la *limpian*.","Aparece de noche: le tiran *almohadas*."]),
 DEF("Causa","Lo que provoca que algo pase","🔗",["La *causa* es lo que provoca que algo pase.","La *consecuencia* es lo que pasa después."]),
 CAU(("Nadie le tiene miedo",'👻'),[("Se siente humillado","😞"),("Se esfuerza más","💪"),("Pierde el orgullo","📉")],["Una causa y varias consecuencias.","Nadie le tiene miedo.","Entonces se siente *humillado*.","Se *esfuerza más*.","Y pierde el *orgullo*."]),
 CL([("CAUSA","🔗"),("CONSECUENCIA","➡️")],[("Nadie se asusta",0),("Se siente humillado",1),("Deja una mancha",0),("La limpian",1)],["¿Causa o consecuencia?","*Nadie se asusta* y *deja una mancha*: causas.","*Se siente humillado* y *la limpian*: consecuencias."]),
 Q("¿Cómo se siente el fantasma?",["Humillado","Orgulloso","Aliviado"],0,["Te toca: ¿cómo se siente el fantasma?","¿Humillado, orgulloso o aliviado?","*Humillado*."]),
 ER([("Confundir causa y consecuencia","Probar con porque y entonces"),("El fantasma no siente nada","Se siente humillado")],["Errores típicos.","*Confundir* causa y consecuencia.","Y creer que el fantasma *no siente nada*."]),
 RES(["Repasemos.","El fantasma *intenta* asustar.","La familia *responde* con practicidad.","La *causa* provoca la *consecuencia*.","Y el fantasma queda *humillado*.","¡Clase terminada! Ahora, *a practicar*."],[["INTENTOS","asustar"],["RESPUESTAS","prácticas"],["CAUSA","lo que provoca"],["FANTASMA","humillado"]])],
(6,3):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"Un fantasma aparece y le ofrecen aceite 😂"},{"yo":True,"txt":"¿Aceite? ¿Para qué?"},{"yo":False,"txt":"Para sus cadenas ruidosas"}],"titulo":"HUMOR E IRONÍA","sub":"lo esperado y lo que pasa","voz":["Lu le cuenta a Juan que a un fantasma le ofrecen aceite.","Juan: ¿aceite? ¿Para qué?","Lu: para sus cadenas ruidosas.","Hoy: *humor e ironía*."]},
 DEF("Ironía","Lo que ocurre es lo contrario de lo esperado","🎭",["La *ironía* muestra lo contrario de lo esperado.","Sirve para burlarse o señalar algo."]),
 TB("ESPERADO Y REAL",["Se espera","Ocurre"],[["Familia aterrada","Le ofrecen aceite"],["Fantasma imponente","Se siente ridículo"],["Misterio","Producto de limpieza"]],["El contraste.","Se espera una familia *aterrada*: le ofrecen *aceite*.","Se espera un fantasma *imponente*: se siente *ridículo*.","Se espera *misterio*: usan un *producto de limpieza*."]),
 DEF("Parodia","Imitar un género para burlarse","🎪",["Una *parodia* imita un género para burlarse de él.","El cuento parodia el *género gótico*."]),
 CL([("HUMOR","😂"),("TERROR","😱")],[("Aceite para cadenas",0),("Mancha de sangre",1),("Almohadas",0)],["¿Qué produce humor?","*Aceite para cadenas* y *almohadas*: humor.","*La mancha de sangre* sería terror."]),
 Q("Imitar un género para burlarse de él es una…",["Parodia","Fábula","Biografía"],0,["Te toca: imitar un género para burlarse de él.","¿Parodia, fábula o biografía?","Una *parodia*."]),
 ER([("La ironía es mentir","Es mostrar lo contrario de lo esperado"),("El humor es solo burla","También señala algo")],["Errores típicos.","Creer que la ironía es *mentir*.","Y pensar que el humor es *solo burla*."]),
 RES(["Repasemos.","La *ironía* es lo contrario de lo esperado.","El *contraste* genera humor.","La *exageración* también.","Y el cuento es una *parodia* gótica.","¡Clase terminada! Ahora, *a practicar*."],[["IRONÍA","contrario"],["CONTRASTE","esperado y real"],["EXAGERAR","hace reír"],["PARODIA","imita y se burla"]])],
(6,4):[
 {"t":"reto","texto":"¿\"El fantasma es simpático\" es un hecho o una opinión?","segundos":6,"respuesta":"Una opinión","emoji":"💭","titulo":"OPINO SOBRE LO LEÍDO","sub":"hechos y opiniones","voz":["Desafío: ¿el fantasma es simpático es un hecho o una opinión? Seis segundos.","Una opinión.","Hoy: *opino sobre lo leído*."]},
 CMP(("HECHO","Ocurre en el texto","📖"),("OPINIÓN","Lo que pienso","💭"),"vs",["No son lo mismo.","El *hecho* ocurre en el texto.","La *opinión* es lo que yo pienso."]),
 TB("ESTRUCTURA",["Parte","Qué hace"],[["Tesis","Dice lo que pienso"],["Argumento","Explica por qué"],["Ejemplo","Lo prueba con el texto"],["Cierre","Vuelve a la tesis"]],["Una opinión tiene partes.","La *tesis* dice lo que pienso.","El *argumento* explica por qué.","El *ejemplo* lo prueba con el texto.","Y el *cierre* vuelve a la tesis."]),
 CL([("HECHO","📖"),("OPINIÓN","💭")],[("Compran el castillo",0),("Es muy divertido",1),("Deja una mancha",0),("Es simpático",1)],["¿Hecho u opinión?","*Compran el castillo* y *deja una mancha*: hechos.","*Es muy divertido* y *es simpático*: opiniones."]),
 TB("CONECTORES",["Función","Ejemplo"],[["Opinar","en mi opinión"],["Explicar","porque"],["Ejemplificar","por ejemplo"],["Cerrar","en conclusión"]],["Conectores para opinar.","*En mi opinión* para opinar.","*Porque* para explicar.","*Por ejemplo* para ejemplificar.","Y *en conclusión* para cerrar."]),
 Q("¿Qué conector sirve para dar un ejemplo?",["Por ejemplo","En conclusión","Pero"],0,["Te toca: ¿qué conector sirve para dar un ejemplo?","¿Por ejemplo, en conclusión o pero?","*Por ejemplo*."]),
 ER([("Opinar sin explicar","Dar argumentos y ejemplos"),("Mezclar hecho y opinión","Separarlos")],["Errores típicos.","*Opinar sin explicar*.","Y *mezclar* hechos con opiniones."]),
 RES(["Repasemos.","El *hecho* ocurre en el texto.","La *opinión* es lo que pienso.","Se arma con *tesis*, *argumentos* y *ejemplos*.","Y se cierra volviendo a la tesis.","¡Clase terminada! Ahora, *a practicar*."],[["HECHO","en el texto"],["OPINIÓN","lo que pienso"],["PARTES","tesis y ejemplos"],["CIERRE","vuelve a la tesis"]])],
(7,1):[
 {"t":"gancho","grande":"3 clases","emoji":"🔤","final":"según dónde cae la fuerza","titulo":"AGUDAS, GRAVES Y ESDRÚJULAS","sub":"y cuándo llevan tilde","voz":["Todas las palabras caen en tres clases.","Según dónde cae la fuerza.","Hoy: *agudas*, *graves* y *esdrújulas*."]},
 DEF("Sílaba tónica","La que se pronuncia con más fuerza","🔊",["La *sílaba tónica* es la que se pronuncia con más fuerza.","En *canción* es *ción*."]),
 TB("TRES CLASES",["Clase","Fuerza","Ejemplo"],[["Aguda","Última","canción"],["Grave","Penúltima","árbol"],["Esdrújula","Antepenúltima","teléfono"]],["Las tres clases.","*Aguda*: la fuerza en la última, como *canción*.","*Grave*: en la penúltima, como *árbol*.","*Esdrújula*: en la antepenúltima, como *teléfono*."]),
 TB("CUÁNDO LLEVAN TILDE",["Clase","Regla"],[["Aguda","Termina en n, s o vocal"],["Grave","NO termina en n, s o vocal"],["Esdrújula","Siempre"]],["Las reglas.","La *aguda* lleva tilde si termina en *n*, *s* o *vocal*.","La *grave* lleva tilde si *no* termina en *n*, *s* ni *vocal*.","Y la *esdrújula* lleva tilde *siempre*."]),
 CL([("AGUDA","1️⃣"),("GRAVE","2️⃣"),("ESDRÚJULA","3️⃣")],[("canción",0),("árbol",1),("música",2),("papel",0)],["¿Qué clase es?","*Canción* y *papel*: agudas.","*Árbol*: grave.","*Música*: esdrújula."]),
 Q("¿Cuál lleva tilde?",["lápiz","papel","casa"],0,["Te toca: ¿cuál lleva tilde?","¿Lápiz, papel o casa?","*Lápiz*: grave terminada en z."]),
 ER([("Tilde a todo lo que suena fuerte","Primero buscar la sílaba tónica"),("Olvidar la tilde en esdrújulas","Siempre llevan")],["Errores típicos.","Poner tilde a *todo lo fuerte*.","Y *olvidar* la tilde en las esdrújulas."]),
 RES(["Repasemos.","*Aguda*: última sílaba.","*Grave*: penúltima.","*Esdrújula*: antepenúltima.","Y la esdrújula lleva tilde *siempre*.","¡Clase terminada! Ahora, *a practicar*."],[["AGUDA","última"],["GRAVE","penúltima"],["ESDRÚJULA","siempre tilde"],["TÓNICA","más fuerza"]])],
(7,2):[
 {"t":"reto","texto":"¿\"País\" tiene una o dos sílabas?","segundos":6,"respuesta":"Dos: pa-ís","emoji":"🔤","titulo":"DIPTONGO Y HIATO","sub":"y la tilde","voz":["Desafío: ¿país tiene una o dos sílabas? Seis segundos.","Dos: pa, ís.","Hoy: *diptongo*, *hiato* y *tilde*."]},
 CMP(("ABIERTAS","a, e, o","🔓"),("CERRADAS","i, u","🔒"),"+",["Dos clases de vocales.","Las *abiertas* son a, e, o.","Las *cerradas* son i, u."]),
 DEF("Diptongo","Dos vocales en una sílaba","🔗",["El *diptongo* son dos vocales en una sola sílaba.","Como *ciu-dad* o *cuo-ta*."]),
 DEF("Hiato","Dos vocales en sílabas distintas","✂️",["El *hiato* son dos vocales en sílabas distintas.","Como *pa-ís* o *rí-o*."]),
 CL([("DIPTONGO","🔗"),("HIATO","✂️")],[("ciudad",0),("país",1),("cuota",0),("día",1)],["¿Diptongo o hiato?","*Ciudad* y *cuota*: diptongos.","*País* y *día*: hiatos."]),
 Q("¿Cuál lleva tilde en el hiato?",["río","peine","ciudad"],0,["Te toca: ¿cuál lleva tilde en el hiato?","¿Río, peine o ciudad?","*Río*."]),
 ER([("Tilde en un diptongo por costumbre","Solo si cumple las reglas generales"),("Olvidar la tilde en país","Hiato con tilde")],["Errores típicos.","Poner tilde a un *diptongo* por costumbre.","Y *olvidar* la tilde en *país*."]),
 RES(["Repasemos.","Las vocales son *abiertas* o *cerradas*.","El *diptongo* es una sílaba.","El *hiato* son dos.","Y el hiato con cerrada tónica *siempre lleva tilde*.","¡Clase terminada! Ahora, *a practicar*."],[["DIPTONGO","una sílaba"],["HIATO","dos sílabas"],["CERRADA TÓNICA","tilde"],["PASO","separar"]])],
(7,3):[
 {"t":"noticia","cinta":"DUDA","titular":"¿Cantaba con b o con v?","bajada":"Las letras que más confunden","emoji":"✏️","titulo":"LETRAS QUE CONFUNDEN","sub":"b, v, g, j y h","voz":["Duda: ¿cantaba se escribe con b o con v?","Son las letras que más confunden.","Hoy: *b*, *v*, *g*, *j* y *h*."]},
 TB("B Y V",["Regla","Ejemplo"],[["Pretéritos en -aba","cantaba"],["b antes de l y r","blanco, brazo"],["v en el verbo ir","voy, vas"]],["Algunas reglas de *b* y *v*.","Los pretéritos en *aba* llevan *b*.","Antes de *l* y *r*, *b*.","Y el verbo *ir* lleva *v*."]),
 DEF("G y J","Los verbos en -ger y -gir llevan g","✏️",["Los verbos terminados en *ger* y *gir* llevan *g*.","Como *coger* y *elegir*.","Excepciones: *tejer* y *crujir*."]),
 CMP(("HECHO","Del verbo hacer","✅"),("ECHO","Del verbo echar","🔄"),"≠",["La *h* no suena pero se escribe.","*Hecho* es de hacer, con *h*.","*Echo* es de echar, sin *h*."]),
 TB("PAREJAS",["Palabra","Uso"],[["hay","Existir"],["ahí","Lugar"],["ay","Queja"]],["Tres parecidas.","*Hay* es existir.","*Ahí* es un lugar.","Y *ay* es una queja."]),
 Q("¿Se escribe «porque» o «por qué» en «¿___ llegaste tarde?»?",["Por qué","Porque","Porqué"],0,["Te toca: ¿porque o por qué en una pregunta?","¿Por qué, porque o porqué?","*Por qué*."]),
 ER([("Cantava","Cantaba"),("Cojer","Coger")],["Errores típicos.","*Cantava* con v.","Y *cojer* con j."]),
 RES(["Repasemos.","Los pretéritos en *aba* llevan *b*.","Los verbos en *ger* llevan *g*.","*Hecho* lleva *h*.","Y distinguí *hay*, *ahí* y *ay*.","¡Clase terminada! Ahora, *a practicar*."],[["B","-aba"],["G","-ger"],["H","hecho"],["PAREJAS","hay, ahí, ay"]])],
(7,4):[
 {"t":"historia","personaje":{"nombre":"Mica","emoji":"👧"},"lugar":"📝","lineas":["Mica escribió un texto en cinco minutos.","Lo releyó en voz alta y encontró tres errores."],"titulo":"DICTADO Y REVISIÓN","sub":"escribir bien","voz":["Mica escribió un texto en cinco minutos.","Lo releyó en voz alta y encontró tres errores.","Hoy: *dictado y revisión*."]},
 DEF("Revisar","Leer de nuevo para corregir","🔍",["*Revisar* es leer de nuevo para corregir.","Conviene hacerlo en *voz alta*."]),
 TB("LAS PASADAS",["Pasada","Qué busco"],[["1","Que se entienda"],["2","Tildes"],["3","b/v, g/j, h"],["4","Mayúsculas y puntos"]],["Cuatro pasadas.","Primero, que se *entienda*.","Después, las *tildes*.","Luego, las letras que *confunden*.","Y por último, *mayúsculas* y puntuación."]),
 DEF("Dictado","Escribir lo que se oye","🎧",["En un *dictado* escribís lo que oís.","Escuchá toda la frase, escribila y *releé*."]),
 CL([("REVISAR","🔍"),("NO REVISAR","❌")],[("Leer en voz alta",0),("Entregar sin releer",1),("Usar diccionario",0)],["¿Buena práctica o no?","*Leer en voz alta* y *usar diccionario*: sí.","*Entregar sin releer*: no."]),
 Q("Para una duda de escritura, ¿qué usás?",["El diccionario","El azar","Nada"],0,["Te toca: ¿qué se usa para una duda de escritura?","¿El diccionario, el azar o nada?","*El diccionario*."]),
 ER([("Revisar una sola vez","Varias pasadas"),("Corregir todo a la vez","Una cosa por pasada")],["Errores típicos.","Revisar *una sola vez*.","Y querer corregir *todo a la vez*."]),
 RES(["Repasemos.","Revisar es *releer*.","Conviene en *voz alta*.","Se hace en *pasadas*, una por tipo de error.","Y ante la duda, el *diccionario*.","¡Clase terminada! Ahora, *a practicar*."],[["REVISAR","releer"],["VOZ ALTA","se oyen faltas"],["PASADAS","una por error"],["DUDA","diccionario"]])]}
for (m,n),es in CLS.items():
    json.dump({"slug":f"leng1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Lengua y Literatura I","titulo":TIT[(m,n)],"sub":f"Lengua y Literatura I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"leng1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
