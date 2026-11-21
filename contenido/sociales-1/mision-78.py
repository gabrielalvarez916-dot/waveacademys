# -*- coding: utf-8 -*-
"""Ciencias Sociales Integradas I · Misión 7 (La población mundial) y Misión 8 (Campo y ciudad en el mundo actual). Ambas COMUN."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}
SID = "a5f9b6fc-7f3b-4743-977d-da7f4f3a37bb"

# ================= MISIÓN 7: LA POBLACIÓN MUNDIAL =================
A1=NV("Vas a explicar cuántas personas somos, dónde vivimos y cómo se calcula la densidad de población.",["Cuántos somos","Dónde vivimos","La densidad de población","Zonas pobladas y despobladas"],[
 S(1,"Cuántos somos",[P("La población mundial superó los <b>8.000 millones</b> de personas en 2022. Más de la mitad vive en Asia, y los países más poblados son India y China, seguidos por Estados Unidos, Indonesia y Pakistán.")]),
 S(1,"La densidad",[D("Densidad de población","Cantidad de habitantes por kilómetro cuadrado: habitantes ÷ superficie."),E("Calcular","Una ciudad tiene 1.200 habitantes y ocupa 40 km².",["Se divide: 1.200 ÷ 40.","Densidad: 30 habitantes por km²."])]),
 S(2,"Pobladas y despobladas",[T("Dónde vive la gente",["Zonas","Por qué"],[["Muy pobladas","Llanuras, costas, valles de ríos y ciudades: hay agua, suelo fértil y trabajo"],["Poco pobladas","Desiertos, polos, selvas densas y altas montañas: clima extremo o difícil acceso"]]),P("Una densidad alta no siempre significa pobreza ni riqueza: hay países muy densos y ricos, y otros muy densos y pobres.")])],
 {"titulo":"calcular","planteo":"Un país tiene 300.000 habitantes y 10.000 km². ¿Cuál es su densidad?","pasos":["Se divide la población por la superficie.","300.000 ÷ 10.000 = 30.","Tiene 30 habitantes por km²."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La densidad se mide en habitantes por ___ cuadrado.","El continente con más habitantes es ___ ."]},
 {"titulo":"tu turno","planteo":"Un lugar tiene 900 habitantes y 30 km². Calculá su densidad y decí si te parece alta o baja."},
 {"titulo":"Dividí","texto":"Densidad = habitantes ÷ superficie. No es lo mismo que el total de habitantes."},
 ["Creer que más habitantes significa más densidad.","Pensar que una población grande ocupa siempre mucho espacio."],
 RS(("Población","Más de 8.000 millones."),("Asia","Más de la mitad."),("Densidad","Habitantes ÷ km²."),("Poco pobladas","Desiertos, polos, montañas.")),
 G(("Población","Conjunto de habitantes de un lugar."),("Densidad","Habitantes por kilómetro cuadrado."),("Superficie","Tamaño de un territorio.")),
 ["Una ciudad tiene 1.200 habitantes y 40 km². ¿Cuál es su densidad? Respondé solo el número.","¿Qué continente concentra más de la mitad de la población mundial?","Los desiertos, ¿están muy poblados o poco poblados?","¿Cuántos miles de millones de personas somos aproximadamente? Respondé solo el número."],
 [["30"],["asia"],["poco poblados","poco","poco poblado"],["8","ocho"]],
 {"incompleto":"Kilómetro. Asia.","solo":"900 ÷ 30 = 30 habitantes por km²: es una densidad baja a media.","carpeta":["30.","Asia.","Poco poblados.","8."]})
A2=NV("Vas a calcular la natalidad, la mortalidad y el crecimiento natural, y a leer una pirámide de población.",["Natalidad y mortalidad","Crecimiento natural","Pirámides de población"],[
 S(1,"Natalidad y mortalidad",[T("Dos tasas",["Tasa","Qué mide"],[["Natalidad","Nacimientos por cada 1.000 habitantes en un año"],["Mortalidad","Muertes por cada 1.000 habitantes en un año"]])]),
 S(1,"Crecimiento natural",[D("Crecimiento natural","Natalidad − mortalidad."),E("Calcular","Natalidad 18 ‰ y mortalidad 8 ‰.",["Se resta: 18 − 8.","Son 10 por mil.","La población crece 1 % al año."])]),
 S(2,"Pirámides",[T("Cómo leerlas",["Forma","Qué indica"],[["Base ancha","Muchos nacimientos: población joven"],["Base angosta y cima ancha","Pocos nacimientos y vida larga: población envejecida"]]),P("Cada barra es un grupo de edad; la izquierda suele mostrar varones y la derecha, mujeres.")])],
 {"titulo":"interpretar","planteo":"Una pirámide tiene la base muy angosta y la parte de arriba ancha. ¿Qué indica?","pasos":["Hay pocos niños.","Hay muchos adultos mayores.","Es una población envejecida."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Natalidad menos mortalidad es el crecimiento ___ .","Una base ancha indica población ___ ."]},
 {"titulo":"tu turno","planteo":"Un país tiene natalidad 25 ‰ y mortalidad 9 ‰. Calculá el crecimiento natural."},
 {"titulo":"Restá","texto":"Si nacen más de los que mueren, la población crece; si no, se achica."},
 ["Sumar natalidad y mortalidad en lugar de restar.","Confundir una base ancha con población envejecida."],
 RS(("Natalidad","Nacimientos por mil."),("Mortalidad","Muertes por mil."),("Crecimiento","Natalidad − mortalidad."),("Pirámide","Base ancha: joven.")),
 G(("Tasa","Cantidad por cada mil habitantes."),("Crecimiento natural","Diferencia entre natalidad y mortalidad."),("Pirámide de población","Gráfico de la población por edad y sexo.")),
 ["Natalidad 20 ‰ y mortalidad 7 ‰. ¿Cuál es el crecimiento natural? Respondé solo el número.","Una pirámide de base ancha, ¿indica población joven o envejecida?","¿Qué mide la tasa de natalidad?","¿Qué se resta para calcular el crecimiento natural? Respondé \"natalidad menos mortalidad\" o \"mortalidad menos natalidad\"."],
 [["13"],["joven","joven."],["nacimientos","los nacimientos","nacimientos por mil"],["natalidad menos mortalidad"]],
 {"incompleto":"Natural. Joven.","solo":"25 − 9 = 16 por mil.","carpeta":["13.","Joven.","Los nacimientos.","Natalidad menos mortalidad."]})
A3=NV("Vas a explicar por qué y hacia dónde se mueve la gente y qué consecuencias tienen las migraciones.",["Qué es migrar","Por qué migran","Tipos de migración","Consecuencias"],[
 S(1,"Qué es migrar",[D("Migración","Traslado de personas de un lugar a otro para vivir en él."),T("Dos caras",["Quien...","Se llama"],[["Sale de su lugar","Emigrante"],["Llega a otro lugar","Inmigrante"]])]),
 S(1,"Por qué migran",[T("Causas",["Causa","Ejemplo"],[["Económicas","Buscar trabajo o mejor sueldo"],["Políticas","Guerras o persecuciones: son refugiados"],["Ambientales","Sequías, inundaciones, terremotos"],["Familiares","Reunirse con parientes"]])]),
 S(2,"Tipos y consecuencias",[T("Tipos",["Tipo","Ejemplo"],[["Interna","Del campo a la ciudad dentro del mismo país"],["Internacional","De un país a otro"]]),P("Las migraciones cambian a los lugares: las ciudades crecen, el campo pierde gente joven y las culturas se mezclan; también pueden aparecer discriminación y falta de vivienda.")])],
 {"titulo":"clasificar","planteo":"Una familia deja su pueblo por una sequía y se muda a la capital de su país. ¿Qué tipo de migración es y por qué causa?","pasos":["Se queda dentro del mismo país: es interna.","Se fue por una sequía: causa ambiental.","Va del campo a la ciudad."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Quien sale de su país es un ___ .","Quien huye de una guerra es un ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una causa y una consecuencia de las migraciones."},
 {"titulo":"Dos puntos de vista","texto":"Un mismo viaje es emigración para el país de salida e inmigración para el de llegada."},
 ["Confundir emigrar con inmigrar.","Creer que se migra solo por trabajo."],
 RS(("Emigrante","Sale."),("Inmigrante","Llega."),("Refugiado","Huye de guerra."),("Interna","Dentro del país.")),
 G(("Migración","Traslado de personas para vivir en otro lugar."),("Refugiado","Persona que huye de una guerra o persecución."),("Éxodo rural","Migración del campo a la ciudad.")),
 ["¿Cómo se llama a la persona que sale de su país para vivir en otro?","¿Cómo se llama a la persona que huye de una guerra?","Una migración del campo a la ciudad dentro del mismo país, ¿es interna o internacional?","Buscar trabajo, ¿es una causa económica o política?"],
 [["emigrante","un emigrante","el emigrante"],["refugiado","un refugiado","el refugiado"],["interna","es interna"],["economica","económica","es economica","es económica"]],
 {"incompleto":"Emigrante. Refugiado.","solo":"Causa: buscar trabajo. Consecuencia: las ciudades crecen.","carpeta":["Emigrante.","Refugiado.","Interna.","Económica."]})
A4=NV("Vas a usar indicadores para comparar las condiciones de vida y explicar las desigualdades.",["Qué es un indicador","El IDH","Desigualdades"],[
 S(1,"Indicadores",[T("Indicadores de calidad de vida",["Indicador","Qué muestra"],[["Esperanza de vida","Años que se espera vivir"],["Mortalidad infantil","Bebés que mueren antes de cumplir un año"],["Alfabetización","Personas que saben leer y escribir"],["Acceso al agua potable","Personas con agua segura"]])]),
 S(1,"El IDH",[D("Índice de Desarrollo Humano (IDH)","Indicador del PNUD, de la ONU, que combina salud (esperanza de vida), educación y nivel de ingreso."),P("Va de 0 a 1: cuanto más cerca de 1, mejores son las condiciones de vida.")]),
 S(2,"Desigualdades",[P("Hay desigualdades <b>entre países</b>, como entre algunos del norte y del sur, y <b>dentro</b> de un mismo país, entre ciudad y campo o entre barrios. Un promedio nacional puede esconder grandes diferencias.")])],
 {"titulo":"comparar","planteo":"País A: esperanza de vida 82 años y mortalidad infantil baja. País B: 58 años y mortalidad infantil alta. ¿Cuál tiene mejores condiciones?","pasos":["Más años de vida indica mejor salud.","Menos mortalidad infantil también.","El país A tiene mejores condiciones."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El IDH combina salud, educación e ___ .","Un IDH cercano a 1 indica ___ condiciones de vida."]},
 {"titulo":"tu turno","planteo":"Explicá por qué un promedio nacional puede esconder desigualdades."},
 {"titulo":"Un solo número no alcanza","texto":"Mirá varios indicadores juntos y mirá también las diferencias dentro del país."},
 ["Creer que un indicador alcanza para comparar países.","Pensar que dentro de un país todos viven igual."],
 RS(("Indicadores","Esperanza de vida y más."),("IDH","Salud, educación e ingreso."),("Rango","De 0 a 1."),("Desigualdad","Entre y dentro de países.")),
 G(("Indicador","Dato que mide un aspecto de la vida de una población."),("IDH","Índice de Desarrollo Humano."),("PNUD","Programa de las Naciones Unidas para el Desarrollo.")),
 ["¿Qué indicador combina salud, educación e ingreso?","Una mortalidad infantil alta, ¿indica mejores o peores condiciones de vida?","¿Qué número es el máximo del IDH? Respondé solo el número.","¿Hay desigualdades dentro de un mismo país? Respondé sí o no."],
 [["idh","el idh","indice de desarrollo humano","índice de desarrollo humano"],["peores","peores condiciones"],["1","uno"],["si","sí"]],
 {"incompleto":"Ingreso. Mejores.","solo":"Porque el promedio mezcla a quienes viven muy bien y a quienes viven muy mal.","carpeta":["El IDH.","Peores.","1.","Sí."]})
ACT7={"1":[N("Un lugar tiene {h} habitantes y 10 km². ¿Cuál es su densidad?",{"formula":"h/10"},"Se divide la población por la superficie.",{"vars":{"h":{"valores":[200,500,1000,3000]}}}),MC("¿Dónde vive más gente?",["Llanuras y costas","Desiertos","Polos","Altas montañas"],"Llanuras y costas","Hay agua, suelo fértil y trabajo.")],
 "2":[{"t":"classify","p":"¿Qué indica la pirámide?","o":{"elementos":["Base ancha","Base angosta y cima ancha","Muchos nacimientos","Pocos nacimientos"],"categorias":["Población joven","Población envejecida"]},"r":{"categorias":{"Base ancha":"Población joven","Base angosta y cima ancha":"Población envejecida","Muchos nacimientos":"Población joven","Pocos nacimientos":"Población envejecida"}},"e":"La base muestra los nacimientos."},MC("El crecimiento natural es…",["Natalidad − mortalidad","Natalidad + mortalidad","Mortalidad − natalidad","Natalidad × mortalidad"],"Natalidad − mortalidad","Se restan.")],
 "3":[{"t":"classify","p":"¿Causa económica, política o ambiental?","o":{"elementos":["Buscar trabajo","Huir de una guerra","Una sequía larga","Mejor sueldo"],"categorias":["Económica","Política","Ambiental"]},"r":{"categorias":{"Buscar trabajo":"Económica","Huir de una guerra":"Política","Una sequía larga":"Ambiental","Mejor sueldo":"Económica"}},"e":"Cada causa tiene su motivo."},MC("Quien llega a un país para vivir en él es un…",["Inmigrante","Emigrante","Turista de paso","Refugiado de guerra necesariamente"],"Inmigrante","Llega al lugar nuevo.")],
 "4":[{"t":"matching","p":"Uní cada indicador con lo que mide.","o":{"izquierda":["Esperanza de vida","Mortalidad infantil","Alfabetización","IDH"],"derecha":["Años que se espera vivir","Bebés que mueren antes del año","Personas que saben leer y escribir","Salud, educación e ingreso"]},"r":{"pares":{"Esperanza de vida":"Años que se espera vivir","Mortalidad infantil":"Bebés que mueren antes del año","Alfabetización":"Personas que saben leer y escribir","IDH":"Salud, educación e ingreso"}},"e":"Cada indicador mide algo distinto."},MC("Un IDH cercano a 1 indica…",["Mejores condiciones de vida","Peores condiciones de vida","Más población","Menos superficie"],"Mejores condiciones de vida","Es el máximo.")],
 "5":[MC("Relámpago. La densidad es habitantes por…",["km²","litro","año"],"km²","Habitantes ÷ superficie.",tiempo=20),MC("Relámpago. La base ancha de una pirámide indica población…",["Joven","Envejecida","Extinta"],"Joven","Muchos nacimientos.",tiempo=20),MC("Relámpago. Quien huye de una guerra es un…",["Refugiado","Turista","Comerciante"],"Refugiado","Causa política.",tiempo=20),MC("Relámpago. El IDH combina salud, educación e…",["Ingreso","Clima","Relieve"],"Ingreso","Va de 0 a 1.",tiempo=20)]}
EX7=[[1,N("Una ciudad tiene 600 habitantes y 30 km². ¿Cuál es su densidad? Respondé solo el número.",{"acepta":[20]},"600 ÷ 30 = 20.")],
 [1,MC("¿Qué continente concentra más de la mitad de la población mundial?",["Asia","África","Europa","América"],"Asia","Allí están India y China.")],
 [1,VF("Los desiertos son zonas muy pobladas.","Falso","Tienen clima extremo y pocos recursos.")],
 [2,N("Natalidad 22 ‰ y mortalidad 8 ‰. ¿Cuál es el crecimiento natural? Respondé solo el número.",{"acepta":[14]},"22 − 8 = 14.")],
 [2,MC("Una pirámide con la base angosta indica…",["Población envejecida","Población joven","Más nacimientos","Menos edades"],"Población envejecida","Pocos nacimientos.")],
 [2,VF("La tasa de natalidad mide las muertes por mil habitantes.","Falso","Mide los nacimientos.")],
 [3,MC("Quien sale de su país para vivir en otro es…",["Emigrante","Inmigrante","Refugiado siempre","Turista"],"Emigrante","Inmigrante es quien llega.")],
 [3,MC("Una migración dentro del mismo país es…",["Interna","Internacional","Imposible","Continental"],"Interna","Como del campo a la ciudad.")],
 [3,VF("Todas las migraciones tienen causas económicas.","Falso","Hay causas políticas, ambientales y familiares.")],
 [4,MC("El IDH combina…",["Salud, educación e ingreso","Clima y relieve","Natalidad y mortalidad","Densidad y superficie"],"Salud, educación e ingreso","Lo calcula el PNUD.")],
 [4,MC("Una mortalidad infantil alta indica…",["Peores condiciones de vida","Mejores condiciones de vida","Más educación","Más ingreso"],"Peores condiciones de vida","Menos salud.")],
 [4,MC("¿Un promedio nacional puede esconder desigualdades?",["Sí","No","Solo en países pequeños","Nunca"],"Sí","Hay diferencias entre barrios y regiones.")],
 [4,VF("Dentro de un mismo país todos viven igual.","Falso","Hay desigualdades internas.")]]
M7={"subject_id":SID,"tema":7,"practica":"Práctica general: la población mundial","examen_titulo":"Nivel jefe: la población mundial","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT7,"examen":EX7}

# ================= MISIÓN 8: CAMPO Y CIUDAD EN EL MUNDO ACTUAL =================
B1=NV("Vas a clasificar las actividades económicas en sectores y explicar cómo se conectan en una cadena productiva.",["Los tres sectores","Ejemplos de cada sector","La cadena productiva"],[
 S(1,"Los tres sectores",[T("Sectores de la economía",["Sector","Qué hace","Ejemplos"],[["Primario","Obtiene recursos de la naturaleza","Agricultura, ganadería, pesca, minería"],["Secundario","Transforma las materias primas","Industria, construcción"],["Terciario","Presta servicios","Comercio, transporte, salud, educación"]])]),
 S(1,"Una cadena productiva",[P("Muchos productos pasan por los tres sectores: el trigo se cosecha (primario), se muele y se hace pan en una fábrica (secundario) y se vende en una panadería (terciario). Cada etapa agrega <b>valor</b>.")]),
 S(2,"Cambios en el trabajo",[P("En el mundo actual, el sector terciario es el que más empleos da: crecen los servicios, mientras que la agricultura necesita menos personas porque se mecanizó.")])],
 {"titulo":"clasificar","planteo":"¿A qué sector pertenece una fábrica de galletitas?","pasos":["Transforma harina, azúcar y otras materias primas.","Eso es industria.","Es del sector secundario."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La pesca pertenece al sector ___ .","El comercio pertenece al sector ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un producto de tu casa y describí su cadena: ¿qué se hace en cada sector?"},
 {"titulo":"Verbo clave","texto":"Primario: obtener. Secundario: transformar. Terciario: servir."},
 ["Pensar que servicios son solo comercio.","Creer que cada producto pertenece a un solo sector."],
 RS(("Primario","Obtiene."),("Secundario","Transforma."),("Terciario","Presta servicios."),("Cadena","Pasa por los tres.")),
 G(("Sector económico","Grupo de actividades con una función parecida."),("Materia prima","Recurso sin elaborar."),("Servicio","Actividad que satisface una necesidad sin producir un objeto.")),
 ["¿Qué sector transforma las materias primas?","La minería, ¿a qué sector pertenece?","La educación, ¿a qué sector pertenece?","La pesca, ¿a qué sector pertenece?"],
 [["secundario","el secundario"],["primario","el primario"],["terciario","el terciario"],["primario","el primario"]],
 {"incompleto":"Primario. Terciario.","solo":"Ejemplo: leche (primario), yogur (secundario) y supermercado (terciario).","carpeta":["El secundario.","Primario.","Terciario.","Primario."]})
B2=NV("Vas a explicar cómo cambió el trabajo en el campo, de la agricultura a la agroindustria.",["Agricultura de subsistencia y comercial","La agroindustria","Tecnología en el campo","Cambios en la población rural"],[
 S(1,"Dos tipos de agricultura",[T("Comparar",["","Subsistencia","Comercial"],[["Para qué","Para consumo propio","Para vender"],["Tecnología","Poca: trabajo manual","Mucha: maquinaria e insumos"],["Escala","Chica","Grande"]])]),
 S(1,"La agroindustria",[D("Agroindustria","Industria que procesa productos del campo: jugos, aceites, harinas, lácteos, conservas."),P("Une el sector primario con el secundario: el productor y la fábrica trabajan en una misma cadena.")]),
 S(2,"Tecnología y población rural",[T("Qué cambió",["Cambio","Efecto"],[["Mecanización","Menos trabajadores por hectárea"],["Semillas mejoradas y agroquímicos","Más rendimiento, pero también riesgos ambientales"],["Agricultura de precisión (GPS, drones)","Se aplica cada insumo donde hace falta"]]),P("Como el campo necesita menos mano de obra, mucha gente joven migra a las ciudades.")])],
 {"titulo":"explicar","planteo":"¿Por qué el campo moderno ocupa menos personas que antes?","pasos":["Las máquinas hacen el trabajo de muchas personas.","La agricultura de precisión ahorra tareas.","Por eso sobra mano de obra y muchos migran a la ciudad."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La agricultura para consumo propio es de ___ .","La industria que procesa productos del campo es la ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un producto agroindustrial y decí qué materia prima usa."},
 {"titulo":"Del campo a la fábrica","texto":"Para reconocer la agroindustria, preguntate si el producto del campo se procesa antes de llegar al consumidor."},
 ["Creer que todo el campo es igual de tecnificado.","Pensar que la tecnología no tiene riesgos."],
 RS(("Subsistencia","Para consumir."),("Comercial","Para vender."),("Agroindustria","Campo + fábrica."),("Precisión","GPS y drones.")),
 G(("Agroindustria","Industria que procesa productos del campo."),("Mecanización","Uso de máquinas en lugar de trabajo manual."),("Agricultura de precisión","Uso de GPS y sensores para aplicar insumos justo donde se necesitan.")),
 ["La agricultura que produce para el consumo propio, ¿es de subsistencia o comercial?","¿Cómo se llama la industria que procesa productos del campo?","¿Qué tecnología usa GPS y drones para cuidar los cultivos?","Un jugo de naranja envasado, ¿es un producto agroindustrial? Respondé sí o no."],
 [["subsistencia","de subsistencia"],["agroindustria","la agroindustria"],["agricultura de precision","agricultura de precisión","precision","precisión"],["si","sí"]],
 {"incompleto":"Subsistencia. Agroindustria.","solo":"Aceite de girasol: usa semillas de girasol.","carpeta":["De subsistencia.","La agroindustria.","La agricultura de precisión.","Sí."]})
B3=NV("Vas a describir cómo se organiza una ciudad y los problemas que enfrenta.",["Las zonas de una ciudad","Usos del suelo","Servicios y redes","Problemas urbanos"],[
 S(1,"Las zonas",[T("Cómo se organiza",["Zona","Qué hay"],[["Centro","Comercios, oficinas, edificios altos y administración"],["Barrios residenciales","Casas y edificios de vivienda"],["Zona industrial","Fábricas y depósitos"],["Periferia","Barrios que van creciendo; a veces con pocos servicios"],["Espacios verdes","Plazas y parques"]])]),
 S(1,"Servicios y redes",[P("Una ciudad necesita redes de agua potable, cloacas, electricidad, transporte y comunicaciones. Cuando una ciudad crece muy rápido, esas redes no siempre llegan a todos los barrios.")]),
 S(2,"Problemas urbanos",[T("Problemas frecuentes",["Problema","Causa"],[["Tránsito","Muchos autos y poco transporte público"],["Falta de vivienda","Crecimiento rápido y precios altos"],["Basura","Mucha población y pocos sistemas de reciclado"],["Desigualdad","Algunos barrios con todos los servicios y otros sin ellos"]])])],
 {"titulo":"ubicar","planteo":"¿En qué zona de la ciudad es más probable encontrar edificios de oficinas y bancos?","pasos":["Los bancos y oficinas necesitan mucho movimiento.","Por eso están en el centro.","Es la zona de comercios y administración."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los barrios que crecen en las afueras forman la ___ .","El agua potable y las cloacas son ___ de servicios."]},
 {"titulo":"tu turno","planteo":"Describí tu barrio: ¿qué zona de la ciudad es y qué servicios tiene?"},
 {"titulo":"Mirá el uso","texto":"Para clasificar una zona, mirá para qué se usa el suelo: vivir, trabajar, producir o descansar."},
 ["Creer que todos los barrios tienen los mismos servicios.","Pensar que la ciudad es un único espacio homogéneo."],
 RS(("Centro","Comercio y oficinas."),("Residencial","Viviendas."),("Periferia","Crece."),("Redes","Agua, luz, transporte.")),
 G(("Periferia","Zona de las afueras de una ciudad."),("Uso del suelo","Para qué se utiliza un terreno."),("Red de servicios","Conjunto de conexiones que llevan agua, luz y otros servicios.")),
 ["¿Cómo se llama la zona con comercios, oficinas y edificios altos?","¿Cómo se llama la zona de las afueras de la ciudad?","¿Las fábricas están en la zona industrial o en los espacios verdes?","¿Todos los barrios tienen los mismos servicios? Respondé sí o no."],
 [["centro","el centro"],["periferia","la periferia"],["industrial","zona industrial","la zona industrial"],["no"]],
 {"incompleto":"Periferia. Redes.","solo":"Respuesta personal: zona y servicios.","carpeta":["El centro.","La periferia.","La zona industrial.","No."]})
B4=NV("Vas a explicar cómo la tecnología reorganiza el campo y la ciudad y qué es la brecha digital.",["Internet y trabajo","Comercio y logística","Tecnología en el campo y la ciudad","Brecha digital"],[
 S(1,"Internet y trabajo",[P("Con Internet se puede <b>teletrabajar</b>: trabajar a distancia. Algunas personas se mudan a pueblos más tranquilos, y las empresas ya no necesitan tantas oficinas en el centro.")]),
 S(1,"Comercio y logística",[T("Qué cambió",["Cambio","Efecto en el territorio"],[["Comercio electrónico","Menos locales, más depósitos y repartos"],["Transporte en contenedores","Los productos viajan por barco, tren y camión"],["Trenes y rutas de alta velocidad","Conectan ciudades y campos con rapidez"]])]),
 S(2,"Campo y ciudad inteligentes",[T("Tecnologías",["Dónde","Ejemplo"],[["Campo","Drones y GPS en la agricultura de precisión"],["Ciudad","Semáforos inteligentes, transporte con aplicaciones, sensores"]])]),
 S(2,"Brecha digital",[D("Brecha digital","Diferencia de acceso a Internet y a dispositivos entre personas o lugares."),P("En muchas zonas rurales, la conexión es lenta o no existe: eso limita la educación, el trabajo y el acceso a servicios.")])],
 {"titulo":"analizar","planteo":"¿Cómo cambia una ciudad si crece mucho el comercio electrónico?","pasos":["Se compra más desde casa.","Hacen falta depósitos y más repartos.","Cambia el tránsito y la forma de los barrios."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Trabajar a distancia se llama ___ .","La diferencia de acceso a Internet es la brecha ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una tecnología que haya cambiado la vida en tu barrio o en un campo que conozcas."},
 {"titulo":"Conectar es incluir","texto":"Cuando analices una tecnología, preguntate también quién queda sin acceso."},
 ["Pensar que la tecnología llega igual a todos los lugares.","Creer que el comercio electrónico no necesita territorio."],
 RS(("Teletrabajo","A distancia."),("Comercio electrónico","Más repartos."),("Precisión","Drones y GPS."),("Brecha digital","Desigual acceso.")),
 G(("Teletrabajo","Trabajo a distancia usando Internet."),("Logística","Organización del transporte y almacenamiento de productos."),("Brecha digital","Desigualdad en el acceso a Internet.")),
 ["¿Cómo se llama el trabajo a distancia por Internet?","¿Cómo se llama la diferencia de acceso a Internet entre personas o lugares?","¿Qué tecnología usa drones y GPS para cuidar los cultivos?","¿El comercio electrónico necesita depósitos y repartos? Respondé sí o no."],
 [["teletrabajo","el teletrabajo"],["brecha digital","la brecha digital"],["agricultura de precision","agricultura de precisión","precision","precisión"],["si","sí"]],
 {"incompleto":"Teletrabajo. Digital.","solo":"Respuesta personal: una tecnología y su efecto.","carpeta":["Teletrabajo.","La brecha digital.","La agricultura de precisión.","Sí."]})
ACT8={"1":[{"t":"classify","p":"¿A qué sector pertenece?","o":{"elementos":["Cosechar trigo","Fábrica de galletitas","Escuela","Pesca"],"categorias":["Primario","Secundario","Terciario"]},"r":{"categorias":{"Cosechar trigo":"Primario","Fábrica de galletitas":"Secundario","Escuela":"Terciario","Pesca":"Primario"}},"e":"Obtener, transformar, servir."},MC("¿Qué sector emplea a más personas en el mundo actual?",["Terciario","Primario","Secundario","Ninguno"],"Terciario","Crecen los servicios.")],
 "2":[{"t":"classify","p":"¿Subsistencia o comercial?","o":{"elementos":["Huerta para comer en casa","Campo que exporta soja","Cultivo manual de una familia","Gran plantación con maquinaria"],"categorias":["Subsistencia","Comercial"]},"r":{"categorias":{"Huerta para comer en casa":"Subsistencia","Campo que exporta soja":"Comercial","Cultivo manual de una familia":"Subsistencia","Gran plantación con maquinaria":"Comercial"}},"e":"Depende del destino."},MC("La agroindustria es la industria que…",["Procesa productos del campo","Fabrica máquinas","Presta servicios","Extrae petróleo"],"Procesa productos del campo","Une campo e industria.")],
 "3":[{"t":"matching","p":"Uní cada zona con lo que hay.","o":{"izquierda":["Centro","Periferia","Zona industrial","Espacio verde"],"derecha":["Oficinas y comercios","Barrios en crecimiento","Fábricas","Plazas y parques"]},"r":{"pares":{"Centro":"Oficinas y comercios","Periferia":"Barrios en crecimiento","Zona industrial":"Fábricas","Espacio verde":"Plazas y parques"}},"e":"Cada zona tiene su uso."},MC("¿Cuál es un problema urbano?",["El tránsito","La cosecha","El pastoreo","La pesca"],"El tránsito","Muchos autos y poco transporte público.")],
 "4":[{"t":"classify","p":"¿Tecnología del campo o de la ciudad?","o":{"elementos":["Drones y GPS","Semáforos inteligentes","Agricultura de precisión","Transporte con aplicaciones"],"categorias":["Campo","Ciudad"]},"r":{"categorias":{"Drones y GPS":"Campo","Semáforos inteligentes":"Ciudad","Agricultura de precisión":"Campo","Transporte con aplicaciones":"Ciudad"}},"e":"Cada ámbito, sus tecnologías."},MC("La brecha digital es…",["La diferencia de acceso a Internet","Una grieta en el suelo","Un tipo de cultivo","Un servicio de transporte"],"La diferencia de acceso a Internet","Limita la educación y el trabajo.")],
 "5":[MC("Relámpago. La minería es del sector…",["Primario","Secundario","Terciario"],"Primario","Obtiene recursos.",tiempo=20),MC("Relámpago. La agroindustria une el campo con la…",["Industria","Escuela","Plaza"],"Industria","Procesa productos.",tiempo=20),MC("Relámpago. Las oficinas están sobre todo en el…",["Centro","Campo","Mar"],"Centro","Zona de comercio y administración.",tiempo=20),MC("Relámpago. Trabajar a distancia es…",["Teletrabajo","Éxodo rural","Subsistencia"],"Teletrabajo","Por Internet.",tiempo=20)]}
EX8=[[1,MC("¿Qué sector transforma materias primas?",["Secundario","Primario","Terciario","Ninguno"],"Secundario","Es la industria.")],
 [1,MC("El comercio pertenece al sector…",["Terciario","Primario","Secundario","Extractivo"],"Terciario","Presta servicios.")],
 [1,VF("Un producto pasa por un solo sector.","Falso","Suele pasar por los tres.")],
 [2,MC("La agricultura de subsistencia produce…",["Para consumo propio","Solo para exportar","Para fábricas","Para vender caro"],"Para consumo propio","Es de escala chica.")],
 [2,MC("La mecanización del campo provocó…",["Menos trabajadores por hectárea","Más trabajadores","Menos cosecha","Menos rendimiento"],"Menos trabajadores por hectárea","Las máquinas reemplazan trabajo manual.")],
 [2,VF("La agroindustria procesa productos del campo.","Verdadero","Como jugos, aceites y harinas.")],
 [3,MC("¿Dónde están la mayoría de los comercios y oficinas?",["En el centro","En la periferia","En el campo","En el mar"],"En el centro","Es la zona más activa.")],
 [3,MC("La periferia es…",["La zona de las afueras","El centro","Un parque","Una fábrica"],"La zona de las afueras","Suele crecer rápido.")],
 [3,VF("Todos los barrios de una ciudad tienen los mismos servicios.","Falso","Hay desigualdades.")],
 [4,MC("El teletrabajo es…",["Trabajar a distancia por Internet","Trabajar de noche","Trabajar en una fábrica","Trabajar en el campo"],"Trabajar a distancia por Internet","Cambia dónde se vive y se trabaja.")],
 [4,MC("La brecha digital es…",["La desigualdad de acceso a Internet","Un tipo de cultivo","Un barrio","Un servicio de transporte"],"La desigualdad de acceso a Internet","Limita educación y trabajo.")],
 [4,MC("La agricultura de precisión usa…",["GPS y drones","Solo arado manual","Cartas","Radio"],"GPS y drones","Aplica insumos donde hacen falta.")],
 [4,VF("La tecnología llega igual a todos los lugares.","Falso","Hay brecha digital.")]]
M8={"subject_id":SID,"tema":8,"practica":"Práctica general: campo y ciudad en el mundo actual","examen_titulo":"Nivel jefe: campo y ciudad en el mundo actual","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT8,"examen":EX8}
for n,m in ((7,M7),(8,M8)):
    os.makedirs(os.path.join(AQUI,f"mision-{n}"),exist_ok=True); json.dump(m,open(os.path.join(AQUI,f"mision-{n}",f"mision-{n}.json"),"w"),ensure_ascii=False)

# ================= CLASES ANIMADAS =================
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={(5,1):"3029e488-5ba8-4032-b5fd-dd5a3a00cfa3",(5,2):"e6acbef3-5c27-474d-bb7c-54247c97bec1",(5,3):"dd05e528-5f20-4e8f-9a40-107f5b9ebd8a",(5,4):"06577aa6-32ec-469f-b28d-f43f2316036a",(6,1):"5e1454b9-74fb-43f0-9f22-19c1bf1a9c6f",(6,2):"0ef71248-d8a1-4e6a-9c78-7f8eacf2bcde",(6,3):"2a1555cb-959d-402a-aa6c-e7e544072c25",(6,4):"fed71c24-110e-4701-9ac7-ce1834d85f60"}
TIT={(5,1):"Recursos que se renuevan y recursos que se agotan",(5,2):"Petróleo, gas y carbón: recursos estratégicos",(5,3):"El agua: un recurso que no se reparte parejo",(5,4):"Minerales y cultivos que mueven la economía mundial",(6,1):"Suelos que se degradan: erosión y expansión agrícola",(6,2):"Contaminación del aire, el agua y la tierra",(6,3):"Cambio climático y fenómenos extremos",(6,4):"Políticas ambientales: de las cumbres a la comunidad"}
RES=lambda v,items:{"t":"resumen","voz":v,"items":items,"fin":{"titulo":"¡CLASE TERMINADA!","sub":"Ahora, a practicar 🚀"}}
Q=lambda p,o,c,v:{"t":"pregunta","pregunta":p,"opciones":o,"correcta":c,"voz":v}
ER=lambda it,v:{"t":"errores","items":[{"mal":a,"bien":b} for a,b in it],"voz":v}
DEF=lambda w,t,e,v:{"t":"definicion","palabra":w,"texto":t,"emoji":e,"voz":v}
CMP=lambda a,b,s,v:{"t":"comparar","a":{"cab":a[0],"texto":a[1],"emoji":a[2]},"b":{"cab":b[0],"texto":b[1],"emoji":b[2]},"signo":s,"voz":v}
TB=lambda t,c,f,v:{"t":"tabla","titulo":t,"columnas":c,"filas":f,"voz":v}
CAU=lambda c,it,v:{"t":"causas","causa":{"txt":c[0],"emoji":c[1]},"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
AD=lambda a,d,v:{"t":"antesdespues","antes":{"cab":a[0],"emoji":a[1],"texto":a[2]},"despues":{"cab":d[0],"emoji":d[1],"texto":d[2]},"voz":v}
DA=lambda n,a,d,t,e,v:{"t":"dato","numero":n,"antes":a,"despues":d,"texto":t,"emoji":e,"voz":v}
CL=lambda cj,fi,v:{"t":"clasificar","cajas":[{"cab":a,"emoji":b} for a,b in cj],"fichas":[{"txt":a,"caja":b} for a,b in fi],"voz":v}
PA=lambda t,it,v:{"t":"pasos","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
def NEU(e,**k): e=dict(e); e["neutro"]=k; return e
STEPS={(7,1):"58e4949e-1f3e-408e-8bfa-88b4b4046b9e",(7,2):"4ea01feb-73a8-4bda-b0ae-c75b8ff4a491",(7,3):"d3591306-0ffe-4b17-b75f-ef4ddf09592e",(7,4):"ee7ec63c-b37c-4dec-a7d2-b3bb80042f3e",(8,1):"13884cf2-1909-44bc-84f7-e238534d0a70",(8,2):"b5c1a162-2eec-4627-b615-07d8573276ad",(8,3):"a1d26376-b802-4088-bad0-3972acc8c4dd",(8,4):"23e37342-25f4-4723-8e54-48a5c98bb327"}
TIT={(7,1):"Cuántos somos y dónde vivimos",(7,2):"Natalidad, mortalidad y pirámides de población",(7,3):"Por qué y hacia dónde se mueve la gente",(7,4):"Condiciones de vida: indicadores y desigualdades",(8,1):"Sectores de la economía y actividades productivas",(8,2):"Espacios rurales: del cultivo a la agroindustria",(8,3):"Espacios urbanos: cómo se organiza una ciudad",(8,4):"Tecnologías que reorganizan el territorio"}
RES=lambda v,items:{"t":"resumen","voz":v,"items":items,"fin":{"titulo":"¡CLASE TERMINADA!","sub":"Ahora, a practicar 🚀"}}
Q=lambda p,o,c,v:{"t":"pregunta","pregunta":p,"opciones":o,"correcta":c,"voz":v}
ER=lambda it,v:{"t":"errores","items":[{"mal":a,"bien":b} for a,b in it],"voz":v}
DEF=lambda w,t,e,v:{"t":"definicion","palabra":w,"texto":t,"emoji":e,"voz":v}
CMP=lambda a,b,s,v:{"t":"comparar","a":{"cab":a[0],"texto":a[1],"emoji":a[2]},"b":{"cab":b[0],"texto":b[1],"emoji":b[2]},"signo":s,"voz":v}
TB=lambda t,c,f,v:{"t":"tabla","titulo":t,"columnas":c,"filas":f,"voz":v}
CAU=lambda c,it,v:{"t":"causas","causa":{"txt":c[0],"emoji":c[1]},"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
DA=lambda n,a,d,t,e,v:{"t":"dato","numero":n,"antes":a,"despues":d,"texto":t,"emoji":e,"voz":v}
CL=lambda cj,fi,v:{"t":"clasificar","cajas":[{"cab":a,"emoji":b} for a,b in cj],"fichas":[{"txt":a,"caja":b} for a,b in fi],"voz":v}
PA=lambda t,it,v:{"t":"pasos","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
CLS={(7,1):[
 {"t":"noticia","cinta":"HITO MUNDIAL","titular":"Ya somos más de 8.000 millones","bajada":"Y la mitad vive en Asia","emoji":"🌍","titulo":"LA POBLACIÓN","sub":"cuántos somos y dónde vivimos","voz":["Hito mundial: ya somos más de ocho mil millones de personas.","Y más de la mitad vive en Asia.","Hoy: *la población mundial*."]},
 DA("8.000","millones de personas","viven en el planeta","Superamos esa cifra en 2022","👥",["Somos más de *ocho mil millones* de personas.","Superamos esa cifra en el año dos mil veintidós."]),
 {"t":"mapa","zona":"mundo","pasos":[{"resaltar":["India","China"],"color":"#c0392b","texto":"Los más poblados"},{"resaltar":["Estados Unidos","Indonesia","Pakistán"],"color":"#d9a441","texto":"Otros muy poblados"}],"voz":["Los países más poblados.","*India* y *China* encabezan la lista.","Les siguen *Estados Unidos*, *Indonesia* y *Pakistán*."]},
 DEF("Densidad de población","Habitantes por kilómetro cuadrado","📏",["La *densidad* se calcula dividiendo los habitantes por la superficie.","Se mide en habitantes por kilómetro cuadrado."]),
 PA("CALCULAR LA DENSIDAD",[("Tomá los habitantes","👥"),("Tomá la superficie","📐"),("Dividí","➗")],["Tres pasos.","Tomá los *habitantes*: por ejemplo, mil doscientos.","Tomá la *superficie*: cuarenta kilómetros cuadrados.","*Dividí*: mil doscientos entre cuarenta da treinta habitantes por kilómetro cuadrado."]),
 CL([("MUY POBLADAS","🏙️"),("POCO POBLADAS","🏜️")],[("Costas",0),("Desiertos",1),("Valles de ríos",0),("Polos",1)],["¿Dónde vive más gente?","*Costas* y *valles de ríos*: hay agua y suelo fértil.","*Desiertos* y *polos*: clima extremo."]),
 Q("Una ciudad tiene 600 habitantes y 30 kilómetros cuadrados. ¿Cuál es su densidad?",["20","30","180"],0,["Te toca: seiscientos habitantes en treinta kilómetros cuadrados.","¿Veinte, treinta o ciento ochenta?","Seiscientos entre treinta da *veinte* habitantes por kilómetro cuadrado."]),
 ER([("Más habitantes es más densidad","Depende de la superficie"),("Los desiertos están muy poblados","Están poco poblados")],["Errores típicos.","Creer que *más habitantes* siempre es *más densidad*.","Y pensar que los *desiertos* están muy poblados."]),
 RES(["Repasemos.","Somos más de *ocho mil millones*.","Más de la mitad vive en *Asia*.","La *densidad* es habitantes entre superficie.","Y la gente vive donde hay *agua* y *trabajo*.","¡Clase terminada! Ahora, *a practicar*."],[["POBLACIÓN","más de 8.000 millones"],["ASIA","más de la mitad"],["DENSIDAD","habitantes ÷ km²"],["POBLADAS","costas y llanuras"]])],
(7,2):[
 {"t":"chat","contacto":{"nombre":"Abu","emoji":"👵"},"mensajes":[{"yo":False,"txt":"En mi época éramos 8 hermanos"},{"yo":True,"txt":"¡Hoy casi nadie tiene tantos!"},{"yo":False,"txt":"Cambió la población, nieta 😊"}],"titulo":"NATALIDAD Y MORTALIDAD","sub":"y pirámides de población","voz":["Abu le cuenta a su nieta que en su época eran ocho hermanos.","La nieta dice que hoy casi nadie tiene tantos.","Abu: cambió la población.","Hoy: *natalidad*, *mortalidad* y *pirámides*."]},
 TB("DOS TASAS",["Tasa","Qué mide"],[["Natalidad","Nacimientos por mil"],["Mortalidad","Muertes por mil"]],["Dos tasas básicas.","La *natalidad*: nacimientos por cada mil habitantes en un año.","La *mortalidad*: muertes por cada mil habitantes en un año."]),
 DEF("Crecimiento natural","Natalidad menos mortalidad","➕",["El *crecimiento natural* se calcula restando.","Natalidad menos mortalidad."]),
 PA("UN EJEMPLO",[("Natalidad: 18","👶"),("Mortalidad: 8","🕯️"),("18 − 8 = 10","➖")],["Un ejemplo.","Natalidad: *dieciocho* por mil.","Mortalidad: *ocho* por mil.","Dieciocho menos ocho: crece *diez por mil*, un uno por ciento."]),
 CMP(("BASE ANCHA","Muchos nacimientos","👶"),("BASE ANGOSTA","Pocos nacimientos y vida larga","👴"),"vs",["Así se lee una pirámide.","La *base ancha* indica muchos nacimientos: población *joven*.","La *base angosta* con la cima ancha indica población *envejecida*."]),
 CL([("JOVEN","👶"),("ENVEJECIDA","👴")],[("Base ancha",0),("Cima ancha",1),("Muchos nacimientos",0)],["¿Joven o envejecida?","*Base ancha* y *muchos nacimientos*: joven.","*Cima ancha*: envejecida."]),
 Q("Natalidad veinte por mil y mortalidad siete por mil. ¿Cuál es el crecimiento natural?",["13","27","3"],0,["Te toca: natalidad veinte y mortalidad siete.","¿Trece, veintisiete o tres?","Se *resta*: veinte menos siete, *trece*."]),
 ER([("Sumar natalidad y mortalidad","Se restan"),("Base ancha = envejecida","Base ancha = joven")],["Errores típicos.","*Sumar* las dos tasas en lugar de restar.","Y confundir *base ancha* con población envejecida."]),
 RES(["Repasemos.","La *natalidad* mide nacimientos.","La *mortalidad*, muertes.","El *crecimiento natural* es la resta.","Y la *pirámide* muestra la edad de la población.","¡Clase terminada! Ahora, *a practicar*."],[["NATALIDAD","nacimientos por mil"],["MORTALIDAD","muertes por mil"],["CRECIMIENTO","natalidad − mortalidad"],["PIRÁMIDE","base ancha: joven"]])],
(7,3):[
 {"t":"historia","personaje":{"nombre":"Amina","emoji":"👩"},"lugar":"🧳","lineas":["Amina dejó su ciudad por la guerra.","Llegó a otro país con una valija y mucha esperanza."],"titulo":"MIGRACIONES","sub":"por qué y hacia dónde se mueve la gente","voz":["Amina dejó su ciudad por la guerra.","Llegó a otro país con una valija y mucha esperanza.","Hoy: las *migraciones*."]},
 DEF("Migración","Traslado de personas para vivir en otro lugar","🚶",["Una *migración* es el traslado de personas para vivir en otro lugar.","Quien sale es *emigrante*; quien llega, *inmigrante*."]),
 CAU(("Por qué se migra",'🧭'),[("Económicas","💼"),("Políticas","🕊️"),("Ambientales","🌪️"),("Familiares","👪")],["Hay muchas causas.","*Económicas*: buscar trabajo o mejor sueldo.","*Políticas*: guerras y persecuciones; quienes huyen son *refugiados*.","*Ambientales*: sequías, inundaciones o terremotos.","Y *familiares*: reunirse con parientes."]),
 CMP(("INTERNA","Dentro del mismo país","🏙️"),("INTERNACIONAL","De un país a otro","✈️"),"vs",["Hay dos tipos.","La *interna*: por ejemplo, del campo a la ciudad.","La *internacional*: de un país a otro."]),
 CL([("EMIGRANTE","⬅️"),("INMIGRANTE","➡️")],[("Sale de su país",0),("Llega a otro país",1)],["¿Emigrante o inmigrante?","El que *sale* es emigrante.","El que *llega* es inmigrante."]),
 Q("Alguien huye de una guerra. ¿Cómo se llama?",["Refugiado","Turista","Comerciante"],0,["Te toca: alguien huye de una guerra.","¿Refugiado, turista o comerciante?","*Refugiado*."]),
 TB("CONSECUENCIAS",["Lugar","Cambio"],[["Ciudades","Crecen"],["Campo","Pierde gente joven"],["Culturas","Se mezclan"]],["Las migraciones cambian los lugares.","Las *ciudades* crecen.","El *campo* pierde gente joven.","Y las *culturas* se mezclan."]),
 ER([("Emigrar = inmigrar","Salir y llegar"),("Solo se migra por trabajo","Hay varias causas")],["Errores típicos.","Confundir *emigrar* con *inmigrar*.","Y creer que se migra *solo por trabajo*."]),
 RES(["Repasemos.","Migrar es *trasladarse*.","Se migra por causas *económicas*, políticas, ambientales y familiares.","Puede ser *interna* o *internacional*.","Y cambia a los lugares.","¡Clase terminada! Ahora, *a practicar*."],[["EMIGRANTE","sale"],["INMIGRANTE","llega"],["REFUGIADO","huye de guerra"],["INTERNA","dentro del país"]])],
(7,4):[
 {"t":"reto","texto":"¿Dónde se vive más años: en un país rico o en uno pobre?","segundos":6,"respuesta":"En general, en el país con mejores condiciones de vida","emoji":"🌍","titulo":"CONDICIONES DE VIDA","sub":"indicadores y desigualdades","voz":["Desafío: ¿dónde se vive más años, en un país rico o en uno pobre? Seis segundos.","En general, se vive más donde hay mejores condiciones de vida.","Hoy: *indicadores* y *desigualdades*."]},
 TB("INDICADORES",["Indicador","Qué muestra"],[["Esperanza de vida","Años que se espera vivir"],["Mortalidad infantil","Bebés que mueren antes del año"],["Alfabetización","Saber leer y escribir"]],["Algunos indicadores.","La *esperanza de vida*: cuántos años se espera vivir.","La *mortalidad infantil*: bebés que mueren antes de cumplir un año.","La *alfabetización*: personas que saben leer y escribir."]),
 DEF("IDH","Combina salud, educación e ingreso","📊",["El *Índice de Desarrollo Humano* lo calcula el PNUD, de la ONU.","Combina salud, educación e ingreso, y va de cero a uno."]),
 CMP(("IDH CERCANO A 1","Mejores condiciones","📈"),("IDH BAJO","Peores condiciones","📉"),"vs",["Cómo se lee.","Un IDH *cercano a uno* indica mejores condiciones de vida.","Un IDH *bajo*, peores condiciones."]),
 CAU(("Desigualdades",'⚖️'),[("Entre países","🌐"),("Dentro del país","🏘️")],["Hay desigualdades de dos tipos.","*Entre países*, como del norte y del sur.","Y *dentro* de un mismo país, entre ciudad y campo o entre barrios."]),
 CL([("MEJORES CONDICIONES","📈"),("PEORES CONDICIONES","📉")],[("Vive más años",0),("Mueren más bebés",1),("Saben leer",0)],["¿Mejores o peores condiciones?","*Vivir más años* y *saber leer*: mejores.","*Que mueran más bebés*: peores."]),
 Q("¿Qué indicador combina salud, educación e ingreso?",["El IDH","La densidad","La natalidad"],0,["Te toca: ¿qué indicador combina salud, educación e ingreso?","¿El IDH, la densidad o la natalidad?","El *IDH*."]),
 ER([("Un indicador alcanza","Conviene mirar varios"),("Dentro del país todos viven igual","Hay desigualdades internas")],["Errores típicos.","Creer que *un indicador* alcanza.","Y pensar que dentro de un país *todos viven igual*."]),
 RES(["Repasemos.","Los *indicadores* miden la calidad de vida.","El *IDH* combina salud, educación e ingreso.","Va de *cero a uno*.","Y hay *desigualdades* entre y dentro de los países.","¡Clase terminada! Ahora, *a practicar*."],[["INDICADORES","miden la vida"],["IDH","salud, educación, ingreso"],["RANGO","de 0 a 1"],["DESIGUALDAD","entre y dentro"]])],
(8,1):[
 {"t":"historia","personaje":{"nombre":"Pablo","emoji":"👦"},"lugar":"🍞","lineas":["Pablo se preguntó de dónde viene su pan.","Del trigo, del molino y de la panadería."],"titulo":"SECTORES","sub":"de la economía","voz":["Pablo se preguntó de dónde viene su pan.","Del trigo, del molino y de la panadería.","Hoy: los *sectores de la economía*."]},
 TB("LOS TRES SECTORES",["Sector","Qué hace","Ejemplo"],[["Primario","Obtiene","Pesca, minería"],["Secundario","Transforma","Industria"],["Terciario","Presta servicios","Comercio, salud"]],["Tres sectores.","El *primario* obtiene recursos de la naturaleza: pesca, minería, agricultura.","El *secundario* los transforma: la industria.","El *terciario* presta servicios: comercio, transporte, salud y educación."]),
 PA("LA CADENA DEL PAN",[("Cosechar trigo","🌾"),("Moler y hacer pan","🏭"),("Vender en la panadería","🛒")],["Una cadena productiva.","Se *cosecha* el trigo: sector primario.","Se *muele* y se hace pan: sector secundario.","Se *vende* en la panadería: sector terciario."]),
 DEF("Valor agregado","Valor que suma cada etapa de la cadena","➕",["Cada etapa agrega *valor* al producto.","Un kilo de trigo vale menos que el mismo trigo convertido en pan."]),
 CL([("PRIMARIO","⛏️"),("SECUNDARIO","🏭"),("TERCIARIO","🛒")],[("Pesca",0),("Fábrica de pan",1),("Escuela",2)],["¿A qué sector pertenece cada una?","La *pesca*: primario.","La *fábrica*: secundario.","La *escuela*: terciario."]),
 Q("¿Qué sector transforma las materias primas?",["Secundario","Primario","Terciario"],0,["Te toca: ¿qué sector transforma las materias primas?","¿Secundario, primario o terciario?","El *secundario*: la industria."]),
 DEF("Cambio actual","El terciario es el que más empleos da","📈",["Hoy el sector *terciario* es el que más empleos da.","La agricultura necesita menos gente porque se mecanizó."]),
 ER([("Servicios son solo comercio","Incluyen salud, educación y más"),("Un producto es de un solo sector","Pasa por los tres")],["Errores típicos.","Creer que *servicios* son solo comercio.","Y pensar que un producto es *de un solo sector*."]),
 RES(["Repasemos.","El *primario* obtiene.","El *secundario* transforma.","El *terciario* presta servicios.","Y la *cadena* pasa por los tres.","¡Clase terminada! Ahora, *a practicar*."],[["PRIMARIO","obtiene"],["SECUNDARIO","transforma"],["TERCIARIO","servicios"],["CADENA","suma valor"]])],
(8,2):[
 {"t":"gancho","grande":"1 tractor","emoji":"🚜","final":"100 trabajadores","titulo":"EL CAMPO ACTUAL","sub":"del cultivo a la agroindustria","voz":["Un tractor moderno puede hacer el trabajo de muchísimos trabajadores.","¿Qué le pasó al campo?","Hoy: *del cultivo a la agroindustria*."]},
 CMP(("SUBSISTENCIA","Para consumo propio","🥕"),("COMERCIAL","Para vender","🚜"),"vs",["Dos tipos de agricultura.","La de *subsistencia*: se produce para comer en casa, casi sin tecnología.","La *comercial*: se produce para vender, con maquinaria e insumos."]),
 DEF("Agroindustria","Industria que procesa productos del campo","🥫",["La *agroindustria* procesa productos del campo.","Jugos, aceites, harinas, lácteos y conservas."]),
 PA("TECNOLOGÍA EN EL CAMPO",[("Mecanización","🚜"),("Semillas mejoradas","🌱"),("GPS y drones","📡")],["Tres cambios.","La *mecanización*: máquinas en lugar de trabajo manual.","Las *semillas mejoradas* y los agroquímicos: más rendimiento, con riesgos ambientales.","Y la *agricultura de precisión*: GPS y drones."]),
 CAU(("Menos gente en el campo",'🏙️'),[("Más máquinas","🚜"),("Migran los jóvenes","🚶")],["¿Por qué hay menos gente en el campo?","Porque hay *más máquinas*.","Y muchos *jóvenes migran* a las ciudades."]),
 CL([("SUBSISTENCIA","🥕"),("COMERCIAL","🚜")],[("Huerta familiar",0),("Exportar soja",1),("Cultivo familiar",0)],["¿Subsistencia o comercial?","La *huerta familiar* y el *cultivo manual*: subsistencia.","*Exportar soja*: comercial."]),
 Q("¿Cómo se llama la industria que procesa productos del campo?",["Agroindustria","Minería","Pesca"],0,["Te toca: ¿cómo se llama la industria que procesa productos del campo?","¿Agroindustria, minería o pesca?","La *agroindustria*."]),
 ER([("Todo el campo es igual de tecnificado","Hay mucha diferencia"),("La tecnología no tiene riesgos","Puede dañar el ambiente")],["Errores típicos.","Creer que *todo el campo* está igual de tecnificado.","Y pensar que la tecnología *no tiene riesgos*."]),
 RES(["Repasemos.","Hay agricultura de *subsistencia* y *comercial*.","La *agroindustria* procesa el campo.","La *tecnología* reduce el trabajo manual.","Y muchos jóvenes *migran* a la ciudad.","¡Clase terminada! Ahora, *a practicar*."],[["SUBSISTENCIA","para consumir"],["COMERCIAL","para vender"],["AGROINDUSTRIA","campo + fábrica"],["PRECISIÓN","GPS y drones"]])],
(8,3):[
 {"t":"noticia","cinta":"TRÁNSITO","titular":"Hora pico: la ciudad no se mueve","bajada":"Millones llegan al centro cada mañana","emoji":"🚗","titulo":"LA CIUDAD","sub":"cómo se organiza","voz":["Hora pico: la ciudad no se mueve.","Millones de personas llegan al centro cada mañana.","Hoy: *cómo se organiza una ciudad*."]},
 TB("ZONAS DE LA CIUDAD",["Zona","Qué hay"],[["Centro","Comercio y oficinas"],["Residencial","Viviendas"],["Industrial","Fábricas"],["Periferia","Barrios en crecimiento"]],["Las zonas de una ciudad.","El *centro*: comercios, oficinas y edificios altos.","Los barrios *residenciales*: viviendas.","La zona *industrial*: fábricas.","Y la *periferia*: los barrios que van creciendo."]),
 DEF("Uso del suelo","Para qué se usa cada terreno","🗺️",["El *uso del suelo* es para qué se utiliza cada terreno.","Vivir, trabajar, producir o descansar."]),
 CAU(("Redes de servicios",'🔌'),[("Agua y cloacas","🚰"),("Electricidad","💡"),("Transporte","🚌")],["Una ciudad necesita redes.","*Agua y cloacas*.","*Electricidad*.","Y *transporte*. Si la ciudad crece muy rápido, no siempre llegan a todos."]),
 CL([("CENTRO","🏢"),("PERIFERIA","🏘️")],[("Bancos y oficinas",0),("Barrios nuevos",1),("Edificios altos",0)],["¿Centro o periferia?","*Bancos y oficinas* y *edificios altos*: centro.","*Barrios nuevos*: periferia."]),
 Q("¿Cuál es un problema urbano?",["El tránsito","La cosecha","La pesca"],0,["Te toca: ¿cuál es un problema urbano?","¿El tránsito, la cosecha o la pesca?","El *tránsito*: muchos autos y poco transporte público."]),
 TB("PROBLEMAS URBANOS",["Problema","Causa"],[["Tránsito","Muchos autos"],["Vivienda","Crecimiento rápido"],["Basura","Mucha población"]],["Problemas frecuentes.","El *tránsito*: muchos autos.","La falta de *vivienda*: crecimiento rápido.","Y la *basura*: mucha población."]),
 ER([("Todos los barrios tienen lo mismo","Hay desigualdades"),("La ciudad es un solo espacio","Tiene zonas distintas")],["Errores típicos.","Creer que *todos los barrios* tienen los mismos servicios.","Y pensar que la ciudad es *un solo espacio*."]),
 RES(["Repasemos.","La ciudad tiene *zonas*.","Cada una tiene su *uso del suelo*.","Necesita *redes* de servicios.","Y enfrenta *problemas* como el tránsito.","¡Clase terminada! Ahora, *a practicar*."],[["CENTRO","comercio y oficinas"],["PERIFERIA","crece"],["REDES","agua, luz, transporte"],["PROBLEMAS","tránsito y vivienda"]])],
(8,4):[
 {"t":"chat","contacto":{"nombre":"Cami","emoji":"👩"},"mensajes":[{"yo":False,"txt":"Me mudé al pueblo y trabajo desde casa 💻"},{"yo":True,"txt":"¿Y la oficina?"},{"yo":False,"txt":"Es mi compu y buena conexión 😄"}],"titulo":"TECNOLOGÍA Y TERRITORIO","sub":"cómo reorganiza campo y ciudad","voz":["Cami se mudó a un pueblo y trabaja desde casa.","Mati pregunta por la oficina.","Cami: es su compu y una buena conexión.","Hoy: *tecnologías que reorganizan el territorio*."]},
 DEF("Teletrabajo","Trabajar a distancia por Internet","💻",["El *teletrabajo* es trabajar a distancia usando Internet.","Algunas personas se mudan lejos del centro."]),
 CAU(("Comercio electrónico",'🛒'),[("Más depósitos","📦"),("Más repartos","🚚")],["El *comercio electrónico* cambia el territorio.","Hacen falta *más depósitos*.","Y *más repartos* por las calles."]),
 TB("TECNOLOGÍAS",["Dónde","Ejemplo"],[["Campo","Drones y GPS"],["Ciudad","Semáforos inteligentes"]],["Tecnologías según el lugar.","En el *campo*: drones y GPS para cuidar los cultivos.","En la *ciudad*: semáforos inteligentes, aplicaciones de transporte y sensores."]),
 DEF("Brecha digital","Diferencia de acceso a Internet","📶",["La *brecha digital* es la diferencia de acceso a Internet.","En zonas rurales a veces es lenta o no existe, y eso limita la educación y el trabajo."]),
 CL([("CAMPO","🌾"),("CIUDAD","🏙️")],[("Drones y GPS",0),("Semáforo digital",1),("Riego de precisión",0)],["¿Campo o ciudad?","*Drones, GPS* y *riego de precisión*: campo.","*Semáforo digital*: ciudad."]),
 Q("¿Cómo se llama la diferencia de acceso a Internet?",["Brecha digital","Éxodo rural","Subsistencia"],0,["Te toca: ¿cómo se llama la diferencia de acceso a Internet?","¿Brecha digital, éxodo rural o subsistencia?","*Brecha digital*."]),
 ER([("La tecnología llega igual a todos","Hay brecha digital"),("El comercio electrónico no usa territorio","Necesita depósitos y repartos")],["Errores típicos.","Creer que la tecnología *llega igual a todos*.","Y pensar que el comercio electrónico *no usa territorio*."]),
 RES(["Repasemos.","El *teletrabajo* cambia dónde se vive.","El *comercio electrónico* necesita depósitos y repartos.","La *tecnología* cambia campo y ciudad.","Y la *brecha digital* deja a algunos afuera.","¡Clase terminada! Ahora, *a practicar*."],[["TELETRABAJO","a distancia"],["COMERCIO","depósitos y repartos"],["PRECISIÓN","GPS y drones"],["BRECHA","acceso desigual"]])]}
for (m,n),es in CLS.items():
    json.dump({"slug":f"soc1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Ciencias Sociales Integradas I","titulo":TIT[(m,n)],"sub":f"Ciencias Sociales Integradas I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"soc1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
