# -*- coding: utf-8 -*-
"""Ciudadanía I y Ciudadanía I Argentina · Misiones 4 y 5 (VARIANTE)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
sys.path.insert(0, AQUI)
from practica import P as PRACTICA
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}

FB=lambda p,h,e,**k:{"t":"fill_blank","p":p,"o":[],"r":{"huecos":h},"e":e,**k}
MS=lambda p,o,c,e,**k:{"t":"multi_select","p":p,"o":o,"r":{"correctas":c},"e":e,**k}
TT=lambda p,seg,tocar,e,**k:{"t":"tap_text","p":p,"o":{"segmentos":seg,"modo":"palabras"},"r":{"tocar":tocar},"e":e,**k}
KW=lambda p,ayuda,ref,e,**k:{"t":"keywords","p":p,"o":{"ayuda":ayuda},"r":ref,"e":e,**k}
SID = "a549d16a-c872-4df7-b243-e4b508bd8668"
# ============ MISIÓN 4: PARTIDOS POLÍTICOS Y ELECCIONES ============
A1=NV("Vas a explicar qué hace un partido político y por qué son importantes en una democracia.",["Qué es un partido","Funciones","Programa e ideología","Oposición y gobierno"],[
 S(1,"Qué es un partido",[D("Partido político","Organización de ciudadanos que comparte ideas y busca llegar al gobierno o influir en él mediante elecciones.")]),
 S(1,"Funciones",[T("Qué hacen",["Función","En qué consiste"],[["Representar","Llevar a las instituciones las demandas de sectores de la sociedad"],["Proponer","Presentar un programa de gobierno"],["Competir","Presentar candidatos en las elecciones"],["Formar","Capacitar a militantes y futuros dirigentes"],["Controlar","Vigilar a quienes gobiernan, si están en la oposición"]])]),
 S(2,"Programa e ideología",[P("Cada partido tiene una <b>ideología</b> (una forma de ver la sociedad) y una <b>plataforma</b> (lo que promete hacer). Los votantes comparan plataformas antes de elegir.")]),
 S(2,"Oposición y gobierno",[PN("Quien gana las elecciones gobierna; los demás partidos forman la <b>oposición</b>, que controla, critica y propone alternativas. En la Argentina existen partidos nacionales y también partidos de distrito, que actúan en una provincia.","Quien gana las elecciones gobierna; los demás partidos forman la <b>oposición</b>, que controla, critica y propone alternativas. En cada país existen partidos nacionales y también partidos regionales o locales.")])],
 {"titulo":"relacionar","planteo":"¿Por qué una democracia con un solo partido permitido no es plena?","pasos":["Los votantes no pueden elegir entre propuestas distintas.","No hay oposición que controle.","Falta el pluralismo."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Lo que un partido promete hacer es su ___ .","Los partidos que no gobiernan forman la ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí una función de los partidos y explicá por qué es importante."},
 {"titulo":"Comparar propuestas","texto":"Antes de votar, compará las plataformas de los partidos."},
 ["Creer que todos los partidos piensan igual.","Pensar que la oposición no sirve de nada."],
 RS(("Partido","Organización con ideas comunes."),("Funciones","Representar, proponer, competir."),("Plataforma","Lo que promete."),("Oposición","Controla y propone.")),
 G(("Partido político","Organización que compite por el gobierno."),("Ideología","Forma de ver la sociedad."),("Plataforma","Programa de un partido."),("Oposición","Partidos que no gobiernan.")),
 ["¿Cómo se llama la organización que compite en elecciones para gobernar?","¿Cómo se llama el programa de propuestas de un partido?","¿La oposición controla al gobierno? Respondé sí o no.","¿Cómo se llama la forma de ver la sociedad que guía a un partido?"],
 [["partido politico","partido político","un partido politico","un partido político","partido"],["plataforma","la plataforma","programa"],["si","sí"],["ideologia","ideología","la ideologia","la ideología"]],
 {"incompleto":"Plataforma. Oposición.","solo":"Los partidos representan, proponen y compiten.","carpeta":["Partido político.","Plataforma.","Sí.","Ideología."]})
A2=NV("Vas a distinguir los sistemas electorales mayoritario y proporcional y explicar cómo se reparten los cargos.",["Qué es un sistema electoral","Mayoritario","Proporcional","Balotaje"],[
 S(1,"Qué es un sistema electoral",[D("Sistema electoral","Conjunto de reglas que transforma los votos en cargos."),P("Con los mismos votos, distintos sistemas pueden dar resultados distintos.")]),
 S(1,"Mayoritario",[P("En el sistema <b>mayoritario</b>, gana el cargo quien obtiene más votos y los demás no obtienen representación. Es simple, pero deja sin representación a muchos votantes.")]),
 S(2,"Proporcional",[P("En el sistema <b>proporcional</b>, los cargos se reparten según el porcentaje de votos de cada lista. Si una lista obtiene el 30 %, recibe cerca del 30 % de las bancas. Así hay más pluralismo.")]),
 S(2,"Balotaje",[PN("Cuando ningún candidato supera el mínimo exigido, se hace una <b>segunda vuelta</b> (balotaje) entre los dos más votados. En la Argentina, para presidente se gana en primera vuelta con el 45 % de los votos, o con el 40 % y 10 puntos de diferencia sobre el segundo.","Cuando ningún candidato supera el mínimo exigido, muchos países hacen una <b>segunda vuelta</b> (balotaje) entre los dos más votados. Cada país fija qué porcentaje hace falta para ganar en primera vuelta.")])],
 {"titulo":"calcular","planteo":"Se eligen 10 bancas y una lista saca el 40 % de los votos. ¿Cuántas bancas le corresponden en un sistema proporcional?","pasos":["40 % de 10 es 4.","Le corresponden cerca de 4 bancas.","En un sistema mayoritario puro, ganaría solo si es la más votada."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El sistema donde gana quien tiene más votos es el ___ .","El sistema que reparte bancas según el porcentaje de votos es el ___ ."]},
 {"titulo":"tu turno","planteo":"Explicá una ventaja y una desventaja de cada sistema."},
 {"titulo":"Votos y cargos","texto":"Preguntate siempre cómo se convierten los votos en cargos."},
 ["Pensar que todos los sistemas dan el mismo resultado.","Creer que el proporcional deja sin voz a las minorías."],
 RS(("Sistema electoral","Votos a cargos."),("Mayoritario","Gana el más votado."),("Proporcional","Según el porcentaje."),("Balotaje","Segunda vuelta.")),
 G(("Banca","Cargo en un cuerpo legislativo."),("Lista","Conjunto de candidatos de un partido."),("Balotaje","Segunda vuelta entre los dos más votados."),("Proporcionalidad","Reparto según el porcentaje.")),
 ["¿Cómo se llama el sistema donde gana el cargo quien tiene más votos?","¿Cómo se llama el sistema que reparte cargos según el porcentaje de votos?","¿El balotaje es una segunda vuelta entre los dos más votados? Respondé sí o no.","Con 20 bancas y una lista con el 50 % de los votos en un sistema proporcional, ¿cuántas bancas recibe? Respondé solo el número."],
 [["mayoritario","el mayoritario"],["proporcional","el proporcional"],["si","sí"],["10"]],
 {"incompleto":"Mayoritario. Proporcional.","solo":"Proporcional: más pluralismo. Mayoritario: más simple.","carpeta":["Mayoritario.","Proporcional.","Sí.","10."]})
A3=NV("Vas a comparar el voto obligatorio y el voluntario con sus ventajas y desventajas.",["Dos modelos","Argumentos a favor del obligatorio","Argumentos a favor del voluntario","Participación y calidad"],[
 S(1,"Dos modelos",[PN("En el voto <b>obligatorio</b>, las personas habilitadas deben votar y, si no lo hacen sin justificación, pueden recibir una multa. En el <b>voluntario</b>, cada quien decide. En la Argentina el voto es obligatorio desde los 18 hasta los 70 años; a los 16 y 17 y desde los 71 es optativo.","En el voto <b>obligatorio</b>, las personas habilitadas deben votar y, si no lo hacen sin justificación, pueden recibir una sanción. En el <b>voluntario</b>, cada quien decide. Algunos países, como Australia y Bélgica, tienen voto obligatorio; en otros es voluntario.")]),
 S(1,"A favor del obligatorio",[T("Argumentos",["Argumento","Idea"],[["Mayor participación","Vota casi todo el padrón"],["Legitimidad","El gobierno representa a más gente"],["Igualdad","Participan también quienes suelen quedar afuera"]])]),
 S(2,"A favor del voluntario",[T("Argumentos",["Argumento","Idea"],[["Libertad","Nadie debería ser obligado a votar"],["Interés real","Vota quien se informa y se interesa"],["Sin multas","No se sanciona a nadie"]])]),
 S(2,"Participación y calidad",[P("La obligatoriedad aumenta la cantidad de votos, pero no garantiza que sean informados. Por eso conviven con políticas de <b>educación cívica</b> y de acceso a la información.")])],
 {"titulo":"comparar","planteo":"¿Qué argumento da cada modelo?","pasos":["Obligatorio: más participación y legitimidad.","Voluntario: libertad de elegir si votar.","Cada uno prioriza un valor distinto."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Si votar es un deber, el voto es ___ .","Si cada persona decide si vota, el voto es ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un modelo y escribí tres argumentos a favor."},
 {"titulo":"Dos valores","texto":"Libertad y participación: cada sistema pone el acento en uno."},
 ["Pensar que obligatorio significa votar por alguien determinado.","Creer que un modelo es siempre mejor."],
 RS(("Obligatorio","Se debe votar."),("Voluntario","Se decide."),("A favor del primero","Participación."),("A favor del segundo","Libertad.")),
 G(("Padrón","Lista de personas habilitadas para votar."),("Obligatorio","Que se debe cumplir."),("Voluntario","Que se hace por decisión propia."),("Legitimidad","Aceptación de las autoridades.")),
 ["¿Cómo se llama el voto que hay que emitir por obligación?","¿Cómo se llama el voto que cada persona decide emitir o no?","¿La obligatoriedad aumenta la participación? Respondé sí o no.","¿Cómo se llama la lista de personas habilitadas para votar?"],
 [["obligatorio","el obligatorio","voto obligatorio"],["voluntario","el voluntario","voto voluntario"],["si","sí"],["padron","padrón","el padron","el padrón"]],
 {"incompleto":"Obligatorio. Voluntario.","solo":"Obligatorio: más participación. Voluntario: libertad de decidir.","carpeta":["Obligatorio.","Voluntario.","Sí.","Padrón."]})
A4=NV("Vas a analizar cómo las campañas, los medios y el financiamiento influyen en las elecciones.",["La campaña","Los medios","Financiamiento","Elecciones justas"],[
 S(1,"La campaña",[P("La campaña electoral es el período en que los partidos presentan candidatos y propuestas. Incluye debates, actos, publicidad y redes sociales.")]),
 S(1,"Los medios",[PN("Los medios informan sobre candidatos y propuestas, pero también pueden favorecer a unos sobre otros. Por eso importa la <b>pluralidad de voces</b>. En la Argentina existe una veda electoral: se prohíbe hacer campaña en los días previos a la votación.","Los medios informan sobre candidatos y propuestas, pero también pueden favorecer a unos sobre otros. Por eso importa la <b>pluralidad de voces</b>. Muchos países fijan un período de silencio electoral antes de la votación.")]),
 S(2,"Financiamiento",[T("De dónde sale el dinero",["Fuente","Detalle"],[["Aportes públicos","El Estado financia parte de la campaña"],["Aportes privados","Donaciones con límites y registro"],["Rendición de cuentas","Los partidos deben informar cuánto gastan"]]),PN("En la Argentina, una ley regula el financiamiento de los partidos y exige rendir cuentas.","En muchos países, una ley regula el financiamiento de los partidos y exige rendir cuentas.")]),
 S(2,"Elecciones justas",[P("Para que una elección sea justa debe haber reglas iguales para todos, límites al gasto, transparencia y acceso equilibrado a los medios.")])],
 {"titulo":"analizar","planteo":"¿Por qué conviene limitar los aportes privados a una campaña?","pasos":["Quien más dinero aporta podría tener más influencia.","Eso rompe la igualdad entre partidos.","Los límites y la transparencia lo evitan."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los partidos deben informar cuánto gastan: es la ___ de cuentas.","La existencia de muchas voces en los medios es la ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres cosas que mirarías antes de creer una propuesta de campaña."},
 {"titulo":"Seguir el dinero","texto":"Preguntate quién financia una campaña y por qué."},
 ["Creer que la publicidad es información neutral.","Pensar que el financiamiento no influye."],
 RS(("Campaña","Candidatos y propuestas."),("Medios","Informan y pueden influir."),("Financiamiento","Aportes públicos y privados."),("Justicia","Reglas iguales.")),
 G(("Campaña","Período de propuestas antes de votar."),("Pluralidad","Variedad de voces."),("Rendición de cuentas","Informar cómo se gasta."),("Veda","Período sin campaña.")),
 ["¿Cómo se llama el período en que los partidos presentan propuestas antes de votar?","¿Cómo se llama informar cuánto y en qué se gastó?","¿Los aportes privados pueden influir en una campaña? Respondé sí o no.","¿Cómo se llama la variedad de voces en los medios?"],
 [["campana","campaña","la campana","la campaña"],["rendicion de cuentas","rendición de cuentas","la rendicion de cuentas","la rendición de cuentas"],["si","sí"],["pluralidad","la pluralidad"]],
 {"incompleto":"Campaña. Rendición.","solo":"Miro quién financia, comparo fuentes y verifico datos.","carpeta":["Campaña.","Rendición de cuentas.","Sí.","Pluralidad."]})
ACT4={"1":[{"t":"matching","p":"Uní cada función de los partidos con su descripción.","o":{"izquierda":["Representar","Proponer","Competir","Controlar"],"derecha":["Llevar demandas a las instituciones","Presentar un programa","Presentar candidatos","Vigilar a quienes gobiernan"]},"r":{"pares":{"Representar":"Llevar demandas a las instituciones","Proponer":"Presentar un programa","Competir":"Presentar candidatos","Controlar":"Vigilar a quienes gobiernan"}},"e":"Cada función, su descripción."},VF("Todos los partidos piensan igual.","Falso","Cada uno tiene su ideología.")],
 "2":[{"t":"classify","p":"¿Mayoritario o proporcional?","o":{"elementos":["Gana quien tiene más votos","Bancas según el porcentaje","Más pluralismo","Más simple"],"categorias":["Mayoritario","Proporcional"]},"r":{"categorias":{"Gana quien tiene más votos":"Mayoritario","Bancas según el porcentaje":"Proporcional","Más pluralismo":"Proporcional","Más simple":"Mayoritario"}},"e":"Cada sistema tiene sus rasgos."},FB("La segunda vuelta entre los dos más votados es el ___ .",[["balotaje"]],"Balotaje.")],
 "3":[MS("¿Cuáles son argumentos a favor del voto obligatorio?",["Mayor participación","Más legitimidad","Libertad de no votar","Participan más personas"],["Mayor participación","Más legitimidad","Participan más personas"],"La libertad de no votar es un argumento del voto voluntario."),{"t":"ordering","p":"Ordená de más a menos obligación.","o":["Voto voluntario sin sanción","Voto obligatorio con multa","Voto obligatorio sin multa efectiva"],"r":{"orden":["Voto obligatorio con multa","Voto obligatorio sin multa efectiva","Voto voluntario sin sanción"]},"e":"Cuanto más sanción, más obligación."}],
 "4":[TT("Tocá los tipos de aporte: «Los aportes públicos y los privados financian campañas».",["Los","aportes","públicos","y","los","privados","financian","campañas"],[2,5],"Los dos tipos de aporte."),VF("El financiamiento puede influir en una campaña.","Verdadero","Por eso se regula.")],
 "5":[MC("Relámpago. Los partidos que no gobiernan forman la…",["Oposición","Plataforma","Banca"],"Oposición","Controlan al gobierno.",tiempo=20),VF("Relámpago. El sistema proporcional reparte cargos según el porcentaje.","Verdadero","Más pluralismo.",tiempo=20),MC("Relámpago. La segunda vuelta se llama…",["Balotaje","Padrón","Veda"],"Balotaje","Entre los dos más votados.",tiempo=20),VF("Relámpago. El voto obligatorio garantiza que el voto sea informado.","Falso","Aumenta la cantidad, no la calidad.",tiempo=20)]}
EX4=[[1,MC("Un partido político es…",["Una organización que compite por el gobierno","Un tribunal","Un medio","Un sindicato"],"Una organización que compite por el gobierno","Busca ganar elecciones.")],
 [1,FB("Los partidos que no gobiernan forman la ___ .",[["oposicion","oposición"]],"Controla y propone.")],
 [1,VF("La plataforma es lo que el partido promete hacer.","Verdadero","Es su programa.")],
 [2,MC("El sistema donde gana quien tiene más votos es…",["Mayoritario","Proporcional","Mixto","Directo"],"Mayoritario","Los demás no obtienen cargos.")],
 [2,MC("El sistema que reparte bancas según el porcentaje es…",["Proporcional","Mayoritario","Directo","Obligatorio"],"Proporcional","Más pluralismo.")],
 [2,N("Se eligen 10 bancas y una lista saca el 30 % de los votos en un sistema proporcional. ¿Cuántas bancas recibe?",{"acepta":[3]},"30 % de 10 es 3.")],
 [3,MC("En el voto obligatorio…",["Se debe votar","Se decide si votar","No hay padrón","Se vota dos veces"],"Se debe votar","Hay sanción si no se justifica.")],
 [3,VF("El voto voluntario respeta la libertad de decidir si votar.","Verdadero","Es su argumento.")],
 [3,MC("Una ventaja del voto obligatorio es…",["Mayor participación","Menos padrón","Más multas","Menos legitimidad"],"Mayor participación","Vota casi todo el padrón.")],
 [4,MC("Rendir cuentas significa…",["Informar cuánto y en qué se gastó","Votar","Debatir","Ganar"],"Informar cuánto y en qué se gastó","Da transparencia.")],
 [4,MS("Una elección es justa si hay…",["Reglas iguales","Transparencia","Límites al gasto","Censura"],["Reglas iguales","Transparencia","Límites al gasto"],"La censura lo impide.")],
 [4,FB("La variedad de voces en los medios es la ___ .",[["pluralidad"]],"Pluralidad.")],
 [4,VF("El financiamiento de las campañas no tiene importancia.","Falso","Influye y por eso se regula.")]]
M4={"subject_id":SID,"tema":4,"practica":"Práctica general: partidos políticos y elecciones","examen_titulo":"Nivel jefe: partidos políticos y elecciones","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT4,"examen":EX4}

# ============ MISIÓN 5: EL ESTADO DE DERECHO ============
B1=NV("Vas a explicar qué significa Estado de derecho y por qué nadie está por encima de la ley.",["Qué es","Rasgos","Sin impunidad","Estado de derecho y democracia"],[
 S(1,"Qué es",[D("Estado de derecho","Organización política en la que el poder se ejerce según leyes conocidas, iguales para todos y aplicadas por jueces independientes.")]),
 S(1,"Rasgos",[T("Qué lo caracteriza",["Rasgo","Qué significa"],[["Imperio de la ley","Todos, incluidos los gobernantes, deben cumplir la ley"],["Igualdad ante la ley","Nadie tiene privilegios"],["Derechos garantizados","Existen vías para reclamarlos"],["Jueces independientes","Deciden según la ley, sin presiones"],["Publicidad de las normas","Las leyes son conocidas"]])]),
 S(2,"Sin impunidad",[P("En un Estado de derecho, quien comete un delito, sea quien sea, tiene que responder ante la justicia. Un gobierno no puede actuar fuera de la ley ni cambiar las reglas a su conveniencia.")]),
 S(2,"Estado de derecho y democracia",[PN("Estado de derecho y democracia se necesitan: sin elecciones libres no hay control popular, y sin leyes que limiten al poder, el voto puede quedar vacío. En la Argentina, el Estado de derecho se apoya en la Constitución Nacional.","Estado de derecho y democracia se necesitan: sin elecciones libres no hay control popular, y sin leyes que limiten al poder, el voto puede quedar vacío. En cada país, el Estado de derecho se apoya en la Constitución.")])],
 {"titulo":"identificar","planteo":"Un funcionario usa su cargo para no pagar una multa. ¿Qué principio se rompe?","pasos":["La ley debe valer para todos.","Aquí hay un privilegio.","Se rompe la igualdad ante la ley."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Nadie está por encima de la ley: es el imperio de la ___ .","Los jueces deben decidir con ___ y sin presiones."]},
 {"titulo":"tu turno","planteo":"Escribí tres situaciones donde se respete el Estado de derecho."},
 {"titulo":"Igual para todos","texto":"Si una regla vale para unos y no para otros, algo falla."},
 ["Creer que el gobierno puede actuar fuera de la ley.","Pensar que Estado de derecho es solo tener leyes."],
 RS(("Estado de derecho","Poder limitado por la ley."),("Rasgos","Igualdad, jueces independientes."),("Impunidad","No debe existir."),("Democracia","Se necesitan.")),
 G(("Imperio de la ley","La ley rige a todos."),("Impunidad","Falta de castigo."),("Independencia judicial","Jueces sin presiones."),("Privilegio","Ventaja injusta.")),
 ["¿Cómo se llama el Estado en el que el poder se ejerce según leyes iguales para todos?","¿Cómo se llama la falta de castigo para quien comete un delito?","¿Los gobernantes deben cumplir la ley? Respondé sí o no.","¿Qué deben tener los jueces para decidir sin presiones?"],
 [["estado de derecho","el estado de derecho"],["impunidad","la impunidad"],["si","sí"],["independencia","independencia judicial","la independencia"]],
 {"incompleto":"Ley. Independencia.","solo":"Si un funcionario evita una multa por su cargo, rompe la igualdad ante la ley.","carpeta":["Estado de derecho.","Impunidad.","Sí.","Independencia."]})
B2=NV("Vas a explicar cómo la división de poderes y los controles mutuos limitan el poder.",["Tres poderes","Controles","Equilibrio","Ejemplos"],[
 S(1,"Tres poderes",[PN("El poder se reparte entre el <b>Legislativo</b> (hace las leyes), el <b>Ejecutivo</b> (las aplica y gobierna) y el <b>Judicial</b> (las interpreta y juzga). En la Argentina, el Legislativo es el Congreso (Diputados y Senadores), el Ejecutivo es el presidente y el Judicial incluye a la Corte Suprema.","El poder se reparte entre el <b>Legislativo</b> (hace las leyes), el <b>Ejecutivo</b> (las aplica y gobierna) y el <b>Judicial</b> (las interpreta y juzga). Cada país nombra de modo distinto a sus instituciones.")]),
 S(1,"Controles",[T("Cómo se controlan",["Poder que controla","Cómo","A quién"],[["Legislativo","Aprueba leyes, investiga, puede iniciar un juicio político","Ejecutivo y jueces"],["Ejecutivo","Puede vetar leyes","Legislativo"],["Judicial","Declara inconstitucional lo que viola la Constitución","Ejecutivo y Legislativo"]])]),
 S(2,"Equilibrio",[P("Este sistema se llama de <b>frenos y contrapesos</b>: cada poder frena a los otros y los equilibra. Así ninguno puede concentrar todo.")]),
 S(2,"Ejemplos",[P("Si el Ejecutivo dicta una norma que viola derechos, un juez puede declararla inconstitucional. Si una ley es injusta, el Ejecutivo puede vetarla y el Legislativo discutirla de nuevo.")])],
 {"titulo":"relacionar","planteo":"¿Qué poder controla a quién cuando un juez anula una norma del gobierno?","pasos":["El Judicial revisa la norma.","Declara que viola la Constitución.","Así controla al Ejecutivo."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El poder que juzga y aplica las leyes a casos concretos es el ___ .","Cada poder frena a los otros en el sistema de frenos y ___ ."]},
 {"titulo":"tu turno","planteo":"Explicá con un ejemplo cómo un poder controla a otro."},
 {"titulo":"Frenos y contrapesos","texto":"Si un solo poder lo decide todo, no hay control."},
 ["Pensar que los tres poderes no se relacionan.","Creer que el Judicial dicta las leyes."],
 RS(("Poderes","Legislativo, Ejecutivo, Judicial."),("Controles","Veto, juicio político, inconstitucionalidad."),("Frenos y contrapesos","Se equilibran."),("Sin control","Hay abusos.")),
 G(("Veto","Rechazo del Ejecutivo a una ley."),("Juicio político","Proceso para remover a un funcionario."),("Inconstitucional","Contrario a la Constitución."),("Contrapeso","Fuerza que equilibra a otra.")),
 ["¿Cómo se llama el rechazo del Ejecutivo a una ley?","¿Cómo se llama lo que es contrario a la Constitución?","¿Cada poder controla a los otros? Respondé sí o no.","¿Qué poder hace las leyes?"],
 [["veto","el veto"],["inconstitucional","es inconstitucional"],["si","sí"],["legislativo","el legislativo","poder legislativo"]],
 {"incompleto":"Judicial. Contrapesos.","solo":"Un juez declara inconstitucional una norma del Ejecutivo.","carpeta":["Veto.","Inconstitucional.","Sí.","Legislativo."]})
B3=NV("Vas a explicar qué es una constitución, qué contiene y por qué es la norma suprema.",["Qué es","Partes","Norma suprema","Por qué importa"],[
 S(1,"Qué es",[D("Constitución","Ley fundamental de un Estado que organiza el poder y garantiza los derechos de las personas.")]),
 S(1,"Partes",[T("Qué contiene",["Parte","Qué trata"],[["Declaraciones","Los principios y valores del Estado"],["Derechos y garantías","Qué derechos se reconocen y cómo protegerlos"],["Organización del poder","Cómo funcionan los poderes y los gobiernos"]])]),
 S(2,"Norma suprema",[PN("Una constitución es la <b>norma suprema</b>: ninguna ley, decreto o sentencia puede contradecirla. La Constitución Nacional argentina se sancionó en 1853 y se reformó varias veces, la última en 1994.","Una constitución es la <b>norma suprema</b>: ninguna ley, decreto o sentencia puede contradecirla. Cada país tiene su propia constitución, que puede haber sido reformada varias veces.")]),
 S(2,"Por qué importa",[P("Sin constitución, quienes gobiernan podrían cambiar las reglas cuando quisieran. La constitución limita el poder y protege a las personas, incluso frente al propio Estado.")])],
 {"titulo":"clasificar","planteo":"«Todas las personas son iguales ante la ley». ¿A qué parte de la Constitución pertenece?","pasos":["Habla de un derecho.","Se trata de los derechos y garantías.","Pertenece a esa parte."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La norma que está por encima de todas las demás es la norma ___ .","La constitución limita el poder y protege los ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí dos derechos y dos reglas de organización del poder que debería tener una constitución."},
 {"titulo":"Por encima","texto":"Si una ley contradice la constitución, la ley pierde."},
 ["Pensar que una constitución es una ley más.","Creer que solo habla de derechos."],
 RS(("Constitución","Ley fundamental."),("Partes","Declaraciones, derechos, poder."),("Suprema","Por encima de todas."),("Importa","Limita al poder.")),
 G(("Constitución","Ley fundamental del Estado."),("Norma suprema","La de mayor jerarquía."),("Garantía","Medio para proteger un derecho."),("Decreto","Norma dictada por el Ejecutivo.")),
 ["¿Cómo se llama la ley fundamental de un Estado?","¿Cómo se llama la norma que está por encima de todas las demás?","¿Una ley puede contradecir la constitución? Respondé sí o no.","¿Qué protege la constitución además de limitar el poder: los derechos o las multas?"],
 [["constitucion","constitución","la constitucion","la constitución"],["suprema","norma suprema","la norma suprema"],["no"],["derechos","los derechos"]],
 {"incompleto":"Suprema. Derechos.","solo":"La Constitución organiza el poder y garantiza derechos.","carpeta":["Constitución.","Norma suprema.","No.","Los derechos."]})
B4=NV("Vas a explicar cómo se protege la constitución: control de constitucionalidad, reforma difícil y garantías.",["Control de constitucionalidad","Reforma difícil","Garantías","Cuidarla entre todos"],[
 S(1,"Control de constitucionalidad",[P("Los jueces pueden revisar si una norma respeta la constitución y declararla <b>inconstitucional</b> si no lo hace. Ese control evita que las leyes y las decisiones del gobierno violen derechos.")]),
 S(1,"Reforma difícil",[P("Cambiar la constitución exige un procedimiento especial, más exigente que el de una ley común (mayorías más grandes, asambleas o consultas). Esto la hace <b>rígida</b> y la protege de cambios apresurados.")]),
 S(2,"Garantías",[PN("Las garantías son herramientas para reclamar cuando un derecho es violado. En la Argentina, el <b>amparo</b> protege derechos frente a actos ilegales y el <b>hábeas corpus</b> protege la libertad física.","Las garantías son herramientas para reclamar cuando un derecho es violado. Muchos países tienen figuras como el <b>amparo</b>, que protege derechos frente a actos ilegales, y el <b>hábeas corpus</b>, que protege la libertad física.")]),
 S(2,"Cuidarla entre todos",[P("La constitución se protege cuando la ciudadanía la conoce, reclama sus derechos, exige que se cumpla y participa en las decisiones que pueden afectarla.")])],
 {"titulo":"aplicar","planteo":"Una autoridad detiene a una persona sin orden judicial. ¿Qué garantía puede usarse?","pasos":["Se afecta la libertad física.","La garantía que la protege es el hábeas corpus.","Un juez revisa la detención."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Declarar que una ley viola la constitución es declararla ___ .","Una constitución difícil de reformar es una constitución ___ ."]},
 {"titulo":"tu turno","planteo":"Explicá con un ejemplo cómo una garantía protege un derecho."},
 {"titulo":"Conocerla","texto":"Una constitución que nadie conoce se cuida peor."},
 ["Creer que la constitución se puede cambiar como cualquier ley.","Pensar que las garantías son solo para abogados."],
 RS(("Control","Jueces revisan las normas."),("Reforma","Procedimiento especial."),("Garantías","Amparo y hábeas corpus."),("Ciudadanía","Conocer y reclamar.")),
 G(("Control de constitucionalidad","Revisión de si una norma respeta la constitución."),("Rígida","Difícil de reformar."),("Amparo","Garantía contra actos ilegales."),("Hábeas corpus","Garantía de la libertad física.")),
 ["¿Cómo se llama el control de si una norma respeta la constitución?","¿Cómo se llama la garantía que protege la libertad física?","¿La constitución es más difícil de reformar que una ley común? Respondé sí o no.","¿Cómo se llama la constitución difícil de reformar: rígida o flexible?"],
 [["control de constitucionalidad","el control de constitucionalidad","constitucionalidad"],["habeas corpus","hábeas corpus","el habeas corpus","el hábeas corpus"],["si","sí"],["rigida","rígida"]],
 {"incompleto":"Inconstitucional. Rígida.","solo":"Hábeas corpus: protege contra una detención sin orden judicial.","carpeta":["Control de constitucionalidad.","Hábeas corpus.","Sí.","Rígida."]})
ACT5={"1":[MS("¿Cuáles son rasgos del Estado de derecho?",["Imperio de la ley","Igualdad ante la ley","Jueces independientes","Privilegios para el gobierno"],["Imperio de la ley","Igualdad ante la ley","Jueces independientes"],"Los privilegios lo contradicen."),VF("Un gobierno puede actuar fuera de la ley si tiene muchos votos.","Falso","Siempre debe cumplir la ley.")],
 "2":[{"t":"matching","p":"Uní cada poder con su función.","o":{"izquierda":["Legislativo","Ejecutivo","Judicial"],"derecha":["Hace las leyes","Gobierna y las aplica","Interpreta las leyes y juzga"]},"r":{"pares":{"Legislativo":"Hace las leyes","Ejecutivo":"Gobierna y las aplica","Judicial":"Interpreta las leyes y juzga"}},"e":"Cada poder, su función."},FB("El rechazo del Ejecutivo a una ley es el ___ .",[["veto"]],"Veto.")],
 "3":[{"t":"classify","p":"¿A qué parte de la constitución pertenece?","o":{"elementos":["Igualdad ante la ley","Cómo se elige al Ejecutivo","Libertad de expresión","Funciones del Congreso"],"categorias":["Derechos y garantías","Organización del poder"]},"r":{"categorias":{"Igualdad ante la ley":"Derechos y garantías","Cómo se elige al Ejecutivo":"Organización del poder","Libertad de expresión":"Derechos y garantías","Funciones del Congreso":"Organización del poder"}},"e":"Derechos por un lado, organización por otro."},VF("Una ley puede contradecir la constitución.","Falso","La constitución es la norma suprema.")],
 "4":[{"t":"ordering","p":"Ordená qué ocurre cuando una norma viola la constitución.","o":["Un juez la declara inconstitucional","Una persona reclama","La norma deja de aplicarse","Se revisa la norma"],"r":{"orden":["Una persona reclama","Se revisa la norma","Un juez la declara inconstitucional","La norma deja de aplicarse"]},"e":"Del reclamo a la anulación."},TT("Tocá las garantías: «El amparo y el hábeas corpus protegen derechos».",["El","amparo","y","el","hábeas","corpus","protegen","derechos"],[1,4,5],"Son garantías.")],
 "5":[MC("Relámpago. Nadie está por encima de la ley: es…",["Imperio de la ley","Veto","Amparo"],"Imperio de la ley","Rige a todos.",tiempo=20),VF("Relámpago. El Judicial hace las leyes.","Falso","Las hace el Legislativo.",tiempo=20),MC("Relámpago. La norma suprema es…",["La constitución","Un decreto","Una ordenanza"],"La constitución","Está por encima.",tiempo=20),VF("Relámpago. El hábeas corpus protege la libertad física.","Verdadero","Contra detenciones ilegales.",tiempo=20)]}
EX5=[[1,MC("El Estado de derecho es el Estado en el que…",["El poder se ejerce según leyes iguales para todos","El gobierno hace lo que quiere","No hay jueces","Solo hay elecciones"],"El poder se ejerce según leyes iguales para todos","Nadie está por encima.")],
 [1,FB("Nadie está por encima de la ley: es el imperio de la ___ .",[["ley"]],"Rige a todos.")],
 [1,VF("La impunidad es la falta de castigo para quien comete un delito.","Verdadero","Un Estado de derecho la evita.")],
 [2,MC("El poder que hace las leyes es el…",["Legislativo","Ejecutivo","Judicial","Federal"],"Legislativo","Las sanciona.")],
 [2,MC("El rechazo del Ejecutivo a una ley es el…",["Veto","Amparo","Balotaje","Decreto"],"Veto","Es un control.")],
 [2,VF("En el sistema de frenos y contrapesos cada poder controla a los otros.","Verdadero","Se equilibran.")],
 [3,MC("La constitución es…",["La ley fundamental del Estado","Una ley común","Un decreto","Una sentencia"],"La ley fundamental del Estado","Organiza el poder y garantiza derechos.")],
 [3,MS("La constitución contiene…",["Derechos y garantías","Organización del poder","Declaraciones","Multas de tránsito"],["Derechos y garantías","Organización del poder","Declaraciones"],"Las multas están en otras normas.")],
 [3,VF("Una ley puede estar por encima de la constitución.","Falso","La constitución es suprema.")],
 [4,MC("Declarar que una norma viola la constitución es declararla…",["Inconstitucional","Obligatoria","Rígida","Proporcional"],"Inconstitucional","Lo hacen los jueces.")],
 [4,MC("La garantía que protege la libertad física es el…",["Hábeas corpus","Amparo","Veto","Balotaje"],"Hábeas corpus","Contra detenciones ilegales.")],
 [4,FB("Una constitución difícil de reformar es una constitución ___ .",[["rigida","rígida"]],"Rígida.")],
 [4,VF("Reformar la constitución exige un procedimiento más exigente que una ley común.","Verdadero","La protege de cambios apresurados.")]]
M5={"subject_id":SID,"tema":5,"practica":"Práctica general: el Estado de derecho","examen_titulo":"Nivel jefe: el Estado de derecho","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT5,"examen":EX5}
for n,m in ((4,M4),(5,M5)):
    m["act"]["5"]=PRACTICA[n]; os.makedirs(os.path.join(AQUI,f"mision-{n}"),exist_ok=True); json.dump(m,open(os.path.join(AQUI,f"mision-{n}",f"mision-{n}.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={(4,1):"74c81990-3677-41e1-8270-891b47744779",(4,2):"97ee0ee4-0312-43c4-8d30-d81a6a8acd9b",(4,3):"dd1e81bf-b167-42cd-a05b-88f1a25e648b",(4,4):"05d0d9cf-d17e-47fe-b2bc-13f56ce34173",(5,1):"1a34c1a5-d1a4-41ad-895c-ca7cac30781b",(5,2):"b83a7c37-a7f7-4282-805c-02376271d0ec",(5,3):"7acdd5ac-286b-4312-b11b-ce492b9786c2",(5,4):"e10072f4-eb81-46b8-9e29-752412fb3207"}
TIT={(4,1):"Qué hace un partido político",(4,2):"Sistemas electorales: mayoría y proporcionalidad",(4,3):"Voto obligatorio y voto voluntario",(4,4):"Campañas, medios y financiamiento",(5,1):"Qué significa Estado de derecho",(5,2):"División de poderes y control mutuo",(5,3):"Qué es una constitución y para qué sirve",(5,4):"Cómo se protege la constitución"}
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
CLS={(4,1):[
 RET("¿Cómo se llama la organización que compite en elecciones para gobernar?",6,"Partido político","🏳️","QUÉ HACE UN","partido político",["Desafío: ¿cómo se llama la organización que compite en elecciones para gobernar? Seis segundos.","Partido político.","Hoy: *qué hace un partido político*."]),
 DEF("Partido político","Organización que compite por el gobierno","🏳️",["Un *partido político* reúne a personas con ideas comunes.","Busca llegar al gobierno o influir en él."]),
 TB("FUNCIONES",["Función","Qué hace"],[["Representar","Lleva demandas"],["Proponer","Presenta un programa"],["Competir","Presenta candidatos"],["Controlar","Vigila al gobierno"]],["Las funciones de un partido.","*Representar*: lleva demandas.","*Proponer*: presenta un programa.","*Competir*: presenta candidatos.","Y *controlar*: vigila al gobierno."]),
 CMP(("IDEOLOGÍA","Cómo ve la sociedad","💭"),("PLATAFORMA","Lo que promete hacer","📋"),"+",["Dos conceptos clave.","La *ideología* es cómo ve la sociedad.","La *plataforma* es lo que promete hacer."]),
 CL([("GOBIERNO","🏛️"),("OPOSICIÓN","🔍")],[("Aplica políticas",0),("Controla y critica",1),("Propone otras",1)],["¿Gobierno u oposición?","*Aplica políticas*: gobierno.","*Controla* y *propone otras*: oposición."]),
 Q("Los partidos que no gobiernan forman la…",["Oposición","Plataforma","Banca"],0,["Te toca: los partidos que no gobiernan.","¿Oposición, plataforma o banca?","La *oposición*."]),
 ER([("Todos los partidos piensan igual","Cada uno tiene su ideología"),("La oposición no sirve","Controla y propone")],["Errores típicos.","Creer que todos piensan *igual*.","Y que la *oposición* no sirve."]),
 RES(["Repasemos.","Un *partido* compite por el gobierno.","Cumple varias *funciones*.","Tiene *ideología* y *plataforma*.","Y la *oposición* controla.","¡Clase terminada! Ahora, *a practicar*."],[["PARTIDO","compite"],["FUNCIONES","representar, proponer"],["PLATAFORMA","lo que promete"],["OPOSICIÓN","controla"]])],
(4,2):[
 NOT("ELECCIONES","Mismos votos, distinto reparto","Todo depende del sistema electoral","🗳️","SISTEMAS ELECTORALES","mayoría y proporcionalidad",["Noticia: mismos votos, distinto reparto.","Todo depende del sistema electoral.","Hoy: *sistemas electorales*."]),
 DEF("Sistema electoral","Reglas que convierten votos en cargos","🧮",["Un *sistema electoral* convierte votos en cargos.","Distintos sistemas dan distintos resultados."]),
 CMP(("MAYORITARIO","Gana quien tiene más votos","🥇"),("PROPORCIONAL","Bancas según el porcentaje","📊"),"vs",["Dos sistemas.","El *mayoritario*: gana el más votado.","El *proporcional*: bancas según el porcentaje."]),
 CAU(("Lista con 40 % de votos",'📊'),[("10 bancas en juego","🏛️"),("40 % de 10","🧮"),("Recibe 4 bancas","✅")],["Un ejemplo proporcional.","Una lista saca el *cuarenta por ciento*.","Hay *diez bancas*.","Recibe *cuatro bancas*."]),
 DEF("Balotaje","Segunda vuelta entre los dos más votados","🔁",["El *balotaje* es una segunda vuelta.","Se hace entre los dos más votados."]),
 Q("El sistema que reparte bancas según el porcentaje es el…",["Proporcional","Mayoritario","Directo"],0,["Te toca: reparte bancas según el porcentaje.","¿Proporcional, mayoritario o directo?","El *proporcional*."]),
 ER([("Todos los sistemas dan igual resultado","Cambian los resultados"),("El proporcional elimina minorías","Les da representación")],["Errores típicos.","Creer que *todos* dan igual resultado.","Y que el proporcional *elimina minorías*."]),
 RES(["Repasemos.","El *sistema electoral* convierte votos en cargos.","El *mayoritario* premia al más votado.","El *proporcional* reparte por porcentaje.","Y el *balotaje* es segunda vuelta.","¡Clase terminada! Ahora, *a practicar*."],[["SISTEMA","votos a cargos"],["MAYORITARIO","gana el más votado"],["PROPORCIONAL","por porcentaje"],["BALOTAJE","segunda vuelta"]])],
(4,3):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"¿Votar debería ser obligatorio? 🗳️"},{"yo":True,"txt":"Yo creo que sí 🙋"},{"yo":False,"txt":"¿Y la libertad de elegir?"}],"titulo":"VOTO OBLIGATORIO","sub":"o voluntario","voz":["Lu pregunta: ¿votar debería ser obligatorio?","Juan: yo creo que sí.","Lu: ¿y la libertad de elegir?","Hoy: *voto obligatorio y voto voluntario*."]},
 CMP(("OBLIGATORIO","Hay que votar","📜"),("VOLUNTARIO","Cada uno decide","🤷"),"vs",["Dos modelos.","En el *obligatorio* hay que votar.","En el *voluntario* cada uno decide."]),
 TB("A FAVOR DEL OBLIGATORIO",["Argumento","Idea"],[["Participación","Vota casi todo el padrón"],["Legitimidad","Más gente representada"],["Igualdad","Participan todos"]],["Argumentos del obligatorio.","*Participación*: vota casi todo el padrón.","*Legitimidad*: más gente representada.","*Igualdad*: participan todos."]),
 TB("A FAVOR DEL VOLUNTARIO",["Argumento","Idea"],[["Libertad","Nadie obliga"],["Interés real","Vota quien se informa"],["Sin multas","No se sanciona"]],["Argumentos del voluntario.","*Libertad*: nadie obliga.","*Interés real*: vota quien se informa.","*Sin multas*."]),
 CL([("OBLIGATORIO","📜"),("VOLUNTARIO","🤷")],[("Más participación",0),("Libertad de decidir",1),("Padrón completo",0)],["¿De cuál es el argumento?","*Más participación* y *padrón completo*: obligatorio.","*Libertad de decidir*: voluntario."]),
 Q("¿Qué ventaja tiene el voto obligatorio?",["Mayor participación","Menos padrón","Más multas"],0,["Te toca: ventaja del voto obligatorio.","¿Mayor participación, menos padrón o más multas?","*Mayor participación*."]),
 ER([("Obligatorio es votar por alguien","Es votar, pero libremente"),("Un modelo es siempre mejor","Cada uno prioriza un valor")],["Errores típicos.","Creer que obligatorio es votar por *alguien*.","Y que un modelo es *siempre mejor*."]),
 RES(["Repasemos.","En el *obligatorio* hay que votar.","En el *voluntario* se decide.","El primero busca *participación*.","El segundo prioriza la *libertad*.","¡Clase terminada! Ahora, *a practicar*."],[["OBLIGATORIO","hay que votar"],["VOLUNTARIO","se decide"],["VENTAJA 1","participación"],["VENTAJA 2","libertad"]])],
(4,4):[
 RET("¿Cómo se llama informar cuánto y en qué gastó un partido?",6,"Rendición de cuentas","💰","CAMPAÑAS, MEDIOS","y financiamiento",["Desafío: ¿cómo se llama informar cuánto y en qué gastó un partido? Seis segundos.","Rendición de cuentas.","Hoy: *campañas, medios y financiamiento*."]),
 DEF("Campaña electoral","Período de propuestas antes de votar","📣",["La *campaña electoral* es el período previo a la votación.","Se presentan candidatos y propuestas."]),
 CMP(("MEDIOS","Informan y pueden influir","📺"),("REDES","Difunden rápido y sin filtro","📱"),"+",["Dos canales.","Los *medios* informan y pueden influir.","Las *redes* difunden rápido y sin filtro."]),
 TB("FINANCIAMIENTO",["Fuente","Detalle"],[["Aportes públicos","Pone el Estado"],["Aportes privados","Con límites"],["Rendición","Se informa"]],["De dónde sale el dinero.","Los *aportes públicos* los pone el Estado.","Los *privados* tienen límites.","Y hay *rendición de cuentas*."]),
 CL([("AYUDA","✅"),("DAÑA","❌")],[("Límites al gasto",0),("Dinero sin control",1),("Transparencia",0),("Publicidad oculta",1)],["¿Ayuda o daña?","*Límites* y *transparencia*: ayudan.","*Dinero sin control* y *publicidad oculta*: dañan."]),
 Q("Informar cuánto y en qué se gastó es…",["Rendición de cuentas","Balotaje","Veda"],0,["Te toca: informar cuánto y en qué se gastó.","¿Rendición de cuentas, balotaje o veda?","*Rendición de cuentas*."]),
 ER([("La publicidad es información neutral","Busca persuadir"),("El dinero no influye","Puede influir")],["Errores típicos.","Creer que la publicidad es *neutral*.","Y que el dinero *no influye*."]),
 RES(["Repasemos.","La *campaña* presenta propuestas.","Los *medios* informan y pueden influir.","El *financiamiento* se regula.","Y la *transparencia* hace justa la elección.","¡Clase terminada! Ahora, *a practicar*."],[["CAMPAÑA","propuestas"],["MEDIOS","informan"],["DINERO","se regula"],["JUSTICIA","reglas iguales"]])],
(5,1):[
 NOT("JUSTICIA","Un funcionario no paga una multa","La ley vale para todos","⚖️","ESTADO DE DERECHO","qué significa",["Noticia: un funcionario no paga una multa.","La ley vale para todos.","Hoy: *qué significa Estado de derecho*."]),
 DEF("Estado de derecho","El poder limitado por leyes iguales para todos","⚖️",["En un *Estado de derecho* el poder se ejerce según leyes.","Leyes conocidas e iguales para todos."]),
 TB("RASGOS",["Rasgo","Qué significa"],[["Imperio de la ley","Rige a todos"],["Igualdad","Sin privilegios"],["Jueces independientes","Sin presiones"],["Derechos","Se garantizan"]],["Los rasgos.","*Imperio de la ley*: rige a todos.","*Igualdad*: sin privilegios.","*Jueces independientes*.","Y *derechos* garantizados."]),
 DEF("Impunidad","Falta de castigo","🚫",["La *impunidad* es la falta de castigo.","Un Estado de derecho la evita."]),
 CL([("RESPETA","✅"),("ROMPE","❌")],[("Igualdad de todos",0),("Privilegios",1),("Jueces libres",0),("Cambiar reglas",1)],["¿Respeta o rompe el Estado de derecho?","*Igualdad de todos* y *jueces libres*: respetan.","*Privilegios* y *cambiar reglas*: rompen."]),
 Q("¿Quién debe cumplir la ley?",["Todos","Solo los ciudadanos","Solo los jueces"],0,["Te toca: ¿quién debe cumplir la ley?","¿Todos, solo los ciudadanos o solo los jueces?","*Todos*, también los gobernantes."]),
 ER([("El gobierno puede actuar fuera de la ley","Debe cumplirla"),("Es solo tener leyes","Es que valgan para todos")],["Errores típicos.","Creer que el gobierno *puede actuar fuera de la ley*.","Y que alcanza con *tener leyes*."]),
 RES(["Repasemos.","El poder se limita con *leyes*.","Hay *igualdad* ante la ley.","Los *jueces* son independientes.","Y no debe haber *impunidad*.","¡Clase terminada! Ahora, *a practicar*."],[["ESTADO DE DERECHO","poder limitado"],["IGUALDAD","sin privilegios"],["JUECES","independientes"],["IMPUNIDAD","se evita"]])],
(5,2):[
 {"t":"gancho","grande":"Tres poderes","emoji":"⚖️","final":"que se controlan entre sí","titulo":"DIVISIÓN DE PODERES","sub":"y control mutuo","voz":["El poder se reparte en tres.","Y cada uno controla a los otros.","Hoy: *división de poderes y control mutuo*."]},
 TB("TRES PODERES",["Poder","Función"],[["Legislativo","Hace las leyes"],["Ejecutivo","Gobierna"],["Judicial","Juzga"]],["Los tres poderes.","El *legislativo* hace las leyes.","El *ejecutivo* gobierna.","El *judicial* juzga."]),
 TB("CONTROLES",["Poder","Cómo controla"],[["Legislativo","Investiga y puede juzgar políticamente"],["Ejecutivo","Veta leyes"],["Judicial","Declara inconstitucional"]],["Cómo se controlan.","El *legislativo* investiga.","El *ejecutivo* puede *vetar*.","El *judicial* puede declarar algo *inconstitucional*."]),
 DEF("Frenos y contrapesos","Cada poder frena a los otros","🔁",["El sistema se llama *frenos y contrapesos*.","Cada poder frena a los otros."]),
 CL([("LEGISLATIVO","📜"),("EJECUTIVO","🏛️"),("JUDICIAL","⚖️")],[("Votar una ley",0),("Vetar una ley",1),("Anular una norma",2)],["¿Qué poder lo hace?","*Votar una ley*: legislativo.","*Vetar*: ejecutivo.","*Anular una norma*: judicial."]),
 Q("El rechazo del Ejecutivo a una ley es el…",["Veto","Amparo","Balotaje"],0,["Te toca: el rechazo del ejecutivo a una ley.","¿Veto, amparo o balotaje?","El *veto*."]),
 ER([("Los poderes no se relacionan","Se controlan"),("El judicial dicta las leyes","Las hace el legislativo")],["Errores típicos.","Creer que los poderes *no se relacionan*.","Y que el judicial *dicta las leyes*."]),
 RES(["Repasemos.","Hay tres *poderes*.","Cada uno tiene *controles*.","Son *frenos y contrapesos*.","Así ninguno *concentra* el poder.","¡Clase terminada! Ahora, *a practicar*."],[["PODERES","tres"],["CONTROLES","veto, juicio político"],["EQUILIBRIO","frenos y contrapesos"],["SIN CONTROL","abusos"]])],
(5,3):[
 RET("¿Cuál es la ley fundamental de un Estado?",5,"La constitución","📜","QUÉ ES UNA CONSTITUCIÓN","y para qué sirve",["Desafío: ¿cuál es la ley fundamental de un Estado? Cinco segundos.","La constitución.","Hoy: *qué es una constitución y para qué sirve*."]),
 DEF("Constitución","Ley fundamental del Estado","📜",["La *constitución* es la ley fundamental de un Estado.","Organiza el poder y garantiza derechos."]),
 TB("PARTES",["Parte","Trata de"],[["Declaraciones","Principios"],["Derechos y garantías","Qué se reconoce"],["Organización","Cómo funcionan los poderes"]],["Qué contiene.","Las *declaraciones*: principios.","Los *derechos y garantías*.","Y la *organización* del poder."]),
 DEF("Norma suprema","Por encima de todas las demás","👑",["La constitución es la *norma suprema*.","Ninguna ley puede contradecirla."]),
 CL([("DERECHOS","⚖️"),("ORGANIZACIÓN","🏛️")],[("Expresión libre",0),("Poderes del Estado",1),("Igualdad",0)],["¿Derechos u organización?","*Expresión libre* e *igualdad*: derechos.","*Poderes del Estado*: organización."]),
 Q("La norma que está por encima de todas es…",["La constitución","Un decreto","Una ordenanza"],0,["Te toca: la norma por encima de todas.","¿La constitución, un decreto o una ordenanza?","*La constitución*."]),
 ER([("Es una ley más","Es la norma suprema"),("Solo habla de derechos","También organiza el poder")],["Errores típicos.","Creer que es *una ley más*.","Y que *solo* habla de derechos."]),
 RES(["Repasemos.","La *constitución* es la ley fundamental.","Tiene *declaraciones*, *derechos* y organización.","Es la *norma suprema*.","Y *limita* al poder.","¡Clase terminada! Ahora, *a practicar*."],[["CONSTITUCIÓN","ley fundamental"],["PARTES","tres"],["SUPREMA","sobre todas"],["FUNCIÓN","limita al poder"]])],
(5,4):[
 NOT("TRIBUNALES","Un juez anula una norma","Violaba la constitución","⚖️","PROTEGER LA CONSTITUCIÓN","cómo se logra",["Noticia: un juez anula una norma.","Violaba la constitución.","Hoy: *cómo se protege la constitución*."]),
 DEF("Control de constitucionalidad","Los jueces revisan si una norma respeta la constitución","🔍",["Los jueces hacen el *control de constitucionalidad*.","Revisan si una norma respeta la constitución."]),
 DEF("Constitución rígida","Difícil de reformar","🔒",["Una constitución *rígida* es difícil de reformar.","Exige un procedimiento especial."]),
 TB("GARANTÍAS",["Garantía","Protege"],[["Amparo","Derechos frente a actos ilegales"],["Hábeas corpus","La libertad física"]],["Las garantías.","El *amparo* protege derechos frente a actos ilegales.","El *hábeas corpus* protege la libertad física."]),
 CL([("PROTEGE","✅"),("DEBILITA","❌")],[("Conocerla",0),("Ignorar un abuso",1),("Reclamar derechos",0),("Cambiarla apurados",1)],["¿Protege o debilita la constitución?","*Conocerla* y *reclamar derechos*: protegen.","*Ignorar abusos* y *cambiarla apurados*: debilitan."]),
 Q("¿Qué garantía protege la libertad física?",["Hábeas corpus","Amparo","Veto"],0,["Te toca: protege la libertad física.","¿Hábeas corpus, amparo o veto?","El *hábeas corpus*."]),
 ER([("Se cambia como una ley común","Exige un procedimiento especial"),("Las garantías son para abogados","Son para todos")],["Errores típicos.","Creer que se cambia como *una ley común*.","Y que las garantías son *solo para abogados*."]),
 RES(["Repasemos.","Los jueces hacen el *control*.","La reforma es *difícil*.","Las *garantías* protegen derechos.","Y la *ciudadanía* la cuida.","¡Clase terminada! Ahora, *a practicar*."],[["CONTROL","jueces revisan"],["REFORMA","difícil"],["GARANTÍAS","amparo, hábeas corpus"],["CIUDADANÍA","conocer y reclamar"]])]}
for (m,n),es in CLS.items():
    json.dump({"sin_variante":True,"slug":f"ciud1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Ciudadanía I","titulo":TIT[(m,n)],"sub":f"Ciudadanía I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"ciud1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
