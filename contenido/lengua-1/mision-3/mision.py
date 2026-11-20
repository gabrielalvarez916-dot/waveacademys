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

from matplotlib.patches import FancyBboxPatch
def fig_orden():
    fig, ax = plt.subplots(figsize=(7.2, 2.6)); ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 4.4)
    H=["Sale en bici","Llueve fuerte","Se cae","Despierta en el hospital"]; rel=[3,0,1,2]
    ax.text(0.1, 3.95, "Orden del relato", fontsize=9, color=V, weight="bold"); ax.text(0.1, 1.75, "Orden cronológico", fontsize=9, color=V, weight="bold")
    for k,i in enumerate(rel): ax.add_patch(FancyBboxPatch((0.2+k*3, 2.5), 2.6, 1.1, boxstyle="round,pad=0.05", fc=C, ec=O)); ax.text(1.5+k*3, 3.05, H[i], ha="center", va="center", fontsize=8, color=O)
    for i in range(4): ax.add_patch(FancyBboxPatch((0.2+i*3, 0.3), 2.6, 1.1, boxstyle="round,pad=0.05", fc="white", ec=O)); ax.text(1.5+i*3, 0.85, f"{i+1}. {H[i]}", ha="center", va="center", fontsize=8, color=O)
    return png(fig)
N1=NV("Vas a distinguir el orden cronológico del orden del relato y reconocer los recursos para jugar con el tiempo.",["Dos órdenes","Retrospección, anticipación e in medias res","Núcleos narrativos","Conectores temporales"],[
 S(1,"Dos órdenes",[D("Orden cronológico","Cómo pasaron los hechos, uno detrás de otro."),D("Orden del relato","Cómo el narrador decide contarlos."),IMG("Una historia, dos órdenes","El relato empieza por el final y vuelve atrás.","Cuatro tarjetas en el orden del relato y debajo las mismas en orden cronológico.",fig_orden())]),
 S(1,"Jugar con el tiempo",[T("Recursos",["Recurso","Qué hace","Ejemplo"],[["Retrospección","Vuelve al pasado","Tres horas antes, había salido en bici."],["Anticipación","Adelanta el futuro","Nunca imaginó que sería su última carrera."],["In medias res","Empieza en plena acción","—¡Corré! —gritó, mientras el puente se derrumbaba."]])]),
 S(2,"Núcleos narrativos",[P("Los <b>núcleos narrativos</b> son las acciones principales: si se quita una, la historia cambia o no se entiende. Las <b>acciones secundarias</b> (describir, detenerse en detalles) enriquecen el relato pero pueden quitarse sin romperlo.")]),
 S(2,"Conectores temporales",[T("Conectores",["Para…","Ejemplos"],[["Ir al pasado","años atrás, la noche anterior, tiempo antes"],["Hechos simultáneos","mientras, en ese momento"],["Avanzar","luego, más tarde, al día siguiente"],["Lo inesperado","de pronto, de repente, en ese instante"]])])],
 {"titulo":"reordenar","planteo":"\"Lucía despertó en el hospital. Tres horas antes había salido en bici. Se largó a llover y se cayó.\" Escribí el orden cronológico.","pasos":["1) Salió en bici.","2) Se largó a llover.","3) Se cayó.","4) Despertó en el hospital. El relato usa retrospección."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Empezar una historia en plena acción se llama in medias ___ .","\"Años atrás\" es un conector ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí el comienzo de un relato que empiece por el final y use una retrospección."},
 {"titulo":"Marcá los saltos","texto":"Cuando cambies de momento, avisale al lector con un conector temporal: así no se pierde."},
 ["Confundir el orden del relato con el cronológico.","Saltar en el tiempo sin conectores."],
 RS(("Dos órdenes","Cronológico y del relato."),("Recursos","Retrospección, anticipación, in medias res."),("Núcleos","Acciones principales."),("Conectores","Ubican en el tiempo.")),
 G(("Cronológico","Según el tiempo en que ocurrió."),("Retrospección","Vuelta al pasado en un relato."),("Anticipación","Adelanto de algo que pasará."),("In medias res","Comienzo en plena acción.")),
 ["\"Nunca imaginó que aquel mensaje le cambiaría la vida.\" ¿Retrospección o anticipación?","Una historia que empieza en plena persecución, ¿qué recurso usa?","\"Años atrás\": ¿lleva al pasado o al futuro?","¿Cómo se llaman las acciones principales de un relato?"],
 [["anticipacion","anticipación"],["in medias res"],["pasado","al pasado"],["nucleos narrativos","núcleos narrativos","nucleos","núcleos"]],
 {"incompleto":"Res. Temporal.","solo":"Respuesta personal: empieza por el final y vuelve atrás con un conector.","carpeta":["Anticipación.","In medias res.","Al pasado.","Núcleos narrativos."]})
N2=NV("Vas a usar el pretérito perfecto simple y el imperfecto para narrar.",["Las formas","Acción y fondo","Coherencia de tiempos"],[
 S(1,"Las formas",[T("Dos pasados",["Persona","Perfecto simple","Imperfecto"],[["Yo","caminé, tuve","caminaba, tenía"],["Vos","caminaste, tuviste","caminabas, tenías"],["Él / ella","caminó, tuvo","caminaba, tenía"],["Nosotros","caminamos, tuvimos","caminábamos, teníamos"],["Ellos","caminaron, tuvieron","caminaban, tenían"]])]),
 S(1,"Acción y fondo",[P("El <b>perfecto simple</b> expresa acciones puntuales y terminadas: son las que hacen <b>avanzar</b> la historia (abrió, gritó, corrió). El <b>imperfecto</b> pinta el <b>fondo</b>: descripciones, acciones que duraban o que se repetían (era de noche, llovía, siempre llegaba tarde)."),E("Fondo + acción","Era tarde y llovía cuando alguien golpeó la puerta.",["Era: imperfecto, describe.","Llovía: imperfecto, acción que duraba.","Golpeó: perfecto simple, la acción que irrumpe."])]),
 S(2,"Coherencia",[P("Un relato en pasado no salta al presente sin motivo: \"Entró y <b>ve</b> la carta\" es incorrecto; lo correcto es \"Entró y <b>vio</b> la carta\". Para lo que dura de fondo, imperfecto: \"mientras <b>leía</b>\", no \"mientras <b>leí</b>\".")])],
 {"titulo":"elegir","planteo":"Completá: \"Todos los veranos mi abuela (preparar) dulce de higos. Un día, el frasco (explotar).\"","pasos":["Todos los veranos: costumbre → preparaba (imperfecto).","Un día: acción puntual → explotó (perfecto simple)."]},
 {"titulo":"completar","planteo":"Completá con el pasado adecuado.","pasos":["Mientras ___ (cocinar), sonó el teléfono.","De pronto, la luz se ___ (apagar)."]},
 {"titulo":"tu turno","planteo":"Escribí un párrafo que empiece describiendo el lugar en imperfecto y siga con dos acciones en perfecto simple."},
 {"titulo":"Preguntá: ¿duraba o pasó?","texto":"Si duraba o se repetía, imperfecto. Si pasó de una vez y terminó, perfecto simple."},
 ["Saltar del pasado al presente.","Usar perfecto simple para lo que es fondo."],
 RS(("Perfecto simple","Acción que avanza."),("Imperfecto","Fondo y costumbre."),("Juntos","Fondo + acción."),("Coherencia","No saltar al presente.")),
 G(("Pretérito","Tiempo pasado."),("Perfecto simple","Pasado de acciones puntuales: cantó."),("Imperfecto","Pasado de fondo o costumbre: cantaba.")),
 ["Conjugá en perfecto simple: él (abrir).","Conjugá en imperfecto: nosotros (vivir).","\"Siempre llegaba tarde\": ¿perfecto simple o imperfecto?","Corregí: \"Entró y ve la carta\". Escribí solo el verbo correcto."],
 [["abrio","abrió"],["viviamos","vivíamos"],["imperfecto"],["vio"]],
 {"incompleto":"cocinaba. apagó.","solo":"Respuesta personal.","carpeta":["Abrió.","Vivíamos.","Imperfecto.","Vio."]})
N3=NV("Vas a enriquecer un relato con detalles: mostrar en vez de decir, los sentidos y palabras precisas.",["Mostrar, no decir","Los cinco sentidos","Palabras precisas"],[
 S(1,"Mostrar, no decir",[T("Decir y mostrar",["Dice","Muestra"],[["Tenía miedo.","Le temblaban las manos y no podía tragar."],["Estaba feliz.","Saltó del banco y abrazó a todos los que tenía cerca."],["Era una casa vieja.","Las persianas colgaban torcidas y el musgo trepaba por las paredes."]])]),
 S(1,"Los sentidos",[P("El detalle entra por los sentidos: <b>vista</b> (la luz amarilla del farol), <b>oído</b> (el crujido de la escalera), <b>olfato</b> (olor a tierra mojada), <b>tacto</b> (la baranda helada), <b>gusto</b> (un sabor a óxido).")]),
 S(2,"Palabras precisas",[T("Más precisión",["General","Preciso"],[["caminó despacio","se arrastró"],["una casa fea","una casa descascarada"],["dijo enojado","escupió"],["un ruido","un chirrido"]]),P("Poné el detalle en los momentos importantes; el resto, contalo rápido.")])],
 {"titulo":"reescribir","planteo":"Reescribí mostrando: \"Estaba aburrido en clase.\"","pasos":["Pienso qué hace alguien aburrido.","Elijo acciones y sentidos.","\"Dibujaba círculos en el margen y contaba los minutos que faltaban para el timbre.\""]},
 {"titulo":"completar","planteo":"Completá con una palabra más precisa.","pasos":["\"Hizo un ruido\" → hizo un ___ (de una puerta vieja).","\"Comió rápido\" → ___ la comida."]},
 {"titulo":"tu turno","planteo":"Describí en tu carpeta un lugar que conozcas usando al menos tres sentidos."},
 {"titulo":"Cerrá los ojos","texto":"Antes de escribir, imaginá la escena: qué se ve, qué se oye, a qué huele. Eso es lo que hay que contar."},
 ["Nombrar la emoción en lugar de mostrarla.","Describir todo con la misma intensidad."],
 RS(("Mostrar","No nombrar la emoción."),("Sentidos","Vista, oído, olfato, tacto, gusto."),("Precisión","Verbos y adjetivos justos."),("Dosis","Detalle donde importa.")),
 G(("Mostrar","Hacer ver la emoción con acciones y sensaciones."),("Sensorial","Que llega por los sentidos."),("Preciso","Exacto, justo para lo que se quiere decir.")),
 ["\"Tenía miedo\": ¿muestra o dice?","¿Qué sentido aparece en \"olor a tierra mojada\"?","Escribí un verbo más preciso para \"caminó despacio\".","¿Qué sentido aparece en \"la baranda helada\"?"],
 [["dice"],["olfato","el olfato"],["se arrastro","se arrastró","arrastro","arrastró","se arrastraba"],["tacto","el tacto"]],
 {"incompleto":"chirrido. Devoró.","solo":"Respuesta personal con tres sentidos.","carpeta":["Dice.","Olfato.","Se arrastró.","Tacto."]})
N4=NV("Vas a revisar y corregir un relato propio en cuatro pasadas.",["Las cuatro pasadas","Tiempos y repeticiones","El diálogo con raya"],[
 S(1,"Cuatro pasadas",[T("Revisión",["Pasada","Me pregunto"],[["Orden","¿Se entiende qué pasó y cuándo?"],["Tiempos verbales","¿Mantengo el pasado?"],["Repeticiones","¿Repito palabras? ¿Puedo usar sinónimos o pronombres?"],["Puntuación","¿Están bien los puntos, comas y diálogos?"]])]),
 S(1,"Un relato corregido",[T("Correcciones",["Antes","Después","Por qué"],[["Lucía entra al cuarto","Lucía entró al cuarto","Mantener el pasado"],["Lucía vio a Lucía en el espejo","Vio su reflejo en el espejo","Evitar la repetición"],["y entonces… y entonces","de pronto","Variar los conectores"]])]),
 S(2,"El diálogo",[P("Cada intervención va en <b>renglón nuevo</b> y empieza con <b>raya</b> (—). Si el narrador agrega algo, se separa con otra raya: —¿Hay alguien ahí? —preguntó Lucía."),P("Truco final: leé tu texto en voz alta. El oído encuentra errores que el ojo no ve.")])],
 {"titulo":"corregir","planteo":"Corregí: \"Juan abre la puerta. Juan ve una sombra y entonces grita y entonces corre.\"","pasos":["Tiempos: abrió, vio, gritó, corrió.","Repetición: Juan… él (o se omite).","Conectores: de pronto, enseguida.","\"Juan abrió la puerta. De pronto vio una sombra, gritó y salió corriendo.\""]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Cada intervención de un diálogo empieza con ___ .","Para no repetir un nombre puedo usar un ___ ."]},
 {"titulo":"tu turno","planteo":"En la actividad de este nivel vas a corregir un relato con errores: el tutor revisa tu versión y te da pistas."},
 {"titulo":"Una cosa por vez","texto":"No intentes corregir todo junto: una pasada por cada aspecto."},
 ["Revisar todo de una sola vez.","Usar guion corto (-) en lugar de raya en los diálogos."],
 RS(("Pasadas","Orden, tiempos, repeticiones, puntuación."),("Tiempos","Mantener el pasado."),("Repeticiones","Sinónimos y pronombres."),("Diálogos","Renglón nuevo y raya.")),
 G(("Revisar","Releer para mejorar."),("Raya","Signo (—) del diálogo."),("Sinónimo","Palabra de significado parecido.")),
 ["Corregí el verbo: \"Ayer Lucía entra al cuarto\". Escribí solo el verbo correcto.","¿Con qué signo empieza una intervención de diálogo: raya o comillas?","¿Qué se revisa en la segunda pasada?","Escribí un pronombre para no repetir \"Lucía\"."],
 [["entro","entró"],["raya","con raya"],["tiempos verbales","los tiempos verbales","tiempos","los tiempos"],["ella"]],
 {"incompleto":"Raya. Pronombre.","solo":"Respuesta personal con tres correcciones.","carpeta":["Entró.","Raya.","Los tiempos verbales.","Ella."]})
ACT={"1":[{"t":"ordering","p":"Ordená cronológicamente: \"Despertó en el hospital. Tres horas antes había salido en bici; se largó a llover y se cayó.\"","o":["Despertó en el hospital","Se cayó","Salió en bici","Se largó a llover"],"r":{"orden":["Salió en bici","Se largó a llover","Se cayó","Despertó en el hospital"]},"e":"El relato empieza por el final: es una retrospección."},
  {"t":"matching","p":"Uní cada recurso con su ejemplo.","o":{"izquierda":["Retrospección","Anticipación","In medias res"],"derecha":["Años atrás, había vivido en el sur.","Nunca imaginó que sería su último viaje.","—¡Corré! —gritó, mientras el puente caía."]},"r":{"pares":{"Retrospección":"Años atrás, había vivido en el sur.","Anticipación":"Nunca imaginó que sería su último viaje.","In medias res":"—¡Corré! —gritó, mientras el puente caía."}},"e":"Pasado, futuro y plena acción."}],
 "2":[{"t":"tap_text","p":"Clasificá los verbos: \"Era tarde y llovía cuando alguien golpeó la puerta y gritó.\"","o":{"segmentos":["Era","tarde","y","llovía","cuando","alguien","golpeó","la","puerta","y","gritó"],"modo":"palabras","categorias":["Imperfecto","Perfecto simple"]},"r":{"categorias":{"0":"Imperfecto","3":"Imperfecto","6":"Perfecto simple","10":"Perfecto simple"}},"e":"El imperfecto pinta el fondo; el perfecto simple, las acciones."},
  MC("\"Mientras ___, sonó el teléfono.\"",["cocinaba","cociné","cocino","cocinaré"],"cocinaba","Acción que duraba de fondo: imperfecto.")],
 "3":[
  MC("¿Cuál es la versión más precisa de \"hizo un ruido la puerta\"?",["La puerta chirrió","La puerta hizo un ruido feo","La puerta hizo mucho ruido","Hubo un ruido en la puerta"],"La puerta chirrió","Un verbo preciso reemplaza la frase general.")],
 "4":[{"t":"keywords","p":"Corregí este relato y escribilo bien: \"Juan abre la puerta. Juan ve una sombra y entonces grita y entonces corre. -¿Quién está ahí? pregunta Juan.\"","o":{"ayuda":"Revisá tiempos verbales, repeticiones, conectores y el diálogo con raya."},"r":"Versión corregida en pasado (abrió, vio, gritó, corrió, preguntó), sin repetir Juan, con conectores variados en lugar de y entonces, y el diálogo con raya: —¿Quién está ahí? —preguntó.","e":"Cuatro pasadas: orden, tiempos, repeticiones y puntuación."},
  MC("¿Cuál diálogo está bien escrito?",["—¿Quién es? —preguntó Lucía.","-¿Quién es? preguntó Lucía.","\"¿Quién es?\" —Lucía preguntó—","—¿Quién es? preguntó Lucía—"],"—¿Quién es? —preguntó Lucía.","Raya al inicio y antes de la voz del narrador.")],
 "5":[MC("Relámpago. Empezar en plena acción es…",["In medias res","Retrospección","Anticipación"],"In medias res","Se arranca en el medio.",tiempo=20),MC("Relámpago. \"Llovía\" está en…",["Imperfecto","Perfecto simple","Presente"],"Imperfecto","Fondo que dura.",tiempo=20),MC("Relámpago. \"Olor a pan tostado\" usa el sentido del…",["Olfato","Gusto","Tacto"],"Olfato","Se huele.",tiempo=20),MC("Relámpago. El diálogo se marca con…",["Raya","Paréntesis","Asterisco"],"Raya","—Así.",tiempo=20)]}
EXAMEN=[[1,MC("\"Tres horas antes, había salido en bici.\" ¿Qué recurso es?",["Retrospección","Anticipación","In medias res","Orden lineal"],"Retrospección","Vuelve al pasado.")],[1,MC("¿Qué son los núcleos narrativos?",["Las acciones principales que sostienen la historia","Las descripciones","Los diálogos","Los títulos"],"Las acciones principales que sostienen la historia","Si se quitan, la historia cambia.")],[1,VF("El orden del relato siempre coincide con el orden cronológico.","Falso","El narrador puede alterarlo.")],
 [2,MC("\"Era de noche y el viento ___ cuando la luz se ___.\"",["soplaba / apagó","sopló / apagaba","soplaba / apagaba","sopla / apaga"],"soplaba / apagó","Fondo en imperfecto, acción en perfecto simple.")],[2,MC("¿Qué expresa el imperfecto en un relato?",["El fondo, descripciones y costumbres","Solo acciones terminadas","El futuro","Órdenes"],"El fondo, descripciones y costumbres","El perfecto simple hace avanzar.")],[2,MC("¿Cuál tiene un error de tiempo verbal?",["Entró y ve la carta.","Entró y vio la carta.","Mientras leía, sonó el timbre.","Siempre llegaba tarde."],"Entró y ve la carta.","Salta al presente.")],
 [3,MC("¿Cuál muestra en lugar de decir?",["Se mordía las uñas y miraba el reloj","Estaba nervioso","Sentía nervios","Tenía muchos nervios"],"Se mordía las uñas y miraba el reloj","Muestra con acciones.")],[3,MC("\"El crujido de la escalera\" apela al…",["Oído","Tacto","Olfato","Gusto"],"Oído","Es un sonido.")],[3,VF("Conviene describir todo con el mismo nivel de detalle.","Falso","El detalle va en los momentos importantes.")],
 [4,MC("¿Qué se revisa en la pasada de repeticiones?",["Palabras repetidas que se pueden reemplazar","La raya del diálogo","El título","El tamaño de la letra"],"Palabras repetidas que se pueden reemplazar","Con sinónimos o pronombres.")],[4,MC("¿Cuál es la mejor corrección de \"y entonces grita y entonces corre\"?",["De pronto gritó y salió corriendo","Y entonces gritó y entonces corrió","Grita y corre","Entonces y gritó"],"De pronto gritó y salió corriendo","Pasado y conectores variados.")],[4,MC("¿Por qué conviene leer el texto en voz alta al revisarlo?",["El oído detecta errores que el ojo saltea","Para que lo escuche la familia","Porque es obligatorio","Para memorizarlo"],"El oído detecta errores que el ojo saltea","Es un truco de revisión.")],[4,VF("Cada intervención de un diálogo va en renglón nuevo con raya.","Verdadero","—Así se marca.")]]
M={"subject_id":"e1b0726d-08aa-4d9e-9060-18489f529da2","tema":3,"practica":"Práctica general: narrar con orden","examen_titulo":"Nivel jefe: narrar con orden","niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-3.json"),"w"),ensure_ascii=False); print("ok")
