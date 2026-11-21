# -*- coding: utf-8 -*-
"""Arte y Comunicación I · Misión 6 (Escultura y objeto) · COMÚN. Genera mision-6.json y 4 clases."""
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
def img_cubo():
    fig, ax = plt.subplots(figsize=(5.6, 4.2)); ax.set_xlim(0, 4.5); ax.set_ylim(0, 3.4); ax.axis("off"); ax.set_aspect("equal")
    cel = [(1, 2), (0, 1), (1, 1), (2, 1), (3, 1), (1, 0)]
    for k, (x, y) in enumerate(cel):
        ax.add_patch(plt.Rectangle((x + 0.2, y + 0.2), 1, 1, fc=C if k != 2 else "#e8913a", ec=V, lw=2.5, zorder=2))
    ax.add_patch(plt.Rectangle((4.2, 1.2), 0.25, 1, fc="#bbb", ec=V, lw=1.5, zorder=1))
    ax.text(1.7, 1.7, "Base", ha="center", va="center", fontsize=11, color=O, fontweight="bold", zorder=5)
    ax.annotate("Caras", xy=(0.7, 1.7), xytext=(0.0, 3.0), arrowprops=dict(arrowstyle="->", color=O, lw=1.5), fontsize=11, color=O, fontweight="bold")
    ax.annotate("Solapa para pegar", xy=(4.3, 1.7), xytext=(2.9, 3.0), arrowprops=dict(arrowstyle="->", color=O, lw=1.5), fontsize=11, color=O, fontweight="bold")
    ax.annotate("Pliegues", xy=(2.2, 1.2), xytext=(3.0, 0.1), arrowprops=dict(arrowstyle="->", color=O, lw=1.5), fontsize=11, color=O, fontweight="bold")
    return png(fig)
B1=NV("Vas a modelar con arcilla o masa para crear formas en volumen.",["Modelar","Preparar la masa","Técnicas de modelado","Secado y cuidado"],[
 S(1,"Modelar",[D("Modelado","Técnica que da forma a una materia blanda, como arcilla o masa, con las manos o con herramientas."),P("Modelar es construir en volumen: se puede agregar y quitar material hasta lograr la forma.")]),
 S(1,"Preparar la masa",[T("Antes de modelar",["Paso","Para qué sirve"],[["Amasar","Saca el aire y la deja pareja"],["Humedecer apenas","Evita que se agriete"],["Armar una bola","Es el punto de partida de la forma"]])]),
 S(2,"Técnicas de modelado",[T("Tres técnicas básicas",["Técnica","Cómo es"],[["Pellizcado","Se hunde el pulgar y se pellizcan las paredes"],["Rollitos","Se apilan tiras enrolladas"],["Placas","Se estira la masa y se cortan piezas"]])]),
 S(2,"Secado y cuidado",[P("La pieza se seca despacio y lejos del sol directo para que no se agriete. Las piezas de arcilla se cocinan en horno cerámico, y las de masa se dejan secar al aire."),IM("Paciencia","Un secado lento evita grietas.")])],
 {"titulo":"modelar","planteo":"Querés modelar un cuenco. ¿Cómo lo hacés?","pasos":["Amasar para sacar el aire.","Hacer una bola y hundir el pulgar en el centro.","Pellizcar las paredes hasta que queden parejas.","Dejar secar lento y a la sombra."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La técnica que da forma a una materia blanda es el ___ .","Para sacar el aire de la masa se la ___ ."]},
 {"titulo":"tu turno","planteo":"Modelá una pieza pequeña con masa o arcilla usando pellizcado y un detalle hecho con rollitos. Anotá qué te costó."},
 {"titulo":"Sacá el aire","texto":"Amasá bien antes de modelar: el aire atrapado puede romper la pieza."},
 ["Dejar burbujas de aire en la masa.","Secar la pieza al sol fuerte de golpe."],
 RS(("Modelado","Dar forma a materia blanda."),("Amasar","Saca el aire."),("Técnicas","Pellizcado, rollitos y placas."),("Secado","Lento y sin sol directo.")),
 G(("Modelado","Dar forma a una materia blanda."),("Arcilla","Tierra que se moldea húmeda."),("Pellizcado","Técnica con los dedos."),("Placa","Masa estirada.")),
 ["¿Cómo se llama la técnica que da forma a una materia blanda?","¿Qué se hace con la masa para sacarle el aire?","¿El secado conviene que sea lento? Respondé sí o no.","¿Conviene dejar burbujas de aire dentro de la masa? Respondé sí o no."],
 [["modelado","el modelado"],["amasar","se amasa","amasarla"],["si","sí"],["no"]],
 {"incompleto":"Modelado. Amasar.","solo":"Hice un cuenco con pellizcado y le agregué un asa con rollitos. Me costó que las paredes quedaran parejas.","carpeta":["Modelado.","Amasar.","Sí.","No."]})
B2=NV("Vas a construir una obra uniendo materiales reutilizados.",["Ensamblar","Formas de unir","Materiales reutilizados","Un mensaje con sentido"],[
 S(1,"Ensamblar",[D("Ensamblaje","Obra que se arma uniendo partes u objetos distintos."),P("Al ensamblar, cada pieza aporta su forma, su color y su historia.")]),
 S(1,"Formas de unir",[T("Maneras de unir piezas",["Forma","Ejemplo"],[["Pegar","Con adhesivo o cola vinílica"],["Atar","Con hilo, alambre o cuerda"],["Encastrar","Haciendo cortes que calcen"],["Clavar o abrochar","Con clavos o broches, con ayuda adulta"]])]),
 S(2,"Materiales reutilizados",[P("Cajas, tapas, telas, cables y envases se pueden reutilizar. Reutilizar reduce los residuos y permite crear con lo que ya existe."),IM("Limpios y seguros","Los materiales se limpian y se evitan los que tienen filos peligrosos.")]),
 S(2,"Un mensaje con sentido",[P("Un ensamblaje puede decir algo sobre el consumo, el ambiente o la memoria. Elegir los materiales con intención hace que la obra comunique mejor.")])],
 {"titulo":"ensamblar","planteo":"Querés hacer un robot con materiales reutilizados. ¿Cómo lo armás?","pasos":["Juntar cajas, tapitas y tubos.","Armar el cuerpo con cajas pegadas.","Atar los brazos con alambre blando.","Agregar detalles con tapitas."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La obra que se arma uniendo partes u objetos distintos es un ___ .","Los materiales que se usan de nuevo son ___ ."]},
 {"titulo":"tu turno","planteo":"Armá un ensamblaje con al menos tres materiales reutilizados y escribí qué mensaje querés dar."},
 {"titulo":"Pensá antes de pegar","texto":"Probá cómo se ven las piezas juntas antes de pegarlas."},
 ["Usar materiales con filos peligrosos.","Pegar todo sin probar antes la composición."],
 RS(("Ensamblaje","Une partes distintas."),("Unir","Pegar, atar o encastrar."),("Reutilizar","Menos residuos."),("Mensaje","Ideas con intención.")),
 G(("Ensamblaje","Obra hecha uniendo partes."),("Encastrar","Unir con cortes que calzan."),("Reutilizar","Usar de nuevo."),("Residuo","Lo que se tira.")),
 ["¿Cómo se llama la obra que se arma uniendo partes u objetos distintos?","¿Cómo se llama usar un material de nuevo en vez de tirarlo?","¿Reutilizar materiales reduce los residuos? Respondé sí o no.","¿Conviene usar materiales con filos peligrosos? Respondé sí o no."],
 [["ensamblaje","el ensamblaje"],["reutilizar","reutilizarlo","reutilizacion","reutilización"],["si","sí"],["no"]],
 {"incompleto":"Ensamblaje. Reutilizar.","solo":"Armé un robot con cajas, tapitas y tubos. Quise mostrar que lo que parece basura puede convertirse en arte.","carpeta":["Ensamblaje.","Reutilizar.","Sí.","No."]})
B3=NV("Vas a transformar objetos cotidianos en obras de arte.",["El objeto como obra","Elegir el objeto","Cambiar su sentido","Mostrar la obra"],[
 S(1,"El objeto como obra",[D("Objeto encontrado","Objeto de uso cotidiano que un artista elige y presenta como obra."),P("Algunos artistas cambiaron el arte al usar objetos comunes. Al sacarlos de su contexto, se los mira de otra manera.")]),
 S(1,"Elegir el objeto",[T("Cómo elegir",["Pregunta","Para qué sirve"],[["¿Qué forma tiene?","Detectar su aspecto"],["¿Para qué se usa?","Pensar su historia"],["¿Qué podría ser?","Imaginar otros usos"]])]),
 S(2,"Cambiar su sentido",[T("Tres maneras de transformarlo",["Manera","Ejemplo"],[["Descontextualizar","Poner una cuchara en un marco, como una escultura"],["Combinar","Unir un zapato y una planta"],["Modificar","Pintar o cubrir el objeto"]])]),
 S(2,"Mostrar la obra",[P("La forma de mostrar una obra también comunica. Un título, una base y una buena iluminación ayudan a que el público la vea como arte."),IM("El título cuenta","Un título puede cambiar cómo se mira la obra.")])],
 {"titulo":"transformar","planteo":"Tenés una cuchara de madera. ¿Cómo la convertís en obra?","pasos":["Mirar su forma y su historia.","Imaginar que parece una persona.","Pintarle una cara y vestirla con tela.","Ponerle un título y una base."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un objeto de uso cotidiano presentado como obra es un objeto ___ .","Sacar un objeto de su lugar habitual es ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un objeto cotidiano, transformalo con una de las tres maneras y ponele título. Anotá qué querés mostrar."},
 {"titulo":"Mirá distinto","texto":"Mirá el objeto como si no supieras para qué sirve: así aparecen otras formas."},
 ["Creer que un objeto cotidiano nunca puede ser arte.","Presentar la obra sin título ni base."],
 RS(("Objeto encontrado","Cotidiano y elegido."),("Elegir","Forma, uso y posibilidades."),("Transformar","Descontextualizar, combinar, modificar."),("Mostrar","Título y base.")),
 G(("Objeto encontrado","Cotidiano elegido como obra."),("Contexto","Lugar habitual de algo."),("Descontextualizar","Sacar de su lugar."),("Título","Nombre de la obra.")),
 ["¿Cómo se llama el objeto de uso cotidiano que se presenta como obra?","¿Cómo se llama sacar un objeto de su lugar habitual?","¿Un título puede cambiar cómo se mira la obra? Respondé sí o no.","¿Un objeto cotidiano nunca puede ser arte? Respondé sí o no."],
 [["objeto encontrado","encontrado","el objeto encontrado"],["descontextualizar","descontextualizacion","descontextualización"],["si","sí"],["no"]],
 {"incompleto":"Encontrado. Descontextualizar.","solo":"Elegí un cepillo de dientes y lo puse en un marco como si fuera una escultura. Lo llamé 'Sonrisa de hoy'.","carpeta":["Objeto encontrado.","Descontextualizar.","Sí.","No."]})
B4=NV("Vas a armar volúmenes con papel y cartón.",["Del plano al volumen","Plegar, cortar y pegar","Volúmenes básicos","Construir y decorar"],[
 S(1,"Del plano al volumen",[D("Desarrollo plano","Dibujo de un volumen abierto sobre una superficie plana, listo para cortar y plegar."),P("Con una hoja de cartón bien planificada se pueden armar cubos, cajas y figuras en tres dimensiones.")]),
 S(1,"Plegar, cortar y pegar",[T("Herramientas y su uso",["Acción","Cómo se hace"],[["Cortar","Con tijera, siguiendo las líneas"],["Plegar","Marcando antes con una regla y algo sin punta"],["Pegar","Con solapas y pegamento en poca cantidad"]])]),
 S(2,"Volúmenes básicos",[P("Los volúmenes básicos son el cubo, la pirámide, el cilindro y el cono. Al combinarlos se arman objetos más complejos."),IMG("Desarrollo plano de un cubo","Seis caras y una solapa para pegar.","Seis cuadrados unidos en forma de cruz que forman el desarrollo plano de un cubo, con una base central, cuatro caras laterales y una cara superior, y una pequeña solapa para pegar. Se marcan las caras, la solapa y los pliegues.",img_cubo())]),
 S(2,"Construir y decorar",[P("Una vez armado el volumen se puede decorar con pintura, papeles o texturas. Conviene decorar antes de pegar las caras finales, cuando el cartón todavía está plano."),IM("Probá con papel","Hacer una prueba con papel común evita gastar cartón bueno.")])],
 {"titulo":"construir","planteo":"Querés armar una caja con tapa. ¿Cómo lo hacés?","pasos":["Dibujar el desarrollo plano con la regla.","Cortar por el contorno.","Marcar y plegar por las líneas internas.","Pegar las solapas con poco pegamento."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El dibujo plano de un volumen abierto, listo para plegar, es el ___ .","La parte pequeña que se pega para unir dos caras es la ___ ."]},
 {"titulo":"tu turno","planteo":"Armá un cubo de cartón a partir de su desarrollo plano y decoralo. Anotá qué ajustaste."},
 {"titulo":"Medí dos veces","texto":"Medí dos veces antes de cortar una vez."},
 ["Cortar sin haber trazado antes el desarrollo.","Poner demasiado pegamento y mojar el cartón."],
 RS(("Desarrollo","Volumen abierto y plano."),("Cortar","Siguiendo las líneas."),("Plegar","Marcando antes."),("Solapa","Se pega al unir.")),
 G(("Desarrollo plano","Volumen abierto sobre un plano."),("Solapa","Pestaña para pegar."),("Volumen","Espacio que ocupa un cuerpo."),("Pliegue","Línea donde se dobla.")),
 ["¿Cómo se llama el dibujo plano de un volumen abierto?","¿Cómo se llama la pestaña pequeña que se pega para unir dos caras?","¿Conviene marcar el pliegue antes de doblar? Respondé sí o no.","¿Conviene poner mucho pegamento? Respondé sí o no."],
 [["desarrollo plano","desarrollo","el desarrollo plano"],["solapa","la solapa","pestana","pestaña"],["si","sí"],["no"]],
 {"incompleto":"Desarrollo. Solapa.","solo":"Dibujé el desarrollo de un cubo, lo corté, marqué los pliegues y pegué las solapas. Tuve que agrandar la solapa porque se despegaba.","carpeta":["Desarrollo plano.","Solapa.","Sí.","No."]})
ACT6={"1":[{"t":"classify","p":"¿Qué técnica de modelado es?","o":{"elementos":["Hundir el pulgar y pellizcar","Apilar tiras enrolladas","Estirar la masa y cortar piezas","Pellizcar las paredes del cuenco"],"categorias":["Pellizcado","Rollitos","Placas"]},"r":{"categorias":{"Hundir el pulgar y pellizcar":"Pellizcado","Apilar tiras enrolladas":"Rollitos","Estirar la masa y cortar piezas":"Placas","Pellizcar las paredes del cuenco":"Pellizcado"}},"e":"Cada técnica tiene su forma."},MC("¿Para qué se amasa la arcilla?",["Para sacar el aire","Para mojarla","Para pintarla","Para secarla"],"Para sacar el aire","El aire atrapado puede romper la pieza.")],
 "2":[{"t":"matching","p":"Uní cada forma de unir con su ejemplo.","o":{"izquierda":["Pegar","Atar","Encastrar"],"derecha":["Con cola vinílica","Con hilo o alambre","Haciendo cortes que calzan"]},"r":{"pares":{"Pegar":"Con cola vinílica","Atar":"Con hilo o alambre","Encastrar":"Haciendo cortes que calzan"}},"e":"Cada forma tiene su método."},VF("Reutilizar materiales reduce los residuos.","Verdadero","Se usa lo que ya existe.")],
 "3":[MS("¿Cómo se puede transformar un objeto cotidiano?",["Descontextualizarlo","Combinarlo con otro","Modificarlo","Esconderlo sin mostrar"],["Descontextualizarlo","Combinarlo con otro","Modificarlo"],"Esconderlo no lo transforma en obra."),FB("Un objeto cotidiano presentado como obra es un objeto ___ .",[["encontrado"]],"Lo elige un artista.")],
 "4":[{"t":"ordering","p":"Ordená los pasos para armar un cubo de cartón.","o":["Pegar solapas","Dibujar el desarrollo","Plegar","Cortar"],"r":{"orden":["Dibujar el desarrollo","Cortar","Plegar","Pegar solapas"]},"e":"Del plano al volumen."},TT("Tocá la palabra clave: «El desarrollo plano se corta y se pliega».",["El","desarrollo","plano","se","corta","y","se","pliega."],[1],"Es el dibujo del volumen abierto.")],
 "5":[{"t":"classify","p":"Técnica o material.","o":{"elementos":["Pellizcado","Arcilla","Ensamblaje","Cartón"],"categorias":["Técnica","Material"]},"r":{"categorias":{"Pellizcado":"Técnica","Arcilla":"Material","Ensamblaje":"Técnica","Cartón":"Material"}},"e":"Una se hace; el otro se usa.","tiempo":30},
  VF("Un objeto cotidiano nunca puede ser arte.","Falso","Puede serlo si se lo transforma.",tiempo=15),
  {"t":"matching","p":"Uní cada volumen con su descripción.","o":{"izquierda":["Cubo","Cilindro","Pirámide"],"derecha":["Seis caras cuadradas","Base circular","Caras que llegan a un punto"]},"r":{"pares":{"Cubo":"Seis caras cuadradas","Cilindro":"Base circular","Pirámide":"Caras que llegan a un punto"}},"e":"Cada volumen se reconoce.","tiempo":35},
  FB("La parte pequeña que se pega al unir dos caras es la ___ .",[["solapa"]],"Une las caras.",tiempo=20)]}
EX6=[[1,MC("La técnica que da forma a una materia blanda es el…",["Modelado","Grabado","Collage","Boceto"],"Modelado","Se hace con las manos o herramientas.")],
 [1,VF("Se amasa la arcilla para sacarle el aire.","Verdadero","Evita roturas.")],
 [1,MC("Las tiras enrolladas que se apilan son la técnica de…",["Rollitos","Pellizcado","Placas","Calado"],"Rollitos","Se construye en capas.")],
 [2,MC("La obra que se arma uniendo partes u objetos distintos es el…",["Ensamblaje","Frotage","Boceto","Grabado"],"Ensamblaje","Cada pieza aporta algo.")],
 [2,VF("Reutilizar materiales reduce los residuos.","Verdadero","Se crea con lo que ya existe.")],
 [2,MC("Unir piezas haciendo cortes que calzan es…",["Encastrar","Pegar","Atar","Clavar"],"Encastrar","No necesita adhesivo.")],
 [3,MC("Un objeto de uso cotidiano presentado como obra es un objeto…",["Encontrado","Perdido","Pintado","Modelado"],"Encontrado","Lo elige un artista.")],
 [3,VF("Sacar un objeto de su lugar habitual se llama descontextualizar.","Verdadero","Cambia cómo se lo mira.")],
 [3,FB("Un ___ puede cambiar cómo se mira la obra.",[["titulo","título"]],"Orienta la lectura.")],
 [4,MC("El dibujo plano de un volumen abierto es el…",["Desarrollo plano","Boceto","Collage","Contorno"],"Desarrollo plano","Se corta y se pliega.")],
 [4,VF("Conviene marcar el pliegue antes de doblar el cartón.","Verdadero","Queda más prolijo.")],
 [4,MC("La pestaña que se pega para unir dos caras es la…",["Solapa","Base","Tapa","Arista"],"Solapa","Une las caras.")],
 [4,MS("¿Qué conviene al armar un volumen de cartón?",["Trazar el desarrollo","Marcar los pliegues","Poner poco pegamento","Cortar sin medir"],["Trazar el desarrollo","Marcar los pliegues","Poner poco pegamento"],"Siempre se mide antes de cortar.")]]
M6={"subject_id":SID,"tema":6,"practica":"Práctica general: escultura y objeto","examen_titulo":"Nivel jefe: escultura y objeto","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT6,"examen":EX6}
os.makedirs(os.path.join(AQUI,"mision-6"),exist_ok=True); json.dump(M6,open(os.path.join(AQUI,"mision-6","mision-6.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={1:"7c3a5809-046c-470a-a79f-4168cfee8fcf",2:"9385be43-90f4-4278-a7b4-92c945c94d10",3:"d7fac365-692a-4a07-83cd-a8d063da77e9",4:"b16d80ec-a9aa-4eb4-a90d-602a8ec74560"}
TIT={1:"Modelar con arcilla y masa",2:"Construir con ensamblajes y materiales reutilizados",3:"Arte con objetos cotidianos",4:"Armar volúmenes en papel y cartón"}
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
VE=lambda a,b,ia,ib,am,v:{"t":"venn","a":a,"b":b,"itemsA":ia,"itemsB":ib,"ambos":am,"voz":v}
FL=lambda t,it,v:{"t":"flujo","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
MAT=lambda t,c,v:{"t":"matriz","titulo":t,"celdas":[{"cab":a,"txt":b} for a,b in c],"voz":v}
CH=lambda n,m,t,s,v:{"t":"chat","contacto":{"nombre":n[0],"emoji":n[1]},"mensajes":[{"yo":a,"txt":b} for a,b in m],"titulo":t,"sub":s,"voz":v}
DA=lambda n,a,d,t,e,v:{"t":"dato","numero":n,"antes":a,"despues":d,"texto":t,"emoji":e,"voz":v}
CLS={1:[
 NOT("ESCULTURA","Una bola de masa","Se vuelve un cuenco","🏺","MODELAR","con arcilla y masa",["Noticia: una bola de masa se vuelve un cuenco.","Con las manos y mucha paciencia.","Hoy: *modelar con arcilla y masa*."]),
 DEF("Modelado","Dar forma a una materia blanda","🏺",["El *modelado* da forma a una materia blanda.","Se puede agregar y quitar material."]),
 FL("PREPARAR Y MODELAR",[("Amasar","✋"),("Armar la bola","⚪"),("Modelar","🏺"),("Secar lento","⏳")],["Un camino de cuatro pasos.","Primero, *amasar*.","Después, armar una *bola*.","Luego, *modelar*.","Y por último, *secar lento*."]),
 AD(("SIN AMASAR","💥","Quedan burbujas y se rompe"),("AMASADA","✅","Queda firme y pareja"),["La diferencia se nota.","Sin amasar, quedan *burbujas* y se rompe.","Amasada, queda *firme y pareja*."]),
 Q("¿Para qué se amasa la masa?",["Para sacar el aire","Para mojarla","Para pintarla"],0,["Te toca: amasar.","¿Para sacar el aire, para mojarla o para pintarla?","Para *sacar el aire*."]),
 ER([("Burbujas de aire","Amasar bien"),("Sol fuerte de golpe","Secado lento")],["Errores típicos.","Dejar *burbujas de aire*.","Y secar al *sol fuerte* de golpe."]),
 RES(["Repasemos.","El *modelado* da forma a la materia.","Se *amasa* primero.","Hay tres técnicas: *pellizcado, rollitos y placas*.","Y el secado es *lento*.","¡Clase terminada! Ahora, *a practicar*."],[["MODELADO","dar forma"],["AMASAR","sacar el aire"],["TÉCNICAS","tres básicas"],["SECADO","lento"]])],
2:[
 RET("¿Cómo se llama la obra que une partes u objetos distintos?",6,"Ensamblaje","🧩","ENSAMBLAJES","y materiales reutilizados",["Desafío: ¿cómo se llama la obra que une partes u objetos distintos? Seis segundos.","Ensamblaje.","Hoy: *ensamblajes y materiales reutilizados*."]),
 DEF("Ensamblaje","Obra que une partes distintas","🧩",["Un *ensamblaje* une partes u objetos distintos.","Cada pieza aporta algo."]),
 MAT("CÓMO UNIR",[("PEGAR","Con cola vinílica"),("ATAR","Con hilo o alambre"),("ENCASTRAR","Con cortes que calzan"),("CLAVAR","Solo con ayuda adulta")],["Cuatro formas de unir.","*Pegar*: con cola vinílica.","*Atar*: con hilo o alambre.","*Encastrar*: con cortes que calzan.","Y *clavar*, solo con ayuda adulta."]),
 CAU(("Reutilizar","♻️"),[("Menos residuos","🗑️"),("Ideas nuevas","💡")],["Reutilizar tiene *efectos*.","Hay *menos residuos*.","Y salen *ideas nuevas*."]),
 Q("Unir con cortes que calzan es…",["Encastrar","Pegar","Clavar"],0,["Te toca: unir con cortes.","¿Encastrar, pegar o clavar?","*Encastrar*."]),
 ER([("Filos peligrosos","Materiales seguros"),("Pegar sin probar","Probar antes")],["Errores típicos.","Usar materiales con *filos peligrosos*.","Y *pegar sin probar* la composición."]),
 RES(["Repasemos.","Un *ensamblaje* une partes.","Se puede *pegar, atar o encastrar*.","*Reutilizar* reduce residuos.","Y el *mensaje* importa.","¡Clase terminada! Ahora, *a practicar*."],[["ENSAMBLAJE","une partes"],["UNIR","pegar, atar, encastrar"],["REUTILIZAR","menos residuos"],["MENSAJE","con intención"]])],
3:[
 NOT("ARTE","Una cuchara en un marco","Y ya parece escultura","🥄","OBJETOS COTIDIANOS","convertidos en arte",["Noticia: una cuchara en un marco parece una escultura.","Cambia el contexto.","Hoy: *objetos cotidianos convertidos en arte*."]),
 DEF("Objeto encontrado","Cotidiano presentado como obra","🥄",["Un *objeto encontrado* es un objeto cotidiano.","Elegido y presentado como obra."]),
 VE("OBJETO","OBRA",["Se usa todos los días","Tiene una función"],["Tiene un título","Se muestra con intención"],["Una cuchara en un marco"],["Objeto y obra.","El *objeto* tiene una función.","La *obra* tiene título e intención.","Y un objeto elegido puede ser *las dos cosas*."]),
 BQ("TRANSFORMAR UN OBJETO",[("DESCONTEXTUALIZAR","Sacarlo de su lugar"),("COMBINAR","Unirlo con otro"),("MODIFICAR","Pintar o cubrir")],["Tres maneras de transformarlo.","*Descontextualizar*: sacarlo de su lugar.","*Combinar*: unirlo con otro.","Y *modificar*: pintarlo o cubrirlo."]),
 Q("Sacar un objeto de su lugar habitual es…",["Descontextualizar","Amasar","Plegar"],0,["Te toca: sacar un objeto de su lugar.","¿Descontextualizar, amasar o plegar?","*Descontextualizar*."]),
 ER([("Un objeto cotidiano no es arte","Puede serlo"),("Sin título ni base","Mostrarlo con intención")],["Errores típicos.","Creer que un objeto cotidiano *no puede ser arte*.","Y mostrarlo *sin título* ni base."]),
 RES(["Repasemos.","El *objeto encontrado* es cotidiano y elegido.","Se elige por *forma y uso*.","Se transforma de *tres maneras*.","Y el *título* cuenta.","¡Clase terminada! Ahora, *a practicar*."],[["ENCONTRADO","cotidiano y elegido"],["ELEGIR","forma y uso"],["TRANSFORMAR","tres maneras"],["TÍTULO","orienta la lectura"]])],
4:[
 RET("¿Cómo se llama el dibujo plano de un volumen abierto?",6,"Desarrollo plano","📦","VOLÚMENES","en papel y cartón",["Desafío: ¿cómo se llama el dibujo plano de un volumen abierto? Seis segundos.","Desarrollo plano.","Hoy: *volúmenes en papel y cartón*."]),
 LI("ARMAR UN CUBO",[("1","Dibujar","✏️"),("2","Cortar","✂️"),("3","Plegar","📐"),("4","Pegar","🧴")],["Cuatro pasos para armar un cubo.","Primero, *dibujar* el desarrollo.","Después, *cortar*.","Luego, *plegar*.","Y al final, *pegar*."]),
 DA("6","caras","tiene un cubo","Y todas son cuadrados iguales","🎲",["Un dato del cubo.","Tiene *seis caras*."]),
 Q("La pestaña que se pega para unir caras es la…",["Solapa","Base","Arista"],0,["Te toca: la pestaña de pegado.","¿Solapa, base o arista?","La *solapa*."]),
 ER([("Cortar sin trazar","Dibujar antes"),("Mucho pegamento","Poco y parejo")],["Errores típicos.","*Cortar sin trazar* el desarrollo.","Y poner *mucho pegamento*."]),
 RES(["Repasemos.","El *desarrollo plano* es el volumen abierto.","Se *corta* y se *pliega*.","Se pega con *solapas*.","Y se *decora* al final.","¡Clase terminada! Ahora, *a practicar*."],[["DESARROLLO","volumen abierto"],["CORTAR","siguiendo líneas"],["PLEGAR","marcando antes"],["SOLAPA","para pegar"]])]}
_N={'zoom':lambda e:len(e['niveles']),'antesdespues':lambda e:2,'linea':lambda e:len(e['eventos']),'flujo':lambda e:len(e['items'])}
for es in CLS.values():
    for e in es:
        if e['t'] in _N and len(e['voz'])==_N[e['t']](e)+1: e['voz']=[e['voz'][0]+' '+e['voz'][1]]+e['voz'][2:]
for n,es in CLS.items():
    json.dump({"slug":f"arte1-m6-n{n}","step_id":STEPS[n],"materia":"Arte y Comunicación I","titulo":TIT[n],"sub":f"Arte y Comunicación I · Misión 6 · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"arte1-m6-n{n}.json"),"w"),ensure_ascii=False)
print("ok")
