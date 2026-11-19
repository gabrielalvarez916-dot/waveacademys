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
def fig_camino():
    fig, ax = plt.subplots(figsize=(8, 1.6)); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 1.6)
    for i, t in enumerate(["Observar", "Preguntar", "Hipótesis", "Experimentar", "Concluir"]):
        x = 1 + i * 2; ax.add_patch(plt.Rectangle((x - 0.85, 0.35), 1.7, 0.9, facecolor=C, edgecolor=O, lw=1.6)); ax.text(x, 0.8, t, ha="center", va="center", fontsize=11, color=O, weight="bold")
        if i < 4: ax.annotate("", xy=(x + 1.15, 0.8), xytext=(x + 0.88, 0.8), arrowprops=dict(arrowstyle="->", color=V, lw=2))
    return png(fig)
def fig_te():
    fig, ax = plt.subplots(figsize=(5.6, 2.8)); t = [0, 5, 10, 15, 20, 25, 30]; T = [80, 69, 60, 53, 47, 42, 38]
    ax.plot(t, T, "-o", color=V, lw=2.2); ax.set_xlabel("Tiempo (min)", color=O); ax.set_ylabel("Temperatura (°C)", color=O); ax.set_title("Cómo se enfría el té", color=O, fontsize=11)
    ax.set_xticks(t); ax.set_ylim(30, 85); ax.grid(alpha=.3)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    return png(fig)

N1={"objetivo":"Vas a poder observar con atención, distinguir preguntas investigables y escribir una hipótesis que se pueda poner a prueba.",
"vas_a_ver":["Qué es observar en ciencia","Preguntas investigables","Qué es una hipótesis","Cómo escribirla: si… entonces…","El camino de la investigación"],
"secciones":[
 S(1,"Observar",[D("Observar","En ciencia, <b>observar</b> es mirar con atención los detalles y <b>registrarlos</b>: qué cambió, cuánto, dónde y en cuánto tiempo."),
  E("Dos cubitos de hielo","Uno al sol y otro a la sombra.",["Observación pobre: \"el del sol se derritió rápido\".","Observación científica: \"al sol tardó 6 minutos; a la sombra, 15\".","La segunda tiene datos que se pueden comparar."])]),
 S(1,"Preguntas investigables",[D("Pregunta investigable","Es una pregunta que se puede responder <b>observando o haciendo un experimento</b>. Las preguntas de gusto u opinión no son investigables."),
  T("¿Se puede investigar?",["Pregunta","¿Investigable?"],[["¿El hielo se derrite más rápido al sol?","Sí"],["¿Cuánto tarda en derretirse un cubito?","Sí"],["¿El hielo es lindo?","No: es un gusto"]])]),
 S(2,"La hipótesis",[P("Una <b>hipótesis</b> es una <b>posible respuesta</b> a la pregunta investigable, que se puede poner a prueba. Se suele escribir con la forma <b>si…, entonces…</b>"),
  E("La hipótesis del hielo","Pregunta: ¿el calor influye en cuánto tarda en derretirse el hielo?",["Hipótesis: si el hielo recibe más calor, entonces se derrite más rápido.","Prueba: un cubito bajo una lámpara y otro sin lámpara.","Si el de la lámpara se derrite antes, la hipótesis se confirma."])]),
 S(2,"El camino de la investigación",[P("Observar → preguntar → proponer una hipótesis → experimentar → concluir. Si la hipótesis no se confirma, no es un fracaso: también se aprende y se propone otra."),
  IMG("El camino de la investigación","Cada paso lleva al siguiente.","Cinco recuadros unidos por flechas: observar, preguntar, hipótesis, experimentar y concluir.",fig_camino())]),
],
"ejemplo_completo":{"titulo":"el pan","planteo":"Un pan guardado en un lugar húmedo se llenó de hongos antes que otro guardado en un lugar seco. Escribí una pregunta investigable y una hipótesis.","pasos":["Observación: el pan del lugar húmedo tuvo hongos antes.","Pregunta investigable: ¿la humedad influye en cuánto tardan en aparecer los hongos?","Hipótesis: si el pan está en un lugar más húmedo, entonces le aparecen hongos más rápido.","Se podría probar con dos panes iguales, uno en un lugar húmedo y otro en uno seco."]},
"ejemplo_incompleto":{"titulo":"la planta","planteo":"Completá los espacios.","pasos":["Pregunta: ¿la luz influye en el crecimiento de una planta? Es una pregunta ___ .","Hipótesis: si la planta recibe más luz, ___ crece más."]},
"ejemplo_solo":{"titulo":"el azúcar","planteo":"Escribí una hipótesis para la pregunta: ¿el azúcar se disuelve más rápido en agua caliente que en agua fría?"},
"tip":{"titulo":"Si… entonces…","texto":"Si tu hipótesis no tiene la forma si… entonces…, probá reescribirla así: te ayuda a ver qué tenés que cambiar y qué tenés que medir."},
"ojo":["Escribir la hipótesis como pregunta: tiene que ser una respuesta posible.","Confundir una hipótesis con una opinión: la hipótesis se puede comprobar."],
"resumen":[{"titulo":"Observar","texto":"Mirar con atención y registrar datos."},{"titulo":"Pregunta investigable","texto":"Se responde observando o experimentando."},{"titulo":"Hipótesis","texto":"Posible respuesta: si…, entonces…"},{"titulo":"Camino","texto":"Observar, preguntar, hipótesis, experimentar, concluir."}],
"glosario":[{"palabra":"Observar","significado":"Mirar con atención y anotar los detalles."},{"palabra":"Registro","significado":"Lo que se anota de lo observado."},{"palabra":"Investigable","significado":"Que se puede averiguar con observaciones o experimentos."},{"palabra":"Hipótesis","significado":"Posible respuesta que se pone a prueba."},{"palabra":"Experimento","significado":"Prueba preparada para comprobar una hipótesis."}],
"carpeta":["¿La pregunta \"¿el chocolate es rico?\" es investigable? Respondé sí o no.","¿La pregunta \"¿cuánto tarda en hervir un litro de agua?\" es investigable? Respondé sí o no.","Completá la hipótesis: si una planta recibe más agua, ___ crece más. ¿Qué palabra falta?","Un compañero escribió como hipótesis: \"¿El sol derrite el hielo?\". ¿Eso es una pregunta o una hipótesis?"],
"respuestas_carpeta":[["no"],["si","sí"],["entonces"],["pregunta","una pregunta"]],
"soluciones":{"incompleto":"Investigable. Entonces.","solo":"Si el agua está más caliente, entonces el azúcar se disuelve más rápido.","carpeta":["No: es una opinión, no se puede medir.","Sí: se puede medir con un reloj.","Entonces.","Es una pregunta: la hipótesis sería \"si el hielo está al sol, entonces se derrite más rápido\"."]}}
N2={"objetivo":"Vas a poder identificar las variables de un experimento y diseñar uno en el que cambie una sola cosa.",
"vas_a_ver":["Qué es una variable","Variable independiente y dependiente","Variables controladas","Grupo control","Experimentos bien y mal diseñados"],
"secciones":[
 S(1,"Variables",[D("Variable","Una <b>variable</b> es algo que <b>puede cambiar</b> en un experimento: la luz, el agua, la temperatura, el tiempo."),
  P("En un experimento con plantas y luz, son variables la cantidad de luz, el agua de riego, el tipo de tierra y lo que crece la planta.")]),
 S(1,"Independiente y dependiente",[D("Dos tipos","La <b>variable independiente</b> es la que se <b>cambia a propósito</b>. La <b>variable dependiente</b> es la que se <b>mide</b> para ver el efecto."),
  T("Experimento: ¿la luz influye en el crecimiento?",["Variable","Cuál es","Qué se hace"],[["Independiente","La luz","Una planta con luz y otra sin"],["Dependiente","El crecimiento","Se mide la altura"],["Controladas","Agua, tierra, maceta","Se dejan iguales"]])]),
 S(2,"Variables controladas y grupo control",[P("Las <b>variables controladas</b> se dejan <b>iguales</b> en todo el experimento, para que solo influya la independiente. El <b>grupo control</b> es el que no recibe el cambio y sirve para comparar."),
  E("Cubitos en agua","¿El hielo se derrite más rápido en agua tibia?",["Independiente: la temperatura del agua.","Dependiente: el tiempo que tarda el cubito.","Controladas: mismo vaso, misma cantidad de agua, cubitos del mismo tamaño.","Grupo control: el cubito en agua fría."])]),
 S(2,"Una sola variable por vez",[P("Si se cambian dos cosas a la vez (la luz y el agua), no se puede saber cuál produjo el efecto. Por eso, en un buen experimento <b>cambia una sola variable</b>.")]),
],
"ejemplo_completo":{"titulo":"el pan y la humedad","planteo":"Se quiere saber si la humedad influye en la aparición de hongos en el pan. Identificá las variables.","pasos":["Independiente: la humedad (un pan en lugar húmedo y otro en lugar seco).","Dependiente: los días que tardan en aparecer los hongos.","Controladas: el mismo tipo de pan, el mismo tamaño y la misma temperatura.","Grupo control: el pan del lugar seco."]},
"ejemplo_incompleto":{"titulo":"el azúcar","planteo":"¿El azúcar se disuelve más rápido en agua caliente? Completá los espacios.","pasos":["Variable independiente: la ___ del agua.","Variable dependiente: el ___ que tarda en disolverse."]},
"ejemplo_solo":{"titulo":"la pelota","planteo":"¿La altura desde la que cae una pelota influye en cuánto rebota? Nombrá la variable independiente y la dependiente."},
"tip":{"titulo":"Preguntate qué cambio y qué mido","texto":"La que cambiás vos es la independiente; la que medís para ver qué pasó es la dependiente. Todo lo demás, igual."},
"ojo":["Cambiar más de una variable a la vez.","Olvidar el grupo control: sin comparación no hay conclusión."],
"resumen":[{"titulo":"Independiente","texto":"La que se cambia."},{"titulo":"Dependiente","texto":"La que se mide."},{"titulo":"Controladas","texto":"Las que se dejan iguales."},{"titulo":"Grupo control","texto":"Sin el cambio, para comparar."}],
"glosario":[{"palabra":"Variable","significado":"Algo que puede cambiar en un experimento."},{"palabra":"Independiente","significado":"Variable que se cambia a propósito."},{"palabra":"Dependiente","significado":"Variable que se mide."},{"palabra":"Controlada","significado":"Variable que se deja igual."},{"palabra":"Grupo control","significado":"El que no recibe el cambio."}],
"carpeta":["En un experimento sobre si la luz influye en el crecimiento de una planta, ¿cuál es la variable independiente?","En ese mismo experimento, ¿cuál es la variable dependiente?","Si se quiere saber si el agua tibia derrite más rápido el hielo, ¿la cantidad de agua debe ser igual o distinta en los dos vasos?","Un compañero cambió la luz y el riego al mismo tiempo. ¿Puede saber cuál influyó? Respondé sí o no."],
"respuestas_carpeta":[["luz","la luz"],["crecimiento","el crecimiento","altura","la altura"],["igual"],["no"]],
"soluciones":{"incompleto":"Temperatura. Tiempo.","solo":"Independiente: la altura desde la que cae. Dependiente: cuánto rebota.","carpeta":["La luz.","El crecimiento (la altura).","Igual: es una variable controlada.","No: cambiaron dos variables a la vez."]}}
N3={"objetivo":"Vas a poder registrar datos de un experimento en una tabla con unidades y representarlos en un gráfico.",
"vas_a_ver":["Registrar en el momento","La tabla de datos","Las unidades","El gráfico","Leer un gráfico"],
"secciones":[
 S(1,"Registrar los datos",[D("Registro","Registrar es <b>anotar cada medición en el momento</b>, con su <b>unidad</b>. Lo que no se anota, se olvida o se recuerda mal."),
  P("Para estudiar cómo se enfría un té, se mide la temperatura con un termómetro cada 5 minutos y se anota enseguida.")]),
 S(1,"La tabla de datos",[D("Tabla","Ordena las mediciones en columnas. Cada columna lleva su <b>nombre</b> y su <b>unidad</b> en el encabezado."),
  T("Temperatura del té",["Tiempo (min)","Temperatura (°C)"],[["0","80"],["10","60"],["20","47"],["30","38"]])]),
 S(2,"El gráfico",[P("Un gráfico muestra de un vistazo <b>cómo cambia</b> una variable. Lleva <b>título</b>, <b>ejes con nombre y unidad</b> y una <b>escala pareja</b>. Para datos que cambian con el tiempo se usa un gráfico de líneas."),
  IMG("Cómo se enfría el té","La línea baja rápido al principio y cada vez más despacio.","Gráfico de líneas de la temperatura del té, de 80 °C a 38 °C en 30 minutos.",fig_te())]),
 S(2,"Leer el gráfico",[P("En el gráfico del té se ve algo que en la tabla cuesta ver: en los primeros 10 minutos bajó 20 grados y en los últimos 10, solo 9. El té se enfría <b>cada vez más despacio</b>.")]),
],
"ejemplo_completo":{"titulo":"la planta","planteo":"Una planta midió 2 cm el día 1, 5 cm el día 4, 8 cm el día 7 y 11 cm el día 10. Armá la tabla y describí cómo creció.","pasos":["Columnas: Día y Altura (cm).","Filas: 1 y 2; 4 y 5; 7 y 8; 10 y 11.","Cada 3 días creció 3 cm.","Creció de forma pareja: el gráfico sería una línea recta que sube."]},
"ejemplo_incompleto":{"titulo":"la tabla","planteo":"Completá los espacios.","pasos":["El encabezado de la columna de tiempo lleva su unidad: Tiempo ( ___ ).","Entre el minuto 0 (80 °C) y el 10 (60 °C), el té bajó ___ °C."]},
"ejemplo_solo":{"titulo":"el hielo","planteo":"Un cubito pesaba 20 g a los 0 minutos, 14 g a los 5 y 8 g a los 10. ¿Cuántos gramos perdió cada 5 minutos?"},
"tip":{"titulo":"Unidad siempre","texto":"Un número sin unidad no dice nada: 60 puede ser grados, minutos o centímetros. Escribí siempre la unidad."},
"ojo":["Anotar los datos sin unidades.","Hacer un gráfico con escala despareja o sin nombre en los ejes."],
"resumen":[{"titulo":"Registrar","texto":"En el momento y con unidad."},{"titulo":"Tabla","texto":"Columnas con nombre y unidad."},{"titulo":"Gráfico","texto":"Título, ejes y escala pareja."},{"titulo":"Leer","texto":"Ver cómo cambia la variable."}],
"glosario":[{"palabra":"Medición","significado":"Valor que se obtiene al medir."},{"palabra":"Unidad","significado":"Lo que acompaña al número: °C, min, cm."},{"palabra":"Eje","significado":"Cada una de las líneas del gráfico donde van los valores."},{"palabra":"Escala","significado":"Cómo se numeran los ejes."},{"palabra":"Gráfico de líneas","significado":"Muestra cómo algo cambia en el tiempo."}],
"carpeta":["En la tabla del té, ¿cuántos grados bajó entre el minuto 10 y el 20?","¿Qué tipo de gráfico conviene para ver cómo cambia algo en el tiempo?","Si una planta mide 4 cm el lunes y 7 cm el jueves, ¿cuántos cm creció?","Un compañero anotó \"temperatura: 47\". ¿Qué le falta?"],
"respuestas_carpeta":[["13","13°C","13 °C"],["lineas","líneas","de lineas","de líneas"],["3","3cm","3 cm"],["unidad","la unidad"]],
"soluciones":{"incompleto":"min. 20.","solo":"6 g cada 5 minutos: 20 − 14 = 6 y 14 − 8 = 6.","carpeta":["13 °C: 60 − 47.","De líneas.","3 cm: 7 − 4.","La unidad: 47 °C."]}}
N4={"objetivo":"Vas a poder escribir un informe de laboratorio completo, con una conclusión que use los datos.",
"vas_a_ver":["Para qué sirve un informe","Las partes del informe","El procedimiento como receta","Resultados y conclusión","Cuando la hipótesis no se confirma"],
"secciones":[
 S(1,"Para qué sirve",[D("Informe de laboratorio","Es un texto que cuenta un experimento para que otra persona lo <b>entienda</b> y lo pueda <b>repetir</b> igual."),
  P("Los científicos comparten sus informes para que otros revisen si llegaron al mismo resultado.")]),
 S(1,"Las partes",[T("Partes del informe",["Parte","Qué tiene"],[["Título","De qué trata"],["Pregunta","Lo que se quiere averiguar"],["Hipótesis","La posible respuesta"],["Materiales","Todo lo que se usó"],["Procedimiento","Los pasos, numerados"],["Resultados","Los datos: tabla y gráfico"],["Conclusión","La respuesta a la pregunta"]],"Las tres primeras se escriben antes de experimentar.")]),
 S(2,"Procedimiento y resultados",[P("El <b>procedimiento</b> se escribe como una receta, con pasos numerados y medidas: \"1) Poner 200 ml de agua en cada vaso…\". En los <b>resultados</b> van solo los datos, sin opinar."),
  E("El experimento del hielo","Así quedarían dos partes.",["Procedimiento: 1) Poner un cubito de 10 g bajo una lámpara. 2) Poner otro igual sin lámpara. 3) Medir el tiempo hasta que se derritan.","Resultados: con lámpara, 6 minutos; sin lámpara, 15 minutos."])]),
 S(2,"La conclusión",[P("La conclusión <b>responde la pregunta</b> y dice si la hipótesis <b>se confirmó o no</b>, usando los datos. Si no se confirmó, se dice igual: también es un resultado. Ejemplo: \"El calor acelera el derretimiento: con lámpara tardó 6 minutos y sin lámpara 15. La hipótesis se confirmó.\"")]),
],
"ejemplo_completo":{"titulo":"conclusión del pan","planteo":"Resultados: el pan en lugar húmedo tuvo hongos a los 3 días; el del lugar seco, a los 9. Hipótesis: si el pan está en un lugar más húmedo, le aparecen hongos más rápido. Escribí la conclusión.","pasos":["Comparar: 3 días contra 9 días.","Responder la pregunta: la humedad acelera la aparición de hongos.","Decir qué pasó con la hipótesis: se confirmó.","Conclusión: la humedad hace que los hongos aparezcan antes (3 días contra 9); la hipótesis se confirmó."]},
"ejemplo_incompleto":{"titulo":"ordenar","planteo":"Completá los espacios.","pasos":["La parte que dice todo lo que se usó se llama ___ .","La parte que responde la pregunta se llama ___ ."]},
"ejemplo_solo":{"titulo":"la hipótesis que falló","planteo":"Hipótesis: si una planta recibe música, crece más. Resultado: las dos plantas crecieron igual. ¿Qué dice la conclusión sobre la hipótesis?"},
"tip":{"titulo":"Como una receta","texto":"Leé tu procedimiento como si fueras otra persona: si no podés repetir el experimento solo con eso, falta algo."},
"ojo":["Cambiar la hipótesis después de ver los resultados.","Escribir una conclusión que no usa los datos, como \"salió bien\"."],
"resumen":[{"titulo":"Antes","texto":"Título, pregunta e hipótesis."},{"titulo":"Cómo","texto":"Materiales y procedimiento."},{"titulo":"Después","texto":"Resultados y conclusión."},{"titulo":"Conclusión","texto":"Responde con datos."}],
"glosario":[{"palabra":"Informe","significado":"Texto que cuenta un experimento."},{"palabra":"Procedimiento","significado":"Los pasos que se siguieron."},{"palabra":"Resultados","significado":"Los datos que se obtuvieron."},{"palabra":"Conclusión","significado":"La respuesta a la pregunta, con datos."},{"palabra":"Confirmar","significado":"Comprobar que la hipótesis era correcta."}],
"carpeta":["¿Qué parte del informe se escribe con pasos numerados?","¿En qué parte del informe van la tabla y el gráfico?","¿La hipótesis se escribe antes o después de hacer el experimento?","Un compañero escribió como conclusión \"el experimento salió bien\". ¿Qué le falta usar?"],
"respuestas_carpeta":[["procedimiento","el procedimiento"],["resultados","los resultados"],["antes"],["datos","los datos"]],
"soluciones":{"incompleto":"Materiales. Conclusión.","solo":"Que no se confirmó: la música no hizo que la planta creciera más.","carpeta":["El procedimiento.","En los resultados.","Antes.","Los datos: responder la pregunta y decir si la hipótesis se confirmó."]}}
ACT={
"1":[{"t":"classify","p":"Clasificá cada pregunta.","o":{"elementos":["¿El hielo se derrite más rápido al sol?","¿Cuánto tarda en hervir el agua?","¿El verde es el color más lindo?","¿Qué fruta es la más rica?"],"categorias":["Investigable","No investigable"]},"r":{"categorias":{"¿El hielo se derrite más rápido al sol?":"Investigable","¿Cuánto tarda en hervir el agua?":"Investigable","¿El verde es el color más lindo?":"No investigable","¿Qué fruta es la más rica?":"No investigable"}},"e":"Las investigables se responden observando o midiendo; las otras son gustos."},
     MC("¿Cuál de estas es una hipótesis?",["¿La luz hace crecer a las plantas?","Si una planta recibe más luz, entonces crece más","Las plantas son lindas","Voy a regar la planta"],"Si una planta recibe más luz, entonces crece más","Es una posible respuesta que se puede poner a prueba.")],
"2":[MC("Experimento: ¿la temperatura del agua influye en cuánto tarda en disolverse el azúcar? ¿Cuál es la variable independiente?",["El tiempo","La temperatura del agua","La cantidad de azúcar","El vaso"],"La temperatura del agua","Es la que se cambia a propósito."),
     VF("En un buen experimento se cambian varias variables a la vez para ahorrar tiempo.","Falso","Se cambia una sola, si no, no se sabe cuál produjo el efecto.")],
"3":[N("Un té estaba a 70 °C y 10 minutos después a {b} °C. ¿Cuántos grados bajó?",{"formula":"70-b"},"Se resta la temperatura final a la inicial.",{"vars":{"b":{"min":40,"max":62}}}),
     MC("¿Qué le falta a la medición \"altura: 12\"?",["Un título","La unidad","Un gráfico","Nada"],"La unidad","12 cm, 12 mm o 12 m no son lo mismo.")],
"4":[{"t":"ordering","p":"Ordená las partes del informe.","o":["Conclusión","Hipótesis","Materiales","Pregunta","Resultados","Procedimiento","Título"],"r":{"orden":["Título","Pregunta","Hipótesis","Materiales","Procedimiento","Resultados","Conclusión"]},"e":"Primero lo que se escribe antes de experimentar; al final, los resultados y la conclusión."},
     MC("¿Cuál es la mejor conclusión?",["El experimento salió bien","Con lámpara el hielo tardó 6 min y sin lámpara 15: el calor acelera el derretimiento y la hipótesis se confirmó","Me gustó hacer el experimento","El hielo es frío"],"Con lámpara el hielo tardó 6 min y sin lámpara 15: el calor acelera el derretimiento y la hipótesis se confirmó","Responde la pregunta y usa los datos.")],
"5":[MC("Relámpago. \"Si el agua está más caliente, el azúcar se disuelve más rápido\" es…",["Una pregunta","Una hipótesis","Una conclusión"],"Una hipótesis","Es una posible respuesta que se puede probar.",tiempo=20),
     MC("Relámpago. La variable que se mide se llama…",["Independiente","Dependiente","Controlada"],"Dependiente","Es la que muestra el efecto.",tiempo=20),
     MC("Relámpago. Para ver cómo cambia algo en el tiempo conviene un gráfico…",["Circular","De líneas","De barras"],"De líneas","Muestra la evolución.",tiempo=20),
     MC("Relámpago. ¿En qué parte del informe van los pasos numerados?",["Procedimiento","Conclusión","Título"],"Procedimiento","Como una receta.",tiempo=20)],
}
EXAMEN=[
 [1,MC("¿Cuál es una observación científica?",["El hielo se derritió rápido","El cubito tardó 6 minutos en derretirse","Me gusta el hielo","El hielo es frío"],"El cubito tardó 6 minutos en derretirse","Tiene un dato concreto.")],
 [1,VF("\"¿Qué perro es el más lindo?\" es una pregunta investigable.","Falso","Es una opinión, no se puede medir.")],
 [1,MC("¿Qué forma suele tener una hipótesis?",["¿Por qué…?","Si…, entonces…","Me parece que…","Ojalá…"],"Si…, entonces…","Une lo que se cambia con lo que se espera.")],
 [2,MC("En un experimento sobre si la luz influye en el crecimiento, el agua de riego debe ser…",["Distinta en cada planta","Igual en las dos plantas","Muchísima","No importa"],"Igual en las dos plantas","Es una variable controlada.")],
 [2,MC("¿Para qué sirve el grupo control?",["Para comparar","Para ganar tiempo","Para decorar","No sirve"],"Para comparar","No recibe el cambio.")],
 [2,MC("¿Cuál es la variable dependiente en \"¿la altura de caída influye en el rebote de una pelota?\"?",["La altura de caída","Lo que rebota","La pelota","El piso"],"Lo que rebota","Es lo que se mide.")],
 [3,N("Una planta medía 3 cm y una semana después 8 cm. ¿Cuántos cm creció?",{"acepta":[5]},"8 − 3.")],
 [3,MC("¿Qué debe tener el encabezado de cada columna de una tabla de datos?",["Un dibujo","Nombre y unidad","Un color","Nada"],"Nombre y unidad","Ej.: Tiempo (min).")],
 [3,VF("En un gráfico, la escala de los ejes debe ir de a saltos iguales.","Verdadero","Si no, el gráfico engaña.")],
 [4,MC("¿Qué parte del informe se escribe antes de hacer el experimento?",["La conclusión","Los resultados","La hipótesis","Ninguna"],"La hipótesis","Junto con el título y la pregunta.")],
 [4,MC("Si la hipótesis no se confirma, en la conclusión…",["Se cambia la hipótesis","Se dice que no se confirmó","Se borran los datos","Se repite hasta que salga"],"Se dice que no se confirmó","También es un resultado.")],
 [4,MC("¿Para qué sirve escribir el procedimiento con pasos numerados?",["Para que otro pueda repetir el experimento","Para que sea más largo","Para decorar","No sirve"],"Para que otro pueda repetir el experimento","Como una receta.")],
 [4,VF("En los resultados se escriben los datos obtenidos, sin opinar.","Verdadero","Las interpretaciones van en la conclusión.")],
]
M={"subject_id":"9fa85d7b-ee7a-4853-8486-a69f9b539c12","tema":1,"practica":"Práctica general: ciencia y método","examen_titulo":"Nivel jefe: ciencia y método","niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-1.json"),"w"),ensure_ascii=False)
print("ok")
