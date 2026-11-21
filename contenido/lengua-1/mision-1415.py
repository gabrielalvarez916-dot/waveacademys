# -*- coding: utf-8 -*-
"""Lengua y Literatura I · Misión 14 (Escuchar y hablar en clase) y Misión 15 (Cohesión del texto)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}
SID = "e1b0726d-08aa-4d9e-9060-18489f529da2"

FB=lambda p,h,e,**k:{"t":"fill_blank","p":p,"o":[],"r":{"huecos":h},"e":e,**k}
MS=lambda p,o,c,e,**k:{"t":"multi_select","p":p,"o":o,"r":{"correctas":c},"e":e,**k}
TT=lambda p,seg,tocar,e,**k:{"t":"tap_text","p":p,"o":{"segmentos":seg,"modo":"palabras"},"r":{"tocar":tocar},"e":e,**k}
KW=lambda p,ayuda,ref,e,**k:{"t":"keywords","p":p,"o":{"ayuda":ayuda},"r":ref,"e":e,**k}
# ================= MISIÓN 14: ESCUCHAR Y HABLAR EN CLASE =================
A1=NV("Vas a planificar una exposición oral con inicio, desarrollo y cierre, y a cuidar la voz y el cuerpo.",["Elegir y organizar","Esquema","Apoyos","Voz y cuerpo"],[
 S(1,"Elegir y organizar",[D("Exposición oral","Presentación en voz alta de un tema ante un público, con un orden previo."),P("Se elige un tema acotado, se busca información en fuentes confiables y se anotan solo las <b>ideas clave</b>.")]),
 S(1,"Esquema",[T("Estructura",["Parte","Qué hago"],[["Inicio","Saludo, tema y por qué importa"],["Desarrollo","Tres o cuatro ideas con ejemplos"],["Cierre","Resumen y agradecimiento"]])]),
 S(2,"Apoyos",[P("Las imágenes, los esquemas y las fichas ayudan, pero <b>no se leen</b>. Cada diapositiva o cartel lleva pocas palabras; lo importante lo decís vos.")]),
 S(2,"Voz y cuerpo",[T("Cuidá",["Aspecto","Consejo"],[["Voz","Clara, sin gritar"],["Ritmo","Ni muy rápido ni muy lento"],["Mirada","Al público, no al papel"],["Postura","Firme y relajada"],["Tiempo","Ensayar con reloj"]])])],
 {"titulo":"organizar","planteo":"Ordená tu exposición sobre los volcanes.","pasos":["Inicio: saludo y qué es un volcán.","Desarrollo: partes, tipos y un ejemplo.","Cierre: resumen y agradecimiento."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Las partes de una exposición son inicio, desarrollo y ___ .","Los apoyos visuales no se ___ ."]},
 {"titulo":"tu turno","planteo":"Armá el esquema de una exposición de tres minutos sobre un tema que te guste."},
 {"titulo":"Ensayá en voz alta","texto":"Practicar frente al espejo o a un familiar baja los nervios y mejora el tiempo."},
 ["Leer todo de un papel.","Llenar las diapositivas de texto."],
 RS(("Esquema","Inicio, desarrollo, cierre."),("Apoyos","Pocas palabras."),("Voz","Clara."),("Ensayo","Con reloj.")),
 G(("Exposición","Presentación oral de un tema."),("Ideas clave","Lo más importante."),("Ritmo","Velocidad al hablar.")),
 ["¿Cómo se llama la última parte de una exposición?","¿Los apoyos visuales se leen o se explican?","¿Conviene ensayar con reloj? Respondé sí o no.","¿Cuántas ideas conviene presentar: tres o cuatro, o cuarenta?"],
 [["cierre","el cierre"],["se explican","explican","explicarse","se explican."],["si","sí"],["tres o cuatro","3 o 4","tres","cuatro"]],
 {"incompleto":"Cierre. Leen.","solo":"Inicio: saludo y tema. Desarrollo: tres ideas. Cierre: resumen.","carpeta":["El cierre.","Se explican.","Sí.","Tres o cuatro."]})
A2=NV("Vas a escuchar con atención y tomar notas útiles con palabras clave, abreviaturas y esquemas.",["Escucha activa","Palabras clave","Abreviaturas y símbolos","Repasar las notas"],[
 S(1,"Escucha activa",[D("Escucha activa","Escuchar con atención, sin interrumpir, buscando entender y recordar lo que se dice."),P("Mirá a quien habla, evitá distracciones y pensá qué es lo más importante.")]),
 S(1,"Palabras clave",[P("No se copia todo: se anotan <b>palabras clave</b>, fechas, nombres y números. Una nota es breve y se entiende después.")]),
 S(2,"Abreviaturas y símbolos",[T("Ahorrá tiempo",["Símbolo","Significa"],[["→","lleva a, causa"],["=","es igual a"],["+","más, además"],["p. ej.","por ejemplo"],["!","importante"]])]),
 S(2,"Repasar",[T("Después de la clase",["Paso","Qué hago"],[["1","Releo y completo lo que falte"],["2","Subrayo las ideas principales"],["3","Escribo un resumen de dos líneas"],["4","Anoto mis dudas"]])])],
 {"titulo":"tomar notas","planteo":"Escuchás: «La fotosíntesis es el proceso por el que las plantas fabrican su alimento usando luz, agua y dióxido de carbono». Anotá.","pasos":["Fotosíntesis = plantas fabrican alimento.","Usan: luz + agua + CO2.","! Es el proceso clave de las plantas."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Escuchar con atención y sin interrumpir es la escucha ___ .","En las notas se anotan palabras ___ ."]},
 {"titulo":"tu turno","planteo":"Tomá notas de un video corto y escribí un resumen de dos líneas."},
 {"titulo":"Anotá lo esencial","texto":"Si copiás todo, dejás de escuchar; anotá solo lo importante."},
 ["Copiar todo textual.","No repasar las notas después."],
 RS(("Escucha activa","Atención."),("Notas","Palabras clave."),("Símbolos","Ahorran tiempo."),("Repaso","Después de la clase.")),
 G(("Nota","Apunte breve."),("Abreviatura","Forma corta de una palabra."),("Palabra clave","Palabra esencial de una idea.")),
 ["¿Cómo se llama escuchar con atención y sin interrumpir?","¿Qué símbolo se usa para «causa» o «lleva a»?","¿Se anota todo textual o solo lo esencial?","¿Conviene repasar las notas después de la clase? Respondé sí o no."],
 [["escucha activa","activa"],["→","flecha","la flecha"],["solo lo esencial","lo esencial","esencial"],["si","sí"]],
 {"incompleto":"Activa. Clave.","solo":"Fotosíntesis = plantas fabrican alimento; usan luz + agua + CO2.","carpeta":["Escucha activa.","→","Lo esencial.","Sí."]})
A3=NV("Vas a participar en un debate con turnos, argumentos y respeto.",["Qué es un debate","Roles y turnos","Hablar con respeto","Refutar sin atacar"],[
 S(1,"Qué es un debate",[D("Debate","Intercambio organizado de opiniones sobre un tema, donde cada parte defiende su posición con argumentos."),P("No se trata de ganar a gritos: se trata de <b>entender y convencer con razones</b>.")]),
 S(1,"Roles y turnos",[T("Quién hace qué",["Rol","Función"],[["Moderador","Da la palabra y cuida el tiempo"],["Equipo a favor","Defiende la tesis"],["Equipo en contra","La cuestiona con razones"],["Público","Escucha y hace preguntas"]])]),
 S(2,"Hablar con respeto",[T("Reglas",["Regla","Ejemplo"],[["Pedir la palabra","Levanto la mano"],["No interrumpir","Espero mi turno"],["Criticar la idea","No el aspecto de la persona"],["Escuchar","Tomo nota para responder"]])]),
 S(2,"Refutar sin atacar",[P("Para refutar: <b>reconozco</b> algo, <b>discrepo</b> con una razón y <b>propongo</b>. Ejemplo: «Es cierto que cuesta, pero a largo plazo se ahorra».")])],
 {"titulo":"participar","planteo":"Otro equipo dice: «Las tareas no sirven». ¿Cómo respondés?","pasos":["Reconozco: a veces son largas.","Discrepo: pero ayudan a practicar.","Propongo: tareas más cortas y claras."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Quien da la palabra y cuida el tiempo es el ___ .","En un debate se critica la idea y no a la ___ ."]},
 {"titulo":"tu turno","planteo":"Preparen en grupo dos argumentos a favor y dos en contra de un tema."},
 {"titulo":"Escuchá para responder","texto":"Anotá las ideas del otro equipo: te sirven para refutar."},
 ["Interrumpir a los gritos.","Responder con burlas."],
 RS(("Debate","Opiniones con razones."),("Roles","Moderador y equipos."),("Respeto","Turnos."),("Refutar","Reconozco y discrepo.")),
 G(("Moderador","Quien coordina el debate."),("Refutar","Rebatir un argumento con razones."),("Turno","Momento de hablar.")),
 ["¿Cómo se llama quien coordina el debate?","¿Se critica la idea o a la persona?","¿Está permitido interrumpir a gritos? Respondé sí o no.","¿Cómo se llama rebatir un argumento con razones?"],
 [["moderador","el moderador"],["la idea","idea"],["no"],["refutar","refutacion","refutación"]],
 {"incompleto":"Moderador. Persona.","solo":"Es cierto que son largas; sin embargo ayudan a practicar; propongo hacerlas más cortas.","carpeta":["Moderador.","La idea.","No.","Refutar."]})
A4=NV("Vas a evaluar un debate con una grilla de criterios y dar una devolución respetuosa.",["Criterios","La grilla","Dar una devolución","Autoevaluarme"],[
 S(1,"Criterios",[T("Qué se mira",["Criterio","Pregunta"],[["Claridad","¿Se entendió la tesis?"],["Argumentos","¿Hubo razones y ejemplos?"],["Respeto","¿Se respetaron turnos?"],["Escucha","¿Se respondió a lo que dijo el otro?"],["Tiempo","¿Se cumplió el tiempo?"]])]),
 S(1,"La grilla",[T("Ejemplo de grilla",["Criterio","Logrado","En proceso"],[["Claridad","",""],["Argumentos","",""],["Respeto","",""]])]),
 S(2,"Devolución",[P("Una devolución útil dice <b>dos cosas que salieron bien</b> y <b>una para mejorar</b>, con un ejemplo concreto: «Tu ejemplo del reciclaje fue claro; podrías hablar más despacio».")]),
 S(2,"Autoevaluarme",[P("Al terminar, preguntate: ¿escuché? ¿respeté los turnos? ¿di razones? ¿qué haría distinto? Anotá un objetivo para el próximo debate.")])],
 {"titulo":"evaluar","planteo":"Un equipo dio buenos argumentos pero interrumpió. ¿Cómo lo evaluás?","pasos":["Argumentos: logrado.","Respeto: en proceso.","Devolución: tus argumentos fueron claros; la próxima, esperá tu turno."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La tabla que ordena los criterios para evaluar es la ___ .","Una devolución útil lleva dos aciertos y una ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una devolución para un compañero con dos aciertos y una mejora."},
 {"titulo":"Con ejemplos","texto":"Una devolución con ejemplos concretos sirve más que un «estuvo bien»."},
 ["Dar una devolución sin ejemplos.","Criticar a la persona en lugar de la tarea."],
 RS(("Criterios","Claridad, argumentos, respeto."),("Grilla","Ordena la evaluación."),("Devolución","Dos aciertos y una mejora."),("Autoevaluación","Un objetivo.")),
 G(("Grilla","Cuadro de criterios."),("Devolución","Comentario para mejorar."),("Autoevaluación","Evaluar el propio trabajo.")),
 ["¿Cómo se llama la tabla de criterios para evaluar?","¿Cuántas mejoras lleva una devolución útil: una o diez?","¿Una devolución debe dar ejemplos concretos? Respondé sí o no.","¿Cómo se llama evaluar el propio trabajo?"],
 [["grilla","la grilla"],["una","1","una mejora"],["si","sí"],["autoevaluacion","autoevaluación"]],
 {"incompleto":"Grilla. Mejora.","solo":"Tu ejemplo fue claro; respetaste turnos; podrías hablar más despacio.","carpeta":["Grilla.","Una.","Sí.","Autoevaluación."]})
ACT14={"1":[{"t":"ordering","p":"Ordená las partes de una exposición.","o":["Cierre","Inicio","Desarrollo"],"r":{"orden":["Inicio","Desarrollo","Cierre"]},"e":"De la presentación al cierre."},MS("¿Qué conviene hacer al exponer?",["Mirar al público","Ensayar con reloj","Leer todo de un papel","Usar pocas palabras en los carteles"],["Mirar al público","Ensayar con reloj","Usar pocas palabras en los carteles"],"No se lee todo.")],
 "2":[{"t":"classify","p":"¿Qué se anota?","o":{"elementos":["Fechas","Palabras clave","Chistes del docente","Números importantes"],"categorias":["Se anota","No hace falta"]},"r":{"categorias":{"Fechas":"Se anota","Palabras clave":"Se anota","Chistes del docente":"No hace falta","Números importantes":"Se anota"}},"e":"Se anota lo esencial."},FB("Escuchar con atención y sin interrumpir es la escucha ___ .",[["activa"]],"Activa.")],
 "3":[{"t":"matching","p":"Uní cada rol con su función.","o":{"izquierda":["Moderador","Equipo a favor","Equipo en contra","Público"],"derecha":["Da la palabra","Defiende la tesis","Cuestiona con razones","Escucha y pregunta"]},"r":{"pares":{"Moderador":"Da la palabra","Equipo a favor":"Defiende la tesis","Equipo en contra":"Cuestiona con razones","Público":"Escucha y pregunta"}},"e":"Cada rol cumple una función."},VF("En un debate se puede interrumpir cuando se quiere.","Falso","Se respetan los turnos.")],
 "4":[KW("Escribí una devolución para un compañero que expuso un tema: dos cosas que salieron bien y una para mejorar, con un ejemplo concreto.","Dos aciertos, una mejora y un ejemplo; tono respetuoso.","Devolución con dos aciertos concretos, una sugerencia de mejora con ejemplo y tono respetuoso, centrada en la tarea y no en la persona.","Se evalúa ejemplos, respeto y claridad."),MS("¿Qué criterios puede tener una grilla de debate?",["Claridad","Argumentos","Respeto","Color de ropa"],["Claridad","Argumentos","Respeto"],"El color de ropa no es un criterio.")],
 "5":[MC("Relámpago. La última parte de una exposición es el…",["Cierre","Saludo","Desarrollo"],"Cierre","Resume.",tiempo=20),VF("Relámpago. Se anota todo textual al tomar notas.","Falso","Solo lo esencial.",tiempo=20),MC("Relámpago. Quien coordina el debate es el…",["Moderador","Público","Rival"],"Moderador","Da la palabra.",tiempo=20),VF("Relámpago. Una devolución lleva ejemplos concretos.","Verdadero","Así sirve.",tiempo=20)]}
EX14=[[1,MC("Las partes de una exposición son…",["Inicio, desarrollo y cierre","Solo desarrollo","Título y firma","Pregunta y respuesta"],"Inicio, desarrollo y cierre","Un orden previo.")],
 [1,MS("Consejos para exponer:",["Mirar al público","Ensayar","Leer todo","Cuidar la voz"],["Mirar al público","Ensayar","Cuidar la voz"],"No se lee todo.")],
 [1,VF("Los apoyos visuales se leen palabra por palabra.","Falso","Se explican.")],
 [2,MC("Escuchar con atención y sin interrumpir es…",["Escucha activa","Escucha pasiva","Ruido","Dictado"],"Escucha activa","Se busca entender.")],
 [2,FB("En las notas se anotan palabras ___ .",[["clave"]],"Lo esencial.")],
 [2,VF("Conviene repasar las notas después de clase.","Verdadero","Ayuda a recordar.")],
 [3,MC("El moderador…",["Da la palabra y cuida el tiempo","Defiende siempre la tesis","Interrumpe","Aplaude"],"Da la palabra y cuida el tiempo","Coordina.")],
 [3,MS("Reglas de un debate:",["Pedir la palabra","No interrumpir","Criticar la idea","Gritar"],["Pedir la palabra","No interrumpir","Criticar la idea"],"Gritar no.")],
 [3,VF("Se critica a la persona y no a la idea.","Falso","Se critica la idea.")],
 [4,MC("Una grilla sirve para…",["Ordenar criterios de evaluación","Dibujar","Copiar","Dictar"],"Ordenar criterios de evaluación","Es un cuadro.")],
 [4,FB("Una devolución útil lleva dos aciertos y una ___ .",[["mejora"]],"Con ejemplos.")],
 [4,MC("Evaluar el propio trabajo es la…",["Autoevaluación","Exposición","Refutación","Moderación"],"Autoevaluación","Se hace al final.")],
 [4,VF("Una devolución sin ejemplos es igual de útil.","Falso","Los ejemplos ayudan.")]]
M14={"subject_id":SID,"tema":14,"practica":"Práctica general: escuchar y hablar en clase","examen_titulo":"Nivel jefe: escuchar y hablar en clase","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT14,"examen":EX14}

# ================= MISIÓN 15: COHESIÓN DEL TEXTO =================
B1=NV("Vas a usar conectores para enlazar ideas y que el texto fluya.",["Qué es la cohesión","Clases de conectores","Elegir el conector","Usarlos con medida"],[
 S(1,"Cohesión",[D("Cohesión","Conjunto de recursos que enlazan las partes de un texto para que se lea como un todo."),P("Un texto sin cohesión parece una lista de oraciones sueltas.")]),
 S(1,"Clases de conectores",[T("Conectores",["Función","Ejemplos"],[["Adición","además, también"],["Oposición","pero, sin embargo"],["Causa","porque, ya que"],["Consecuencia","por eso, entonces"],["Orden","primero, luego, finalmente"],["Ejemplo","por ejemplo"]])]),
 S(2,"Elegir",[P("Preguntate qué relación hay entre las dos ideas: ¿se suman?, ¿se oponen?, ¿una explica a la otra?, ¿una es resultado de la otra? Eso decide el conector.")]),
 S(2,"Con medida",[P("No hace falta un conector en cada oración: usalos donde la relación no sea obvia. Repetir siempre <i>y</i> o <i>entonces</i> empobrece el texto.")])],
 {"titulo":"unir","planteo":"Unir: «Estudié mucho. Aprobé el examen».","pasos":["La segunda idea es consecuencia de la primera.","Conector de consecuencia: por eso.","Estudié mucho; por eso aprobé el examen."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los conectores como «pero» y «sin embargo» expresan ___ .","Los conectores como «porque» expresan ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres pares de oraciones y unilos con conectores de distinta clase."},
 {"titulo":"Qué relación hay","texto":"Antes de elegir un conector, pensá cómo se relacionan las ideas."},
 ["Repetir siempre y o entonces.","Usar un conector que no corresponde."],
 RS(("Cohesión","Enlaza."),("Adición","Además."),("Oposición","Sin embargo."),("Causa y consecuencia","Porque y por eso.")),
 G(("Conector","Palabra que enlaza ideas."),("Cohesión","Unión entre las partes de un texto."),("Consecuencia","Resultado de algo.")),
 ["¿Qué conector expresa oposición: «sin embargo» o «además»?","¿Qué conector expresa consecuencia: «por eso» o «pero»?","¿«Porque» expresa causa o consecuencia?","¿Hace falta un conector en cada oración? Respondé sí o no."],
 [["sin embargo"],["por eso"],["causa","expresa causa"],["no"]],
 {"incompleto":"Oposición. Causa.","solo":"Estudié mucho; por eso aprobé. Es difícil; sin embargo, me gusta.","carpeta":["Sin embargo.","Por eso.","Causa.","No."]})
B2=NV("Vas a evitar repeticiones con pronombres, sinónimos y otros recursos de referencia.",["Repetir sin necesidad","Pronombres","Sinónimos y generales","Elipsis"],[
 S(1,"Repeticiones",[P("Repetir la misma palabra una y otra vez cansa. Para evitarlo hay recursos que <b>remiten</b> a algo ya dicho.")]),
 S(1,"Pronombres",[T("Antes y después",["Antes","Después"],[["Sofía llegó. Sofía saludó.","Sofía llegó. Ella saludó."],["Compré un libro y leí el libro.","Compré un libro y lo leí."]])]),
 S(2,"Sinónimos y generales",[T("Otros recursos",["Recurso","Ejemplo"],[["Sinónimo","casa → hogar, vivienda"],["Palabra general","perro → el animal"],["Descripción","Messi → el capitán argentino"]])]),
 S(2,"Elipsis",[D("Elipsis","Omisión de una palabra que se entiende por el contexto."),P("En <i>Sofía llegó y saludó</i>, no repetimos «Sofía» antes de «saludó».")])],
 {"titulo":"mejorar","planteo":"Mejorá: «María tiene un gato. El gato de María es negro. María quiere mucho al gato».","pasos":["Usar pronombres: ella, lo.","Usar un sinónimo o palabra general: el animal.","María tiene un gato negro y lo quiere mucho."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La palabra que reemplaza a un sustantivo es el ___ .","Omitir una palabra que se entiende es una ___ ."]},
 {"titulo":"tu turno","planteo":"Reescribí un párrafo repetitivo usando tres recursos distintos."},
 {"titulo":"Variá con sentido","texto":"Cambiá la palabra solo si el lector sigue sabiendo de qué hablás."},
 ["Cambiar tanto las palabras que no se entiende a qué se refiere.","Repetir el nombre en cada oración."],
 RS(("Referencia","Remite a algo dicho."),("Pronombre","Ella, lo."),("Sinónimo","Hogar por casa."),("Elipsis","Se omite.")),
 G(("Referencia","Palabra que remite a otra."),("Sinónimo","Palabra de significado parecido."),("Elipsis","Omisión de algo conocido.")),
 ["¿Qué palabra evita repetir «Sofía»?","«Hogar» por «casa», ¿es un sinónimo o un pronombre?","Omitir una palabra que se entiende por el contexto, ¿es una elipsis o un conector?","¿Se puede cambiar una palabra si el lector deja de entender? Respondé sí o no."],
 [["ella","un pronombre","pronombre"],["sinonimo","sinónimo","es un sinonimo","es un sinónimo"],["elipsis","una elipsis","es una elipsis"],["no"]],
 {"incompleto":"Pronombre. Elipsis.","solo":"María tiene un gato negro y lo quiere mucho.","carpeta":["Ella.","Sinónimo.","Elipsis.","No."]})
B3=NV("Vas a usar la coma, el punto y los párrafos para organizar las ideas.",["Los signos","Coma y punto","Dos puntos y punto y coma","Párrafos"],[
 S(1,"Los signos",[T("Cada signo, una pausa",["Signo","Función"],[["Coma","Pausa breve: enumera, aclara, separa conectores"],["Punto y seguido","Cierra una oración, el párrafo sigue"],["Punto y aparte","Cierra un párrafo"],["Punto final","Cierra el texto"]])]),
 S(1,"Coma",[T("Usos",["Uso","Ejemplo"],[["Enumerar","Compré pan, leche y queso."],["Después de un conector","Sin embargo, llegué tarde."],["Aclarar","Mi tía, que vive en Salta, vino."]])]),
 S(2,"Dos puntos y punto y coma",[T("Otros signos",["Signo","Uso"],[["Dos puntos","Antes de una enumeración o una cita"],["Punto y coma","Separa ideas relacionadas más largas que una coma"]])]),
 S(2,"Párrafos",[P("Un párrafo desarrolla <b>una idea principal</b>. Cuando cambia la idea, se hace <b>punto y aparte</b> y se empieza otro párrafo.")])],
 {"titulo":"puntuar","planteo":"Puntuá: «Compré manzanas peras y bananas sin embargo no compré uvas».","pasos":["Enumeración con comas: manzanas, peras y bananas.","Después del conector va coma: sin embargo,.","Compré manzanas, peras y bananas; sin embargo, no compré uvas."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El signo que cierra un párrafo es el punto y ___ .","Un párrafo desarrolla una sola idea ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un texto de dos párrafos con las comas y los puntos bien usados."},
 {"titulo":"Una idea, un párrafo","texto":"Si cambiás de idea, cambiá de párrafo."},
 ["Poner coma entre sujeto y verbo.","Escribir un texto en un solo bloque."],
 RS(("Coma","Pausa breve."),("Punto y seguido","Sigue el párrafo."),("Punto y aparte","Nuevo párrafo."),("Párrafo","Una idea.")),
 G(("Párrafo","Parte de un texto con una idea."),("Punto y aparte","Cierra un párrafo."),("Enumeración","Lista de elementos.")),
 ["¿Qué signo cierra un párrafo?","¿Qué signo cierra una oración pero el párrafo sigue?","¿Un párrafo desarrolla una idea o cinco?","¿Se pone coma después de «sin embargo»? Respondé sí o no."],
 [["punto y aparte","el punto y aparte"],["punto y seguido","el punto y seguido"],["una","una idea","1"],["si","sí"]],
 {"incompleto":"Aparte. Principal.","solo":"Dos párrafos: el primero presenta la idea; el segundo, el ejemplo.","carpeta":["Punto y aparte.","Punto y seguido.","Una.","Sí."]})
B4=NV("Vas a revisar la cohesión de un texto y reescribirlo mejorando conectores, referencias y puntuación.",["Leer como lector","Lista de revisión","Reescribir","Comparar"],[
 S(1,"Leer como lector",[P("Para revisar, leé el texto como si fueras otra persona: ¿se entiende sin explicarlo?, ¿las ideas pasan una a otra con naturalidad?")]),
 S(1,"Lista de revisión",[T("Preguntas",["Pregunta","Si no..."],[["¿Hay conectores donde hacen falta?","Agregarlos"],["¿Se repiten palabras sin necesidad?","Usar pronombres o sinónimos"],["¿Cada párrafo tiene una idea?","Dividir o unir"],["¿Los signos están bien puestos?","Corregir"]])]),
 S(2,"Reescribir",[P("Se reescribe de a una pasada por vez: primero los conectores, después las repeticiones y por último la puntuación.")]),
 S(2,"Comparar",[T("Antes y después",["Antes","Después"],[["Lucas fue al club. Lucas jugó. Lucas volvió tarde.","Lucas fue al club, jugó y volvió tarde."]])])],
 {"titulo":"revisar","planteo":"Revisá: «Fui a la plaza. Fui con mi perro. Mi perro corrió. Me cansé».","pasos":["Conector y elipsis: Fui a la plaza con mi perro.","Conector: El perro corrió y yo me cansé.","Versión: Fui a la plaza con mi perro, que corrió tanto que me cansé."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los recursos que evitan repetir palabras son los ___ y los sinónimos.","Cada párrafo desarrolla una sola ___ ."]},
 {"titulo":"tu turno","planteo":"Revisá un texto tuyo con la lista de revisión y reescribilo."},
 {"titulo":"Una pasada por vez","texto":"Revisar todo a la vez confunde: una pasada, un objetivo."},
 ["Revisar una sola vez y todo junto.","Agregar conectores sin pensar en la relación."],
 RS(("Revisar","Como lector."),("Lista","Conectores, repeticiones, párrafos, signos."),("Reescribir","Una pasada por vez."),("Comparar","Antes y después.")),
 G(("Revisar","Leer para mejorar."),("Reescribir","Escribir de nuevo mejorando.")),
 ["¿Cómo conviene revisar: todo a la vez o una pasada por vez?","¿Qué se usa para evitar repetir una palabra?","¿Qué agrega relaciones entre ideas: los conectores o los títulos?","¿Cada párrafo desarrolla una sola idea? Respondé sí o no."],
 [["una pasada por vez","una por vez","por vez"],["pronombres","pronombre","sinonimos","sinónimos"],["conectores","los conectores"],["si","sí"]],
 {"incompleto":"Pronombres. Idea.","solo":"Fui a la plaza con mi perro, que corrió tanto que me cansé.","carpeta":["Una pasada por vez.","Pronombres.","Los conectores.","Sí."]})
ACT15={"1":[FB("Los conectores como «sin embargo» expresan ___ .",[["oposicion","oposición"]],"Oponen ideas."),{"t":"classify","p":"¿Qué función cumple?","o":{"elementos":["además","por eso","pero","porque"],"categorias":["Adición","Consecuencia","Oposición","Causa"]},"r":{"categorias":{"además":"Adición","por eso":"Consecuencia","pero":"Oposición","porque":"Causa"}},"e":"Cada conector, su relación."}],
 "2":[TT("Tocá el pronombre que reemplaza a Sofía: «Sofía llegó tarde y ella se disculpó».",["Sofía","llegó","tarde","y","ella","se","disculpó"],[4],"Ella remite a Sofía."),{"t":"matching","p":"Uní cada recurso con su ejemplo.","o":{"izquierda":["Pronombre","Sinónimo","Palabra general","Elipsis"],"derecha":["Lo leí","Hogar por casa","El animal por el perro","Llegó y saludó"]},"r":{"pares":{"Pronombre":"Lo leí","Sinónimo":"Hogar por casa","Palabra general":"El animal por el perro","Elipsis":"Llegó y saludó"}},"e":"Recursos para no repetir."}],
 "3":[{"t":"ordering","p":"Ordená de menor a mayor la pausa que marcan.","o":["Punto y aparte","Coma","Punto y seguido"],"r":{"orden":["Coma","Punto y seguido","Punto y aparte"]},"e":"Coma, punto y seguido, punto y aparte."},MS("¿Dónde va coma?",["Después de «sin embargo»","Entre las frutas de una enumeración","Entre el sujeto y el verbo","Antes de una aclaración"],["Después de «sin embargo»","Entre las frutas de una enumeración","Antes de una aclaración"],"No se separa el sujeto del verbo.")],
 "4":[KW("Reescribí este texto mejorando la cohesión: «Fui al parque. Fui con mi hermano. Mi hermano llevó la pelota. Jugamos. Nos cansamos».","Usá conectores, pronombres o elipsis y buena puntuación.","Texto reescrito con conectores, pronombres o elipsis para evitar repeticiones, puntuación correcta y un párrafo coherente.","Se evalúa cohesión y puntuación."),TT("Tocá el conector de consecuencia: «Estudié mucho; por eso aprobé».",["Estudié","mucho;","por","eso","aprobé"],[2,3],"Por eso expresa consecuencia.")],
 "5":[MC("Relámpago. «Sin embargo» expresa…",["Oposición","Causa","Orden"],"Oposición","Contrasta.",tiempo=20),VF("Relámpago. Repetir una palabra sin necesidad mejora el texto.","Falso","Cansa al lector.",tiempo=20),MC("Relámpago. El punto y aparte cierra un…",["Párrafo","Verso","Título"],"Párrafo","Nueva idea.",tiempo=20),VF("Relámpago. Un párrafo desarrolla una idea principal.","Verdadero","Una idea por párrafo.",tiempo=20)]}
EX15=[[1,MC("La cohesión es…",["Lo que enlaza las partes de un texto","Un tipo de letra","Una rima","Un resumen"],"Lo que enlaza las partes de un texto","Hace que fluya.")],
 [1,MC("«Por eso» expresa…",["Consecuencia","Oposición","Causa","Orden"],"Consecuencia","Resultado.")],
 [1,VF("Hace falta un conector en cada oración.","Falso","Solo donde la relación no es obvia.")],
 [2,MC("¿Qué evita repetir un sustantivo?",["Un pronombre","Un título","Una firma","Una tilde"],"Un pronombre","Reemplaza al sustantivo.")],
 [2,FB("«Hogar» por «casa» es un ___ .",[["sinonimo","sinónimo"]],"Significado parecido.")],
 [2,VF("La elipsis omite una palabra que se entiende.","Verdadero","Por contexto.")],
 [3,MC("El signo que cierra un párrafo es…",["Punto y aparte","Coma","Dos puntos","Punto y coma"],"Punto y aparte","Nueva idea.")],
 [3,MS("Usos de la coma:",["Enumerar","Después de un conector","Separar sujeto y verbo","Aclarar"],["Enumerar","Después de un conector","Aclarar"],"No se separa sujeto y verbo.")],
 [3,VF("Un párrafo desarrolla muchas ideas distintas.","Falso","Una idea principal.")],
 [4,MC("Para revisar la cohesión conviene…",["Una pasada por vez","Todo a la vez","No leer","Cambiar el título"],"Una pasada por vez","Con un objetivo cada vez.")],
 [4,MS("Se revisa:",["Conectores","Repeticiones","Párrafos","Color del papel"],["Conectores","Repeticiones","Párrafos"],"El papel no cuenta.")],
 [4,FB("Los recursos que evitan repetir son los pronombres y los ___ .",[["sinonimos","sinónimos"]],"Y la elipsis.")],
 [4,VF("Al reescribir se puede cambiar el sentido del texto.","Falso","Se mejora la forma.")]]
M15={"subject_id":SID,"tema":15,"practica":"Práctica general: cohesión del texto","examen_titulo":"Nivel jefe: cohesión del texto","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT15,"examen":EX15}
for n,m in ((14,M14),(15,M15)):
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
STEPS={(14,1):"7a2ec037-f7ef-4ea0-b088-9bd6006a40a8",(14,2):"d3e5dd65-fb48-44b4-9f31-d6d18d090b99",(14,3):"755a15ad-005c-484f-8f01-d382866e0a4e",(14,4):"f5c85cb7-7cd4-4455-be07-500166bbf469",(15,1):"644960f1-90d7-48ce-8f43-6eebae2e10c8",(15,2):"2927bee0-65cb-4f55-8f6f-1a86b72467f0",(15,3):"9489ec38-dbbf-4975-84f4-73d662e5b6d0",(15,4):"ac736270-c794-41db-8650-d6aca94e7af8"}
TIT={(14,1):"Preparo una exposición",(14,2):"Escucho y tomo notas",(14,3):"Debatimos con respeto",(14,4):"Evaluamos nuestros debates",(15,1):"Palabras que enlazan ideas",(15,2):"Referencias y sustituciones",(15,3):"Puntuación y párrafos",(15,4):"Reviso la cohesión"}
RES=lambda v,items:{"t":"resumen","voz":v,"items":items,"fin":{"titulo":"¡CLASE TERMINADA!","sub":"Ahora, a practicar 🚀"}}
Q=lambda p,o,c,v:{"t":"pregunta","pregunta":p,"opciones":o,"correcta":c,"voz":v}
ER=lambda it,v:{"t":"errores","items":[{"mal":a,"bien":b} for a,b in it],"voz":v}
DEF=lambda w,t,e,v:{"t":"definicion","palabra":w,"texto":t,"emoji":e,"voz":v}
CMP=lambda a,b,s,v:{"t":"comparar","a":{"cab":a[0],"texto":a[1],"emoji":a[2]},"b":{"cab":b[0],"texto":b[1],"emoji":b[2]},"signo":s,"voz":v}
TB=lambda t,c,f,v:{"t":"tabla","titulo":t,"columnas":c,"filas":f,"voz":v}
CAU=lambda c,it,v:{"t":"causas","causa":{"txt":c[0],"emoji":c[1]},"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
CL=lambda cj,fi,v:{"t":"clasificar","cajas":[{"cab":a,"emoji":b} for a,b in cj],"fichas":[{"txt":a,"caja":b} for a,b in fi],"voz":v}
PA=lambda t,it,v:{"t":"pasos","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
AD=lambda a,d,v:{"t":"antesdespues","antes":{"cab":a[0],"emoji":a[1],"texto":a[2]},"despues":{"cab":d[0],"emoji":d[1],"texto":d[2]},"voz":v}
TU=lambda t,v:{"t":"consejo","titulo":"TU TURNO","texto":t,"emoji":"✍️","voz":v}
CLS={(14,1):[
 {"t":"reto","texto":"¿Cuáles son las tres partes de una exposición?","segundos":6,"respuesta":"Inicio, desarrollo y cierre","emoji":"🎤","titulo":"PREPARO UNA EXPOSICIÓN","sub":"orden, apoyos y voz","voz":["Desafío: ¿cuáles son las tres partes de una exposición? Seis segundos.","Inicio, desarrollo y cierre.","Hoy: *preparo una exposición*."]},
 PA("ESQUEMA",[("Inicio","👋"),("Desarrollo","📚"),("Cierre","🔚")],["Una exposición tiene tres partes.","El *inicio*: saludo y tema.","El *desarrollo*: tres o cuatro ideas con ejemplos.","Y el *cierre*: resumen y agradecimiento."]),
 CMP(("APOYO BUENO","Pocas palabras e imágenes","🖼️"),("APOYO MALO","Un párrafo para leer","📄"),"vs",["Los apoyos ayudan, pero no se leen.","Un buen apoyo tiene *pocas palabras*.","Uno malo es un *párrafo* para leer."]),
 TB("VOZ Y CUERPO",["Aspecto","Consejo"],[["Voz","Clara"],["Ritmo","Ni rápido ni lento"],["Mirada","Al público"],["Tiempo","Ensayar"]],["Cuidá cuatro cosas.","La *voz*, clara.","El *ritmo*, ni rápido ni lento.","La *mirada*, al público.","Y el *tiempo*: ensayá con reloj."]),
 CL([("SÍ","✅"),("NO","🚫")],[("Mirar al público",0),("Leer todo",1),("Ensayar con reloj",0)],["¿Conviene o no?","*Mirar al público* y *ensayar con reloj*: sí.","*Leer todo*: no."]),
 Q("¿Cuál es la última parte de una exposición?",["Cierre","Inicio","Desarrollo"],0,["Te toca: ¿cuál es la última parte?","¿Cierre, inicio o desarrollo?","El *cierre*."]),
 TU("Armá el esquema de una exposición de tres minutos",["Ahora te toca: armá el esquema de una exposición.","De *tres minutos*, con inicio, desarrollo y cierre."]),
 ER([("Leer todo de un papel","Mirar al público"),("Diapositivas llenas de texto","Pocas palabras")],["Errores típicos.","*Leer todo* de un papel.","Y llenar de *texto* los apoyos."]),
 RES(["Repasemos.","Una exposición tiene *inicio*, *desarrollo* y *cierre*.","Los apoyos llevan *pocas palabras*.","Cuidá la *voz*, la *mirada* y el *tiempo*.","Y *ensayá*.","¡Clase terminada! Ahora, *a practicar*."],[["PARTES","tres"],["APOYOS","pocas palabras"],["VOZ","clara"],["ENSAYO","con reloj"]])],
(14,2):[
 {"t":"historia","personaje":{"nombre":"Mica","emoji":"👧"},"lugar":"🎧","lineas":["Mica copió todo lo que dijo el profe.","Pero no entendió nada de lo que escuchó."],"titulo":"ESCUCHO Y TOMO NOTAS","sub":"escucha activa","voz":["Mica copió todo lo que dijo el profe.","Pero no entendió nada de lo que escuchó.","Hoy: *escucho y tomo notas*."]},
 DEF("Escucha activa","Escuchar con atención, sin interrumpir","👂",["La *escucha activa* es escuchar con atención y sin interrumpir.","Se busca entender y recordar."]),
 CL([("SE ANOTA","✅"),("NO HACE FALTA","🚫")],[("Fechas",0),("Palabras clave",0),("Chistes",1),("Números",0)],["¿Se anota o no?","*Fechas*, *palabras clave* y *números*: se anotan.","*Chistes*: no hace falta."]),
 TB("SÍMBOLOS",["Símbolo","Significa"],[["→","lleva a"],["=","es igual a"],["+","además"],["!","importante"]],["Símbolos para ahorrar tiempo.","La *flecha*: lleva a.","El *igual*: es igual a.","El *más*: además.","Y la *admiración*: importante."]),
 PA("DESPUÉS DE CLASE",[("Releo","📖"),("Subrayo","🖍️"),("Resumo","📝"),("Anoto dudas","❓")],["Después de la clase.","*Releo* y completo.","*Subrayo* lo principal.","Escribo un *resumen*.","Y anoto mis *dudas*."]),
 Q("¿Qué se anota al escuchar?",["Lo esencial","Todo textual","Nada"],0,["Te toca: ¿qué se anota al escuchar?","¿Lo esencial, todo textual o nada?","*Lo esencial*."]),
 ER([("Copiar todo textual","Anotar lo esencial"),("No repasar las notas","Repasar después")],["Errores típicos.","*Copiar todo* textual.","Y *no repasar* las notas."]),
 RES(["Repasemos.","La *escucha activa* busca entender.","Anotá *palabras clave*.","Usá *símbolos*.","Y *repasá* después de clase.","¡Clase terminada! Ahora, *a practicar*."],[["ESCUCHA","activa"],["NOTAS","palabras clave"],["SÍMBOLOS","ahorran tiempo"],["REPASO","después"]])],
(14,3):[
 {"t":"noticia","cinta":"DEBATE","titular":"Dos equipos, una idea: ¿tareas sí o no?","bajada":"Con turnos y respeto","emoji":"🎙️","titulo":"DEBATIMOS CON RESPETO","sub":"turnos, razones y escucha","voz":["Debate: dos equipos y una idea, ¿tareas sí o no?","Con turnos y respeto.","Hoy: *debatimos con respeto*."]},
 TB("ROLES",["Rol","Función"],[["Moderador","Da la palabra"],["A favor","Defiende"],["En contra","Cuestiona"],["Público","Escucha"]],["Los roles.","El *moderador* da la palabra.","El equipo *a favor* defiende.","El equipo *en contra* cuestiona.","Y el *público* escucha."]),
 CL([("RESPETO","🤝"),("FALTA DE RESPETO","🚫")],[("Pedir la palabra",0),("Interrumpir",1),("Criticar la idea",0),("Burlarse",1)],["¿Respeto o no?","*Pedir la palabra* y *criticar la idea*: respeto.","*Interrumpir* y *burlarse*: no."]),
 PA("REFUTAR",[("Reconozco","🤝"),("Discrepo","↔️"),("Propongo","🛠️")],["Para refutar sin atacar.","*Reconozco* algo.","*Discrepo* con una razón.","Y *propongo*."]),
 Q("¿Quién da la palabra en un debate?",["El moderador","El público","Nadie"],0,["Te toca: ¿quién da la palabra?","¿El moderador, el público o nadie?","El *moderador*."]),
 TU("Preparen dos argumentos a favor y dos en contra de un tema",["Ahora te toca: preparen argumentos.","Dos *a favor* y dos *en contra*."]),
 ER([("Interrumpir a los gritos","Esperar el turno"),("Burlarse del otro","Criticar la idea")],["Errores típicos.","*Interrumpir* a los gritos.","Y *burlarse* del otro."]),
 RES(["Repasemos.","El *debate* defiende ideas con razones.","Hay *moderador* y *equipos*.","Se respetan los *turnos*.","Y se *refuta* sin atacar.","¡Clase terminada! Ahora, *a practicar*."],[["DEBATE","con razones"],["ROLES","moderador y equipos"],["TURNOS","respeto"],["REFUTAR","sin atacar"]])],
(14,4):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"¿Cómo me fue en el debate? 😬"},{"yo":True,"txt":"Tus ejemplos fueron claros 👏"},{"yo":True,"txt":"Podés esperar más tu turno 🙂"}],"titulo":"EVALUAMOS NUESTROS DEBATES","sub":"devolución con respeto","voz":["Lu pregunta cómo le fue en el debate.","Juan: tus ejemplos fueron claros.","Y: podés esperar más tu turno.","Hoy: *evaluamos nuestros debates*."]},
 TB("CRITERIOS",["Criterio","Pregunta"],[["Claridad","¿Se entendió la tesis?"],["Argumentos","¿Hubo razones?"],["Respeto","¿Se respetaron turnos?"],["Tiempo","¿Se cumplió?"]],["Los criterios.","*Claridad*: ¿se entendió la tesis?","*Argumentos*: ¿hubo razones?","*Respeto*: ¿se respetaron turnos?","*Tiempo*: ¿se cumplió?"]),
 DEF("Grilla","Cuadro de criterios para evaluar","📊",["La *grilla* es un cuadro de criterios para evaluar.","Ordena lo que se mira."]),
 PA("UNA BUENA DEVOLUCIÓN",[("Un acierto","✅"),("Otro acierto","✅"),("Una mejora","🛠️")],["Una devolución útil.","Dos *aciertos*.","Y una *mejora*.","Siempre con *ejemplos*."]),
 CL([("DEVOLUCIÓN ÚTIL","✅"),("NO SIRVE","🚫")],[("Con ejemplos",0),("Estuvo bien",1),("Sobre la tarea",0),("Sobre la persona",1)],["¿Sirve o no?","*Con ejemplos* y *sobre la tarea*: sirven.","*Estuvo bien* y *sobre la persona*: no."]),
 Q("¿Cuántas mejoras lleva una devolución útil?",["Una","Diez","Ninguna"],0,["Te toca: ¿cuántas mejoras lleva una devolución?","¿Una, diez o ninguna?","*Una*."]),
 ER([("Devolución sin ejemplos","Con ejemplos concretos"),("Criticar a la persona","Criticar la tarea")],["Errores típicos.","*Sin ejemplos*.","Y criticar a la *persona*."]),
 RES(["Repasemos.","Evaluá con *criterios*.","Usá una *grilla*.","Da *dos aciertos* y *una mejora*.","Y *autoevaluate*.","¡Clase terminada! Ahora, *a practicar*."],[["CRITERIOS","claridad, respeto"],["GRILLA","ordena"],["DEVOLUCIÓN","dos y una"],["AUTOEVALUACIÓN","un objetivo"]])],
(15,1):[
 {"t":"antesdespues","antes":{"cab":"SUELTAS","emoji":"🧩","texto":"Estudié mucho. Aprobé."},"despues":{"cab":"ENLAZADAS","emoji":"🔗","texto":"Estudié mucho; por eso aprobé."},"titulo":"PALABRAS QUE ENLAZAN IDEAS","sub":"conectores","voz":["Sueltas: estudié mucho. Aprobé.","Enlazadas: estudié mucho; por eso aprobé.","Hoy: *palabras que enlazan ideas*."]},
 DEF("Cohesión","Enlaza las partes de un texto","🔗",["La *cohesión* enlaza las partes de un texto.","Sin ella, parece una lista de oraciones sueltas."]),
 TB("CONECTORES",["Función","Ejemplo"],[["Adición","además"],["Oposición","sin embargo"],["Causa","porque"],["Consecuencia","por eso"],["Orden","luego"]],["Clases de conectores.","*Adición*: además.","*Oposición*: sin embargo.","*Causa*: porque.","*Consecuencia*: por eso.","*Orden*: luego."]),
 CL([("OPOSICIÓN","↔️"),("CAUSA","❓"),("CONSECUENCIA","➡️")],[("pero",0),("porque",1),("por eso",2)],["¿Qué relación?","*Pero*: oposición.","*Porque*: causa.","*Por eso*: consecuencia."]),
 Q("¿Qué conector expresa oposición?",["Sin embargo","Además","Luego"],0,["Te toca: ¿qué conector expresa oposición?","¿Sin embargo, además o luego?","*Sin embargo*."]),
 ER([("Repetir siempre «y entonces»","Variar los conectores"),("Conector que no corresponde","Pensar la relación")],["Errores típicos.","Repetir *y entonces*.","Y usar un conector que *no corresponde*."]),
 RES(["Repasemos.","La *cohesión* enlaza.","Los *conectores* expresan adición, oposición, causa y consecuencia.","Elegí según la *relación*.","Y no abuses.","¡Clase terminada! Ahora, *a practicar*."],[["COHESIÓN","enlaza"],["CONECTORES","varias clases"],["ELEGIR","según la relación"],["MEDIDA","sin abusar"]])],
(15,2):[
 {"t":"reto","texto":"Evitá repetir: «María tiene un gato. El gato de María es negro».","segundos":8,"respuesta":"María tiene un gato negro","emoji":"🐈‍⬛","titulo":"REFERENCIAS Y SUSTITUCIONES","sub":"no repetir","voz":["Desafío: evitá repetir. María tiene un gato. El gato de María es negro. Ocho segundos.","María tiene un gato negro.","Hoy: *referencias y sustituciones*."]},
 TB("RECURSOS",["Recurso","Ejemplo"],[["Pronombre","Ella llegó"],["Sinónimo","casa, hogar"],["Palabra general","el animal"],["Elipsis","Llegó y saludó"]],["Recursos para no repetir.","El *pronombre*: ella llegó.","El *sinónimo*: casa y hogar.","La *palabra general*: el animal.","Y la *elipsis*: llegó y saludó."]),
 DEF("Elipsis","Omitir lo que se entiende por el contexto","✂️",["La *elipsis* omite una palabra que se entiende por el contexto.","En *Sofía llegó y saludó*, no repetimos Sofía."]),
 CL([("PRONOMBRE","👤"),("SINÓNIMO","🔁")],[("ella",0),("hogar",1),("lo",0),("vivienda",1)],["¿Pronombre o sinónimo?","*Ella* y *lo*: pronombres.","*Hogar* y *vivienda*: sinónimos."]),
 Q("¿Qué evita repetir «Sofía»?",["Ella","Pero","Luego"],0,["Te toca: ¿qué evita repetir «Sofía»?","¿Ella, pero o luego?","*Ella*."]),
 ER([("Repetir el nombre en cada oración","Pronombres y elipsis"),("Cambiar tanto que no se entiende","Variar con sentido")],["Errores típicos.","*Repetir* el nombre.","Y cambiar tanto que *no se entiende*."]),
 RES(["Repasemos.","Evitá repetir con *pronombres*.","Con *sinónimos*.","Con *palabras generales*.","Y con *elipsis*.","¡Clase terminada! Ahora, *a practicar*."],[["PRONOMBRE","ella, lo"],["SINÓNIMO","hogar"],["GENERAL","el animal"],["ELIPSIS","se omite"]])],
(15,3):[
 {"t":"gancho","grande":"1 idea","emoji":"📄","final":"por párrafo","titulo":"PUNTUACIÓN Y PÁRRAFOS","sub":"organizar el texto","voz":["Un párrafo, una idea.","Y los signos marcan las pausas.","Hoy: *puntuación y párrafos*."]},
 TB("SIGNOS",["Signo","Función"],[["Coma","Pausa breve"],["Punto y seguido","Sigue el párrafo"],["Punto y aparte","Nuevo párrafo"],["Punto final","Cierra el texto"]],["Cada signo, una pausa.","La *coma*: pausa breve.","El *punto y seguido*: sigue el párrafo.","El *punto y aparte*: nuevo párrafo.","Y el *punto final*: cierra el texto."]),
 TB("USOS DE LA COMA",["Uso","Ejemplo"],[["Enumerar","pan, leche y queso"],["Tras conector","Sin embargo, llegué"],["Aclarar","Mi tía, que vive en Salta"]],["Tres usos de la coma.","*Enumerar*.","Después de un *conector*.","Y para *aclarar*."]),
 CL([("COMA","➖"),("PUNTO Y APARTE","⏹️")],[("Enumerar",0),("Cambiar de idea",1),("Tras «sin embargo»",0)],["¿Qué signo?","*Enumerar* y después de *sin embargo*: coma.","*Cambiar de idea*: punto y aparte."]),
 Q("¿Qué signo cierra un párrafo?",["Punto y aparte","Coma","Dos puntos"],0,["Te toca: ¿qué signo cierra un párrafo?","¿Punto y aparte, coma o dos puntos?","*Punto y aparte*."]),
 TU("Escribí un texto de dos párrafos con comas y puntos bien usados",["Ahora te toca: escribí dos párrafos.","Cuidá las *comas* y los *puntos*."]),
 ER([("Coma entre sujeto y verbo","Sin coma"),("Todo en un solo bloque","Un párrafo por idea")],["Errores típicos.","Poner *coma* entre sujeto y verbo.","Y escribir *todo en un bloque*."]),
 RES(["Repasemos.","La *coma* marca una pausa breve.","El *punto y aparte* cierra un párrafo.","Un párrafo, *una idea*.","Y cambiá de párrafo al cambiar de idea.","¡Clase terminada! Ahora, *a practicar*."],[["COMA","pausa breve"],["PUNTO Y APARTE","nuevo párrafo"],["PÁRRAFO","una idea"],["REVISAR","los signos"]])],
(15,4):[
 {"t":"antesdespues","antes":{"cab":"ANTES","emoji":"😵","texto":"Fui al parque. Fui con mi hermano. Jugamos. Nos cansamos."},"despues":{"cab":"DESPUÉS","emoji":"😊","texto":"Fui al parque con mi hermano; jugamos tanto que nos cansamos."},"titulo":"REVISO LA COHESIÓN","sub":"reescribir mejor","voz":["Antes: fui al parque. Fui con mi hermano. Jugamos. Nos cansamos.","Después: fui al parque con mi hermano; jugamos tanto que nos cansamos.","Hoy: *reviso la cohesión*."]},
 PA("LISTA DE REVISIÓN",[("¿Conectores?","🔗"),("¿Repeticiones?","🔁"),("¿Párrafos?","📄"),("¿Signos?","✏️")],["Cuatro preguntas.","¿Hay *conectores* donde hacen falta?","¿Hay *repeticiones*?","¿Cada *párrafo* tiene una idea?","¿Están bien los *signos*?"]),
 DEF("Una pasada por vez","Un objetivo en cada lectura","1️⃣",["Revisá *una pasada por vez*.","Primero los conectores, después las repeticiones y por último los signos."]),
 CL([("MEJORA","✅"),("NO MEJORA","❌")],[("Pronombres",0),("Repetir nombre",1),("Conectores",0),("Todo junto",1)],["¿Mejora o no?","*Pronombres* y *conectores*: mejoran.","*Repetir nombre* y *todo junto*: no."]),
 Q("¿Cómo conviene revisar?",["Una pasada por vez","Todo a la vez","Sin leer"],0,["Te toca: ¿cómo conviene revisar?","¿Una pasada por vez, todo a la vez o sin leer?","*Una pasada por vez*."]),
 TU("Revisá un texto tuyo con la lista y reescribilo",["Ahora te toca: revisá un texto tuyo.","Usá la *lista de revisión* y reescribilo."]),
 ER([("Revisar todo a la vez","Una pasada por vez"),("Conectores sin pensar","Elegir según la relación")],["Errores típicos.","Revisar *todo a la vez*.","Y agregar *conectores sin pensar*."]),
 RES(["Repasemos.","Leé como *lector*.","Usá la *lista de revisión*.","Hacé *una pasada por vez*.","Y *comparé* antes y después.","¡Clase terminada! Ahora, *a practicar*."],[["LEER","como lector"],["LISTA","cuatro preguntas"],["PASADAS","una por vez"],["COMPARAR","antes y después"]])]}
for (m,n),es in CLS.items():
    json.dump({"slug":f"leng1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Lengua y Literatura I","titulo":TIT[(m,n)],"sub":f"Lengua y Literatura I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"leng1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
