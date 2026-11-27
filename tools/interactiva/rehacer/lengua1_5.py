# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 5 · El texto expositivo (la animación queda; lección, actividades y examen nuevos)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD

L = {}
L['1'] = {'temas': [
 T('El texto expositivo',
   m('marcar', rotulo='Texto', items=[
     {'nombre': 'El carpincho', 'texto': '{{El carpincho es el roedor más grande del mundo.|Presenta el tema con un dato.}} {{Puede pesar más de 60 kilos|Informa con datos precisos.}} y {{vive cerca de ríos y lagunas, porque necesita el agua para refrescarse.|Explica el porqué.}}', 'cierre': 'Informa y explica, sin contar una historia ni opinar.'},
     {'nombre': 'Los volcanes', 'texto': '{{Un volcán es una abertura de la corteza terrestre|Define el tema.}} {{por donde sale roca fundida, llamada magma.|Agrega un término técnico y lo explica.}} {{En la Argentina hay volcanes activos en la cordillera.|Da un ejemplo cercano.}}', 'cierre': 'Usa la tercera persona y un vocabulario preciso.'}]),
   m('clasificar_x', consigna='¿Cuál de estos fragmentos es expositivo y cuál cuenta una historia?', cajas=['Expositivo', 'Narrativo'], cuantos=6, items=[
     ['Las abejas se comunican con una danza que indica dónde están las flores.', 0], ['El agua hierve a 100 grados al nivel del mar.', 0], ['Los pingüinos no vuelan, pero son excelentes nadadores.', 0],
     ['Aquella tarde, Pedro encontró una abeja atrapada en la ventana.', 1], ['Cuando llegamos a la costa, los pingüinos nos miraron curiosos.', 1], ['Había una vez un volcán que despertó una noche de invierno.', 1]]),
   ('Texto expositivo', 'El texto expositivo es el que explica un tema para que el lector lo entienda, con información precisa y sin contar una historia ni dar opiniones.'),
   'Es el texto de los libros de estudio, las enciclopedias y las notas de divulgación. Se reconoce porque habla en tercera persona, usa palabras exactas del tema y responde preguntas como qué es, cómo funciona o por qué ocurre.',
   ['Informa y explica un tema.', 'Tercera persona y vocabulario preciso.', 'No cuenta historias ni da opiniones.']),
 T('Tema e idea principal',
   m('capas', items=[
     {'nombre': 'El hornero', 'texto': '{{El hornero construye su nido con barro y paja.|idea principal|La <b>idea principal</b>: lo más importante que se dice del tema.}} {{Tarda varias semanas en terminarlo|idea secundaria|Una <b>idea secundaria</b>: agrega un detalle.}} {{y lo ubica en postes o ramas altas.|idea secundaria}}', 'borrado': 'idea principal', 'inicio': 'Tema: el nido del hornero.', 'cierre': 'Tema: el nido del hornero. Idea principal: lo arma con barro y paja.'},
     {'nombre': 'Los cactus', 'texto': '{{Los cactus almacenan agua en sus tallos.|idea principal|La idea principal.}} {{Por eso sus tallos son gruesos|idea secundaria|Explica una consecuencia.}} {{y pueden vivir meses sin lluvia.|idea secundaria|Agrega un dato.}}', 'borrado': 'idea principal', 'inicio': 'Tema: los cactus y el agua.'}]),
   m('elegir_x', consigna='¿Cuál es la idea principal del párrafo?', items=[
     {'cons': '«Los delfines duermen con medio cerebro por vez. Así pueden seguir nadando y subir a respirar. Cada mitad descansa unas horas.»', 'ops': ['Los delfines duermen con medio cerebro por vez', 'Los delfines suben a respirar', 'Cada mitad descansa unas horas'], 'ayuda': 'Las otras oraciones explican la primera.'},
     {'cons': '«Las hormigas trabajan en equipo. Unas buscan comida, otras cuidan las crías y otras defienden el hormiguero.»', 'ops': ['Las hormigas trabajan en equipo', 'Algunas hormigas cuidan las crías', 'El hormiguero tiene defensas'], 'ayuda': 'Lo demás son ejemplos de ese trabajo.'},
     {'cons': '«Primero aparecieron los teléfonos fijos. Después, los celulares. Hoy, los teléfonos son pequeñas computadoras que llevamos en el bolsillo.»', 'ops': ['Los teléfonos cambiaron mucho con el tiempo', 'Los celulares aparecieron después', 'Los teléfonos fijos fueron los primeros'], 'ayuda': 'A veces la idea principal no está escrita: se arma uniendo todo.'}]),
   ('Idea principal', 'El tema es de qué trata el texto en pocas palabras, y la idea principal es lo más importante que el texto dice sobre ese tema.'),
   'La idea principal suele estar en la primera oración del párrafo, pero también puede aparecer al final o no estar escrita: en ese caso la armamos nosotros uniendo lo que dicen las demás oraciones. Además, cada párrafo de un texto tiene su propia idea principal.',
   ['Tema: ¿de qué trata? (pocas palabras).', 'Idea principal: ¿qué dice de importante?', 'Puede estar al principio, al final o no estar escrita.']),
 T('Ideas secundarias y la prueba del borrado',
   m('capas', items=[
     {'nombre': 'Las ballenas', 'texto': '{{Las ballenas jorobadas viajan miles de kilómetros cada año.|idea principal|Lo importante.}} {{Algunas recorren más de 8000 kilómetros.|idea secundaria|Un dato que suma.}} {{Viajan en grupos pequeños|idea secundaria|Un detalle.}} {{para buscar aguas cálidas donde nacen sus crías.|idea secundaria|Explica el porqué.}}', 'borrado': 'idea principal', 'cierre': 'Si tachamos las secundarias, la idea se sigue entendiendo.'}]),
   m('borrar_x', consigna='Prueba del borrado: tachá las oraciones secundarias y dejá la idea principal.', items=[
     {'oraciones': [['El yaguareté es el felino más grande de América.', 1], ['Puede medir casi dos metros.', 0], ['Su pelaje tiene manchas en forma de roseta.', 0], ['Vive en selvas y montes del norte argentino.', 0]]},
     {'oraciones': [['Los árboles ayudan a limpiar el aire.', 1], ['Absorben dióxido de carbono.', 0], ['Liberan oxígeno durante el día.', 0], ['Un árbol grande puede retener mucho polvo.', 0]]},
     {'oraciones': [['El chocolate se hace con las semillas del cacao.', 1], ['El cacao crece en zonas cálidas.', 0], ['Las semillas se tuestan y se muelen.', 0], ['Los aztecas ya lo tomaban como bebida.', 0]]}]),
   ('Ideas secundarias', 'Las ideas secundarias son las que acompañan a la principal: la explican, agregan datos, dan ejemplos o dicen por qué ocurre.'),
   'Para distinguirlas sirve la prueba del borrado: tachá una oración con la imaginación. Si el párrafo pierde su sentido, era la idea principal; si solo perdés un detalle y lo demás se entiende, era secundaria.',
   ['Explican, agregan datos o dan ejemplos.', 'Si se borran, el texto pierde detalle, no sentido.', 'La principal es la que no se puede borrar.'])],
 'recuerda': [
   R('Texto expositivo', 'explica un tema con información precisa, en tercera persona, sin contar historias ni opinar.', 'El carpincho es el roedor más grande del mundo.'),
   R('Tema', 'es aquello de lo que trata el texto, dicho en pocas palabras y sin detalles.', 'El nido del hornero'),
   R('Idea principal', 'es lo más importante que el texto dice sobre el tema, y puede no estar escrita.', 'El hornero construye su nido con barro.'),
   R('Ideas secundarias', 'explican, agregan datos o dan ejemplos sobre la idea principal.', 'Tarda varias semanas en terminarlo.'),
   R('Prueba del borrado', 'consiste en tachar una oración: si el párrafo pierde sentido, era la principal.', 'Sin «viajan miles de kilómetros», no se entiende.')]}

L['2'] = {'temas': [
 T('El cuadro sinóptico',
   m('esquema', items=[
     {'nombre': 'Los anfibios', 'raiz': 'Anfibios', 'ramas': [['Dónde viven', ['en el agua y en la tierra'], 'Una rama por cada aspecto del tema.'], ['Piel', ['húmeda y sin escamas'], 'Solo palabras clave.'], ['Desarrollo', ['huevo', 'renacuajo', 'adulto'], 'Una rama puede abrir varias ideas.'], ['Ejemplos', ['rana, sapo, salamandra'], 'Los ejemplos también entran.']], 'cierre': 'A la izquierda el tema; con llaves, lo que lo explica.'},
     {'nombre': 'La luna', 'raiz': 'La Luna', 'ramas': [['Qué es', ['satélite natural de la Tierra'], 'Definición.'], ['Fases', ['nueva', 'creciente', 'llena', 'menguante'], 'Partes del tema.'], ['Efecto', ['mareas'], 'Una consecuencia.']], 'cierre': 'Se lee de izquierda a derecha, de lo general a lo particular.'}]),
   m('clasificar_x', consigna='Armá el cuadro sinóptico de «Los planetas»: ubicá cada dato en su llave.', cajas=['Rocosos', 'Gaseosos'], cuantos=6, items=[
     ['Mercurio', 0], ['Venus', 0], ['Tierra', 0], ['Marte', 0], ['Júpiter', 1], ['Saturno', 1], ['Urano', 1], ['Neptuno', 1]]),
   ('Cuadro sinóptico', 'El cuadro sinóptico es un esquema que ordena las ideas con llaves: a la izquierda el tema general y hacia la derecha las ideas que lo explican.'),
   'Sirve para estudiar porque muestra la jerarquía de un vistazo: qué es lo más general y qué depende de qué. En las llaves no van oraciones completas, sino palabras clave que alcanzan para recordar la idea.',
   ['Izquierda: el tema.', 'Llaves: los aspectos y, adentro, sus datos.', 'Solo palabras clave, nunca oraciones largas.']),
 T('El cuadro comparativo',
   m('esquema', items=[
     {'nombre': 'Rana y sapo', 'cols': ['', 'Rana', 'Sapo'], 'filas': [['Piel', 'lisa y húmeda', 'rugosa y seca'], ['Patas', 'largas, para saltar', 'cortas, para caminar'], ['Dónde vive', 'cerca del agua', 'también lejos del agua']], 'cierre': 'Las mismas características para los dos, fila por fila.'},
     {'nombre': 'Sol y Luna', 'cols': ['', 'Sol', 'Luna'], 'filas': [['Qué es', 'una estrella', 'un satélite'], ['Luz', 'propia', 'refleja la del Sol'], ['Distancia', 'muy lejos', 'muy cerca']], 'cierre': 'Así se ven los parecidos y las diferencias.'}]),
   m('completar_x', consigna='Completá el cuadro comparativo entre el día y la noche.', items=[
     {'texto': 'Luz: día → [[luz solar/oscuridad/luz de luna]] · noche → [[poca luz/luz solar/sol fuerte]]. Temperatura: día → [[más alta/más baja/igual]] · noche → [[más baja/más alta/igual]].'},
     {'texto': 'Mamífero o no: delfín → [[mamífero/pez/reptil]] · tiburón → [[pez/mamífero/ave]]. Cómo respira: delfín → [[pulmones/branquias/piel]] · tiburón → [[branquias/pulmones/piel]].'}]),
   ('Cuadro comparativo', 'El cuadro comparativo es una tabla que ubica en columnas dos o más cosas y en filas las características que se comparan.'),
   'La regla es comparar siempre lo mismo para todos: si una fila habla de la piel de la rana, tiene que hablar también de la piel del sapo. Por eso conviene elegir primero las características y después llenar cada casillero.',
   ['Columnas: lo que se compara.', 'Filas: las mismas características para todos.', 'Sirve para ver parecidos y diferencias.']),
 T('Palabras clave',
   m('transformar', items=[
     {'nombre': 'Las obreras', 'antes': 'Las abejas obreras son las encargadas de salir de la colmena para recolectar el néctar de las flores.', 'pasos': [{'v': '{{Obreras}}: salen de la colmena a recolectar néctar.', 'txt': 'Quitamos lo que no suma.'}, {'v': '{{Obreras: recolectan néctar.}}', 'txt': 'Quedan las palabras que guardan la idea.'}], 'cierre': 'Tres palabras alcanzan para recordar la oración.'},
     {'nombre': 'Los glaciares', 'antes': 'Los glaciares son grandes masas de hielo que se forman en las montañas cuando la nieve se acumula durante muchos años.', 'pasos': [{'v': '{{Glaciares}}: masas de hielo en montañas.', 'txt': 'El tema y la definición.'}, {'v': 'Glaciares: masas de hielo · {{nieve acumulada}}.', 'txt': 'Y cómo se forman.'}], 'cierre': 'Las palabras clave condensan la idea.'}]),
   m('elegir_x', consigna='¿Qué opción tiene las mejores palabras clave para esta oración?', items=[
     {'cons': '«Los murciélagos se orientan en la oscuridad gracias a los sonidos que emiten y que rebotan en los objetos.»', 'ops': ['Murciélagos: se orientan con eco', 'Los murciélagos se orientan en la oscuridad', 'Oscuridad, sonidos, objetos'], 'ayuda': 'Tiene que quedar el tema y la idea, en pocas palabras.'},
     {'cons': '«El corazón es un músculo que bombea la sangre a todo el cuerpo a través de las arterias.»', 'ops': ['Corazón: músculo que bombea sangre', 'El corazón es un músculo', 'Arterias y cuerpo'], 'ayuda': 'Qué es y qué hace.'}]),
   ('Palabras clave', 'Las palabras clave son las pocas palabras que condensan una idea y alcanzan para recordarla sin la oración completa.'),
   'Se usan en esquemas, cuadros y fichas para estudiar. Una buena palabra clave conserva el tema y lo que se dice de él; si elegís palabras sueltas sin relación, después no vas a recordar la idea.',
   ['Conservan el tema y la idea.', 'Se quitan artículos y detalles.', 'Si al releerlas no recordás la idea, faltan palabras.'])],
 'recuerda': [
   R('Cuadro sinóptico', 'ordena las ideas con llaves, del tema general a la izquierda a los datos a la derecha.', 'Anfibios { piel, desarrollo, ejemplos'),
   R('Cuadro comparativo', 'pone en columnas lo que se compara y en filas las mismas características para todos.', 'Rana / sapo: piel, patas, dónde vive'),
   R('Palabras clave', 'son las pocas palabras que condensan una idea y alcanzan para recordarla.', 'Obreras: recolectan néctar.'),
   R('Elegir el esquema', 'las llaves sirven para partes de un tema y el cuadro comparativo para comparar.', 'Planetas en llaves; rana y sapo en cuadro')]}

L['3'] = {'temas': [
 T('Parafrasear',
   m('transformar', items=[
     {'nombre': 'El Sol', 'antes': 'La Luna no tiene luz propia: brilla porque refleja la luz del Sol.', 'pasos': [{'v': 'La Luna {{no produce luz}}: brilla porque refleja la del Sol.', 'txt': 'Cambiamos una expresión por otra que dice lo mismo.'}, {'v': '{{La luz que vemos en la Luna viene del Sol}}; ella no produce luz.', 'txt': 'Cambiamos también el orden.'}], 'cierre': 'Mismo sentido, otras palabras.'},
     {'nombre': 'Las plantas', 'antes': 'Las plantas fabrican su alimento usando la luz del sol.', 'pasos': [{'v': '{{Gracias a la luz solar}}, las plantas producen su propio alimento.', 'txt': 'Otro orden y otras palabras, la misma idea.'}], 'cierre': 'Parafrasear demuestra que entendiste.'}]),
   m('elegir_x', consigna='¿Cuál es una buena paráfrasis?', items=[
     {'cons': 'Original: «Los osos polares tienen una capa de grasa que los protege del frío.»', 'ops': ['Una gruesa capa de grasa abriga a los osos polares', 'Los osos polares tienen una capa de grasa que los protege del frío', 'Los osos polares no sienten nunca el frío'], 'ayuda': 'Ni copiar ni cambiar el sentido.'},
     {'cons': 'Original: «El agua cubre casi tres cuartas partes de la superficie terrestre.»', 'ops': ['La mayor parte de la superficie de la Tierra está cubierta de agua', 'El agua cubre casi tres cuartas partes de la superficie terrestre', 'En la Tierra hay más tierra que agua'], 'ayuda': 'La tercera cambia el sentido.'}]),
   ('Parafrasear', 'Parafrasear es decir lo mismo que un texto con otras palabras, sin copiarlo y sin cambiar su sentido.'),
   'Es la base para exponer y para resumir: si podés decirlo con tus palabras, es porque lo entendiste. Hay dos errores típicos: copiar casi igual, cambiando una sola palabra, o cambiar tanto que el sentido ya no es el mismo.',
   ['Cambiar palabras y orden, no la idea.', 'No vale copiar cambiando una palabra.', 'Comprobá que diga exactamente lo mismo.']),
 T('Las partes de una exposición',
   m('esquema', items=[
     {'nombre': 'Los pingüinos', 'raiz': 'Exposición: los pingüinos', 'ramas': [['Apertura', ['presento el tema y digo para qué lo voy a explicar'], '«Hoy les voy a contar cómo sobreviven los pingüinos al frío.»'], ['Desarrollo', ['explico las ideas en orden, con ejemplos'], 'Plumas, grasa, vida en grupo: una idea por vez.'], ['Cierre', ['resumo lo más importante'], '«En síntesis, su cuerpo y su vida en grupo los protegen del frío.»']], 'cierre': 'Apertura, desarrollo y cierre.'}]),
   m('ordenar_x', consigna='Ordená las partes de esta exposición.', items=[
     {'lista': ['Hoy voy a explicar por qué se producen los terremotos.', 'La corteza terrestre está dividida en placas que se mueven.', 'Cuando dos placas chocan, la tierra tiembla.', 'En resumen, los terremotos son el resultado del movimiento de las placas.']},
     {'lista': ['Les voy a contar cómo se forma la lluvia.', 'El sol calienta el agua y la convierte en vapor.', 'El vapor sube, se enfría y forma nubes.', 'Para terminar: la lluvia es agua que vuelve después de subir como vapor.']}]),
   ('Exposición oral', 'La exposición oral es la explicación de un tema a otras personas, preparada antes con un esquema y organizada en apertura, desarrollo y cierre.'),
   'En una escuela online, la exposición suele grabarse en video: eso permite ensayar y volver a grabar. Lo importante es no leer de corrido, sino hablar a partir del esquema, con palabras clave que recuerden cada idea en su orden.',
   ['Apertura: el tema y para qué.', 'Desarrollo: una idea por vez, con ejemplos.', 'Cierre: lo más importante en pocas palabras.']),
 T('Conectores para ordenar lo que digo',
   m('marcar', rotulo='Fragmento', items=[
     {'nombre': 'La miel', 'texto': '{{En primer lugar|Abre: anuncia la primera idea.}}, las abejas juntan néctar. {{Además|Suma otra idea.}}, lo guardan en panales. {{Por ejemplo|Introduce un ejemplo.}}, una colmena puede tener miles de celdas. {{En conclusión|Cierra la exposición.}}, la miel es el resultado de mucho trabajo.', 'cierre': 'Los conectores guían al que escucha.'}]),
   m('completar_x', consigna='Elegí el conector que corresponde.', items=[
     {'texto': '[[Para empezar/En conclusión/Además]], voy a explicar qué es un eclipse. [[Además/Para empezar/En conclusión]], veremos sus tipos. [[En conclusión/Además/Por ejemplo]], un eclipse es una sombra en el cielo.'},
     {'texto': 'Hay animales que hibernan. [[Por ejemplo/En conclusión/En primer lugar]], el oso. [[También/Para terminar/Por ejemplo]] lo hacen algunos murciélagos.'}]),
   ('Conectores de orden', 'Los conectores de orden son expresiones que anuncian, en una exposición, cuándo empieza una idea, cuándo se suma otra, cuándo llega un ejemplo y cuándo se cierra.'),
   'Quien escucha no puede volver atrás como en un libro, por eso necesita estas señales para seguir el hilo. Usá uno distinto para cada función y no los repitas: tres «además» seguidos cansan.',
   ['Empezar: en primer lugar, para empezar.', 'Sumar: además, también. Ejemplo: por ejemplo.', 'Cerrar: en conclusión, para terminar.'])],
 'recuerda': [
   R('Parafrasear', 'es decir lo mismo que un texto con otras palabras, sin copiar y sin cambiar el sentido.', 'La luz de la Luna viene del Sol.'),
   R('Exposición oral', 'explica un tema a otros a partir de un esquema, con apertura, desarrollo y cierre.', 'Los pingüinos y el frío'),
   R('Apertura y cierre', 'la apertura presenta el tema y el cierre resume lo más importante.', '«En síntesis, …»'),
   R('Conectores de orden', 'anuncian el comienzo, una idea nueva, un ejemplo o el final de lo que se explica.', 'En primer lugar, además, en conclusión')]}

L['4'] = {'temas': [
 T('Qué es un resumen',
   m('capas', items=[
     {'nombre': 'El ombú', 'texto': '{{El ombú es una planta típica de la llanura pampeana.|idea principal|Se queda: es lo esencial.}} {{Aunque parece un árbol, en realidad es una hierba gigante.|idea principal|Se queda: dato central.}} {{Algunos tienen más de cien años.|detalle|Se puede sacar.}} {{Su sombra era muy valorada por los gauchos.|detalle|Se puede sacar.}}', 'borrado': 'idea principal', 'cierre': 'Resumen: el ombú, típico de la pampa, es una hierba gigante aunque parezca un árbol.'}]),
   m('elegir_x', consigna='¿Cuál es el mejor resumen?', items=[
     {'cons': 'Texto: «Las tortugas marinas ponen sus huevos en la playa. Cavan un pozo en la arena, ponen cerca de cien huevos y los tapan. Cuando nacen, las crías corren hacia el mar.»', 'ops': ['Las tortugas marinas desovan en la arena de la playa y sus crías, al nacer, van al mar.', 'Las tortugas cavan un pozo en la arena.', 'Me parece increíble que las tortugas pongan cien huevos.'], 'ayuda': 'Ni un solo dato ni una opinión: todas las ideas principales, breves.'},
     {'cons': 'Texto: «El cóndor andino es una de las aves voladoras más grandes. Sus alas abiertas miden más de tres metros. Planea aprovechando las corrientes de aire caliente y casi no aletea.»', 'ops': ['El cóndor es un ave enorme que planea con las corrientes de aire, casi sin aletear.', 'Las alas del cóndor miden tres metros.', 'El cóndor es el ave más linda de los Andes.'], 'ayuda': 'Un buen resumen se entiende solo.'}]),
   ('Resumen', 'El resumen es un texto nuevo y corto que reúne solo lo esencial de otro texto, contado con palabras propias y sin agregar opiniones.'),
   'La prueba de que quedó bien es que alguien que no leyó el texto original pueda entenderlo, y que ocupe bastante menos espacio. Para lograrlo, primero se busca lo esencial de cada párrafo y después se une todo con conectores, como quien arma un texto distinto.',
   ['Conserva las ideas principales.', 'Se escribe con tus palabras.', 'No lleva opiniones ni detalles de más.']),
 T('Generalizar',
   m('transformar', items=[
     {'nombre': 'Frutas', 'antes': 'En el mercado venden manzanas, peras, naranjas y bananas.', 'pasos': [{'v': 'En el mercado venden {{frutas}}.', 'txt': 'Cuatro palabras se reemplazan por una que las incluye.'}], 'cierre': 'Más corto y dice lo mismo.'},
     {'nombre': 'Útiles', 'antes': 'Llevá lápices, gomas, reglas y cuadernos.', 'pasos': [{'v': 'Llevá {{útiles escolares}}.', 'txt': 'Una expresión general reemplaza la lista.'}], 'cierre': 'Generalizar acorta sin perder la idea.'},
     {'nombre': 'Acciones', 'antes': 'Se levantó, se lavó la cara, se vistió y desayunó.', 'pasos': [{'v': '{{Se preparó para salir}}.', 'txt': 'También se pueden resumir acciones en una sola.'}], 'cierre': 'Una frase en lugar de cuatro.'}]),
   m('completar_x', consigna='Elegí la palabra que generaliza la lista.', items=[
     {'texto': 'Perros, gatos y conejos → [[mascotas/animales salvajes/aves]]. Mesa, silla y placard → [[muebles/herramientas/útiles]].'},
     {'texto': 'Rojo, verde y azul → [[colores/frutas/formas]]. Fútbol, vóley y básquet → [[deportes/juegos de mesa/instrumentos]].'},
     {'texto': 'Guitarra, piano y violín → [[instrumentos/muebles/herramientas]]. Lunes, martes y miércoles → [[días/meses/estaciones]].'}]),
   ('Generalizar', 'Generalizar es reemplazar una lista de palabras o de acciones por una sola expresión que las incluye a todas.'),
   'Es una de las herramientas más útiles para resumir, porque acorta el texto sin perder información importante. La palabra general tiene que ser precisa: «animales» es demasiado amplio para hablar de perros y gatos si el texto trata de mascotas.',
   ['Lista de cosas → una palabra que las incluye.', 'Varias acciones → una acción general.', 'Elegí la palabra justa, ni muy amplia ni muy estrecha.']),
 T('Escribir el resumen',
   m('transformar', items=[
     {'nombre': 'El mate', 'antes': 'El mate es una infusión que se prepara con hojas de yerba mate. Los guaraníes ya la consumían antes de la llegada de los españoles. Hoy se toma en la Argentina, Uruguay, Paraguay y el sur de Brasil, y compartirlo es una costumbre muy común.', 'pasos': [{'v': '{{El mate es una infusión de yerba}}', 'txt': 'Idea principal del primer tramo, con otras palabras.'}, {'v': 'El mate es una infusión de yerba {{que ya tomaban los guaraníes}}', 'txt': 'Sumamos el origen.'}, {'v': 'El mate es una infusión de yerba que ya tomaban los guaraníes {{y que hoy se comparte en varios países de la región.}}', 'txt': 'Generalizamos la lista de países.'}], 'cierre': 'Tres oraciones largas en una sola.'}]),
   m('escribir_x', items=[
     {'cons': 'Resumí en una o dos oraciones: «Los pulpos tienen ocho brazos llenos de ventosas. Pueden cambiar de color para camuflarse. Además, son muy inteligentes: algunos aprenden a abrir frascos.»', 'criterios': [{'txt': 'Entre 12 y 40 palabras', 'min': 12}, {'txt': 'Nombra el tema', 're': 'pulpo'}, {'txt': 'Incluye el camuflaje o el color', 're': 'color|camufl'}, {'txt': 'Incluye la inteligencia', 're': 'inteligen|aprend'}], 'modelo': 'Los pulpos tienen ocho brazos con ventosas, cambian de color para esconderse y son muy inteligentes.'}]),
   ('Pasos del resumen', 'Para resumir se lee el texto completo, se marca la idea principal de cada parte, se generaliza lo que se pueda y se escribe un texto nuevo y breve con palabras propias.'),
   'Al final conviene revisar dos cosas: que se entienda solo, sin haber leído el original, y que no haya opiniones propias ni datos inventados. Si el resumen quedó casi tan largo como el texto, todavía tiene detalles de más.',
   ['1. Leo todo y marco las ideas principales.', '2. Generalizo y uno las ideas con conectores.', '3. Reviso: ¿se entiende solo?, ¿es breve?'])],
 'recuerda': [
   R('Resumen', 'reúne en un texto corto lo esencial de otro, contado con palabras propias y sin opinar.', 'El ombú es una hierba gigante de la pampa.'),
   R('Generalizar', 'es reemplazar una lista por una expresión que la incluye toda.', 'manzanas, peras y naranjas → frutas'),
   R('Pasos del resumen', 'leer, marcar las ideas principales, generalizar y escribir un texto nuevo y breve.', 'El mate: infusión de yerba de origen guaraní'),
   R('Revisar el resumen', 'hay que comprobar que se entienda solo y que no tenga opiniones ni datos inventados.', '¿Se entiende sin el original?')]}

A = {
 '1': [
   CLA('¿Qué fragmentos son de un texto expositivo?', ['Expositivo', 'No expositivo'], [('El ombú es una hierba gigante de la pampa.', 'Expositivo'), ('Los colibríes baten sus alas muy rápido.', 'Expositivo'), ('Ese verano, Juan subió a un ombú enorme.', 'No expositivo'), ('Había una vez un colibrí que no sabía volar.', 'No expositivo')], 'El expositivo explica; el narrativo cuenta una historia.'),
   MC('«Las tormentas eléctricas se forman cuando el aire caliente sube rápido. Al chocar con aire frío, se generan nubes de tormenta. Dentro de ellas se producen los rayos.» ¿Cuál es el tema?', ['Cómo se forman las tormentas eléctricas', 'El aire caliente', 'Los rayos peligrosos'], 'Cómo se forman las tormentas eléctricas', 'El tema es de qué trata el texto en pocas palabras.', 'analizar'),
   MS('Elegí las DOS ideas secundarias: «Los camellos resisten muchos días sin beber. Guardan grasa en sus jorobas. Sus pestañas largas los protegen de la arena.»', ['Guardan grasa en sus jorobas.', 'Sus pestañas largas los protegen de la arena.', 'Los camellos resisten muchos días sin beber.'], ['Guardan grasa en sus jorobas.', 'Sus pestañas largas los protegen de la arena.'], 'La principal es la primera: las otras la explican o suman datos.'),
   MC('Un compañero dice que la idea principal siempre es la primera oración. ¿Qué le contestás?', ['No siempre: puede estar al final o no estar escrita', 'Tiene razón, siempre es la primera', 'La idea principal es el título'], 'No siempre: puede estar al final o no estar escrita', 'A veces hay que armarla uniendo las ideas.', 'error')],
 '2': [
   CLA('Armá el cuadro sinóptico de «Los estados del agua».', ['Sólido', 'Líquido', 'Gaseoso'], [('hielo', 'Sólido'), ('granizo', 'Sólido'), ('lluvia', 'Líquido'), ('vapor', 'Gaseoso')], 'Cada dato va en su llave.'),
   UNI('Uní cada tipo de texto con el esquema que mejor le sirve.', [('Partes de una célula', 'Cuadro sinóptico'), ('Diferencias entre ríos y lagos', 'Cuadro comparativo'), ('Pasos para hacer pan', 'Secuencia con flechas')], 'El esquema depende de cómo está organizado el texto.'),
   MC('¿Cuáles son las mejores palabras clave para «Las ballenas azules son los animales más grandes que existieron en la Tierra»?', ['Ballena azul: el animal más grande', 'Ballenas, Tierra, existieron', 'Las ballenas azules son grandes'], 'Ballena azul: el animal más grande', 'Conservan el tema y la idea.', 'analizar'),
   MC('En un cuadro comparativo entre perros y gatos, Martín puso en la fila «Alimento»: perro → «carne y balanceado»; gato → «son muy independientes». ¿Qué error hay?', ['La fila del gato no habla del alimento', 'Le faltan columnas para otros animales', 'No hay ningún error en ese cuadro'], 'La fila del gato no habla del alimento', 'Cada fila compara la misma característica.', 'error')],
 '3': [
   MC('¿Cuál es una buena paráfrasis de «El cerebro consume mucha energía aunque estemos dormidos»?', ['Incluso mientras dormimos, el cerebro gasta mucha energía', 'El cerebro consume mucha energía aunque estemos dormidos', 'Cuando dormimos, el cerebro se apaga'], 'Incluso mientras dormimos, el cerebro gasta mucha energía', 'Otras palabras, mismo sentido.', 'analizar'),
   ORD('Ordená la exposición sobre los glaciares.', ['Voy a explicar qué son los glaciares.', 'Son masas de hielo que se forman en las montañas.', 'Por ejemplo, el Perito Moreno está en Santa Cruz.', 'En conclusión, los glaciares son grandes reservas de agua.'], 'Apertura, desarrollo con ejemplo y cierre.'),
   FB('Completá con conectores: «___, explicaré qué es un cometa. ___, veremos de qué está hecho. ___, el Halley pasa cada 76 años».', [['En primer lugar', 'Para empezar', 'Primero'], ['Además', 'También', 'Después', 'Luego'], ['Por ejemplo']], 'Empezar, sumar y dar un ejemplo.'),
   KW('Escribí la apertura de una exposición de un minuto sobre un animal que te guste: presentá el tema y decí para qué lo vas a explicar.', 'Usá un conector para empezar y nombrá el animal.', [['voy a', 'les voy', 'hoy'], ['explicar', 'contar', 'mostrar']], 2, 'La apertura presenta el tema y el propósito.')],
 '4': [
   TF('Un buen resumen puede incluir la opinión de quien lo escribe.', 'Falso', 'El resumen reproduce lo que dice el texto, sin opiniones.'),
   FB('Generalizá: «Compramos lechuga, tomate, zanahoria y zapallo» → «Compramos ___».', [['verduras', 'hortalizas', 'vegetales']], 'Una palabra que incluya a todas.'),
   MC('Juana resumió un texto de 200 palabras en 180. ¿Qué le falta hacer?', ['Sacar detalles y ejemplos, y generalizar', 'Agregar su opinión', 'Copiar las oraciones principales textuales'], 'Sacar detalles y ejemplos, y generalizar', 'Un resumen es mucho más corto que el original.', 'error'),
   KW('Resumí en dos oraciones: «Los colibríes son las aves más pequeñas. Algunos pesan menos de dos gramos. Baten las alas tan rápido que pueden quedarse quietos en el aire. Se alimentan del néctar de las flores.»', 'Conservá las ideas principales y generalizá.', [['colibr*'], ['pequeñ*', 'chic*'], ['néctar', 'flores'], ['quiet*', 'alas', 'aire']], 3, 'Las aves más chicas, que se quedan quietas en el aire y comen néctar.', 'aplicar')],
}

EX = [
 [1, MC('«Los pingüinos emperador viven en la Antártida. Soportan temperaturas de 40 grados bajo cero. Se juntan en grupos para darse calor.» ¿Cuál es la idea principal?', ['Los pingüinos emperador viven en un lugar muy frío y se adaptan a él', 'Se juntan en grupos', 'La temperatura es de 40 grados bajo cero'], 'Los pingüinos emperador viven en un lugar muy frío y se adaptan a él', 'La idea principal une lo que dicen las oraciones.', 'analizar')],
 [1, CLA('¿Expositivo o narrativo?', ['Expositivo', 'Narrativo'], [('Los volcanes expulsan lava y cenizas.', 'Expositivo'), ('El día que el volcán despertó, huimos al cerro.', 'Narrativo'), ('El agua se congela a cero grados.', 'Expositivo'), ('Mi abuela me contó que una vez nevó en Rosario.', 'Narrativo')], 'Explicar o contar.')],
 [1, MS('Prueba del borrado: elegí las oraciones que se pueden sacar sin perder la idea principal de «Las llamas viven en los Andes. Tienen un pelaje grueso. Pueden cargar hasta 30 kilos».', ['Tienen un pelaje grueso.', 'Pueden cargar hasta 30 kilos.', 'Las llamas viven en los Andes.'], ['Tienen un pelaje grueso.', 'Pueden cargar hasta 30 kilos.'], 'La primera es la principal.')],
 [2, UNI('Uní cada esquema con su característica.', [('Cuadro sinóptico', 'Usa llaves de lo general a lo particular'), ('Cuadro comparativo', 'Tiene columnas y filas'), ('Palabras clave', 'Condensan una idea en pocas palabras')], 'Cada herramienta tiene su forma.')],
 [2, CLA('¿Qué esquema conviene para estudiar cada tema?', ['Cuadro comparativo', 'Cuadro sinóptico'], [('Diferencias entre mamíferos y aves', 'Cuadro comparativo'), ('Partes de una flor', 'Cuadro sinóptico'), ('Ríos y lagos: parecidos y diferencias', 'Cuadro comparativo'), ('Tipos de rocas', 'Cuadro sinóptico')], 'Comparar → columnas y filas; partes y tipos → llaves.', 'analizar')],
 [2, FB('Escribí palabras clave para «Los ríos de llanura corren despacio porque el terreno es casi plano»: «Ríos de llanura: ___ por terreno ___».', [['lentos', 'despacio', 'corren despacio'], ['plano', 'llano', 'casi plano']], 'El tema y la idea, sin artículos.')],
 [3, ODD('¿Cuál de estas NO es una paráfrasis de «Las abejas polinizan las flores»?', ['Las abejas tienen un aguijón', 'Las flores son polinizadas por las abejas', 'Gracias a las abejas, las flores se polinizan', 'Las abejas llevan el polen de flor en flor'], 'Las abejas tienen un aguijón', 'Cambia el sentido: habla de otra cosa.', 'error')],
 [3, ORD('Ordená la exposición sobre la Vía Láctea.', ['Voy a contarles qué es la Vía Láctea.', 'Es la galaxia donde está nuestro sistema solar.', 'Tiene forma de espiral y miles de millones de estrellas.', 'En conclusión, vivimos dentro de una galaxia gigante.'], 'Apertura, desarrollo y cierre.')],
 [3, SA('¿Qué conector usarías para cerrar una exposición? Escribí uno.', ['en conclusion', 'en conclusión', 'para terminar', 'en resumen', 'en sintesis', 'en síntesis', 'para finalizar', 'finalmente'], 'Cerrar: en conclusión, para terminar, en síntesis.', 'aplicar')],
 [4, MC('¿Cuál es el mejor resumen de «El tango nació en Buenos Aires y Montevideo a fines del siglo XIX. Al principio se bailaba en los barrios. Con el tiempo llegó a todo el mundo»?', ['El tango, nacido en el Río de la Plata, pasó de los barrios al mundo.', 'El tango se bailaba en los barrios.', 'El tango es el baile más lindo.'], 'El tango, nacido en el Río de la Plata, pasó de los barrios al mundo.', 'Todas las ideas principales, sin opinión.', 'analizar')],
 [4, FB('Generalizá: «Saltó, corrió, nadó y trepó» → «Hizo mucho ___».', [['ejercicio', 'deporte', 'actividad física']], 'Una expresión que incluya todas las acciones.')],
 [4, MC('Lucas terminó su resumen con «A mí este tema me parece aburrido». ¿Qué error cometió?', ['Agregó una opinión propia', 'Usó palabras propias', 'Fue demasiado breve'], 'Agregó una opinión propia', 'El resumen no lleva opiniones.', 'error')],
 [4, KW('Resumí con tus palabras en una o dos oraciones: «Las hojas de los árboles cambian de color en otoño. Esto ocurre porque dejan de producir clorofila, la sustancia que las hace verdes. Entonces aparecen los amarillos y rojos que estaban ocultos».', 'Conservá la idea principal y la causa.', [['hoja*'], ['otoño'], ['clorofila', 'verde']], 3, 'En otoño las hojas cambian de color porque dejan de producir clorofila.', 'aplicar')],
]

def ajustes(M):
    for k, v in A.items(): M['act'][k] = v
    for q in M['act'].get('5', []): q.setdefault('n', 'recordar')
    M['examen'] = EX
    M['actualizar_preguntas'] = True

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-5/mision-5.json', L, ajustes=ajustes)
