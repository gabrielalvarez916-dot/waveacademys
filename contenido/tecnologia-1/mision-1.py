# -*- coding: utf-8 -*-
"""Tecnología I · Misión 1 · Diseñar productos y procesos (COMÚN). Genera mision-1.json y 4 clases."""
from tec import *
import numpy as np
CUB = [[x,y,0] for x in range(3) for y in range(2)] + [[0,0,1],[0,1,1]]
def img_vistas():
    fig, ax = plt.subplots(1, 3, figsize=(9, 3.0))
    vistas = {"FRENTE (x, z)": {(c[0],c[2]) for c in CUB}, "SUPERIOR (x, y)": {(c[0],c[1]) for c in CUB}, "LATERAL (y, z)": {(c[1],c[2]) for c in CUB}}
    for a,(t,pts) in zip(ax, vistas.items()):
        for (u,v) in pts: a.add_patch(plt.Rectangle((u,v),1,1,facecolor="#9fd0ff",edgecolor="#1b3a5c",lw=2))
        a.set_xlim(-0.3,3.3); a.set_ylim(-0.3,3.3); a.set_aspect("equal"); a.set_xticks([]); a.set_yticks([]); a.set_title(t, fontsize=11, fontweight="bold", color="#1b3a5c")
    return png(fig)
B1=NV("Vas a reconocer las fases del diseño y recorrerlas con un problema real, del problema a la solución.",["Diseñar es resolver","Problema, requisitos y restricciones","Ideas, elección y prototipo","Ensayo y mejora"],[
 S(1,"Diseñar es resolver",[D("Diseño","Proceso ordenado para crear un producto o un proceso que resuelva un problema concreto de las personas."),P("Diseñar no es dibujar algo lindo: es pensar para qué sirve, cómo se hace y cómo se comprueba que funciona. Por eso se hace en fases.")]),
 S(1,"Las fases",[T("Del problema a la solución",["Fase","Qué se hace"],[["Problema","Se define qué necesidad hay y para quién"],["Requisitos y restricciones","Se anota qué tiene que cumplir y qué límites hay: tiempo, materiales, costo"],["Ideas","Se proponen varias soluciones posibles"],["Elección","Se compara y se elige la mejor"],["Prototipo","Se arma un modelo para probar"],["Ensayo y mejora","Se prueba, se registra y se corrige"]])]),
 S(2,"Requisitos y restricciones",[P("Un <b>requisito</b> es lo que el producto tiene que cumplir (por ejemplo, sostener cinco lápices). Una <b>restricción</b> es un límite (por ejemplo, usar solo cartón y gastar poco). Anotarlos antes de dibujar evita rehacer todo.")]),
 S(2,"Un camino que se repite",[P("Las fases no son una escalera de un solo sentido: si el ensayo falla, se vuelve a las ideas o al prototipo. Mejorar es parte del diseño."),IM("Idea clave","Un buen diseño empieza por el problema, no por la solución.")])],
 {"titulo":"recorrer las fases","planteo":"Un grupo quiere diseñar un portalápices para el escritorio. ¿Cómo recorre las fases?","pasos":["Problema: los lápices están desparramados y se pierden.","Requisitos y restricciones: sostener cinco lápices; hacerlo con cartón y gastar poco.","Ideas y elección: se proponen tres formas y se elige la más estable.","Prototipo y ensayo: se arma, se prueba si se vuelca y se corrige la base."]},
 {"titulo":"completar","planteo":"Completá las fases de un diseño.","pasos":["Lo que el producto debe cumplir es un ___ .","Un límite como el costo o el tiempo es una ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un problema de tu casa (por ejemplo, los cargadores enredados) y escribí el problema, un requisito y una restricción."},
 {"titulo":"Primero el problema","texto":"Antes de dibujar, escribí en una frase qué problema resolvés y para quién."},
 ["Empezar a construir sin definir el problema.","Pensar que el diseño termina cuando se arma el prototipo."],
 RS(("Diseño","Proceso para resolver un problema."),("Requisito","Lo que debe cumplir."),("Restricción","Un límite."),("Ensayo","Probar y mejorar.")),
 G(("Diseño","Proceso para crear una solución."),("Requisito","Lo que el producto debe cumplir."),("Restricción","Límite de tiempo, costo o materiales."),("Prototipo","Modelo para probar.")),
 ["Un grupo arma un modelo de cartón para probar una idea. ¿Qué fase es?","Un compañero dice: «Ya sé qué voy a hacer, empiezo a cortar». ¿Qué fase se saltó?","Un portalápices no puede costar más de $500. ¿Es un requisito o una restricción?","Si el ensayo falla, ¿se vuelve a las ideas o al prototipo? Respondé ideas o prototipo."],
 ["aplicar","error","analizar","analizar"],
 [["prototipo","el prototipo"],["problema","definir el problema","requisitos","el problema"],["restriccion","restricción","una restriccion","una restricción"],["ideas","prototipo","las ideas","al prototipo"]],
 {"incompleto":"Requisito. Restricción.","solo":"Respuesta personal: problema, requisito y restricción de algo de tu casa.","carpeta":["Prototipo.","Problema.","Restricción.","Ideas o prototipo."]})
B2=NV("Vas a generar varias alternativas y elegir una con criterios claros, no por gusto.",["Más de una idea","Criterios de elección","Tabla de decisión","Justificar la elección"],[
 S(1,"Más de una idea",[P("La primera idea casi nunca es la mejor. Al proponer dos o tres alternativas se descubren ventajas y problemas que no se veían."),D("Alternativa","Una de las soluciones posibles para el mismo problema.")]),
 S(1,"Criterios de elección",[T("Criterios para comparar",["Criterio","Pregunta"],[["Función","¿Resuelve bien el problema?"],["Materiales","¿Los conseguimos y alcanzan?"],["Seguridad","¿Puede lastimar a alguien?"],["Costo aproximado","¿Entra en el presupuesto?"]])]),
 S(2,"Tabla de decisión",[T("Comparar tres alternativas (1 a 3 puntos)",["Alternativa","Función","Materiales","Seguridad","Costo","Total"],[["A: tubo de cartón","2","3","3","3","11"],["B: caja con divisiones","3","3","3","2","11"],["C: estructura de madera","3","1","2","1","7"]])]),
 S(2,"Justificar",[P("Si dos alternativas empatan, se desempata con el criterio que más pesa en el problema. Después se escribe la elección con una razón: «Elegimos B porque sostiene mejor los lápices y cuesta poco»."),IM("Idea clave","Elegir con criterios permite explicar la decisión a otras personas.")])],
 {"titulo":"desempatar","planteo":"Las alternativas A y B empatan con 11 puntos. El problema exige que el portalápices no se vuelque. ¿Cuál elegís?","pasos":["Se mira el criterio que más pesa: función (que no se vuelque).","B tiene 3 en función y A tiene 2.","Se elige B y se justifica con esa razón."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Cada solución posible para un mismo problema es una ___ .","Las preguntas con las que se compara se llaman ___ de elección."]},
 {"titulo":"tu turno","planteo":"Proponé dos alternativas para guardar los cargadores y compará con función, materiales, seguridad y costo."},
 {"titulo":"Un criterio no alcanza","texto":"Compará siempre con más de un criterio: una idea barata puede ser insegura."},
 ["Elegir «la que más me gusta» sin comparar.","Usar un solo criterio para decidir."],
 RS(("Alternativa","Una solución posible."),("Criterio","Lo que se compara."),("Tabla","Ordena la comparación."),("Justificar","Dar una razón.")),
 G(("Alternativa","Solución posible."),("Criterio","Aspecto con el que se compara."),("Desempatar","Decidir entre dos opciones iguales."),("Justificar","Explicar con razones.")),
 ["Una alternativa es barata pero puede lastimar. ¿Qué criterio la descarta?","Un compañero elige la alternativa «porque es la más linda». ¿Qué le falta?","Una alternativa suma 9 puntos y otra 12. Con los mismos criterios, ¿cuál conviene?","Dos alternativas empatan. ¿Qué se usa para desempatar?"],
 ["aplicar","error","aplicar","analizar"],
 [["seguridad","la seguridad"],["criterios","criterio","comparar","comparar con criterios"],["12","la de 12","la de 12 puntos","la segunda"],["criterio que mas pesa","el criterio que más pesa","el criterio principal","el que mas pesa","el que más pesa"]],
 {"incompleto":"Alternativa. Criterios.","solo":"Respuesta personal: dos alternativas comparadas con cuatro criterios.","carpeta":["Seguridad.","Criterios.","12.","El criterio que más pesa."]})
B3=NV("Vas a representar una pieza con perspectiva, las tres vistas (frente, superior y lateral) y un corte simple.",["Perspectiva","Las tres vistas","Cómo se lee una vista","El corte"],[
 S(1,"Perspectiva",[D("Perspectiva","Dibujo que muestra la pieza como la vemos, con volumen, en una sola imagen."),P("La perspectiva da una idea general del objeto, pero no permite medirlo bien.")]),
 S(1,"Las tres vistas",[T("Vistas",["Vista","Desde dónde se mira"],[["Frente","De frente, mostrando ancho y alto"],["Superior","Desde arriba, mostrando ancho y profundidad"],["Lateral","De costado, mostrando profundidad y alto"]]),IMG("Una pieza y sus tres vistas","Cada vista muestra solo dos dimensiones.","Tres cuadrículas azules: el frente con tres cuadrados abajo y uno arriba a la izquierda, la vista superior con un rectángulo de tres por dos y la lateral con un rectángulo de dos por dos.",img_vistas())]),
 S(2,"Cómo se leen",[P("Las tres vistas se combinan para imaginar la pieza completa: lo que una vista no muestra, lo muestra otra. Si una vista no coincide con las demás, hay un error en el dibujo.")]),
 S(2,"El corte",[D("Corte","Plano imaginario que atraviesa la pieza para mostrar cómo es por dentro."),P("Sirve para dibujar huecos, espesores y partes ocultas. Es como cortar un pan para ver la miga.")])],
 {"titulo":"elegir la vista","planteo":"Querés mostrar cuánta profundidad tiene un estante. ¿Qué vista usás?","pasos":["Profundidad se ve en la vista superior y en la lateral.","La vista de frente no muestra profundidad.","Se usa la vista superior o la lateral."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La vista que se mira desde arriba es la ___ .","El plano imaginario que muestra el interior es el ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un objeto simple (una caja o un libro) y dibujá su vista de frente, superior y lateral."},
 {"titulo":"Una vista, dos medidas","texto":"Cada vista muestra solo dos dimensiones: anotá cuáles antes de dibujar."},
 ["Confundir perspectiva con vista.","Dibujar una vista sin ver el objeto desde ese lado."],
 RS(("Perspectiva","Una imagen con volumen."),("Vistas","Frente, superior y lateral."),("Cada vista","Muestra dos medidas."),("Corte","Muestra el interior.")),
 G(("Perspectiva","Dibujo con volumen."),("Vista","Dibujo del objeto desde un lado."),("Corte","Plano que muestra el interior."),("Dimensión","Medida: ancho, alto o profundidad.")),
 ["Querés mostrar el ancho y la profundidad de una mesa. ¿Qué vista usás?","Un compañero dice que la vista de frente muestra la profundidad. ¿Qué vista la muestra además de la superior?","Para mostrar el grosor de la pared de un vaso, ¿hace falta una vista o un corte?","Querés medir el largo exacto de una pieza. ¿Usás la perspectiva o una vista?"],
 ["aplicar","error","aplicar","analizar"],
 [["superior","la superior","vista superior"],["lateral","la lateral","vista lateral"],["corte","un corte","el corte"],["no"]],
 {"incompleto":"Superior. Corte.","solo":"Respuesta personal: tres vistas dibujadas del mismo objeto.","carpeta":["Superior.","Lateral.","Corte.","Vista."]})
B4=NV("Vas a planear un ensayo: qué se prueba, con qué criterio se aprueba, cómo se registra y cómo se mejora.",["Del prototipo al ensayo","Criterio de aprobación","Registrar resultados","Mejorar y volver a ensayar"],[
 S(1,"Del prototipo al ensayo",[D("Ensayo","Prueba controlada del prototipo para comprobar si cumple los requisitos."),P("Un ensayo no es «ver qué pasa»: se decide antes qué se va a probar y cómo.")]),
 S(1,"Criterio de aprobación",[P("Para saber si el prototipo funciona hace falta un número o una condición clara. Por ejemplo, «sostiene cinco lápices sin volcarse al empujarlo suavemente»."),T("Ejemplo de ensayo",["Qué se prueba","Criterio para aprobar"],[["Estabilidad","No se vuelca al empujar con un dedo"],["Capacidad","Entran cinco lápices"],["Resistencia","Aguanta 1 kg sin deformarse"]])]),
 S(2,"Registrar resultados",[T("Tabla de registro",["Prueba","Resultado","¿Aprobó?"],[["Estabilidad","Se volcó a la segunda vez","No"],["Capacidad","Entran seis lápices","Sí"],["Resistencia","Se dobla con 1 kg","No"]])]),
 S(2,"Mejorar",[P("Con los resultados se decide qué cambiar: una base más ancha, un cartón más grueso. Después se vuelve a ensayar para comprobar que la mejora funcionó."),IM("Idea clave","Un ensayo sin criterio ni registro no sirve para decidir.")])],
 {"titulo":"leer un ensayo","planteo":"El portalápices se volcó en la prueba de estabilidad. ¿Qué se hace?","pasos":["Se registra: estabilidad, no aprobó.","Se busca la causa: la base es angosta.","Se mejora: se agranda la base y se refuerza.","Se vuelve a ensayar con el mismo criterio."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La prueba controlada de un prototipo es el ___ .","La condición que dice si aprobó es el criterio de ___ ."]},
 {"titulo":"tu turno","planteo":"Para un objeto que elijas, escribí qué probarías y con qué criterio aprobaría."},
 {"titulo":"Antes de probar","texto":"Escribí el criterio de aprobación antes de ensayar, así el resultado no se acomoda."},
 ["Probar sin decidir antes qué es «aprobar».","Mejorar el diseño y no volver a ensayar."],
 RS(("Ensayo","Prueba controlada."),("Criterio","Condición para aprobar."),("Registro","Anotar resultados."),("Mejora","Cambiar y volver a ensayar.")),
 G(("Ensayo","Prueba controlada del prototipo."),("Criterio de aprobación","Condición para decidir si aprobó."),("Registro","Anotación de resultados."),("Deformarse","Cambiar de forma al recibir una fuerza.")),
 ["Un prototipo se vuelca al empujarlo y el criterio pedía que no se vuelque. ¿Qué se registra: aprobó o no aprobó?","Un grupo cambia el diseño y no lo vuelve a probar. ¿Qué paso se saltó?","¿Qué se escribe antes de ensayar para saber si algo aprobó?","Un cartón se dobla con 1 kg y el criterio pedía aguantarlo. ¿Qué parte conviene cambiar: el material o el color?"],
 ["aplicar","error","analizar","aplicar"],
 [["no aprobo","no aprobó","no"],["ensayo","volver a ensayar","el ensayo","ensayar de nuevo"],["criterio","criterio de aprobacion","criterio de aprobación","el criterio"],["material","el material","cambiar el material"]],
 {"incompleto":"Ensayo. Criterio.","solo":"Respuesta personal: una prueba con su criterio de aprobación.","carpeta":["No aprobó.","Ensayo.","Criterio.","Material."]})
ACT={"1":[ORD("Ordená las fases del diseño.",["Prototipo","Problema","Elección","Ideas"],["Problema","Ideas","Elección","Prototipo"],"Se parte del problema y se llega al prototipo.",n="aplicar"),
  CLF("¿Requisito o restricción?",["Sostener cinco lápices","Usar solo cartón","Costar menos de $500","Ser estable"],["Requisito","Restricción"],{"Sostener cinco lápices":"Requisito","Usar solo cartón":"Restricción","Costar menos de $500":"Restricción","Ser estable":"Requisito"},"El requisito es lo que debe cumplir; la restricción, el límite.",n="aplicar")],
 "2":[MS("¿Qué criterios sirven para comparar alternativas?",["Función","Seguridad","Costo aproximado","El color favorito de quien dibuja"],["Función","Seguridad","Costo aproximado"],"El gusto personal no es un criterio técnico.",n="analizar"),
  KW("Un compañero elige «la que más me gusta». Explicá qué le falta.","Escribí una frase.",[["criterio*","comparar*","compar*"],["razon*","razón","justific*","explic*"]],1,"Hay que comparar con criterios y justificar la elección.",n="error")],
 "3":[MAT("Uní cada vista con lo que muestra.",["Frente","Superior","Lateral","Corte"],["Ancho y alto","Ancho y profundidad","Profundidad y alto","Interior de la pieza"],"Cada vista muestra solo dos dimensiones.",n="aplicar"),
  TT("Tocá la vista que muestra la profundidad: «La vista de frente muestra ancho y alto; la vista lateral muestra profundidad».",["La","vista","de","frente","muestra","ancho","y","alto;","la","vista","lateral","muestra","profundidad."],[9,10],"La lateral muestra profundidad y alto.",n="analizar")],
 "4":[ORD("Ordená los pasos de un ensayo.",["Mejorar y volver a ensayar","Definir el criterio","Registrar resultados","Probar"],["Definir el criterio","Probar","Registrar resultados","Mejorar y volver a ensayar"],"Primero el criterio, al final la mejora.",n="aplicar"),
  KW("El prototipo se volcó en la prueba de estabilidad. Explicá qué se hace después.","Escribí una frase.",[["registr*","anot*"],["mejor*","cambi*","corre*","agrand*"]],2,"Se registra, se mejora y se vuelve a ensayar.",n="analizar")],
 "5":[MC("Relámpago. ¿Qué va primero en el diseño?",["El problema","El prototipo","El ensayo"],"El problema","Se parte de la necesidad.",tiempo=20,n="recordar"),
  VF("Relámpago. Una restricción es un límite.","Verdadero","Como el costo o los materiales.",tiempo=15,n="recordar"),
  MC("Relámpago. ¿Qué vista se mira desde arriba?",["Superior","Frente","Lateral"],"Superior","Se ve ancho y profundidad.",tiempo=20,n="recordar"),
  FB("Relámpago. La prueba controlada del prototipo es el ___ .",[["ensayo"]],"Se comprueba si cumple.",tiempo=25,n="recordar")]}
EX=[[1,MC("Un grupo arma un modelo para probar una idea. ¿Qué fase es?",["Prototipo","Problema","Elección","Ideas"],"Prototipo","Es un modelo para probar.",n="aplicar")],
 [1,ORD("Ordená las fases.",["Elección","Ensayo y mejora","Problema","Ideas","Prototipo"],["Problema","Ideas","Elección","Prototipo","Ensayo y mejora"],"Del problema a la mejora.",n="aplicar")],
 [1,VF("Un compañero dice: «Ya sé qué hacer, empiezo a construir sin definir el problema». Eso es correcto.","Falso","Se salteó la definición del problema.",n="error")],
 [2,MS("¿Qué criterios sirven para comparar?",["Función","Seguridad","Materiales","Cuánto me gusta"],["Función","Seguridad","Materiales"],"El gusto no es técnico.",n="analizar")],
 [2,CLF("¿Requisito o restricción?",["Sostener cinco lápices","Usar solo cartón","No pasar de $500","No volcarse"],["Requisito","Restricción"],{"Sostener cinco lápices":"Requisito","Usar solo cartón":"Restricción","No pasar de $500":"Restricción","No volcarse":"Requisito"},"Requisito: lo que debe cumplir. Restricción: el límite.",n="aplicar")],
 [2,KW("Dos alternativas empatan. Explicá cómo se desempata.","Escribí una frase.",[["criterio*"],["pes*","import*","principal*"]],2,"Se usa el criterio que más pesa en el problema.",n="analizar")],
 [3,MAT("Uní cada vista con lo que muestra.",["Frente","Superior","Lateral"],["Ancho y alto","Ancho y profundidad","Profundidad y alto"],"Cada vista muestra dos dimensiones.",n="aplicar")],
 [3,MC("Para mostrar el grosor de la pared de un vaso conviene…",["Un corte","La vista superior","Una perspectiva","La vista de frente"],"Un corte","El corte muestra el interior.",n="aplicar")],
 [3,VF("La perspectiva permite medir la pieza con precisión.","Falso","Da idea general; para medir se usan las vistas.",n="analizar")],
 [4,FB("La condición que dice si un prototipo aprobó es el criterio de ___ .",[["aprobacion","aprobación"]],"Se escribe antes de ensayar.",n="recordar")],
 [4,KW("El prototipo se volcó. Explicá qué se hace.","Escribí una frase.",[["registr*","anot*"],["mejor*","cambi*","corre*"],["ensay*","prob*"]],2,"Se registra, se mejora y se vuelve a ensayar.",n="analizar")],
 [4,MC("Un grupo mejora el diseño y no lo vuelve a probar. ¿Qué se saltó?",["El nuevo ensayo","El problema","La elección","El dibujo"],"El nuevo ensayo","Hay que comprobar la mejora.",n="error")],
 [4,ORD("Ordená los pasos de un ensayo.",["Registrar","Probar","Definir el criterio","Mejorar"],["Definir el criterio","Probar","Registrar","Mejorar"],"El criterio va primero.",n="aplicar")]]
M={"subject_id":SID,"tema":1,"practica":"Práctica general: diseñar productos y procesos","examen_titulo":"Nivel jefe: diseñar productos y procesos","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT,"examen":EX}
STEPS={1:"5eb5a210-a324-4a44-a2b9-fbf49426affb",2:"2e19cf4c-5469-469c-a539-c6c5f39922ed",3:"b0b825d5-cc19-4f7a-86be-27d19597fc71",4:"372a1b3d-e53b-4b66-94b4-f9fcc65b93e8"}
TIT={1:"Fases del diseño: del problema a la solución",2:"Buscar alternativas y elegir una",3:"Vistas, cortes y perspectivas",4:"Del diseño al ensayo"}
CLS={1:[
 RET("¿Cómo se llama lo que un producto tiene que cumplir?",6,"Requisito","📐","DISEÑAR","del problema a la solución",["Desafío: ¿cómo se llama lo que un producto tiene que cumplir? Seis segundos.","Requisito.","Hoy: *las fases del diseño*."]),
 FL("LAS FASES DEL DISEÑO",[("Problema","❓"),("Ideas","💡"),("Elección","✅"),("Prototipo","🛠️")],["Primero, el *problema*.","Después, las *ideas*.","Luego, la *elección*.","Y por último, el *prototipo*."]),
 CMP(("REQUISITO","Lo que debe cumplir","✔️"),("RESTRICCIÓN","Un límite: costo, tiempo","⛔"),"vs",["Dos cosas que se anotan antes de dibujar.","El *requisito* es lo que debe cumplir.","La *restricción* es un límite."]),
 CIC("DISEÑAR ES REPETIR",[("Probar","🧪"),("Registrar","📝"),("Mejorar","🔧")],["El diseño no termina al armar.","*Probar*.","*Registrar* lo que pasa.","Y *mejorar*, para volver a probar."]),
 Q("¿Qué va primero al diseñar?",["El problema","El prototipo","La pintura"],0,["Te toca: ¿qué va primero?","¿El problema, el prototipo o la pintura?","El *problema*."]),
 ER([("Empezar a construir ya","Primero definir el problema"),("Diseñar es dibujar lindo","Es resolver un problema")],["Errores típicos.","*Construir ya*, sin definir el problema.","Y creer que diseñar es *dibujar lindo*."]),
 RES(["Repasemos.","Se parte del *problema*.","Se anotan *requisitos* y *restricciones*.","Se eligen ideas y se arma un *prototipo*.","Y se *ensaya y mejora*.","¡Clase terminada! Ahora, *a practicar*."],[["PROBLEMA","qué resolver"],["REQUISITOS","lo que debe cumplir"],["PROTOTIPO","modelo para probar"],["ENSAYO","probar y mejorar"]])],
2:[
 NOT("TECNOLOGÍA","Tres ideas para un mismo problema","Elegir bien empieza por comparar","⚖️","BUSCAR ALTERNATIVAS","y elegir una",["Noticia: tres ideas para un mismo problema.","Elegir bien empieza por comparar.","Hoy: *buscar alternativas y elegir una*."]),
 DEF("Alternativa","Una solución posible al mismo problema","💡",["Una *alternativa* es una solución posible.","Casi nunca la primera idea es la mejor."]),
 MZ("CUATRO CRITERIOS",[("FUNCIÓN","¿Resuelve el problema?"),("MATERIALES","¿Los conseguimos?"),("SEGURIDAD","¿Puede lastimar?"),("COSTO","¿Entra en el presupuesto?")],["Los criterios para comparar.","*Función*: ¿resuelve el problema?","*Materiales*: ¿los conseguimos?","*Seguridad*: ¿puede lastimar?","Y *costo*: ¿entra en el presupuesto?"]),
 CMP(("ALTERNATIVA A","Tubo de cartón: 11 puntos","🥫"),("ALTERNATIVA B","Caja con divisiones: 11 puntos","📦"),"=",["Dos alternativas empatan.","La *A* suma once.","La *B* también suma once."]),
 Q("A y B empatan. ¿Qué se hace?",["Usar el criterio que más pesa","Tirar una moneda","Elegir la más linda"],0,["Te toca: A y B empatan.","¿Criterio que más pesa, moneda o la más linda?","El *criterio que más pesa*."]),
 ER([("Elegir la que más me gusta","Comparar con criterios"),("Usar un solo criterio","Usar varios")],["Errores típicos.","Elegir *la que más gusta*.","Y mirar *un solo criterio*."]),
 RES(["Repasemos.","Se proponen *varias alternativas*.","Se comparan con *criterios*.","Se usa una *tabla*.","Y se *justifica* la elección.","¡Clase terminada! Ahora, *a practicar*."],[["ALTERNATIVAS","más de una"],["CRITERIOS","función, seguridad, costo"],["TABLA","ordena la comparación"],["JUSTIFICAR","dar una razón"]])],
3:[
 RET("¿Qué vista se mira desde arriba?",6,"Superior","👁️","VISTAS Y CORTES","representar una pieza",["Desafío: ¿qué vista se mira desde arriba? Seis segundos.","La superior.","Hoy: *vistas, cortes y perspectivas*."]),
 VIS("UNA PIEZA Y SUS VISTAS",CUB,["Esta es la pieza en perspectiva.","Así se ve de *frente*.","Así se ve desde *arriba*.","Y así de *costado*."]),
 TB("QUÉ MUESTRA CADA VISTA",["Vista","Medidas"],[["Frente","Ancho y alto"],["Superior","Ancho y profundidad"],["Lateral","Profundidad y alto"]],["Cada vista muestra solo dos medidas.","El *frente*: ancho y alto.","La *superior*: ancho y profundidad.","La *lateral*: profundidad y alto."]),
 CMP(("PERSPECTIVA","Una imagen con volumen","🧊"),("VISTA","Un solo lado, medible","📐"),"vs",["Dos formas de dibujar.","La *perspectiva* da una idea general.","La *vista* muestra un lado y permite medir."]),
 DEF("Corte","Plano imaginario que muestra el interior","🔪",["Un *corte* es un plano imaginario.","Muestra cómo es la pieza por dentro."]),
 Q("¿Qué vista muestra el ancho y la profundidad?",["Superior","Frente","Lateral"],0,["Te toca: ancho y profundidad.","¿Superior, frente o lateral?","La *superior*."]),
 RES(["Repasemos.","La *perspectiva* muestra el volumen.","Hay tres vistas: *frente*, *superior* y *lateral*.","Cada una muestra dos medidas.","Y el *corte* muestra el interior.","¡Clase terminada! Ahora, *a practicar*."],[["PERSPECTIVA","volumen"],["VISTAS","tres, dos medidas cada una"],["CORTE","el interior"],["COMBINAR","imaginar la pieza"]])],
4:[
 NOT("TECNOLOGÍA","El prototipo se volcó","¿Y ahora qué?","🧪","DEL DISEÑO AL ENSAYO","probar, registrar y mejorar",["Noticia: el prototipo se volcó.","¿Y ahora qué?","Hoy: *del diseño al ensayo*."]),
 DEF("Ensayo","Prueba controlada del prototipo","🧪",["Un *ensayo* es una prueba controlada.","Se decide antes qué se prueba y cómo."]),
 PA("PASOS DE UN ENSAYO",[("Definir el criterio","🎯"),("Probar","🧪"),("Registrar","📝"),("Mejorar","🔧")],["Cuatro pasos, en orden.","Primero el *criterio de aprobación*.","Después *probar*.","Luego *registrar* el resultado.","Y *mejorar*, para volver a ensayar."]),
 BQ("TABLA DE REGISTRO",[("ESTABILIDAD","No aprobó"),("CAPACIDAD","Aprobó"),("RESISTENCIA","No aprobó")],["Un registro de ejemplo.","*Estabilidad*: no aprobó.","*Capacidad*: aprobó.","*Resistencia*: no aprobó."]),
 AD(("ANTES","🔻","Base angosta: se vuelca"),("DESPUÉS","✅","Base ancha: aprueba"),["Antes se volcaba.","Con la base más ancha, aprueba."]),
 Q("¿Qué se escribe antes de ensayar?",["El criterio de aprobación","El resultado","La nota"],0,["Te toca: antes de ensayar.","¿Criterio, resultado o nota?","El *criterio de aprobación*."]),
 RES(["Repasemos.","El *ensayo* prueba el prototipo.","Se define un *criterio* antes.","Se *registra* lo que pasa.","Y se *mejora* y se vuelve a ensayar.","¡Clase terminada! Ahora, *a practicar*."],[["ENSAYO","prueba controlada"],["CRITERIO","condición para aprobar"],["REGISTRO","anotar resultados"],["MEJORA","cambiar y volver a probar"]])]}
escribir(1, M, STEPS, TIT, CLS)
