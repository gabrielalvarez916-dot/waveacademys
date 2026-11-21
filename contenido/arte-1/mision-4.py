# -*- coding: utf-8 -*-
"""Arte y Comunicación I · Misión 4 (Textura y materia) · COMÚN. Genera mision-4.json y 4 clases."""
import os, sys, io, base64, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}

FB=lambda p,h,e,**k:{"t":"fill_blank","p":p,"o":[],"r":{"huecos":h},"e":e,**k}
MS=lambda p,o,c,e,**k:{"t":"multi_select","p":p,"o":o,"r":{"correctas":c},"e":e,**k}
TT=lambda p,seg,tocar,e,**k:{"t":"tap_text","p":p,"o":{"segmentos":seg,"modo":"palabras"},"r":{"tocar":tocar},"e":e,**k}
KW=lambda p,ayuda,ref,e,**k:{"t":"keywords","p":p,"o":{"ayuda":ayuda},"r":ref,"e":e,**k}
SID = "825b1d79-1ef4-47ee-999d-6b5bbc1080da"
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
V, O, C = "#6a3fa0", "#2b2340", "#efe6fa"
def png(fig):
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig)
    im = Image.open(io.BytesIO(b.getvalue())).convert("RGB").quantize(colors=24); o = io.BytesIO(); im.save(o, format="PNG", optimize=True); return base64.b64encode(o.getvalue()).decode()
def IMG(t, pie, desc, b64): return {"tipo":"imagen","imagen_tipo":"diagrama","titulo":t,"texto":pie,"imagen_descripcion":desc,"imagen_fuente":"Dibujo propio (matplotlib).","png_base64":b64}
def img_texturas():
    fig, axs = plt.subplots(2, 3, figsize=(6.2, 4.2))
    rng = np.random.RandomState(4)
    nombres = ["Rugosa", "Lisa", "Punteada", "Rayada", "Ondulada", "Cuadriculada"]
    for k, ax in enumerate(axs.ravel()):
        ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_xticks([]); ax.set_yticks([]); ax.set_facecolor("#efe9f5")
        for sp in ax.spines.values(): sp.set_color(V); sp.set_linewidth(2)
        if k == 0:
            for _ in range(160):
                x, y = rng.rand(2) * 10; ax.plot([x, x + rng.randn() * .6], [y, y + rng.randn() * .6], color=V, lw=1, alpha=.7)
        elif k == 2: ax.scatter(rng.rand(70) * 10, rng.rand(70) * 10, s=18, color=V)
        elif k == 3:
            for y in np.linspace(0.5, 9.5, 12): ax.plot([0, 10], [y, y], color=V, lw=2)
        elif k == 4:
            xs = np.linspace(0, 10, 200)
            for y in np.linspace(1, 9, 6): ax.plot(xs, y + 0.5 * np.sin(xs * 2), color=V, lw=2)
        elif k == 5:
            for t in np.linspace(0.5, 9.5, 8): ax.plot([t, t], [0, 10], color=V, lw=1.5); ax.plot([0, 10], [t, t], color=V, lw=1.5)
        ax.set_title(nombres[k], fontsize=11, color=O, fontweight="bold")
    fig.tight_layout()
    return png(fig)
B1=NV("Vas a reconocer y describir texturas visuales y táctiles.",["Qué es la textura","Visual y táctil","Texturas en objetos","Textura como mensaje"],[
 S(1,"Qué es la textura",[D("Textura","Aspecto o sensación de la superficie de un objeto: lisa, rugosa, suave, áspera."),P("La textura se percibe con los ojos y con las manos. Un mismo objeto puede verse suave y, al tocarlo, resultar áspero.")]),
 S(1,"Visual y táctil",[T("Dos tipos de textura",["Tipo","Cómo se percibe"],[["Táctil","Se siente al tocar: la tela, la corteza, la arena"],["Visual","Se ve, aunque no se toque: la que se dibuja o se pinta para imitar una superficie"]]),IMG("Texturas visuales","Seis texturas dibujadas con líneas y puntos.","Seis cuadros con texturas dibujadas: rugosa, lisa, punteada, rayada, ondulada y cuadriculada, cada una hecha con líneas o puntos de distinta forma.",img_texturas())]),
 S(2,"Texturas en objetos",[P("Los materiales tienen texturas muy distintas: la madera tiene vetas, la piedra es rugosa, el vidrio es liso y la lana es suave. Reconocerlas ayuda a representarlas."),IM("Tocá y mirá","Observar de cerca un material muestra detalles que de lejos no se ven.")]),
 S(2,"Textura como mensaje",[P("Una textura puede transmitir ideas: lo áspero sugiere dureza o cansancio, lo suave sugiere calidez y cuidado. Los artistas las eligen para reforzar lo que quieren decir.")])],
 {"titulo":"describir","planteo":"Tenés una hoja de papel arrugada y una de vidrio. ¿Cómo describís sus texturas?","pasos":["Papel arrugado: rugoso, con relieves.","Vidrio: liso y frío.","Cada una se puede dibujar con líneas distintas.","Una transmite aspereza y la otra transparencia."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La sensación de la superficie de un objeto es la ___ .","La textura que se ve pero no se toca es la ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí cuatro objetos de tu casa y dibujá la textura de cada uno con líneas y puntos. Escribí si es lisa, rugosa o suave."},
 {"titulo":"Mirá de cerca","texto":"Acercate al objeto: las texturas se descubren cuando mirás con atención."},
 ["Creer que la textura solo se siente con las manos.","Dibujar todas las texturas con el mismo tipo de línea."],
 RS(("Textura","Cómo es la superficie."),("Táctil","Se siente al tocar."),("Visual","Se ve."),("Mensaje","Sugiere ideas.")),
 G(("Textura","Aspecto de una superficie."),("Táctil","Que se percibe al tocar."),("Visual","Que se percibe al mirar."),("Relieve","Parte que sobresale.")),
 ["¿Cómo se llama el aspecto o la sensación de la superficie de un objeto?","¿Cómo se llama la textura que se percibe al tocar?","¿Una textura visual se puede ver aunque no se toque? Respondé sí o no.","¿Conviene dibujar todas las texturas con el mismo tipo de línea? Respondé sí o no."],
 [["textura","la textura"],["tactil","táctil","textura tactil","textura táctil"],["si","sí"],["no"]],
 {"incompleto":"Textura. Táctil.","solo":"Elegí una media, una hoja, una piedra y una taza. La media es suave y la dibujé con rulos. La piedra es rugosa y usé puntos.","carpeta":["Textura.","Táctil.","Sí.","No."]})
B2=NV("Vas a crear texturas con frotage, collage y ensamblaje.",["Frotage","Collage","Ensamblaje","Combinar técnicas"],[
 S(1,"Frotage",[D("Frotage","Técnica que consiste en frotar un lápiz o un crayón sobre un papel apoyado en una superficie con relieve, para copiar su textura."),P("Con el frotage se pueden copiar hojas, monedas, rejillas o troncos.")]),
 S(1,"Collage",[D("Collage","Obra hecha pegando sobre una superficie distintos materiales, como papeles, telas o fotos."),T("Materiales para un collage",["Material","Qué aporta"],[["Papel de revista","Colores y formas"],["Tela","Textura suave"],["Cartón","Relieve"]])]),
 S(2,"Ensamblaje",[D("Ensamblaje","Obra en tres dimensiones armada uniendo objetos o partes de objetos."),P("El ensamblaje puede usar objetos cotidianos y reciclados para crear algo nuevo.")]),
 S(2,"Combinar técnicas",[T("Cuándo usar cada técnica",["Técnica","Resultado"],[["Frotage","Copia una textura real"],["Collage","Construye una imagen con pedazos"],["Ensamblaje","Arma un objeto en volumen"]]),IM("Probá antes","Probar la textura en un papel aparte evita errores en la obra.")])],
 {"titulo":"frotage","planteo":"Querés copiar la textura de una hoja de árbol. ¿Cómo lo hacés?","pasos":["Poner la hoja debajo de un papel fino.","Inclinar un crayón y frotar suavemente.","Mantener quieto el papel.","Ver cómo aparecen las nervaduras."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La técnica de frotar un lápiz sobre un papel apoyado en un relieve es el ___ .","La obra que se arma pegando materiales sobre una superficie es el ___ ."]},
 {"titulo":"tu turno","planteo":"Hacé un frotage de tres superficies distintas y armá con los resultados un collage chico. Escribí qué textura te sorprendió."},
 {"titulo":"Una técnica por vez","texto":"Probá una técnica por vez para ver qué aporta cada una."},
 ["Apretar el papel y moverlo mientras se hace el frotage.","Usar solo pegamento en exceso."],
 RS(("Frotage","Copia texturas."),("Collage","Pega materiales."),("Ensamblaje","Obra en volumen."),("Combinar","Elegir según el resultado.")),
 G(("Frotage","Copiar un relieve frotando."),("Collage","Obra con materiales pegados."),("Ensamblaje","Obra en tres dimensiones."),("Soporte","Superficie sobre la que se trabaja.")),
 ["¿Cómo se llama la técnica de frotar un lápiz sobre un papel apoyado en un relieve?","¿Cómo se llama la obra que se arma pegando materiales sobre una superficie?","¿El ensamblaje es una obra en tres dimensiones? Respondé sí o no.","¿Conviene mover el papel mientras se hace el frotage? Respondé sí o no."],
 [["frotage","el frotage"],["collage","el collage"],["si","sí"],["no"]],
 {"incompleto":"Frotage. Collage.","solo":"Hice frotage de una moneda, una hoja y una rejilla. Después pegué los recortes y armé un paisaje. Me sorprendió la hoja.","carpeta":["Frotage.","Collage.","Sí.","No."]})
B3=NV("Vas a elegir materiales y soportes según lo que querés expresar.",["Soporte y material","Papel y cartón","Tela y madera","Materiales reciclados"],[
 S(1,"Soporte y material",[D("Soporte","Superficie sobre la que se trabaja una obra: papel, tela, madera, pared."),P("El material es lo que se usa para hacer la obra, como lápiz, acrílico o tinta. El soporte y el material se eligen en conjunto.")]),
 S(1,"Papel y cartón",[T("Papeles y cartones",["Soporte","Para qué sirve"],[["Papel liso","Dibujo y lápiz"],["Papel con grano","Acuarela y carbonilla"],["Cartón","Collage y relieves"]])]),
 S(2,"Tela y madera",[P("La tela, como el lienzo, se usa para pintura al óleo y acrílico. La madera da una superficie firme y con vetas propias, que pueden formar parte de la obra."),IM("Preparar el soporte","Algunos soportes necesitan una capa de base antes de pintar.")]),
 S(2,"Materiales reciclados",[P("Cartones, tapitas, telas viejas y envases se pueden reutilizar en una obra. Reciclar también transmite un mensaje sobre el cuidado del ambiente."),T("Ideas de reciclado",["Material","Posible uso"],[["Tapitas","Mosaico"],["Cartón","Relieve"],["Telas","Collage"]])])],
 {"titulo":"elegir","planteo":"Querés hacer una obra con mucho relieve. ¿Qué elegís?","pasos":["Soporte firme: un cartón grueso.","Materiales con volumen: tapitas y telas.","Pegamento fuerte.","Una capa de pintura para unir los colores."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La superficie sobre la que se trabaja una obra es el ___ .","Los materiales usados de nuevo son materiales ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un soporte y dos materiales distintos para una obra sobre tu barrio. Anotá por qué los elegiste."},
 {"titulo":"Soporte y material","texto":"Pensá primero en el soporte y después en los materiales: se eligen juntos."},
 ["Pintar con acuarela sobre un papel muy fino que se rompe.","Tirar materiales que se podrían reutilizar."],
 RS(("Soporte","Superficie de la obra."),("Material","Con lo que se hace."),("Papel y cartón","Según la técnica."),("Reciclados","Dan una segunda vida.")),
 G(("Soporte","Superficie de trabajo."),("Lienzo","Tela para pintar."),("Veta","Dibujo natural de la madera."),("Reciclar","Usar de nuevo.")),
 ["¿Cómo se llama la superficie sobre la que se trabaja una obra?","¿Cómo se llama a los materiales usados de nuevo para hacer una obra?","¿La madera tiene vetas propias? Respondé sí o no.","¿Conviene tirar los materiales que se podrían reutilizar? Respondé sí o no."],
 [["soporte","el soporte"],["reciclados","materiales reciclados","reciclables"],["si","sí"],["no"]],
 {"incompleto":"Soporte. Reciclados.","solo":"Elegí un cartón grueso como soporte, tapitas y telas como materiales. Quise mostrar mi barrio con colores y relieves.","carpeta":["Soporte.","Reciclados.","Sí.","No."]})
B4=NV("Vas a combinar técnicas para armar una obra de técnica mixta.",["Qué es la técnica mixta","Capas y orden","Armonía de texturas","Obra final"],[
 S(1,"Qué es la técnica mixta",[D("Técnica mixta","Obra que combina dos o más técnicas o materiales, como dibujo, pintura y collage."),P("La técnica mixta permite sumar la textura, el color y el volumen en una misma obra.")]),
 S(1,"Capas y orden",[T("Orden de trabajo",["Paso","Qué se hace"],[["1. Fondo","Pintar o pegar la base"],["2. Texturas","Sumar frotage y collage"],["3. Dibujo","Marcar formas con lápiz o tinta"],["4. Detalles","Agregar brillos y toques finales"]])]),
 S(2,"Armonía de texturas",[P("Si hay demasiadas texturas distintas, la obra se ve cargada. Conviene que una domine y las otras acompañen, igual que con los colores."),IM("Descanso visual","Dejar una zona lisa ayuda a que se destaquen las texturas.")]),
 S(2,"Obra final",[T("Qué revisar al terminar",["Pregunta","Qué mirar"],[["¿Se entiende la idea?","Tema y mensaje"],["¿Hay equilibrio?","Texturas y colores"],["¿Se secó todo?","Evitar que se despegue"]])])],
 {"titulo":"técnica mixta","planteo":"Vas a armar una obra sobre el mar con técnica mixta. ¿Cómo la planeás?","pasos":["Fondo: pintura azul con esponja.","Texturas: arena pegada y frotage de redes.","Dibujo: peces con lápiz negro.","Detalles: brillos blancos de pintura."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La obra que combina dos o más técnicas o materiales es de técnica ___ .","Conviene que una textura ___ y las otras acompañen."]},
 {"titulo":"tu turno","planteo":"Armá una obra chica de técnica mixta con al menos tres materiales o técnicas. Anotá el orden que seguiste."},
 {"titulo":"Menos es más","texto":"Una zona lisa le da descanso a la mirada y hace que se luzcan las texturas."},
 ["Pegar todos los materiales a la vez, sin orden.","Usar demasiadas texturas distintas en la misma obra."],
 RS(("Mixta","Combina técnicas."),("Orden","Fondo, texturas, dibujo, detalles."),("Armonía","Una textura domina."),("Revisar","Idea, equilibrio y secado.")),
 G(("Técnica mixta","Combina técnicas o materiales."),("Capa","Cada nivel de material."),("Equilibrio","Reparto parejo."),("Acabado","Toques finales.")),
 ["¿Cómo se llama la obra que combina dos o más técnicas o materiales?","¿Cómo se llama el reparto parejo de texturas y colores en una obra?","¿Conviene usar muchas texturas que compitan entre sí? Respondé sí o no.","¿Conviene dejar una zona lisa para descansar la mirada? Respondé sí o no."],
 [["tecnica mixta","técnica mixta","mixta"],["equilibrio","el equilibrio"],["no"],["si","sí"]],
 {"incompleto":"Mixta. Equilibrio.","solo":"Pinté el fondo, pegué arena, hice frotage de una red, dibujé peces y agregué brillos. Primero hice las capas y después los detalles.","carpeta":["Técnica mixta.","Equilibrio.","No.","Sí."]})
ACT4={"1":[{"t":"classify","p":"¿Táctil o visual?","o":{"elementos":["Corteza de un árbol","Textura dibujada","Lana","Papel de lija pintado"],"categorias":["Táctil","Visual"]},"r":{"categorias":{"Corteza de un árbol":"Táctil","Textura dibujada":"Visual","Lana":"Táctil","Papel de lija pintado":"Visual"}},"e":"Táctil se toca; visual se ve."},MC("La sensación de la superficie de un objeto es la…",["Textura","Perspectiva","Escala","Armonía"],"Textura","Se percibe al tocar o mirar.")],
 "2":[{"t":"matching","p":"Uní cada técnica con su descripción.","o":{"izquierda":["Frotage","Collage","Ensamblaje"],"derecha":["Copia un relieve frotando","Pega materiales sobre una superficie","Obra en tres dimensiones"]},"r":{"pares":{"Frotage":"Copia un relieve frotando","Collage":"Pega materiales sobre una superficie","Ensamblaje":"Obra en tres dimensiones"}},"e":"Cada técnica, su descripción."},VF("En el frotage hay que mover el papel mientras se frota.","Falso","El papel tiene que estar quieto.")],
 "3":[MS("¿Qué pueden ser soportes?",["Papel","Tela","Madera","Un crayón"],["Papel","Tela","Madera"],"El crayón es un material, no un soporte."),FB("La superficie sobre la que se trabaja una obra es el ___ .",[["soporte"]],"Se elige junto con el material.")],
 "4":[{"t":"ordering","p":"Ordená los pasos de una técnica mixta.","o":["Detalles","Fondo","Dibujo","Texturas"],"r":{"orden":["Fondo","Texturas","Dibujo","Detalles"]},"e":"De la base al detalle."},TT("Tocá la palabra clave: «Una técnica mixta combina técnicas».",["Una","técnica","mixta","combina","técnicas."],[2],"Mixta indica combinación.")],
 "5":[{"t":"classify","p":"Técnica o soporte.","o":{"elementos":["Frotage","Lienzo","Collage","Madera"],"categorias":["Técnica","Soporte"]},"r":{"categorias":{"Frotage":"Técnica","Lienzo":"Soporte","Collage":"Técnica","Madera":"Soporte"}},"e":"Una es cómo se hace; el otro, dónde.","tiempo":35},
  VF("El ensamblaje es una obra en tres dimensiones.","Verdadero","Une objetos en volumen.",tiempo=15),
  MC("¿Qué textura se percibe al tocar?",["Táctil","Visual","Cromática"],"Táctil","Se siente con las manos.",tiempo=15),
  FB("Una obra que combina técnicas es de técnica ___ .",[["mixta"]],"Combina dos o más.",tiempo=25)]}
EX4=[[1,MC("El aspecto o la sensación de la superficie de un objeto es la…",["Textura","Proporción","Escala","Armonía"],"Textura","Se percibe al mirar o tocar.")],
 [1,VF("Una textura visual se ve aunque no se toque.","Verdadero","Se dibuja o se pinta.")],
 [1,MC("La textura que se percibe al tocar es la…",["Táctil","Visual","Cromática","Sonora"],"Táctil","Se siente con las manos.")],
 [2,MC("La técnica de frotar un crayón sobre un papel apoyado en un relieve es el…",["Frotage","Collage","Ensamblaje","Boceto"],"Frotage","Copia la textura.")],
 [2,VF("El collage se hace pegando materiales sobre una superficie.","Verdadero","Se combinan papeles, telas o fotos.")],
 [2,MC("Una obra en tres dimensiones armada uniendo objetos es un…",["Ensamblaje","Frotage","Boceto","Grabado"],"Ensamblaje","Tiene volumen.")],
 [3,MC("La superficie sobre la que se trabaja una obra es el…",["Soporte","Boceto","Matiz","Encaje"],"Soporte","Se elige junto con el material.")],
 [3,VF("La madera tiene vetas propias que pueden formar parte de la obra.","Verdadero","Es una textura natural.")],
 [3,FB("Los materiales que se usan de nuevo para hacer una obra son los materiales ___ .",[["reciclados"]],"Transmiten cuidado del ambiente.")],
 [4,MC("Una obra que combina dos o más técnicas o materiales es de técnica…",["Mixta","Simple","Única","Digital"],"Mixta","Suma color, textura y volumen.")],
 [4,VF("Conviene dejar una zona lisa para descansar la mirada.","Verdadero","Ayuda a que se luzcan las texturas.")],
 [4,MC("¿Cuál es el primer paso de una técnica mixta?",["El fondo","Los detalles","El dibujo","El brillo"],"El fondo","Se empieza por la base.")],
 [4,MS("¿Qué conviene revisar al terminar la obra?",["Que se entienda la idea","Que haya equilibrio","Que se haya secado","Que tenga la mayor cantidad de texturas"],["Que se entienda la idea","Que haya equilibrio","Que se haya secado"],"Más texturas no significa mejor obra.")]]
M4={"subject_id":SID,"tema":4,"practica":"Práctica general: textura y materia","examen_titulo":"Nivel jefe: textura y materia","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT4,"examen":EX4}
os.makedirs(os.path.join(AQUI,"mision-4"),exist_ok=True); json.dump(M4,open(os.path.join(AQUI,"mision-4","mision-4.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={1:"3dae644c-c338-4e64-b662-ffbdd829937e",2:"d7134cfb-da95-4d42-94ca-eb30782628e2",3:"b5239197-5ab5-4396-837b-f5e6c7a8dabf",4:"717adfc6-ed47-4200-a4cf-13864aa9735a"}
TIT={1:"Texturas visuales y táctiles",2:"Frotage, collage y ensamblaje",3:"Materiales y soportes",4:"Pintar y dibujar con técnicas mixtas"}
def NEU(e,**k): e=dict(e); e["neutro"]=k; return e
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
DA=lambda n,a,d,t,e,v:{"t":"dato","numero":n,"antes":a,"despues":d,"texto":t,"emoji":e,"voz":v}
RET=lambda tx,seg,resp,em,ti,sub,v:{"t":"reto","texto":tx,"segundos":seg,"respuesta":resp,"emoji":em,"titulo":ti,"sub":sub,"voz":v}
NOT=lambda ci,ti,ba,em,tt,sub,v:{"t":"noticia","cinta":ci,"titular":ti,"bajada":ba,"emoji":em,"titulo":tt,"sub":sub,"voz":v}
BQ=lambda t,it,v:{"t":"bloques","titulo":t,"items":[{"cab":a,"txt":b} for a,b in it],"voz":v}
ZO=lambda it,v:{"t":"zoom","niveles":[{"emoji":a,"txt":b} for a,b in it],"voz":v}
LI=lambda t,ev,v:{"t":"linea","titulo":t,"eventos":[{"fecha":a,"txt":b,"emoji":c} for a,b,c in ev],"voz":v}
BA=lambda t,i,d,g,v:{"t":"balanza","izq":{"cab":i[0],"items":i[1]},"der":{"cab":d[0],"items":d[1]},"gana":g,"voz":v}
FL=lambda t,it,v:{"t":"flujo","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
VE=lambda a,b,ia,ib,am,v:{"t":"venn","a":a,"b":b,"itemsA":ia,"itemsB":ib,"ambos":am,"voz":v}
CLS={1:[
 NOT("TEXTURA","Una hoja de papel","Puede ser rugosa o lisa","📄","TEXTURAS","visuales y táctiles",["Noticia: una hoja de papel puede ser rugosa o lisa.","Hoy: *texturas visuales y táctiles*."]),
 DEF("Textura","Aspecto de una superficie","🧶",["La *textura* es el aspecto de una superficie.","Puede ser lisa, rugosa, suave o áspera."]),
 VE("TÁCTIL","VISUAL",["Se toca","Lana"],["Se ve","Dibujo de lana"],["Es textura"],["Dos tipos de textura.","La *táctil*: se toca.","La *visual*: se ve.","Y las dos son *textura*."]),
 ZO([("🌳","Un tronco"),("🪵","Su corteza"),("🔍","Sus relieves")],["Mirá de cerca.","Un *tronco*.","Su *corteza*.","Y sus *relieves*."]),
 Q("La textura visual…",["Se ve sin tocar","Solo se toca","No existe"],0,["Te toca: la textura visual.","¿Se ve sin tocar, solo se toca o no existe?","*Se ve sin tocar*."]),
 ER([("Una sola línea para todo","Líneas distintas"),("Creer que solo se toca","También se ve")],["Errores típicos.","Usar *una sola línea* para todas las texturas.","Y creer que la textura *solo se toca*."]),
 RES(["Repasemos.","La *textura* es el aspecto de la superficie.","Hay *táctil* y *visual*.","Se puede *dibujar*.","Y también transmite *ideas*.","¡Clase terminada! Ahora, *a practicar*."],[["TEXTURA","aspecto de la superficie"],["TÁCTIL","se toca"],["VISUAL","se ve"],["MENSAJE","sugiere ideas"]])],
2:[
 RET("¿Cómo se llama la técnica de copiar un relieve frotando un crayón?",6,"Frotage","🖍️","FROTAGE","collage y ensamblaje",["Desafío: ¿cómo se llama la técnica de copiar un relieve frotando un crayón? Seis segundos.","Frotage.","Hoy: *frotage, collage y ensamblaje*."]),
 PA("FROTAGE",[("Poner el papel","📄"),("Inclinar el crayón","🖍️"),("Frotar suave","✋"),("Ver el relieve","👀")],["Los pasos del *frotage*.","Primero, el *papel* sobre el relieve.","Después, el *crayón* inclinado.","Se frota *suave*.","Y aparece el *relieve*."]),
 CMP(("COLLAGE","Pega materiales en una superficie","✂️"),("ENSAMBLAJE","Une objetos en volumen","🧩"),"vs",["Dos técnicas distintas.","El *collage* pega materiales en una superficie.","El *ensamblaje* une objetos en volumen."]),
 DA("3","dimensiones","en el ensamblaje","El ensamblaje tiene alto, ancho y profundidad","🧩",["Un dato.","El ensamblaje tiene *tres dimensiones*."]),
 Q("El ensamblaje es una obra…",["En tres dimensiones","Solo plana","Solo de papel"],0,["Te toca: el ensamblaje.","¿En tres dimensiones, solo plana o solo de papel?","*En tres dimensiones*."]),
 ER([("Mover el papel al frotar","Mantenerlo quieto"),("Mucho pegamento","Poco y parejo")],["Errores típicos.","*Mover el papel* al frotar.","Y usar *mucho pegamento*."]),
 RES(["Repasemos.","El *frotage* copia relieves.","El *collage* pega materiales.","El *ensamblaje* tiene volumen.","Y se pueden *combinar*.","¡Clase terminada! Ahora, *a practicar*."],[["FROTAGE","copia texturas"],["COLLAGE","pega materiales"],["ENSAMBLAJE","tres dimensiones"],["COMBINAR","según el resultado"]])],
3:[
 NOT("SOPORTE","Una obra sobre madera","Con las vetas a la vista","🪵","MATERIALES","y soportes",["Noticia: una obra sobre madera deja las vetas a la vista.","Hoy: *materiales y soportes*."]),
 DEF("Soporte","Superficie de la obra","🖼️",["El *soporte* es la superficie de la obra.","Puede ser papel, tela, madera o pared."]),
 TB("PAPELES",["Soporte","Sirve para"],[["Papel liso","Lápiz"],["Papel con grano","Acuarela"],["Cartón","Collage"]],["Tres soportes comunes.","El *papel liso*: lápiz.","El *papel con grano*: acuarela.","Y el *cartón*: collage."]),
 AD(("PAPEL FINO","😬","La acuarela lo rompe"),("PAPEL CON GRANO","😊","Aguanta el agua"),["Elegir bien el soporte.","Con *papel fino*, la acuarela lo rompe.","Con *papel con grano*, aguanta el agua."]),
 FL("RECICLAR",[("Tapitas","🔘"),("Se limpian","🧼"),("Se pegan","🧴"),("Mosaico","🖼️")],["Un ejemplo de *reciclado*.","Las *tapitas*.","Se *limpian*.","Se *pegan*.","Y forman un *mosaico*."]),
 Q("El soporte es…",["La superficie de la obra","El pincel","El color"],0,["Te toca: el soporte.","¿La superficie de la obra, el pincel o el color?","*La superficie de la obra*."]),
 ER([("Acuarela en papel fino","Papel con grano"),("Tirar lo reutilizable","Reciclar")],["Errores típicos.","Pintar *acuarela* en papel muy fino.","Y *tirar* lo reutilizable."]),
 RES(["Repasemos.","El *soporte* es la superficie.","El *material* es lo que se usa.","Se eligen *juntos*.","Y el *reciclado* da segunda vida.","¡Clase terminada! Ahora, *a practicar*."],[["SOPORTE","superficie"],["MATERIAL","lo que se usa"],["JUNTOS","se eligen a la vez"],["RECICLAR","segunda vida"]])],
4:[
 RET("¿Cómo se llama la obra que combina varias técnicas?",6,"Técnica mixta","🎨","TÉCNICA MIXTA","combinar para crear",["Desafío: ¿cómo se llama la obra que combina varias técnicas? Seis segundos.","Técnica mixta.","Hoy: *combinar técnicas*."]),
 LI("ORDEN DE TRABAJO",[("1","Fondo","🎨"),("2","Texturas","🧶"),("3","Dibujo","✏️"),("4","Detalles","✨")],["Las capas de una técnica mixta.","Primero, el *fondo*.","Después, las *texturas*.","Luego, el *dibujo*.","Y al final, los *detalles*."]),
 BA("EQUILIBRIO",("MUCHAS TEXTURAS",["Obra cargada"]),("UNA DOMINA",["Obra clara"]),"der",["El *equilibrio* de texturas.","Muchas texturas cargan la obra.","Con una dominante, la obra se ve *clara*."]),
 BQ("AL TERMINAR",[("IDEA","¿Se entiende?"),("EQUILIBRIO","¿Está parejo?"),("SECADO","¿Se secó todo?")],["Qué revisar al terminar.","La *idea*.","El *equilibrio*.","Y el *secado*."]),
 Q("Para destacar las texturas conviene…",["Dejar una zona lisa","Llenar todo","No pensar"],0,["Te toca: destacar texturas.","¿Dejar una zona lisa, llenar todo o no pensar?","*Dejar una zona lisa*."]),
 RES(["Repasemos.","La *técnica mixta* combina.","Se trabaja por *capas*.","Una textura *domina*.","Y se *revisa* al terminar.","¡Clase terminada! Ahora, *a practicar*."],[["MIXTA","combina técnicas"],["CAPAS","fondo a detalles"],["EQUILIBRIO","una domina"],["REVISAR","idea y secado"]])]}
for n,es in CLS.items():
    json.dump({"slug":f"arte1-m4-n{n}","step_id":STEPS[n],"materia":"Arte y Comunicación I","titulo":TIT[n],"sub":f"Arte y Comunicación I · Misión 4 · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"arte1-m4-n{n}.json"),"w"),ensure_ascii=False)
print("ok")
