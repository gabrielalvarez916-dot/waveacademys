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

from matplotlib.patches import Ellipse, Circle, FancyBboxPatch, Rectangle
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def fig_celulas():
    fig, axs = plt.subplots(1, 2, figsize=(7.4, 3.0))
    for ax in axs: ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.set_aspect("equal")
    a = axs[0]; a.set_title("Célula animal", color=O, fontsize=10)
    a.add_patch(Ellipse((5, 3.5), 7.4, 5.4, fc="#f8d7dd", ec="#c2566b", lw=2)); a.add_patch(Circle((4.4, 3.5), 1.1, fc="#9c7bd6", ec="#5b3f8c")); [a.add_patch(Ellipse(c, 1.0, .45, fc="#f4a259")) for c in ((6.6, 4.6), (6.4, 2.3), (3.3, 2.0))]
    for t, xy, tx in (("Núcleo", (4.4, 3.5), (0.2, 6.6)), ("Membrana", (8.6, 3.5), (7.2, 6.6)), ("Mitocondria", (6.6, 4.6), (6.0, 0.3)), ("Citoplasma", (5.4, 5.6), (2.6, 0.3))): a.annotate(t, xy=xy, xytext=tx, fontsize=8, color=O, arrowprops=dict(arrowstyle="-", color=V))
    b = axs[1]; b.set_title("Célula vegetal", color=O, fontsize=10)
    b.add_patch(Rectangle((1.2, .8), 7.6, 5.4, fc="#d9f2cf", ec="#3f7a3a", lw=4)); b.add_patch(Ellipse((5.8, 3.5), 3.8, 3.0, fc="#bfe6ff", ec="#5aa9d6")); b.add_patch(Circle((2.9, 4.4), .8, fc="#9c7bd6", ec="#5b3f8c")); [b.add_patch(Ellipse(c, .9, .45, fc="#2e8b3a")) for c in ((2.4, 1.6), (7.8, 5.4), (7.9, 1.5))]
    for t, xy, tx in (("Pared celular", (1.2, 3.0), (0.0, 6.6)), ("Vacuola", (5.8, 3.5), (6.0, 6.6)), ("Cloroplasto", (7.9, 1.5), (5.6, 0.0)), ("Núcleo", (2.9, 4.4), (2.0, 0.0))): b.annotate(t, xy=xy, xytext=tx, fontsize=8, color=O, arrowprops=dict(arrowstyle="-", color=V))
    return png(fig)
def fig_micro():
    fig, ax = plt.subplots(figsize=(5.6, 3.6)); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.set_aspect("equal")
    ax.add_patch(Rectangle((2.5, .3), 4, .7, fc="#5b6770")); ax.add_patch(Rectangle((5.6, 1.0), .7, 5.2, fc="#7d8a93")); ax.add_patch(Rectangle((3.3, 6.2), 3.0, .6, fc="#7d8a93"))
    ax.add_patch(Rectangle((3.5, 6.8), .7, 1.0, fc="#3e4a52")); ax.add_patch(Rectangle((3.5, 5.2), .7, 1.0, fc="#3e4a52")); ax.add_patch(Rectangle((2.4, 4.3), 3.4, .3, fc="#3e4a52")); ax.add_patch(Circle((3.85, 1.9), .45, fc="#f4d35e")); ax.add_patch(Circle((6.0, 3.0), .35, fc="#3e4a52"))
    for t, xy, tx in (("Ocular", (3.85, 7.6), (0.2, 7.5)), ("Objetivo", (3.85, 5.3), (0.2, 5.6)), ("Platina", (2.5, 4.45), (0.2, 4.0)), ("Luz", (3.85, 1.9), (0.2, 1.8)), ("Tornillos", (6.3, 3.0), (7.2, 3.0)), ("Brazo", (6.1, 5.0), (7.2, 5.4)), ("Base", (6.4, .6), (7.2, .6))): ax.annotate(t, xy=xy, xytext=tx, fontsize=8.5, color=O, arrowprops=dict(arrowstyle="-", color=V))
    return png(fig)
N1=NV("Vas a reconocer las propiedades que comparten todos los seres vivos y a distinguirlos de lo que no está vivo.",["Propiedades de los seres vivos","El ciclo de vida","Homeostasis","El experimento de Pasteur"],[
 S(1,"Propiedades",[T("Todo ser vivo…",["Propiedad","Qué significa","Ejemplo"],[["Organización celular","Está formado por una o más células","una bacteria, un árbol"],["Nutrición","Incorpora materia y energía","la planta hace fotosíntesis"],["Relación","Responde a estímulos","la planta gira hacia la luz"],["Reproducción","Origina nuevos seres vivos","una semilla da otra planta"],["Homeostasis","Mantiene estable su medio interno","transpirar cuando hace calor"]]),P("Un ser vivo cumple <b>todas</b> las propiedades a la vez. El fuego crece y consume oxígeno, pero no está formado por células: no está vivo.")]),
 S(1,"El ciclo de vida",[P("Todo ser vivo <b>nace</b> de otro, <b>crece y se desarrolla</b> (cambia de forma, como el renacuajo que se vuelve rana), puede <b>reproducirse</b> y finalmente <b>muere</b>. Sus materiales vuelven al ambiente.")]),
 S(2,"¿La vida surge sola?",[E("El experimento de Pasteur (1862)","Dos frascos con caldo hervido: uno de cuello recto y otro de cuello curvo.",["Variable: la forma del cuello.","Cuello recto: el polvo del aire entra y aparecen microbios.","Cuello curvo: el polvo queda en la curva y el caldo sigue limpio.","Conclusión: todo ser vivo proviene de otro ser vivo."])])],
 {"titulo":"¿vivo o no?","planteo":"¿Está viva una semilla de poroto seca?","pasos":["Está formada por células.","Si se la riega, germina: crece y se desarrolla.","Puede originar una planta que dé nuevas semillas.","Está viva, en estado de reposo."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Mantener estable el medio interno se llama ___ .","Pasteur demostró que todo ser vivo proviene de otro ser ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un objeto que crezca o se mueva (una nube, un cristal, un auto) y explicá qué propiedades de los seres vivos le faltan."},
 {"titulo":"Todas, no algunas","texto":"Para decidir si algo está vivo, revisá la lista completa: con una sola que falte, no es un ser vivo."},
 ["Pensar que algo vive solo porque se mueve o crece.","Creer que una semilla seca no está viva."],
 RS(("Células","Base de todo ser vivo."),("Funciones","Nutrición, relación, reproducción."),("Ciclo","Nace, crece, se reproduce, muere."),("Origen","Proviene de otro ser vivo.")),
 G(("Estímulo","Cambio del ambiente que provoca una respuesta."),("Homeostasis","Equilibrio del medio interno."),("Nutrición","Incorporar materia y energía."),("Generación espontánea","Idea antigua de que la vida surge sola.")),
 ["¿Qué propiedad muestra una planta que gira hacia la luz?","¿El fuego está formado por células? Respondé sí o no.","¿Quién demostró con frascos de cuello curvo que la vida no surge sola?","¿Cómo se llama mantener estable el medio interno?"],
 [["relacion","relación","la relación"],["no"],["pasteur","louis pasteur"],["homeostasis","la homeostasis"]],
 {"incompleto":"Homeostasis. Vivo.","solo":"Respuesta personal: le faltan células, nutrición o reproducción.","carpeta":["Relación.","No.","Louis Pasteur.","Homeostasis."]})
N2=NV("Vas a ordenar los niveles de organización de la materia viva, de la célula a la biosfera.",["Del organismo a la célula","Los niveles en orden","Más allá del organismo"],[
 S(1,"Los niveles en orden",[T("De menor a mayor",["Nivel","Qué es","Ejemplo"],[["Célula","Unidad de la vida","neurona"],["Tejido","Células parecidas con la misma función","tejido muscular"],["Órgano","Varios tejidos que trabajan juntos","corazón"],["Sistema","Órganos que cooperan","sistema circulatorio"],["Organismo","El ser vivo completo","una persona"]])]),
 S(2,"Más allá del organismo",[T("Niveles ecológicos",["Nivel","Qué es","Ejemplo"],[["Población","Individuos de la misma especie en un lugar","carpinchos de una laguna"],["Comunidad","Todas las poblaciones juntas","carpinchos, garzas, juncos y peces"],["Ecosistema","Comunidad + ambiente","la laguna con su agua y su suelo"],["Biosfera","Todos los ecosistemas","el planeta con vida"]])])],
 {"titulo":"ordenar","planteo":"Ordená de menor a mayor: corazón, célula muscular, persona, sistema circulatorio, tejido muscular.","pasos":["Célula muscular.","Tejido muscular.","Corazón (órgano).","Sistema circulatorio.","Persona (organismo)."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un grupo de células parecidas forma un ___ .","Todos los peces dorados de un río forman una ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un ser vivo de tu zona y escribí un ejemplo de población, de comunidad y de ecosistema donde aparezca."},
 {"titulo":"Pensá en una casa","texto":"Ladrillos (células), paredes (tejidos), habitaciones (órganos), servicios como el agua (sistemas) y la casa completa (organismo)."},
 ["Confundir tejido con órgano.","Confundir población con comunidad."],
 RS(("Unidad","La célula."),("Cuerpo","Tejido, órgano, sistema."),("Afuera","Población, comunidad."),("Todo","Ecosistema, biosfera.")),
 G(("Tejido","Grupo de células parecidas."),("Órgano","Estructura formada por tejidos."),("Población","Individuos de una especie en un lugar."),("Comunidad","Conjunto de poblaciones.")),
 ["¿Qué nivel es el corazón?","¿Qué nivel forman todos los carpinchos de una laguna?","¿Qué nivel está formado por varios órganos que cooperan?","¿Cuál es el nivel más pequeño con vida?"],
 [["organo","órgano","un organo","un órgano"],["poblacion","población","una población"],["sistema","un sistema"],["celula","célula","la célula"]],
 {"incompleto":"Tejido. Población.","solo":"Respuesta personal.","carpeta":["Órgano.","Población.","Sistema.","La célula."]})
N3=NV("Vas a conocer la teoría celular, las partes de la célula y los tipos de células.",["Teoría celular","Célula animal y vegetal","Procariotas y eucariotas"],[
 S(1,"Teoría celular",[P("1) Todo ser vivo está formado por células. 2) La célula es la unidad de vida y de función. 3) Toda célula proviene de otra célula.")]),
 S(1,"Partes de la célula",[IMG("Célula animal y vegetal","Las partes comunes y las exclusivas de la vegetal.","Dibujo de una célula animal ovalada y una vegetal rectangular con sus partes señaladas.",fig_celulas()),
  T("Partes",["Parte","Función","¿Dónde?"],[["Membrana","Controla qué entra y sale","Ambas"],["Citoplasma","Medio interno","Ambas"],["Núcleo","Guarda el ADN","Ambas"],["Mitocondria","Obtiene energía","Ambas"],["Pared celular","Rígida, da forma","Vegetal"],["Cloroplasto","Fotosíntesis","Vegetal"],["Vacuola grande","Guarda agua","Vegetal"]])]),
 S(2,"Procariotas y eucariotas",[P("Las células <b>procariotas</b> no tienen núcleo: su ADN está suelto en el citoplasma (bacterias). Las <b>eucariotas</b> tienen núcleo (animales, plantas, hongos). Los seres <b>unicelulares</b> tienen una sola célula; los <b>pluricelulares</b>, muchas.")])],
 {"titulo":"identificar","planteo":"Una célula tiene pared celular, cloroplastos y núcleo. ¿De qué tipo es?","pasos":["Tiene núcleo: es eucariota.","Tiene cloroplastos: es vegetal.","Puede ser de una hoja."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La fotosíntesis ocurre en los ___ .","Las bacterias son células ___ : no tienen núcleo."]},
 {"titulo":"tu turno","planteo":"Dibujá en tu carpeta una célula vegetal y señalá cinco partes."},
 {"titulo":"Lo que solo tiene la planta","texto":"Pared, cloroplastos y vacuola grande: si aparece alguno, es una célula vegetal."},
 ["Creer que las plantas no tienen mitocondrias.","Creer que todas las células tienen núcleo."],
 RS(("Teoría celular","Tres ideas."),("Comunes","Membrana, citoplasma, núcleo, mitocondria."),("Vegetal","Pared, cloroplastos, vacuola."),("Tipos","Procariota y eucariota.")),
 G(("ADN","Material genético con las instrucciones de la célula."),("Fotosíntesis","Fabricación de alimento con la luz."),("Procariota","Célula sin núcleo."),("Eucariota","Célula con núcleo.")),
 ["¿En qué parte de la célula se guarda el ADN?","¿Qué parte, exclusiva de la célula vegetal, hace la fotosíntesis?","¿Las bacterias son procariotas o eucariotas?","¿Las células vegetales tienen mitocondrias? Respondé sí o no."],
 [["nucleo","núcleo","el núcleo","en el núcleo"],["cloroplasto","cloroplastos","los cloroplastos"],["procariotas","procariota"],["si","sí"]],
 {"incompleto":"Cloroplastos. Procariotas.","solo":"Respuesta personal con pared, membrana, citoplasma, núcleo, cloroplastos y vacuola.","carpeta":["En el núcleo.","Cloroplastos.","Procariotas.","Sí."]})
N4=NV("Vas a reconocer las partes del microscopio, calcular el aumento y preparar una muestra.",["Partes del microscopio","Aumento total","Preparar y observar"],[
 S(1,"Partes",[IMG("El microscopio óptico","Sus partes principales.","Dibujo de un microscopio con ocular, objetivo, platina, luz, tornillos, brazo y base.",fig_micro())]),
 S(1,"Aumento total",[D("Aumento total","Aumento del ocular × aumento del objetivo."),E("Calcular","Ocular 10× y objetivo 40×.",["Se multiplica: 10 × 40.","Aumento total: 400×.","Se ve 400 veces más grande."])]),
 S(2,"Preparar y observar",[T("Pasos",["Paso","Cómo"],[["1","Muestra muy fina sobre el portaobjetos"],["2","Una gota de agua o colorante"],["3","Cubreobjetos apoyado de costado, sin burbujas"],["4","Enfocar con el menor aumento"],["5","Recién después, pasar a un aumento mayor"]])])],
 {"titulo":"calcular","planteo":"Ocular 10× y objetivo 100×. ¿Aumento total?","pasos":["Se multiplica: 10 × 100.","Aumento total: 1000×."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La lente por donde se mira es el ___ .","La muestra se apoya en la ___ ."]},
 {"titulo":"tu turno","planteo":"Explicá por qué la muestra tiene que ser muy fina."},
 {"titulo":"Del menor al mayor","texto":"Con el menor aumento ves más campo y encontrás la muestra; recién después acercás."},
 ["Sumar los aumentos en lugar de multiplicarlos.","Empezar con el mayor aumento."],
 RS(("Partes","Ocular, objetivos, platina, tornillos, luz."),("Aumento","Ocular × objetivo."),("Muestra","Fina, con cubreobjetos."),("Enfoque","Del menor al mayor.")),
 G(("Ocular","Lente donde se apoya el ojo."),("Objetivo","Lente cercana a la muestra."),("Platina","Plataforma de la muestra."),("Portaobjetos","Vidrio donde va la muestra.")),
 ["Ocular 10× y objetivo 40×: ¿aumento total? Respondé solo el número.","¿Con qué aumento se empieza a enfocar: el menor o el mayor?","¿Cómo se llama la lente por donde se mira?","¿Dónde se apoya el portaobjetos?"],
 [["400","400x","400×"],["menor","el menor"],["ocular","el ocular"],["platina","en la platina","la platina"]],
 {"incompleto":"Ocular. Platina.","solo":"Porque la luz tiene que atravesarla para que se vea.","carpeta":["400.","El menor.","El ocular.","En la platina."]})
ACT={"1":[{"t":"classify","p":"¿Ser vivo o no vivo?","o":{"elementos":["Semilla de poroto","Moho de la fruta","Cristal de sal","Una nube"],"categorias":["Ser vivo","No vivo"]},"r":{"categorias":{"Semilla de poroto":"Ser vivo","Moho de la fruta":"Ser vivo","Cristal de sal":"No vivo","Una nube":"No vivo"}},"e":"Lo vivo está formado por células."},MC("¿Qué demostró el experimento de Pasteur?",["Que todo ser vivo proviene de otro","Que la vida surge del caldo","Que el aire es tóxico","Que el calor crea microbios"],"Que todo ser vivo proviene de otro","El cuello curvo frenó el polvo con microbios.")],
 "2":[{"t":"ordering","p":"Ordená de menor a mayor.","o":["Órgano","Célula","Organismo","Tejido","Sistema"],"r":{"orden":["Célula","Tejido","Órgano","Sistema","Organismo"]},"e":"De la unidad de la vida al ser completo."},MC("Todos los carpinchos de una laguna forman una…",["Población","Comunidad","Biosfera","Especie extinta"],"Población","Una sola especie en un lugar.")],
 "3":[{"t":"matching","p":"Uní cada parte con su función.","o":{"izquierda":["Membrana","Núcleo","Cloroplasto","Mitocondria"],"derecha":["Controla qué entra y sale","Guarda el ADN","Fotosíntesis","Obtiene energía"]},"r":{"pares":{"Membrana":"Controla qué entra y sale","Núcleo":"Guarda el ADN","Cloroplasto":"Fotosíntesis","Mitocondria":"Obtiene energía"}},"e":"Cada parte tiene su función."},MC("Una célula sin núcleo es…",["Procariota","Eucariota","Vegetal","Animal"],"Procariota","Como las bacterias.")],
 "4":[N("Ocular 10× y objetivo {o}×. ¿Cuál es el aumento total?",{"formula":"10*o"},"Se multiplica ocular por objetivo.",{"vars":{"o":{"valores":[4,10,40,100]}}}),MC("¿Con qué aumento se empieza a enfocar?",["El menor","El mayor","Cualquiera","Sin lentes"],"El menor","Así se encuentra la muestra.")],
 "5":[MC("Relámpago. Todo ser vivo está formado por…",["Células","Átomos de oro","Minerales"],"Células","Teoría celular.",tiempo=20),MC("Relámpago. El corazón es un…",["Órgano","Tejido","Sistema"],"Órgano","Formado por tejidos.",tiempo=20),MC("Relámpago. La fotosíntesis ocurre en…",["Cloroplastos","Mitocondrias","Núcleo"],"Cloroplastos","Solo en vegetales.",tiempo=20),MC("Relámpago. Ocular 10× y objetivo 10×:",["100×","20×","1000×"],"100×","Se multiplica.",tiempo=20)]}
EXAMEN=[[1,MC("¿Por qué el fuego no es un ser vivo?",["No está formado por células","No crece","No consume oxígeno","No se mueve"],"No está formado por células","Crece y consume oxígeno, pero no tiene células.")],[1,MC("Transpirar cuando hace calor es un ejemplo de…",["Homeostasis","Reproducción","Nutrición","Fotosíntesis"],"Homeostasis","Mantiene estable la temperatura.")],[1,VF("Una semilla seca no está viva.","Falso","Está viva, en reposo.")],
 [2,MC("Un grupo de células parecidas forma un…",["Tejido","Órgano","Sistema","Organismo"],"Tejido","Varios tejidos forman un órgano.")],[2,MC("Carpinchos, garzas, juncos y peces de una laguna forman una…",["Comunidad","Población","Célula","Biosfera"],"Comunidad","Varias especies juntas.")],[2,MC("¿Cuál está ordenado de menor a mayor?",["Célula, tejido, órgano, sistema","Órgano, célula, tejido, sistema","Tejido, célula, sistema, órgano","Sistema, órgano, tejido, célula"],"Célula, tejido, órgano, sistema","De la unidad al conjunto.")],
 [3,MC("¿Qué parte tienen las células vegetales y no las animales?",["Cloroplastos","Núcleo","Membrana","Mitocondrias"],"Cloroplastos","También pared y vacuola grande.")],[3,MC("¿Qué dice la teoría celular sobre el origen de las células?",["Toda célula proviene de otra célula","Surgen del agua","Las crea el sol","Aparecen solas"],"Toda célula proviene de otra célula","Es su tercera idea.")],[3,VF("Las bacterias son células eucariotas.","Falso","Son procariotas: no tienen núcleo.")],
 [4,N("Ocular 10× y objetivo 40×: ¿aumento total?",{"acepta":[400]},"10 × 40.")],[4,MC("¿Por qué la muestra debe ser muy fina?",["Para que la luz la atraviese","Para que pese menos","Para que no se ensucie","Para que sea más barata"],"Para que la luz la atraviese","El microscopio óptico usa luz.")],[4,MC("¿Qué parte se usa para enfocar?",["Los tornillos","La platina","La base","El ocular"],"Los tornillos","Acercan o alejan la muestra.")],[4,VF("Conviene empezar a enfocar con el mayor aumento.","Falso","Se empieza con el menor.")]]
M={"subject_id":"9fa85d7b-ee7a-4853-8486-a69f9b539c12","tema":3,"practica":"Práctica general: qué es un ser vivo","examen_titulo":"Nivel jefe: qué es un ser vivo","niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-3.json"),"w"),ensure_ascii=False); print("ok")
