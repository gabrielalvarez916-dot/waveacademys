# -*- coding: utf-8 -*-
"""Ciudadanía I y Ciudadanía I Argentina · Misiones 2 y 3 (VARIANTE)."""
import os, sys, json
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
SID = "a549d16a-c872-4df7-b243-e4b508bd8668"
# ============ MISIÓN 2: DEMOCRACIA Y AUTORITARISMOS ============
A1=NV("Vas a explicar qué caracteriza a una democracia y distinguir democracia directa y representativa.",["Qué es la democracia","Rasgos","Directa y representativa","Pluralismo"],[
 S(1,"Qué es la democracia",[D("Democracia","Forma de gobierno en la que el poder viene del pueblo, que elige a sus gobernantes y puede controlarlos."),P("La palabra viene del griego: <b>demos</b> (pueblo) y <b>kratos</b> (poder).")]),
 S(1,"Rasgos",[T("Qué caracteriza a una democracia",["Rasgo","Qué significa"],[["Elecciones libres","Se vota sin presiones y se cuentan bien los votos"],["División de poderes","Nadie concentra todo el poder"],["Derechos garantizados","Se respetan las libertades de todos"],["Alternancia","Los gobiernos cambian por el voto"],["Prensa libre","Se puede informar y criticar"]])]),
 S(2,"Directa y representativa",[T("Dos formas",["Forma","Cómo decide el pueblo"],[["Directa","Vota las decisiones él mismo"],["Representativa","Elige representantes que deciden"],["Semidirecta","Representantes más consulta popular o iniciativa"]]),P("Hoy la mayoría de los países son democracias representativas.")]),
 S(2,"Pluralismo",[PN("En democracia conviven ideas distintas y la mayoría gobierna respetando los derechos de las minorías. En la Argentina, por ejemplo, conviven muchos partidos y opiniones.","En democracia conviven ideas distintas y la mayoría gobierna respetando los derechos de las minorías. En cada país conviven muchos partidos y opiniones.")])],
 {"titulo":"identificar","planteo":"En un país nadie puede criticar al gobierno y las elecciones no tienen competencia. ¿Es una democracia?","pasos":["Sin prensa libre ni elecciones competitivas, falta el control.","El pueblo no puede cambiar a sus gobernantes.","No es una democracia plena."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Cuando los gobiernos cambian por el voto hay ___ .","Si el pueblo elige representantes, la democracia es ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí tres rasgos de la democracia y dá un ejemplo de cada uno."},
 {"titulo":"Control y cambio","texto":"En democracia el pueblo elige y también puede cambiar a sus gobernantes."},
 ["Creer que democracia es solo votar.","Pensar que la mayoría puede quitarle derechos a las minorías."],
 RS(("Democracia","El poder viene del pueblo."),("Rasgos","Elecciones libres, división de poderes."),("Formas","Directa y representativa."),("Pluralismo","Ideas distintas conviven.")),
 G(("Demos","Pueblo."),("Alternancia","Cambio de gobierno por el voto."),("Pluralismo","Convivencia de ideas distintas."),("Minoría","Grupo con menos votos o menos poder.")),
 ["¿Cómo se llama la forma de gobierno en que el poder viene del pueblo?","¿Qué democracia elige representantes: la directa o la representativa?","¿La prensa libre es un rasgo de la democracia? Respondé sí o no.","¿Cómo se llama el cambio de gobierno por el voto?"],
 [["democracia","la democracia"],["representativa","la representativa"],["si","sí"],["alternancia","la alternancia"]],
 {"incompleto":"Democracia. Alternancia.","solo":"Elecciones libres: se vota sin presiones. Alternancia: cambia el gobierno.","carpeta":["Democracia.","Representativa.","Sí.","Alternancia."]})
A2=NV("Vas a describir cómo funciona un régimen autoritario y cómo se diferencia de una democracia.",["Concentración del poder","Control de la información","Represión","Autoritarismo y totalitarismo"],[
 S(1,"Concentración del poder",[P("En un régimen autoritario el poder está concentrado en una persona, un grupo o un partido, y no hay controles reales sobre él. Las elecciones, si existen, no son libres ni competitivas.")]),
 S(1,"Control de la información",[T("Herramientas",["Herramienta","Para qué sirve"],[["Censura","Impedir que se publique lo que molesta al poder"],["Propaganda","Mostrar solo una versión favorable"],["Culto al líder","Presentar al jefe como infalible"],["Educación dirigida","Enseñar una sola visión"]])]),
 S(2,"Represión",[P("Quien critica puede ser perseguido, detenido o silenciado. Se limitan las libertades de reunión, expresión y asociación. A veces el propio Estado viola los derechos humanos.")]),
 S(2,"Autoritarismo y totalitarismo",[T("Diferencia de grado",["Régimen","Rasgo"],[["Autoritario","Limita la política y las libertades, pero deja algunos espacios privados"],["Totalitario","Quiere controlar toda la vida pública y privada"]])])],
 {"titulo":"comparar","planteo":"¿Qué diferencia hay entre censura y prensa libre?","pasos":["La censura prohíbe publicar lo que molesta al poder.","La prensa libre informa y critica sin permiso previo.","Una limita y la otra garantiza la libertad de expresión."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Impedir que se publique algo es la ___ .","En un régimen autoritario el poder está ___ en pocas manos."]},
 {"titulo":"tu turno","planteo":"Escribí tres diferencias entre una democracia y un régimen autoritario."},
 {"titulo":"Sin controles","texto":"Cuando nadie controla al poder, aparecen los abusos."},
 ["Pensar que un régimen autoritario siempre se reconoce por la violencia visible.","Creer que votar alcanza para que haya democracia."],
 RS(("Autoritario","Poder concentrado."),("Herramientas","Censura y propaganda."),("Represión","Persecución de críticos."),("Totalitario","Controla todo.")),
 G(("Censura","Prohibición de publicar."),("Propaganda","Difusión de una sola versión."),("Represión","Persecución o castigo de quien critica."),("Totalitarismo","Control de toda la vida.")),
 ["¿Cómo se llama la prohibición de publicar lo que molesta al poder?","¿Cómo se llama el régimen que quiere controlar toda la vida pública y privada?","¿En un régimen autoritario el poder está concentrado? Respondé sí o no.","¿Cómo se llama la difusión de una sola versión favorable?"],
 [["censura","la censura"],["totalitario","totalitarismo","el totalitarismo"],["si","sí"],["propaganda","la propaganda"]],
 {"incompleto":"Censura. Propaganda.","solo":"Democracia: prensa libre. Autoritarismo: censura.","carpeta":["Censura.","Totalitario.","Sí.","Propaganda."]})
A3=NV("Vas a explicar cómo alternaron democracias y dictaduras en el siglo XX y por qué las dictaduras violaron derechos humanos.",["Un siglo de cambios","Golpes de Estado","Terrorismo de Estado","Volver a la democracia"],[
 S(1,"Un siglo de cambios",[PN("En el siglo XX, la Argentina alternó gobiernos elegidos por voto con golpes de Estado y dictaduras militares. En 1976 comenzó la última, que duró hasta 1983.","En el siglo XX, muchos países de América Latina y de otras regiones alternaron gobiernos elegidos por voto con golpes de Estado y dictaduras. También hubo regímenes totalitarios en Europa, como el fascismo y el nazismo.")]),
 S(1,"Golpes de Estado",[D("Golpe de Estado","Toma del poder por la fuerza, fuera del procedimiento que fija la Constitución."),P("Quienes lo dan suelen suspender la Constitución, cerrar el Congreso y prohibir la actividad política.")]),
 S(2,"Terrorismo de Estado",[T("Qué hicieron las dictaduras más violentas",["Práctica","Qué significa"],[["Detención ilegal","Se llevaba a personas sin orden judicial"],["Tortura","Se maltrataba a los detenidos"],["Desaparición forzada","Se hacía desaparecer a personas sin dar noticias"],["Censura","Se prohibían libros, canciones y medios"]]),P("Esto se llama <b>terrorismo de Estado</b>: el propio Estado viola los derechos humanos.")]),
 S(2,"Volver a la democracia",[PN("En 1983 se recuperó la democracia en la Argentina. En 1985 se juzgó a los jefes militares en el Juicio a las Juntas, un hecho histórico para el mundo.","Muchos países recuperaron la democracia en las últimas décadas del siglo XX. Algunos crearon comisiones de la verdad y juzgaron a los responsables de las violaciones a los derechos humanos.")])],
 {"titulo":"explicar","planteo":"¿Por qué un golpe de Estado rompe la democracia?","pasos":["Toma el poder fuera de la Constitución.","Suspende elecciones y derechos.","El pueblo ya no elige a sus gobernantes."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Tomar el poder por la fuerza es un golpe de ___ .","Cuando el Estado viola los derechos humanos hay terrorismo de ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una breve explicación de por qué los derechos humanos deben protegerse siempre."},
 {"titulo":"Memoria","texto":"Recordar lo que pasó es una forma de evitar que se repita."},
 ["Pensar que una dictadura es solo un cambio de gobierno.","Creer que las violaciones de derechos fueron hechos aislados."],
 RS(("Siglo XX","Democracias y dictaduras."),("Golpe","Toma del poder por la fuerza."),("Terrorismo de Estado","El Estado viola derechos."),("Memoria y justicia","Recordar y juzgar.")),
 G(("Golpe de Estado","Toma ilegal del poder."),("Dictadura","Gobierno sin elecciones libres."),("Desaparición forzada","Hacer desaparecer a una persona."),("Memoria","Recordar para no repetir.")),
 ["¿Cómo se llama la toma del poder por la fuerza, fuera de la Constitución?","¿Cómo se llama que el propio Estado viole los derechos humanos: terrorismo de Estado o participación?","¿Una dictadura suspende las elecciones libres? Respondé sí o no.","¿Recordar lo ocurrido ayuda a evitar que se repita? Respondé sí o no."],
 [["golpe de estado","un golpe de estado","golpe"],["terrorismo de estado","el terrorismo de estado"],["si","sí"],["si","sí"]],
 {"incompleto":"Golpe. Estado.","solo":"Un golpe de Estado rompe la democracia porque el pueblo ya no elige.","carpeta":["Golpe de Estado.","Terrorismo de Estado.","Sí.","Sí."]})
A4=NV("Vas a explicar cómo se defiende la democracia hoy y qué papel tiene cada persona.",["Instituciones","Memoria y justicia","Información confiable","Participar"],[
 S(1,"Instituciones",[P("La democracia se defiende con <b>instituciones fuertes</b>: elecciones limpias, tribunales independientes, un Congreso que controle y una Constitución que se respete.")]),
 S(1,"Memoria y justicia",[PN("En la Argentina, el informe Nunca Más (1984) reunió las denuncias sobre las desapariciones. Memoria, verdad y justicia son pilares para sostener la democracia.","Muchos países crearon comisiones de la verdad y tribunales para investigar los crímenes de las dictaduras. Memoria, verdad y justicia son pilares para sostener la democracia.")]),
 S(2,"Información confiable",[T("Cuidar la información",["Hábito","Para qué sirve"],[["Contrastar fuentes","Evitar noticias falsas"],["Desconfiar de lo viral","No compartir sin verificar"],["Leer varias miradas","Entender mejor un tema"]])]),
 S(2,"Participar",[P("Una democracia se sostiene si las personas <b>participan</b>: votan, se informan, opinan con respeto, se organizan y denuncian los abusos.")])],
 {"titulo":"aplicar","planteo":"Te llega una noticia alarmante por una cadena de mensajes. ¿Qué hacés?","pasos":["No la compartas enseguida.","Buscá la misma noticia en medios confiables.","Si no aparece, es probable que sea falsa."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Memoria, verdad y ___ son pilares de la democracia.","Antes de compartir una noticia conviene ___ las fuentes."]},
 {"titulo":"tu turno","planteo":"Proponé tres acciones que una persona joven puede hacer para cuidar la democracia."},
 {"titulo":"Verificar","texto":"Antes de compartir, verificá."},
 ["Creer que la democracia se cuida sola.","Compartir noticias sin verificar."],
 RS(("Instituciones","Elecciones, justicia, Congreso."),("Memoria","Recordar para no repetir."),("Información","Contrastar fuentes."),("Participación","Votar y organizarse.")),
 G(("Institución","Organismo estable del Estado."),("Verdad","Conocer lo que ocurrió."),("Fuente","Origen de la información."),("Desinformación","Información falsa.")),
 ["¿Cómo se llaman los pilares: memoria, verdad y qué?","¿Qué conviene hacer con una noticia antes de compartirla: verificarla o ignorarla?","¿La democracia se cuida sola? Respondé sí o no.","¿Cómo se llama la información falsa que circula como si fuera verdadera?"],
 [["justicia","y justicia"],["verificarla","verificar","verificarla."],["no"],["desinformacion","desinformación","noticia falsa","noticias falsas"]],
 {"incompleto":"Justicia. Verificar.","solo":"Contrasto fuentes y no comparto lo viral sin verificar.","carpeta":["Justicia.","Verificarla.","No.","Desinformación."]})
ACT2={"1":[{"t":"matching","p":"Uní cada rasgo con su significado.","o":{"izquierda":["Elecciones libres","División de poderes","Alternancia","Prensa libre"],"derecha":["Se vota sin presiones","Nadie concentra el poder","El gobierno cambia por voto","Se puede informar y criticar"]},"r":{"pares":{"Elecciones libres":"Se vota sin presiones","División de poderes":"Nadie concentra el poder","Alternancia":"El gobierno cambia por voto","Prensa libre":"Se puede informar y criticar"}},"e":"Cada rasgo protege la democracia."},VF("Una democracia solo consiste en votar.","Falso","También requiere derechos, controles y libertades.")],
 "2":[MS("¿Cuáles son herramientas de un régimen autoritario?",["Censura","Propaganda","Elecciones competitivas","Culto al líder"],["Censura","Propaganda","Culto al líder"],"Las elecciones competitivas son democráticas."),FB("Impedir que se publique algo que molesta al poder es la ___ .",[["censura"]],"Censura.")],
 "3":[{"t":"ordering","p":"Ordená lo que ocurre con un golpe de Estado.","o":["Se suspenden las elecciones","Se toma el poder por la fuerza","Se limitan los derechos","Se cierra el Congreso"],"r":{"orden":["Se toma el poder por la fuerza","Se cierra el Congreso","Se suspenden las elecciones","Se limitan los derechos"]},"e":"Primero la fuerza, luego se anulan las instituciones."},VF("El terrorismo de Estado viola los derechos humanos.","Verdadero","Lo hace el propio Estado.")],
 "4":[{"t":"classify","p":"¿Ayuda o daña la democracia?","o":{"elementos":["Verificar una noticia","Compartir sin leer","Votar informado","Callar un abuso"],"categorias":["Ayuda","Daña"]},"r":{"categorias":{"Verificar una noticia":"Ayuda","Compartir sin leer":"Daña","Votar informado":"Ayuda","Callar un abuso":"Daña"}},"e":"La democracia se cuida participando."},TT("Tocá los pilares: «Memoria, verdad y justicia sostienen la democracia».",["Memoria,","verdad","y","justicia","sostienen","la","democracia"],[0,1,3],"Son los tres pilares.")],
 "5":[MC("Relámpago. Elegir representantes es una democracia…",["Representativa","Directa","Autoritaria"],"Representativa","Eligen quién decide.",tiempo=20),VF("Relámpago. La censura es un rasgo democrático.","Falso","Es autoritaria.",tiempo=20),MC("Relámpago. Tomar el poder por la fuerza es un…",["Golpe de Estado","Voto","Plebiscito"],"Golpe de Estado","Fuera de la Constitución.",tiempo=20),VF("Relámpago. Contrastar fuentes ayuda a evitar noticias falsas.","Verdadero","Verificar es clave.",tiempo=20)]}
EX2=[[1,MC("La democracia es la forma de gobierno en que el poder viene…",["Del pueblo","De un líder","De la fuerza","De un partido único"],"Del pueblo","Demos: pueblo.")],
 [1,MC("Un rasgo democrático es…",["Elecciones libres","Censura","Partido único","Culto al líder"],"Elecciones libres","Sin presiones.")],
 [1,VF("En democracia se respetan los derechos de las minorías.","Verdadero","Pluralismo.")],
 [2,MC("La censura es…",["Prohibir publicar lo que molesta al poder","Informar con libertad","Votar","Debatir"],"Prohibir publicar lo que molesta al poder","Limita la expresión.")],
 [2,MS("Rasgos de un régimen autoritario:",["Poder concentrado","Represión","Prensa libre","Propaganda"],["Poder concentrado","Represión","Propaganda"],"La prensa libre es democrática.")],
 [2,VF("En un régimen totalitario se controla toda la vida pública y privada.","Verdadero","Es su rasgo.")],
 [3,MC("Un golpe de Estado es…",["Tomar el poder por la fuerza","Una elección","Una ley","Una consulta"],"Tomar el poder por la fuerza","Fuera de la Constitución.")],
 [3,FB("Cuando el Estado viola los derechos humanos hay terrorismo de ___ .",[["estado"]],"Terrorismo de Estado.")],
 [3,VF("Las dictaduras suspenden las elecciones libres.","Verdadero","Anulan el voto del pueblo.")],
 [4,MC("Memoria, verdad y…",["Justicia","Poder","Censura","Silencio"],"Justicia","Son pilares.")],
 [4,MS("Cómo cuidar la democracia hoy:",["Verificar noticias","Participar","Votar informado","Compartir sin leer"],["Verificar noticias","Participar","Votar informado"],"Compartir sin leer la daña.")],
 [4,FB("La información falsa que circula como verdadera es ___ .",[["desinformacion","desinformación"]],"Desinformación.")],
 [4,VF("La democracia se cuida sola.","Falso","Requiere participación.")]]
M2={"subject_id":SID,"tema":2,"practica":"Práctica general: democracia y autoritarismos","examen_titulo":"Nivel jefe: democracia y autoritarismos","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT2,"examen":EX2}

# ============ MISIÓN 3: PARTICIPACIÓN SOCIAL Y POLÍTICA ============
B1=NV("Vas a distinguir formas de participación social y política, individual y colectiva.",["Qué es participar","Social y política","Individual y colectiva","Por qué importa"],[
 S(1,"Qué es participar",[D("Participación","Tomar parte en las decisiones y las acciones que afectan a la comunidad."),P("No se limita a votar: se puede participar en la escuela, el barrio, un club o en internet.")]),
 S(1,"Social y política",[T("Dos tipos",["Tipo","Ejemplo"],[["Social","Voluntariado, comedor barrial, cooperadora escolar"],["Política","Votar, afiliarse a un partido, presentarse a elecciones"]])]),
 S(2,"Individual y colectiva",[T("Dos modos",["Modo","Ejemplo"],[["Individual","Firmar una petición, votar, escribir una carta"],["Colectiva","Marcha, asamblea, centro de estudiantes"]])]),
 S(2,"Por qué importa",[P("Una comunidad donde las personas participan resuelve mejor sus problemas, controla a quienes gobiernan y fortalece la democracia.")])],
 {"titulo":"clasificar","planteo":"Organizar una campaña de limpieza del barrio: ¿participación social o política?","pasos":["No busca cargos ni decisiones de gobierno.","Mejora la vida de la comunidad.","Es participación social."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Votar es una forma de participación ___ .","Una marcha es una participación ___ ."]},
 {"titulo":"tu turno","planteo":"Contá una forma de participación que conozcas y explicá si es social o política."},
 {"titulo":"No solo votar","texto":"Participar es mucho más que votar."},
 ["Creer que participar es solo votar.","Pensar que la participación es solo de los adultos."],
 RS(("Participar","Tomar parte."),("Tipos","Social y política."),("Modos","Individual y colectiva."),("Importa","Fortalece la democracia.")),
 G(("Participación","Tomar parte en lo común."),("Voluntariado","Ayuda sin cobrar."),("Asamblea","Reunión para decidir en conjunto."),("Afiliarse","Inscribirse en un partido.")),
 ["¿Cómo se llama tomar parte en las decisiones y las acciones de la comunidad?","¿Un comedor barrial es participación social o política?","¿Participar es solo votar? Respondé sí o no.","¿Una marcha es una participación individual o colectiva?"],
 [["participacion","participación","la participacion","la participación"],["social","participacion social","participación social"],["no"],["colectiva","participacion colectiva","participación colectiva"]],
 {"incompleto":"Participación. Social.","solo":"Participo en la cooperadora de la escuela: es social y colectiva.","carpeta":["Participación.","Social.","No.","Colectiva."]})
B2=NV("Vas a explicar el voto, el derecho de petición y el derecho a la protesta pacífica.",["El voto","Petición","Protesta","Los límites"],[
 S(1,"El voto",[T("Características del voto democrático",["Característica","Significa"],[["Universal","Pueden votar todas las personas habilitadas"],["Igual","Cada voto vale lo mismo"],["Secreto","Nadie sabe qué votaste"],["Libre","Sin presiones"]]),PN("En la Argentina el voto es obligatorio desde los 18 años y optativo desde los 16 hasta los 17 años y después de los 70.","La edad mínima para votar y si el voto es obligatorio o voluntario cambian de un país a otro, pero en una democracia el voto debe ser universal, igual, secreto y libre.")]),
 S(1,"Petición",[D("Derecho de petición","Posibilidad de dirigirse por escrito a las autoridades para pedir algo o presentar un reclamo."),P("Las autoridades tienen que recibir el pedido y dar una respuesta.")]),
 S(2,"Protesta",[P("La <b>protesta pacífica</b> (marchas, asambleas, cortes de calle organizados) es una forma de expresar reclamos. Está protegida por los derechos de reunión y de expresión.")]),
 S(2,"Los límites",[P("La protesta pacífica no incluye violencia ni daño a otras personas. Los derechos de quienes protestan conviven con los de quienes no participan, y las autoridades deben cuidar a todos.")])],
 {"titulo":"relacionar","planteo":"Un grupo de vecinos junta firmas para pedir una plaza. ¿Qué derecho ejercen?","pasos":["Se dirigen a las autoridades.","Piden algo a nombre de la comunidad.","Ejercen el derecho de petición."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El voto en democracia debe ser universal, igual, secreto y ___ .","Las marchas pacíficas son una forma de ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un pedido corto a una autoridad sobre un problema de tu barrio."},
 {"titulo":"Pacífica","texto":"Un reclamo tiene más fuerza cuando se expresa sin violencia."},
 ["Pensar que votar es lo único que se puede hacer.","Creer que protestar autoriza a dañar a otros."],
 RS(("Voto","Universal, igual, secreto y libre."),("Petición","Pedir por escrito."),("Protesta","Pacífica."),("Límite","Sin violencia.")),
 G(("Voto secreto","Nadie sabe lo que elegiste."),("Petición","Pedido a las autoridades."),("Protesta","Manifestación de un reclamo."),("Firmas","Respaldo de personas a un pedido.")),
 ["¿Cómo se llama el voto que nadie puede conocer: secreto o público?","¿Cómo se llama el derecho de pedir algo a las autoridades?","¿La protesta pacífica es un derecho? Respondé sí o no.","¿Una protesta puede incluir violencia? Respondé sí o no."],
 [["secreto","el secreto"],["peticion","petición","derecho de peticion","derecho de petición"],["si","sí"],["no"]],
 {"incompleto":"Secreto. Petición.","solo":"Pido a la municipalidad más luz en mi cuadra.","carpeta":["Secreto.","Derecho de petición.","Sí.","No."]})
B3=NV("Vas a describir qué hacen las organizaciones y los movimientos sociales y por qué son importantes.",["Organizaciones","Tipos","Movimientos sociales","Cómo funcionan"],[
 S(1,"Organizaciones",[D("Organización social","Grupo organizado de personas que persigue un objetivo común, sin fines de lucro o con fines colectivos."),P("Aparecen cuando las personas se juntan para resolver un problema que no podrían resolver solas.")]),
 S(1,"Tipos",[T("Ejemplos",["Tipo","Qué hace"],[["Sindicato","Defiende los derechos de los trabajadores"],["Cooperativa","Produce o vende entre todos y reparte las ganancias"],["ONG","Trabaja en causas como salud, ambiente o educación"],["Centro de estudiantes","Representa a los alumnos"]])]),
 S(2,"Movimientos sociales",[PN("Un <b>movimiento social</b> es una acción colectiva sostenida que reclama un cambio. En la Argentina, las Madres de Plaza de Mayo, desde 1977, reclamaron por sus hijos desaparecidos y se volvieron un símbolo de derechos humanos.","Un <b>movimiento social</b> es una acción colectiva sostenida que reclama un cambio. En distintos países, movimientos por los derechos civiles, de las mujeres o del ambiente lograron cambiar leyes y costumbres.")]),
 S(2,"Cómo funcionan",[P("Las organizaciones se sostienen con reuniones, reglas claras, decisiones compartidas y objetivos que se pueden explicar a la comunidad.")])],
 {"titulo":"relacionar","planteo":"¿Qué diferencia hay entre una ONG y un sindicato?","pasos":["El sindicato defiende a los trabajadores de un sector.","La ONG se ocupa de una causa social más amplia.","Los dos son organizaciones, con fines distintos."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Una acción colectiva sostenida que reclama un cambio es un movimiento ___ .","La organización que defiende a los trabajadores es el ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí una organización o movimiento y explicá qué problema busca resolver."},
 {"titulo":"Juntos se logra","texto":"Lo que una persona sola no logra, un grupo organizado a veces sí."},
 ["Creer que las organizaciones solo existen para protestar.","Pensar que un movimiento social dura un día."],
 RS(("Organización","Grupo con objetivo común."),("Tipos","Sindicato, ONG, cooperativa."),("Movimiento","Acción colectiva sostenida."),("Funcionan","Con reglas y diálogo.")),
 G(("ONG","Organización no gubernamental."),("Sindicato","Agrupa a los trabajadores."),("Cooperativa","Trabajo compartido."),("Movimiento social","Acción colectiva que reclama cambios.")),
 ["¿Cómo se llama la organización que defiende los derechos de los trabajadores?","¿Cómo se llama una acción colectiva sostenida que reclama un cambio?","¿Una cooperativa reparte las ganancias entre sus miembros? Respondé sí o no.","¿Qué organización representa a los alumnos de una escuela?"],
 [["sindicato","el sindicato"],["movimiento social","un movimiento social","movimiento"],["si","sí"],["centro de estudiantes","el centro de estudiantes"]],
 {"incompleto":"Sindicato. Movimiento.","solo":"Una ONG ambiental busca cuidar los ríos de la zona.","carpeta":["Sindicato.","Movimiento social.","Sí.","Centro de estudiantes."]})
B4=NV("Vas a proponer formas de participación juvenil en tu escuela y tu comunidad.",["Jóvenes y derechos","Espacios","Participación digital","Un proyecto propio"],[
 S(1,"Jóvenes y derechos",[PN("Las personas jóvenes tienen derecho a opinar y a que su opinión se tenga en cuenta. En la Argentina, una ley reconoce los centros de estudiantes en las escuelas secundarias.","Las personas jóvenes tienen derecho a opinar y a que su opinión se tenga en cuenta. En muchos países existen centros de estudiantes y consejos juveniles en las escuelas y en los municipios.")]),
 S(1,"Espacios",[T("Dónde participar",["Espacio","Qué se puede hacer"],[["Centro de estudiantes","Proponer, organizar y representar"],["Consejos juveniles","Opinar sobre políticas para jóvenes"],["Voluntariado","Ayudar en causas de la comunidad"],["Clubes y grupos","Juntarse por intereses comunes"]])]),
 S(2,"Participación digital",[P("Internet permite informarse, difundir causas y organizarse. Pero también exige cuidado: verificar lo que se comparte, respetar a las demás personas y proteger los datos personales.")]),
 S(2,"Un proyecto propio",[T("Pasos para armar un proyecto",["Paso","Qué hacer"],[["1","Detectar un problema real"],["2","Escuchar a los afectados"],["3","Proponer acciones posibles"],["4","Buscar apoyo y organizarse"],["5","Evaluar qué resultó"]])])],
 {"titulo":"aplicar","planteo":"Querés mejorar el patio de la escuela. ¿Por dónde empezás?","pasos":["Hablás con compañeros y docentes para ver qué falta.","Proponés acciones concretas.","Presentás el pedido al centro de estudiantes o a la dirección."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un proyecto empieza detectando un ___ real.","Antes de compartir una causa en redes conviene ___ la información."]},
 {"titulo":"tu turno","planteo":"Escribí un proyecto de participación juvenil en cinco pasos para tu escuela."},
 {"titulo":"Empezar chico","texto":"Un buen proyecto empieza con un problema concreto y cercano."},
 ["Pensar que los jóvenes no pueden participar.","Creer que un proyecto necesita mucho dinero para empezar."],
 RS(("Derecho","Opinar y ser escuchados."),("Espacios","Centros, consejos, voluntariado."),("Digital","Informar con cuidado."),("Proyecto","Problema, acción, evaluación.")),
 G(("Participación juvenil","Acción de los jóvenes en lo común."),("Consejo juvenil","Espacio para opinar sobre políticas."),("Voluntariado","Ayuda sin cobrar."),("Proyecto","Plan para lograr algo.")),
 ["¿Cómo se llama el espacio que representa a los alumnos en la escuela secundaria?","¿Con qué empieza un proyecto de participación: con un problema real o con dinero?","¿Los jóvenes tienen derecho a opinar? Respondé sí o no.","¿Antes de compartir una causa en redes hay que verificar la información? Respondé sí o no."],
 [["centro de estudiantes","el centro de estudiantes"],["problema real","un problema real","un problema","problema"],["si","sí"],["si","sí"]],
 {"incompleto":"Problema. Verificar.","solo":"Propongo arreglar el patio: hablo con compañeros y presento el pedido.","carpeta":["Centro de estudiantes.","Un problema real.","Sí.","Sí."]})
ACT3={"1":[{"t":"classify","p":"¿Participación social o política?","o":{"elementos":["Votar","Voluntariado en un comedor","Afiliarse a un partido","Cooperadora escolar"],"categorias":["Social","Política"]},"r":{"categorias":{"Votar":"Política","Voluntariado en un comedor":"Social","Afiliarse a un partido":"Política","Cooperadora escolar":"Social"}},"e":"Según si busca decisiones de gobierno o ayudar a la comunidad."},VF("Participar es solo votar.","Falso","Hay muchas más formas.")],
 "2":[{"t":"matching","p":"Uní cada característica del voto con su significado.","o":{"izquierda":["Universal","Igual","Secreto","Libre"],"derecha":["Pueden votar todos los habilitados","Cada voto vale lo mismo","Nadie sabe qué elegiste","Sin presiones"]},"r":{"pares":{"Universal":"Pueden votar todos los habilitados","Igual":"Cada voto vale lo mismo","Secreto":"Nadie sabe qué elegiste","Libre":"Sin presiones"}},"e":"Así es el voto democrático."},FB("Pedir algo por escrito a las autoridades es el derecho de ___ .",[["peticion","petición"]],"Derecho de petición.")],
 "3":[MS("¿Cuáles son organizaciones sociales?",["Sindicato","Cooperativa","ONG","Un rumor"],["Sindicato","Cooperativa","ONG"],"Un rumor no es una organización."),{"t":"ordering","p":"Ordená cómo crece un movimiento social.","o":["Logra cambios","Un grupo detecta un problema","Se organiza y suma apoyo","Reclama de forma sostenida"],"r":{"orden":["Un grupo detecta un problema","Se organiza y suma apoyo","Reclama de forma sostenida","Logra cambios"]},"e":"Se construye en etapas."}],
 "4":[TT("Tocá los espacios de participación: «El centro de estudiantes y el voluntariado son espacios para participar».",["El","centro","de","estudiantes","y","el","voluntariado","son","espacios","para","participar"],[1,2,3,6],"Son espacios de participación."),{"t":"ordering","p":"Ordená los pasos de un proyecto.","o":["Evaluar","Escuchar a los afectados","Detectar un problema","Proponer acciones"],"r":{"orden":["Detectar un problema","Escuchar a los afectados","Proponer acciones","Evaluar"]},"e":"De la detección a la evaluación."}],
 "5":[MC("Relámpago. Votar es participación…",["Política","Solo social","Ninguna"],"Política","Decide autoridades.",tiempo=20),VF("Relámpago. La protesta pacífica es un derecho.","Verdadero","Sin violencia.",tiempo=20),MC("Relámpago. El sindicato defiende a…",["Trabajadores","Alumnos","Vecinos"],"Trabajadores","Es su función.",tiempo=20),VF("Relámpago. Los jóvenes no pueden participar.","Falso","Tienen derecho.",tiempo=20)]}
EX3=[[1,MC("Participar es…",["Tomar parte en las decisiones y acciones de la comunidad","Solo votar","Obedecer","Mirar"],"Tomar parte en las decisiones y acciones de la comunidad","Hay muchas formas.")],
 [1,MC("Un voluntariado es participación…",["Social","Solo política","Ninguna","Individual obligatoria"],"Social","Ayuda a la comunidad.")],
 [1,VF("Una marcha es una participación colectiva.","Verdadero","Participan muchas personas.")],
 [2,MC("Un voto secreto significa que…",["Nadie sabe qué elegiste","Todos lo ven","Vale doble","Es obligatorio"],"Nadie sabe qué elegiste","Protege la libertad.")],
 [2,FB("El derecho de pedir algo por escrito a las autoridades es el derecho de ___ .",[["peticion","petición"]],"Derecho de petición.")],
 [2,VF("La protesta pacífica puede incluir violencia.","Falso","Debe ser pacífica.")],
 [3,MC("El sindicato defiende…",["A los trabajadores","A los clientes","A los turistas","A los jueces"],"A los trabajadores","Es su función.")],
 [3,MS("Son organizaciones sociales:",["Sindicato","ONG","Cooperativa","Un rumor"],["Sindicato","ONG","Cooperativa"],"Un rumor no lo es.")],
 [3,VF("Un movimiento social es una acción colectiva sostenida que reclama un cambio.","Verdadero","Dura en el tiempo.")],
 [4,MC("Un proyecto de participación empieza con…",["Un problema real","Mucho dinero","Una orden","Un premio"],"Un problema real","Cercano y concreto.")],
 [4,MC("El centro de estudiantes…",["Representa a los alumnos","Dicta leyes","Reemplaza a la escuela","Elige presidentes"],"Representa a los alumnos","Es su función.")],
 [4,FB("Antes de compartir una causa en redes hay que ___ la información.",[["verificar"]],"Evitar la desinformación.")],
 [4,VF("Los jóvenes tienen derecho a opinar.","Verdadero","Y a que se los escuche.")]]
M3={"subject_id":SID,"tema":3,"practica":"Práctica general: participación social y política","examen_titulo":"Nivel jefe: participación social y política","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT3,"examen":EX3}
for n,m in ((2,M2),(3,M3)):
    os.makedirs(os.path.join(AQUI,f"mision-{n}"),exist_ok=True); json.dump(m,open(os.path.join(AQUI,f"mision-{n}",f"mision-{n}.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={(2,1):"cbf73469-7fd7-400c-9f9a-698aa189cd3c",(2,2):"159aff8d-7ce3-42a3-8a70-cca5fb91edde",(2,3):"55fbfdeb-3bf9-4eae-8ed3-0ce588bc4269",(2,4):"ebff990b-e8eb-4a07-a8c3-6702538c679f",(3,1):"423aae9f-34bc-4f1a-924d-1a5bdea283b8",(3,2):"5d066a00-74c1-4b95-b4d3-0fac873b8035",(3,3):"1e85d51b-9043-488d-9fb8-f87dc83685fb",(3,4):"450a5465-9bdc-4dba-b4ab-fc7cfdd02e5a"}
TIT={(2,1):"Qué caracteriza a una democracia",(2,2):"Cómo funciona un régimen autoritario",(2,3):"Democracias y dictaduras del siglo XX",(2,4):"Cómo se defiende la democracia hoy",(3,1):"Formas de participar",(3,2):"Voto, petición y protesta",(3,3):"Organizaciones y movimientos sociales",(3,4):"Participación juvenil"}
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
CLS={(2,1):[
 RET("¿Cómo se llama la forma de gobierno en que el poder viene del pueblo?",6,"Democracia","🗳️","QUÉ CARACTERIZA","a una democracia",["Desafío: ¿cómo se llama la forma de gobierno en que el poder viene del pueblo? Seis segundos.","Democracia.","Hoy: *qué caracteriza a una democracia*."]),
 DEF("Democracia","El poder viene del pueblo","🗳️",["La *democracia* es la forma de gobierno en que el poder viene del pueblo.","*Demos* es pueblo y *kratos* es poder."]),
 TB("RASGOS",["Rasgo","Qué significa"],[["Elecciones libres","Sin presiones"],["División de poderes","Nadie concentra"],["Derechos","Se respetan"],["Alternancia","Cambia el gobierno"]],["Los rasgos de una democracia.","*Elecciones libres*: sin presiones.","*División de poderes*: nadie concentra.","*Derechos* garantizados.","Y *alternancia*."]),
 CMP(("DIRECTA","El pueblo vota cada decisión","🙋"),("REPRESENTATIVA","El pueblo elige representantes","🏛️"),"vs",["Dos formas de democracia.","En la *directa* el pueblo decide.","En la *representativa* elige quién decide."]),
 CL([("DEMOCRÁTICO","🗳️"),("NO DEMOCRÁTICO","🚫")],[("Prensa libre",0),("Censura",1),("Elecciones libres",0),("Partido único",1)],["¿Democrático o no?","*Prensa libre* y *elecciones libres*: democráticos.","*Censura* y *partido único*: no democráticos."]),
 Q("¿Qué democracia elige representantes?",["Representativa","Directa","Autoritaria"],0,["Te toca: ¿qué democracia elige representantes?","¿Representativa, directa o autoritaria?","La *representativa*."]),
 ER([("Democracia es solo votar","También derechos y controles"),("La mayoría puede quitar derechos","Las minorías se respetan")],["Errores típicos.","Creer que democracia es *solo votar*.","Y que la mayoría puede *quitar derechos*."]),
 RES(["Repasemos.","En democracia el poder viene del *pueblo*.","Hay *elecciones libres* y *división de poderes*.","Puede ser *directa* o *representativa*.","Y respeta el *pluralismo*.","¡Clase terminada! Ahora, *a practicar*."],[["DEMOCRACIA","poder del pueblo"],["RASGOS","elecciones libres"],["FORMAS","directa, representativa"],["PLURALISMO","ideas distintas"]])],
(2,2):[
 NOT("SIN PRENSA","Un diario no puede publicar","El gobierno decide qué se dice","🗞️","RÉGIMEN AUTORITARIO","cómo funciona",["Noticia: un diario no puede publicar.","El gobierno decide qué se dice.","Hoy: *cómo funciona un régimen autoritario*."]),
 DEF("Régimen autoritario","Poder concentrado y sin controles","🔒",["Un *régimen autoritario* concentra el poder en pocas manos.","Y no tiene controles reales."]),
 TB("HERRAMIENTAS",["Herramienta","Para qué"],[["Censura","Prohibir publicar"],["Propaganda","Una sola versión"],["Culto al líder","Líder infalible"],["Represión","Perseguir críticos"]],["Las herramientas del autoritarismo.","La *censura* prohíbe publicar.","La *propaganda* muestra una sola versión.","El *culto al líder*.","Y la *represión*."]),
 CMP(("AUTORITARIO","Limita la política y las libertades","🔒"),("TOTALITARIO","Quiere controlar toda la vida","🕸️"),"vs",["Dos grados.","El *autoritario* limita la política.","El *totalitario* quiere controlar toda la vida."]),
 CL([("DEMOCRACIA","🗳️"),("AUTORITARISMO","🔒")],[("Prensa libre",0),("Censura",1),("Alternancia",0),("Represión",1)],["¿De cuál es?","*Prensa libre* y *alternancia*: democracia.","*Censura* y *represión*: autoritarismo."]),
 Q("Impedir que se publique algo es…",["Censura","Alternancia","Petición"],0,["Te toca: impedir que se publique algo.","¿Censura, alternancia o petición?","*Censura*."]),
 ER([("Siempre se reconoce por la violencia visible","A veces es silencioso"),("Votar alcanza","Faltan libertades y controles")],["Errores típicos.","Creer que siempre se ve la *violencia*.","Y que *votar alcanza*."]),
 RES(["Repasemos.","El poder está *concentrado*.","Usa *censura* y *propaganda*.","Hay *represión*.","El *totalitarismo* quiere controlar todo.","¡Clase terminada! Ahora, *a practicar*."],[["PODER","concentrado"],["CENSURA","prohibir publicar"],["REPRESIÓN","perseguir"],["TOTALITARIO","controla todo"]])],
(2,3):[
 {"t":"gancho","grande":"Un siglo","emoji":"⏳","final":"de democracias y dictaduras","titulo":"DEMOCRACIAS Y DICTADURAS","sub":"del siglo XX","voz":["El siglo veinte alternó votos y golpes de Estado.","Muchos países vivieron las dos cosas.","Hoy: *democracias y dictaduras del siglo veinte*."]},
 DEF("Golpe de Estado","Toma del poder por la fuerza","🪖",["Un *golpe de Estado* es tomar el poder por la fuerza.","Fuera de lo que fija la Constitución."]),
 PA("QUÉ HACE UN GOLPE",[("Toma el poder","🪖"),("Cierra el Congreso","🏛️"),("Suspende elecciones","🗳️"),("Limita derechos","🔒")],["Cómo avanza un golpe.","Toma el *poder*.","Cierra el *Congreso*.","Suspende las *elecciones*.","Y limita los *derechos*."]),
 TB("TERRORISMO DE ESTADO",["Práctica","Qué es"],[["Detención ilegal","Sin orden judicial"],["Tortura","Maltrato"],["Desaparición","Sin noticias"],["Censura","Se prohíbe"]],["Terrorismo de Estado.","*Detención ilegal*: sin orden judicial.","*Tortura*: maltrato.","*Desaparición forzada*.","Y *censura*."]),
 DEF("Memoria","Recordar para no repetir","🕯️",["La *memoria* es recordar lo ocurrido.","Ayuda a que no se repita."]),
 Q("Cuando el Estado viola los derechos humanos hay…",["Terrorismo de Estado","Alternancia","Participación"],0,["Te toca: el Estado viola los derechos humanos.","¿Terrorismo de Estado, alternancia o participación?","*Terrorismo de Estado*."]),
 ER([("Dictadura es solo otro gobierno","Anula la voluntad del pueblo"),("Fueron hechos aislados","Fueron sistemáticos")],["Errores típicos.","Creer que una dictadura es *solo otro gobierno*.","Y que las violaciones fueron *hechos aislados*."]),
 RES(["Repasemos.","Un *golpe de Estado* rompe la democracia.","Las dictaduras *suspenden* elecciones.","El *terrorismo de Estado* viola derechos.","Y la *memoria* ayuda a evitar que se repita.","¡Clase terminada! Ahora, *a practicar*."],[["GOLPE","toma el poder"],["DICTADURA","sin elecciones"],["TERRORISMO","viola derechos"],["MEMORIA","no repetir"]])],
(2,4):[
 RET("Te llega una noticia alarmante por chat. ¿Qué hacés primero?",8,"Verificarla","📱","DEFENDER LA DEMOCRACIA","hoy",["Desafío: te llega una noticia alarmante por chat. ¿Qué hacés primero? Ocho segundos.","Verificarla.","Hoy: *cómo se defiende la democracia hoy*."]),
 DEF("Instituciones","Organismos estables del Estado","🏛️",["La democracia se defiende con *instituciones fuertes*.","Elecciones limpias, justicia independiente y Congreso."]),
 PA("TRES PILARES",[("Memoria","🕯️"),("Verdad","🔎"),("Justicia","⚖️")],["Tres pilares.","La *memoria*.","La *verdad*.","Y la *justicia*."]),
 TB("CUIDAR LA INFORMACIÓN",["Hábito","Sirve para"],[["Contrastar fuentes","Evitar falsas"],["No compartir viral","Frenar bulos"],["Leer varias miradas","Entender mejor"]],["Hábitos para informarse.","*Contrastar fuentes*.","No compartir lo *viral* sin verificar.","Y leer *varias miradas*."]),
 CL([("AYUDA","✅"),("DAÑA","❌")],[("Votar informado",0),("Compartir sin leer",1),("Participar",0),("Callar un abuso",1)],["¿Ayuda o daña?","*Votar informado* y *participar*: ayudan.","*Compartir sin leer* y *callar un abuso*: dañan."]),
 Q("Antes de compartir una noticia conviene…",["Verificarla","Reenviarla","Ignorarla"],0,["Te toca: antes de compartir una noticia.","¿Verificarla, reenviarla o ignorarla?","*Verificarla*."]),
 ER([("La democracia se cuida sola","Requiere participación"),("Compartir sin verificar","Contrastar antes")],["Errores típicos.","Creer que la democracia *se cuida sola*.","Y *compartir* sin verificar."]),
 RES(["Repasemos.","Hacen falta *instituciones fuertes*.","Memoria, verdad y *justicia*.","*Información* confiable.","Y *participación* de todos.","¡Clase terminada! Ahora, *a practicar*."],[["INSTITUCIONES","fuertes"],["PILARES","memoria, verdad, justicia"],["INFORMACIÓN","verificar"],["PARTICIPAR","entre todos"]])],
(3,1):[
 {"t":"gancho","grande":"Más que votar","emoji":"🙋","final":"participar es todo lo que hacemos juntos","titulo":"FORMAS DE PARTICIPAR","sub":"social y política","voz":["¿Participar es solo votar?","No: hay muchas formas.","Hoy: *formas de participar*."]},
 DEF("Participación","Tomar parte en lo común","🙋",["La *participación* es tomar parte en las decisiones y acciones de la comunidad.","Se puede en la escuela, el barrio o internet."]),
 CMP(("SOCIAL","Ayudar a la comunidad","🤲"),("POLÍTICA","Influir en el gobierno","🗳️"),"vs",["Dos tipos de participación.","La *social* ayuda a la comunidad.","La *política* influye en el gobierno."]),
 CL([("SOCIAL","🤲"),("POLÍTICA","🗳️")],[("Voluntariado",0),("Votar",1),("Cooperadora",0),("Afiliarse a partido",1)],["¿Social o política?","*Voluntariado* y *cooperadora*: social.","*Votar* y *afiliarse*: política."]),
 CMP(("INDIVIDUAL","Una persona sola","👤"),("COLECTIVA","Muchas juntas","👥"),"vs",["Otra diferencia.","*Individual*: una sola persona.","*Colectiva*: muchas personas juntas."]),
 Q("Un comedor barrial es participación…",["Social","Política","Ninguna"],0,["Te toca: un comedor barrial.","¿Social, política o ninguna?","*Social*."]),
 ER([("Participar es solo votar","Hay muchas formas"),("Es cosa de adultos","Es de todos")],["Errores típicos.","Creer que participar es *solo votar*.","Y que es *cosa de adultos*."]),
 RES(["Repasemos.","Participar es *tomar parte*.","Puede ser *social* o *política*.","*Individual* o *colectiva*.","Y *fortalece* la democracia.","¡Clase terminada! Ahora, *a practicar*."],[["PARTICIPAR","tomar parte"],["TIPOS","social y política"],["MODOS","individual, colectiva"],["IMPORTA","democracia"]])],
(3,2):[
 RET("¿Qué voto es el que nadie puede conocer?",5,"El voto secreto","🗳️","VOTO, PETICIÓN","y protesta",["Desafío: ¿qué voto es el que nadie puede conocer? Cinco segundos.","El voto secreto.","Hoy: *voto, petición y protesta*."]),
 TB("EL VOTO",["Rasgo","Significa"],[["Universal","Todos los habilitados"],["Igual","Vale lo mismo"],["Secreto","Nadie sabe"],["Libre","Sin presiones"]],["Cómo es el voto democrático.","*Universal*: todos los habilitados.","*Igual*: todos valen lo mismo.","*Secreto*: nadie sabe qué votaste.","Y *libre*."]),
 DEF("Petición","Pedir por escrito a las autoridades","✉️",["El *derecho de petición* es pedir algo por escrito a las autoridades.","Tienen que responder."]),
 DEF("Protesta pacífica","Expresar un reclamo sin violencia","📢",["La *protesta pacífica* es expresar un reclamo sin violencia.","Está protegida por la libertad de expresión."]),
 CL([("PACÍFICA","🕊️"),("NO PACÍFICA","🚫")],[("Marcha organizada",0),("Daño a otros",1),("Asamblea",0),("Agresión",1)],["¿Pacífica o no?","*Marcha organizada* y *asamblea*: pacíficas.","*Daño* y *agresión*: no lo son."]),
 Q("El derecho de pedir algo por escrito es el derecho de…",["Petición","Censura","Voto"],0,["Te toca: pedir algo por escrito.","¿Petición, censura o voto?","*Petición*."]),
 ER([("Votar es lo único que se puede hacer","Hay más formas"),("Protestar autoriza dañar","Debe ser pacífica")],["Errores típicos.","Creer que *votar* es lo único.","Y que *protestar* autoriza a dañar."]),
 RES(["Repasemos.","El voto es *universal*, *igual*, *secreto* y *libre*.","La *petición* pide a las autoridades.","La *protesta* es pacífica.","Y tiene *límites*.","¡Clase terminada! Ahora, *a practicar*."],[["VOTO","secreto y libre"],["PETICIÓN","por escrito"],["PROTESTA","pacífica"],["LÍMITE","sin violencia"]])],
(3,3):[
 NOT("BARRIO","Vecinos arman una cooperativa","Compran juntos y reparten ganancias","🏘️","ORGANIZACIONES","y movimientos sociales",["Noticia: vecinos arman una cooperativa.","Compran juntos y reparten ganancias.","Hoy: *organizaciones y movimientos sociales*."]),
 DEF("Organización social","Grupo organizado con un objetivo común","🤝",["Una *organización social* es un grupo organizado con un objetivo común.","Aparece cuando solos no podemos resolver un problema."]),
 TB("TIPOS",["Tipo","Qué hace"],[["Sindicato","Defiende trabajadores"],["Cooperativa","Trabajo compartido"],["ONG","Causas sociales"],["Centro de estudiantes","Representa alumnos"]],["Tipos de organizaciones.","El *sindicato* defiende a los trabajadores.","La *cooperativa* comparte el trabajo.","La *ONG* trabaja una causa.","Y el *centro de estudiantes* representa a los alumnos."]),
 DEF("Movimiento social","Acción colectiva que reclama cambios","✊",["Un *movimiento social* es una acción colectiva sostenida.","Reclama un cambio."]),
 CL([("ORGANIZACIÓN","🤝"),("MOVIMIENTO","✊")],[("Sindicato",0),("Reclamo sostenido",1),("ONG",0),("Cambio de leyes",1)],["¿Organización o movimiento?","*Sindicato* y *ONG*: organizaciones.","*Reclamo sostenido* y *cambio de leyes*: movimiento."]),
 Q("¿Qué defiende un sindicato?",["Trabajadores","Alumnos","Vecinos"],0,["Te toca: ¿qué defiende un sindicato?","¿Trabajadores, alumnos o vecinos?","A los *trabajadores*."]),
 ER([("Solo existen para protestar","También proponen y ayudan"),("Un movimiento dura un día","Es sostenido")],["Errores típicos.","Creer que existen *solo para protestar*.","Y que un movimiento *dura un día*."]),
 RES(["Repasemos.","Una *organización* tiene un objetivo común.","Hay *sindicatos*, *ONG* y *cooperativas*.","Un *movimiento* reclama cambios.","Y funcionan con *reglas* y diálogo.","¡Clase terminada! Ahora, *a practicar*."],[["ORGANIZACIÓN","objetivo común"],["TIPOS","sindicato, ONG"],["MOVIMIENTO","reclama cambios"],["FUNCIONAN","con reglas"]])],
(3,4):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"El patio está hecho un desastre 😩"},{"yo":True,"txt":"¿Y si lo proponemos al centro?"},{"yo":False,"txt":"¿Y eso sirve? 🤔"}],"titulo":"PARTICIPACIÓN JUVENIL","sub":"en tu escuela","voz":["Lu dice que el patio está hecho un desastre.","Juan: ¿y si lo proponemos al centro de estudiantes?","Lu: ¿y eso sirve?","Hoy: *participación juvenil*."]},
 DEF("Participación juvenil","Los jóvenes opinan y deciden","🧑‍🎓",["Los jóvenes tienen derecho a *opinar*.","Y a que su opinión se tenga en cuenta."]),
 TB("ESPACIOS",["Espacio","Qué hacer"],[["Centro de estudiantes","Proponer"],["Consejos juveniles","Opinar"],["Voluntariado","Ayudar"],["Clubes","Juntarse"]],["Dónde participar.","En el *centro de estudiantes*.","En *consejos juveniles*.","En el *voluntariado*.","Y en *clubes*."]),
 PA("UN PROYECTO",[("Detectar un problema","🔎"),("Escuchar a los afectados","👂"),("Proponer acciones","💡"),("Evaluar","✅")],["Un proyecto en pasos.","*Detectá* un problema.","*Escuchá* a los afectados.","*Proponé* acciones.","Y *evaluá*."]),
 CL([("CON CUIDADO","⚠️"),("SIN CUIDADO","❌")],[("Verificar datos",0),("Pasar tus datos",1),("Respetar a otros",0),("Difundir rumores",1)],["En redes, ¿con cuidado o sin cuidado?","*Verificar datos* y *respetar*: con cuidado.","*Pasar tus datos* y *difundir rumores*: sin cuidado."]),
 Q("Un proyecto de participación empieza con…",["Un problema real","Dinero","Una orden"],0,["Te toca: un proyecto empieza con...","¿Un problema real, dinero o una orden?","Un *problema real*."]),
 ER([("Los jóvenes no pueden participar","Tienen derecho"),("Hace falta mucho dinero","Se empieza con lo cercano")],["Errores típicos.","Creer que los jóvenes *no pueden*.","Y que hace falta *mucho dinero*."]),
 RES(["Repasemos.","Los jóvenes tienen *derecho a opinar*.","Hay *espacios* para participar.","En redes, *verificá* y respetá.","Y un proyecto parte de un *problema real*.","¡Clase terminada! Ahora, *a practicar*."],[["DERECHO","opinar"],["ESPACIOS","centros, consejos"],["REDES","con cuidado"],["PROYECTO","problema real"]])]}
for (m,n),es in CLS.items():
    json.dump({"sin_variante":True,"slug":f"ciud1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Ciudadanía I","titulo":TIT[(m,n)],"sub":f"Ciudadanía I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"ciud1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
