# -*- coding: utf-8 -*-
"""Arte y Comunicación I · Misión 2 (Dibujar lo que vemos) · COMÚN. Genera mision-2.json y 4 clases."""
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
def img_esfera():
    fig, ax = plt.subplots(figsize=(6.2, 4.2)); ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis("off")
    ax.fill_between([0, 10], 0, 2.6, color="#e9e4ef", zorder=0)
    from matplotlib.patches import Ellipse
    ax.add_patch(Ellipse((6.9, 2.3), 4.4, 0.9, color="#6f6580", alpha=0.65, zorder=1))
    xs = np.linspace(-1, 1, 300); X, Y = np.meshgrid(xs, xs); R2 = X ** 2 + Y ** 2; m = R2 <= 1
    Z = np.sqrt(np.clip(1 - R2, 0, 1)); L = np.array([-0.5, 0.6, 0.62]); L = L / np.linalg.norm(L)
    I = np.clip(X * L[0] + Y * L[1] + Z * L[2], 0, 1); I = 0.14 + 0.86 * I
    I = I + 0.10 * np.clip((X * 0.5 - Y * 0.6 - 0.55) / 0.45, 0, 1) * (R2 > 0.55)
    img = np.ones((300, 300, 4)); g = np.clip(I, 0, 1); img[..., 0] = 0.30 + 0.62 * g; img[..., 1] = 0.22 + 0.60 * g; img[..., 2] = 0.45 + 0.50 * g; img[..., 3] = m
    ax.imshow(img, extent=(2.6, 6.6, 2.6, 6.6), origin="lower", zorder=2)
    kw = dict(arrowprops=dict(arrowstyle="->", color=O, lw=1.6), fontsize=11, color=O, fontweight="bold", zorder=5)
    ax.annotate("Luz", xy=(3.7, 6.0), xytext=(0.3, 6.5), **kw)
    ax.annotate("Sombra propia", xy=(5.8, 3.9), xytext=(7.0, 5.6), **kw)
    ax.annotate("Sombra proyectada", xy=(8.2, 2.3), xytext=(6.6, 0.5), **kw)
    ax.annotate("Luz reflejada", xy=(5.5, 3.05), xytext=(1.0, 1.2), **kw)
    return png(fig)
def img_persp():
    fig, ax = plt.subplots(figsize=(6.4, 3.6)); ax.set_xlim(0, 1); ax.set_ylim(-0.1, 1); ax.axis("off")
    hz = 0.55; vp = (0.5, hz)
    ax.plot([0, 1], [hz, hz], color=V, lw=2.2); ax.plot(*vp, "o", color="#e8913a", ms=9, zorder=5)
    for x0 in (0.0, 1.0): ax.plot([x0, vp[0]], [0, vp[1]], color=O, lw=1.6, ls="--")
    for side, x0 in ((-1, 0.18), (1, 0.82)):
        for t in (0.05, 0.42, 0.68):
            px = x0 + (vp[0] - x0) * t; py = 0 + (hz - 0) * t; s = 0.22 * (1 - t); h = 1.3 * s
            ax.add_patch(plt.Rectangle((px - s / 2, py), s, h, fc=C, ec=V, lw=2, zorder=3))
            for cx, cy in ((px - s / 2, py + h), (px + s / 2, py + h)): ax.plot([cx, vp[0]], [cy, vp[1]], color=V, lw=0.8, ls=":")
    ax.annotate("Línea de horizonte", xy=(0.88, hz), xytext=(0.66, 0.9), arrowprops=dict(arrowstyle="->", color=O, lw=1.5), fontsize=11, color=O, fontweight="bold")
    ax.annotate("Punto de fuga", xy=vp, xytext=(0.3, 0.9), arrowprops=dict(arrowstyle="->", color=O, lw=1.5), fontsize=11, color=O, fontweight="bold")
    return png(fig)
B1=NV("Vas a dibujar un objeto observándolo, yendo de la forma general al detalle.",["Dibujar mirando","De lo general a lo particular","Medir con la mirada","Contorno y detalle"],[
 S(1,"Dibujar mirando",[D("Dibujo de observación","Dibujo hecho mirando un objeto real, para representarlo tal como se ve y no como se imagina."),P("Los símbolos que dibujamos de memoria, como un sol con rayos o una casa de techo triangular, nos engañan. Al observar, el dibujo se parece más al objeto real.")]),
 S(1,"De lo general a lo particular",[T("Pasos del dibujo de observación",["Paso","Qué se hace"],[["1. Encajar","Marcar con trazos suaves el tamaño y la posición total del objeto"],["2. Estructura","Dibujar las formas simples que lo componen"],["3. Contorno","Afinar el borde con líneas más firmes"],["4. Detalle","Sumar texturas y marcas pequeñas"]])]),
 S(2,"Medir con la mirada",[P("Se pueden comparar tamaños con el lápiz extendido: se cierra un ojo, se toma una medida del objeto y se la compara con otras partes. Así se controla la proporción sin usar regla."),IM("Trazo suave primero","Los trazos de encaje son suaves para poder corregir.")]),
 S(2,"Contorno y detalle",[T("Dos tipos de línea",["Línea","Para qué sirve"],[["Contorno","Marca el borde del objeto"],["Detalle","Muestra texturas, marcas y relieves"]]),P("Un contorno de grosor variable, más grueso donde hay sombra o donde el objeto está más cerca, da sensación de volumen.")])],
 {"titulo":"dibujar","planteo":"Vas a dibujar una taza. ¿Cómo se aplican los cuatro pasos?","pasos":["Encajar: un rectángulo suave que cubre toda la taza.","Estructura: un cilindro y un óvalo arriba para la boca.","Contorno: afinar el borde y agregar el asa.","Detalle: marcar el brillo y las manchas."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Dibujar mirando un objeto real es un dibujo de ___ .","Los trazos del primer paso, para poder corregir, son ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un objeto pequeño y dibujalo siguiendo los cuatro pasos. Escribí qué paso te costó más."},
 {"titulo":"Dibujá lo que ves","texto":"Dibujá lo que ves y no lo que creés que es: mirá más tiempo el objeto que la hoja."},
 ["Empezar por los detalles antes de encajar el objeto.","Dibujar de memoria en vez de mirar."],
 RS(("Observación","Dibujar mirando."),("Pasos","Encajar, estructura, contorno, detalle."),("Medir","Con el lápiz extendido."),("Trazo","Suave al principio.")),
 G(("Encaje","Primer esquema general del objeto."),("Estructura","Formas simples que componen algo."),("Contorno","Borde del objeto."),("Proporción","Relación de tamaños.")),
 ["¿Cómo se llama el dibujo hecho mirando un objeto real?","¿Cómo se llama el primer paso, en el que se marca el tamaño total del objeto?","¿Conviene empezar por los detalles? Respondé sí o no.","¿Conviene que los trazos de encaje sean suaves? Respondé sí o no."],
 [["dibujo de observacion","dibujo de observación","observacion","observación"],["encaje","encajar","el encaje"],["no"],["si","sí"]],
 {"incompleto":"Observación. Suaves.","solo":"Dibujé un vaso: encajé un rectángulo, marqué un cilindro, afiné el borde y sumé el brillo. Me costó más la estructura.","carpeta":["Dibujo de observación.","Encaje.","No.","Sí."]})
B2=NV("Vas a representar el volumen de un objeto con luz y sombra.",["La fuente de luz","Partes de la sombra","Claroscuro y volumen","Valores"],[
 S(1,"La fuente de luz",[D("Fuente de luz","Lugar de donde viene la luz; define qué zonas se iluminan y cuáles quedan en sombra."),P("Antes de sombrear hay que decidir de dónde viene la luz y mantenerla igual en todo el dibujo.")]),
 S(1,"Partes de la sombra",[T("Zonas de un objeto iluminado",["Zona","Qué es"],[["Luz","Zona más clara, la que mira a la fuente"],["Sombra propia","Zona del objeto que no recibe luz"],["Sombra proyectada","Sombra que el objeto deja sobre el piso"],["Luz reflejada","Brillo suave dentro de la sombra"]])]),
 S(2,"Claroscuro y volumen",[D("Claroscuro","Contraste entre zonas claras y oscuras que da sensación de volumen."),P("Un círculo plano se convierte en una esfera cuando se le agrega un degradé de luz a sombra."),IMG("Las zonas de la luz y la sombra","Una esfera iluminada desde arriba a la izquierda.","Una esfera sombreada, con la luz llegando desde arriba a la izquierda. Se señalan la luz, la sombra propia en el lado opuesto, la sombra proyectada sobre el piso y un brillo suave de luz reflejada en el borde de la sombra.",img_esfera())]),
 S(2,"Valores",[P("Los valores son los distintos tonos de gris, del más claro al más oscuro. Se logran apretando más o menos el lápiz o superponiendo capas. Un buen dibujo usa una escala de valores amplia."),IM("Pasá de a poco","Oscurecé en capas: es más fácil oscurecer que aclarar.")])],
 {"titulo":"sombrear","planteo":"Vas a sombrear una esfera. ¿Cómo se ubican la luz y las sombras?","pasos":["Decidir que la luz viene de arriba a la izquierda.","La zona más clara va arriba a la izquierda.","La sombra propia va abajo a la derecha.","La sombra proyectada cae del lado opuesto a la luz."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El contraste entre zonas claras y oscuras que da volumen es el ___ .","La sombra que un objeto deja sobre el piso es la sombra ___ ."]},
 {"titulo":"tu turno","planteo":"Dibujá una esfera con una fuente de luz a tu elección y marcá la luz, la sombra propia y la sombra proyectada."},
 {"titulo":"Una sola luz","texto":"Elegí una única fuente de luz y no la cambies durante el dibujo."},
 ["Cambiar de lugar la fuente de luz a mitad del dibujo.","Dibujar la sombra proyectada del mismo lado que la luz."],
 RS(("Luz","Define zonas claras y oscuras."),("Sombras","Propia y proyectada."),("Claroscuro","Contraste que da volumen."),("Valores","Tonos de gris.")),
 G(("Volumen","Sensación de tres dimensiones."),("Claroscuro","Contraste de luz y sombra."),("Degradé","Paso gradual de claro a oscuro."),("Valor","Tono de claro a oscuro.")),
 ["¿Cómo se llama el contraste entre zonas claras y oscuras que da sensación de volumen?","¿Cómo se llama la sombra que el objeto deja sobre el piso?","¿La sombra proyectada cae del lado opuesto a la luz? Respondé sí o no.","¿Conviene cambiar de lugar la fuente de luz a mitad del dibujo? Respondé sí o no."],
 [["claroscuro","el claroscuro"],["sombra proyectada","proyectada","la sombra proyectada"],["si","sí"],["no"]],
 {"incompleto":"Claroscuro. Proyectada.","solo":"Luz arriba a la izquierda: zona clara arriba a la izquierda, sombra propia abajo a la derecha y sombra proyectada hacia la derecha sobre el piso.","carpeta":["Claroscuro.","Sombra proyectada.","Sí.","No."]})
B3=NV("Vas a comparar proporciones y dibujar objetos con perspectiva de un punto de fuga.",["Proporción","Medir y comparar","Perspectiva","Punto de fuga y horizonte"],[
 S(1,"Proporción",[D("Proporción","Relación de tamaño entre las partes de un objeto o entre varios objetos."),P("Por ejemplo, en un rostro los ojos están a la mitad de la altura de la cabeza. Conocer las proporciones ayuda a que un dibujo se vea creíble.")]),
 S(1,"Medir y comparar",[T("Cómo controlar proporciones",["Método","Cómo se hace"],[["Unidad de medida","Elegir una parte como unidad, por ejemplo el ancho de la cabeza"],["Comparar","Ver cuántas veces entra esa unidad en el resto"],["Alinear","Verificar con líneas imaginarias horizontales y verticales"]])]),
 S(2,"Perspectiva",[D("Perspectiva","Técnica para representar el espacio y la profundidad sobre una superficie plana."),P("Los objetos se ven más pequeños cuanto más lejos están, y las líneas paralelas parecen juntarse en el horizonte.")]),
 S(2,"Punto de fuga y horizonte",[T("Elementos de la perspectiva",["Elemento","Qué es"],[["Línea de horizonte","Línea a la altura de los ojos de quien mira"],["Punto de fuga","Punto del horizonte donde se juntan las líneas paralelas"],["Líneas de fuga","Líneas que van desde los objetos hasta el punto de fuga"]]),IMG("Perspectiva de un punto de fuga","Los objetos se achican hacia el punto de fuga.","Una calle vista de frente: una línea de horizonte, un punto de fuga en el centro y, a cada lado, tres cajas que se hacen más chicas al alejarse. Líneas punteadas unen sus bordes superiores con el punto de fuga.",img_persp())])],
 {"titulo":"dibujar","planteo":"Vas a dibujar una calle con perspectiva. ¿Cómo se arma?","pasos":["Trazar la línea de horizonte a la altura de los ojos.","Marcar el punto de fuga en el centro.","Dibujar las líneas de fuga de los bordes de la calle.","Poner las casas más pequeñas a medida que se alejan."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La relación de tamaño entre las partes de un objeto es la ___ .","El punto donde se juntan las líneas paralelas en el horizonte es el punto de ___ ."]},
 {"titulo":"tu turno","planteo":"Dibujá un pasillo o una calle con un punto de fuga y poné al menos tres objetos que se achiquen al alejarse."},
 {"titulo":"El horizonte a tus ojos","texto":"La línea de horizonte siempre está a la altura de tus ojos: si te agachás, baja."},
 ["Hacer que los objetos lejanos tengan el mismo tamaño que los cercanos.","Poner el punto de fuga fuera de la línea de horizonte."],
 RS(("Proporción","Relación de tamaños."),("Medir","Con una unidad."),("Perspectiva","Representa la profundidad."),("Fuga","Punto donde se juntan las líneas.")),
 G(("Proporción","Relación de tamaños."),("Horizonte","Línea a la altura de los ojos."),("Punto de fuga","Donde se juntan las paralelas."),("Profundidad","Sensación de distancia.")),
 ["¿Cómo se llama la relación de tamaño entre las partes de un objeto?","¿Cómo se llama el punto donde se juntan las líneas paralelas en el horizonte?","¿Los objetos más lejanos se ven más pequeños? Respondé sí o no.","¿La línea de horizonte está a la altura de los ojos de quien mira? Respondé sí o no."],
 [["proporcion","proporción","la proporcion","la proporción"],["punto de fuga","fuga","el punto de fuga"],["si","sí"],["si","sí"]],
 {"incompleto":"Proporción. Fuga.","solo":"Dibujé una calle con el punto de fuga al centro, casas que se achican al alejarse y tres postes cada vez más chicos.","carpeta":["Proporción.","Punto de fuga.","Sí.","Sí."]})
B4=NV("Vas a usar un cuaderno de artista para bocetar a diario y registrar tu mirada.",["Qué es un boceto","El cuaderno de artista","Bocetar rápido","Hábito y progreso"],[
 S(1,"Qué es un boceto",[D("Boceto","Dibujo rápido y sin terminar que sirve para captar una idea, una forma o un momento."),P("Un boceto no busca ser perfecto: busca registrar. Puede tener errores, tachaduras y notas al margen.")]),
 S(1,"El cuaderno de artista",[T("Para qué sirve",["Uso","Ejemplo"],[["Practicar","Dibujar objetos cotidianos"],["Registrar","Anotar ideas, colores y detalles"],["Experimentar","Probar materiales y técnicas"],["Ver el progreso","Comparar páginas viejas con nuevas"]])]),
 S(2,"Bocetar rápido",[T("Ejercicios cortos",["Ejercicio","Tiempo"],[["Gesto","30 segundos"],["Contorno ciego","1 minuto, sin mirar la hoja"],["Boceto con valores","5 minutos"]]),P("Limitar el tiempo ayuda a no perderse en los detalles y a captar lo esencial.")]),
 S(2,"Hábito y progreso",[P("Dibujar un poco todos los días enseña más que hacerlo mucho una vez por semana. Conviene fechar cada página y escribir una nota breve sobre lo que se observó."),IM("Diez minutos por día","La constancia mejora más que la inspiración.")])],
 {"titulo":"hábito","planteo":"Querés armar el hábito de bocetar. ¿Cómo se organiza?","pasos":["Elegir un cuaderno que se pueda llevar a todas partes.","Fijar diez minutos por día para bocetar.","Fechar cada página y anotar lo que se observó.","Cada semana, repasar las páginas y elegir una mejora."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un dibujo rápido y sin terminar que capta una idea es un ___ .","Conviene ___ cada página del cuaderno."]},
 {"titulo":"tu turno","planteo":"Hacé tres bocetos de objetos de tu casa, de 1, 5 y 10 minutos, y anotá la fecha y qué descubriste en cada uno."},
 {"titulo":"Sin borrar","texto":"En el cuaderno no se borra: se dibuja encima y se aprende del error."},
 ["Querer que cada boceto sea perfecto.","Dibujar solo cuando hay inspiración."],
 RS(("Boceto","Dibujo rápido."),("Cuaderno","Practicar y registrar."),("Tiempo","Ejercicios cortos."),("Hábito","Un poco cada día.")),
 G(("Boceto","Dibujo rápido sin terminar."),("Gesto","Boceto muy rápido de la postura."),("Contorno ciego","Dibujar sin mirar la hoja."),("Constancia","Hacer algo todos los días.")),
 ["¿Cómo se llama el dibujo rápido y sin terminar que capta una idea?","¿Cómo se llama el ejercicio de dibujar el contorno sin mirar la hoja?","¿Un boceto tiene que ser perfecto? Respondé sí o no.","¿Dibujar un poco todos los días ayuda a mejorar? Respondé sí o no."],
 [["boceto","el boceto"],["contorno ciego","el contorno ciego"],["no"],["si","sí"]],
 {"incompleto":"Boceto. Fechar.","solo":"1 minuto: una llave, solo el contorno. 5 minutos: una taza con sombras. 10 minutos: mis zapatillas con detalles. Las formas simples ayudan mucho.","carpeta":["Boceto.","Contorno ciego.","No.","Sí."]})
ACT2={"1":[{"t":"ordering","p":"Ordená los pasos del dibujo de observación.","o":["Detalle","Encajar","Contorno","Estructura"],"r":{"orden":["Encajar","Estructura","Contorno","Detalle"]},"e":"De lo general a lo particular."},MC("¿Para qué sirve medir con el lápiz extendido?",["Controlar las proporciones","Borrar errores","Dar color","Hacer sombras"],"Controlar las proporciones","Se compara el tamaño de las partes.")],
 "2":[{"t":"classify","p":"¿Qué zona es?","o":{"elementos":["Zona más clara","Zona del objeto sin luz","Sombra sobre el piso","Brillo suave en la sombra"],"categorias":["Luz","Sombra propia","Sombra proyectada","Luz reflejada"]},"r":{"categorias":{"Zona más clara":"Luz","Zona del objeto sin luz":"Sombra propia","Sombra sobre el piso":"Sombra proyectada","Brillo suave en la sombra":"Luz reflejada"}},"e":"Cada zona tiene su nombre."},VF("El claroscuro da sensación de volumen.","Verdadero","Contrasta zonas claras y oscuras.")],
 "3":[{"t":"matching","p":"Uní cada elemento con su definición.","o":{"izquierda":["Línea de horizonte","Punto de fuga","Líneas de fuga","Proporción"],"derecha":["A la altura de los ojos","Donde se juntan las paralelas","Van del objeto al punto de fuga","Relación de tamaños"]},"r":{"pares":{"Línea de horizonte":"A la altura de los ojos","Punto de fuga":"Donde se juntan las paralelas","Líneas de fuga":"Van del objeto al punto de fuga","Proporción":"Relación de tamaños"}},"e":"Cada elemento, su definición."},MS("¿Qué ocurre en perspectiva?",["Los objetos lejanos se ven más pequeños","Las paralelas parecen juntarse","Todos los objetos miden lo mismo","El horizonte está a la altura de los ojos"],["Los objetos lejanos se ven más pequeños","Las paralelas parecen juntarse","El horizonte está a la altura de los ojos"],"Los objetos no miden lo mismo según la distancia.")],
 "4":[FB("Un dibujo rápido y sin terminar es un ___ .",[["boceto"]],"Capta una idea."),TT("Tocá el tiempo diario sugerido: «Conviene dibujar diez minutos por día».",["Conviene","dibujar","diez","minutos","por","día."],[2,3],"Un poco todos los días.")],
 "5":[{"t":"matching","p":"Relámpago. Uní cada ejercicio con su tiempo.","o":{"izquierda":["Gesto","Contorno ciego","Boceto con valores"],"derecha":["30 segundos","1 minuto","5 minutos"]},"r":{"pares":{"Gesto":"30 segundos","Contorno ciego":"1 minuto","Boceto con valores":"5 minutos"}},"e":"Ejercicios cortos.","tiempo":35},
  VF("Relámpago. Los objetos lejanos se dibujan más grandes.","Falso","Se achican al alejarse.",tiempo=15),
  FB("Relámpago. El contraste de luz y sombra que da volumen es el ___ .",[["claroscuro"]],"Crea volumen.",tiempo=25),
  MC("Relámpago. La sombra que cae sobre el piso es la sombra…",["Proyectada","Propia","Reflejada"],"Proyectada","Cae fuera del objeto.",tiempo=15)]}
EX2=[[1,MC("Dibujar mirando un objeto real es un dibujo de…",["Observación","Memoria","Fantasía","Invención"],"Observación","Se representa lo que se ve.")],
 [1,VF("El primer paso es encajar el objeto con trazos suaves.","Verdadero","Permite corregir.")],
 [1,MS("¿Qué pasos forman el dibujo de observación?",["Encajar","Estructura","Contorno","Pintar con acuarela"],["Encajar","Estructura","Contorno"],"También el detalle; pintar no es un paso.")],
 [2,MC("El contraste entre zonas claras y oscuras que da volumen es el…",["Claroscuro","Degradé","Contorno","Horizonte"],"Claroscuro","Crea la sensación de volumen.")],
 [2,VF("La sombra proyectada cae del lado opuesto a la luz.","Verdadero","Se aleja de la fuente.")],
 [2,MC("La sombra propia es…",["La zona del objeto que no recibe luz","La que cae sobre el piso","El brillo suave","El fondo"],"La zona del objeto que no recibe luz","Está sobre el mismo objeto.")],
 [3,MC("El punto donde se juntan las líneas paralelas en el horizonte es el…",["Punto de fuga","Punto de luz","Contorno","Encaje"],"Punto de fuga","Es parte de la perspectiva.")],
 [3,VF("En perspectiva, los objetos más lejanos se dibujan más pequeños.","Verdadero","Así se logra profundidad.")],
 [3,FB("La relación de tamaño entre las partes de un objeto es la ___ .",[["proporcion","proporción"]],"Se controla midiendo.")],
 [4,MC("Un dibujo rápido y sin terminar que capta una idea es un…",["Boceto","Mural","Retrato final","Afiche"],"Boceto","No busca ser perfecto.")],
 [4,VF("Dibujar un poco todos los días ayuda más que hacerlo mucho una vez por semana.","Verdadero","La constancia mejora la práctica.")],
 [4,MC("El contorno ciego se dibuja…",["Sin mirar la hoja","Con regla","Solo con color","De memoria"],"Sin mirar la hoja","Entrena la observación.")],
 [4,MS("¿Para qué sirve el cuaderno de artista?",["Practicar","Registrar ideas","Experimentar","Entregarlo como examen"],["Practicar","Registrar ideas","Experimentar"],"Es un espacio de práctica, no un examen.")]]
M2={"subject_id":SID,"tema":2,"practica":"Práctica general: dibujar lo que vemos","examen_titulo":"Nivel jefe: dibujar lo que vemos","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT2,"examen":EX2}
os.makedirs(os.path.join(AQUI,"mision-2"),exist_ok=True); json.dump(M2,open(os.path.join(AQUI,"mision-2","mision-2.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={1:"0a3ba594-2b1a-41ba-b141-3b9c1fa5a692",2:"e3538802-9418-4394-87e2-68dc214a8a62",3:"9703d8d2-c8ed-4ac6-b324-a4dec1016b92",4:"c2ef1d7e-08f0-4b00-bf2f-af17d03809ed"}
TIT={1:"Dibujo de observación: del contorno al detalle",2:"Luz y sombra: claroscuro y volumen",3:"Proporción y perspectiva",4:"El cuaderno de artista: bocetar a diario"}
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
LI=lambda t,ev,v:{"t":"linea","titulo":t,"eventos":[{"fecha":a,"txt":b,"emoji":c} for a,b,c in ev],"voz":v}
VE=lambda a,b,ia,ib,am,v:{"t":"venn","a":a,"b":b,"itemsA":ia,"itemsB":ib,"ambos":am,"voz":v}
FL=lambda t,it,v:{"t":"flujo","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
MAT=lambda t,c,v:{"t":"matriz","titulo":t,"celdas":[{"cab":a,"txt":b} for a,b in c],"voz":v}
CIC=lambda t,it,v:{"t":"ciclo","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
ZO=lambda it,v:{"t":"zoom","niveles":[{"emoji":a,"txt":b} for a,b in it],"voz":v}
BAR=lambda t,u,it,v:{"t":"barras","titulo":t,"unidad":u,"items":[{"txt":a,"valor":b} for a,b in it],"voz":v}
BA=lambda i,d,g,v:{"t":"balanza","izq":{"cab":i[0],"items":i[1]},"der":{"cab":d[0],"items":d[1]},"gana":g,"voz":v}
CLS={1:[
 RET("¿Cómo se llama el dibujo hecho mirando un objeto real?",6,"Dibujo de observación","✏️","DIBUJAR LO QUE VEMOS","del contorno al detalle",["Desafío: ¿cómo se llama el dibujo hecho mirando un objeto real? Seis segundos.","Dibujo de observación.","Hoy: *del contorno al detalle*."]),
 DEF("Dibujo de observación","Dibujar mirando un objeto real","👁️",["El *dibujo de observación* se hace mirando un objeto real.","Se dibuja lo que se ve, no lo que se imagina."]),
 FL("LOS CUATRO PASOS",[("Encajar","📦"),("Estructura","🧱"),("Contorno","✒️"),("Detalle","🔎")],["Cuatro pasos, de lo general a lo particular.","*Encajar*: el tamaño total.","*Estructura*: formas simples.","*Contorno*: el borde.","Y *detalle*: texturas."]),
 DEF("Lápiz extendido","Para comparar medidas","📏",["Con el *lápiz extendido* se comparan medidas.","Así se controla la proporción."]),
 AD(("ENCAJAR","🪶","Trazo suave, se corrige"),("CONTORNO","✒️","Trazo firme, queda"),["El trazo cambia.","Al *encajar*, es suave y se corrige.","Al hacer el *contorno*, es firme y queda."]),
 Q("El primer paso del dibujo de observación es…",["Encajar","Detallar","Pintar"],0,["Te toca: el primer paso.","¿Encajar, detallar o pintar?","*Encajar*."]),
 ER([("Empezar por el detalle","Empezar por el encaje"),("Dibujar de memoria","Mirar el objeto")],["Errores típicos.","Empezar por el *detalle*.","Y dibujar *de memoria*."]),
 RES(["Repasemos.","Se dibuja *mirando*.","Se va de lo *general* a lo particular.","Se mide con el *lápiz extendido*.","Y el trazo empieza *suave*.","¡Clase terminada! Ahora, *a practicar*."],[["OBSERVAR","dibujar mirando"],["PASOS","encajar a detalle"],["MEDIR","lápiz extendido"],["TRAZO","suave al inicio"]])],
2:[
 NOT("DIBUJO","Un círculo plano","Se vuelve una esfera","⚪","LUZ Y SOMBRA","claroscuro y volumen",["Noticia: un círculo plano se vuelve una esfera.","Con luz y sombra.","Hoy: *luz y sombra, claroscuro y volumen*."]),
 CAU(("Fuente de luz","💡"),[("Zonas claras","⚪"),("Sombras","⬛")],["Todo empieza en la *fuente de luz*.","De ella salen las *zonas claras*.","Y también las *sombras*."]),
 MAT("ZONAS",[("LUZ","La más clara"),("SOMBRA PROPIA","En el objeto"),("SOMBRA PROYECTADA","Sobre el piso"),("LUZ REFLEJADA","Brillo en la sombra")],["Las zonas de un objeto iluminado.","La *luz*: la más clara.","La *sombra propia*: en el objeto.","La *proyectada*: sobre el piso.","Y la *luz reflejada*."]),
 DEF("Claroscuro","Contraste de claro y oscuro","🌗",["El *claroscuro* es el contraste entre claro y oscuro.","Da sensación de volumen."]),
 CL([("EN EL OBJETO","⚪"),("SOBRE EL PISO","⬛")],[("Sombra propia",0),("Sombra proyectada",1),("Luz reflejada",0),("Mancha al lado",1)],["¿En el objeto o sobre el piso?","*Sombra propia* y *luz reflejada*: en el objeto.","*Sombra proyectada*: sobre el piso."]),
 Q("La sombra proyectada cae…",["Opuesta a la luz","Hacia la luz","Siempre arriba"],0,["Te toca: la sombra proyectada.","¿Opuesta a la luz, hacia la luz o arriba?","*Opuesta a la luz*."]),
 ER([("Cambiar la luz a mitad del dibujo","Mantener una sola luz"),("Sombra del lado de la luz","Del lado opuesto")],["Errores típicos.","*Cambiar la luz* a mitad del dibujo.","Y poner la sombra *del lado de la luz*."]),
 RES(["Repasemos.","Primero se elige la *luz*.","Hay sombra *propia* y *proyectada*.","El *claroscuro* da volumen.","Y se oscurece *en capas*.","¡Clase terminada! Ahora, *a practicar*."],[["LUZ","una sola fuente"],["SOMBRAS","propia y proyectada"],["CLAROSCURO","da volumen"],["VALORES","en capas"]])],
3:[
 RET("¿Cómo se llama el punto donde se juntan las paralelas en el horizonte?",6,"Punto de fuga","🛣️","PROPORCIÓN","y perspectiva",["Desafío: ¿cómo se llama el punto donde se juntan las líneas paralelas en el horizonte? Seis segundos.","Punto de fuga.","Hoy: *proporción y perspectiva*."]),
 DEF("Proporción","Relación entre tamaños","⚖️",["La *proporción* es la relación entre tamaños.","Se controla midiendo y comparando."]),
 ZO([("🏠","Casa cerca: grande"),("🏘️","Casas lejos: chicas"),("⛰️","Montañas: diminutas")],["La *perspectiva* representa la profundidad.","Lo cercano se ve *grande*.","Lo lejano, *chico*.","Y lo más lejano, *diminuto*."]),
 BQ("ELEMENTOS",[("HORIZONTE","A la altura de los ojos"),("PUNTO DE FUGA","Donde se juntan las paralelas"),("LÍNEAS DE FUGA","Hacia el punto de fuga")],["Elementos de la perspectiva.","El *horizonte*: a la altura de los ojos.","El *punto de fuga*: donde se juntan las paralelas.","Y las *líneas de fuga*."]),
 CL([("CERCA","🔍"),("LEJOS","🔭")],[("Se ve grande",0),("Se ve pequeño",1),("Más detalle",0),("Menos detalle",1)],["¿Cerca o lejos?","*Se ve grande* y *más detalle*: cerca.","*Se ve pequeño* y *menos detalle*: lejos."]),
 Q("La línea de horizonte está a la altura de…",["Los ojos","Los pies","El techo"],0,["Te toca: el horizonte.","¿Los ojos, los pies o el techo?","La altura de los *ojos*."]),
 ER([("Objetos lejanos del mismo tamaño","Más pequeños al alejarse"),("Punto de fuga fuera del horizonte","En el horizonte")],["Errores típicos.","Dibujar objetos *lejanos* del mismo tamaño.","Y poner el *punto de fuga* fuera del horizonte."]),
 RES(["Repasemos.","La *proporción* compara tamaños.","La *perspectiva* da profundidad.","El *punto de fuga* está en el horizonte.","Y lo lejano *se achica*.","¡Clase terminada! Ahora, *a practicar*."],[["PROPORCIÓN","comparar tamaños"],["PERSPECTIVA","profundidad"],["FUGA","en el horizonte"],["LEJOS","más pequeño"]])],
4:[
 NOT("CUADERNO","Diez minutos por día","Mejoran más que una vez por semana","📓","EL CUADERNO","de artista",["Noticia: diez minutos por día mejoran más que una vez por semana.","Con un cuaderno.","Hoy: *el cuaderno de artista*."]),
 DEF("Boceto","Dibujo rápido sin terminar","✏️",["Un *boceto* es un dibujo rápido y sin terminar.","Capta una idea o un momento."]),
 BAR("TIEMPO DE CADA EJERCICIO","min",[("Gesto",0.5),("Contorno ciego",1),("Con valores",5)],["Ejercicios cortos.","El *gesto*: treinta segundos.","El *contorno ciego*: un minuto.","Y el boceto *con valores*: cinco minutos."]),
 DEF("Contorno ciego","Dibujar sin mirar la hoja","🙈",["El *contorno ciego* se dibuja sin mirar la hoja.","Entrena la observación."]),
 BA(("AYUDA",["Dibujar a diario","Fechar páginas"]),("NO AYUDA",["Querer perfección"]),"izq",["¿Qué ayuda al cuaderno?","*Dibujar a diario* y *fechar páginas* ayudan.","*Querer perfección* no ayuda."]),
 Q("Un boceto…",["No busca ser perfecto","Debe ser perfecto","No se fecha"],0,["Te toca: un boceto.","¿No busca ser perfecto, debe ser perfecto o no se fecha?","*No busca ser perfecto*."]),
 RES(["Repasemos.","El *boceto* es rápido.","El *cuaderno* sirve para practicar.","Los ejercicios son *cortos*.","Y la *constancia* mejora.","¡Clase terminada! Ahora, *a practicar*."],[["BOCETO","rápido"],["CUADERNO","practicar y registrar"],["TIEMPO","ejercicios cortos"],["HÁBITO","cada día"]])]}
for n,es in CLS.items():
    json.dump({"slug":f"arte1-m2-n{n}","step_id":STEPS[n],"materia":"Arte y Comunicación I","titulo":TIT[n],"sub":f"Arte y Comunicación I · Misión 2 · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"arte1-m2-n{n}.json"),"w"),ensure_ascii=False)
print("ok")
