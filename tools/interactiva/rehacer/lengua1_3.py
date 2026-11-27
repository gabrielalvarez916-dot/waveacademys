# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 3 · Clases de palabras (la animación queda; lección, actividades y examen nuevos)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD

L = {}
L['1'] = {'temas': [
 T('El sustantivo',
   m('clases', items=[
     {'nombre': 'En el club', 'texto': '{{Martina|propio}} dejó la {{mochila|común concreto}} en el {{vestuario|común concreto}} del {{Club Atlético Paraná|propio}} con mucha {{alegría|común abstracto}}.',
      'expl': {'propio': 'Los <b>propios</b> nombran a uno solo y van con mayúscula.', 'común concreto': 'Los <b>comunes concretos</b> nombran cosas que se pueden ver o tocar.', 'común abstracto': 'Los <b>abstractos</b> nombran ideas o sentimientos: no se tocan.'}},
     {'nombre': 'El viaje', 'texto': 'El {{tren|común concreto}} salió de {{Rosario|propio}} y el {{miedo|común abstracto}} de {{Tomás|propio}} desapareció al ver el {{río|común concreto}}.'}]),
   m('clasificar_x', consigna='¿Qué clase de sustantivo es cada palabra?', cajas=['Propio', 'Común concreto', 'Común abstracto'], cuantos=6, items=[
     ['Mendoza', 0], ['Lucía', 0], ['Atlántico', 0], ['bicicleta', 1], ['ventana', 1], ['perro', 1], ['libertad', 2], ['tristeza', 2], ['paciencia', 2]]),
   ('Sustantivo', 'El sustantivo es la palabra que nombra personas, animales, objetos, lugares, ideas o sentimientos, y puede llevar un artículo delante.'),
   'Una prueba rápida para reconocerlo es ponerle un artículo adelante: si «el», «la», «los» o «las» encajan, seguramente es un sustantivo. Los propios se escriben con mayúscula porque nombran a uno solo, como una persona o una ciudad.',
   ['Propios: nombran a uno solo y van con mayúscula.', 'Comunes concretos: se pueden ver o tocar.', 'Comunes abstractos: ideas, sentimientos y cualidades.']),
 T('Género y número',
   m('transformar', items=[
     {'nombre': 'Lápiz', 'antes': 'el lápiz', 'pasos': [{'v': '{{los}} lápiz', 'txt': 'El artículo pasa a plural.'}, {'v': 'los lápi{{ces}}', 'txt': 'Termina en z: la z cambia por c y se agrega -es.'}], 'cierre': 'el lápiz → los lápices'},
     {'nombre': 'Canción', 'antes': 'la canción', 'pasos': [{'v': '{{las}} canción', 'txt': 'El artículo en plural.'}, {'v': 'las cancion{{es}}', 'txt': 'Termina en consonante: se agrega -es (y se va la tilde).'}], 'cierre': 'la canción → las canciones'},
     {'nombre': 'Actor', 'antes': 'el actor', 'pasos': [{'v': '{{la}} actor', 'txt': 'Cambiamos el género del artículo.'}, {'v': 'la actr{{iz}}', 'txt': 'Algunos femeninos cambian la terminación entera.'}], 'cierre': 'el actor → la actriz'}]),
   m('completar_x', consigna='Elegí la forma correcta.', items=[
     {'texto': 'Compré dos [[peces/pezes/pez]] para la pecera y tres [[lápices/lápizs/lápiz]] de colores.'},
     {'texto': 'En el acto cantaron todas las [[canciones/cancións/canción]] y aplaudieron los [[actores/actors/actor]].'},
     {'texto': 'La [[actriz/actora/actor]] saludó al público junto a la [[poeta/poetisa/poeto]] invitada.'}]),
   ('Género y número', 'Los sustantivos tienen género, masculino o femenino, y número, singular o plural; el artículo que los acompaña muestra ese género y número.'),
   'El plural casi siempre se forma con -s o con -es, pero hay casos que conviene mirar: si la palabra termina en z, la z cambia por c. Algunos sustantivos no cambian nada en plural, como «la crisis, las crisis», y ahí el artículo es la única pista.',
   ['Vocal sin tilde: se agrega -s (casa, casas).', 'Consonante: se agrega -es (árbol, árboles).', 'Terminada en z: cambia a c (luz, luces).']),
 T('El adjetivo y la concordancia',
   m('clases', items=[
     {'nombre': 'La casa', 'texto': '{{Esta|adjetivo determinativo}} casa {{antigua|adjetivo calificativo}} tiene {{tres|adjetivo determinativo}} ventanas {{enormes|adjetivo calificativo}}.',
      'expl': {'adjetivo determinativo': 'Los <b>determinativos</b> precisan al sustantivo: cuál, cuántos, de quién.', 'adjetivo calificativo': 'Los <b>calificativos</b> dicen cómo es: una cualidad.'}},
     {'nombre': 'El perro', 'texto': '{{Mi|adjetivo determinativo}} perro {{negro|adjetivo calificativo}} persigue a {{aquellas|adjetivo determinativo}} palomas {{grises|adjetivo calificativo}}.'}]),
   m('completar_x', consigna='Hacé concordar el adjetivo con el sustantivo.', items=[
     {'texto': 'Las calles [[mojadas/mojado/mojada]] brillaban bajo los faroles [[viejos/vieja/viejas]].'},
     {'texto': 'Mi hermana es muy [[alegre/alegra/alegres]] y sus amigos son [[simpáticos/simpática/simpático]].'},
     {'texto': 'Encontramos unas piedras [[redondas/redondo/redonda]] y un caracol [[pequeño/pequeña/pequeños]].'}]),
   ('Adjetivo', 'El adjetivo acompaña al sustantivo para decir cómo es o para precisarlo, y concuerda con él en género y número.'),
   'Concordar significa que el adjetivo copia el género y el número del sustantivo: «calles mojadas», nunca «calles mojado». Algunos adjetivos tienen una sola forma para los dos géneros, como «alegre», «feliz» o «grande», y solo cambian en plural.',
   ['Calificativos: una cualidad (alto, dulce, oscuro).', 'Determinativos: cuál, cuántos o de quién (este, tres, mi).', 'Concuerdan en género y número con el sustantivo.'])],
 'recuerda': [
   R('Sustantivo', 'es la palabra que nombra personas, animales, objetos, lugares, ideas o sentimientos.', 'mochila, Rosario, alegría'),
   R('Sustantivo propio', 'nombra a uno solo, en particular, y se escribe siempre con mayúscula.', 'Martina, Mendoza'),
   R('Sustantivo abstracto', 'nombra ideas, sentimientos o cualidades que no se pueden tocar.', 'libertad, miedo'),
   R('Plural', 'se forma con -s después de vocal, con -es después de consonante y con -ces si termina en z.', 'luz → luces'),
   R('Adjetivo', 'acompaña al sustantivo para decir cómo es o precisar cuál, cuántos o de quién.', 'esta casa antigua'),
   R('Concordancia', 'es que el adjetivo tenga el mismo género y número que su sustantivo.', 'calles mojadas')]}

L['2'] = {'temas': [
 T('Qué es un verbo',
   m('marcar', rotulo='Oración', items=[
     {'nombre': 'La tormenta', 'texto': 'El viento {{sopló|Acción: algo que pasa.}} toda la noche y los chicos {{estaban|Estado: cómo estaban.}} asustados. A la mañana el cielo {{se despejó|Proceso: un cambio.}}.', 'cierre': 'Los verbos expresan acciones, estados o procesos.'},
     {'nombre': 'El recreo', 'texto': 'Juan {{corre|Acción.}} por el patio, Ana {{parece|Estado.}} cansada y el hielo del bebedero {{se derrite|Proceso.}} al sol.', 'cierre': 'En la oración, el verbo es la palabra que cambia según quién y cuándo.'}]),
   m('marcar_x', consigna='Tocá solo los verbos.', items=[
     {'cons': 'Oración: «Mi abuela cocina pan los domingos y lo reparte entre los vecinos.»', 'texto': '[[Mi|0]] [[abuela|0]] [[cocina|1]] [[pan|0]] [[los|0]] [[domingos|0]] [[y|0]] [[lo|0]] [[reparte|1]] [[entre|0]] [[los|0]] [[vecinos|0]]'},
     {'cons': 'Oración: «Llovió fuerte, pero igual salimos y jugamos en la plaza.»', 'texto': '[[Llovió|1]] [[fuerte|0]] [[pero|0]] [[igual|0]] [[salimos|1]] [[y|0]] [[jugamos|1]] [[en|0]] [[la|0]] [[plaza|0]]'}]),
   ('Verbo', 'El verbo es la palabra que expresa acciones, estados o procesos y cambia su forma según la persona, el número, el tiempo y el modo.'),
   'Todos los verbos tienen un nombre, el infinitivo, que termina en -ar, -er o -ir: así aparecen en el diccionario. Para reconocer un verbo en una oración, probá cambiarle el tiempo: «cocina» puede pasar a «cocinó» o «cocinará»; un sustantivo no puede hacer eso.',
   ['Primera conjugación: -ar (cantar).', 'Segunda: -er (comer). Tercera: -ir (vivir).', 'Si cambia con el tiempo, es un verbo.']),
 T('Persona, número y tiempo',
   m('conjugador', verbos=['caminar', 'saltar', 'comer', 'correr', 'vivir', 'escribir'], tiempos=['presente', 'pretérito perfecto simple', 'futuro']),
   m('conjugar_x', verbos=['caminar', 'saltar', 'comer', 'correr', 'vivir', 'escribir'], tiempos=['presente', 'pretérito perfecto simple', 'futuro']),
   ('Accidentes del verbo', 'Los accidentes del verbo son los cambios de su terminación, la desinencia, que indican quién realiza la acción, cuántos son y cuándo ocurre.'),
   'Por eso alcanza con mirar la terminación para saber mucho: en «comimos» sabemos que fuimos nosotros, que éramos varios y que ya pasó. La parte que no cambia es la raíz y guarda el significado del verbo.',
   ['Persona: primera (yo), segunda (vos) o tercera (él, ella).', 'Número: singular o plural.', 'Tiempo: presente, pasado o futuro.']),
 T('Los modos del verbo',
   m('marcar', rotulo='Oración', items=[
     {'nombre': 'Estudiar', 'texto': '{{Estudio|Indicativo: afirmo un hecho real.}} todas las tardes. {{Ojalá apruebe|Subjuntivo: expreso un deseo.}} el examen. {{Estudiá|Imperativo: doy una orden.}} vos también.', 'cierre': 'El mismo verbo cambia de modo según la actitud de quien habla.'},
     {'nombre': 'Llover', 'texto': 'Mañana {{lloverá|Indicativo: lo doy como algo que va a pasar.}}. {{Quizás llueva|Subjuntivo: es una posibilidad.}} toda la semana. {{Llevá|Imperativo: un pedido.}} el paraguas.', 'cierre': 'Hecho, deseo o duda, orden: tres modos.'}]),
   m('clasificar_x', consigna='¿En qué modo está el verbo destacado?', cajas=['Indicativo', 'Subjuntivo', 'Imperativo'], cuantos=6, items=[
     ['Mi hermano TRABAJA en una panadería.', 0], ['Ayer VIMOS una película.', 0], ['El tren LLEGARÁ a las ocho.', 0],
     ['Ojalá GANE nuestro equipo.', 1], ['Quizás VENGAN mañana.', 1], ['Espero que te GUSTE el regalo.', 1],
     ['CERRÁ la ventana, por favor.', 2], ['TRAÉ las llaves.', 2], ['ESCUCHÁ esta canción.', 2]]),
   ('Modo verbal', 'El modo verbal muestra la actitud de quien habla: si presenta algo como un hecho, como un deseo o una duda, o como una orden.'),
   'Para reconocer el modo, preguntate qué está haciendo quien habla. Si afirma o cuenta algo que pasa, pasó o pasará, es indicativo. Si desea, duda o supone, es subjuntivo, que suele aparecer después de «ojalá», «quizás» o «que». Si pide u ordena, es imperativo.',
   ['Indicativo: hechos reales.', 'Subjuntivo: deseos, dudas y posibilidades.', 'Imperativo: órdenes y pedidos.'])],
 'recuerda': [
   R('Verbo', 'expresa acciones, estados o procesos y cambia según persona, número, tiempo y modo.', 'sopló, estaban, se despejó'),
   R('Infinitivo', 'es el nombre del verbo y termina en -ar, -er o -ir, como aparece en el diccionario.', 'cantar, comer, vivir'),
   R('Raíz y desinencia', 'la raíz guarda el significado y la desinencia indica persona, número y tiempo.', 'com-imos: raíz com, desinencia -imos'),
   R('Modo indicativo', 'presenta la acción como un hecho real, pasado, presente o futuro.', 'Estudio todas las tardes.'),
   R('Modo subjuntivo', 'expresa deseos, dudas o posibilidades, muchas veces después de ojalá o quizás.', 'Ojalá apruebe.'),
   R('Modo imperativo', 'sirve para dar órdenes o hacer pedidos a quien escucha.', 'Cerrá la ventana.')]}

L['3'] = {'temas': [
 T('El adverbio',
   m('clases', items=[
     {'nombre': 'La mudanza', 'texto': '{{Ayer|tiempo}} nos mudamos {{lejos|lugar}}. Los muebles llegaron {{bien|modo}}, pero tardamos {{mucho|cantidad}} en acomodarlos.',
      'expl': {'tiempo': 'Adverbios de <b>tiempo</b>: responden ¿cuándo?', 'lugar': 'De <b>lugar</b>: ¿dónde?', 'modo': 'De <b>modo</b>: ¿cómo?', 'cantidad': 'De <b>cantidad</b>: ¿cuánto?'}},
     {'nombre': 'El partido', 'texto': '{{Hoy|tiempo}} jugamos {{afuera|lugar}}; corrimos {{rápido|modo}} y nos cansamos {{bastante|cantidad}}.'}]),
   m('clasificar_x', consigna='¿Qué indica cada adverbio?', cajas=['Lugar', 'Tiempo', 'Modo', 'Cantidad', 'Afirmación o negación'], cuantos=6, items=[
     ['acá', 0], ['debajo', 0], ['mañana', 1], ['nunca', 1], ['despacio', 2], ['mal', 2], ['poco', 3], ['demasiado', 3], ['también', 4], ['tampoco', 4]]),
   ('Adverbio', 'El adverbio es una palabra invariable que agrega una circunstancia, como el lugar, el tiempo, el modo o la cantidad.'),
   'Invariable quiere decir que nunca cambia de género ni de número: decimos «ella corre rápido» y «ellos corren rápido». Una buena manera de encontrarlo es hacerle preguntas al verbo: ¿dónde?, ¿cuándo?, ¿cómo?, ¿cuánto?',
   ['¿Dónde? Lugar (cerca, arriba).', '¿Cuándo? Tiempo (hoy, siempre). ¿Cómo? Modo (bien, así).', '¿Cuánto? Cantidad (muy, poco).']),
 T('Qué modifica el adverbio',
   m('marcar', rotulo='Oración', items=[
     {'nombre': 'Al verbo', 'texto': 'El caballo galopa {{velozmente|Modifica al verbo «galopa»: dice cómo.}}.', 'cierre': 'Lo más común: el adverbio acompaña a un verbo.'},
     {'nombre': 'Al adjetivo', 'texto': 'La sopa está {{muy|Modifica al adjetivo «caliente»: dice cuánto.}} caliente.', 'cierre': 'También puede intensificar un adjetivo.'},
     {'nombre': 'A otro adverbio', 'texto': 'Llegaste {{bastante|Modifica al adverbio «tarde».}} tarde.', 'cierre': 'Y hasta a otro adverbio.'}]),
   m('elegir_x', consigna='¿A qué palabra modifica el adverbio en mayúsculas?', items=[
     {'cons': 'El examen fue BASTANTE difícil.', 'ops': ['A «difícil», un adjetivo', 'A «examen», un sustantivo', 'A «fue», el verbo'], 'ayuda': '¿Qué es «bastante»? Cuánto de difícil.'},
     {'cons': 'Mi abuelo camina DESPACIO por la vereda.', 'ops': ['A «camina», el verbo', 'A «abuelo», un sustantivo', 'A «vereda», un sustantivo'], 'ayuda': '¿Cómo camina?'},
     {'cons': 'Lo terminaste MUY rápido.', 'ops': ['A «rápido», otro adverbio', 'A «terminaste», el verbo', 'A «lo», un pronombre'], 'ayuda': '«Muy» dice cuánto de rápido.'}]),
   ('Función del adverbio', 'El adverbio modifica a un verbo, a un adjetivo o a otro adverbio, nunca a un sustantivo.'),
   'Esta regla ayuda a distinguirlo del adjetivo: en «un auto rápido», «rápido» acompaña a un sustantivo y concuerda con él, así que es adjetivo; en «maneja rápido», acompaña al verbo y no cambia, así que es adverbio.',
   ['Con un verbo: «corre lejos».', 'Con un adjetivo: «muy alto».', 'Con otro adverbio: «bastante tarde».']),
 T('La preposición',
   m('marcar', rotulo='Frase', items=[
     {'nombre': 'La plaza', 'texto': 'Nos sentamos {{bajo|Preposición: une «nos sentamos» con «el árbol».}} el árbol {{de|Preposición: une «árbol» con «la plaza».}} la plaza.', 'cierre': 'La preposición siempre necesita una palabra después: su término.'},
     {'nombre': 'El viaje', 'texto': 'Viajé {{desde|Preposición: indica el origen.}} Salta {{hasta|Preposición: indica el final del recorrido.}} Ushuaia {{con|Preposición: indica compañía.}} mi tía.', 'cierre': 'Cada preposición agrega una relación: origen, destino, compañía.'}]),
   m('completar_x', consigna='Elegí la preposición que corresponde.', items=[
     {'texto': 'Guardé los libros [[en/con/hacia]] la mochila y salí [[hacia/sin/bajo]] la escuela.'},
     {'texto': 'Hice la torta [[sin/por/ante]] azúcar y la decoré [[con/desde/tras]] frutillas.'},
     {'texto': 'El gato duerme [[sobre/según/hasta]] el sillón [[desde/con/sin]] la mañana.'}]),
   ('Preposición', 'La preposición es una palabra invariable que une una palabra con otra, llamada término, y muestra la relación entre ellas.'),
   'No tiene significado por sí sola: «desde» o «con» no dicen nada hasta que aparece su término. Las preposiciones son una lista cerrada y conviene conocerlas de memoria, porque más adelante ayudan a analizar las oraciones.',
   ['a, ante, bajo, con, contra, de, desde, durante, en, entre', 'hacia, hasta, mediante, para, por, según, sin, sobre, tras', 'Siempre van seguidas de su término.'])],
 'recuerda': [
   R('Adverbio', 'es una palabra invariable que agrega circunstancias de lugar, tiempo, modo o cantidad.', 'ayer, lejos, bien, mucho'),
   R('Invariable', 'significa que no cambia de género ni de número aunque cambie la oración.', 'ella corre rápido / ellos corren rápido'),
   R('Qué modifica', 'el adverbio modifica a un verbo, a un adjetivo o a otro adverbio, nunca a un sustantivo.', 'muy caliente'),
   R('Preposición', 'es una palabra invariable que une una palabra con su término y marca la relación.', 'bajo el árbol'),
   R('Término', 'es la palabra o el grupo que va después de la preposición y la completa.', 'desde Salta')]}

L['4'] = {'temas': [
 T('El pronombre',
   m('transformar', items=[
     {'nombre': 'Lucía', 'antes': 'Lucía llegó tarde. Lucía pidió disculpas y Lucía se sentó.', 'pasos': [{'v': 'Lucía llegó tarde. {{Ella}} pidió disculpas y Lucía se sentó.', 'txt': '«Ella» reemplaza a «Lucía»: ya sabemos de quién se habla.'}, {'v': 'Lucía llegó tarde. Ella pidió disculpas y {{se sentó}}.', 'txt': 'La tercera vez ni hace falta: el verbo ya dice que fue ella.'}], 'cierre': 'El pronombre evita repetir el sustantivo.'},
     {'nombre': 'La bici', 'antes': 'Me regalaron una bici. Cuido la bici y guardo la bici en el garaje.', 'pasos': [{'v': 'Me regalaron una bici. {{La}} cuido y {{la}} guardo en el garaje.', 'txt': '«La» reemplaza a «la bici» delante del verbo.'}], 'cierre': 'Hay pronombres que se ubican pegados al verbo.'}]),
   m('completar_banco_x', consigna='Llevá cada pronombre a su lugar para no repetir.', items=[
     {'texto': 'Mi primo vino a casa. [[Él]] trajo un juego nuevo y [[lo]] probamos toda la tarde.', 'extra': ['Ella', 'la']},
     {'texto': 'Las vecinas organizaron una feria. [[Ellas]] vendieron tortas y [[las]] hicieron en una noche.', 'extra': ['Ellos', 'los']},
     {'texto': 'Encontré tu cuaderno. [[Lo]] dejé sobre la mesa. ¿Es [[tuyo]]?', 'extra': ['La', 'mío']}]),
   ('Pronombre', 'El pronombre es la palabra que ocupa el lugar de un sustantivo o señala a una persona o cosa sin nombrarla.'),
   'Sirve para no repetir y para que el texto avance más liviano. Pero tiene una condición: el lector tiene que saber a quién reemplaza. Si en la oración aparecen dos personas, un «ella» puede confundir, y conviene repetir el nombre.',
   ['Reemplaza a un sustantivo ya nombrado.', 'Evita repeticiones en el texto.', 'Tiene que quedar claro a quién se refiere.']),
 T('Clases de pronombres',
   m('clases', items=[
     {'nombre': 'Las llaves', 'texto': '—¿Estas llaves son {{tuyas|posesivo}}? —preguntó {{ella|personal}}. —No, las {{mías|posesivo}} son {{esas|demostrativo}} del llavero rojo.',
      'expl': {'posesivo': 'Los <b>posesivos</b> indican de quién es algo.', 'personal': 'Los <b>personales</b> nombran a las personas gramaticales: yo, vos, él…', 'demostrativo': 'Los <b>demostrativos</b> señalan algo según la distancia.'}},
     {'nombre': 'El regalo', 'texto': '{{Nosotros|personal}} elegimos {{este|demostrativo}} y {{ustedes|personal}} eligieron {{aquel|demostrativo}}; el {{nuestro|posesivo}} era más grande.'}]),
   m('clasificar_x', consigna='¿Qué clase de pronombre es?', cajas=['Personal', 'Posesivo', 'Demostrativo'], cuantos=6, items=[
     ['yo', 0], ['nosotras', 0], ['ellos', 0], ['mío', 1], ['tuyos', 1], ['suya', 1], ['este', 2], ['esa', 2], ['aquellos', 2]]),
   ('Clases de pronombres', 'Los pronombres personales nombran a las personas gramaticales, los posesivos indican pertenencia y los demostrativos señalan según la distancia.'),
   'Ojo con una trampa frecuente: «este» o «mi» pueden ser adjetivos. En «este libro», «este» acompaña a un sustantivo y es adjetivo determinativo; en «quiero este», está solo, ocupando el lugar del sustantivo, y entonces es pronombre.',
   ['Personales: yo, vos, él, ella, nosotros, ustedes, ellos.', 'Posesivos: mío, tuyo, suyo, nuestro.', 'Demostrativos: este, ese, aquel (cerca, medio, lejos).']),
 T('La conjunción',
   m('marcar', rotulo='Oración', items=[
     {'nombre': 'La salida', 'texto': 'Quería ir al cine {{pero|Oposición: la segunda idea se opone a la primera.}} llovía, así que me quedé {{y|Suma: agrega otra acción.}} leí un libro.', 'cierre': 'Las conjunciones unen y muestran la relación.'},
     {'nombre': 'El postre', 'texto': '¿Querés helado {{o|Opción: hay que elegir una.}} flan? No como {{ni|Suma negativa.}} chocolate {{ni|Suma negativa.}} dulce de leche {{porque|Causa: explica el motivo.}} me duele la panza.', 'cierre': 'Cada conjunción tiene un significado distinto.'}]),
   m('completar_x', consigna='Elegí la conjunción que da sentido a la oración.', items=[
     {'texto': 'Estudié mucho [[pero/porque/ni]] la prueba fue difícil. Me fue bien [[porque/o/pero]] repasé todo.'},
     {'texto': 'Podés venir hoy [[o/ni/porque]] mañana. Mi hermana [[e/y/u]] Inés también vienen.'},
     {'texto': 'No tengo hambre [[ni/o/pero]] sed. Hay siete [[u/o/e]] ocho invitados.'}]),
   ('Conjunción', 'La conjunción es una palabra invariable que une palabras u oraciones y muestra qué relación hay entre ellas.'),
   'Hay dos cambios que suenan raro pero son obligatorios: «y» se transforma en «e» delante de una palabra que empieza con el sonido i («padres e hijos»), y «o» pasa a «u» delante del sonido o («siete u ocho»). Así no se juntan dos vocales iguales.',
   ['Suma: y, e, ni.', 'Opción: o, u. Oposición: pero, aunque.', 'Causa: porque.'])],
 'recuerda': [
   R('Pronombre', 'ocupa el lugar de un sustantivo o señala a alguien sin nombrarlo, para no repetir.', 'Lucía llegó. Ella se sentó.'),
   R('Pronombre personal', 'nombra a las personas gramaticales: quien habla, quien escucha y de quien se habla.', 'yo, vos, ellos'),
   R('Pronombre posesivo', 'indica a quién pertenece algo y aparece sin sustantivo al lado.', 'Esas son mías.'),
   R('Pronombre o adjetivo', 'es adjetivo si acompaña a un sustantivo y pronombre si lo reemplaza.', 'este libro / quiero este'),
   R('Conjunción', 'une palabras u oraciones y muestra si se suman, se oponen, se elige o hay una causa.', 'Quería ir, pero llovía.'),
   R('Cambio de y por e', 'ocurre delante del sonido i, y o pasa a u delante del sonido o.', 'padres e hijos; siete u ocho')]}

A = {
 '1': [
   CLA('Clasificá los sustantivos de esta oración: «Valentina sintió orgullo cuando subió al escenario del Teatro Colón».', ['Propio', 'Común concreto', 'Común abstracto'], [('Valentina', 'Propio'), ('Teatro Colón', 'Propio'), ('escenario', 'Común concreto'), ('orgullo', 'Común abstracto')], 'Propios con mayúscula; abstractos: ideas o sentimientos.'),
   FB('Escribí el plural: «una luz → dos ___», «un camión → dos ___», «un mes → dos ___».', [['luces'], ['camiones'], ['meses']], 'z → ces; consonante → -es.'),
   MC('Un compañero escribió: «Las chicas llegaron cansado y contento». ¿Qué está mal?', ['Los adjetivos no concuerdan con «chicas»', 'Falta un sustantivo propio', 'El verbo está en futuro'], 'Los adjetivos no concuerdan con «chicas»', 'Tiene que ser «cansadas y contentas»: femenino plural.', 'error'),
   TAP('Tocá los dos adjetivos: «Aquella torre antigua da miedo de noche».', ['Aquella', 'torre', 'antigua', 'da', 'miedo', 'de', 'noche'], [0, 2], '«Aquella» es determinativo y «antigua», calificativo.', 'analizar')],
 '2': [
   TAP('Tocá los tres verbos: «Los pájaros volaron alto, se posaron en el techo y cantaron».', ['Los', 'pájaros', 'volaron', 'alto', 'se', 'posaron', 'en', 'el', 'techo', 'y', 'cantaron'], [2, 5, 10], 'Son las palabras que cambiarían con el tiempo.', 'analizar'),
   UNI('Uní cada verbo con su persona, número y tiempo.', [('cantaremos', '1.ª plural, futuro'), ('comiste', '2.ª singular, pasado'), ('viven', '3.ª plural, presente'), ('escribí', '1.ª singular, pasado')], 'La desinencia lo dice todo.'),
   CLA('¿En qué modo está cada verbo?', ['Indicativo', 'Subjuntivo', 'Imperativo'], [('Mañana viajamos a Córdoba.', 'Indicativo'), ('Ojalá haga buen tiempo.', 'Subjuntivo'), ('Prepará la valija.', 'Imperativo'), ('Quizás llegue tarde.', 'Subjuntivo')], 'Hecho, deseo o duda, orden.'),
   MC('Sofía dice: «En "Ojalá salga el sol", el verbo está en indicativo porque habla del futuro». ¿Tiene razón?', ['No: es subjuntivo, expresa un deseo', 'Sí: todo lo que pasa en el futuro es indicativo', 'No: es imperativo'], 'No: es subjuntivo, expresa un deseo', 'Después de «ojalá» va subjuntivo: no se afirma, se desea.', 'error')],
 '3': [
   CLA('¿Qué indica cada adverbio?', ['Lugar', 'Tiempo', 'Modo', 'Cantidad'], [('afuera', 'Lugar'), ('todavía', 'Tiempo'), ('claramente', 'Modo'), ('demasiado', 'Cantidad')], 'Preguntá dónde, cuándo, cómo y cuánto.'),
   MC('En «Tenemos un perro tranquilo» y «El perro duerme tranquilo», ¿qué es «tranquilo» en cada caso?', ['Adjetivo y después adverbio', 'Adverbio en los dos casos', 'Adjetivo en los dos casos'], 'Adjetivo y después adverbio', 'En la primera acompaña al sustantivo; en la segunda dice cómo duerme.', 'analizar'),
   FB('Completá con preposiciones: «Salimos ___ la mañana, caminamos ___ el río y volvimos ___ casa».', [['a', 'por', 'en', 'durante'], ['hasta', 'hacia', 'por'], ['a']], 'Cada preposición marca una relación.'),
   TAP('Tocá la preposición que está mal usada: «Me voy de vacaciones a la playa en mi familia».', ['Me', 'voy', 'de', 'vacaciones', 'a', 'la', 'playa', 'en', 'mi', 'familia'], [7], 'Para la compañía va «con»: «con mi familia».', 'error')],
 '4': [
   FB('Reemplazá la repetición por un pronombre: «Martín perdió la pelota. ___ buscó por todo el patio y ___ encontró detrás del árbol».', [['Martín la', 'la'], ['la']], 'Delante del verbo, «la» reemplaza a «la pelota».'),
   CLA('Clasificá las palabras destacadas: «ESTE cuaderno es MÍO; ESE es TUYO y AQUEL también».', ['Adjetivo determinativo', 'Pronombre'], [('ESTE (cuaderno)', 'Adjetivo determinativo'), ('MÍO', 'Pronombre'), ('ESE', 'Pronombre'), ('AQUEL', 'Pronombre')], 'Si acompaña a un sustantivo, es adjetivo; si lo reemplaza, pronombre.', 'analizar'),
   MC('«Llegaron Juan y Pedro. Él traía la torta.» ¿Qué problema tiene?', ['No se sabe a quién se refiere «él»', 'Falta una conjunción', 'El verbo está mal conjugado'], 'No se sabe a quién se refiere «él»', 'Con dos personas, el pronombre es ambiguo: conviene repetir el nombre.', 'error'),
   FB('Completá con la conjunción correcta: «Invitamos a padres ___ hijos. Pueden venir siete ___ ocho personas por familia».', [['e'], ['u']], '«y» pasa a «e» delante de i; «o» pasa a «u» delante de o.')],
}

EX = [
 [1, CLA('Clasificá: «Con mucha paciencia, Ramiro armó una maqueta del Obelisco».', ['Propio', 'Común concreto', 'Común abstracto'], [('Ramiro', 'Propio'), ('Obelisco', 'Propio'), ('maqueta', 'Común concreto'), ('paciencia', 'Común abstracto')], 'Mayúscula, objeto o idea.')],
 [1, MC('¿Cuál de estas frases tiene un error de concordancia?', ['Unas flores amarillo', 'Unos zapatos nuevos', 'Una mesa redonda'], 'Unas flores amarillo', 'Tiene que ser «amarillas»: femenino plural.', 'error')],
 [1, FB('Escribí el plural de «nariz» y de «reloj».', [['narices'], ['relojes']], 'z → ces; consonante → -es.')],
 [2, TAP('Tocá el verbo en subjuntivo: «Espero que mañana salga el sol y podamos ir al río».', ['Espero', 'que', 'mañana', 'salga', 'el', 'sol', 'y', 'podamos', 'ir', 'al', 'río'], [3, 7], 'Después de «espero que» van deseos: subjuntivo.', 'analizar')],
 [2, SA('¿En qué persona y número está «escribimos»? (Respondé por ejemplo: primera plural).', ['primera plural', 'primera persona plural', '1.ª plural', '1a plural', 'primera del plural', 'nosotros'], 'La desinencia -imos indica nosotros.', 'aplicar')],
 [2, MC('Un chico dice: «En "Cerrá la puerta" no hay verbo porque no cuenta ninguna acción». ¿Qué le contestás?', ['Sí hay: «cerrá» es un verbo en modo imperativo', 'Tiene razón: es una orden, no un verbo', 'El verbo es «puerta»'], 'Sí hay: «cerrá» es un verbo en modo imperativo', 'Las órdenes también son verbos: modo imperativo.', 'error')],
 [3, MC('En «Llegaste demasiado temprano», ¿a qué modifica «demasiado»?', ['A «temprano», otro adverbio', 'A «llegaste», el verbo', 'A nada: es una preposición'], 'A «temprano», otro adverbio', 'Dice cuánto de temprano.', 'analizar')],
 [3, CLA('¿Adverbio o preposición?', ['Adverbio', 'Preposición'], [('lejos', 'Adverbio'), ('hacia', 'Preposición'), ('mañana (en «vuelvo mañana»)', 'Adverbio'), ('sin', 'Preposición')], 'La preposición siempre necesita un término después.')],
 [3, FB('Completá con una preposición: «Fuimos ___ Córdoba ___ auto».', [['a', 'hacia', 'hasta'], ['en']], 'Destino y medio.')],
 [4, MS('Elegí TODOS los pronombres: «Ella me dijo que el libro rojo es suyo y que aquel es nuestro».', ['Ella', 'rojo', 'suyo', 'aquel', 'nuestro', 'libro'], ['Ella', 'suyo', 'aquel', 'nuestro'], '«Rojo» es adjetivo y «libro», sustantivo.')],
 [4, MC('¿Qué conjunción completa bien? «Quería ir a la fiesta, ___ me quedé estudiando.»', ['pero', 'porque', 'ni'], 'pero', 'Las ideas se oponen.', 'aplicar')],
 [4, MC('¿Cuál está bien escrita?', ['Agua e hielo', 'Siete u ocho', 'Uno o otro'], 'Siete u ocho', '«o» pasa a «u» delante del sonido o.', 'recordar')],
 [4, KW('Escribí dos oraciones sobre tu mascota o un animal que te guste: en la segunda usá un pronombre para no repetir su nombre y una conjunción para unir dos ideas.', 'Por ejemplo: «… Ella duerme mucho y come poco».', [['él', 'ella', 'lo', 'la', 'le'], ['y', 'pero', 'porque', 'o', 'ni']], 2, 'Pronombre para no repetir y conjunción para unir.', 'aplicar')],
]

def ajustes(M):
    for k, v in A.items(): M['act'][k] = v
    for q in M['act'].get('5', []): q.setdefault('n', 'recordar')
    M['examen'] = EX
    M['actualizar_preguntas'] = True

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-3/mision-3.json', L, ajustes=ajustes)
