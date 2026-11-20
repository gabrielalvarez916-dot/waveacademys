# -*- coding: utf-8 -*-
"""Ciencias Naturales Integradas I · Misión 1 · Ciencia y método. Genera mision-1.json (se carga con cargar_mision)."""
import os, sys, io, base64, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "matematica-1", "mision-4"))
from base import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
V, O, C = "#0e7c7b", "#243b3f", "#d8f0ea"
def png(fig):
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig)
    im = Image.open(io.BytesIO(b.getvalue())).convert("RGB").quantize(colors=16); o = io.BytesIO(); im.save(o, format="PNG", optimize=True); return base64.b64encode(o.getvalue()).decode()
def IMG(t, pie, desc, b64): return {"tipo":"imagen","imagen_tipo":"diagrama","titulo":t,"texto":pie,"imagen_descripcion":desc,"imagen_fuente":"Dibujo propio (matplotlib).","png_base64":b64}
LEC="Leé el cuento «La liga de los pelirrojos», de Arthur Conan Doyle (está en la biblioteca de la plataforma o en cualquier edición de Las aventuras de Sherlock Holmes)."
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]

from matplotlib.patches import Rectangle, Ellipse
def fig_tunel():
    fig, ax = plt.subplots(figsize=(7, 3)); ax.axis("off"); ax.set_xlim(0, 14); ax.set_ylim(0, 6)
    ax.add_patch(Rectangle((0, 4.2), 14, 1.8, color="#d8f0ff")); ax.add_patch(Rectangle((0, 0), 14, 4.2, color="#8a5a35")); ax.add_patch(Rectangle((0, 4.0), 14, .25, color="#5daa45"))
    ax.add_patch(Rectangle((1.5, 4.25), 2.6, 1.4, color="#e9d5b0", ec=O)); ax.text(2.8, 5.0, "Casa de\nWilson", ha="center", va="center", fontsize=8, color=O)
    ax.add_patch(Rectangle((9.6, 4.25), 3.2, 1.5, color="#c9d3df", ec=O)); ax.text(11.2, 5.0, "Banco", ha="center", va="center", fontsize=9, color=O, weight="bold")
    ax.add_patch(Ellipse((2.8, 3.3), 2.4, 1.0, color="#3d2512")); ax.text(2.8, 3.3, "sótano", ha="center", va="center", color="white", fontsize=8)
    ax.add_patch(Ellipse((11.2, 3.0), 2.8, 1.2, color="#3d2512")); ax.text(11.2, 3.0, "bóveda (oro)", ha="center", va="center", color="#f4b63f", fontsize=8, weight="bold")
    ax.plot([2.8, 2.8, 11.2, 11.2], [2.8, 1.2, 1.2, 2.4], color="#2e1b0d", lw=10, solid_capstyle="round"); ax.text(7, 0.55, "túnel cavado por John Clay", ha="center", color="white", fontsize=9, weight="bold")
    return png(fig)

N1=NV("Vas a reconocer el cuento policial, sus personajes y el método de Sherlock Holmes.",["El cuento policial","Los personajes","El método de Holmes"],[
 S(1,"El cuento policial",[D("Cuento policial","Relato con un <b>enigma</b> (un misterio) que un <b>detective</b> resuelve."),P(LEC)]),
 S(1,"Los personajes",[T("Personajes",["Rol","En el cuento"],[["Detective","Sherlock Holmes"],["Ayudante y narrador","El doctor Watson"],["Cliente","Jabez Wilson, prestamista pelirrojo"],["Culpable","John Clay"]])]),
 S(2,"El método de Holmes",[P("Holmes <b>observa</b> cada detalle, <b>junta pistas</b>, <b>deduce</b> con lógica y <b>comprueba</b> antes de acusar. Nunca adivina."),E("Una deducción","Al conocer a Wilson, Holmes nota su manga derecha gastada y brillante.",["La manga se gasta al apoyarla en un escritorio.","Deduce que escribió mucho últimamente.","Era cierto: Wilson copiaba la enciclopedia."])])],
 {"titulo":"deducir","planteo":"Una persona tiene barro fresco en los zapatos y el paraguas mojado. ¿Qué deducís?","pasos":["Barro fresco: caminó por tierra hace poco.","Paraguas mojado: llueve o llovió.","Conclusión: viene de afuera, de un lugar con tierra, bajo la lluvia."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El narrador de los casos de Holmes es ___ .","El misterio de un policial se llama ___ ."]},
 {"titulo":"el cliente","planteo":"Según el cuento, ¿qué trabajo hacía Jabez Wilson para la liga?"},
 {"titulo":"Observá como Holmes","texto":"Mientras leés, anotá en tu carpeta cada detalle raro que aparezca. Muchos son pistas."},
 ["Confundir adivinar con deducir.","Creer que Holmes narra: narra Watson."],
 RS(("Policial","Enigma y detective."),("Detective","Sherlock Holmes."),("Narrador","Watson."),("Método","Observar, juntar pistas, deducir.")),
 G(("Enigma","Misterio que hay que resolver."),("Detective","Quien investiga."),("Deducir","Sacar una conclusión lógica de pistas."),("Cliente","Quien trae el caso.")),
 ["¿Cómo se llama el detective del cuento?","¿Quién narra las historias de Holmes?","¿De qué color tenía el pelo Jabez Wilson?","¿Cuál es el oficio de Jabez Wilson: prestamista o médico?"],
 [["sherlock holmes","holmes","sherlock"],["watson","el doctor watson","doctor watson"],["rojo","pelirrojo","colorado"],["prestamista"]],
 {"incompleto":"Watson. Enigma.","solo":"Copiar a mano la enciclopedia, cuatro horas por día.","carpeta":["Sherlock Holmes.","El doctor Watson.","Rojo (pelirrojo).","Prestamista."]})
N2=NV("Vas a distinguir pistas de falsas pistas en «La liga de los pelirrojos».",["Pista y falsa pista","El caso de Wilson","Detalles que importan"],[
 S(1,"Pista y falsa pista",[D("Pista","Dato que acerca a la verdad."),D("Falsa pista","Dato que distrae y hace mirar al lado equivocado.")]),
 S(1,"El caso",[P("Wilson ve un aviso que le muestra su ayudante, Vincent Spaulding. La Liga de los Pelirrojos le paga cuatro libras por semana por copiar la enciclopedia, cuatro horas por día. A las ocho semanas, la liga desaparece.")]),
 S(2,"Detalles que importan",[T("Pistas del cuento",["Detalle","Por qué importa"],[["El ayudante cobra la mitad del sueldo","Tiene otro interés en estar ahí"],["Pasa horas en el sótano","Hace algo escondido"],["Tiene las rodillas gastadas","Excava"],["Hay un banco detrás de la casa","Allí está el oro"]]),P("La liga y la enciclopedia son la <b>gran distracción</b>: sirven para sacar a Wilson de su casa.")])],
 {"titulo":"pensar el motivo","planteo":"¿Para qué alguien inventaría una liga que paga por copiar una enciclopedia?","pasos":["El trabajo no tiene utilidad real.","Obliga a Wilson a salir cuatro horas por día.","Alguien necesita la casa vacía.","La liga es una trampa."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un dato que distrae se llama ___ pista.","El ayudante tenía las ___ gastadas."]},
 {"titulo":"tu pista","planteo":"Elegí una pista del cuento y explicá en tu carpeta qué te hace pensar."},
 {"titulo":"Desconfiá de lo llamativo","texto":"En un policial, lo más raro suele ser la distracción; la verdad está en los detalles chicos."},
 ["Creer el primer dato llamativo.","Ignorar los detalles chicos."],
 RS(("Pista","Acerca a la verdad."),("Falsa pista","Distrae."),("El caso","La liga era una trampa."),("Clave","Los detalles chicos.")),
 G(("Pista","Dato útil para resolver."),("Falsa pista","Dato que confunde."),("Liga","Asociación de personas."),("Prestamista","Quien presta dinero con interés.")),
 ["¿Cuántas libras por semana pagaba la liga?","¿Cuántas semanas trabajó Wilson para la liga?","¿Dónde pasaba horas el ayudante?","¿La liga era una pista o una distracción?"],
 [["4","cuatro"],["8","ocho"],["sotano","sótano","en el sotano","en el sótano"],["distraccion","distracción","una distraccion","una distracción","falsa pista"]],
 {"incompleto":"Falsa. Rodillas.","solo":"Respuesta personal: nombrá la pista y qué sugiere.","carpeta":["Cuatro.","Ocho.","En el sótano.","Una distracción."]})
N3=NV("Vas a reconstruir el caso uniendo las pistas y reconocer las dos historias del policial.",["Unir pistas","Las dos historias","La revelación"],[
 S(1,"Unir pistas",[E("La deducción de Holmes","Holmes visita la casa de Wilson.",["Golpea la vereda con el bastón: busca un hueco.","Mira las rodillas del ayudante: gastadas de excavar.","Ve que detrás está el banco.","Deduce: un túnel hasta la bóveda del banco."]),IMG("El plan de los ladrones","Del sótano de Wilson a la bóveda del banco.","Corte del terreno: la casa de Wilson con su sótano, un túnel bajo tierra y la bóveda del banco con oro.",fig_tunel())]),
 S(1,"Las dos historias",[T("Dos historias",["Historia","Qué cuenta"],[["Del crimen","Clay cava un túnel para robar el oro del banco"],["De la investigación","Holmes reúne pistas y lo descubre"]])]),
 S(2,"La revelación",[P("Holmes, Watson y la policía esperan de noche en la bóveda del banco. Atrapan a <b>John Clay</b>, el falso ayudante, cuando sale del túnel. Después Holmes explica cómo lo dedujo: esa es la <b>revelación</b>.")])],
 {"titulo":"ordenar","planteo":"Ordená la deducción de Holmes.","pasos":["El ayudante pasa horas en el sótano.","Tiene las rodillas gastadas.","El banco está detrás de la casa.","Conclusión: un túnel al banco."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El verdadero nombre del ayudante era John ___ .","Holmes golpea la vereda con su ___ ."]},
 {"titulo":"tu resumen","planteo":"Escribí en tu carpeta el caso en cinco oraciones, en orden."},
 {"titulo":"Usá porque","texto":"Para explicar una deducción, uní las pistas con porque y entonces: así se ve la lógica."},
 ["Contar el caso desordenado.","Dar la solución sin explicar las pistas."],
 RS(("Dos historias","Crimen e investigación."),("Deducción","Unir pistas con lógica."),("Revelación","El detective explica."),("Culpable","John Clay.")),
 G(("Bóveda","Lugar seguro del banco."),("Túnel","Pasaje bajo tierra."),("Revelación","Explicación final del caso."),("Reconstruir","Contar lo que pasó en orden.")),
 ["¿Cómo se llamaba en realidad el ayudante de Wilson?","¿Qué querían robar los ladrones del banco: oro o cuadros?","¿Qué estaban cavando desde el sótano?","¿Con qué golpea Holmes la vereda?"],
 [["john clay","clay"],["oro"],["tunel","túnel","un tunel","un túnel"],["baston","bastón","su baston","su bastón","con su bastón","con el bastón"]],
 {"incompleto":"Clay. Bastón.","solo":"Respuesta personal en cinco oraciones ordenadas.","carpeta":["John Clay.","Oro.","Un túnel.","Con su bastón."]})
N4=NV("Vas a planificar y escribir un enigma breve con pistas y revelación.",["Planificar","Estructura","Juego limpio"],[
 S(1,"Planificar",[T("Plan",["Parte","Qué decido"],[["Misterio","Qué pasó"],["Detective","Quién investiga"],["Pistas","Dos verdaderas y una falsa"],["Revelación","Cómo se resuelve"]])]),
 S(1,"Estructura",[P("Situación inicial: aparece el <b>enigma</b>. Desarrollo: la <b>investigación</b>, pista por pista. Desenlace: la <b>revelación</b>.")]),
 S(2,"Juego limpio",[P("Como en «La liga de los pelirrojos», la solución tiene que salir de las pistas que el lector ya vio. Nada de resolver por casualidad.")])],
 {"titulo":"la torta","planteo":"Planificá un enigma: desapareció la torta del cumpleaños.","pasos":["Misterio: la torta no está.","Detective: Juan.","Pistas: migas en el sillón y el perro escondido; falsa pista: la ventana abierta.","Revelación: el perro se la comió."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El momento en que se explica todo es la ___ .","Un enigma tiene que tener al menos dos ___ verdaderas."]},
 {"titulo":"tu enigma","planteo":"Escribí en tu carpeta un enigma de una página, con dos pistas, una falsa pista y la revelación."},
 {"titulo":"Empezá por el final","texto":"Decidí primero la solución y después escondé las pistas que llevan a ella."},
 ["Resolver por casualidad.","Contar la solución al principio."],
 RS(("Planificar","Misterio, detective, pistas."),("Estructura","Enigma, investigación, revelación."),("Pistas","Dos verdaderas, una falsa."),("Juego limpio","La solución en las pistas.")),
 G(("Planificar","Pensar antes de escribir."),("Desarrollo","Parte central del relato."),("Juego limpio","Regla: la solución sale de las pistas.")),
 ["¿Cuántas pistas verdaderas lleva tu enigma como mínimo?","¿Cómo se llama la parte final donde se explica el caso?","¿Conviene contar la solución al principio? Respondé sí o no.","¿Qué se decide primero según el consejo: la solución o el título?"],
 [["2","dos"],["revelacion","revelación","la revelación","la revelacion"],["no"],["solucion","solución","la solución","la solucion"]],
 {"incompleto":"Revelación. Pistas.","solo":"Respuesta personal: revisá que tenga enigma, investigación y revelación.","carpeta":["Dos.","La revelación.","No.","La solución."]})
ACT={"1":[MC("¿Quién narra los casos de Sherlock Holmes?",["Holmes","Watson","Wilson","Clay"],"Watson","Es su ayudante."),MC("¿Qué hace Holmes antes de acusar?",["Adivina","Comprueba","Se va","Pregunta a la víctima"],"Comprueba","Observa, deduce y comprueba.")],
"2":[{"t":"classify","p":"¿Pista o distracción?","o":{"elementos":["Rodillas gastadas","Horas en el sótano","La enciclopedia","La liga"],"categorias":["Pista","Distracción"]},"r":{"categorias":{"Rodillas gastadas":"Pista","Horas en el sótano":"Pista","La enciclopedia":"Distracción","La liga":"Distracción"}},"e":"La liga servía para sacar a Wilson de su casa."},MC("¿Para qué servía la liga?",["Sacar a Wilson de su casa","Ayudar a los pelirrojos","Vender enciclopedias","Nada"],"Sacar a Wilson de su casa","Necesitaban la casa vacía.")],
"3":[{"t":"ordering","p":"Ordená la deducción.","o":["Un túnel al banco","Rodillas gastadas","Ayudante en el sótano","Banco detrás de la casa"],"r":{"orden":["Ayudante en el sótano","Rodillas gastadas","Banco detrás de la casa","Un túnel al banco"]},"e":"Cada pista lleva a la siguiente."},MC("¿Quién era el ayudante?",["John Clay","Watson","Un policía","El banquero"],"John Clay","Un ladrón buscado.")],
"4":[{"t":"ordering","p":"Ordená la estructura del enigma.","o":["Revelación","Aparece el enigma","Investigación"],"r":{"orden":["Aparece el enigma","Investigación","Revelación"]},"e":"Inicio, desarrollo y desenlace."},MC("Juego limpio significa que…",["La solución sale de las pistas","El detective adivina","No hay pistas","El final se cuenta primero"],"La solución sale de las pistas","El lector podría resolverlo.")],
"5":[MC("Relámpago. El misterio de un policial es el…",["Enigma","Narrador","Título"],"Enigma","Hay que resolverlo.",tiempo=20),MC("Relámpago. La liga pagaba por copiar…",["Una enciclopedia","Cartas","Mapas"],"Una enciclopedia","Cuatro horas por día.",tiempo=20),MC("Relámpago. Los ladrones cavaban un…",["Túnel","Pozo de agua","Jardín"],"Túnel","Hasta el banco.",tiempo=20),MC("Relámpago. La explicación final es la…",["Revelación","Pista","Introducción"],"Revelación","El detective explica.",tiempo=20)]}
EXAMEN=[[1,MC("¿Quién escribió las historias de Sherlock Holmes?",["Arthur Conan Doyle","Oscar Wilde","Edgar Allan Poe","Julio Verne"],"Arthur Conan Doyle","Las publicó desde 1887.")],[1,MC("¿Qué es deducir?",["Adivinar","Sacar una conclusión lógica de pistas","Preguntar al culpable","Leer rápido"],"Sacar una conclusión lógica de pistas","Es el método de Holmes.")],[1,VF("En un cuento policial siempre hay un enigma.","Verdadero","Es lo que se resuelve.")],
[2,MC("¿Qué es una falsa pista?",["Un dato que distrae","La solución","El título","El narrador"],"Un dato que distrae","Hace mirar al lado equivocado.")],[2,MC("¿Por qué el ayudante aceptaba cobrar la mitad?",["Tenía otro interés en estar en la casa","Era generoso","No sabía contar","Era pariente"],"Tenía otro interés en estar en la casa","Quería cavar el túnel.")],[2,VF("Wilson trabajó para la liga durante ocho semanas.","Verdadero","Después la liga desapareció.")],
[3,MC("¿Qué deduce Holmes de las rodillas gastadas del ayudante?",["Que excava","Que reza","Que juega al fútbol","Nada"],"Que excava","Pasaba horas en el sótano.")],[3,MC("¿Qué había detrás de la casa de Wilson?",["Un banco","Una escuela","Un río","Un teatro"],"Un banco","Con oro en la bóveda.")],[3,MC("¿Cuáles son las dos historias del policial?",["La del crimen y la de la investigación","La del amor y la del viaje","Dos finales","Dos narradores"],"La del crimen y la de la investigación","Una oculta y una contada.")],
[4,MC("¿Qué se recomienda decidir primero al escribir un enigma?",["La solución","El título","El nombre del perro","La tapa"],"La solución","Después se esconden las pistas.")],[4,VF("En un buen enigma el detective resuelve el caso por casualidad.","Falso","Tiene que resolverlo con pistas.")],[4,MC("¿Qué va en el desenlace de un enigma?",["La revelación","El enigma","Las primeras pistas","La presentación"],"La revelación","Se explica todo.")],[4,MC("Un enigma bien armado tiene…",["Pistas verdaderas y alguna falsa","Solo la solución","Ninguna pista","Solo falsas pistas"],"Pistas verdaderas y alguna falsa","Así es desafiante y justo.")]]
M={"subject_id":"e1b0726d-08aa-4d9e-9060-18489f529da2","tema":2,"practica":"Práctica general: el cuento policial","examen_titulo":"Nivel jefe: el cuento policial","niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-2.json"),"w"),ensure_ascii=False); print("ok")
