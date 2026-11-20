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

def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]

from matplotlib.patches import Ellipse, Circle
import numpy as np
def fig_orbita():
    fig, ax = plt.subplots(figsize=(6.6, 3.0)); ax.axis("off"); ax.set_xlim(-7.5, 7.5); ax.set_ylim(-3.6, 3.4); ax.set_aspect("equal")
    ax.add_patch(Ellipse((0, 0), 12, 5, fill=False, ls="--", ec=O)); ax.add_patch(Circle((0, 0), .8, fc="#f4b63f"))
    for (x, y, t) in ((0, -2.5, "21/12: verano en el sur"), (6, 0, "21/3: otoño en el sur"), (0, 2.5, "21/6: invierno en el sur"), (-6, 0, "21/9: primavera en el sur")):
        ax.add_patch(Circle((x, y), .38, fc="#2f6fa8")); ax.text(x, y + (-.85 if y < 0 else .65 if y > 0 else -.85), t, ha="center", fontsize=8, color=O)
    ax.text(0, -.05, "Sol", ha="center", va="center", fontsize=8, color="#3a2a10")
    return png(fig)
def fig_grilla():
    fig, ax = plt.subplots(figsize=(4.6, 3.6)); ax.axis("off"); ax.set_xlim(-1.9, 1.9); ax.set_ylim(-1.3, 1.3); ax.set_aspect("equal")
    ax.add_patch(Circle((0, 0), 1, fc="#d9ecfa", ec=O))
    for la in (-60, -30, 30, 60): y = np.sin(np.radians(la)); h = np.cos(np.radians(la)); ax.plot([-h, h], [y, y], color="#7aa8c9", lw=.7)
    for lo in (30, 60): ax.add_patch(Ellipse((0, 0), 2*np.sin(np.radians(lo)), 2, fill=False, ec="#7aa8c9", lw=.7))
    ax.plot([-1, 1], [0, 0], color="#c0392b", lw=2); ax.plot([0, 0], [-1, 1], color="#e08e0b", lw=2)
    yb = np.sin(np.radians(-34)); xb = -np.cos(np.radians(-34)) * np.sin(np.radians(58)); ax.plot(xb, yb, "o", color=V, ms=7)
    ax.text(1.05, 0, "Ecuador 0°", fontsize=8, color="#c0392b", va="center"); ax.text(0.05, 1.08, "Greenwich 0°", fontsize=8, color="#e08e0b"); ax.text(-1.85, yb - .15, "Buenos Aires\n34° S, 58° O", fontsize=7.5, color=V)
    ax.text(1.05, .6, "Hemisferio\nnorte", fontsize=7.5, color=O); ax.text(1.05, -.75, "Hemisferio\nsur", fontsize=7.5, color=O)
    return png(fig)
N1=NV("Vas a explicar el día, la noche y las estaciones con los movimientos de la Tierra.",["Rotación","Traslación","El eje inclinado","Las estaciones"],[
 S(1,"Dos movimientos",[T("Movimientos de la Tierra",["Movimiento","Qué es","Duración","Consecuencia"],[["Rotación","Gira sobre su eje","24 horas","Día y noche"],["Traslación","Gira alrededor del Sol","365 días y casi 6 horas","Estaciones (con el eje inclinado) y año bisiesto"]])]),
 S(1,"Las estaciones",[P("El eje de la Tierra está <b>inclinado unos 23,5°</b>. Mientras la Tierra se traslada, cada hemisferio recibe los rayos del Sol más directos en distintos momentos: por eso hay estaciones, y son <b>opuestas</b> en el norte y en el sur."),IMG("Las estaciones en el hemisferio sur","La Tierra en cuatro momentos de su órbita.","El Sol en el centro y la Tierra en cuatro posiciones con las fechas de inicio de cada estación en el sur.",fig_orbita())]),
 S(2,"Un error muy común",[P("En verano la Tierra <b>no</b> está más cerca del Sol. Si la causa fuera la distancia, sería verano en todo el planeta al mismo tiempo; en cambio, cuando en Argentina es verano, en España es invierno.")])],
 {"titulo":"explicar","planteo":"¿Por qué en Navidad hace calor en Argentina y frío en Europa?","pasos":["Navidad es a fin de año.","En esa época el hemisferio sur recibe los rayos más directos del Sol.","Por eso es verano en Argentina e invierno en Europa, en el hemisferio norte.","La causa es la inclinación del eje, no la distancia al Sol."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El día y la noche se producen por la ___ .","Una vuelta completa alrededor del Sol dura unos ___ días."]},
 {"titulo":"tu turno","planteo":"Explicá con tus palabras por qué un año bisiesto tiene un día más."},
 {"titulo":"Opuestas","texto":"Siempre que te pregunten por la estación del otro hemisferio, pensá en la opuesta: verano ↔ invierno, otoño ↔ primavera."},
 ["Creer que el verano se debe a la cercanía al Sol.","Confundir rotación con traslación."],
 RS(("Rotación","24 h: día y noche."),("Traslación","Un año."),("Eje","Inclinado: estaciones."),("Hemisferios","Estaciones opuestas.")),
 G(("Eje terrestre","Línea imaginaria sobre la que gira la Tierra."),("Hemisferio","Mitad de la Tierra."),("Año bisiesto","Año de 366 días, cada cuatro años.")),
 ["¿Qué movimiento produce el día y la noche?","¿Qué estación empieza en el hemisferio sur hacia el 21 de diciembre?","Cuando en Argentina es invierno, ¿qué estación es en España?","¿Las estaciones se deben a la distancia al Sol? Respondé sí o no."],
 [["rotacion","rotación","la rotación"],["verano","el verano"],["verano","el verano"],["no"]],
 {"incompleto":"Rotación. 365.","solo":"Porque cada año sobran casi 6 horas; en cuatro años suman un día.","carpeta":["La rotación.","El verano.","Verano.","No."]})
N2=NV("Vas a ubicar lugares en el planeta con latitud y longitud.",["Paralelos y meridianos","Latitud y longitud","Los hemisferios","Coordenadas de un lugar"],[
 S(1,"La red de coordenadas",[IMG("Paralelos y meridianos","El Ecuador y Greenwich son las líneas cero.","Globo con paralelos, meridianos, el Ecuador, el meridiano de Greenwich y Buenos Aires marcado.",fig_grilla()),
  T("Las líneas",["Línea","Recorrido","Línea cero"],[["Paralelo","De este a oeste","Ecuador"],["Meridiano","De polo a polo","Greenwich"]])]),
 S(1,"Latitud y longitud",[T("Coordenadas",["Coordenada","Distancia a…","Valores"],[["Latitud","El Ecuador","0° a 90°, norte (N) o sur (S)"],["Longitud","El meridiano de Greenwich","0° a 180°, este (E) u oeste (O)"]])]),
 S(2,"Coordenadas de un lugar",[E("Buenos Aires","¿Dónde está?",["Está al sur del Ecuador: latitud sur.","Está al oeste de Greenwich: longitud oeste.","Coordenadas aproximadas: 34° S, 58° O.","En el GPS aparecen con signo menos: −34, −58."])])],
 {"titulo":"leer coordenadas","planteo":"Un lugar tiene 0° de latitud y 78° O de longitud. ¿Qué podés decir?","pasos":["Latitud 0°: está sobre el Ecuador.","Longitud oeste: está en el hemisferio oeste, como América.","Es Quito, la capital de Ecuador."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El paralelo 0° se llama ___ .","Argentina está en los hemisferios sur y ___ ."]},
 {"titulo":"tu turno","planteo":"Buscá en un mapa o en un celular las coordenadas de tu ciudad y escribilas con N/S y E/O."},
 {"titulo":"Primero la latitud","texto":"Las coordenadas se dicen en orden: primero latitud (N o S), después longitud (E u O)."},
 ["Dar coordenadas sin N, S, E u O.","Confundir paralelos con meridianos."],
 RS(("Ecuador","Latitud 0°."),("Greenwich","Longitud 0°."),("Latitud","Norte o sur."),("Longitud","Este u oeste.")),
 G(("Paralelo","Línea imaginaria de este a oeste."),("Meridiano","Línea imaginaria de polo a polo."),("Coordenadas","Latitud y longitud de un punto.")),
 ["¿Cómo se llama el paralelo 0°?","¿Cómo se llama el meridiano 0°?","Argentina está en el hemisferio norte o sur?","¿Qué coordenada indica la distancia al Ecuador: latitud o longitud?"],
 [["ecuador","el ecuador"],["greenwich","meridiano de greenwich","el meridiano de greenwich"],["sur"],["latitud","la latitud"]],
 {"incompleto":"Ecuador. Oeste.","solo":"Respuesta personal con N/S y E/O.","carpeta":["Ecuador.","Meridiano de Greenwich.","Sur.","Latitud."]})
N3=NV("Vas a calcular la hora en otros lugares del mundo usando los husos horarios.",["Qué es un huso horario","Al este y al oeste","Calcular la hora","La línea de cambio de fecha"],[
 S(1,"Los husos horarios",[D("Huso horario","Cada una de las 24 franjas de 15° de longitud en las que se divide la Tierra, con la misma hora."),P("360° ÷ 24 horas = 15° por hora. Hacia el <b>este</b> la hora se adelanta; hacia el <b>oeste</b>, se atrasa. Argentina está en el huso <b>UTC −3</b>.")]),
 S(1,"Calcular",[T("Si en Buenos Aires son las 12",["Ciudad","Huso","Hora"],[["Buenos Aires","UTC −3","12 h"],["Londres","UTC 0","15 h"],["Madrid","UTC +1","16 h"],["Tokio","UTC +9","0 h del día siguiente"],["Los Ángeles","UTC −8","7 h"]]),P("Algunos países usan horario de verano y adelantan una hora parte del año; en los ejemplos no se tiene en cuenta.")]),
 S(2,"Cambio de fecha",[P("Sobre el meridiano 180° está la <b>línea internacional de cambio de fecha</b>: al cruzarla hacia el oeste se suma un día, y hacia el este se resta.")])],
 {"titulo":"calcular","planteo":"En Buenos Aires (UTC −3) son las 20. ¿Qué hora es en Madrid (UTC +1)?","pasos":["Diferencia de husos: de −3 a +1 hay 4.","Madrid está al este: se suman 4 horas.","20 + 4 = 24: medianoche, ya del día siguiente."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Cada huso horario mide ___ grados.","Hacia el oeste, la hora se ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un país que te interese, averiguá su huso y calculá qué hora es allá cuando en Argentina son las 18."},
 {"titulo":"Contá los husos","texto":"Restá los números de los husos: la diferencia es la cantidad de horas. Al este se suman; al oeste se restan."},
 ["Restar cuando el lugar está al este.","Olvidar que puede cambiar el día."],
 RS(("24 husos","De 15° cada uno."),("Al este","Se adelanta."),("Al oeste","Se atrasa."),("Argentina","UTC −3.")),
 G(("Huso horario","Franja de la Tierra con la misma hora."),("UTC","Hora de referencia mundial."),("Línea de cambio de fecha","Meridiano 180°, donde cambia el día.")),
 ["¿En cuántos husos horarios se divide la Tierra?","¿Cuántos grados mide cada huso?","En Buenos Aires son las 10. ¿Qué hora es en Londres (UTC 0)? Respondé solo el número.","Hacia el este, la hora ¿se adelanta o se atrasa?"],
 [["24"],["15","15°"],["13","13 h","13hs"],["se adelanta","adelanta"]],
 {"incompleto":"15. Atrasa.","solo":"Respuesta personal.","carpeta":["24.","15°.","13.","Se adelanta."]})
N4=NV("Vas a comparar el globo y el planisferio, reconocer los elementos de un mapa y usar la escala.",["Globo y planisferio","Elementos de un mapa","La escala","Tipos de mapas"],[
 S(1,"Globo y planisferio",[T("Comparación",["","Globo","Planisferio"],[["Forma","Esférica, real","Plana"],["Tamaños","Reales","Deformados"],["Se ve","Una parte a la vez","Todo el planeta"]]),P("En el planisferio más usado, las zonas cercanas a los polos se agrandan: Groenlandia parece tan grande como África, pero África es unas 14 veces más grande.")]),
 S(1,"Elementos de un mapa",[T("Elementos",["Elemento","Para qué sirve"],[["Título","Dice qué muestra el mapa"],["Referencias","Explican colores y símbolos"],["Escala","Indica cuánto se achicó la realidad"],["Orientación","Marca el norte (rosa de los vientos)"]])]),
 S(2,"La escala y los tipos",[E("Escala 1:100.000","Dos ciudades están a 8 cm en el mapa.",["1 cm del mapa = 100.000 cm reales = 1 km.","8 cm = 8 km."]),T("Tipos de mapas",["Tipo","Muestra"],[["Físico","Relieve, ríos, montañas"],["Político","Países, provincias, capitales"],["Temático","Un tema: lluvias, población, cultivos"]])])],
 {"titulo":"usar la escala","planteo":"Escala 1:50.000. Dos puntos están a 6 cm. ¿Distancia real?","pasos":["1 cm = 50.000 cm = 500 m.","6 × 500 m = 3000 m.","Distancia real: 3 km."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un mapa que muestra países y capitales es ___ .","El elemento que explica los símbolos son las ___ ."]},
 {"titulo":"tu turno","planteo":"Dibujá en tu carpeta un mapa simple de tu barrio con título, referencias, orientación y una escala aproximada."},
 {"titulo":"Antes de leer, mirá","texto":"Título, referencias y escala: con esas tres cosas ya sabés qué estás mirando."},
 ["Creer que el planisferio muestra los tamaños reales.","Leer un mapa sin mirar las referencias."],
 RS(("Globo","Real pero parcial."),("Planisferio","Completo pero deformado."),("Elementos","Título, referencias, escala, norte."),("Escala","1 cm = distancia real.")),
 G(("Planisferio","Mapa plano de todo el planeta."),("Escala","Relación entre el mapa y la realidad."),("Referencias","Explicación de los símbolos de un mapa.")),
 ["Escala 1:100.000: si dos pueblos están a 5 cm en el mapa, ¿a cuántos km están? Respondé solo el número.","¿Qué tipo de mapa muestra montañas y ríos?","¿Qué elemento del mapa indica dónde está el norte?","¿Qué es más grande en la realidad: África o Groenlandia?"],
 [["5","5 km"],["fisico","físico","un mapa físico","el físico"],["orientacion","orientación","la orientación","rosa de los vientos","la rosa de los vientos"],["africa","áfrica"]],
 {"incompleto":"Político. Referencias.","solo":"Respuesta personal.","carpeta":["5.","Físico.","La orientación (rosa de los vientos).","África."]})
ACT={"1":[{"t":"matching","p":"Uní cada movimiento con lo que produce.","o":{"izquierda":["Rotación","Traslación + eje inclinado","Las casi 6 horas que sobran por año"],"derecha":["Día y noche","Estaciones","Año bisiesto"]},"r":{"pares":{"Rotación":"Día y noche","Traslación + eje inclinado":"Estaciones","Las casi 6 horas que sobran por año":"Año bisiesto"}},"e":"Cada movimiento tiene su consecuencia."},MC("¿Por qué cuando en Argentina es verano en Europa es invierno?",["Por la inclinación del eje terrestre","Porque Argentina está más cerca del Sol","Porque la Tierra gira más rápido en el sur","Porque en Europa hay más nubes"],"Por la inclinación del eje terrestre","Cada hemisferio recibe los rayos directos en distinto momento.")],
 "2":[{"t":"classify","p":"¿Latitud o longitud?","o":{"elementos":["34° S","58° O","0° (Ecuador)","0° (Greenwich)"],"categorias":["Latitud","Longitud"]},"r":{"categorias":{"34° S":"Latitud","58° O":"Longitud","0° (Ecuador)":"Latitud","0° (Greenwich)":"Longitud"}},"e":"N/S es latitud; E/O es longitud."},MC("Un lugar está a 0° de latitud. ¿Dónde está?",["Sobre el Ecuador","En el polo sur","Sobre Greenwich","En Argentina"],"Sobre el Ecuador","El Ecuador es la latitud cero.")],
 "3":[N("En Buenos Aires (UTC −3) son las {h}. ¿Qué hora es en Madrid (UTC +1)? (Si pasa de 24, restá 24)",{"formula":"(h+4)%24"},"Madrid está 4 husos al este: se suman 4 horas.",{"vars":{"h":{"min":6,"max":22}}}),MC("¿Cuántos grados de longitud mide cada huso horario?",["15°","24°","30°","10°"],"15°","360° ÷ 24.")],
 "4":[N("Escala 1:100.000. Dos ciudades están a {c} cm en el mapa. ¿Cuántos km hay en la realidad?",{"formula":"c"},"Cada centímetro es un kilómetro.",{"vars":{"c":{"min":2,"max":15}}}),{"t":"matching","p":"Uní cada mapa con su tipo.","o":{"izquierda":["Montañas y ríos","Países y capitales","Lluvias del año"],"derecha":["Físico","Político","Temático"]},"r":{"pares":{"Montañas y ríos":"Físico","Países y capitales":"Político","Lluvias del año":"Temático"}},"e":"Cada tipo muestra algo distinto."}],
 "5":[MC("Relámpago. El día y la noche se producen por la…",["Rotación","Traslación","Inclinación"],"Rotación","Gira sobre su eje.",tiempo=20),MC("Relámpago. El meridiano 0° es…",["Greenwich","El Ecuador","El trópico"],"Greenwich","Divide este y oeste.",tiempo=20),MC("Relámpago. Argentina está en el huso…",["UTC −3","UTC 0","UTC +3"],"UTC −3","Tres horas menos que Londres.",tiempo=20),MC("Relámpago. Un mapa de lluvias es…",["Temático","Político","Físico"],"Temático","Un solo tema.",tiempo=20)]}
EXAMEN=[[1,MC("¿Qué causa las estaciones del año?",["La inclinación del eje y la traslación","La distancia al Sol","La rotación","La Luna"],"La inclinación del eje y la traslación","Cada hemisferio recibe rayos directos en distinto momento.")],[1,MC("¿Cuánto dura la rotación?",["Unas 24 horas","365 días","Un mes","Una semana"],"Unas 24 horas","Produce el día y la noche.")],[1,VF("Cuando en Argentina es verano, en el hemisferio norte también es verano.","Falso","Las estaciones son opuestas.")],
 [2,MC("Buenos Aires está aproximadamente en…",["34° S, 58° O","34° N, 58° E","0°, 0°","58° S, 34° O"],"34° S, 58° O","Hemisferios sur y oeste.")],[2,MC("Los meridianos van…",["De polo a polo","De este a oeste","Solo por el Ecuador","En espiral"],"De polo a polo","Los paralelos van de este a oeste.")],[2,VF("La latitud indica la distancia al meridiano de Greenwich.","Falso","Indica la distancia al Ecuador.")],
 [3,N("En Buenos Aires (UTC −3) son las 9. ¿Qué hora es en Londres (UTC 0)?",{"acepta":[12]},"Se suman 3 horas.")],[3,MC("Hacia el oeste, la hora…",["Se atrasa","Se adelanta","No cambia","Cambia de día siempre"],"Se atrasa","Una hora menos por huso.")],[3,MC("¿Qué pasa al cruzar el meridiano 180°?",["Cambia la fecha","Cambia la estación","Se invierten los hemisferios","Nada"],"Cambia la fecha","Es la línea internacional de cambio de fecha.")],
 [4,MC("¿Por qué Groenlandia parece enorme en muchos planisferios?",["Porque el planisferio deforma cerca de los polos","Porque es el país más grande","Porque está mal dibujado a propósito","Porque está en el Ecuador"],"Porque el planisferio deforma cerca de los polos","África es unas 14 veces más grande.")],[4,N("Escala 1:100.000. Dos puntos a 7 cm en el mapa. ¿Cuántos km reales?",{"acepta":[7]},"1 cm = 1 km.")],[4,MC("¿Qué elemento del mapa explica qué significa cada color?",["Las referencias","El título","La escala","La orientación"],"Las referencias","Sin ellas no se puede leer el mapa.")],[4,VF("Un mapa político muestra países, provincias y capitales.","Verdadero","Muestra divisiones políticas.")]]
M={"subject_id":"a5f9b6fc-7f3b-4743-977d-da7f4f3a37bb","tema":2,"practica":"Práctica general: la Tierra y el espacio geográfico","examen_titulo":"Nivel jefe: la Tierra y el espacio geográfico","niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-2.json"),"w"),ensure_ascii=False); print("ok")
