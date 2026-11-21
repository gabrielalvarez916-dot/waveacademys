# -*- coding: utf-8 -*-
"""Arte y Comunicación I · Misión 1 (Aprender a mirar) · COMÚN. Genera mision-1.json y 4 clases."""
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
def img_ppl():
    fig, ax = plt.subplots(1, 3, figsize=(9, 3.2))
    rng = np.random.default_rng(3)
    x = rng.uniform(0.05, 0.95, 40); y = rng.uniform(0.05, 0.95, 40); s = rng.uniform(10, 260, 40)
    ax[0].scatter(x, y, s=s, color=V); ax[0].set_title("PUNTO", color=O, fontsize=12, fontweight="bold")
    t = np.linspace(0, 1, 100)
    ax[1].plot([0.05, 0.95], [0.9, 0.9], color=V, lw=3); ax[1].plot([0.1, 0.1], [0.1, 0.8], color=V, lw=3)
    ax[1].plot([0.25, 0.6], [0.1, 0.75], color=V, lw=3); ax[1].plot(0.65 + 0.3 * t, 0.45 + 0.25 * np.sin(t * 9), color=V, lw=3)
    ax[1].plot([0.3, 0.4, 0.5, 0.6, 0.7], [0.12, 0.3, 0.12, 0.3, 0.12], color=V, lw=3); ax[1].set_title("LÍNEA", color=O, fontsize=12, fontweight="bold")
    from matplotlib.patches import Rectangle, Circle
    ax[2].add_patch(Rectangle((0.08, 0.15), 0.55, 0.6, color="#6a3fa0", alpha=0.85)); ax[2].add_patch(Circle((0.62, 0.6), 0.28, color="#e8913a", alpha=0.75))
    ax[2].add_patch(Rectangle((0.45, 0.1), 0.45, 0.35, color="#3aa6a0", alpha=0.7)); ax[2].set_title("PLANO", color=O, fontsize=12, fontweight="bold")
    for a in ax: a.set_xlim(0, 1); a.set_ylim(0, 1); a.set_xticks([]); a.set_yticks([]); a.set_aspect("equal")
    return png(fig)
def img_rubin():
    pts = [(0.0,0.46),(0.08,0.40),(0.20,0.30),(0.30,0.27),(0.36,0.19),(0.42,0.27),(0.47,0.21),(0.52,0.25),(0.57,0.20),(0.62,0.25),(0.67,0.17),(0.72,0.13),(0.76,0.24),(0.83,0.27),(0.90,0.30),(1.0,0.36)]
    yy = np.linspace(0, 1, 400); w = np.interp(yy, [p[0] for p in pts], [p[1] for p in pts])
    w = np.convolve(np.pad(w, 6, mode="edge"), np.ones(13) / 13, mode="valid")[:400]
    fig, a = plt.subplots(figsize=(3.4, 3.8))
    a.fill_betweenx(yy, -1, -w, color=O); a.fill_betweenx(yy, w, 1, color=O); a.fill_betweenx(yy, -w, w, color="#f4e6c8")
    a.set_xlim(-0.8, 0.8); a.set_ylim(0, 1); a.set_xticks([]); a.set_yticks([])
    a.set_title("¿Un vaso o dos rostros?", color=O, fontsize=12, fontweight="bold")
    for sp in a.spines.values(): sp.set_color(O)
    return png(fig)
B1=NV("Vas a distinguir ver, observar y apreciar, y practicar una mirada atenta.",["Ver y observar","Apreciar","Tres niveles de la mirada","Entrenar la mirada"],[
 S(1,"Ver y observar",[D("Ver","Percibir con los ojos de manera automática, sin esfuerzo ni atención."),D("Observar","Mirar con atención y con un propósito: buscar detalles, relaciones y diferencias."),P("Pasamos el día viendo cientos de imágenes, pero observamos muy pocas. Aprender a mirar es pasar de ver a observar.")]),
 S(1,"Apreciar",[D("Apreciar","Valorar lo que se observa: reconocer qué lo hace interesante, bello, expresivo o significativo."),P("Apreciar no es solo decir si algo gusta o no: es poder explicar por qué nos llama la atención, y eso se aprende.")]),
 S(2,"Tres niveles de la mirada",[T("De ver a apreciar",["Nivel","Qué hacemos"],[["Ver","Percibir sin pensar, por ejemplo pasar frente a un mural"],["Observar","Buscar detalles, por ejemplo contar los colores y las formas del mural"],["Apreciar","Valorar y explicar qué transmite el mural y por qué"]])]),
 S(2,"Entrenar la mirada",[T("Ejercicios para observar",["Ejercicio","Cómo se hace"],[["Mirar despacio","Dedicar un minuto entero a un solo objeto"],["Preguntar","¿Qué forma, color y textura tiene?"],["Comparar","Buscar qué cambia entre dos objetos parecidos"],["Anotar","Escribir o dibujar lo que se descubre"]]),IM("Mirar es una práctica","Cuanto más se observa, más se descubre.")])],
 {"titulo":"observar","planteo":"Tenés una hoja de árbol en la mano. ¿Cómo pasás de verla a apreciarla?","pasos":["Ver: percibir que es una hoja verde.","Observar: notar su forma, sus nervaduras y sus bordes.","Apreciar: explicar qué la hace interesante, por ejemplo su simetría."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Mirar con atención y con un propósito es ___ .","Valorar lo que se observa y explicar por qué es ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un objeto y miralo durante un minuto. Escribí cinco detalles que antes no habías notado."},
 {"titulo":"Un minuto entero","texto":"Mirá un solo objeto durante un minuto completo: siempre aparece algo nuevo."},
 ["Pensar que ver y observar son lo mismo.","Creer que apreciar es solo decir si algo gusta."],
 RS(("Ver","Percibir sin atención."),("Observar","Mirar con propósito."),("Apreciar","Valorar y explicar."),("Entrenar","Mirar despacio y anotar.")),
 G(("Observar","Mirar con atención."),("Apreciar","Valorar y explicar por qué."),("Detalle","Parte pequeña que suma sentido."),("Textura","Cómo se ve o se siente una superficie.")),
 ["¿Cómo se llama mirar con atención y con un propósito?","¿Cómo se llama valorar lo que se observa y poder explicar por qué?","¿Ver es lo mismo que observar? Respondé sí o no.","¿Mirar un objeto durante un minuto entero ayuda a descubrir detalles? Respondé sí o no."],
 [["observar","observacion","observación"],["apreciar","apreciacion","apreciación"],["no"],["si","sí"]],
 {"incompleto":"Observar. Apreciar.","solo":"Una taza: el asa tiene una curva, hay una mancha en el borde, el esmalte brilla, la base es rugosa y las sombras son más azules.","carpeta":["Observar.","Apreciar.","No.","Sí."]})
B2=NV("Vas a reconocer el punto, la línea y el plano como elementos básicos del lenguaje visual y usarlos para describir imágenes.",["El punto","La línea","El plano","Los tres juntos"],[
 S(1,"El punto",[D("Punto","Marca mínima que ocupa un lugar en el espacio y atrae la mirada."),P("Un punto solo concentra la atención. Muchos puntos juntos forman texturas, sombras o imágenes enteras.")]),
 S(1,"La línea",[D("Línea","Recorrido de un punto en movimiento; une, separa y marca dirección."),T("Tipos de línea",["Tipo","Qué transmite"],[["Recta horizontal","Calma y estabilidad"],["Recta vertical","Firmeza y altura"],["Diagonal","Movimiento y tensión"],["Curva","Suavidad y fluidez"],["Quebrada","Inquietud y energía"]])]),
 S(2,"El plano",[D("Plano","Superficie de dos dimensiones que se forma cuando una línea se cierra o se extiende."),P("Los planos pueden ser de color, de textura o de luz. Al superponerse crean sensación de profundidad."),IMG("Punto, línea y plano","Los tres elementos básicos del lenguaje visual.","Tres recuadros: uno con puntos de distintos tamaños, otro con líneas rectas, curvas y quebradas, y otro con planos de color superpuestos.",img_ppl())]),
 S(2,"Los tres juntos",[P("En una imagen casi nunca aparecen aislados: el punto marca focos de atención, las líneas guían la mirada y los planos organizan el espacio. Para analizar una imagen se puede buscar dónde hay puntos, qué líneas la recorren y cuántos planos tiene.")])],
 {"titulo":"analizar","planteo":"Una imagen tiene un camino diagonal que baja hacia una casita pequeña, rodeada de campo. ¿Qué elementos hay y qué transmiten?","pasos":["La diagonal es una línea: marca dirección y movimiento.","La casita pequeña funciona como un punto de atención.","El campo que la rodea es un plano que organiza el espacio."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un recorrido que une, separa o marca dirección es una ___ .","La marca mínima que atrae la mirada es el ___ ."]},
 {"titulo":"tu turno","planteo":"Dibujá en tu carpeta tres cuadros pequeños: uno solo con puntos, otro solo con líneas y otro solo con planos de color."},
 {"titulo":"Uno por uno","texto":"Dibujá cada elemento por separado antes de combinarlos: así se entiende qué aporta cada uno."},
 ["Creer que una línea siempre es recta.","Pensar que un plano es solo una forma geométrica pintada."],
 RS(("Punto","Marca mínima que atrae."),("Línea","Une, separa y guía."),("Plano","Superficie de dos dimensiones."),("Juntos","Se combinan en toda imagen.")),
 G(("Punto","Marca mínima."),("Línea","Recorrido de un punto."),("Plano","Superficie."),("Profundidad","Sensación de distancia.")),
 ["¿Cómo se llama la marca mínima que atrae la mirada?","¿Cómo se llama el recorrido de un punto en movimiento?","¿La línea diagonal transmite movimiento? Respondé sí o no.","¿Los planos pueden superponerse y crear profundidad? Respondé sí o no."],
 [["punto","el punto"],["linea","línea","la linea","la línea"],["si","sí"],["si","sí"]],
 {"incompleto":"Línea. Punto.","solo":"Cuadro 1: puntos que forman una textura. Cuadro 2: líneas curvas y rectas. Cuadro 3: planos de color superpuestos.","carpeta":["Punto.","Línea.","Sí.","Sí."]})
B3=NV("Vas a distinguir forma y figura, y reconocer la relación entre figura y fondo en una imagen.",["Forma y figura","Fondo","Figura y fondo","Espacio positivo y negativo"],[
 S(1,"Forma y figura",[D("Forma","Aspecto exterior de algo: su contorno, sin importar qué represente."),D("Figura","Forma que reconocemos como algo concreto, por ejemplo una casa o un árbol."),T("Tipos de forma",["Tipo","Ejemplo"],[["Geométrica","Círculo, cuadrado, triángulo"],["Orgánica","Hoja, nube, mancha"],["Abstracta","Formas inventadas sin referencia real"]])]),
 S(1,"Fondo",[D("Fondo","Zona que rodea a la figura y la hace destacar."),P("Una figura se ve por contraste con su fondo: claro sobre oscuro, grande sobre pequeño, lleno sobre vacío.")]),
 S(2,"Figura y fondo",[P("El cerebro separa siempre lo que mira en figura y fondo. A veces se pueden invertir: en el dibujo de abajo se ve un vaso o dos rostros de perfil, según qué zona se tome como figura."),IMG("Figura y fondo","Una misma imagen, dos lecturas.","Una zona clara central con forma de vaso entre dos zonas oscuras que dibujan dos rostros de perfil enfrentados. Se puede leer como un vaso o como dos rostros.",img_rubin())]),
 S(2,"Espacio positivo y negativo",[T("Dos espacios",["Espacio","Qué es"],[["Positivo","El ocupado por la figura"],["Negativo","El espacio vacío que la rodea"]]),IM("Mirar el vacío","Dibujar el espacio negativo ayuda a lograr contornos más precisos.")])],
 {"titulo":"separar","planteo":"En un afiche hay una silueta negra sobre un cielo amarillo. ¿Qué es la figura y qué es el fondo?","pasos":["La silueta negra es la figura.","El cielo amarillo es el fondo.","El contraste de color hace que la figura se destaque."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La zona que rodea a la figura y la hace destacar es el ___ .","El espacio vacío que rodea a la figura es el espacio ___ ."]},
 {"titulo":"tu turno","planteo":"Poné un objeto frente a una pared y dibujá solo el espacio vacío que lo rodea, sin dibujar el objeto."},
 {"titulo":"Invertí la mirada","texto":"Si un dibujo te sale mal, probá a mirar y dibujar el fondo en lugar de la figura."},
 ["Pensar que el fondo no importa.","Creer que forma y figura son lo mismo."],
 RS(("Forma","Contorno."),("Figura","Forma reconocible."),("Fondo","Rodea y hace destacar."),("Espacios","Positivo y negativo.")),
 G(("Forma","Contorno de algo."),("Figura","Forma reconocible."),("Contraste","Diferencia que hace destacar."),("Silueta","Contorno oscuro de una figura.")),
 ["¿Cómo se llama la zona que rodea a la figura y la hace destacar?","¿Cómo se llama el espacio vacío que rodea a la figura?","¿Una hoja o una nube son formas orgánicas? Respondé sí o no.","¿Una figura se destaca por contraste con su fondo? Respondé sí o no."],
 [["fondo","el fondo"],["espacio negativo","negativo","el espacio negativo"],["si","sí"],["si","sí"]],
 {"incompleto":"Fondo. Negativo.","solo":"Dibujé las formas vacías entre el asa y el cuerpo de la taza, y entre la taza y la pared; la taza apareció sola.","carpeta":["Fondo.","Espacio negativo.","Sí.","Sí."]})
B4=NV("Vas a leer una obra siguiendo cuatro pasos: describir, analizar, interpretar y valorar.",["Describir","Analizar","Interpretar","Valorar"],[
 S(1,"Describir",[D("Describir","Decir qué se ve, sin opinar: personajes, objetos, colores, lugar."),P("La descripción es objetiva: cualquier persona debería reconocer lo que se dice. Empezar describiendo evita apurar interpretaciones.")]),
 S(1,"Analizar",[D("Analizar","Observar cómo está hecha la obra: elementos visuales, composición, técnica y materiales."),T("Qué analizar",["Aspecto","Pregunta"],[["Elementos","¿Qué puntos, líneas y planos hay?"],["Color","¿Qué colores dominan?"],["Composición","¿Cómo se ordena lo que se ve?"],["Técnica","¿Con qué materiales se hizo?"]])]),
 S(2,"Interpretar",[D("Interpretar","Proponer qué significa la obra o qué transmite, apoyándose en lo que se observó."),P("Puede haber varias interpretaciones válidas, siempre que se expliquen con pruebas visibles en la obra.")]),
 S(2,"Valorar",[P("Valorar es dar una opinión fundamentada: qué logra la obra, qué nos provoca y por qué. «Me gusta porque…» es mejor que «me gusta» a secas."),IM("Cuatro pasos","Describir, analizar, interpretar y valorar, siempre en ese orden.")])],
 {"titulo":"leer","planteo":"Una obra muestra una figura pequeña en un campo amplio, con colores fríos. ¿Cómo la leemos?","pasos":["Describir: hay una persona pequeña y un campo muy grande.","Analizar: los colores fríos y el espacio vacío dominan la imagen.","Interpretar: puede transmitir soledad o calma.","Valorar: logra emoción por el contraste entre la figura y el espacio."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Decir qué se ve, sin opinar, es ___ .","Proponer qué significa una obra es ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí una imagen que tengas a mano y escribí una frase para cada paso: describir, analizar, interpretar y valorar."},
 {"titulo":"Sin apuro","texto":"No saltes a interpretar: primero describí todo lo que ves."},
 ["Interpretar sin mirar bien la obra.","Decir solo «me gusta» sin explicar por qué."],
 RS(("Describir","Qué se ve."),("Analizar","Cómo está hecha."),("Interpretar","Qué significa."),("Valorar","Opinión fundamentada.")),
 G(("Composición","Cómo se ordenan los elementos."),("Técnica","Modo de hacer una obra."),("Interpretar","Proponer un significado."),("Fundamentar","Dar razones.")),
 ["¿Cómo se llama el paso de decir qué se ve, sin opinar?","¿Cómo se llama el paso de proponer qué significa la obra?","¿Una obra puede tener varias interpretaciones válidas? Respondé sí o no.","¿Conviene que una opinión esté fundamentada? Respondé sí o no."],
 [["describir","descripcion","descripción"],["interpretar","interpretacion","interpretación"],["si","sí"],["si","sí"]],
 {"incompleto":"Describir. Interpretar.","solo":"Describo: un puente rojo sobre un río. Analizo: la diagonal del puente guía la mirada. Interpreto: une dos orillas. Valoro: me atrae por el contraste de colores.","carpeta":["Describir.","Interpretar.","Sí.","Sí."]})
ACT1={"1":[{"t":"classify","p":"¿Ver, observar o apreciar?","o":{"elementos":["Pasar frente a un mural sin mirarlo","Contar los colores de un mural","Explicar por qué un mural emociona"],"categorias":["Ver","Observar","Apreciar"]},"r":{"categorias":{"Pasar frente a un mural sin mirarlo":"Ver","Contar los colores de un mural":"Observar","Explicar por qué un mural emociona":"Apreciar"}},"e":"Cada nivel pide más atención."},MS("¿Qué ayuda a entrenar la mirada?",["Mirar despacio","Preguntarse por forma y color","Mirar sin atención","Anotar lo que se descubre"],["Mirar despacio","Preguntarse por forma y color","Anotar lo que se descubre"],"Mirar sin atención no entrena.")],
 "2":[{"t":"matching","p":"Uní cada línea con lo que transmite.","o":{"izquierda":["Recta horizontal","Recta vertical","Diagonal","Curva"],"derecha":["Calma","Firmeza","Movimiento","Suavidad"]},"r":{"pares":{"Recta horizontal":"Calma","Recta vertical":"Firmeza","Diagonal":"Movimiento","Curva":"Suavidad"}},"e":"Cada línea comunica algo distinto."},FB("La marca mínima que atrae la mirada es el ___ .",[["punto"]],"Concentra la atención.")],
 "3":[TT("Tocá la figura: «La silueta negra se destaca sobre el cielo amarillo».",["La","silueta","negra","se","destaca","sobre","el","cielo","amarillo."],[1,2],"La silueta es la figura; el cielo, el fondo."),{"t":"classify","p":"¿Forma geométrica u orgánica?","o":{"elementos":["Círculo","Hoja","Cuadrado","Nube"],"categorias":["Geométrica","Orgánica"]},"r":{"categorias":{"Círculo":"Geométrica","Hoja":"Orgánica","Cuadrado":"Geométrica","Nube":"Orgánica"}},"e":"Las orgánicas vienen de la naturaleza."}],
 "4":[{"t":"ordering","p":"Ordená los pasos para leer una obra.","o":["Valorar","Describir","Interpretar","Analizar"],"r":{"orden":["Describir","Analizar","Interpretar","Valorar"]},"e":"Siempre en ese orden."},MC("Describir significa…",["Decir qué se ve, sin opinar","Decir qué significa","Dar una opinión","Elegir colores"],"Decir qué se ve, sin opinar","Es objetivo.")],
 "5":[{"t":"classify","p":"Relámpago. ¿Qué elemento es?","o":{"elementos":["Una marca mínima","Un trazo diagonal","Una superficie de color"],"categorias":["Punto","Línea","Plano"]},"r":{"categorias":{"Una marca mínima":"Punto","Un trazo diagonal":"Línea","Una superficie de color":"Plano"}},"e":"Los tres elementos básicos.","tiempo":35},
  VF("Relámpago. Observar es lo mismo que ver.","Falso","Observar lleva atención.",tiempo=15),
  FB("Relámpago. La zona que rodea a la figura es el ___ .",[["fondo"]],"Hace destacar la figura.",tiempo=25),
  MC("Relámpago. El primer paso para leer una obra es…",["Describir","Valorar","Interpretar"],"Describir","Se dice qué se ve.",tiempo=15)]}
EX1=[[1,MC("Mirar con atención y con un propósito es…",["Observar","Ver","Apreciar","Olvidar"],"Observar","Busca detalles.")],
 [1,VF("Ver y observar son exactamente lo mismo.","Falso","Observar lleva atención y propósito.")],
 [1,MS("¿Qué ayuda a entrenar la mirada?",["Mirar despacio","Preguntarse por forma y color","Mirar sin atención","Anotar lo que se descubre"],["Mirar despacio","Preguntarse por forma y color","Anotar lo que se descubre"],"Mirar sin atención no entrena.")],
 [2,MC("La marca mínima que atrae la mirada es…",["El punto","La línea","El plano","El fondo"],"El punto","Concentra la atención.")],
 [2,VF("La línea diagonal suele transmitir movimiento.","Verdadero","Genera tensión y dinamismo.")],
 [2,MC("Una superficie de dos dimensiones es…",["Un plano","Un punto","Una línea","Una textura"],"Un plano","Puede ser de color, textura o luz.")],
 [3,MC("La zona que rodea a la figura y la hace destacar es el…",["Fondo","Contorno","Plano","Detalle"],"Fondo","Se destaca por contraste.")],
 [3,FB("El espacio vacío que rodea a la figura es el espacio ___ .",[["negativo"]],"Dibujarlo ayuda a precisar contornos.")],
 [3,VF("Una hoja o una nube son formas orgánicas.","Verdadero","Las geométricas son círculo, cuadrado o triángulo.")],
 [4,MC("El primer paso para leer una obra es…",["Describir","Valorar","Interpretar","Analizar"],"Describir","Se dice qué se ve.")],
 [4,VF("Una obra puede tener varias interpretaciones válidas.","Verdadero","Si se fundamentan en lo que se ve.")],
 [4,MC("Valorar significa…",["Dar una opinión fundamentada","Contar cuántos colores hay","Copiar la obra","Describir sin opinar"],"Dar una opinión fundamentada","Con razones.")],
 [4,MS("¿Qué se analiza de una obra?",["Los elementos visuales","La composición","La técnica","El precio de venta"],["Los elementos visuales","La composición","La técnica"],"El precio no es parte del análisis visual.")]]
M1={"subject_id":SID,"tema":1,"practica":"Práctica general: aprender a mirar","examen_titulo":"Nivel jefe: aprender a mirar","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT1,"examen":EX1}
os.makedirs(os.path.join(AQUI,"mision-1"),exist_ok=True); json.dump(M1,open(os.path.join(AQUI,"mision-1","mision-1.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={1:"7d590c30-c66c-44a2-b6fb-6b7f3ffcf245",2:"94680619-a7e1-484d-bce1-085216c602fa",3:"8259e398-5296-47e7-b44d-f789ddcf2d17",4:"54adbab1-a61e-448d-9543-d20e8c9c4ffd"}
TIT={1:"La mirada: ver, observar y apreciar",2:"Punto, línea y plano",3:"Forma, figura y fondo",4:"Leer una obra paso a paso"}
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
 RET("¿Cómo se llama mirar con atención y con un propósito?",6,"Observar","👁️","APRENDER A MIRAR","ver, observar y apreciar",["Desafío: ¿cómo se llama mirar con atención y con un propósito? Seis segundos.","Observar.","Hoy: *ver, observar y apreciar*."]),
 DEF("Ver","Percibir sin atención","👀",["*Ver* es percibir con los ojos de manera automática.","No hace falta esfuerzo."]),
 DEF("Observar","Mirar con atención y propósito","🔍",["*Observar* es mirar con atención y con un propósito.","Se buscan detalles y diferencias."]),
 DEF("Apreciar","Valorar y explicar por qué","🎨",["*Apreciar* es valorar lo que se observa.","Y poder explicar por qué."]),
 CL([("VER","👀"),("OBSERVAR","🔍"),("APRECIAR","🎨")],[("Pasar sin mirar",0),("Contar colores",1),("Explicar la emoción",2),("Notar detalles",1)],["¿Ver, observar o apreciar?","*Pasar sin mirar*: ver.","*Contar colores* y *notar detalles*: observar.","*Explicar la emoción*: apreciar."]),
 Q("¿Qué ayuda a entrenar la mirada?",["Mirar despacio","Mirar sin atención","Mirar rápido"],0,["Te toca: ¿qué entrena la mirada?","¿Mirar despacio, sin atención o rápido?","*Mirar despacio*."]),
 ER([("Ver y observar son lo mismo","Observar lleva atención"),("Apreciar es que guste","Es valorar y explicar")],["Errores típicos.","Creer que *ver y observar* son lo mismo.","Y que *apreciar* es solo que guste."]),
 RES(["Repasemos.","*Ver* es automático.","*Observar* busca detalles.","*Apreciar* valora y explica.","Y la mirada *se entrena*.","¡Clase terminada! Ahora, *a practicar*."],[["VER","automático"],["OBSERVAR","con propósito"],["APRECIAR","valorar y explicar"],["ENTRENAR","mirar despacio"]])],
2:[
 NOT("ARTE","Un punto, una línea, un plano","Con tres elementos se arma una imagen","✏️","PUNTO, LÍNEA","y plano",["Noticia: con tres elementos se arma una imagen.","Un punto, una línea y un plano.","Hoy: *punto, línea y plano*."]),
 DEF("Punto","Marca mínima que atrae la mirada","⚫",["El *punto* es la marca mínima.","Atrae la mirada."]),
 DEF("Línea","Recorrido de un punto","📏",["La *línea* es el recorrido de un punto en movimiento.","Une, separa y marca dirección."]),
 TB("TIPOS DE LÍNEA",["Línea","Transmite"],[["Horizontal","Calma"],["Vertical","Firmeza"],["Diagonal","Movimiento"],["Curva","Suavidad"]],["Tipos de línea.","La *horizontal*: calma.","La *vertical*: firmeza.","La *diagonal*: movimiento.","Y la *curva*: suavidad."]),
 DEF("Plano","Superficie de dos dimensiones","🟪",["El *plano* es una superficie de dos dimensiones.","Al superponerse crea profundidad."]),
 CL([("PUNTO","⚫"),("LÍNEA","📏"),("PLANO","🟪")],[("Marca mínima",0),("Trazo diagonal",1),("Mancha de color",2),("Camino curvo",1)],["¿Punto, línea o plano?","*Marca mínima*: punto.","*Trazo diagonal* y *camino curvo*: líneas.","*Mancha de color*: plano."]),
 Q("¿Qué transmite la línea diagonal?",["Movimiento","Calma","Firmeza"],0,["Te toca: la línea diagonal.","¿Movimiento, calma o firmeza?","*Movimiento*."]),
 RES(["Repasemos.","El *punto* atrae la mirada.","La *línea* guía y marca dirección.","El *plano* organiza el espacio.","Y los tres *se combinan*.","¡Clase terminada! Ahora, *a practicar*."],[["PUNTO","atrae la mirada"],["LÍNEA","guía"],["PLANO","organiza"],["JUNTOS","forman imágenes"]])],
3:[
 RET("¿Cómo se llama la zona que rodea a la figura?",6,"Fondo","🖼️","FORMA, FIGURA","y fondo",["Desafío: ¿cómo se llama la zona que rodea a la figura? Seis segundos.","Fondo.","Hoy: *forma, figura y fondo*."]),
 DEF("Forma","Contorno de algo","🔷",["La *forma* es el contorno de algo.","Sin importar qué represente."]),
 DEF("Figura","Forma que reconocemos","🌳",["La *figura* es una forma que reconocemos.","Por ejemplo, una casa o un árbol."]),
 CMP(("FIGURA","Lo que se destaca","⬛"),("FONDO","Lo que la rodea","🟨"),"+",["Siempre van juntos.","La *figura* es lo que se destaca.","El *fondo* es lo que la rodea."]),
 CL([("GEOMÉTRICA","🔺"),("ORGÁNICA","🍃")],[("Círculo",0),("Hoja",1),("Cuadrado",0),("Nube",1)],["¿Geométrica u orgánica?","*Círculo* y *cuadrado*: geométricas.","*Hoja* y *nube*: orgánicas."]),
 Q("El espacio vacío que rodea a la figura es el espacio…",["Negativo","Positivo","Lleno"],0,["Te toca: el espacio vacío que rodea a la figura.","¿Negativo, positivo o lleno?","El espacio *negativo*."]),
 ER([("El fondo no importa","Hace destacar la figura"),("Forma y figura son iguales","La figura se reconoce")],["Errores típicos.","Creer que el *fondo no importa*.","Y confundir *forma* con *figura*."]),
 RES(["Repasemos.","La *forma* es el contorno.","La *figura* es reconocible.","El *fondo* la hace destacar.","Y el espacio *negativo* también cuenta.","¡Clase terminada! Ahora, *a practicar*."],[["FORMA","contorno"],["FIGURA","reconocible"],["FONDO","la hace destacar"],["NEGATIVO","espacio vacío"]])],
4:[
 NOT("ARTE","Una obra se puede leer","En cuatro pasos","🖼️","LEER UNA OBRA","paso a paso",["Noticia: una obra se puede leer.","En cuatro pasos.","Hoy: *leer una obra paso a paso*."]),
 PA("LOS CUATRO PASOS",[("Describir","📝"),("Analizar","🔍"),("Interpretar","💭"),("Valorar","⭐")],["Cuatro pasos.","*Describir*.","*Analizar*.","*Interpretar*.","Y *valorar*."]),
 DEF("Describir","Decir qué se ve, sin opinar","📝",["*Describir* es decir qué se ve.","Sin opinar."]),
 TB("QUÉ ANALIZAR",["Aspecto","Pregunta"],[["Elementos","Puntos, líneas, planos"],["Color","¿Cuáles dominan?"],["Composición","¿Cómo se ordena?"],["Técnica","¿Con qué se hizo?"]],["Qué se analiza.","Los *elementos*.","El *color*.","La *composición*.","Y la *técnica*."]),
 CL([("DESCRIBIR","📝"),("INTERPRETAR","💭")],[("Hay un puente rojo",0),("Une dos orillas",1),("Hay un río",0),("Transmite calma",1)],["¿Describir o interpretar?","*Hay un puente rojo* y *hay un río*: describir.","*Une dos orillas* y *transmite calma*: interpretar."]),
 Q("El primer paso para leer una obra es…",["Describir","Valorar","Interpretar"],0,["Te toca: el primer paso.","¿Describir, valorar o interpretar?","*Describir*."]),
 ER([("Interpretar sin mirar","Primero describir"),("Decir solo me gusta","Explicar por qué")],["Errores típicos.","*Interpretar* sin mirar bien.","Y decir solo *me gusta*."]),
 RES(["Repasemos.","Se *describe* lo que se ve.","Se *analiza* cómo está hecha.","Se *interpreta* qué significa.","Y se *valora* con razones.","¡Clase terminada! Ahora, *a practicar*."],[["DESCRIBIR","qué se ve"],["ANALIZAR","cómo está hecha"],["INTERPRETAR","qué significa"],["VALORAR","con razones"]])]}
for n,es in CLS.items():
    json.dump({"slug":f"arte1-m1-n{n}","step_id":STEPS[n],"materia":"Arte y Comunicación I","titulo":TIT[n],"sub":f"Arte y Comunicación I · Misión 1 · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"arte1-m1-n{n}.json"),"w"),ensure_ascii=False)
print("ok")
