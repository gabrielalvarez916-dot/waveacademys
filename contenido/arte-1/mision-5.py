# -*- coding: utf-8 -*-
"""Arte y Comunicación I · Misión 5 (Componer el espacio) · COMÚN. Genera mision-5.json y 4 clases."""
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
def img_comp():
    fig, axs = plt.subplots(1, 3, figsize=(6.6, 2.9))
    for ax, t in zip(axs, ["Simétrica", "Asimétrica", "Regla de tercios"]):
        ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_xticks([]); ax.set_yticks([]); ax.set_facecolor("#efe9f5")
        for sp in ax.spines.values(): sp.set_color(V); sp.set_linewidth(2)
        ax.set_title(t, fontsize=11, color=O, fontweight="bold")
    a = axs[0]; a.add_patch(plt.Circle((2.7, 5), 1.5, color=V)); a.add_patch(plt.Circle((7.3, 5), 1.5, color=V)); a.plot([5, 5], [0, 10], color="#e8913a", lw=1.5, ls="--")
    b = axs[1]; b.add_patch(plt.Circle((3, 6), 2.4, color=V)); b.add_patch(plt.Circle((7.6, 3), 1.0, color="#e8913a"))
    c = axs[2]
    for t in (10 / 3, 20 / 3): c.plot([t, t], [0, 10], color="#999", lw=1, ls=":"); c.plot([0, 10], [t, t], color="#999", lw=1, ls=":")
    c.add_patch(plt.Circle((20 / 3, 20 / 3), 0.9, color=V)); c.add_patch(plt.Rectangle((0.8, 1.0), 3.2, 1.4, color="#e8913a"))
    fig.tight_layout()
    return png(fig)
def img_planos():
    fig, axs = plt.subplots(1, 3, figsize=(6.6, 2.9))
    for ax, t, r, y in zip(axs, ["Plano general", "Plano medio", "Primer plano"], [0.9, 2.4, 4.3], [3.2, 5.0, 5.2]):
        ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_xticks([]); ax.set_yticks([]); ax.set_facecolor("#efe9f5")
        for sp in ax.spines.values(): sp.set_color(V); sp.set_linewidth(2)
        ax.set_title(t, fontsize=11, color=O, fontweight="bold")
        ax.add_patch(plt.Circle((5, y + r * 0.9), r * 0.55, color="#e8913a")); ax.add_patch(plt.Rectangle((5 - r * .7, y - r * 1.1), r * 1.4, r * 1.6, color=V))
        ax.plot([0, 10], [1.2, 1.2], color="#999", lw=1)
    fig.tight_layout()
    return png(fig)
B1=NV("Vas a organizar los elementos de una imagen con equilibrio, ritmo y puntos de interés.",["Qué es componer","Equilibrio","Ritmo","Puntos de interés"],[
 S(1,"Qué es componer",[D("Composición","Forma en que se organizan los elementos dentro del espacio de una obra."),P("Una buena composición guía la mirada y ayuda a que se entienda lo que se quiere mostrar.")]),
 S(1,"Equilibrio",[T("Tipos de equilibrio",["Tipo","Cómo es"],[["Simétrico","Los elementos se repiten parejos a ambos lados de un eje"],["Asimétrico","Los elementos son distintos, pero se compensan por peso y color"]]),IMG("Tres formas de componer","Simétrica, asimétrica y regla de tercios.","Tres cuadros: en el primero dos círculos iguales a ambos lados de un eje; en el segundo un círculo grande y uno pequeño de otro color que se compensan; en el tercero una cuadrícula de tercios con un círculo en una intersección y un rectángulo abajo a la izquierda.",img_comp())]),
 S(2,"Ritmo",[D("Ritmo","Repetición de elementos que crea movimiento en la obra."),P("El ritmo puede ser regular, si el elemento se repite igual, o variado, si cambia de tamaño, color o distancia.")]),
 S(2,"Puntos de interés",[P("El punto de interés es la zona que más atrae la mirada. Se destaca con contraste, tamaño, color o ubicándolo en las intersecciones de la regla de tercios."),IM("Un solo protagonista","Conviene que haya un punto de interés principal.")])],
 {"titulo":"componer","planteo":"Vas a componer una imagen con una casa y un árbol. ¿Cómo lo hacés?","pasos":["Dividir la hoja en tercios con líneas suaves.","Poner la casa en una intersección.","Colocar el árbol del otro lado para compensar.","Repetir ventanas para crear ritmo."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La forma de organizar los elementos en el espacio de una obra es la ___ .","La repetición de elementos que crea movimiento es el ___ ."]},
 {"titulo":"tu turno","planteo":"Hacé tres composiciones chicas con las mismas formas: una simétrica, una asimétrica y una con regla de tercios. Anotá cuál te gustó más."},
 {"titulo":"Mirá el conjunto","texto":"Antes de dibujar un detalle, mirá cómo queda el conjunto en la hoja."},
 ["Poner todos los elementos en el centro.","Querer destacar todo al mismo tiempo."],
 RS(("Composición","Organiza el espacio."),("Equilibrio","Simétrico o asimétrico."),("Ritmo","Repetición."),("Interés","Punto que atrae.")),
 G(("Composición","Organización de los elementos."),("Simetría","Partes iguales a ambos lados."),("Ritmo","Repetición que da movimiento."),("Contraste","Diferencia que destaca.")),
 ["¿Cómo se llama la forma de organizar los elementos en el espacio de una obra?","¿Cómo se llama la repetición de elementos que crea movimiento?","¿Conviene que haya un punto de interés principal? Respondé sí o no.","¿Conviene poner todos los elementos en el centro? Respondé sí o no."],
 [["composicion","composición","la composicion","la composición"],["ritmo","el ritmo"],["si","sí"],["no"]],
 {"incompleto":"Composición. Ritmo.","solo":"Hice tres cuadros con una casa y un árbol: simétrico con ambos al centro, asimétrico con la casa grande y el árbol chico, y uno con la casa en un tercio. Me gustó el de tercios.","carpeta":["Composición.","Ritmo.","Sí.","No."]})
B2=NV("Vas a elegir planos, encuadres y puntos de vista para mostrar una escena.",["Los planos","Encuadre","Punto de vista","Elegir con intención"],[
 S(1,"Los planos",[IMG("Planos de una imagen","Plano general, plano medio y primer plano.","Tres cuadros con la misma figura: en el plano general se ve pequeña y rodeada de espacio; en el plano medio se ve de la cintura para arriba; en el primer plano ocupa casi todo el cuadro.",img_planos()),T("Los planos más usados",["Plano","Qué muestra"],[["General","Todo el lugar y la figura chica"],["Medio","La figura de la cintura para arriba"],["Primer plano","El detalle, como el rostro"]])]),
 S(1,"Encuadre",[D("Encuadre","Recorte de la escena que decidimos mostrar."),P("Lo que queda fuera del encuadre no se ve. Encuadrar es elegir qué entra y qué se deja afuera.")]),
 S(2,"Punto de vista",[T("Desde dónde se mira",["Punto de vista","Efecto"],[["A la altura de los ojos","Natural, cercano"],["Picado, desde arriba","El objeto parece chico o débil"],["Contrapicado, desde abajo","El objeto parece grande e imponente"]])]),
 S(2,"Elegir con intención",[P("Un mismo objeto cambia de significado según el plano y el punto de vista. Por eso conviene preguntarse qué se quiere transmitir antes de elegir."),IM("Probar varios","Hacer bocetos del mismo tema desde varios puntos de vista ayuda a decidir.")])],
 {"titulo":"encuadrar","planteo":"Querés mostrar un árbol enorme. ¿Qué plano y punto de vista elegís?","pasos":["Punto de vista contrapicado, desde abajo.","Plano general para que se vea completo.","Dejar poco cielo para sentir su altura.","Probar un boceto desde arriba para comparar."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El recorte de la escena que decidimos mostrar es el ___ .","Mirar desde abajo hacia arriba es un punto de vista ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un objeto y hacé tres bocetos: plano general, primer plano y desde un punto de vista picado. Escribí qué cambia."},
 {"titulo":"Decidí qué entra","texto":"Antes de dibujar, decidí qué entra en el cuadro y qué se queda afuera."},
 ["Mostrar siempre todo con el mismo plano.","Creer que el punto de vista no cambia el mensaje."],
 RS(("Planos","General, medio y primer plano."),("Encuadre","Qué se muestra."),("Picado","Desde arriba."),("Contrapicado","Desde abajo.")),
 G(("Plano","Distancia a la que se ve el objeto."),("Encuadre","Recorte de la escena."),("Picado","Visto desde arriba."),("Contrapicado","Visto desde abajo.")),
 ["¿Cómo se llama el recorte de la escena que decidimos mostrar?","¿Cómo se llama el punto de vista desde abajo hacia arriba?","¿El primer plano muestra un detalle de cerca? Respondé sí o no.","¿Un mismo objeto puede cambiar de significado según el punto de vista? Respondé sí o no."],
 [["encuadre","el encuadre"],["contrapicado","el contrapicado","contrapicada"],["si","sí"],["si","sí"]],
 {"incompleto":"Encuadre. Contrapicado.","solo":"Elegí una lámpara. En plano general se ve chica, en primer plano se ve el detalle de la pantalla y desde arriba parece aplastada.","carpeta":["Encuadre.","Contrapicado.","Sí.","Sí."]})
B3=NV("Vas a reconocer y representar espacios interiores, exteriores, públicos y privados.",["Interior y exterior","Público y privado","Representar el lugar","Atmósfera"],[
 S(1,"Interior y exterior",[T("Dos tipos de espacio",["Espacio","Ejemplos"],[["Interior","Una habitación, un aula, un museo"],["Exterior","Una plaza, una calle, un patio"]])]),
 S(1,"Público y privado",[D("Espacio público","Lugar abierto a todas las personas, como una plaza o una biblioteca."),D("Espacio privado","Lugar de uso reservado, como una casa o un jardín propio.")]),
 S(2,"Representar el lugar",[P("Para representar un espacio se eligen sus elementos más importantes y su escala: un interior suele mostrar paredes y muebles, y un exterior, cielo, suelo y construcciones."),IM("Mirar el espacio","Observar un lugar real antes de dibujarlo ayuda a captar su carácter.")]),
 S(2,"Atmósfera",[P("Los colores, la luz y los objetos crean la atmósfera de un espacio. Una luz cálida y pocos objetos pueden dar sensación de calma, mientras que muchos objetos y colores fuertes dan sensación de movimiento.")])],
 {"titulo":"espacio","planteo":"Querés dibujar tu cuarto como un espacio íntimo. ¿Qué decidís?","pasos":["Es un espacio interior y privado.","Mostrar los muebles más importantes.","Usar luz cálida y colores suaves.","Agregar objetos personales que cuenten quién lo usa."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un lugar abierto a todas las personas es un espacio ___ .","Los colores y la luz crean la ___ de un espacio."]},
 {"titulo":"tu turno","planteo":"Dibujá dos espacios de tu barrio, uno interior y uno exterior, y escribí si son públicos o privados."},
 {"titulo":"Un espacio con carácter","texto":"Pensá qué sensación querés que tenga el espacio antes de elegir los colores."},
 ["Creer que un espacio exterior siempre es público.","Dibujar todos los objetos sin elegir los importantes."],
 RS(("Interior","Dentro de un lugar cubierto."),("Exterior","Al aire libre."),("Público","Abierto a todos."),("Privado","De uso reservado.")),
 G(("Interior","Espacio cubierto."),("Exterior","Espacio al aire libre."),("Público","De todas las personas."),("Atmósfera","Sensación de un lugar.")),
 ["¿Cómo se llama el espacio abierto a todas las personas?","¿Cómo se llama la sensación que crean los colores y la luz en un espacio?","¿Una plaza es un espacio exterior? Respondé sí o no.","¿Un patio propio siempre es un espacio público? Respondé sí o no."],
 [["publico","público","espacio publico","espacio público"],["atmosfera","atmósfera","la atmosfera","la atmósfera"],["si","sí"],["no"]],
 {"incompleto":"Público. Atmósfera.","solo":"Dibujé mi aula, un espacio interior y público, y la plaza, exterior y pública. En el aula puse pupitres y en la plaza, árboles y bancos.","carpeta":["Público.","Atmósfera.","Sí.","No."]})
B4=NV("Vas a pasar de la representación plana al volumen y a representar el espacio en tres dimensiones.",["Dos y tres dimensiones","Planta y vista","Maqueta","Probar y ajustar"],[
 S(1,"Dos y tres dimensiones",[D("Bidimensional","Obra o figura que tiene alto y ancho, como un dibujo sobre una hoja."),D("Tridimensional","Obra o figura que tiene alto, ancho y profundidad, como una escultura.")]),
 S(1,"Planta y vista",[T("Representar un espacio",["Representación","Qué muestra"],[["Planta","El espacio visto desde arriba"],["Vista frontal","El espacio visto de frente"],["Maqueta","El espacio en volumen y a escala"]])]),
 S(2,"Maqueta",[P("Una maqueta es un modelo en tres dimensiones de un espacio. Se arma con cartón, papel, plastilina u objetos pequeños, manteniendo las proporciones."),IM("Escala","Todas las partes deben usar la misma escala para que la maqueta se vea creíble.")]),
 S(2,"Probar y ajustar",[P("Al pasar del plano a la maqueta se descubren problemas que en el dibujo no se veían. Conviene probar, mirar desde varios lados y ajustar.")])],
 {"titulo":"maqueta","planteo":"Vas a hacer la maqueta de tu aula. ¿Cómo lo hacés?","pasos":["Dibujar la planta del aula.","Cortar cartones con la medida de cada pared.","Armar los muebles con cajitas pequeñas.","Mirar desde varios lados y ajustar."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Una obra con alto y ancho es ___ .","Un modelo en tres dimensiones de un espacio es una ___ ."]},
 {"titulo":"tu turno","planteo":"Dibujá la planta de un cuarto y armá una maqueta sencilla con cartón. Anotá qué ajustes tuviste que hacer."},
 {"titulo":"Misma escala","texto":"Medí todo con la misma regla: así las partes de la maqueta se ven proporcionadas."},
 ["Armar la maqueta sin hacer antes la planta.","Usar escalas distintas para cada parte."],
 RS(("2D","Alto y ancho."),("3D","Alto, ancho y profundidad."),("Planta","Vista desde arriba."),("Maqueta","Modelo en volumen.")),
 G(("Bidimensional","Con alto y ancho."),("Tridimensional","Con profundidad."),("Planta","Vista desde arriba."),("Maqueta","Modelo en volumen.")),
 ["¿Cómo se llama la obra que tiene alto, ancho y profundidad?","¿Cómo se llama el modelo en tres dimensiones de un espacio?","¿La planta muestra el espacio visto desde arriba? Respondé sí o no.","¿Conviene usar escalas distintas para cada parte de la maqueta? Respondé sí o no."],
 [["tridimensional","tridimensional","3d"],["maqueta","la maqueta"],["si","sí"],["no"]],
 {"incompleto":"Tridimensional. Maqueta.","solo":"Dibujé la planta de mi cuarto y armé una maqueta con cartón. Me di cuenta de que la cama tapaba la puerta y la moví.","carpeta":["Tridimensional.","Maqueta.","Sí.","No."]})
ACT5={"1":[{"t":"classify","p":"¿Simétrico o asimétrico?","o":{"elementos":["Dos círculos iguales a los lados","Un círculo grande y uno chico","Mariposa con alas iguales","Casa a un lado y árbol al otro"],"categorias":["Simétrico","Asimétrico"]},"r":{"categorias":{"Dos círculos iguales a los lados":"Simétrico","Un círculo grande y uno chico":"Asimétrico","Mariposa con alas iguales":"Simétrico","Casa a un lado y árbol al otro":"Asimétrico"}},"e":"Simétrico es parejo; asimétrico se compensa."},MC("¿Dónde conviene poner un punto de interés?",["En una intersección de tercios","En una esquina cortada","Siempre bien pegado al borde","Nunca importa"],"En una intersección de tercios","La regla de tercios guía la mirada.")],
 "2":[{"t":"matching","p":"Uní cada plano con lo que muestra.","o":{"izquierda":["Plano general","Plano medio","Primer plano","Contrapicado"],"derecha":["Todo el lugar","De la cintura para arriba","El detalle de cerca","Visto desde abajo"]},"r":{"pares":{"Plano general":"Todo el lugar","Plano medio":"De la cintura para arriba","Primer plano":"El detalle de cerca","Contrapicado":"Visto desde abajo"}},"e":"Cada plano muestra una distancia."},VF("El encuadre es el recorte de la escena que decidimos mostrar.","Verdadero","Lo que queda afuera no se ve.")],
 "3":[MS("¿Cuáles son espacios exteriores?",["Una plaza","Una calle","Un patio","Un aula"],["Una plaza","Una calle","Un patio"],"El aula es un espacio interior."),FB("Un lugar abierto a todas las personas es un espacio ___ .",[["publico","público"]],"Todos pueden usarlo.")],
 "4":[{"t":"ordering","p":"Ordená los pasos para hacer una maqueta.","o":["Armar con cartón","Probar y ajustar","Dibujar la planta","Medir las paredes"],"r":{"orden":["Dibujar la planta","Medir las paredes","Armar con cartón","Probar y ajustar"]},"e":"Del plano al volumen."},TT("Tocá la palabra: «Una maqueta es un modelo tridimensional».",["Una","maqueta","es","un","modelo","tridimensional."],[5],"Tridimensional: con profundidad.")],
 "5":[{"t":"ordering","p":"Ordená de menor a mayor cercanía.","o":["Primer plano","Plano general","Plano medio"],"r":{"orden":["Plano general","Plano medio","Primer plano"]},"e":"Cada plano se acerca más.","tiempo":35},
  VF("Un exterior siempre es público.","Falso","Un patio propio es exterior y privado.",tiempo=15),
  FB("La repetición de elementos que crea movimiento es el ___ .",[["ritmo"]],"Puede ser regular o variado.",tiempo=20),
  {"t":"classify","p":"2D o 3D.","o":{"elementos":["Dibujo en hoja","Escultura","Maqueta","Pintura en lienzo"],"categorias":["2D","3D"]},"r":{"categorias":{"Dibujo en hoja":"2D","Escultura":"3D","Maqueta":"3D","Pintura en lienzo":"2D"}},"e":"Las 3D tienen profundidad.","tiempo":30}]}
EX5=[[1,MC("La forma de organizar los elementos en el espacio de una obra es la…",["Composición","Perspectiva","Textura","Paleta"],"Composición","Guía la mirada.")],
 [1,VF("Un equilibrio asimétrico compensa elementos distintos por peso y color.","Verdadero","No es parejo pero es equilibrado.")],
 [1,MC("El punto de interés es…",["La zona que más atrae la mirada","El fondo","El marco","La firma"],"La zona que más atrae la mirada","Se destaca con contraste o tamaño.")],
 [2,MC("El plano que muestra un detalle de cerca es el…",["Primer plano","Plano general","Plano medio","Plano de fondo"],"Primer plano","Ocupa casi todo el cuadro.")],
 [2,VF("El punto de vista contrapicado mira desde abajo.","Verdadero","Hace parecer grande al objeto.")],
 [2,MC("El recorte de la escena que decidimos mostrar es el…",["Encuadre","Ritmo","Contorno","Soporte"],"Encuadre","Elige qué entra y qué no.")],
 [3,MC("Un lugar abierto a todas las personas es un espacio…",["Público","Privado","Cerrado","Oculto"],"Público","Todos pueden usarlo.")],
 [3,VF("Una plaza es un espacio exterior.","Verdadero","Está al aire libre.")],
 [3,FB("Los colores y la luz crean la ___ de un espacio.",[["atmosfera","atmósfera"]],"Es la sensación del lugar.")],
 [4,MC("Una obra con alto, ancho y profundidad es…",["Tridimensional","Bidimensional","Plana","Lineal"],"Tridimensional","Tiene volumen.")],
 [4,VF("La planta muestra el espacio visto desde arriba.","Verdadero","Es un plano del lugar.")],
 [4,MC("Un modelo en tres dimensiones de un espacio es una…",["Maqueta","Planta","Vista","Paleta"],"Maqueta","Se arma a escala.")],
 [4,MS("¿Qué conviene al hacer una maqueta?",["Usar la misma escala","Medir las paredes","Probar y ajustar","Cambiar la escala en cada parte"],["Usar la misma escala","Medir las paredes","Probar y ajustar"],"La escala debe ser la misma.")]]
M5={"subject_id":SID,"tema":5,"practica":"Práctica general: componer el espacio","examen_titulo":"Nivel jefe: componer el espacio","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT5,"examen":EX5}
os.makedirs(os.path.join(AQUI,"mision-5"),exist_ok=True); json.dump(M5,open(os.path.join(AQUI,"mision-5","mision-5.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={1:"1c3e7d0f-d0ca-4124-a7cf-16b7dfcc6fd5",2:"5e653e4d-a451-4b16-9e41-006d915c2095",3:"3d7d3c5d-0faa-41a4-9a25-7607f35315af",4:"ba46ce18-6de9-410a-a125-21b1df4fae55"}
TIT={1:"Composición: equilibrio, ritmo y puntos de interés",2:"Planos, encuadres y puntos de vista",3:"Espacios para mirar: interiores, exteriores, públicos y privados",4:"Del plano al volumen: representar el espacio"}
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
 RET("¿Cómo se llama la forma de organizar los elementos en una obra?",6,"Composición","🧩","COMPONER EL ESPACIO","equilibrio, ritmo e interés",["Desafío: ¿cómo se llama la forma de organizar los elementos en una obra? Seis segundos.","Composición.","Hoy: *equilibrio, ritmo y puntos de interés*."]),
 DEF("Composición","Organizar los elementos del espacio","🧩",["La *composición* es la forma de organizar los elementos.","Guía la mirada."]),
 BQ("TRES CLAVES",[("EQUILIBRIO","Simétrico o asimétrico"),("RITMO","Repetición con movimiento"),("INTERÉS","Lo que atrae la mirada")],["Tres claves de la composición.","El *equilibrio*: simétrico o asimétrico.","El *ritmo*: repetición con movimiento.","Y el *interés*: lo que atrae la mirada."]),
 Q("Un buen punto de interés se ubica…",["En una intersección de tercios","Siempre en una esquina","Nunca importa"],0,["Te toca: el punto de interés.","¿En una intersección de tercios, en una esquina o nunca importa?","En una *intersección de tercios*."]),
 ER([("Todo en el centro","Usar los tercios"),("Destacar todo a la vez","Un protagonista")],["Errores típicos.","Poner *todo en el centro*.","Y querer *destacar todo* a la vez."]),
 RES(["Repasemos.","Componer es *organizar* el espacio.","El *equilibrio* puede ser simétrico o asimétrico.","El *ritmo* repite y da movimiento.","Y el *interés* atrae la mirada.","¡Clase terminada! Ahora, *a practicar*."],[["COMPOSICIÓN","organiza"],["EQUILIBRIO","simétrico o no"],["RITMO","repetición"],["INTERÉS","atrae la mirada"]])],
2:[
 NOT("ENCUADRE","El mismo objeto","Cambia según el plano","🎥","PLANOS Y ENCUADRES","puntos de vista",["Noticia: el mismo objeto cambia según el plano.","Y según desde dónde se mire.","Hoy: *planos, encuadres y puntos de vista*."]),
 ZO([("🏞️","Plano general: todo el lugar"),("🧍","Plano medio: de la cintura"),("👁️","Primer plano: el detalle")],["Tres planos, cada vez más cerca.","El *plano general* muestra todo el lugar.","El *plano medio*, de la cintura para arriba.","Y el *primer plano*, el detalle."]),
 CMP(("PICADO","Desde arriba: el objeto parece chico","⬇️"),("CONTRAPICADO","Desde abajo: parece grande","⬆️"),"vs",["Dos puntos de vista.","El *picado* mira desde arriba.","El *contrapicado* mira desde abajo."]),
 Q("El recorte de la escena que mostramos es el…",["Encuadre","Ritmo","Contorno"],0,["Te toca: el recorte de la escena.","¿Encuadre, ritmo o contorno?","El *encuadre*."]),
 ER([("Mismo plano siempre","Probar varios planos"),("El punto de vista no importa","Cambia el mensaje")],["Errores típicos.","Usar *siempre el mismo plano*.","Y creer que el *punto de vista* no importa."]),
 RES(["Repasemos.","Hay planos *general, medio y primer plano*.","El *encuadre* elige qué entra.","El punto de vista puede ser *picado o contrapicado*.","Y todo cambia el *mensaje*.","¡Clase terminada! Ahora, *a practicar*."],[["PLANOS","tres distancias"],["ENCUADRE","qué entra"],["PUNTO DE VISTA","arriba o abajo"],["MENSAJE","cambia con la elección"]])],
3:[
 CH(("Lu","👧"),[(False,"¿Dibujaste la plaza?"),(True,"Sí, un espacio exterior y público"),(False,"¿Y tu cuarto? ¿Interior y privado?")],"ESPACIOS","para mirar",["Un chat sobre espacios.","Lu pregunta si dibujaste la plaza.","Respondés que es exterior y público.","Y ella pregunta por tu cuarto: interior y privado."]),
 DEF("Espacio público","Abierto a todas las personas","🏞️",["Un *espacio público* está abierto a todas las personas.","Por ejemplo, una plaza."]),
 VE("PÚBLICO","PRIVADO",["Una plaza","Una biblioteca"],["Una casa","Un jardín propio"],["Se pueden dibujar"],["Dos tipos de espacio.","El *público*: una plaza o una biblioteca.","El *privado*: una casa o un jardín propio.","Y los dos se pueden *dibujar*."]),
 AD(("INTERIOR","🏠","Una habitación o un aula"),("EXTERIOR","🌳","Una plaza o una calle"),["Dos formas de espacio.","El *interior* es cubierto.","El *exterior* es al aire libre."]),
 Q("Un lugar abierto a todos es un espacio…",["Público","Privado","Oculto"],0,["Te toca: lugar abierto a todos.","¿Público, privado u oculto?","*Público*."]),
 ER([("Todo exterior es público","Un patio propio es privado"),("Dibujar todos los objetos","Elegir los importantes")],["Errores típicos.","Creer que *todo exterior es público*.","Y dibujar *todos los objetos*."]),
 RES(["Repasemos.","Hay espacios *interiores y exteriores*.","Y *públicos y privados*.","Se eligen los *elementos importantes*.","Y la *atmósfera* cuenta.","¡Clase terminada! Ahora, *a practicar*."],[["INTERIOR","cubierto"],["EXTERIOR","aire libre"],["PÚBLICO","para todos"],["ATMÓSFERA","luz y color"]])],
4:[
 RET("¿Cómo se llama la obra que tiene alto, ancho y profundidad?",6,"Tridimensional","📦","DEL PLANO AL VOLUMEN","representar el espacio",["Desafío: ¿cómo se llama la obra que tiene alto, ancho y profundidad? Seis segundos.","Tridimensional.","Hoy: *del plano al volumen*."]),
 DA("3","dimensiones","en una maqueta","Alto, ancho y profundidad","📦",["Un dato clave.","Una maqueta tiene *tres dimensiones*."]),
 LI("DEL PLANO A LA MAQUETA",[("1","Planta","📐"),("2","Medidas","📏"),("3","Maqueta","🏠")],["Del plano al volumen.","Primero, la *planta*.","Después, las *medidas*.","Y por último, la *maqueta*."]),
 PA("PARA ARMARLA",[("Cartón","📦"),("Pegamento","🧴"),("Regla","📏")],["Lo que necesitás.","*Cartón*.","*Pegamento*.","Y una *regla*."]),
 Q("Una maqueta es un modelo…",["Tridimensional","Solo plano","Solo escrito"],0,["Te toca: la maqueta.","¿Tridimensional, solo plano o solo escrito?","*Tridimensional*."]),
 RES(["Repasemos.","Lo *bidimensional* tiene alto y ancho.","Lo *tridimensional*, también profundidad.","La *planta* se ve desde arriba.","Y la *maqueta* se arma a escala.","¡Clase terminada! Ahora, *a practicar*."],[["2D","alto y ancho"],["3D","con profundidad"],["PLANTA","desde arriba"],["MAQUETA","a escala"]])]}
_N={'zoom':lambda e:len(e['niveles']),'antesdespues':lambda e:2,'linea':lambda e:len(e['eventos']),'flujo':lambda e:len(e['items'])}
for es in CLS.values():
    for e in es:
        if e['t'] in _N and len(e['voz'])==_N[e['t']](e)+1: e['voz']=[e['voz'][0]+' '+e['voz'][1]]+e['voz'][2:]
for n,es in CLS.items():
    json.dump({"slug":f"arte1-m5-n{n}","step_id":STEPS[n],"materia":"Arte y Comunicación I","titulo":TIT[n],"sub":f"Arte y Comunicación I · Misión 5 · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"arte1-m5-n{n}.json"),"w"),ensure_ascii=False)
print("ok")
