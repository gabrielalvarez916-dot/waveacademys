# -*- coding: utf-8 -*-
"""Ciudadanía I y Ciudadanía I Argentina · Misiones 6 y 7 (VARIANTE)."""
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
# ============ MISIÓN 6: DERECHOS HUMANOS Y TRATADOS ============
A1=NV("Vas a explicar qué son los derechos humanos y cuáles son sus características.",["Qué son","Características","De dónde vienen","Por qué se protegen"],[
 S(1,"Qué son",[D("Derechos humanos","Derechos que tiene toda persona por el solo hecho de serlo, sin distinción de origen, sexo, religión u otra condición.")]),
 S(1,"Características",[T("Cinco rasgos",["Rasgo","Qué significa"],[["Universales","Valen para todas las personas, en todo lugar"],["Inalienables","No se pueden quitar ni renunciar a ellos"],["Indivisibles","No se pueden separar ni jerarquizar"],["Interdependientes","Cada uno se relaciona con los demás"],["Progresivos","Se amplían con el tiempo"]])]),
 S(2,"De dónde vienen",[P("La idea de que toda persona tiene derechos por ser persona viene de muchas tradiciones y creció tras grandes violaciones, como las guerras y los genocidios. Se reconoció en documentos internacionales y en las constituciones.")]),
 S(2,"Por qué se protegen",[PN("Los derechos humanos se protegen para evitar abusos del poder y garantizar una vida digna. En la Argentina, la memoria de la última dictadura volvió central la defensa de los derechos humanos.","Los derechos humanos se protegen para evitar abusos del poder y garantizar una vida digna. En muchos países, la experiencia de dictaduras y guerras volvió central su defensa.")])],
 {"titulo":"relacionar","planteo":"¿Por qué un derecho humano es inalienable?","pasos":["Pertenece a la persona por ser persona.","Nadie puede quitárselo.","Tampoco puede renunciar a él."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los derechos que valen para todas las personas son ___ .","Los derechos que se amplían con el tiempo son ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí tres derechos humanos y explicá por qué son importantes."},
 {"titulo":"Por ser persona","texto":"Un derecho humano no se gana ni se pierde: se tiene por ser persona."},
 ["Pensar que los derechos humanos se otorgan como un premio.","Creer que algunos derechos valen más que otros."],
 RS(("Derechos humanos","De toda persona."),("Rasgos","Universales, inalienables, indivisibles."),("Origen","Tras graves violaciones."),("Protección","Evitar abusos.")),
 G(("Universal","Que vale para todos."),("Inalienable","Que no se puede quitar."),("Indivisible","Que no se puede separar."),("Dignidad","Valor de toda persona.")),
 ["¿Cómo se llaman los derechos que tiene toda persona por el solo hecho de serlo?","¿Cómo se llaman los derechos que no se pueden quitar: inalienables o temporales?","¿Los derechos humanos valen para todas las personas? Respondé sí o no.","¿Los derechos humanos se otorgan como un premio? Respondé sí o no."],
 [["derechos humanos","los derechos humanos"],["inalienables","los inalienables"],["si","sí"],["no"]],
 {"incompleto":"Derechos humanos. Universales.","solo":"Derecho a la educación: universal, de todos; y a la vida: nadie puede quitarlo.","carpeta":["Derechos humanos.","Inalienables.","Sí.","No."]})
A2=NV("Vas a explicar qué es la Declaración Universal de Derechos Humanos de 1948, por qué se creó y qué establece.",["Contexto","Qué establece","Valor","Alcance"],[
 S(1,"Contexto",[P("Después de la Segunda Guerra Mundial y de los crímenes del nazismo, las naciones del mundo crearon la <b>ONU</b> y buscaron un acuerdo para que esas violaciones no se repitieran. En 1948 su Asamblea General aprobó la <b>Declaración Universal de Derechos Humanos</b>.")]),
 S(1,"Qué establece",[T("Ideas centrales",["Idea","Qué dice"],[["Igualdad y dignidad","Todos nacemos libres e iguales en dignidad y derechos"],["No discriminación","Sin distinción de raza, sexo, religión, opinión u origen"],["Vida y libertad","Nadie puede ser esclavizado ni torturado"],["Derechos sociales","Trabajo, educación, salud, vivienda"]]),P("Tiene 30 artículos.")]),
 S(2,"Valor",[P("La Declaración no es un tratado, pero tiene gran valor moral y político. Inspiró tratados obligatorios y constituciones de muchos países.")]),
 S(2,"Alcance",[PN("En la Argentina, desde la reforma de 1994 la Declaración Universal tiene jerarquía constitucional, junto con otros instrumentos de derechos humanos.","En muchos países, la Declaración Universal inspira las constituciones y las leyes sobre derechos humanos.")])],
 {"titulo":"explicar","planteo":"¿Por qué se creó la Declaración Universal en 1948?","pasos":["Acababa de terminar la Segunda Guerra Mundial.","Se habían cometido crímenes terribles.","Se buscó un acuerdo para evitar que se repitieran."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La Declaración Universal tiene ___ artículos.","La Declaración fue aprobada por la ___ en 1948."]},
 {"titulo":"tu turno","planteo":"Elegí un artículo o idea de la Declaración y explicá cómo se aplica hoy."},
 {"titulo":"Nunca más","texto":"La Declaración nació para que los crímenes del pasado no se repitan."},
 ["Pensar que la Declaración es una ley obligatoria por sí sola.","Creer que solo trata de derechos políticos."],
 RS(("Año","1948."),("Origen","Posguerra."),("Contenido","30 artículos."),("Valor","Moral y político.")),
 G(("ONU","Organización de las Naciones Unidas."),("Declaración","Documento que proclama principios."),("Discriminación","Trato desigual injusto."),("Posguerra","Tiempo posterior a una guerra.")),
 ["¿En qué año se aprobó la Declaración Universal de Derechos Humanos? Respondé solo el número.","¿Qué organismo la aprobó: la ONU o la UNESCO?","¿La Declaración Universal tiene 30 artículos? Respondé sí o no.","¿Se creó después de la Segunda Guerra Mundial? Respondé sí o no."],
 [["1948"],["onu","la onu"],["si","sí"],["si","sí"]],
 {"incompleto":"1948. ONU.","solo":"Se creó para evitar que se repitan los crímenes de la guerra.","carpeta":["1948.","La ONU.","Sí.","Sí."]})
A3=NV("Vas a distinguir los derechos civiles, políticos, económicos, sociales y culturales y dar ejemplos.",["Civiles y políticos","Económicos, sociales y culturales","Derechos de solidaridad","Indivisibles"],[
 S(1,"Civiles y políticos",[T("Protegen la libertad",["Tipo","Ejemplos"],[["Civiles","Vida, libertad, igualdad ante la ley, libre expresión"],["Políticos","Votar, ser elegido, participar, asociarse"]])]),
 S(1,"Económicos, sociales y culturales",[T("Aseguran una vida digna",["Tipo","Ejemplos"],[["Económicos","Trabajo, salario justo, sindicalización"],["Sociales","Salud, educación, vivienda, seguridad social"],["Culturales","Participar de la cultura, usar el propio idioma"]])]),
 S(2,"Derechos de solidaridad",[P("Se los llama también <b>derechos de tercera generación</b>: la paz, un ambiente sano, el desarrollo. Se ejercen entre todos y para todos.")]),
 S(2,"Indivisibles",[P("Aunque se los clasifique, todos los derechos están conectados: sin educación (social) es difícil ejercer el voto informado (político), y sin libertad de expresión (civil) es difícil reclamar salud.")])],
 {"titulo":"clasificar","planteo":"¿A qué tipo de derecho pertenece «recibir atención de salud»?","pasos":["Se trata de un servicio básico para vivir con dignidad.","Pertenece a los derechos sociales.","Los Estados deben facilitar su acceso."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El derecho a votar es un derecho ___ .","El derecho a la educación es un derecho ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un ejemplo de cada tipo de derecho."},
 {"titulo":"Todos conectados","texto":"Un derecho sin los otros queda incompleto."},
 ["Pensar que los derechos sociales son un favor.","Creer que solo importan los derechos políticos."],
 RS(("Civiles","Libertad e igualdad."),("Políticos","Participación."),("Económicos y sociales","Vida digna."),("Solidaridad","Paz y ambiente.")),
 G(("Derechos civiles","Protegen la libertad."),("Derechos políticos","Permiten participar."),("Derechos sociales","Aseguran vida digna."),("Solidaridad","Derechos de todos y para todos.")),
 ["¿Cómo se llaman los derechos que permiten votar y ser elegido?","¿A qué tipo de derecho pertenece la salud?","¿Un ambiente sano es un derecho de solidaridad? Respondé sí o no.","¿Todos los derechos están conectados? Respondé sí o no."],
 [["politicos","políticos","los politicos","los políticos"],["sociales","los sociales","social"],["si","sí"],["si","sí"]],
 {"incompleto":"Políticos. Sociales.","solo":"Civil: libre expresión. Político: votar. Social: educación.","carpeta":["Políticos.","Sociales.","Sí.","Sí."]})
A4=NV("Vas a explicar qué son los tratados internacionales de derechos humanos y qué obligan a hacer a los Estados.",["Qué es un tratado","Principales tratados","Ratificar","Controlar su cumplimiento"],[
 S(1,"Qué es un tratado",[D("Tratado internacional","Acuerdo escrito entre Estados que los obliga jurídicamente a cumplir lo pactado.")]),
 S(1,"Principales tratados",[T("Algunos ejemplos",["Tratado","Qué protege"],[["Pacto de Derechos Civiles y Políticos (1966)","Libertades y participación"],["Pacto de Derechos Económicos, Sociales y Culturales (1966)","Trabajo, salud, educación"],["Convención sobre los Derechos del Niño (1989)","Niñas, niños y adolescentes"],["Convención contra la discriminación de la mujer (1979)","Igualdad de las mujeres"],["Convención Americana (1969)","Derechos en América"]])]),
 S(2,"Ratificar",[PN("Un Estado se obliga a cumplir un tratado cuando lo <b>ratifica</b>. En la Argentina, varios tratados de derechos humanos tienen jerarquía constitucional desde 1994.","Un Estado se obliga a cumplir un tratado cuando lo <b>ratifica</b>. Cada país decide qué jerarquía le da a esos tratados en su orden jurídico.")]),
 S(2,"Controlar su cumplimiento",[P("Existen comités y tribunales internacionales que revisan si los Estados cumplen. Una persona puede reclamar ante ellos cuando agotó los recursos de su país.")])],
 {"titulo":"explicar","planteo":"¿En qué se diferencia una declaración de un tratado?","pasos":["La declaración proclama principios.","El tratado obliga jurídicamente a los Estados que lo ratifican.","Por eso el tratado puede exigirse."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Cuando un Estado acepta obligarse por un tratado, lo ___ .","La Convención de 1989 protege a niñas, niños y ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un tratado y explicá qué derechos protege y por qué es importante."},
 {"titulo":"Obligan","texto":"Un tratado ratificado obliga: no es solo una buena intención."},
 ["Pensar que un tratado obliga a países que no lo ratificaron.","Creer que los tratados no pueden reclamarse."],
 RS(("Tratado","Acuerdo obligatorio."),("Ratificar","Aceptar obligarse."),("Ejemplos","Pactos y convenciones."),("Control","Comités y tribunales.")),
 G(("Tratado","Acuerdo entre Estados."),("Ratificar","Confirmar un tratado."),("Convención","Tratado sobre un tema."),("Pacto","Acuerdo internacional.")),
 ["¿Cómo se llama el acuerdo escrito entre Estados que los obliga jurídicamente?","¿Cómo se llama aceptar obligarse por un tratado?","¿La Convención sobre los Derechos del Niño es de 1989? Respondé sí o no.","¿Puede reclamarse ante un comité internacional cuando se agotaron los recursos del país? Respondé sí o no."],
 [["tratado","un tratado","tratado internacional"],["ratificar","ratificarlo","ratificarlo."],["si","sí"],["si","sí"]],
 {"incompleto":"Tratado. Ratificar.","solo":"Convención del Niño: protege a niñas, niños y adolescentes.","carpeta":["Tratado.","Ratificar.","Sí.","Sí."]})
ACT6={"1":[MS("¿Cuáles son características de los derechos humanos?",["Universales","Inalienables","Se compran","Indivisibles"],["Universales","Inalienables","Indivisibles"],"No se compran ni se otorgan."),VF("Los derechos humanos se pierden si una persona no los usa.","Falso","Son inalienables.")],
 "2":[{"t":"ordering","p":"Ordená los hechos que llevaron a la Declaración Universal.","o":["Se aprueba la Declaración","Termina la Segunda Guerra Mundial","Se crea la ONU","Se conocen los crímenes de guerra"],"r":{"orden":["Se conocen los crímenes de guerra","Termina la Segunda Guerra Mundial","Se crea la ONU","Se aprueba la Declaración"]},"e":"Del horror al acuerdo."},FB("La Declaración Universal se aprobó en el año ___ .",[["1948"]],"1948.")],
 "3":[{"t":"classify","p":"¿Qué tipo de derecho es?","o":{"elementos":["Votar","Recibir atención de salud","Libre expresión","Tener trabajo digno"],"categorias":["Civil o político","Económico o social"]},"r":{"categorias":{"Votar":"Civil o político","Recibir atención de salud":"Económico o social","Libre expresión":"Civil o político","Tener trabajo digno":"Económico o social"}},"e":"Libertades por un lado, vida digna por otro."},VF("Los derechos sociales son un favor del Estado.","Falso","Son derechos.")],
 "4":[{"t":"matching","p":"Uní cada tratado con lo que protege.","o":{"izquierda":["Convención del Niño","Pacto de derechos civiles","Pacto de derechos sociales","Convención contra la discriminación de la mujer"],"derecha":["Niñez y adolescencia","Libertades y participación","Trabajo, salud, educación","Igualdad de las mujeres"]},"r":{"pares":{"Convención del Niño":"Niñez y adolescencia","Pacto de derechos civiles":"Libertades y participación","Pacto de derechos sociales":"Trabajo, salud, educación","Convención contra la discriminación de la mujer":"Igualdad de las mujeres"}},"e":"Cada tratado, su objeto."},TT("Tocá la palabra que significa aceptar un tratado: «El Estado ratifica el tratado».",["El","Estado","ratifica","el","tratado"],[2],"Ratificar es aceptar obligarse.")],
 "5":[MC("Relámpago. Los derechos humanos valen para…",["Todas las personas","Solo adultos","Solo ciudadanos"],"Todas las personas","Son universales.",tiempo=20),VF("Relámpago. La Declaración Universal es de 1948.","Verdadero","Tras la guerra.",tiempo=20),MC("Relámpago. El derecho a votar es…",["Político","Social","Cultural"],"Político","Permite participar.",tiempo=20),VF("Relámpago. Un tratado ratificado obliga al Estado.","Verdadero","Es jurídicamente obligatorio.",tiempo=20)]}
EX6=[[1,MC("Los derechos humanos son los que tiene toda persona…",["Por el solo hecho de serlo","Por ser adulta","Por ser ciudadana","Por pagar impuestos"],"Por el solo hecho de serlo","Sin distinción.")],
 [1,FB("Los derechos que no se pueden quitar son ___ .",[["inalienables"]],"No se quitan ni se renuncia.")],
 [1,VF("Los derechos humanos son universales.","Verdadero","Valen para todos.")],
 [2,MC("La Declaración Universal se aprobó en…",["1948","1789","1994","1914"],"1948","Posguerra.")],
 [2,MC("¿Quién la aprobó?",["La ONU","La FIFA","La OEA","Un país"],"La ONU","Su Asamblea General.")],
 [2,VF("La Declaración Universal tiene 30 artículos.","Verdadero","Son 30.")],
 [3,MC("El derecho a votar es…",["Político","Social","Cultural","Económico"],"Político","Permite participar.")],
 [3,MS("Son derechos sociales:",["Salud","Educación","Votar","Vivienda"],["Salud","Educación","Vivienda"],"Votar es político.")],
 [3,VF("Todos los derechos están conectados.","Verdadero","Son indivisibles e interdependientes.")],
 [4,MC("Un tratado internacional es…",["Un acuerdo que obliga a los Estados","Una opinión","Una costumbre","Una ley local"],"Un acuerdo que obliga a los Estados","Si lo ratifican.")],
 [4,FB("Aceptar obligarse por un tratado es ___ .",[["ratificar"]],"Ratificar.")],
 [4,MC("La Convención de 1989 protege a…",["Niñas, niños y adolescentes","Trabajadores","Jueces","Turistas"],"Niñas, niños y adolescentes","Derechos del niño.")],
 [4,VF("Un tratado obliga a países que no lo ratificaron.","Falso","Solo obliga a quien lo ratifica.")]]
M6={"subject_id":SID,"tema":6,"practica":"Práctica general: derechos humanos y tratados","examen_titulo":"Nivel jefe: derechos humanos y tratados","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT6,"examen":EX6}

# ============ MISIÓN 7: GARANTÍAS PARA PROTEGER DERECHOS ============
B1=NV("Vas a explicar qué son las garantías constitucionales y para qué sirven.",["Derecho y garantía","Qué garantías hay","Cómo funcionan","Por qué importan"],[
 S(1,"Derecho y garantía",[D("Garantía constitucional","Herramienta que permite exigir que se cumpla un derecho o que se repare su violación."),P("Tener un derecho escrito no alcanza: hace falta un camino para reclamarlo si alguien lo viola.")]),
 S(1,"Qué garantías hay",[T("Principales garantías",["Garantía","Protege"],[["Amparo","Derechos frente a actos u omisiones ilegales"],["Hábeas corpus","La libertad física"],["Hábeas data","Los datos personales"]])]),
 S(2,"Cómo funcionan",[P("Se presentan ante un juez, que revisa el caso de forma rápida. Si comprueba la violación, ordena que cese o que se repare.")]),
 S(2,"Por qué importan",[PN("Las garantías convierten los derechos en algo exigible. En la Argentina, el artículo 43 de la Constitución Nacional reconoce el amparo, el hábeas corpus y el hábeas data.","Las garantías convierten los derechos en algo exigible. En muchos países, la constitución reconoce el amparo, el hábeas corpus y el hábeas data.")])],
 {"titulo":"relacionar","planteo":"¿Qué diferencia hay entre un derecho y una garantía?","pasos":["El derecho es lo que se reconoce.","La garantía es la herramienta para reclamarlo.","Sin garantía, el derecho queda en el papel."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La herramienta para exigir un derecho es la ___ .","La garantía de la libertad física es el hábeas ___ ."]},
 {"titulo":"tu turno","planteo":"Explicá con tus palabras por qué un derecho necesita garantías."},
 {"titulo":"En el papel","texto":"Un derecho sin garantía puede quedar solo en el papel."},
 ["Creer que tener un derecho escrito alcanza.","Pensar que las garantías son solo para casos extremos."],
 RS(("Garantía","Herramienta para exigir derechos."),("Tipos","Amparo, hábeas corpus, hábeas data."),("Cómo","Ante un juez."),("Por qué","Derechos exigibles.")),
 G(("Garantía","Herramienta de protección."),("Amparo","Protege derechos frente a actos ilegales."),("Hábeas corpus","Protege la libertad física."),("Hábeas data","Protege los datos personales.")),
 ["¿Cómo se llama la herramienta para exigir que se cumpla un derecho?","¿Qué garantía protege la libertad física?","¿Qué garantía protege los datos personales?","¿Las garantías se presentan ante un juez? Respondé sí o no."],
 [["garantia","garantía","una garantia","una garantía"],["habeas corpus","hábeas corpus","el habeas corpus","el hábeas corpus"],["habeas data","hábeas data","el habeas data","el hábeas data"],["si","sí"]],
 {"incompleto":"Garantía. Corpus.","solo":"El derecho es lo que se reconoce; la garantía permite reclamarlo.","carpeta":["Garantía.","Hábeas corpus.","Hábeas data.","Sí."]})
B2=NV("Vas a explicar qué es el amparo, cuándo se usa y cómo se presenta.",["Qué es","Cuándo se usa","Cómo se presenta","Qué logra"],[
 S(1,"Qué es",[D("Amparo","Garantía que protege derechos reconocidos cuando una autoridad o un particular los lesiona o amenaza con actos u omisiones ilegales.")]),
 S(1,"Cuándo se usa",[T("Ejemplos",["Situación","Derecho en juego"],[["Una empresa de salud niega un tratamiento","Salud"],["Un municipio impide el acceso a una escuela","Educación"],["Se contamina un río de la zona","Ambiente sano"],["Se censura una publicación","Libre expresión"]])]),
 S(2,"Cómo se presenta",[P("Se presenta por escrito ante un juez, explicando el hecho, el derecho afectado y lo que se pide. Se tramita de manera más rápida que un juicio común.")]),
 S(2,"Qué logra",[PN("El juez puede ordenar que cese el acto o que se cumpla lo debido. En la Argentina, el amparo está previsto en el artículo 43 de la Constitución Nacional.","El juez puede ordenar que cese el acto o que se cumpla lo debido. En muchos países, el amparo tiene rango constitucional.")])],
 {"titulo":"aplicar","planteo":"Una obra social niega un medicamento necesario. ¿Qué podés hacer?","pasos":["Reunís los documentos del caso.","Presentás un amparo ante un juez.","El juez puede ordenar que se entregue el medicamento."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El amparo protege derechos frente a actos ___ .","Se presenta por escrito ante un ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una situación real o inventada donde convenga presentar un amparo."},
 {"titulo":"Rápido","texto":"El amparo existe para actuar rápido cuando un derecho está en peligro."},
 ["Pensar que el amparo solo se usa contra el Estado.","Creer que se necesita mucho tiempo para tramitarlo."],
 RS(("Amparo","Protege derechos."),("Uso","Ante actos ilegales."),("Cómo","Por escrito, ante un juez."),("Resultado","Cesa o se cumple.")),
 G(("Amparo","Garantía rápida de derechos."),("Acto ilegal","Hecho contrario a la ley."),("Omisión","No hacer lo debido."),("Particular","Persona o empresa privada.")),
 ["¿Qué garantía protege derechos frente a actos ilegales?","¿Ante quién se presenta un amparo?","¿El amparo puede usarse contra una empresa privada? Respondé sí o no.","¿El amparo es un trámite más rápido que un juicio común? Respondé sí o no."],
 [["amparo","el amparo"],["juez","un juez","ante un juez","el juez"],["si","sí"],["si","sí"]],
 {"incompleto":"Amparo. Juez.","solo":"Una obra social niega un medicamento: presento un amparo ante un juez.","carpeta":["Amparo.","Un juez.","Sí.","Sí."]})
B3=NV("Vas a explicar qué son el hábeas corpus y el hábeas data y en qué casos se usan.",["Hábeas corpus","Cuándo se usa","Hábeas data","Datos personales"],[
 S(1,"Hábeas corpus",[D("Hábeas corpus","Garantía que protege la libertad física: permite pedir a un juez que revise una detención ilegal o arbitraria.")]),
 S(1,"Cuándo se usa",[T("Casos",["Caso","Qué se pide"],[["Detención sin orden de un juez","Que el juez revise y libere si es ilegal"],["Traslado ilegal de un detenido","Que se corrija"],["Amenaza de detención arbitraria","Que se evite"]])]),
 S(2,"Hábeas data",[D("Hábeas data","Garantía que permite conocer qué datos personales tiene un registro, y pedir que se corrijan, actualicen o supriman si son falsos o discriminatorios.")]),
 S(2,"Datos personales",[PN("Hoy empresas y organismos guardan muchos datos nuestros. Por eso el hábeas data protege la intimidad. En la Argentina, una ley de protección de datos personales complementa esta garantía.","Hoy empresas y organismos guardan muchos datos nuestros. Por eso el hábeas data protege la intimidad. En muchos países, leyes de protección de datos personales complementan esta garantía.")])],
 {"titulo":"aplicar","planteo":"Una base de datos tiene información falsa sobre vos. ¿Qué garantía usás?","pasos":["Se trata de tus datos personales.","Usás el hábeas data.","Pedís que se corrija o se elimine."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La garantía de la libertad física es el hábeas ___ .","La garantía de los datos personales es el hábeas ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un caso para cada garantía."},
 {"titulo":"Mis datos","texto":"Tenés derecho a saber qué datos tuyos guardan los demás."},
 ["Confundir hábeas corpus con hábeas data.","Pensar que los datos personales no tienen protección."],
 RS(("Hábeas corpus","Libertad física."),("Hábeas data","Datos personales."),("Corpus","Detención ilegal."),("Data","Corregir información.")),
 G(("Hábeas corpus","Garantía contra detenciones ilegales."),("Hábeas data","Garantía sobre datos personales."),("Arbitrario","Sin razón válida."),("Intimidad","Vida privada.")),
 ["¿Qué garantía protege contra una detención ilegal?","¿Qué garantía permite corregir datos personales falsos?","¿El hábeas data protege la intimidad? Respondé sí o no.","¿Una detención sin orden judicial puede revisarse con hábeas corpus? Respondé sí o no."],
 [["habeas corpus","hábeas corpus","el habeas corpus","el hábeas corpus"],["habeas data","hábeas data","el habeas data","el hábeas data"],["si","sí"],["si","sí"]],
 {"incompleto":"Corpus. Data.","solo":"Hábeas data: pido corregir un dato falso sobre mí.","carpeta":["Hábeas corpus.","Hábeas data.","Sí.","Sí."]})
B4=NV("Vas a explicar qué es el acceso a la justicia y qué obstáculos y herramientas existen para ejercerlo.",["Qué es","Obstáculos","Herramientas","Qué puede hacer cada persona"],[
 S(1,"Qué es",[D("Acceso a la justicia","Posibilidad real de que toda persona reclame sus derechos ante un juez o un organismo y obtenga una respuesta justa y a tiempo.")]),
 S(1,"Obstáculos",[T("Qué lo dificulta",["Obstáculo","Ejemplo"],[["Económicos","Costo de un abogado o de un juicio"],["Geográficos","Vivir lejos de un tribunal"],["Culturales","No conocer los derechos o los trámites"],["De tiempo","Procesos muy largos"]])]),
 S(2,"Herramientas",[PN("Para facilitar el acceso existen la defensa pública gratuita, los servicios de asesoramiento, la mediación para resolver conflictos sin juicio y la gratuidad de ciertos trámites. En la Argentina funcionan además los centros de acceso a la justicia.","Para facilitar el acceso existen la defensa pública gratuita, los servicios de asesoramiento, la mediación para resolver conflictos sin juicio y la gratuidad de ciertos trámites. Muchos países tienen además oficinas de asistencia legal gratuita.")]),
 S(2,"Qué puede hacer cada persona",[P("Informarse sobre sus derechos, guardar pruebas, acudir a un servicio de asesoramiento gratuito y, si corresponde, presentar el reclamo ante el organismo o juez competente.")])],
 {"titulo":"aplicar","planteo":"Una persona no puede pagar un abogado. ¿Qué puede hacer?","pasos":["Acudir a la defensa pública gratuita.","Pedir asesoramiento en un servicio gratuito.","Presentar su reclamo con esa ayuda."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Resolver un conflicto sin juicio, con ayuda de una persona neutral, es la ___ .","El servicio gratuito de abogados para quien no puede pagar es la defensa ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres obstáculos para acceder a la justicia y una solución para cada uno."},
 {"titulo":"Justicia para todos","texto":"Un derecho que no se puede reclamar no sirve."},
 ["Pensar que sin dinero no se puede reclamar nada.","Creer que todo conflicto necesita juicio."],
 RS(("Acceso","Poder reclamar."),("Obstáculos","Dinero, distancia, desconocimiento."),("Herramientas","Defensa pública, mediación."),("Persona","Informarse y reclamar.")),
 G(("Acceso a la justicia","Posibilidad real de reclamar."),("Mediación","Resolver un conflicto con ayuda neutral."),("Defensa pública","Abogados gratuitos."),("Prueba","Dato que respalda un reclamo.")),
 ["¿Cómo se llama la posibilidad real de reclamar derechos ante la justicia?","¿Cómo se llama resolver un conflicto con ayuda neutral y sin juicio?","¿Existe la defensa pública gratuita? Respondé sí o no.","¿Vivir lejos de un tribunal puede ser un obstáculo? Respondé sí o no."],
 [["acceso a la justicia","el acceso a la justicia"],["mediacion","mediación","la mediacion","la mediación"],["si","sí"],["si","sí"]],
 {"incompleto":"Acceso. Mediación.","solo":"Sin dinero para un abogado: acudo a la defensa pública gratuita.","carpeta":["Acceso a la justicia.","Mediación.","Sí.","Sí."]})
ACT7={"1":[{"t":"matching","p":"Uní cada garantía con lo que protege.","o":{"izquierda":["Amparo","Hábeas corpus","Hábeas data"],"derecha":["Derechos frente a actos ilegales","Libertad física","Datos personales"]},"r":{"pares":{"Amparo":"Derechos frente a actos ilegales","Hábeas corpus":"Libertad física","Hábeas data":"Datos personales"}},"e":"Cada garantía, su objeto."},VF("Con tener el derecho escrito alcanza.","Falso","Hace falta una garantía para reclamarlo.")],
 "2":[MS("¿En qué casos conviene un amparo?",["Salud negada","Contaminación de un río","Censura","Cambiar de cancha de fútbol"],["Salud negada","Contaminación de un río","Censura"],"Cambiar de cancha no afecta un derecho."),FB("El amparo se presenta por escrito ante un ___ .",[["juez"]],"Ante un juez.")],
 "3":[{"t":"classify","p":"¿Hábeas corpus o hábeas data?","o":{"elementos":["Detención sin orden","Dato personal falso","Traslado ilegal de un detenido","Información privada mal usada"],"categorias":["Hábeas corpus","Hábeas data"]},"r":{"categorias":{"Detención sin orden":"Hábeas corpus","Dato personal falso":"Hábeas data","Traslado ilegal de un detenido":"Hábeas corpus","Información privada mal usada":"Hábeas data"}},"e":"Libertad por un lado, datos por otro."},VF("El hábeas data permite corregir datos falsos.","Verdadero","Corregir, actualizar o suprimir.")],
 "4":[{"t":"ordering","p":"Ordená los pasos para reclamar un derecho.","o":["Presentar el reclamo","Reunir pruebas","Informarse sobre los derechos","Buscar asesoramiento gratuito"],"r":{"orden":["Informarse sobre los derechos","Reunir pruebas","Buscar asesoramiento gratuito","Presentar el reclamo"]},"e":"De informarse a reclamar."},TT("Tocá los obstáculos: «El costo y la distancia dificultan el acceso a la justicia».",["El","costo","y","la","distancia","dificultan","el","acceso","a","la","justicia"],[1,4],"Dinero y distancia.")],
 "5":[MC("Relámpago. La garantía de la libertad física es…",["Hábeas corpus","Hábeas data","Amparo"],"Hábeas corpus","Contra detenciones ilegales.",tiempo=20),VF("Relámpago. El hábeas data protege los datos personales.","Verdadero","Permite corregirlos.",tiempo=20),MC("Relámpago. Resolver un conflicto sin juicio es…",["Mediación","Veto","Balotaje"],"Mediación","Ayuda neutral.",tiempo=20),VF("Relámpago. Sin dinero no se puede reclamar nada.","Falso","Hay defensa pública gratuita.",tiempo=20)]}
EX7=[[1,MC("Una garantía constitucional es…",["Una herramienta para exigir un derecho","Un derecho","Un impuesto","Un partido"],"Una herramienta para exigir un derecho","Protege los derechos.")],
 [1,MC("¿Ante quién se presenta una garantía?",["Un juez","Un partido","Un medio","Un vecino"],"Un juez","Revisa el caso.")],
 [1,VF("Un derecho sin garantía puede quedar en el papel.","Verdadero","Falta cómo reclamarlo.")],
 [2,MC("El amparo protege derechos frente a…",["Actos ilegales","Cualquier opinión","El clima","Los impuestos"],"Actos ilegales","Del Estado o de particulares.")],
 [2,MC("El amparo se presenta…",["Por escrito ante un juez","En la plaza","En un diario","Por teléfono"],"Por escrito ante un juez","Se tramita rápido.")],
 [2,VF("El amparo puede usarse contra una empresa privada.","Verdadero","Si lesiona un derecho.")],
 [3,MC("El hábeas corpus protege…",["La libertad física","Los datos personales","La propiedad","El voto"],"La libertad física","Contra detenciones ilegales.")],
 [3,MC("El hábeas data protege…",["Los datos personales","La libertad física","El trabajo","El ambiente"],"Los datos personales","Permite corregirlos.")],
 [3,VF("Una detención sin orden judicial puede revisarse con hábeas corpus.","Verdadero","Es su finalidad.")],
 [4,MC("El acceso a la justicia es…",["Poder reclamar derechos y obtener respuesta","Tener un juicio","Pagar abogados","Evitar reclamar"],"Poder reclamar derechos y obtener respuesta","Real y a tiempo.")],
 [4,MS("Obstáculos de acceso a la justicia:",["Costo","Distancia","Desconocimiento de derechos","Gratuidad de la defensa"],["Costo","Distancia","Desconocimiento de derechos"],"La defensa gratuita es una herramienta.")],
 [4,FB("Resolver un conflicto con ayuda neutral y sin juicio es la ___ .",[["mediacion","mediación"]],"Mediación.")],
 [4,VF("Existe la defensa pública gratuita para quien no puede pagar un abogado.","Verdadero","Facilita el acceso.")]]
M7={"subject_id":SID,"tema":7,"practica":"Práctica general: garantías para proteger derechos","examen_titulo":"Nivel jefe: garantías para proteger derechos","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT7,"examen":EX7}
for n,m in ((6,M6),(7,M7)):
    os.makedirs(os.path.join(AQUI,f"mision-{n}"),exist_ok=True); json.dump(m,open(os.path.join(AQUI,f"mision-{n}",f"mision-{n}.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={(6,1):"5e9c7abf-9857-46bc-8c16-e449b6f3dfbc",(6,2):"40989d93-f70c-4f1b-a28a-4d98741b7457",(6,3):"f9d4db73-b15b-4417-b07b-42b029474b3e",(6,4):"31a8e3df-9a2c-4b31-b309-ac46928e395f",(7,1):"9b22902c-87ed-459b-8ee1-c4e91a8fb9d2",(7,2):"d57e0bb7-af1d-4f4c-9f08-132cc8a1dbf3",(7,3):"8f97ce25-0b9e-46d2-aef1-3565b1c577ba",(7,4):"8798d051-e573-4726-b34e-1691caff18ed"}
TIT={(6,1):"Qué son los derechos humanos",(6,2):"La Declaración Universal de 1948",(6,3):"Derechos civiles, políticos, económicos y sociales",(6,4):"Tratados y pactos internacionales",(7,1):"Qué son las garantías constitucionales",(7,2):"El amparo",(7,3):"Hábeas corpus y hábeas data",(7,4):"Acceso a la justicia"}
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
CLS={(6,1):[
 RET("¿Quiénes tienen derechos humanos?",5,"Todas las personas","🌍","DERECHOS HUMANOS","qué son",["Desafío: ¿quiénes tienen derechos humanos? Cinco segundos.","Todas las personas.","Hoy: *qué son los derechos humanos*."]),
 DEF("Derechos humanos","Los que toda persona tiene por serlo","🧑‍🤝‍🧑",["Los *derechos humanos* son los que toda persona tiene por serlo.","Sin distinción de origen, sexo o religión."]),
 TB("CINCO RASGOS",["Rasgo","Significa"],[["Universales","Valen para todos"],["Inalienables","No se quitan"],["Indivisibles","No se separan"],["Interdependientes","Se relacionan"],["Progresivos","Se amplían"]],["Sus rasgos.","*Universales*: valen para todos.","*Inalienables*: no se quitan.","*Indivisibles*: no se separan.","*Interdependientes*: se relacionan.","Y *progresivos*: se amplían."]),
 CAU(("Graves violaciones",'⚠️'),[("Guerras y genocidios","💥"),("Nace la idea de protegerlos","💡"),("Se escriben en documentos","📜")],["Cómo surgieron.","Hubo *graves violaciones*.","Hubo *guerras y genocidios*.","Se pensó en *protegerlos*.","Y se escribieron *documentos*."]),
 CL([("DERECHO HUMANO","🧑‍🤝‍🧑"),("NO LO ES","❌")],[("Vivir con dignidad",0),("Un premio",1),("Educación",0)],["¿Derecho humano o no?","*Vivir con dignidad* y *educación*: lo son.","*Un premio*: no lo es."]),
 Q("Los derechos que no se pueden quitar son…",["Inalienables","Temporales","Opcionales"],0,["Te toca: los que no se pueden quitar.","¿Inalienables, temporales u opcionales?","Los *inalienables*."]),
 ER([("Se otorgan como un premio","Se tienen por ser persona"),("Unos valen más que otros","Son indivisibles")],["Errores típicos.","Creer que se *otorgan* como un premio.","Y que unos *valen más* que otros."]),
 RES(["Repasemos.","Son derechos de *toda persona*.","Son *universales* e *inalienables*.","También *indivisibles*.","Y se protegen para evitar *abusos*.","¡Clase terminada! Ahora, *a practicar*."],[["DERECHOS","de toda persona"],["RASGOS","universales"],["ORIGEN","graves violaciones"],["PROTECCIÓN","evitar abusos"]])],
(6,2):[
 NOT("1948","Se aprueba la Declaración Universal","Treinta artículos para todos","🌍","DECLARACIÓN UNIVERSAL","de 1948",["Noticia: se aprueba la Declaración Universal.","Treinta artículos para todos.","Hoy: *la Declaración Universal de mil novecientos cuarenta y ocho*."]),
 CAU(("Segunda Guerra Mundial",'💥'),[("Crímenes de guerra","⚠️"),("Se crea la ONU","🏛️"),("Se escribe la Declaración","📜")],["Cómo nació.","Terminó la *Segunda Guerra Mundial*.","Se conocieron los *crímenes*.","Se creó la *ONU*.","Y se escribió la *Declaración*."]),
 TB("IDEAS CENTRALES",["Idea","Dice"],[["Igualdad y dignidad","Todos nacemos iguales"],["No discriminación","Sin distinción"],["Vida y libertad","Sin esclavitud ni tortura"],["Derechos sociales","Trabajo, salud, educación"]],["Sus ideas.","*Igualdad y dignidad*.","*No discriminación*.","*Vida y libertad*.","Y *derechos sociales*."]),
 DEF("Declaración","Proclama principios","📜",["Una *declaración* proclama principios.","Tiene gran valor moral y político."]),
 CL([("DECLARACIÓN","📜"),("TRATADO","✍️")],[("Proclama principios",0),("Obliga por ley",1),("Inspira leyes",0)],["¿Declaración o tratado?","*Proclama principios* e *inspira leyes*: declaración.","*Obliga por ley*: tratado."]),
 Q("¿En qué año se aprobó la Declaración Universal?",["1948","1789","1994"],0,["Te toca: ¿en qué año se aprobó?","¿Mil novecientos cuarenta y ocho, mil setecientos ochenta y nueve o mil novecientos noventa y cuatro?","En *1948*."]),
 ER([("Es una ley obligatoria","Es una declaración"),("Solo trata de política","Incluye derechos sociales")],["Errores típicos.","Creer que es *ley obligatoria* por sí sola.","Y que *solo* trata de política."]),
 RES(["Repasemos.","Se aprobó en *1948*.","Nació tras la *guerra*.","Tiene *treinta artículos*.","Y tiene valor *moral* y político.","¡Clase terminada! Ahora, *a practicar*."],[["AÑO","1948"],["ORIGEN","posguerra"],["ARTÍCULOS","treinta"],["VALOR","moral y político"]])],
(6,3):[
 {"t":"gancho","grande":"Libres y dignos","emoji":"⚖️","final":"dos tipos de derechos","titulo":"TIPOS DE DERECHOS","sub":"civiles, políticos, sociales","voz":["Algunos derechos protegen la libertad.","Otros aseguran una vida digna.","Hoy: *derechos civiles, políticos, económicos y sociales*."]},
 TB("LIBERTAD",["Tipo","Ejemplos"],[["Civiles","Vida, expresión"],["Políticos","Votar, participar"]],["Protegen la libertad.","Los *civiles*: vida y expresión.","Los *políticos*: votar y participar."]),
 TB("VIDA DIGNA",["Tipo","Ejemplos"],[["Económicos","Trabajo, salario"],["Sociales","Salud, educación"],["Culturales","Idioma, cultura"]],["Aseguran una vida digna.","Los *económicos*: trabajo y salario.","Los *sociales*: salud y educación.","Los *culturales*: idioma y cultura."]),
 DEF("Solidaridad","Paz y ambiente sano","🌱",["Los derechos de *solidaridad* incluyen la paz y un ambiente sano.","Se ejercen entre todos."]),
 CL([("CIVIL O POLÍTICO","🗳️"),("ECONÓMICO O SOCIAL","🏥")],[("Votar",0),("Atención de salud",1),("Libre expresión",0),("Trabajo digno",1)],["¿De qué tipo?","*Votar* y *libre expresión*: civil o político.","*Salud* y *trabajo digno*: económico o social."]),
 Q("El derecho a votar es…",["Político","Social","Cultural"],0,["Te toca: el derecho a votar.","¿Político, social o cultural?","Es *político*."]),
 ER([("Los sociales son un favor","Son derechos"),("Solo importan los políticos","Todos están conectados")],["Errores típicos.","Creer que los sociales son *un favor*.","Y que *solo* importan los políticos."]),
 RES(["Repasemos.","Hay derechos *civiles* y *políticos*.","Otros son *económicos*, *sociales* y culturales.","También de *solidaridad*.","Y todos están *conectados*.","¡Clase terminada! Ahora, *a practicar*."],[["CIVILES","libertad"],["POLÍTICOS","participar"],["SOCIALES","vida digna"],["SOLIDARIDAD","paz y ambiente"]])],
(6,4):[
 RET("¿Cómo se llama aceptar obligarse por un tratado?",6,"Ratificar","✍️","TRATADOS Y PACTOS","internacionales",["Desafío: ¿cómo se llama aceptar obligarse por un tratado? Seis segundos.","Ratificar.","Hoy: *tratados y pactos internacionales*."]),
 DEF("Tratado internacional","Acuerdo escrito entre Estados","✍️",["Un *tratado internacional* es un acuerdo escrito entre Estados.","Los obliga jurídicamente."]),
 TB("EJEMPLOS",["Tratado","Protege"],[["Pacto civil (1966)","Libertades"],["Pacto social (1966)","Trabajo y salud"],["Convención Niño (1989)","Niñez"],["Convención Mujer (1979)","Igualdad"]],["Algunos tratados.","El *Pacto civil y político*: libertades.","El *Pacto económico y social*: trabajo y salud.","La *Convención del Niño*.","Y la de la *mujer*."]),
 CMP(("DECLARACIÓN","Proclama principios","📜"),("TRATADO","Obliga a quien ratifica","✍️"),"vs",["Dos instrumentos.","La *declaración* proclama.","El *tratado* obliga a quien lo ratifica."]),
 CL([("OBLIGA","✅"),("NO OBLIGA","❌")],[("Tratado ratificado",0),("Sin ratificar",1),("Pacto ratificado",0)],["¿Obliga o no?","*Tratado ratificado* y *pacto ratificado*: obligan.","*Sin ratificar*: no obliga."]),
 Q("Aceptar obligarse por un tratado es…",["Ratificar","Vetar","Votar"],0,["Te toca: aceptar obligarse por un tratado.","¿Ratificar, vetar o votar?","*Ratificar*."]),
 ER([("Obligan a quien no los ratificó","Solo a quien ratifica"),("No se pueden reclamar","Hay comités y tribunales")],["Errores típicos.","Creer que obligan a quien *no ratificó*.","Y que *no se pueden reclamar*."]),
 RES(["Repasemos.","Un *tratado* obliga jurídicamente.","Se *ratifica*.","Hay *pactos* y *convenciones*.","Y hay *comités* que controlan.","¡Clase terminada! Ahora, *a practicar*."],[["TRATADO","obliga"],["RATIFICAR","aceptar"],["EJEMPLOS","pactos"],["CONTROL","comités"]])],
(7,1):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"Tengo derecho a la salud, ¿no? 🏥"},{"yo":True,"txt":"Sí, pero ¿y si te lo niegan?"},{"yo":False,"txt":"¿Y entonces?"}],"titulo":"GARANTÍAS","sub":"para exigir derechos","voz":["Lu dice que tiene derecho a la salud.","Juan: sí, pero ¿y si te lo niegan?","Lu: ¿y entonces?","Hoy: *las garantías constitucionales*."]},
 DEF("Garantía","Herramienta para exigir un derecho","🛡️",["Una *garantía* es una herramienta para exigir un derecho.","Permite reclamar si alguien lo viola."]),
 TB("TRES GARANTÍAS",["Garantía","Protege"],[["Amparo","Derechos"],["Hábeas corpus","Libertad física"],["Hábeas data","Datos personales"]],["Tres garantías.","El *amparo*: derechos.","El *hábeas corpus*: libertad física.","El *hábeas data*: datos personales."]),
 PA("CÓMO SE USAN",[("Se presenta ante un juez","⚖️"),("El juez revisa rápido","⏱️"),("Ordena cesar o reparar","✅")],["Cómo funcionan.","Se presentan ante un *juez*.","El juez revisa *rápido*.","Y ordena *cesar* o reparar."]),
 CL([("DERECHO","⚖️"),("GARANTÍA","🛡️")],[("Salud",0),("Amparo",1),("Hábeas corpus",1)],["¿Derecho o garantía?","*Salud*: derecho.","*Amparo* y *hábeas corpus*: garantías."]),
 Q("La herramienta para exigir un derecho es la…",["Garantía","Veda","Banca"],0,["Te toca: herramienta para exigir un derecho.","¿Garantía, veda o banca?","La *garantía*."]),
 ER([("Tener el derecho escrito alcanza","Hace falta una garantía"),("Solo para casos extremos","Sirven en muchos casos")],["Errores típicos.","Creer que el derecho *escrito* alcanza.","Y que son *solo* para casos extremos."]),
 RES(["Repasemos.","Una *garantía* exige un derecho.","Hay *amparo*, *hábeas corpus* y *hábeas data*.","Se presentan ante un *juez*.","Y hacen los derechos *exigibles*.","¡Clase terminada! Ahora, *a practicar*."],[["GARANTÍA","herramienta"],["TIPOS","tres"],["DÓNDE","ante un juez"],["FIN","derechos exigibles"]])],
(7,2):[
 NOT("SALUD","Niegan un medicamento","Una familia presenta un amparo","💊","EL AMPARO","protege derechos",["Noticia: niegan un medicamento.","Una familia presenta un amparo.","Hoy: *el amparo*."]),
 DEF("Amparo","Protege derechos frente a actos ilegales","🛡️",["El *amparo* protege derechos frente a actos ilegales.","Del Estado o de particulares."]),
 TB("CUÁNDO SE USA",["Situación","Derecho"],[["Niegan tratamiento","Salud"],["Impiden escolarizar","Educación"],["Contaminan un río","Ambiente sano"],["Censuran","Expresión"]],["Casos de amparo.","Niegan un tratamiento: *salud*.","Impiden la escuela: *educación*.","Contaminan un río: *ambiente sano*.","Censuran: *expresión*."]),
 PA("CÓMO SE PRESENTA",[("Reunir pruebas","📁"),("Escribir el reclamo","✍️"),("Presentarlo ante un juez","⚖️")],["Para presentarlo.","*Reuní* pruebas.","*Escribí* el reclamo.","Y *presentalo* ante un juez."]),
 CL([("CONVIENE AMPARO","✅"),("NO CONVIENE","❌")],[("Salud negada",0),("Cambiar de cancha",1),("Censura",0)],["¿Conviene amparo?","*Salud negada* y *censura*: sí.","*Cambiar de cancha*: no."]),
 Q("¿Ante quién se presenta un amparo?",["Un juez","Un partido","Un medio"],0,["Te toca: ¿ante quién se presenta?","¿Un juez, un partido o un medio?","Ante *un juez*."]),
 ER([("Solo contra el Estado","También contra particulares"),("Tarda años","Se tramita rápido")],["Errores típicos.","Creer que es *solo contra el Estado*.","Y que *tarda años*."]),
 RES(["Repasemos.","El *amparo* protege derechos.","Se usa ante *actos ilegales*.","Se presenta ante un *juez*.","Y busca que *cese* o se cumpla.","¡Clase terminada! Ahora, *a practicar*."],[["AMPARO","protege derechos"],["USO","actos ilegales"],["CÓMO","ante un juez"],["RESULTADO","cesa o se cumple"]])],
(7,3):[
 RET("¿Qué garantía protege contra una detención ilegal?",6,"Hábeas corpus","⛓️","HÁBEAS CORPUS","y hábeas data",["Desafío: ¿qué garantía protege contra una detención ilegal? Seis segundos.","Hábeas corpus.","Hoy: *hábeas corpus y hábeas data*."]),
 DEF("Hábeas corpus","Protege la libertad física","⛓️",["El *hábeas corpus* protege la libertad física.","Permite revisar una detención ilegal."]),
 DEF("Hábeas data","Protege los datos personales","🗂️",["El *hábeas data* protege los datos personales.","Permite corregirlos o suprimirlos."]),
 CMP(("HÁBEAS CORPUS","Contra detenciones ilegales","⛓️"),("HÁBEAS DATA","Sobre datos personales","🗂️"),"vs",["Dos garantías.","El *corpus* protege la libertad.","El *data* protege la información."]),
 CL([("CORPUS","⛓️"),("DATA","🗂️")],[("Detención sin orden",0),("Dato falso",1),("Traslado ilegal",0),("Información privada",1)],["¿Corpus o data?","*Detención sin orden* y *traslado ilegal*: corpus.","*Dato falso* e *información privada*: data."]),
 Q("¿Qué garantía permite corregir datos personales falsos?",["Hábeas data","Hábeas corpus","Amparo"],0,["Te toca: corregir datos personales falsos.","¿Hábeas data, hábeas corpus o amparo?","El *hábeas data*."]),
 ER([("Confundir corpus con data","Corpus es libertad; data es información"),("Los datos no tienen protección","Se protegen")],["Errores típicos.","Confundir *corpus* con *data*.","Y creer que los datos *no se protegen*."]),
 RES(["Repasemos.","El *corpus* protege la libertad.","El *data* protege los datos personales.","Se presentan ante un *juez*.","Y cuidan la *intimidad*.","¡Clase terminada! Ahora, *a practicar*."],[["CORPUS","libertad física"],["DATA","datos personales"],["DÓNDE","ante un juez"],["FIN","intimidad"]])],
(7,4):[
 NOT("JUSTICIA","Sin dinero para un abogado","Hay defensa pública gratuita","⚖️","ACCESO A LA JUSTICIA","derechos que se pueden reclamar",["Noticia: sin dinero para un abogado.","Hay defensa pública gratuita.","Hoy: *acceso a la justicia*."]),
 DEF("Acceso a la justicia","Poder reclamar y obtener respuesta","⚖️",["El *acceso a la justicia* es poder reclamar derechos.","Y obtener una respuesta justa y a tiempo."]),
 TB("OBSTÁCULOS",["Obstáculo","Ejemplo"],[["Económicos","Costo"],["Geográficos","Distancia"],["Culturales","No conocer derechos"],["De tiempo","Procesos largos"]],["Qué lo dificulta.","Los *económicos*: el costo.","Los *geográficos*: la distancia.","Los *culturales*: no conocer derechos.","Y los de *tiempo*."]),
 TB("HERRAMIENTAS",["Herramienta","Qué hace"],[["Defensa pública","Abogados gratis"],["Mediación","Sin juicio"],["Asesoramiento","Orienta"]],["Para facilitar el acceso.","La *defensa pública*: abogados gratis.","La *mediación*: sin juicio.","Y el *asesoramiento*: orienta."]),
 CL([("OBSTÁCULO","🚧"),("HERRAMIENTA","🛠️")],[("Distancia",0),("Defensa pública",1),("Costo",0),("Mediación",1)],["¿Obstáculo o herramienta?","*Distancia* y *costo*: obstáculos.","*Defensa pública* y *mediación*: herramientas."]),
 Q("Resolver un conflicto con ayuda neutral y sin juicio es…",["Mediación","Veto","Balotaje"],0,["Te toca: resolver sin juicio con ayuda neutral.","¿Mediación, veto o balotaje?","La *mediación*."]),
 ER([("Sin dinero no se puede reclamar","Hay defensa gratuita"),("Todo conflicto necesita juicio","Se puede mediar")],["Errores típicos.","Creer que *sin dinero* no se puede reclamar.","Y que todo conflicto necesita *juicio*."]),
 RES(["Repasemos.","El *acceso* es poder reclamar.","Hay obstáculos *económicos*, *geográficos* y culturales.","Existen *defensa pública* y *mediación*.","Y cada persona puede *informarse*.","¡Clase terminada! Ahora, *a practicar*."],[["ACCESO","poder reclamar"],["OBSTÁCULOS","dinero, distancia"],["HERRAMIENTAS","defensa, mediación"],["PERSONA","informarse"]])]}
for (m,n),es in CLS.items():
    json.dump({"sin_variante":True,"slug":f"ciud1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Ciudadanía I","titulo":TIT[(m,n)],"sub":f"Ciudadanía I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"ciud1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
