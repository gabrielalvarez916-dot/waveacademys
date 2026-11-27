# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 4 · Sujeto y predicado (la animación queda; lección, actividades y examen nuevos)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD

L = {}
L['1'] = {'temas': [
 T('Sujeto y predicado',
   m('oracion', items=[
     {'partes': [['Las nubes negras', 'S', 'El <b>sujeto</b>: de quién se habla.'], ['taparon el sol de golpe', 'P', 'El <b>predicado</b>: lo que se dice del sujeto.']], 'cierre': 'Toda oración bimembre se divide en estas dos partes.'},
     {'partes': [['Mi abuelo', 'S', 'Sujeto: de quién hablamos.'], ['arregla bicicletas en su taller', 'P', 'Predicado: qué hace.']], 'cierre': 'Sujeto + predicado.'}]),
   m('analizar_x', consigna='Llevá cada etiqueta a su parte: S (sujeto) o P (predicado).', items=[
     {'bloques': [['Los delfines', 'S'], ['saltaban junto al barco', 'P']]},
     {'bloques': [['La maestra de música', 'S'], ['trajo una guitarra nueva', 'P']]},
     {'bloques': [['Mis primos de Salta', 'S'], ['llegan el viernes', 'P']]}]),
   ('Sujeto y predicado', 'El sujeto es la parte de la oración que nombra de quién o de qué se habla, y el predicado es lo que se dice de ese sujeto.'),
   'Dividir la oración en estas dos partes es el primer paso de todo análisis. El predicado siempre contiene al verbo conjugado; el sujeto, en cambio, suele tener un sustantivo como palabra central.',
   ['Sujeto: ¿de quién se habla?', 'Predicado: ¿qué se dice de él?', 'El verbo conjugado siempre está en el predicado.']),
 T('Cómo encontrar el sujeto',
   m('marcar', rotulo='Oración', items=[
     {'nombre': 'Sujeto al final', 'texto': 'Por la ventana {{entraba|Paso 1: buscamos el verbo conjugado.}} {{un viento helado|Paso 2: le preguntamos al verbo ¿qué entraba? La respuesta es el sujeto.}}.', 'cierre': 'El sujeto puede ir al final: no hay que buscarlo siempre al principio.'},
     {'nombre': 'Sujeto en el medio', 'texto': 'Anoche {{los perros del barrio|Paso 2: ¿quiénes ladraron? Los perros del barrio.}} {{ladraron|Paso 1: el verbo.}} sin parar.', 'cierre': 'Primero el verbo, después la pregunta.'}]),
   m('etiquetar_x', consigna='Tocá una etiqueta y después la parte de la oración. Ojo: el sujeto no siempre está primero.', items=[
     {'texto': '[[En la plaza jugaban|Predicado]] [[unos chicos|Sujeto]] [[hasta tarde|Predicado]]'},
     {'texto': '[[Me encanta|Predicado]] [[el olor del pan recién hecho|Sujeto]]'},
     {'texto': '[[Ayer llegó|Predicado]] [[la carta de mi tía|Sujeto]]'}]),
   ('Cómo encontrar el sujeto', 'Para encontrar el sujeto se busca primero el verbo conjugado y se le pregunta quién o qué realiza esa acción.'),
   'El orden de las palabras engaña: muchas veces el sujeto aparece en el medio o al final de la oración. Si arrancás siempre por el verbo, no importa dónde esté. Cuando el sujeto va en el medio, el predicado queda partido en dos partes.',
   ['Paso 1: encontrá el verbo conjugado.', 'Paso 2: preguntale ¿quién? o ¿qué?', 'Lo que responde es el sujeto, esté donde esté.']),
 T('Sujeto simple, compuesto y concordancia',
   m('marcar', rotulo='Oración', items=[
     {'nombre': 'Compuesto', 'texto': '{{Mi hermana y su amiga|Sujeto compuesto: dos núcleos unidos por «y».}} {{viajaron|El verbo va en plural porque son dos.}} a Mendoza.', 'cierre': 'Dos núcleos → verbo en plural.'},
     {'nombre': 'Simple', 'texto': '{{El equipo de mi escuela|Sujeto simple: un solo núcleo, «equipo».}} {{ganó|Verbo en singular: concuerda con «equipo», no con «escuela».}} la final.', 'cierre': 'El verbo concuerda con el núcleo del sujeto.'}]),
   m('completar_x', consigna='Elegí la forma del verbo que concuerda con el sujeto.', items=[
     {'texto': 'El perro y el gato [[duermen/duerme]] juntos. La caja de los lápices [[está/están]] vacía.'},
     {'texto': 'Ni mi primo ni yo [[sabíamos/sabía]] el camino. Los chicos del quinto piso [[gritan/grita]] mucho.'},
     {'texto': 'Me [[gustan/gusta]] las películas de terror. Me [[gusta/gustan]] el helado de limón.'}]),
   ('Sujeto compuesto', 'El sujeto compuesto tiene dos o más núcleos unidos por una conjunción, como y, ni u o, y el verbo concuerda con todos en plural.'),
   'La concordancia es que el verbo coincida en número y persona con el núcleo del sujeto. El error más común aparece cuando hay otras palabras entre el núcleo y el verbo: en «la caja de los lápices está vacía», el núcleo es «caja», no «lápices».',
   ['Simple: un solo núcleo.', 'Compuesto: dos o más núcleos unidos por y, ni, o.', 'El verbo concuerda con el núcleo, no con la palabra más cercana.'])],
 'recuerda': [
   R('Sujeto', 'es la parte de la oración que nombra de quién o de qué se habla.', 'Las nubes negras taparon el sol.'),
   R('Predicado', 'es lo que se dice del sujeto y siempre contiene el verbo conjugado.', 'taparon el sol de golpe'),
   R('Encontrar el sujeto', 'se busca el verbo y se le pregunta quién o qué realiza la acción.', '¿Qué entraba? Un viento helado.'),
   R('Sujeto compuesto', 'tiene dos o más núcleos unidos por conjunción y lleva el verbo en plural.', 'Mi hermana y su amiga viajaron.'),
   R('Concordancia', 'es que el verbo coincida en número y persona con el núcleo del sujeto.', 'La caja de los lápices está vacía.')]}

L['2'] = {'temas': [
 T('Los núcleos',
   m('oracion', items=[
     {'partes': [['El viejo faro del puerto', 'S', 'Sujeto.', [['faro', 'N']]], ['ilumina a los barcos', 'P', 'Predicado.', [['ilumina', 'NV']]]], 'cierre': 'N: núcleo del sujeto (sustantivo) · NV: núcleo verbal.'},
     {'partes': [['Varias gaviotas blancas', 'S', 'Sujeto.', [['gaviotas', 'N']]], ['volaban sobre el agua', 'P', 'Predicado.', [['volaban', 'NV']]]], 'cierre': 'Cada parte tiene su palabra central.'}]),
   m('marcar_x', consigna='Tocá los dos núcleos: el del sujeto (sustantivo) y el del predicado (verbo).', items=[
     {'cons': 'Oración: «La bicicleta roja de Ana tiene un pinchazo.»', 'texto': '[[La|0]] [[bicicleta|1]] [[roja|0]] [[de|0]] [[Ana|0]] [[tiene|1]] [[un|0]] [[pinchazo|0]]'},
     {'cons': 'Oración: «Los alumnos nuevos visitaron el museo.»', 'texto': '[[Los|0]] [[alumnos|1]] [[nuevos|0]] [[visitaron|1]] [[el|0]] [[museo|0]]'},
     {'cons': 'Oración: «Un ruido extraño despertó a toda la familia.»', 'texto': '[[Un|0]] [[ruido|1]] [[extraño|0]] [[despertó|1]] [[a|0]] [[toda|0]] [[la|0]] [[familia|0]]'}]),
   ('Núcleo', 'El núcleo es la palabra más importante de cada parte: en el sujeto suele ser un sustantivo y en el predicado es el verbo conjugado, llamado núcleo verbal.'),
   'Para comprobar cuál es el núcleo, probá sacar las demás palabras: «El viejo faro del puerto ilumina» se puede reducir a «faro ilumina» y la oración sigue diciendo lo esencial. Lo que se puede sacar sin romper la idea son los modificadores.',
   ['Núcleo del sujeto (N): un sustantivo o un pronombre.', 'Núcleo del predicado (NV): el verbo conjugado.', 'Lo demás acompaña y se llama modificador.']),
 T('Modificador directo e indirecto',
   m('oracion', items=[
     {'partes': [['La casa de piedra', 'S', 'Sujeto.', [['La', 'MD'], ['casa', 'N'], ['de piedra', 'MI']]], ['se veía desde la ruta', 'P', 'Predicado.']], 'cierre': 'MD: pegado al núcleo · MI: empieza con preposición.'},
     {'partes': [['Los tres hijos del panadero', 'S', 'Sujeto.', [['Los', 'MD'], ['tres', 'MD'], ['hijos', 'N'], ['del panadero', 'MI']]], ['reparten el pan', 'P', 'Predicado.']], 'cierre': 'Puede haber varios MD.'}]),
   m('analizar_x', consigna='Analizá el sujeto: llevá cada etiqueta a su palabra.', items=[
     {'bloques': [['Una', 'MD'], ['lámpara', 'N'], ['antigua', 'MD'], ['de bronce', 'MI']]},
     {'bloques': [['El', 'MD'], ['perro', 'N'], ['de mis vecinos', 'MI']], 'extra': ['NV']},
     {'bloques': [['Las', 'MD'], ['flores', 'N'], ['del jardín', 'MI'], ['secas', 'MD']]}]),
   ('Modificadores del sujeto', 'El modificador directo (MD) es un artículo o un adjetivo pegado al núcleo; el modificador indirecto (MI) empieza con una preposición.'),
   'La diferencia está en cómo se unen al núcleo: el MD lo hace sin ninguna palabra en el medio, mientras que el MI necesita una preposición que haga de puente, como «de», «con» o «sin». Por eso, para encontrar un MI, buscá la preposición.',
   ['MD: artículos y adjetivos (la, tres, antigua).', 'MI: preposición + término (de piedra, sin techo).', '«del» = de + el: también arranca un MI.']),
 T('La aposición',
   m('oracion', items=[
     {'partes': [['Rosario, mi ciudad natal,', 'S', 'Sujeto.', [['Rosario', 'N'], ['mi ciudad natal', 'aposición']]], ['está junto al río Paraná', 'P', 'Predicado.']], 'cierre': 'La aposición nombra lo mismo que el núcleo con otras palabras.'},
     {'partes': [['Don Julio, el almacenero,', 'S', 'Sujeto.', [['Don Julio', 'N'], ['el almacenero', 'aposición']]], ['nos fía siempre', 'P', 'Predicado.']], 'cierre': 'Va entre comas cuando explica.'}]),
   m('analizar_x', consigna='Analizá el sujeto con aposición.', items=[
     {'bloques': [['Lola', 'N'], ['mi perra', 'aposición']], 'extra': ['MI']},
     {'bloques': [['El', 'MD'], ['Aconcagua', 'N'], ['la montaña más alta de América', 'aposición']]},
     {'bloques': [['Messi', 'N'], ['el capitán', 'aposición']], 'extra': ['MD']}]),
   ('Aposición', 'La aposición es un sustantivo, con sus modificadores, que se ubica junto al núcleo y lo nombra de otra manera para aclararlo.'),
   'Una prueba segura: si podés sacar el núcleo y dejar solo la aposición, la oración sigue diciendo lo mismo. «Mi ciudad natal está junto al río» funciona igual que «Rosario está junto al río», porque las dos expresiones se refieren a lo mismo.',
   ['Nombra lo mismo que el núcleo.', 'Cuando explica, va entre comas.', 'Prueba: reemplaza al núcleo sin cambiar el sentido.'])],
 'recuerda': [
   R('Núcleo del sujeto', 'es la palabra central del sujeto, casi siempre un sustantivo o un pronombre.', 'El viejo faro → faro'),
   R('Núcleo verbal', 'es el verbo conjugado, que funciona como la palabra central de todo el predicado.', 'ilumina a los barcos → ilumina'),
   R('Modificador directo', 'es un artículo o adjetivo que acompaña al núcleo sin ninguna palabra en el medio.', 'la casa, lámpara antigua'),
   R('Modificador indirecto', 'se une al núcleo mediante una preposición y su término.', 'casa de piedra'),
   R('Aposición', 'es un sustantivo que nombra lo mismo que el núcleo y suele ir entre comas.', 'Rosario, mi ciudad natal,')]}

L['3'] = {'temas': [
 T('El sujeto tácito',
   m('marcar', rotulo='Oración', items=[
     {'nombre': 'Fuimos', 'texto': 'El sábado {{fuimos|La terminación -imos indica «nosotros».}} al río y {{volvimos|Otra vez «nosotros».}} tarde.', 'cierre': 'Sujeto tácito: nosotros.'},
     {'nombre': 'Trajiste', 'texto': '¿{{Trajiste|-aste: la terminación dice «vos».}} el mate? {{Olvidaste|También vos.}} la yerba.', 'cierre': 'Sujeto tácito: vos.'}]),
   m('completar_x', consigna='¿Cuál es el sujeto tácito de cada oración?', items=[
     {'texto': '«Cantamos en el acto.» → [[nosotros/ellos/yo]]. «Llegaron temprano.» → [[ellos/nosotros/vos]].'},
     {'texto': '«Estudiás mucho.» → [[vos/yo/ella]]. «Perdí el colectivo.» → [[yo/ustedes/él]].'},
     {'texto': '«Escribirán una carta.» → [[ellos/nosotros/yo]]. «Comeremos afuera.» → [[nosotros/ellos/vos]].'}]),
   ('Sujeto tácito', 'El sujeto tácito es el que no aparece escrito en la oración, pero se reconoce por la terminación del verbo.'),
   'En español se puede omitir el sujeto porque el verbo ya lo dice: «fuimos» solo puede ser «nosotros». La oración sigue siendo bimembre, porque tiene sujeto aunque no se vea. Al analizarla, se escribe el sujeto tácito entre paréntesis.',
   ['La desinencia del verbo indica la persona.', 'La oración tácita sigue siendo bimembre.', 'Se anota así: S. T. (nosotros).']),
 T('Oraciones unimembres',
   m('esquema', items=[{'nombre': 'Unimembres', 'cols': ['Tipo', 'Ejemplo', 'Por qué no tiene sujeto'], 'filas': [
       ['Fenómenos del clima', 'Llovió toda la tarde.', 'nadie realiza la acción'], ['Con «hay» y «hace»', 'Hay tres pájaros. Hace calor.', 'el verbo no tiene quién lo haga'],
       ['Sin verbo', '¡Qué susto! Prohibido estacionar.', 'no se puede preguntar ¿quién?']], 'cierre': 'Si no se puede dividir en sujeto y predicado, es unimembre.'}]),
   m('clasificar_x', consigna='¿Bimembre o unimembre?', cajas=['Bimembre', 'Unimembre'], cuantos=6, items=[
     ['Mi tía cocina muy bien.', 0], ['Llegamos tarde al cine.', 0], ['Los árboles perdieron sus hojas.', 0],
     ['Nieva en la cordillera.', 1], ['Hay muchas nubes.', 1], ['¡Qué lindo día!', 1], ['Hace frío.', 1], ['Silencio, por favor.', 1]]),
   ('Oración unimembre', 'La oración unimembre es la que no se puede dividir en sujeto y predicado, porque no hay nadie que realice la acción o porque no tiene verbo.'),
   'El caso que más confunde es «hay»: en «hay muchas nubes» parece que «muchas nubes» es el sujeto, pero no lo es. La prueba está en la concordancia: decimos «hay una nube» y «hay muchas nubes», con el verbo siempre igual.',
   ['Clima: llueve, nieva, amanece.', '«Hay» y «hace» con tiempo o clima.', 'Frases sin verbo: saludos, carteles, exclamaciones.'])],
 'recuerda': [
   R('Sujeto tácito', 'no está escrito en la oración, pero se reconoce por la terminación del verbo.', 'Fuimos al río → (nosotros)'),
   R('Oración bimembre', 'se puede dividir en sujeto y predicado, aunque el sujeto sea tácito.', 'Llegamos tarde.'),
   R('Oración unimembre', 'no se puede dividir en sujeto y predicado porque nadie realiza la acción o no hay verbo.', 'Nieva en la cordillera.'),
   R('El verbo haber', 'en oraciones como «hay pan» no tiene sujeto y no cambia aunque lo que sigue sea plural.', 'Hay una nube / hay muchas nubes')]}

L['4'] = {'temas': [
 T('Analizar paso a paso',
   m('oracion', items=[
     {'partes': [['El hermano mayor de Paula, un experto en ajedrez,', 'S', 'Paso 1 y 2: el verbo es «ganó»; ¿quién ganó? Ese es el sujeto.', [['El', 'MD'], ['hermano', 'N'], ['mayor', 'MD'], ['de Paula', 'MI'], ['un experto en ajedrez', 'aposición']]], ['ganó el torneo', 'P', 'El resto es el predicado.', [['ganó', 'NV']]]], 'cierre': 'Oración bimembre, sujeto simple.'},
     {'partes': [['Las calles del centro', 'S', 'Verbo: «estaban»; ¿qué estaba? Las calles del centro.', [['Las', 'MD'], ['calles', 'N'], ['del centro', 'MI']]], ['estaban vacías', 'P', 'Predicado.', [['estaban', 'NV']]]], 'cierre': 'Oración bimembre.'}]),
   m('analizar_x', consigna='Analizá la oración completa: llevá cada etiqueta a su parte.', items=[
     {'bloques': [['La', 'MD'], ['plaza', 'N'], ['del barrio', 'MI'], ['tiene', 'NV'], ['juegos nuevos', 'P']]},
     {'bloques': [['Ana', 'N'], ['mi vecina', 'aposición'], ['toca', 'NV'], ['el piano', 'P']]},
     {'bloques': [['Los', 'MD'], ['cuadernos', 'N'], ['viejos', 'MD'], ['están', 'NV'], ['en el placard', 'P']]}]),
   ('Análisis sintáctico', 'Analizar una oración es marcar sus partes y la función de cada palabra, siguiendo siempre el mismo orden: verbo, sujeto, núcleo y modificadores.'),
   'Seguir el orden evita errores: primero el verbo, porque con él se encuentra el sujeto; después el núcleo del sujeto, y recién al final sus modificadores. Por último se dice si la oración es bimembre o unimembre.',
   ['1. Marco el verbo (NV) y pregunto ¿quién?', '2. Separo sujeto y predicado; marco el núcleo.', '3. Marco MD, MI y aposición; digo qué tipo de oración es.']),
 T('Expandir una oración',
   m('transformar', items=[
     {'nombre': 'El tren', 'antes': 'El tren llegó.', 'pasos': [{'v': 'El tren {{viejo}} llegó.', 'txt': 'Agregamos un MD: un adjetivo pegado al núcleo.'}, {'v': 'El tren viejo {{de carga}} llegó.', 'txt': 'Un MI: preposición + término.'}, {'v': 'El tren viejo de carga{{, el último del día,}} llegó.', 'txt': 'Una aposición entre comas.'}], 'cierre': 'Mismo núcleo, mucho más información.'},
     {'nombre': 'La perra', 'antes': 'La perra ladró.', 'pasos': [{'v': 'La perra {{negra}} ladró.', 'txt': 'MD.'}, {'v': 'La perra negra {{de mis vecinos}} ladró.', 'txt': 'MI.'}], 'cierre': 'Los modificadores hacen que el lector vea la escena.'}]),
   m('escribir_x', items=[
     {'cons': 'Expandí el sujeto de «El chico corrió.» agregando al menos un modificador directo y uno indirecto.', 'criterios': [{'txt': 'Al menos 6 palabras', 'min': 6}, {'txt': 'Conserva el núcleo «chico»', 're': 'chico'}, {'txt': 'Tiene un MI (de, con, sin…)', 're': ' (de|del|con|sin) '}], 'modelo': 'El chico alto del quinto piso corrió.'},
     {'cons': 'Expandí el sujeto de «La casa se vendió.» con un MD, un MI y una aposición entre comas.', 'criterios': [{'txt': 'Conserva «casa»', 're': 'casa'}, {'txt': 'Tiene un MI', 're': ' (de|del|con|sin) '}, {'txt': 'Tiene una aposición entre comas', 're': ',[^,]+,'}], 'modelo': 'La casa antigua de la esquina, la más grande del barrio, se vendió.'}]),
   ('Expandir', 'Expandir una oración es agregarle modificadores para que diga más y mejor, sin cambiar su estructura de sujeto y predicado.'),
   'Al escribir, una oración muy pelada informa poco. Los modificadores del sujeto permiten precisar cuál, cómo es y de quién, y la aposición agrega una explicación. El núcleo sigue siendo el mismo: solo crece lo que lo rodea.',
   ['MD: cómo es (alto, viejo).', 'MI: de quién o de qué (del vecino, de madera).', 'Aposición: una explicación entre comas.'])],
 'recuerda': [
   R('Orden del análisis', 'primero el verbo, después el sujeto con su núcleo y al final los modificadores.', 'ganó → ¿quién ganó? → hermano'),
   R('Clasificar la oración', 'al terminar el análisis se dice si es bimembre o unimembre.', 'Las calles estaban vacías: bimembre'),
   R('Expandir', 'es agregar modificadores al núcleo para que la oración diga más, sin cambiar su estructura.', 'El tren viejo de carga llegó.'),
   R('Modificadores juntos', 'un mismo núcleo puede tener varios MD, un MI y una aposición a la vez.', 'El hermano mayor de Paula, un experto, ganó.')]}

A = {
 '1': [
   CLA('Separá sujeto y predicado de «Los chicos del club entrenan los sábados».', ['Sujeto', 'Predicado'], [('Los chicos', 'Sujeto'), ('del club', 'Sujeto'), ('entrenan', 'Predicado'), ('los sábados', 'Predicado')], 'Preguntá al verbo: ¿quiénes entrenan?'),
   TAP('Tocá las palabras del sujeto: «Desde el balcón miraba la tormenta mi abuela».', ['Desde', 'el', 'balcón', 'miraba', 'la', 'tormenta', 'mi', 'abuela'], [6, 7], '¿Quién miraba? Mi abuela: el sujeto está al final.', 'analizar'),
   MC('Un compañero dice que en «Me gustan los helados» el sujeto es «me». ¿Qué le contestás?', ['El sujeto es «los helados», con el verbo en plural', 'Tiene razón: «me» indica quién habla', 'La oración no tiene ningún sujeto'], 'El sujeto es «los helados», con el verbo en plural', '¿Qué me gusta? Los helados: por eso «gustan» va en plural.', 'error'),
   FB('Completá con el verbo que concuerda: «El ramo de flores ___ (estar) sobre la mesa. Juan y Lía ___ (llegar) tarde».', [['está', 'estaba'], ['llegaron', 'llegan', 'llegarán']], 'El núcleo «ramo» es singular; el sujeto compuesto va en plural.')],
 '2': [
   TAP('Tocá el núcleo del sujeto: «Una nube enorme de humo cubrió la ciudad».', ['Una', 'nube', 'enorme', 'de', 'humo', 'cubrió', 'la', 'ciudad'], [1], 'Si sacás todo lo demás, «nube cubrió» sigue teniendo sentido.', 'analizar'),
   CLA('Clasificá cada parte del sujeto «El gato gris de mi abuela».', ['MD', 'N', 'MI'], [('El', 'MD'), ('gato', 'N'), ('gris', 'MD'), ('de mi abuela', 'MI')], 'El MI empieza con preposición.'),
   MC('En «Córdoba, la Docta, celebra su fundación», ¿qué es «la Docta»?', ['Una aposición: nombra lo mismo que el núcleo', 'Un modificador indirecto', 'El núcleo del predicado'], 'Una aposición: nombra lo mismo que el núcleo', 'Prueba: «La Docta celebra su fundación» dice lo mismo.', 'analizar'),
   MC('Martina marcó «de madera» como MD en «La mesa de madera». ¿Qué error cometió?', ['Es MI porque empieza con «de»', 'Es el núcleo del sujeto', 'No hay ningún error'], 'Es MI porque empieza con «de»', 'El MD va pegado al núcleo, sin preposición.', 'error')],
 '3': [
   UNI('Uní cada oración con su sujeto tácito.', [('Salimos temprano.', 'nosotros'), ('Compraste pan.', 'vos'), ('Viajaron en tren.', 'ellos'), ('Leí el libro.', 'yo')], 'La desinencia del verbo dice la persona.'),
   CLA('¿Bimembre o unimembre?', ['Bimembre', 'Unimembre'], [('Amaneció nublado.', 'Unimembre'), ('Hay leche en la heladera.', 'Unimembre'), ('Llegamos cansados.', 'Bimembre'), ('El viento sopla fuerte.', 'Bimembre')], 'Con sujeto tácito, sigue siendo bimembre.'),
   MC('Un alumno escribió: «Habían muchas personas en la fila». ¿Está bien?', ['No: va «había», sin plural', 'Sí: «personas» es plural', 'No: va «hubieron»'], 'No: va «había», sin plural', 'La oración es unimembre: el verbo no cambia.', 'error'),
   MC('«Escribimos una carta a la directora.» ¿Qué clase de oración es?', ['Bimembre con sujeto tácito (nosotros)', 'Unimembre', 'Bimembre con sujeto compuesto'], 'Bimembre con sujeto tácito (nosotros)', 'El sujeto no se ve, pero está.', 'aplicar')],
 '4': [
   ORD('Ordená los pasos para analizar una oración.', ['Marcar el verbo (NV)', 'Preguntarle ¿quién? y separar el sujeto', 'Marcar el núcleo del sujeto', 'Marcar MD, MI y aposición', 'Decir si es bimembre o unimembre'], 'El verbo siempre va primero.'),
   CLA('Analizá: «Los dos perros del guardia ladraban».', ['MD', 'N', 'MI', 'NV'], [('Los', 'MD'), ('dos', 'MD'), ('perros', 'N'), ('del guardia', 'MI'), ('ladraban', 'NV')], 'Sujeto: Los dos perros del guardia; predicado: ladraban.'),
   MC('¿Cuál es la expansión correcta del sujeto de «El libro cayó»?', ['El libro viejo de mi abuelo cayó.', 'El libro cayó al piso.', 'El libro cayó muy rápido.'], 'El libro viejo de mi abuelo cayó.', 'Las otras agregan al predicado, no al sujeto.', 'analizar'),
   KW('Escribí una oración sobre un lugar que te guste cuyo sujeto tenga un MD, un MI y una aposición. Después indicá cuál es el núcleo.', 'Por ejemplo: «El río Paraná, el más ancho que conozco, …». ', [['de', 'del', 'con', 'sin'], [','], ['núcleo', 'N']], 2, 'Un sujeto bien expandido y su núcleo marcado.', 'aplicar')],
}

EX = [
 [1, TAP('Tocá las palabras del sujeto: «Por el camino de tierra venían tres caballos».', ['Por', 'el', 'camino', 'de', 'tierra', 'venían', 'tres', 'caballos'], [6, 7], '¿Qué venía? Tres caballos.', 'analizar')],
 [1, FB('Completá con el verbo que concuerda: «La lista de invitados ___ (ser) larga».', [['es', 'era']], 'El núcleo es «lista», singular.', 'aplicar')],
 [1, MC('En «Ni Lucas ni Sofía trajeron el libro», ¿cómo es el sujeto?', ['Compuesto, con dos núcleos', 'Simple, con un núcleo', 'Tácito, sin escribir'], 'Compuesto, con dos núcleos', 'Lucas y Sofía, unidos por «ni».', 'aplicar')],
 [2, CLA('Clasificá: «La vieja estación de trenes».', ['MD', 'N', 'MI'], [('La', 'MD'), ('vieja', 'MD'), ('estación', 'N'), ('de trenes', 'MI')], 'MI con preposición.')],
 [2, MC('Si en «Laura, mi profesora de inglés, viaja a Londres» sacamos «Laura», la oración dice lo mismo. ¿Qué prueba eso sobre «mi profesora de inglés»?', ['Que es una aposición del núcleo', 'Que es un modificador indirecto', 'Que es el predicado'], 'Que es una aposición del núcleo', 'Nombra a la misma persona que «Laura».', 'analizar')],
 [2, MC('Un chico dice: «En "El auto de mi papá" el núcleo es "papá"». ¿Qué le contestás?', ['El núcleo es «auto», no «papá»', 'Tiene razón: «papá» es el núcleo', 'Ese sujeto no tiene núcleo'], 'El núcleo es «auto», no «papá»', 'Lo que va después de la preposición es término del MI.', 'error')],
 [3, SA('¿Cuál es el sujeto tácito de «Terminaremos la tarea a la noche»?', ['nosotros', 'nosotras', 'nosotros/as'], 'La desinencia -emos indica nosotros.', 'aplicar')],
 [3, CLA('¿Bimembre o unimembre?', ['Bimembre', 'Unimembre'], [('Hace mucho calor.', 'Unimembre'), ('¡Feliz cumpleaños!', 'Unimembre'), ('Ganamos el partido.', 'Bimembre'), ('Mis tíos viven en Neuquén.', 'Bimembre')], 'Clima, frases sin verbo, sujeto tácito.')],
 [3, MC('¿Cuál está bien escrita?', ['Hubo muchos problemas.', 'Hubieron muchos problemas.', 'Habían muchos problemas.'], 'Hubo muchos problemas.', 'Con «haber» la oración es unimembre y el verbo queda en singular.', 'error')],
 [4, ORD('Ordená el análisis de «Mi tío, el cocinero, prepara pastas».', ['Verbo: prepara', 'Sujeto: Mi tío, el cocinero', 'Núcleo: tío', 'Modificadores: Mi (MD), el cocinero (aposición)'], 'Verbo, sujeto, núcleo y modificadores.')],
 [4, MS('En «Las hojas secas del otoño cubrían la vereda», elegí TODOS los modificadores del sujeto.', ['Las', 'secas', 'del otoño', 'cubrían', 'la vereda'], ['Las', 'secas', 'del otoño'], '«cubrían» es el NV y «la vereda» es parte del predicado.')],
 [4, MC('¿Cuál de estas oraciones tiene el sujeto más expandido?', ['La gata blanca de Inés, una siamesa, duerme.', 'La gata duerme en el sillón.', 'La gata duerme.'], 'La gata blanca de Inés, una siamesa, duerme.', 'Tiene MD, MI y aposición.', 'analizar')],
 [4, KW('Analizá por escrito «El pueblo de mis abuelos tiene una plaza grande»: decí cuál es el sujeto, su núcleo, sus modificadores y el núcleo verbal.', 'Usá las siglas N, MD, MI y NV.', [['pueblo'], ['tiene'], ['de mis abuelos', 'mi'], ['md', 'el']], 3, 'S: El pueblo de mis abuelos (N pueblo, MD el, MI de mis abuelos); NV: tiene.', 'aplicar')],
]

def ajustes(M):
    for k, v in A.items(): M['act'][k] = v
    for q in M['act'].get('5', []):
        q.setdefault('n', 'recordar')
        if q['p'].startswith('Relámpago. "Nieva"'): q['o'] = ['Unimembre', 'Bimembre', 'Sujeto tácito']
    M['examen'] = EX
    M['actualizar_preguntas'] = True

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-4/mision-4.json', L, ajustes=ajustes)
