# -*- coding: utf-8 -*-
"""Arte y Comunicación I · Misión 3 (El color) · COMÚN. Genera mision-3.json y 4 clases."""
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
def img_rueda():
    fig, ax = plt.subplots(figsize=(5.4, 4.6)); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.2, 1.3); ax.axis("off"); ax.set_aspect("equal")
    from matplotlib.patches import Wedge
    cols = ["#e63946", "#f4722b", "#f9c22e", "#9ccc3b", "#2fa84f", "#1fb5a3", "#2b7fd1", "#4a4ec9", "#8a3fc0", "#c63a96", "#d6336c", "#e8505b"]
    nombres = {0: "Rojo", 2: "Amarillo", 6: "Azul"}
    for i, c in enumerate(cols):
        a0 = 90 - (i + 1) * 30; ax.add_patch(Wedge((0, 0), 1.0, a0, a0 + 30, width=0.45, fc=c, ec="white", lw=2))
    ax.text(0, 0, "Círculo\ncromático", ha="center", va="center", fontsize=11, color=O, fontweight="bold")
    ax.annotate("Primarios: rojo,\namarillo y azul", xy=(0.2, 0.8), xytext=(0.55, 1.15), arrowprops=dict(arrowstyle="->", color=O, lw=1.5), fontsize=10, color=O, fontweight="bold")
    ax.annotate("Cálidos", xy=(0.7, 0.35), xytext=(1.0, 0.0), arrowprops=dict(arrowstyle="->", color=O, lw=1.5), fontsize=11, color=O, fontweight="bold")
    ax.annotate("Fríos", xy=(-0.75, -0.3), xytext=(-1.28, -1.0), arrowprops=dict(arrowstyle="->", color=O, lw=1.5), fontsize=11, color=O, fontweight="bold")
    return png(fig)
B1=NV("Vas a mezclar pigmentos y entender cómo se organiza el color.",["Pigmentos y luz","Primarios y secundarios","Círculo cromático","Mezclas y tonos"],[
 S(1,"Pigmentos y luz",[D("Pigmento","Sustancia que da color a una pintura y que absorbe parte de la luz que recibe."),P("Un objeto se ve de un color porque refleja ese color y absorbe los demás. Al mezclar pigmentos se absorbe cada vez más luz, por eso la mezcla se oscurece.")]),
 S(1,"Primarios y secundarios",[T("Colores pigmento",["Tipo","Colores"],[["Primarios","Rojo, amarillo y azul"],["Secundarios","Naranja, verde y violeta, mezcla de dos primarios"],["Terciarios","Mezcla de un primario y un secundario vecino"]])]),
 S(2,"Círculo cromático",[D("Círculo cromático","Ordena los colores en círculo, de modo que se vea cómo se relacionan."),IMG("Círculo cromático","Doce colores ordenados en círculo.","Un círculo de doce colores: rojo, naranja, amarillo, verde, azul, violeta y sus mezclas intermedias. Se marcan los primarios y la mitad de colores cálidos y la mitad de colores fríos.",img_rueda())]),
 S(2,"Mezclas y tonos",[T("Cómo cambiar un color",["Para…","Se agrega…"],[["Aclarar","Blanco"],["Oscurecer","Negro o su complementario"],["Apagar","Un poco de su color opuesto"]]),IM("Poco a poco","Se agrega el color oscuro de a gotas: un poco alcanza.")])],
 {"titulo":"mezclar","planteo":"Querés obtener verde. ¿Cómo lo mezclás y lo ajustás?","pasos":["Mezclar amarillo y azul.","Más amarillo da un verde claro y cálido.","Más azul da un verde oscuro y frío.","Agregar blanco para aclarar si hace falta."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los colores que salen de mezclar dos primarios son los ___ .","El círculo ordena los colores para ver cómo se ___ ."]},
 {"titulo":"tu turno","planteo":"Con tres colores primarios y blanco armá seis muestras: tres secundarios y tres tonos aclarados. Rotulá cada una."},
 {"titulo":"Un color por vez","texto":"Mezclá dos colores por vez: así sabés qué hizo cada uno."},
 ["Agregar mucho color oscuro de golpe.","Mezclar muchos colores a la vez y no saber el resultado."],
 RS(("Primarios","Rojo, amarillo y azul."),("Secundarios","Mezcla de dos primarios."),("Círculo","Ordena los colores."),("Tonos","Con blanco o negro.")),
 G(("Pigmento","Sustancia que da color."),("Primario","Color que no sale de otros."),("Secundario","Mezcla de dos primarios."),("Tono","Variación clara u oscura.")),
 ["¿Cómo se llaman los colores rojo, amarillo y azul?","¿Qué color sale de mezclar amarillo y azul?","¿Se aclara un color agregando blanco? Respondé sí o no.","¿Conviene agregar mucho color oscuro de golpe? Respondé sí o no."],
 [["primarios","los primarios","colores primarios"],["verde","el verde"],["si","sí"],["no"]],
 {"incompleto":"Primarios. Verde.","solo":"Mezclé amarillo y azul y salió verde. Con más azul se hizo oscuro y con blanco quedó claro. Las muestras las rotulé una por una.","carpeta":["Primarios.","Verde.","Sí.","No."]})
B2=NV("Vas a reconocer colores cálidos y fríos y armar combinaciones que funcionen.",["Cálidos y fríos","Colores complementarios","Armonías","Contraste"],[
 S(1,"Cálidos y fríos",[T("Temperatura del color",["Grupo","Colores y sensación"],[["Cálidos","Rojo, naranja y amarillo: transmiten energía y cercanía"],["Fríos","Azul, verde y violeta: transmiten calma y distancia"]]),P("Los colores cálidos parecen acercarse y los fríos parecen alejarse. Por eso se usan para dar profundidad.")]),
 S(1,"Colores complementarios",[D("Colores complementarios","Los que están enfrentados en el círculo cromático; juntos se ven más intensos."),P("Rojo y verde, azul y naranja, amarillo y violeta son pares complementarios.")]),
 S(2,"Armonías",[T("Tipos de armonía",["Armonía","Cómo se arma"],[["Análoga","Colores vecinos en el círculo"],["Complementaria","Colores opuestos en el círculo"],["Monocromática","Un solo color con sus tonos claros y oscuros"]])]),
 S(2,"Contraste",[P("El contraste es la diferencia entre colores. Un contraste fuerte, como amarillo sobre violeta, llama la atención. Un contraste suave, como dos azules, da calma."),IM("Un protagonista","Conviene que un color domine y los otros acompañen.")])],
 {"titulo":"armonía","planteo":"Querés un cartel que llame la atención. ¿Qué colores elegís?","pasos":["Elegir un par complementario, por ejemplo azul y naranja.","Usar uno como color principal.","Usar el otro solo en detalles.","Agregar blanco o neutro para descansar la vista."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los colores enfrentados en el círculo son los ___ .","Una armonía de un solo color con sus tonos es ___ ."]},
 {"titulo":"tu turno","planteo":"Pintá tres cuadrados chicos, uno con armonía análoga, uno complementaria y uno monocromática, y escribí cuál te gustó más."},
 {"titulo":"Mirá la temperatura","texto":"Antes de pintar decidí si la escena será más cálida o más fría."},
 ["Usar todos los colores con la misma fuerza.","Creer que el contraste fuerte siempre queda mejor."],
 RS(("Cálidos","Rojo, naranja, amarillo."),("Fríos","Azul, verde, violeta."),("Complementarios","Opuestos en el círculo."),("Armonías","Análoga, complementaria, mono.")),
 G(("Cálido","Color que da energía."),("Frío","Color que da calma."),("Complementario","Color opuesto."),("Armonía","Combinación equilibrada.")),
 ["¿Cómo se llaman los colores enfrentados en el círculo cromático?","¿Cómo se llama la armonía de un solo color con sus tonos?","¿Los colores cálidos parecen acercarse? Respondé sí o no.","¿Conviene que todos los colores tengan la misma fuerza? Respondé sí o no."],
 [["complementarios","los complementarios","colores complementarios"],["monocromatica","monocromática","armonia monocromatica","armonía monocromática"],["si","sí"],["no"]],
 {"incompleto":"Complementarios. Monocromática.","solo":"Hice tres cuadrados: verdes vecinos, azul con naranja y solo rojos. El de azul y naranja llama más la atención.","carpeta":["Complementarios.","Monocromática.","Sí.","No."]})
B3=NV("Vas a usar el color para transmitir emociones y significados.",["Color y emoción","Significados","Cultura y contexto","Intención"],[
 S(1,"Color y emoción",[P("Los colores se asocian con emociones. Por ejemplo, el rojo puede sugerir pasión o peligro, el azul calma o tristeza, el amarillo alegría y el negro misterio o duelo."),T("Algunas asociaciones habituales",["Color","Puede transmitir"],[["Rojo","Energía, pasión, peligro"],["Azul","Calma, confianza, tristeza"],["Amarillo","Alegría, atención"],["Verde","Naturaleza, esperanza"]])]),
 S(1,"Significados",[D("Valor simbólico del color","Significado que una comunidad le da a un color más allá de su aspecto."),P("Un mismo color puede significar cosas distintas según la cultura y la época.")]),
 S(2,"Cultura y contexto",[P("En muchas culturas el blanco se asocia con la paz, pero en otras con el duelo. Los colores de una bandera o de un equipo también tienen significados propios."),IM("Preguntar antes de suponer","Cuando un color tiene un significado, conviene saber de dónde viene.")]),
 S(2,"Intención",[T("Decisiones de color con propósito",["Pregunta","Ejemplo"],[["¿Qué quiero transmitir?","Calma"],["¿Qué colores lo logran?","Azules y verdes suaves"],["¿Qué evito?","Rojos intensos"]])])],
 {"titulo":"intención","planteo":"Querés pintar una escena que transmita calma. ¿Qué decidís?","pasos":["Elegir azules y verdes suaves.","Usar contrastes bajos.","Agregar un toque cálido pequeño como detalle.","Evitar rojos intensos que rompan la calma."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El significado que una comunidad le da a un color es su valor ___ .","El azul suele transmitir ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí una emoción y pintá una mancha de color que la represente. Escribí por qué elegiste esos colores."},
 {"titulo":"Color con motivo","texto":"Cada color de tu obra debería tener una razón para estar."},
 ["Creer que un color significa lo mismo en todas las culturas.","Elegir colores sin pensar qué se quiere transmitir."],
 RS(("Emoción","El color transmite emociones."),("Símbolo","Significado dado por la comunidad."),("Cultura","Cambia el significado."),("Intención","Elegir con propósito.")),
 G(("Emoción","Sensación que algo provoca."),("Símbolo","Cosa que representa una idea."),("Cultura","Costumbres de un pueblo."),("Intención","Lo que quiero transmitir.")),
 ["¿Cómo se llama el significado que una comunidad le da a un color?","¿Qué emoción suele transmitir el azul suave?","¿Un color significa lo mismo en todas las culturas? Respondé sí o no.","¿Conviene elegir colores sin pensar qué se quiere transmitir? Respondé sí o no."],
 [["valor simbolico","valor simbólico","simbolico","simbólico"],["calma","tranquilidad"],["no"],["no"]],
 {"incompleto":"Simbólico. Calma.","solo":"Elegí la tristeza: azules grises y un poco de violeta. Dejé un toque amarillo para mostrar esperanza.","carpeta":["Valor simbólico.","Calma.","No.","No."]})
B4=NV("Vas a armar una paleta propia para pintar con un propósito.",["Qué es una paleta","Cómo elegir colores","Probar y ajustar","Pintar con la paleta"],[
 S(1,"Qué es una paleta",[D("Paleta","Conjunto limitado de colores elegidos para una obra."),P("Usar pocos colores hace que la obra se vea unida. Una paleta de cinco o seis colores alcanza para pintar casi cualquier cosa.")]),
 S(1,"Cómo elegir colores",[T("Pasos para armar la paleta",["Paso","Qué se hace"],[["1. Propósito","Definir qué se quiere transmitir"],["2. Dominante","Elegir el color principal"],["3. Apoyos","Sumar dos colores que acompañen"],["4. Acento","Sumar un color pequeño que resalte"]])]),
 S(2,"Probar y ajustar",[P("Antes de pintar se prueban los colores juntos en una hoja aparte. Si algo no funciona, se cambia un color o su cantidad, no todo."),IM("Hoja de pruebas","Una hoja chica para probar evita arruinar la obra final.")]),
 S(2,"Pintar con la paleta",[T("Proporciones sugeridas",["Color","Cantidad aproximada"],[["Dominante","Más de la mitad"],["Apoyos","Un tercio"],["Acento","Muy poco"]]),P("Mantener las proporciones ayuda a que la obra tenga orden y un punto de atención.")])],
 {"titulo":"paleta","planteo":"Vas a pintar un paisaje de atardecer. ¿Cómo armás la paleta?","pasos":["Propósito: transmitir calidez y calma.","Dominante: naranja.","Apoyos: violeta y rosado suave.","Acento: un toque de amarillo."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un conjunto limitado de colores elegidos para una obra es una ___ .","El color pequeño que resalta es el ___ ."]},
 {"titulo":"tu turno","planteo":"Armá una paleta de cinco colores para una obra sobre el mar, probala en una hoja aparte y pintá una escena chica."},
 {"titulo":"Pocos colores","texto":"Una paleta chica te obliga a mezclar y a descubrir tonos nuevos."},
 ["Usar todos los colores del estuche en la misma obra.","Pintar la obra final sin probar antes."],
 RS(("Paleta","Colores elegidos."),("Dominante","Color principal."),("Acento","Toque que resalta."),("Prueba","Hoja aparte.")),
 G(("Paleta","Colores elegidos para una obra."),("Dominante","El que más se ve."),("Acento","Toque pequeño que resalta."),("Unidad","Que todo parezca parte de lo mismo.")),
 ["¿Cómo se llama el conjunto limitado de colores elegidos para una obra?","¿Cómo se llama el color pequeño que resalta?","¿Conviene probar los colores en una hoja aparte? Respondé sí o no.","¿Conviene usar todos los colores del estuche en la misma obra? Respondé sí o no."],
 [["paleta","la paleta"],["acento","el acento"],["si","sí"],["no"]],
 {"incompleto":"Paleta. Acento.","solo":"Para el mar elegí azul, verde agua, blanco, arena y un acento naranja. Primero probé en una hoja y después pinté una escena chica.","carpeta":["Paleta.","Acento.","Sí.","No."]})
ACT3={"1":[{"t":"classify","p":"¿Primario o secundario?","o":{"elementos":["Rojo","Verde","Azul","Naranja"],"categorias":["Primario","Secundario"]},"r":{"categorias":{"Rojo":"Primario","Verde":"Secundario","Azul":"Primario","Naranja":"Secundario"}},"e":"Los secundarios salen de mezclar dos primarios."},MC("¿Qué se agrega para aclarar un color?",["Blanco","Negro","Su opuesto","Nada"],"Blanco","El blanco aclara.")],
 "2":[{"t":"matching","p":"Uní cada término con su definición.","o":{"izquierda":["Cálidos","Fríos","Complementarios","Monocromática"],"derecha":["Rojo, naranja y amarillo","Azul, verde y violeta","Enfrentados en el círculo","Un solo color con sus tonos"]},"r":{"pares":{"Cálidos":"Rojo, naranja y amarillo","Fríos":"Azul, verde y violeta","Complementarios":"Enfrentados en el círculo","Monocromática":"Un solo color con sus tonos"}},"e":"Cada término, su definición."},VF("Los colores cálidos parecen acercarse.","Verdadero","Dan sensación de cercanía.")],
 "3":[MS("¿Qué pueden influir en el significado de un color?",["La cultura","La época","El contexto","El tamaño del lápiz"],["La cultura","La época","El contexto"],"El tamaño del lápiz no cambia el significado."),FB("El significado que una comunidad le da a un color es su valor ___ .",[["simbolico","simbólico"]],"Es lo que representa.")],
 "4":[{"t":"ordering","p":"Ordená los pasos para armar una paleta.","o":["Acento","Propósito","Apoyos","Dominante"],"r":{"orden":["Propósito","Dominante","Apoyos","Acento"]},"e":"De la idea al detalle."},TT("Tocá el color que ocupa más lugar: «El dominante ocupa más de la mitad».",["El","dominante","ocupa","más","de","la","mitad."],[1],"El dominante es el principal.")],
 "5":[{"t":"classify","p":"Cálido o frío.","o":{"elementos":["Rojo","Azul","Amarillo","Violeta"],"categorias":["Cálido","Frío"]},"r":{"categorias":{"Rojo":"Cálido","Azul":"Frío","Amarillo":"Cálido","Violeta":"Frío"}},"e":"Cada color tiene su temperatura.","tiempo":30},
  FB("El color que sale de mezclar amarillo y azul es el ___ .",[["verde"]],"Es un secundario.",tiempo=20),
  VF("Un color significa lo mismo en todas las culturas.","Falso","Cambia según la cultura.",tiempo=15),
  {"t":"ordering","p":"Ordená de mayor a menor cantidad en una paleta.","o":["Acento","Dominante","Apoyos"],"r":{"orden":["Dominante","Apoyos","Acento"]},"e":"El dominante es el más usado.","tiempo":40}]}
EX3=[[1,MC("Los colores primarios son…",["Rojo, amarillo y azul","Verde, naranja y violeta","Blanco y negro","Rosa y gris"],"Rojo, amarillo y azul","No salen de otras mezclas.")],
 [1,VF("Mezclar azul y amarillo da verde.","Verdadero","Es un secundario.")],
 [1,MC("Para aclarar un color se agrega…",["Blanco","Negro","Más pigmento oscuro","Agua sucia"],"Blanco","El blanco aclara.")],
 [2,MC("Los colores complementarios son los que…",["Están enfrentados en el círculo","Están juntos","Son del mismo grupo","No se pueden mezclar"],"Están enfrentados en el círculo","Juntos se ven más intensos.")],
 [2,VF("Los colores fríos transmiten calma y distancia.","Verdadero","Son azules, verdes y violetas.")],
 [2,MS("¿Qué armonías existen?",["Análoga","Complementaria","Monocromática","Aleatoria"],["Análoga","Complementaria","Monocromática"],"La aleatoria no es una armonía.")],
 [3,MC("El significado que una comunidad le da a un color es su valor…",["Simbólico","Químico","Físico","Técnico"],"Simbólico","Representa una idea.")],
 [3,VF("Un mismo color puede significar cosas distintas según la cultura.","Verdadero","Depende del contexto.")],
 [3,FB("El azul suave suele transmitir ___ .",[["calma","tranquilidad"]],"Es un color frío.")],
 [4,MC("Un conjunto limitado de colores elegidos para una obra es una…",["Paleta","Textura","Perspectiva","Escala"],"Paleta","Da unidad a la obra.")],
 [4,VF("Conviene probar los colores en una hoja aparte antes de pintar la obra final.","Verdadero","Evita arruinar la obra.")],
 [4,MC("El color pequeño que resalta en una paleta es el…",["Acento","Dominante","Apoyo","Fondo"],"Acento","Llama la atención.")],
 [4,MS("¿Qué pasos sirven para armar una paleta?",["Definir el propósito","Elegir el dominante","Sumar apoyos","Usar todos los colores del estuche"],["Definir el propósito","Elegir el dominante","Sumar apoyos"],"Una paleta es limitada.")]]
M3={"subject_id":SID,"tema":3,"practica":"Práctica general: el color","examen_titulo":"Nivel jefe: el color","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT3,"examen":EX3}
os.makedirs(os.path.join(AQUI,"mision-3"),exist_ok=True); json.dump(M3,open(os.path.join(AQUI,"mision-3","mision-3.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={1:"ff3f0d15-4115-4ac1-b6c3-44df868c8615",2:"0d6335c7-2017-4149-877d-8dab43074484",3:"81c9c80d-0a2a-453d-bf9e-bd9236d276a5",4:"2bb1c736-3f2a-4dd8-91e7-972f9c6da816"}
TIT={1:"Pigmentos y círculo cromático",2:"Colores cálidos, fríos y armonías",3:"El color y las emociones",4:"Una paleta propia para pintar con propósito"}
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
CLS={1:[
 RET("¿Qué color sale de mezclar amarillo y azul?",6,"Verde","🎨","EL COLOR","pigmentos y círculo cromático",["Desafío: ¿qué color sale de mezclar amarillo y azul? Seis segundos.","Verde.","Hoy: *pigmentos y círculo cromático*."]),
 DEF("Pigmento","Sustancia que da color","🖌️",["Un *pigmento* es una sustancia que da color.","Absorbe parte de la luz que recibe."]),
 PA("PRIMARIOS",[("Rojo","🔴"),("Amarillo","🟡"),("Azul","🔵")],["Tres colores primarios.","*Rojo*.","*Amarillo*.","Y *azul*.","No salen de otras mezclas."]),
 CL([("PRIMARIO","⭐"),("SECUNDARIO","🔀")],[("Rojo",0),("Verde",1),("Azul",0),("Naranja",1)],["¿Primario o secundario?","*Rojo* y *azul*: primarios.","*Verde* y *naranja*: secundarios."]),
 TB("CAMBIAR UN COLOR",["Para…","Agregar"],[["Aclarar","Blanco"],["Oscurecer","Negro"],["Apagar","Su opuesto"]],["Cómo cambiar un color.","Para *aclarar*: blanco.","Para *oscurecer*: negro.","Y para *apagar*: su opuesto."]),
 Q("Amarillo más azul da…",["Verde","Naranja","Violeta"],0,["Te toca: amarillo más azul.","¿Verde, naranja o violeta?","*Verde*."]),
 ER([("Mucho oscuro de golpe","De a gotas"),("Mezclar muchos colores a la vez","Dos por vez")],["Errores típicos.","Agregar *mucho oscuro* de golpe.","Y mezclar *muchos colores* a la vez."]),
 RES(["Repasemos.","Hay tres *primarios*.","Dos primarios dan un *secundario*.","El *círculo* los ordena.","Y con *blanco o negro* cambia el tono.","¡Clase terminada! Ahora, *a practicar*."],[["PRIMARIOS","rojo, amarillo, azul"],["SECUNDARIOS","dos primarios"],["CÍRCULO","ordena colores"],["TONOS","blanco o negro"]])],
2:[
 NOT("COLOR","Un cartel que llama la atención","Usa colores opuestos","🪧","CÁLIDOS Y FRÍOS","armonías",["Noticia: un cartel llama la atención usando colores opuestos.","Hoy: *colores cálidos, fríos y armonías*."]),
 CL([("CÁLIDO","🔥"),("FRÍO","❄️")],[("Rojo",0),("Azul",1),("Amarillo",0),("Violeta",1)],["¿Cálido o frío?","*Rojo* y *amarillo*: cálidos.","*Azul* y *violeta*: fríos."]),
 DEF("Complementarios","Opuestos en el círculo","↔️",["Los *complementarios* están enfrentados en el círculo.","Juntos se ven más intensos."]),
 TB("ARMONÍAS",["Armonía","Cómo se arma"],[["Análoga","Colores vecinos"],["Complementaria","Colores opuestos"],["Monocromática","Un solo color"]],["Tipos de armonía.","*Análoga*: colores vecinos.","*Complementaria*: opuestos.","Y *monocromática*: un solo color."]),
 Q("Los colores cálidos parecen…",["Acercarse","Alejarse","Desaparecer"],0,["Te toca: los cálidos.","¿Acercarse, alejarse o desaparecer?","*Acercarse*."]),
 ER([("Todos los colores con la misma fuerza","Un protagonista"),("Contraste fuerte siempre","Según la intención")],["Errores típicos.","Usar todos los colores *con la misma fuerza*.","Y creer que el contraste fuerte *siempre* queda mejor."]),
 RES(["Repasemos.","Hay colores *cálidos* y *fríos*.","Los *complementarios* son opuestos.","Hay tres *armonías*.","Y conviene un color *protagonista*.","¡Clase terminada! Ahora, *a practicar*."],[["TEMPERATURA","cálidos y fríos"],["COMPLEMENTARIOS","opuestos"],["ARMONÍAS","tres tipos"],["CONTRASTE","un protagonista"]])],
3:[
 RET("¿Qué emoción suele transmitir el azul suave?",6,"Calma","💙","EL COLOR","y las emociones",["Desafío: ¿qué emoción suele transmitir el azul suave? Seis segundos.","Calma.","Hoy: *el color y las emociones*."]),
 TB("ASOCIACIONES",["Color","Transmite"],[["Rojo","Energía, peligro"],["Azul","Calma, tristeza"],["Amarillo","Alegría"],["Verde","Naturaleza"]],["Algunas asociaciones.","El *rojo*: energía o peligro.","El *azul*: calma o tristeza.","El *amarillo*: alegría.","Y el *verde*: naturaleza."]),
 DEF("Valor simbólico","Lo que un color representa","🏳️",["El *valor simbólico* es lo que un color representa.","Lo da la comunidad."]),
 CL([("DEPENDE","🌍"),("NO DEPENDE","📏")],[("Sentido del blanco",0),("Tamaño del pincel",1),("Época",0),("Cantidad de pintura",1)],["¿Depende de la cultura?","*Significado* y *época*: dependen.","*Pincel* y *cantidad*: no dependen."]),
 Q("Un color significa lo mismo en…",["Ninguna cultura única","Todas las culturas","Solo Argentina"],0,["Te toca: significados.","¿Ninguna cultura única, todas o solo Argentina?","El significado *cambia* según la cultura."]),
 ER([("Suponer que significa lo mismo","Preguntar de dónde viene"),("Elegir sin pensar","Elegir con intención")],["Errores típicos.","Creer que significa *lo mismo en todas partes*.","Y elegir colores *sin pensar*."]),
 RES(["Repasemos.","Los colores transmiten *emociones*.","Tienen *valor simbólico*.","Cambia según la *cultura*.","Y se elige *con intención*.","¡Clase terminada! Ahora, *a practicar*."],[["EMOCIÓN","el color transmite"],["SÍMBOLO","lo da la comunidad"],["CULTURA","cambia significados"],["INTENCIÓN","con propósito"]])],
4:[
 NOT("PALETA","Cinco colores alcanzan","Para pintar casi todo","🎨","LA PALETA","propia",["Noticia: cinco colores alcanzan para pintar casi cualquier cosa.","Hoy: *una paleta propia*."]),
 DEF("Paleta","Colores elegidos para una obra","🎨",["Una *paleta* es un conjunto limitado de colores.","Se eligen para una obra."]),
 PA("PASOS",[("Propósito","🎯"),("Dominante","🟧"),("Apoyos","🟪"),("Acento","✨")],["Cuatro pasos.","El *propósito*.","El *dominante*.","Los *apoyos*.","Y el *acento*."]),
 TB("PROPORCIONES",["Color","Cantidad"],[["Dominante","Más de la mitad"],["Apoyos","Un tercio"],["Acento","Muy poco"]],["Proporciones sugeridas.","El *dominante*: más de la mitad.","Los *apoyos*: un tercio.","Y el *acento*: muy poco."]),
 Q("Antes de pintar la obra final conviene…",["Probar en una hoja","Usar todos los colores","Pintar sin pensar"],0,["Te toca: antes de pintar.","¿Probar en una hoja, usar todos los colores o pintar sin pensar?","*Probar en una hoja*."]),
 RES(["Repasemos.","La *paleta* es limitada.","Se arma con *propósito*.","Se *prueba* antes.","Y se respetan las *proporciones*.","¡Clase terminada! Ahora, *a practicar*."],[["PALETA","pocos colores"],["PASOS","propósito a acento"],["PRUEBA","hoja aparte"],["PROPORCIÓN","dominante grande"]])]}
for n,es in CLS.items():
    json.dump({"slug":f"arte1-m3-n{n}","step_id":STEPS[n],"materia":"Arte y Comunicación I","titulo":TIT[n],"sub":f"Arte y Comunicación I · Misión 3 · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"arte1-m3-n{n}.json"),"w"),ensure_ascii=False)
print("ok")
