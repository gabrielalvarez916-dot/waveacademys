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

from matplotlib.patches import Rectangle, Polygon
def fig_libro():
    fig, ax = plt.subplots(figsize=(7.2, 3.3)); ax.axis("off"); ax.set_xlim(0, 14.4); ax.set_ylim(-1.4, 6)
    ax.add_patch(Rectangle((0.2, 0), 4, 5.6, color="#5b3f8c")); [ax.plot([0.6, 3.8 if i < 7 else 2.4], [4.8 - i*.5]*2, color="#d6c4ff", lw=3) for i in range(8)]
    ax.add_patch(Rectangle((4.3, 0), 0.7, 5.6, color="#3f2a66")); ax.text(4.65, 2.8, "EL FARO DE LOS GATOS", rotation=90, ha="center", va="center", color="white", fontsize=6)
    ax.add_patch(Rectangle((5.1, 0), 4, 5.6, color="#7458c4")); ax.text(7.1, 4.8, "El faro de\nlos gatos", ha="center", va="center", color="white", fontsize=12, weight="bold"); ax.text(7.1, 1.1, "Ana Ríos", ha="center", color="white", fontsize=10); ax.text(7.1, 0.5, "Brújula", ha="center", color="#d6c4ff", fontsize=8)
    ax.add_patch(Rectangle((9.6, 0), 4.3, 5.6, facecolor="white", edgecolor="#bdb2d6")); ax.text(11.75, 5, "ÍNDICE", ha="center", fontsize=10, weight="bold", color=O)
    for i in range(5): ax.text(9.9, 4.2 - i*.75, f"{i+1}. ............", fontsize=8, color=O); ax.text(13.6, 4.2 - i*.75, str(5+i*12), fontsize=8, color=O, ha="right")
    for x, t in ((2.2, "Contratapa:\nde qué trata"), (4.65, "Lomo"), (7.1, "Tapa: título,\nautor, editorial"), (11.75, "Índice:\nlos capítulos")):
        ax.text(x, -0.75, t, ha="center", va="center", fontsize=8.5, color=V, weight="bold")
    return png(fig)
def fig_parrafo():
    fig, ax = plt.subplots(figsize=(7, 2.4)); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 4)
    ax.add_patch(Rectangle((0.1, 1.1), 9.8, 2.8, facecolor="#fbf8ff", edgecolor="#bdb2d6"))
    L = ["      Leo poco. Me cuesta concentrarme.", "Pero este año quiero leer más novelas,", "sobre todo de misterio."]
    for i, t in enumerate(L): ax.text(0.4, 3.4 - i*.8, t, fontsize=11, color=O, family="DejaVu Sans")
    ax.annotate("sangría", xy=(0.7, 3.35), xytext=(0.6, 0.4), color=V, fontsize=8.5, weight="bold", arrowprops=dict(arrowstyle="->", color=V))
    ax.annotate("mayúscula", xy=(1.15, 3.35), xytext=(2.0, 0.4), color=V, fontsize=8.5, weight="bold", arrowprops=dict(arrowstyle="->", color=V))
    ax.annotate("punto seguido", xy=(2.65, 3.3), xytext=(3.8, 0.4), color=V, fontsize=8.5, weight="bold", arrowprops=dict(arrowstyle="->", color=V))
    ax.annotate("punto y aparte", xy=(3.75, 1.7), xytext=(6.6, 0.4), color=V, fontsize=8.5, weight="bold", arrowprops=dict(arrowstyle="->", color=V))
    return png(fig)
def fig_ficha():
    fig, ax = plt.subplots(figsize=(5.2, 2.6)); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 5)
    ax.add_patch(Rectangle((0.2, 0.2), 9.6, 4.6, facecolor="#fffbea", edgecolor="#e6d38a", lw=2)); ax.add_patch(Rectangle((0.2, 4.0), 9.6, 0.8, color="#f4b63f"))
    ax.text(5, 4.4, "FICHA BIBLIOGRÁFICA", ha="center", va="center", fontsize=10, weight="bold", color="#3a2a10")
    for i, (a, b) in enumerate((("Autor:", "Ríos, Ana"), ("Título:", "El faro de los gatos"), ("Editorial:", "Brújula"), ("Año:", "2021"))):
        y = 3.4 - i*.85; ax.text(0.6, y, a, fontsize=10, color="#7458c4", weight="bold", va="center"); ax.text(3.2, y, b, fontsize=10, color=O, va="center"); ax.plot([0.6, 9.4], [y-.35]*2, color="#e6d38a", lw=1)
    return png(fig)

N1={"objetivo":"Vas a repasar las estrategias de lectura: usar el paratexto, leer en tres momentos, reconocer la estructura de un relato y el narrador.",
"vas_a_ver":["El paratexto","Leer en tres momentos","Inferir","Estructura del relato","El narrador"],
"secciones":[
 S(1,"El paratexto",[D("Paratexto","Todo lo que acompaña al texto: <b>tapa, contratapa, título, autor, índice e imágenes</b>. Sirve para <b>anticipar</b> de qué trata antes de leer."),IMG("Las partes de un libro","Tapa, lomo, contratapa e índice: el paratexto.","Libro desplegado con contratapa, lomo, tapa e índice marcados.",fig_libro())]),
 S(1,"Leer en tres momentos",[T("Los tres momentos",["Momento","Qué hago"],[["Antes","Miro el paratexto y anticipo"],["Durante","Me hago preguntas, subrayo e infiero"],["Después","Resumo con mis palabras y opino"]]),
  D("Inferir","Deducir lo que el texto <b>no dice</b> a partir de pistas. Si el perro volvió con barro hasta las orejas, se infiere que estuvo en un charco.")]),
 S(2,"La estructura del relato",[T("Partes de un relato",["Parte","Qué cuenta","Ejemplo"],[["Situación inicial","Quiénes, dónde, cómo están","Lara vive con su abuelo, guardián de un faro"],["Conflicto","Algo rompe la calma","En una tormenta el faro se apaga y un barco se acerca a las rocas"],["Desenlace","Cómo se resuelve","Lara sube los 200 escalones y enciende la luz a mano"]])]),
 S(2,"El narrador",[P("El <b>narrador</b> es la voz que cuenta la historia; no es el autor. En <b>primera persona</b> es un personaje (\"yo busqué\"); en <b>tercera persona</b> cuenta desde afuera (\"Lara subió\"). Si conoce todo, incluso lo que piensan y sienten los personajes, es un narrador <b>omnisciente</b>.")]),
],
"ejemplo_completo":{"titulo":"leer un cuento","planteo":"Un cuento se titula \"La noche del apagón\" y en la tapa hay una vela. Aplicá los tres momentos.","pasos":["Antes: anticipo que habrá una noche sin luz y quizás algo de miedo.","Durante: me pregunto qué pasará y busco pistas.","Después: resumo la historia en tres oraciones.","Opino si me gustó y por qué."]},
"ejemplo_incompleto":{"titulo":"completar","planteo":"Completá los espacios.","pasos":["La parte del relato donde algo rompe la calma se llama ___ .","Si el narrador dice \"yo corrí\", está en ___ persona."]},
"ejemplo_solo":{"titulo":"inferir","planteo":"\"Ana entró empapada y dejó el paraguas roto en la puerta.\" ¿Qué podés inferir del tiempo afuera?"},
"tip":{"titulo":"Antes de leer, mirá","texto":"Dedicale un minuto al paratexto: tapa, contratapa e índice. Vas a entender mucho más rápido."},
"ojo":["Confundir al autor con el narrador.","Empezar a leer sin mirar el paratexto."],
"resumen":[{"titulo":"Paratexto","texto":"Tapa, contratapa, índice: sirven para anticipar."},{"titulo":"Tres momentos","texto":"Antes, durante y después."},{"titulo":"Estructura","texto":"Situación inicial, conflicto, desenlace."},{"titulo":"Narrador","texto":"Primera o tercera persona."}],
"glosario":[{"palabra":"Paratexto","significado":"Lo que acompaña al texto."},{"palabra":"Anticipar","significado":"Imaginar de qué trata antes de leer."},{"palabra":"Inferir","significado":"Deducir lo que el texto no dice."},{"palabra":"Conflicto","significado":"Problema que rompe la situación inicial."},{"palabra":"Narrador","significado":"Voz que cuenta la historia."}],
"carpeta":["¿Cómo se llama la parte del relato donde se resuelve el problema?","\"Yo abrí la puerta\": ¿primera o tercera persona?","¿Cómo se llama todo lo que acompaña al texto (tapa, índice, contratapa)?","¿Quién cuenta la historia: el autor o el narrador?"],
"respuestas_carpeta":[["desenlace","el desenlace"],["primera","primera persona","1.ª","1ra"],["paratexto","el paratexto"],["narrador","el narrador"]],
"soluciones":{"incompleto":"Conflicto. Primera.","solo":"Que llovía fuerte y había viento.","carpeta":["El desenlace.","Primera persona.","Paratexto.","El narrador."]}}
N2={"objetivo":"Vas a reconocer los géneros literarios y no literarios, y los subgéneros narrativos, para elegir mejor qué leer.",
"vas_a_ver":["Qué es un género","Narrativo, poético, teatral y no literario","Subgéneros narrativos","Mito, leyenda, fábula y cuento"],
"secciones":[
 S(1,"Las grandes familias",[D("Género","Familia de textos que se parecen en su forma y en lo que buscan."),
  T("Géneros",["Género","Qué hace","Ejemplos"],[["Narrativo","Cuenta una historia","cuento, novela"],["Poético","Versos, ritmo, emociones","poema, canción"],["Teatral","Diálogos para actuar","obra de teatro"],["No literario","Informa o explica","noticia, enciclopedia"]])]),
 S(1,"Subgéneros narrativos",[T("Subgéneros",["Subgénero","Qué tiene"],[["Maravilloso","Magia, hadas, dragones"],["Ciencia ficción","Futuro, ciencia y tecnología"],["Policial","Un enigma y alguien que lo resuelve"],["Terror","Busca provocar miedo"],["Realista","Hechos que podrían pasar"]])]),
 S(2,"Historias de siempre",[T("Relatos tradicionales",["Tipo","Qué tiene"],[["Mito","Dioses y héroes; explica el origen del mundo"],["Leyenda","Explica el origen de algo, en un lugar real"],["Fábula","Animales que hablan y una moraleja"],["Cuento","Ficción breve, de cualquier subgénero"]])]),
 S(2,"Elegir por género",[P("Conocer los géneros ayuda a saber qué esperar de un libro. Tener un género favorito está bien, pero probar otros puede llevarte a tu próximo libro preferido.")]),
],
"ejemplo_completo":{"titulo":"clasificar","planteo":"Un relato cuenta cómo una diosa creó el río Paraná. ¿Qué es?","pasos":["Aparece una diosa.","Explica el origen de algo de la naturaleza.","Los relatos con dioses que explican orígenes son mitos.","Es un mito."]},
"ejemplo_incompleto":{"titulo":"completar","planteo":"Completá los espacios.","pasos":["Una historia con robots en el año 3000 es de ciencia ___ .","La enseñanza final de una fábula se llama ___ ."]},
"ejemplo_solo":{"titulo":"tu turno","planteo":"Pensá en un libro, película o serie que te guste. ¿A qué subgénero pertenece y por qué?"},
"tip":{"titulo":"Mirá los elementos","texto":"Para saber el subgénero, buscá qué elementos aparecen: magia, tecnología, un crimen, algo que da miedo o hechos posibles."},
"ojo":["Confundir mito y leyenda: el mito tiene dioses y explica el origen del mundo.","Creer que todo texto es literario: la noticia informa."],
"resumen":[{"titulo":"Género","texto":"Familia de textos parecidos."},{"titulo":"Familias","texto":"Narrativo, poético, teatral, no literario."},{"titulo":"Subgéneros","texto":"Maravilloso, ciencia ficción, policial, terror, realista."},{"titulo":"Tradicionales","texto":"Mito, leyenda, fábula."}],
"glosario":[{"palabra":"Género","significado":"Familia de textos."},{"palabra":"Subgénero","significado":"Grupo dentro de un género."},{"palabra":"Moraleja","significado":"Enseñanza final de una fábula."},{"palabra":"Mito","significado":"Relato de dioses sobre el origen del mundo."},{"palabra":"Leyenda","significado":"Relato del origen de algo en un lugar real."}],
"carpeta":["Una historia con un crimen y un detective, ¿de qué subgénero es?","¿Cómo se llama la enseñanza al final de una fábula?","¿A qué género pertenece una noticia: literario o no literario?","Un relato sobre el origen de la yerba mate en la selva misionera, ¿es mito o leyenda?"],
"respuestas_carpeta":[["policial"],["moraleja","la moraleja"],["no literario"],["leyenda"]],
"soluciones":{"incompleto":"Ficción. Moraleja.","solo":"Respuesta personal: nombrá el subgénero y los elementos que lo muestran.","carpeta":["Policial.","Moraleja.","No literario.","Leyenda."]}}
N3={"objetivo":"Vas a escribir un texto de punto de partida usando el proceso de escritura, párrafos y conectores.",
"vas_a_ver":["El proceso de escritura","Oración y párrafo","Conectores","Cómo armar mi punto de partida"],
"secciones":[
 S(1,"El proceso de escritura",[T("Pasos para escribir",["Paso","Qué hago"],[["Planificar","Decido qué digo y en qué orden"],["Borrador","Escribo sin miedo a equivocarme"],["Revisar","Leo, corrijo y mejoro"],["Pasar en limpio","Escribo la versión final"]])]),
 S(1,"Oración y párrafo",[D("Oración","Empieza con <b>mayúscula</b> y termina en <b>punto</b>. Tiene sentido completo."),D("Párrafo","Grupo de oraciones sobre <b>una misma idea</b>. Termina en punto y aparte."),IMG("Un párrafo, marcado","Sangría, mayúscula, punto seguido y punto y aparte.","Párrafo de tres líneas con sus marcas señaladas.",fig_parrafo())]),
 S(2,"Conectores",[T("Conectores básicos",["Para…","Conectores"],[["Sumar","y, también, además"],["Oponer","pero, sin embargo"],["Dar una causa","porque, ya que"],["Dar una consecuencia","entonces, por eso"]])]),
 S(2,"Mi punto de partida",[E("Cuatro párrafos","Un texto sobre mí como lector.",["1) Quién soy como lector.","2) Un libro o historia que me gustó y por qué.","3) Qué me cuesta al leer o escribir.","4) Qué quiero lograr este año."])]),
],
"ejemplo_completo":{"titulo":"un párrafo","planteo":"Escribí el párrafo 2 del punto de partida.","pasos":["Elijo una historia: un cuento de terror que leí el año pasado.","Digo por qué me gustó: me tuvo nervioso hasta el final.","Uso un conector: \"porque\".","Resultado: \"Me gustó mucho un cuento de terror porque me tuvo nervioso hasta el final.\""]},
"ejemplo_incompleto":{"titulo":"conectores","planteo":"Completá con el conector adecuado.","pasos":["Me gusta leer, ___ no tengo mucho tiempo.","Leí mucho este verano, ___ ahora leo más rápido."]},
"ejemplo_solo":{"titulo":"tu punto de partida","planteo":"Escribí en tu carpeta tu texto de punto de partida con los cuatro párrafos."},
"tip":{"titulo":"Leelo en voz alta","texto":"Al revisar, leé tu texto en voz alta: donde te quedás sin aire, falta un punto."},
"ojo":["Escribir todo en una sola oración larguísima.","Repetir \"y entonces\" en lugar de variar los conectores."],
"resumen":[{"titulo":"Proceso","texto":"Planificar, escribir, revisar, pasar en limpio."},{"titulo":"Oración","texto":"Mayúscula y punto."},{"titulo":"Párrafo","texto":"Una idea; punto y aparte."},{"titulo":"Conectores","texto":"Unen ideas: y, pero, porque, por eso."}],
"glosario":[{"palabra":"Borrador","significado":"Primera versión de un texto."},{"palabra":"Revisar","significado":"Releer para corregir y mejorar."},{"palabra":"Oración","significado":"De mayúscula a punto, con sentido completo."},{"palabra":"Párrafo","significado":"Oraciones sobre una misma idea."},{"palabra":"Conector","significado":"Palabra que une ideas."}],
"carpeta":["¿Cuántas oraciones hay en: \"Llegué tarde. Llovía y perdí el colectivo.\"? Respondé con un número.","¿Qué conector opone ideas: \"porque\" o \"pero\"?","¿Cómo termina un párrafo: con punto seguido o con punto y aparte?","¿Cuál es el primer paso del proceso de escritura?"],
"respuestas_carpeta":[["2","dos"],["pero"],["punto y aparte","con punto y aparte"],["planificar"]],
"soluciones":{"incompleto":"pero. por eso.","solo":"Respuesta personal: revisá que tenga cuatro párrafos, mayúsculas, puntos y conectores.","carpeta":["2.","Pero.","Con punto y aparte.","Planificar."]}}
N4={"objetivo":"Vas a elegir libros usando el paratexto, armar fichas bibliográficas y planificar tu año lector.",
"vas_a_ver":["Elegir con el paratexto","Cuatro preguntas para elegir","La ficha bibliográfica","Mi plan de lectura"],
"secciones":[
 S(1,"Elegir con el paratexto",[T("Qué mirar",["Parte","Qué me dice"],[["Tapa","Título, autor, editorial"],["Contratapa","De qué trata, sin contar el final"],["Índice","Los capítulos y cómo está armado"]])]),
 S(1,"Cuatro preguntas",[P("<b>Género</b>: ¿qué tengo ganas de leer? <b>Recomendación</b>: ¿quién me lo aconsejó? <b>Primera página</b>: ¿me engancha? <b>Largo</b>: ¿me da el tiempo?")]),
 S(2,"La ficha bibliográfica",[D("Ficha bibliográfica","Registra un libro con <b>autor</b> (apellido, nombre), <b>título</b>, <b>editorial</b> y <b>año</b>."),
  IMG("Una ficha bibliográfica","Autor, título, editorial y año.","Ficha de cartulina con los cuatro datos de un libro.",fig_ficha())]),
 S(2,"Mi plan de lectura",[P("Tu año ya tiene paradas: un cuento policial, la novela <b>El fantasma de Canterville</b> de Oscar Wilde, poesía, teatro y un libro que elijas vos. Anotá en tu carpeta qué otros libros querés sumar. Y recordá: si un libro no te engancha, podés cambiarlo.")]),
],
"ejemplo_completo":{"titulo":"armar una ficha","planteo":"El libro \"La isla del viento\", de Pablo Sosa, editorial Faro, año 2019. Armá la ficha.","pasos":["Autor: apellido primero, Sosa, Pablo.","Título: La isla del viento.","Editorial: Faro.","Año: 2019."]},
"ejemplo_incompleto":{"titulo":"completar","planteo":"Completá los espacios.","pasos":["En la ficha, el autor se escribe primero con el ___ .","El resumen que dice de qué trata un libro está en la ___ ."]},
"ejemplo_solo":{"titulo":"tu ficha","planteo":"Elegí un libro que tengas en casa y armá su ficha bibliográfica."},
"tip":{"titulo":"La primera página","texto":"Antes de llevarte un libro, leé la primera página: si te dan ganas de seguir, es buena señal."},
"ojo":["Elegir un libro solo por la tapa.","Escribir el nombre antes del apellido en la ficha."],
"resumen":[{"titulo":"Paratexto","texto":"Tapa, contratapa, índice."},{"titulo":"Elegir","texto":"Género, recomendación, primera página, largo."},{"titulo":"Ficha","texto":"Autor, título, editorial, año."},{"titulo":"Plan","texto":"Mi año lector."}],
"glosario":[{"palabra":"Contratapa","significado":"Parte de atrás del libro con un resumen."},{"palabra":"Índice","significado":"Lista de capítulos."},{"palabra":"Editorial","significado":"Empresa que publica el libro."},{"palabra":"Ficha bibliográfica","significado":"Registro de los datos de un libro."},{"palabra":"Plan de lectura","significado":"Lista de libros para leer en un tiempo."}],
"carpeta":["¿Qué parte del libro tiene el resumen de qué trata?","En la ficha, ¿qué va primero: el apellido o el nombre del autor?","¿Qué dato falta en esta ficha: \"Ríos, Ana. El faro de los gatos. 2021.\"?","¿Dónde están los capítulos de un libro?"],
"respuestas_carpeta":[["contratapa","la contratapa"],["apellido","el apellido"],["editorial","la editorial"],["indice","índice","en el indice","en el índice","el índice"]],
"soluciones":{"incompleto":"Apellido. Contratapa.","solo":"Respuesta personal: apellido, nombre. Título. Editorial. Año.","carpeta":["La contratapa.","El apellido.","La editorial.","En el índice."]}}
ACT={
"1":[{"t":"ordering","p":"Ordená las partes del relato.","o":["Desenlace","Situación inicial","Conflicto"],"r":{"orden":["Situación inicial","Conflicto","Desenlace"]},"e":"Primero se presenta, después algo pasa y al final se resuelve."},
     MC("\"Al ver la carta, Tomás la guardó rápido y cambió de tema.\" ¿Qué se infiere?",["No quiere que los demás sepan qué dice","No sabe leer","La carta está en blanco","Está aburrido"],"No quiere que los demás sepan qué dice","Esconderla y cambiar de tema son pistas.")],
"2":[{"t":"classify","p":"Clasificá cada historia.","o":{"elementos":["Dragón y hechizo","Robots en Marte","Robo y detective","Fantasma en el sótano"],"categorias":["Maravilloso","Ciencia ficción","Policial","Terror"]},"r":{"categorias":{"Dragón y hechizo":"Maravilloso","Robots en Marte":"Ciencia ficción","Robo y detective":"Policial","Fantasma en el sótano":"Terror"}},"e":"Cada subgénero tiene sus elementos."},
     MC("Animales que hablan y una enseñanza al final:",["Mito","Leyenda","Fábula","Noticia"],"Fábula","La enseñanza es la moraleja.")],
"3":[{"t":"keywords","p":"Escribí tu texto de punto de partida en cuatro párrafos: quién sos como lector, un libro o historia que te gustó y por qué, qué te cuesta al leer o escribir y qué querés lograr. Usá al menos dos conectores.","o":{"ayuda":"Cuatro párrafos, con mayúscula, punto y aparte y conectores (porque, pero, por eso…)."},"r":{"grupos":[["leo","leer","lector*","lectora*","libro*","historia*"],["porque","ya que"],["pero","sin embargo","aunque"],["quiero","me gustaria*","lograr","objetivo"]],"minimo":3},"e":"Tiene que contar cómo leés, por qué te gustó algo, qué te cuesta y qué querés lograr, con conectores."},MC("¿Qué conector completa? \"Estudié mucho, ___ me fue bien.\"",["pero","por eso","sin embargo","aunque"],"por eso","Es una consecuencia."),
     {"t":"ordering","p":"Ordená el proceso de escritura.","o":["Revisar","Pasar en limpio","Planificar","Escribir el borrador"],"r":{"orden":["Planificar","Escribir el borrador","Revisar","Pasar en limpio"]},"e":"Primero se piensa, después se escribe y se corrige."}],
"4":[{"t":"matching","p":"Uní cada dato con su ejemplo.","o":{"izquierda":["Autor","Título","Editorial","Año"],"derecha":["Ríos, Ana","El faro de los gatos","Brújula","2021"]},"r":{"pares":{"Autor":"Ríos, Ana","Título":"El faro de los gatos","Editorial":"Brújula","Año":"2021"}},"e":"Los cuatro datos de la ficha."},
     MC("¿Dónde encontrás de qué trata un libro sin leerlo?",["En la contratapa","En la última página","En el código de barras","En el lomo"],"En la contratapa","Tiene un resumen sin contar el final.")],
"5":[MC("Relámpago. \"Yo encontré la llave\" está en…",["Primera persona","Tercera persona"],"Primera persona","El narrador es un personaje.",tiempo=20),
     MC("Relámpago. Un relato con dioses que explica el origen del mundo es un…",["Mito","Cuento","Poema"],"Mito","Explica orígenes con dioses.",tiempo=20),
     MC("Relámpago. Cada párrafo desarrolla…",["Una idea","Todas las ideas","Un diálogo"],"Una idea","Y termina en punto y aparte.",tiempo=20),
     MC("Relámpago. En la ficha, el autor se escribe…",["Apellido, nombre","Nombre apellido","Solo el nombre"],"Apellido, nombre","Ej.: Ríos, Ana.",tiempo=20)],
}
EXAMEN=[
 [1,MC("¿Para qué sirve mirar el paratexto antes de leer?",["Para anticipar de qué trata","Para saber el final","Para no leer","Para contar páginas"],"Para anticipar de qué trata","Tapa, contratapa e índice dan pistas.")],
 [1,MC("\"Sabía que su hermano mentía, aunque nadie más lo notara.\" ¿Qué narrador es?",["Tercera persona omnisciente","Primera persona","Narrador testigo","No hay narrador"],"Tercera persona omnisciente","Conoce lo que piensa el personaje.")],
 [1,VF("El autor y el narrador son siempre la misma persona.","Falso","El autor escribe; el narrador es la voz que cuenta.")],
 [2,MC("Un relato del litoral explica por qué el hornero hace su nido de barro. ¿Qué es?",["Leyenda","Mito","Fábula","Cuento policial"],"Leyenda","Explica un origen en un lugar real, sin dioses creadores ni moraleja.")],
 [2,MC("¿Qué texto es no literario?",["Un cuento","Una noticia","Un poema","Una obra de teatro"],"Una noticia","Informa sobre hechos reales.")],
 [2,VF("La leyenda explica el origen de algo y suele ubicarse en un lugar real.","Verdadero","Como la leyenda de la yerba mate.")],
 [3,MC("¿Cuál está bien escrita?",["llegué tarde porque llovía.","Llegué tarde porque llovía.","Llegué tarde porque llovía","llegué tarde porque llovía"],"Llegué tarde porque llovía.","Mayúscula al inicio y punto al final.")],
 [3,MC("\"Estudié toda la semana; ___, me fue mal.\" ¿Qué conector va?",["sin embargo","por eso","además","porque"],"sin embargo","El resultado es contrario a lo esperado.")],
 [3,MC("¿Qué se hace en el paso de revisar?",["Releer, corregir y mejorar","Elegir el tema","Tirar el texto","Copiar otro texto"],"Releer, corregir y mejorar","Es parte del proceso de escritura.")],
 [4,MC("¿Qué datos lleva una ficha bibliográfica?",["Autor, título, editorial y año","Solo el título","Color de tapa y precio","Cantidad de páginas y peso"],"Autor, título, editorial y año","Los cuatro datos básicos.")],
 [4,MC("¿Cómo se escribe el autor en la ficha?",["Ana Ríos","Ríos, Ana","ANA","Ríos"],"Ríos, Ana","Apellido, nombre.")],
 [4,VF("En el índice aparecen los capítulos del libro.","Verdadero","Muestra cómo está armado.")],
 [4,MC("¿Qué podés hacer si un libro no te engancha después de un buen rato?",["Dejarlo y elegir otro","Leerlo obligado","Dejar de leer","Romperlo"],"Dejarlo y elegir otro","Es un derecho del lector.")],
]
M={"subject_id":"e1b0726d-08aa-4d9e-9060-18489f529da2","tema":1,"practica":"Práctica general: volver a leer","examen_titulo":"Nivel jefe: volver a leer","niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-1.json"),"w"),ensure_ascii=False)
print("ok")
