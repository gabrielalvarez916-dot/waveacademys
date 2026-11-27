# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 8 · La descripción (la clase animada queda; lección, actividades y examen nuevos)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD

L = {}
L['1'] = {'temas': [
 T('Describir es elegir rasgos',
   m('versiones', rotulo='Versión', items=[
     {'nombre': 'Lista', 'texto': '{{Don Ernesto tiene dos ojos, una nariz, dos orejas, pelo, camisa y zapatos.|Enumera todo sin elegir: no se distingue de nadie.}}'},
     {'nombre': 'Selección', 'texto': '{{Don Ernesto tiene las cejas tan espesas que parecen dos techos sobre los ojos|Un rasgo único que lo hace reconocible.}}, y {{siempre lleva un lápiz detrás de la oreja|Un detalle que dice algo de él.}}.'}]),
   m('elegir_x', consigna='¿Qué rasgo describe mejor a cada persona, para que el lector la reconozca?', items=[
     {'cons': 'Querés describir a la bibliotecaria del barrio.', 'ops': ['Lleva los anteojos colgados de una cadenita y habla en susurros', 'Tiene dos brazos y dos piernas', 'Es una persona'], 'ayuda': 'Buscá lo que la distingue de los demás.'},
     {'cons': 'Querés describir a tu entrenador de fútbol.', 'ops': ['Tiene la voz ronca de tanto gritar indicaciones', 'Tiene pelo en la cabeza', 'Usa ropa'], 'ayuda': 'Un rasgo propio vale más que uno que tiene todo el mundo.'},
     {'cons': 'Querés describir a una vecina muy vieja.', 'ops': ['Tiene las manos llenas de arrugas y siempre huelen a jabón', 'Es una señora', 'Vive en una casa'], 'ayuda': 'Elegí un detalle concreto y sensorial.'}]),
   ('Descripción', 'La descripción es el texto o el fragmento que muestra cómo es una persona, un lugar o un objeto, eligiendo los rasgos que mejor lo distinguen.'),
   'Describir no es hacer un inventario: si se nombra todo, nada se destaca. Quien describe selecciona pocos rasgos, los más llamativos o significativos, para que el lector pueda imaginar a esa persona y no a cualquier otra.',
   ['Se eligen rasgos, no se enumera todo.', 'Mejor lo propio que lo que tienen todos.', 'El objetivo: que el lector pueda imaginar.']),
 T('Retrato físico y retrato psicológico',
   m('marcar', rotulo='Retrato', items=[
     {'nombre': 'La abuela', 'texto': 'Mi abuela es {{bajita, de pelo blanco recogido en un rodete|Físico: cómo se ve.}} y {{ojos chiquitos detrás de unos anteojos enormes|Físico.}}. {{Es paciente con todos|Psicológico: su forma de ser.}}, pero {{se enoja si alguien llega tarde a la mesa|Psicológico: un rasgo de carácter.}}.', 'cierre': 'Por fuera y por dentro: un retrato completo.'},
     {'nombre': 'El vecino', 'texto': 'El vecino del quinto es {{altísimo y flaco, con la espalda un poco encorvada|Físico.}}. {{Es tímido: saluda bajando la vista|Psicológico, mostrado con un gesto.}} y {{generoso: les arregla la bici a todos los chicos del edificio|Psicológico, mostrado con una acción.}}.', 'cierre': 'El carácter se muestra mejor con acciones.'}]),
   m('clasificar_x', consigna='¿Rasgo físico o psicológico?', cajas=['Físico', 'Psicológico'], cuantos=6, items=[
     ['Tiene una cicatriz en la ceja izquierda', 0], ['Usa el pelo rapado', 0], ['Camina arrastrando los pies', 0], ['Tiene las uñas pintadas de verde', 0],
     ['Nunca pierde la calma', 1], ['Es desconfiada con los desconocidos', 1], ['Le encanta hacer reír a los demás', 1], ['Es muy orgulloso', 1]]),
   ('Retrato', 'El retrato es la descripción de una persona; puede ser físico, cuando muestra cómo se ve, o psicológico, cuando muestra cómo es su carácter.'),
   'Un retrato completo suele combinar los dos: primero lo que se ve, después cómo es la persona. Conviene seguir un orden, de lo general a lo particular, para que el lector arme la imagen de a poco y no se pierda entre detalles sueltos.',
   ['Físico: cuerpo, cara, ropa, gestos.', 'Psicológico: carácter y forma de ser.', 'Orden: de lo general a lo particular.']),
 T('Mostrar en lugar de decir',
   m('versiones', rotulo='Carácter', items=[
     {'nombre': 'Decir', 'texto': '{{Tomás es muy distraído.|Nombra el rasgo: el lector tiene que creerle al narrador.}}'},
     {'nombre': 'Mostrar', 'texto': '{{Tomás salió a la calle con una zapatilla de cada color y el cepillo de dientes en el bolsillo.|Muestra el rasgo con un hecho: el lector lo descubre solo.}}'},
     {'nombre': 'Decir', 'texto': '{{Ana es valiente.|Solo nombra.}}'},
     {'nombre': 'Mostrar', 'texto': '{{Cuando el perro grande se acercó gruñendo, Ana se puso delante de su hermanito y no se movió.|Una acción concreta muestra la valentía.}}'}]),
   m('elegir_x', consigna='¿Qué rasgo de carácter muestra cada acción?', items=[
     {'cons': '«Lucía cuenta las monedas tres veces antes de pagar y nunca invita nada.»', 'ops': ['Es tacaña', 'Es generosa', 'Es distraída'], 'ayuda': 'Pensá qué dice de ella lo que hace.'},
     {'cons': '«Martín se queda después de clase a ayudar a los que no entendieron, sin que nadie se lo pida.»', 'ops': ['Es solidario', 'Es tímido', 'Es impaciente'], 'ayuda': 'Ayuda sin que se lo pidan.'},
     {'cons': '«La señora Rita revisa tres veces que la puerta esté cerrada y mira por la ventana cada vez que pasa un auto.»', 'ops': ['Es desconfiada', 'Es alegre', 'Es perezosa'], 'ayuda': 'Fijate en lo que repite.'}]),
   ('Mostrar el carácter', 'Mostrar el carácter es presentar un rasgo psicológico a través de acciones, gestos o palabras del personaje, en lugar de nombrarlo directamente.'),
   'Cuando el texto dice «es valiente», el lector tiene que creerle; cuando muestra a alguien que se planta frente a un perro furioso, el lector lo comprueba y lo recuerda. Los buenos retratos combinan pocas afirmaciones con muchas acciones que las prueban.',
   ['Decir: nombra el rasgo («es generosa»).', 'Mostrar: lo prueba con una acción.', 'Mostrar convence y se recuerda más.'])],
 'recuerda': [
   R('Descripción', 'muestra cómo es una persona, un lugar o un objeto eligiendo los rasgos que mejor lo distinguen.', 'Las cejas espesas como dos techos'),
   R('Retrato físico', 'describe cómo se ve una persona: cuerpo, cara, ropa y gestos.', 'Bajita, con el pelo blanco en un rodete'),
   R('Retrato psicológico', 'describe el carácter y la forma de ser de una persona.', 'Paciente, pero se enoja si llegan tarde'),
   R('Selección de rasgos', 'es elegir pocos rasgos propios y significativos en lugar de enumerarlo todo.', 'Un lápiz siempre detrás de la oreja'),
   R('Mostrar el carácter', 'es presentar un rasgo con acciones o gestos, en lugar de nombrarlo.', 'Se planta frente al perro: es valiente')]}

L['2'] = {'temas': [
 T('El orden espacial',
   m('marcar', rotulo='Lugar', items=[
     {'nombre': 'La cocina', 'texto': '{{Al entrar|Punto de partida: la puerta.}}, se ve una mesa de madera con un mantel a cuadros. {{A la derecha|Conector de lugar: sigue el recorrido.}}, la heladera vieja. {{Al fondo|Más lejos.}}, una ventana que da al patio, y {{sobre la ventana|Hacia arriba.}}, una planta que cuelga.', 'cierre': 'Un recorrido ordenado, como si camináramos por el lugar.'},
     {'nombre': 'La plaza', 'texto': '{{En el centro de la plaza|Punto de partida: el centro.}} hay una fuente seca. {{Alrededor|Se abre hacia afuera.}}, bancos verdes descascarados. {{Más allá|Más lejos todavía.}}, los juegos, y {{detrás de los juegos|Al final del recorrido.}}, una hilera de paraísos.', 'cierre': 'Del centro hacia afuera: otro orden posible.'}]),
   m('ordenar_x', consigna='Ordená la descripción para que siga un recorrido de afuera hacia adentro.', items=[
     {'lista': ['Desde la vereda se ve una casa de rejas negras', 'Al cruzar el portón aparece un jardín con rosales', 'Adentro, el living tiene un sillón gastado', 'En el fondo del living, una escalera sube al primer piso']},
     {'lista': ['Desde la ruta se ve el techo rojo de la escuela rural', 'Junto a la tranquera hay un mástil con la bandera', 'En el patio, dos árboles dan sombra a los bancos', 'Dentro del aula, los pupitres miran hacia el pizarrón']}]),
   ('Orden espacial', 'El orden espacial es el recorrido que sigue una descripción para presentar un lugar: de afuera hacia adentro, de cerca a lejos, de arriba hacia abajo o de izquierda a derecha.'),
   'Si los elementos aparecen mezclados, el lector no puede armar el lugar en su cabeza. Por eso se elige un punto de partida y un recorrido, y se usan conectores de lugar, como «al fondo», «a la derecha» o «sobre», que funcionan como las indicaciones de un mapa.',
   ['Un punto de partida y un recorrido.', 'Conectores: al fondo, junto a, sobre, detrás de.', 'Sin orden, el lector se pierde.']),
 T('Describir con los cinco sentidos',
   m('marcar', rotulo='Lugar', items=[
     {'nombre': 'La panadería', 'texto': 'En la panadería {{el aire huele a pan recién horneado y a canela|Olfato.}}. {{Las medialunas brillan en la vidriera|Vista.}}, {{se escucha el chirrido de la puerta del horno|Oído.}} y {{el mostrador está tibio al tacto|Tacto.}}.', 'cierre': 'Cuatro sentidos: el lector casi está ahí.'},
     {'nombre': 'La playa', 'texto': '{{El sol rebota en la arena blanca|Vista.}}, {{las olas rompen con un rugido parejo|Oído.}}, {{la brisa trae olor a sal|Olfato.}} y {{en los labios queda un gusto salado|Gusto.}}.', 'cierre': 'Hasta el gusto puede aparecer.'}]),
   m('clasificar_x', consigna='¿Con qué sentido se percibe cada detalle?', cajas=['Vista', 'Oído', 'Olfato', 'Tacto'], cuantos=6, items=[
     ['Una pared pintada de amarillo', 0], ['La luz que entra por las persianas', 0], ['El tic tac de un reloj de pared', 1], ['Perros que ladran a lo lejos', 1],
     ['Olor a humedad en el sótano', 2], ['Perfume de jazmines en el patio', 2], ['La baranda helada de la escalera', 3], ['Una alfombra suave bajo los pies', 3]]),
   ('Descripción sensorial', 'La descripción sensorial presenta un lugar a través de lo que se percibe con varios sentidos: vista, oído, olfato, tacto y gusto.'),
   'La vista es el sentido que más usamos, pero los olores, los sonidos y las texturas hacen que el lector sienta que está en el lugar. Un buen detalle sensorial, como el olor a pan o el frío de una baranda, vale más que muchas líneas sobre colores y tamaños.',
   ['No te quedes solo con la vista.', 'Olores y sonidos dan vida al lugar.', 'Un detalle exacto vale más que muchos generales.']),
 T('La atmósfera',
   m('versiones', rotulo='Atmósfera', items=[
     {'nombre': 'Acogedora', 'texto': 'La casa {{olía a torta en el horno|Olor agradable.}}; {{la luz amarilla de la lámpara caía sobre el sillón|Luz cálida.}} y {{se oía a alguien tararear en la cocina|Sonido familiar.}}.'},
     {'nombre': 'Inquietante', 'texto': 'La casa {{olía a encierro|Olor desagradable.}}; {{una sola lamparita parpadeaba al final del pasillo|Luz débil y cambiante.}} y {{algo crujía en el piso de arriba|Sonido sin explicación.}}.'}]),
   m('elegir_x', consigna='¿Qué atmósfera crea cada descripción?', items=[
     {'cons': '«Las nubes negras tapaban la luna; el viento hacía golpear una persiana suelta y nadie contestaba en la casa.»', 'ops': ['Inquietante', 'Alegre', 'Tranquila'], 'ayuda': 'Oscuridad, ruidos y silencio.'},
     {'cons': '«Los chicos corrían entre los puestos de la feria, sonaba una cumbia y olía a garrapiñada.»', 'ops': ['Festiva', 'Triste', 'Amenazante'], 'ayuda': 'Movimiento, música y olores dulces.'},
     {'cons': '«El lago estaba quieto como un espejo; solo se oía, a lo lejos, el canto de un zorzal.»', 'ops': ['Serena', 'Caótica', 'Peligrosa'], 'ayuda': 'Quietud y un solo sonido suave.'}]),
   ('Atmósfera', 'La atmósfera es la sensación general que transmite un lugar descripto, como calma, alegría o miedo, y se construye con la elección de los detalles.'),
   'Un mismo lugar puede parecer acogedor o amenazante según qué detalles se elijan: la luz, los sonidos, los olores y el clima. Cuando leas una descripción, preguntate qué sensación te deja; cuando escribas, elegí todos los detalles en la misma dirección.',
   ['La atmósfera es la sensación del lugar.', 'Se arma con luz, sonidos, olores y clima.', 'Todos los detalles apuntan a la misma sensación.'])],
 'recuerda': [
   R('Orden espacial', 'es el recorrido que sigue la descripción de un lugar: de afuera hacia adentro, de cerca a lejos o de arriba hacia abajo.', 'Al entrar… a la derecha… al fondo'),
   R('Conectores de lugar', 'son palabras que ubican los elementos y guían al lector por el recorrido.', 'junto a, sobre, detrás de, al fondo'),
   R('Descripción sensorial', 'usa varios sentidos, no solo la vista, para que el lector sienta el lugar.', 'Olor a canela y el chirrido del horno'),
   R('Atmósfera', 'es la sensación general que transmite un lugar, construida con los detalles elegidos.', 'Una lamparita que parpadea: inquietante')]}

L['3'] = {'temas': [
 T('Adjetivos precisos',
   m('transformar', items=[
     {'nombre': 'La casa', 'antes': 'Era una casa linda.', 'pasos': [{'v': 'Era una casa {{luminosa}}.', 'txt': '«Linda» no dice cómo es; «luminosa» sí.'}, {'v': 'Era una casa luminosa, {{con ventanales que daban al río}}.', 'txt': 'Un detalle concreto completa la imagen.'}], 'cierre': 'Del adjetivo vago al preciso.'},
     {'nombre': 'La comida', 'antes': 'La sopa estaba rica.', 'pasos': [{'v': 'La sopa estaba {{espesa y humeante}}.', 'txt': 'Dos adjetivos exactos reemplazan uno vago.'}, {'v': 'La sopa estaba espesa y humeante, {{con olor a zapallo}}.', 'txt': 'Se suma un sentido.'}], 'cierre': 'El lector ya puede imaginarla.'}]),
   m('elegir_x', consigna='¿Qué adjetivo da una imagen más precisa?', items=[
     {'cons': 'Un perro ___ dormía en el umbral.', 'ops': ['sarnoso', 'feo', 'normal'], 'ayuda': 'Buscá el que te permite verlo.'},
     {'cons': 'Llegamos a un pueblo ___ y silencioso.', 'ops': ['polvoriento', 'lindo', 'bueno'], 'ayuda': 'Uno vago y uno exacto: elegí el exacto.'},
     {'cons': 'La abuela tenía las manos ___.', 'ops': ['arrugadas', 'raras', 'normales'], 'ayuda': 'Un rasgo que se puede ver.'}]),
   ('Adjetivo preciso', 'Un adjetivo preciso es el que muestra un rasgo concreto que el lector puede imaginar, a diferencia de los vagos, como lindo, feo, bueno o raro.'),
   'Los adjetivos vagos dicen la opinión de quien escribe, pero no cómo es la cosa: «linda» puede significar mil cosas. Los precisos, como luminosa, polvoriento o arrugadas, muestran. Además, conviene usar pocos: uno exacto vale más que tres parecidos.',
   ['Evitá: lindo, feo, bueno, raro, normal.', 'Preferí rasgos que se vean, se oigan o se toquen.', 'Pocos y exactos, no muchos y parecidos.']),
 T('Comparación y metáfora',
   m('recursos', items=[
     {'recurso': 'Comparación', 'frase': 'Sus ojos brillaban como dos faroles', 'a': 'los ojos', 'b': 'los faroles', 'rasgo': 'brillan en la oscuridad', 'literal': 'Sus ojos brillaban mucho', 'porque': 'Une las dos cosas con «como»: es una comparación.'},
     {'recurso': 'Metáfora', 'frase': 'Sus ojos eran dos faroles en la noche', 'a': 'los ojos', 'b': 'los faroles', 'rasgo': 'brillan en la oscuridad', 'literal': 'Sus ojos brillaban mucho', 'porque': 'Dice que una cosa ES la otra, sin «como»: es una metáfora.'},
     {'recurso': 'Comparación', 'frase': 'El lago estaba quieto como un espejo', 'a': 'el lago', 'b': 'un espejo', 'rasgo': 'superficie lisa que refleja', 'literal': 'El lago estaba muy quieto', 'porque': 'Usa «como»: comparación.'}]),
   m('clasificar_x', consigna='¿Comparación o metáfora?', cajas=['Comparación', 'Metáfora'], cuantos=6, items=[
     ['Su voz era suave como el terciopelo', 0], ['Corría como un rayo', 0], ['El pan estaba duro como una piedra', 0],
     ['Su voz era terciopelo', 1], ['El estadio era un hervidero', 1], ['La luna, un plato de plata sobre el techo', 1]]),
   ('Comparación y metáfora', 'La comparación relaciona dos cosas por un rasgo común usando «como» u otro nexo; la metáfora las identifica directamente, diciendo que una es la otra.'),
   'Las dos sirven para describir de manera más viva: en lugar de decir que el lago estaba muy quieto, se lo relaciona con un espejo y el lector lo ve. Para entenderlas hay que encontrar el rasgo compartido: los ojos y los faroles tienen en común que brillan en la oscuridad.',
   ['Comparación: con «como» (o «parecía»).', 'Metáfora: sin nexo, «es» la otra cosa.', 'Clave: el rasgo que comparten.']),
 T('La personificación',
   m('recursos', items=[
     {'recurso': 'Personificación', 'frase': 'El viento aullaba entre los árboles', 'a': 'el viento', 'b': 'un ser que aúlla', 'rasgo': 'un sonido fuerte y lastimero', 'literal': 'El viento soplaba fuerte y hacía ruido', 'porque': 'Le da al viento una acción de un ser vivo.'},
     {'recurso': 'Personificación', 'frase': 'La casa vieja nos miraba con sus ventanas rotas', 'a': 'la casa', 'b': 'alguien que mira', 'rasgo': 'parece vigilar', 'literal': 'La casa tenía las ventanas rotas', 'porque': 'Atribuye a un objeto la capacidad de mirar.'}]),
   m('elegir_x', consigna='¿Qué efecto produce cada personificación?', items=[
     {'cons': '«Los árboles se abrazaban sobre el camino.»', 'ops': ['Las ramas se juntan y forman un techo', 'Los árboles se mueven de lugar', 'Hay gente abrazada en el camino'], 'ayuda': 'Pensá cómo se ven los árboles.'},
     {'cons': '«La ciudad dormía bajo la nieve.»', 'ops': ['Todo estaba quieto y en silencio', 'La gente se había ido de vacaciones', 'Había mucho ruido'], 'ayuda': '¿Cómo está algo que duerme?'},
     {'cons': '«El reloj se burlaba de mi apuro.»', 'ops': ['El tiempo parecía pasar lento a propósito', 'El reloj estaba roto', 'El reloj se reía de verdad'], 'ayuda': 'Es una impresión de quien espera.'}]),
   ('Personificación', 'La personificación es el recurso que atribuye a objetos, animales o fenómenos naturales acciones o sentimientos propios de las personas.'),
   'Es muy usada en la descripción de lugares porque les da vida y ayuda a crear la atmósfera: una casa que «mira» con sus ventanas rotas resulta inquietante, y una ciudad que «duerme» transmite calma. Como los demás recursos, no se lee al pie de la letra.',
   ['Da a las cosas acciones humanas.', 'Ayuda a crear la atmósfera.', 'No se lee al pie de la letra.'])],
 'recuerda': [
   R('Adjetivo preciso', 'muestra un rasgo concreto que el lector puede imaginar, a diferencia de los vagos.', 'luminosa en lugar de linda'),
   R('Adjetivo vago', 'expresa una opinión sin mostrar cómo es la cosa, como lindo, feo, bueno o raro.', 'Era una casa linda'),
   R('Comparación', 'relaciona dos cosas por un rasgo común usando «como» u otro nexo.', 'Quieto como un espejo'),
   R('Metáfora', 'identifica una cosa con otra sin nexo, diciendo que una es la otra.', 'Sus ojos eran dos faroles'),
   R('Personificación', 'atribuye a objetos, animales o fenómenos naturales acciones o sentimientos propios de las personas.', 'El viento aullaba entre los árboles')]}

L['4'] = {'temas': [
 T('Qué falla en una descripción',
   m('revision', items=[
     {'nombre': 'Mi barrio', 'borrador': 'Mi barrio es lindo. Hay casas lindas y una plaza linda. También hay árboles y gente. Es un lugar bueno.', 'criterios': [['Tiene rasgos concretos', False, 'lindo, bueno: todo vago'], ['Sigue un orden', False, 'salta de las casas a la gente'], ['Usa más de un sentido', False, 'solo dice lo que hay'], ['Transmite una atmósfera', False, 'no se siente nada']],
      'final': 'Mi barrio es tranquilo. Desde la esquina se ven casas bajas con rejas verdes; al fondo, la plaza, con sus tilos que perfuman todo en noviembre y los chicos que gritan en la hamaca.'},
     {'nombre': 'Mi tía', 'borrador': 'Mi tía es buena. Tiene pelo y ojos. Es muy buena con todos y es buena persona.', 'criterios': [['Tiene rasgos concretos', False, 'pelo y ojos tiene todo el mundo'], ['Muestra el carácter con acciones', False, 'solo repite «buena»'], ['Evita repeticiones', False, 'buena aparece tres veces']],
      'final': 'Mi tía tiene el pelo colorado siempre atado con un lápiz. Cada domingo cocina una olla enorme de guiso por si cae alguien sin avisar.'}]),
   m('marcar_x', consigna='Tocá las palabras vagas que habría que reemplazar.', items=[
     {'cons': 'Descripción de una casa de campo.', 'texto': '[[La|0]] [[casa|0]] [[era|0]] [[linda|1]] [[y|0]] [[tenía|0]] [[un|0]] [[jardín|0]] [[bueno|1]] [[con|0]] [[cosas|1]] [[raras|1]] [[por|0]] [[todos|0]] [[lados|0]].'},
     {'cons': 'Retrato de un profesor.', 'texto': '[[El|0]] [[profesor|0]] [[era|0]] [[normal|1]], [[con|0]] [[barba|0]] [[gris|0]] [[y|0]] [[una|0]] [[voz|0]] [[rara|1]] [[que|0]] [[era|0]] [[muy|0]] [[buena|1]].'}]),
   ('Revisión de una descripción', 'Revisar una descripción es releerla con preguntas concretas para encontrar lo que falla: palabras vagas, falta de orden, repeticiones o un solo sentido.'),
   'Las descripciones pobres suelen tener los mismos problemas: adjetivos vagos que se repiten, rasgos que tiene cualquiera y ningún orden. Hacerse preguntas, como «¿el lector puede imaginarlo?» o «¿hay algo que se oiga o se huela?», permite detectarlos uno por uno.',
   ['¿Hay palabras vagas o repetidas?', '¿Sigue un orden?', '¿Usa más de un sentido? ¿Se siente algo?']),
 T('Reescribir para mejorar',
   m('transformar', items=[
     {'nombre': 'El aula', 'antes': 'El aula era fea y vieja.', 'pasos': [{'v': 'El aula tenía {{las paredes descascaradas}} y vieja.', 'txt': 'Cambiamos «fea» por un rasgo concreto.'}, {'v': 'El aula tenía las paredes descascaradas {{y un pizarrón con manchas de tiza antiguas}}.', 'txt': 'Mostramos lo viejo con un detalle.'}, {'v': 'El aula tenía las paredes descascaradas y un pizarrón con manchas de tiza antiguas; {{olía a humedad}}.', 'txt': 'Sumamos otro sentido.'}], 'cierre': 'Misma idea, mucho más clara.'}]),
   m('transformar_x', consigna='Reescribí la descripción como se pide.', items=[
     {'cons': 'Reemplazá «lindo» por rasgos concretos y agregá un olor.', 'texto': 'El parque era lindo.', 'pide': ['olor|olía|perfume|aroma'], 'prohibe': ['lindo']},
     {'cons': 'Reemplazá «buena» por una acción que muestre cómo es.', 'texto': 'Mi vecina es buena.', 'pide': [], 'prohibe': ['buena']},
     {'cons': 'Agregá un sonido y un conector de lugar a esta descripción.', 'texto': 'La estación estaba llena de gente.', 'pide': ['junto|al fondo|detrás|sobre|frente|a la derecha|a la izquierda|cerca|lejos'], 'prohibe': []}]),
   ('Reescribir', 'Reescribir una descripción es conservar lo que se quiere mostrar y mejorar la forma: cambiar lo vago por lo concreto, ordenar y sumar sentidos.'),
   'Reescribir no es copiar ni empezar de cero: la idea se mantiene y se cambian las palabras que no funcionan. Conviene ir de a un problema por vez: primero los adjetivos vagos, después el orden, al final los sentidos y la atmósfera.',
   ['Conservá la idea.', 'Cambiá lo vago por lo concreto.', 'Mejorá de a un problema por vez.']),
 T('Comparar versiones',
   m('versiones', rotulo='Versión', items=[
     {'nombre': 'Primera', 'texto': '{{El mercado era grande y tenía muchas cosas.|Vago: no se ve nada.}}'},
     {'nombre': 'Segunda', 'texto': '{{El mercado era enorme, con puestos de frutas y verduras.|Más concreto, pero solo con la vista.}}'},
     {'nombre': 'Tercera', 'texto': '{{En el mercado, los puestos de frutas formaban pasillos de colores|Vista precisa.}}; {{los vendedores gritaban ofertas|Oído.}} y {{todo olía a mandarina|Olfato.}}.'}]),
   m('elegir_x', consigna='¿Qué versión describe mejor?', items=[
     {'cons': 'Descripción de un perro.', 'ops': ['Un perro petiso y panzón, que mueve la cola en círculos cuando escucha la llave', 'Un perro lindo y bueno', 'Un perro normal con cuatro patas'], 'ayuda': 'Buscá rasgos propios y una acción.'},
     {'cons': 'Descripción de una tormenta.', 'ops': ['El cielo se puso violeta y los truenos hacían temblar los vidrios', 'Hubo una tormenta fea', 'Llovió mucho y fue raro'], 'ayuda': 'Buscá detalles que se vean y se oigan.'},
     {'cons': 'Descripción de un abuelo.', 'ops': ['Huele a tabaco dulce y silba tangos mientras arregla la radio', 'Es un abuelo bueno y viejo', 'Es una persona mayor normal'], 'ayuda': 'Sentidos y acciones.'}]),
   ('Comparar versiones', 'Comparar versiones de una descripción permite ver qué cambios la mejoran: rasgos concretos, más sentidos, orden y acciones que muestran.'),
   'Al poner una al lado de la otra, se nota que la mejor versión no es la más larga, sino la que tiene detalles mejor elegidos. Esta comparación también sirve para revisar tus propios textos: leé tu primera versión y preguntate qué le faltaría para parecerse a la mejor.',
   ['La mejor no es la más larga.', 'Gana la que tiene detalles mejor elegidos.', 'Usá la comparación para revisar lo tuyo.'])],
 'recuerda': [
   R('Revisar una descripción', 'es releerla con preguntas concretas para detectar palabras vagas, falta de orden o un solo sentido.', '¿El lector puede imaginarlo?'),
   R('Palabras vagas', 'son las que expresan una opinión sin mostrar cómo es algo y suelen repetirse.', 'lindo, bueno, normal, raro'),
   R('Reescribir', 'es conservar la idea y mejorar la forma, cambiando lo vago por lo concreto.', 'Fea → paredes descascaradas'),
   R('Mejor versión', 'es la que tiene los detalles mejor elegidos, no necesariamente la más larga.', 'Pasillos de colores y olor a mandarina')]}

A = {
 '1': [
   CLA('¿Rasgo físico o psicológico?', ['Físico', 'Psicológico'], [('Tiene las orejas grandes y despegadas', 'Físico'), ('Es muy terca', 'Psicológico'), ('Usa una campera de cuero gastada', 'Físico'), ('Se pone nerviosa antes de hablar en público', 'Psicológico')], 'Lo que se ve o la forma de ser.', 'aplicar'),
   UNI('Uní cada acción con el rasgo de carácter que muestra.', [('Comparte su merienda con quien no trajo', 'generoso'), ('Revisa tres veces que la puerta esté cerrada', 'desconfiado'), ('Se ríe de sus propios errores', 'de buen humor'), ('Interrumpe a todos para hablar', 'impaciente')], 'Las acciones muestran el carácter.', 'analizar'),
   ODD('Tres rasgos sirven para reconocer a alguien y uno no. ¿Cuál no sirve?', ['Tiene una nariz', 'Siempre lleva una boina roja', 'Tiene una cicatriz en el mentón', 'Habla con acento cordobés'], 'Tiene una nariz', 'Es un rasgo que tiene todo el mundo.', 'analizar'),
   MC('Un compañero describe a su abuela así: «Es buena, buena y muy buena». ¿Qué le recomendás?', ['Mostrar su bondad con una acción concreta', 'Agregar más veces la palabra «buena»', 'Describir solo su ropa'], 'Mostrar su bondad con una acción concreta', 'Mostrar convence más que repetir el adjetivo.', 'error')],
 '2': [
   CLA('¿Con qué sentido se percibe?', ['Vista', 'Oído', 'Olfato', 'Tacto'], [('El brillo del sol en la ventana', 'Vista'), ('El zumbido de las moscas', 'Oído'), ('El olor a tierra mojada', 'Olfato'), ('La arena caliente bajo los pies', 'Tacto')], 'Pensá cómo te enterás de cada detalle.', 'aplicar'),
   ORD('Ordená la descripción de arriba hacia abajo.', ['El techo de chapa estaba oxidado', 'De las paredes colgaban fotos viejas', 'Sobre la mesa había un mantel bordado', 'El piso de madera crujía a cada paso'], 'Un recorrido vertical.', 'aplicar'),
   MC('«El pasillo estaba oscuro, olía a encierro y una puerta golpeaba sola.» ¿Qué atmósfera crea?', ['Inquietante', 'Festiva', 'Tranquila'], 'Inquietante', 'Oscuridad, mal olor y un ruido sin explicación.', 'analizar'),
   TAP('Tocá los DOS conectores de lugar: «Junto a la puerta había un paragüero y, al fondo del pasillo, una ventana con rejas.»', ['Junto a', 'la puerta', 'había un paragüero', 'y,', 'al fondo', 'del pasillo,', 'una ventana con rejas.'], [0, 4], 'Los conectores de lugar ubican los elementos.', 'analizar')],
 '3': [
   CLA('¿Comparación, metáfora o personificación?', ['Comparación', 'Metáfora', 'Personificación'], [('Dormía como un tronco', 'Comparación'), ('Su risa era una cascada', 'Metáfora'), ('El sol se escondió avergonzado', 'Personificación'), ('Frío como el hielo', 'Comparación')], 'Con como, sin como o acciones humanas.', 'aplicar'),
   UNI('Uní cada adjetivo vago con un reemplazo preciso.', [('una casa linda', 'una casa luminosa'), ('un perro feo', 'un perro sarnoso'), ('una comida rica', 'una comida picante'), ('un día raro', 'un día nublado y ventoso')], 'Lo preciso muestra cómo es.', 'aplicar'),
   MC('En «Sus ojos eran dos faroles», ¿qué rasgo comparten los ojos y los faroles?', ['Brillan en la oscuridad', 'Son redondos y de vidrio', 'Están en la calle'], 'Brillan en la oscuridad', 'La metáfora se apoya en un rasgo común.', 'analizar'),
   MC('Mica dice que «El viento silbaba» es una comparación. ¿Qué recurso es en realidad?', ['Personificación: el viento hace algo humano', 'Comparación: usa «como»', 'Metáfora: dice que el viento es otra cosa'], 'Personificación: el viento hace algo humano', 'No hay «como»: se le atribuye una acción humana.', 'error')],
 '4': [
   TAP('Tocá las TRES palabras vagas: «El patio era lindo, con plantas raras y un banco bueno.»', ['El patio', 'era', 'lindo,', 'con plantas', 'raras', 'y un banco', 'bueno.'], [2, 4, 6], 'Lindo, raras y bueno no muestran nada.', 'error'),
   ORD('Ordená las versiones de la peor a la mejor.', ['La escuela era linda.', 'La escuela era grande y antigua.', 'La escuela era antigua, con escaleras de mármol gastadas.', 'La escuela era antigua: escaleras de mármol gastadas y un eco que repetía cada paso.'], 'Cada versión suma algo concreto.', 'analizar'),
   MC('¿Qué cambio mejora más la oración «La plaza era bonita»?', ['«En la plaza, los jacarandás cubrían de violeta los bancos»', '«La plaza era muy pero muy bonita»', '«La plaza era bonita y linda»'], '«En la plaza, los jacarandás cubrían de violeta los bancos»', 'Cambia lo vago por un detalle concreto.', 'aplicar'),
   KW('Reescribí la descripción «La cocina era linda» con al menos un rasgo concreto y un sentido que no sea la vista.', 'Cambiá «linda» y sumá un olor, un sonido o una textura.', [['olía', 'olor', 'perfume', 'aroma', 'sonaba', 'ruido', 'se oía', 'tibi*', 'frío', 'suave', 'áspero', 'calor'], ['mesa', 'azulejo*', 'ventana', 'horno', 'olla*', 'pared*', 'mantel', 'heladera', 'cocina']], 2, 'Por ejemplo: «La cocina tenía azulejos verdes y olía a pan recién horneado».', 'aplicar')],
 '5': [
   CLA('¿Qué recurso de la descripción aparece?', ['Retrato psicológico', 'Descripción sensorial', 'Orden espacial', 'Metáfora'], [('Es paciente, pero no soporta las mentiras', 'Retrato psicológico'), ('Olía a café y se oía la radio', 'Descripción sensorial'), ('Al entrar, la mesa; al fondo, la ventana', 'Orden espacial'), ('La luna era una moneda de plata', 'Metáfora')], 'Repasá lo aprendido en la misión.', 'analizar'),
   MC('¿Cuál es el mejor retrato?', ['«Tiene la voz ronca y se ríe tapándose la boca»', '«Es una persona normal y simpática»', '«Tiene ojos, pelo y una boca»'], '«Tiene la voz ronca y se ríe tapándose la boca»', 'Rasgos propios y un gesto que muestra.', 'aplicar'),
   UNI('Uní cada descripción con la atmósfera que crea.', [('Una lamparita que parpadea y pasos en el techo', 'inquietante'), ('Música, risas y olor a pochoclo', 'festiva'), ('Un lago quieto y el canto lejano de un pájaro', 'serena'), ('Bocinas, gritos y gente que corre', 'caótica')], 'Los detalles construyen la sensación.', 'analizar'),
   ORD('Ordená los pasos para mejorar una descripción.', ['Releerla con preguntas', 'Marcar las palabras vagas', 'Reemplazarlas por rasgos concretos', 'Sumar otro sentido y revisar el orden'], 'Revisar, detectar, reemplazar, completar.', 'aplicar')],
}

EX = [
 [1, CLA('¿Rasgo físico o psicológico?', ['Físico', 'Psicológico'], [('Tiene pecas en toda la cara', 'Físico'), ('Es muy desconfiado', 'Psicológico'), ('Camina con bastón', 'Físico'), ('Le cuesta pedir perdón', 'Psicológico')], 'Lo que se ve o la forma de ser.', 'aplicar')],
 [1, MC('¿Qué oración MUESTRA que alguien es generoso, en lugar de decirlo?', ['Le regaló su campera nueva a un compañero con frío', 'Es una persona muy generosa', 'Todos dicen que es generoso'], 'Le regaló su campera nueva a un compañero con frío', 'Una acción concreta prueba el rasgo.', 'analizar')],
 [1, TF('Describir bien es nombrar todos los rasgos de una persona, sin dejar ninguno.', 'Falso', 'Describir es elegir los rasgos que la distinguen.', 'recordar')],
 [2, ORD('Ordená la descripción de afuera hacia adentro.', ['Desde la calle se ve un portón de hierro', 'Detrás del portón, un jardín con limoneros', 'Al entrar, un hall con piso de baldosas', 'Al fondo del hall, la escalera'], 'Un recorrido para no perder al lector.', 'aplicar')],
 [2, CLA('¿Con qué sentido se percibe?', ['Vista', 'Oído', 'Olfato'], [('Paredes amarillas', 'Vista'), ('Un perro que ladra', 'Oído'), ('Olor a lavandina', 'Olfato')], 'Cómo te enterás de cada detalle.', 'aplicar')],
 [2, MC('«Las persianas golpeaban con el viento y en la casa vacía nadie respondía.» ¿Qué atmósfera crea?', ['Inquietante', 'Alegre', 'Festiva'], 'Inquietante', 'Ruidos sin explicación y una casa vacía.', 'analizar')],
 [3, CLA('¿Comparación, metáfora o personificación?', ['Comparación', 'Metáfora', 'Personificación'], [('Blanco como la nieve', 'Comparación'), ('El río era una serpiente de plata', 'Metáfora'), ('Las olas besaban la orilla', 'Personificación')], 'Con como, sin como, o acciones humanas.', 'aplicar')],
 [3, SA('Reemplazá el adjetivo vago por uno preciso: «Un día ___ (en lugar de feo), con nubes negras y viento».', ['tormentoso', 'nublado', 'gris', 'oscuro', 'lluvioso', 'ventoso', 'frío', 'helado', 'sombrío'], 'Un adjetivo que muestre cómo era el día.', 'aplicar')],
 [3, MC('¿Por qué «Sus manos eran dos ramas secas» es una metáfora?', ['Porque dice que las manos son ramas, sin usar «como»', 'Porque usa «como» para comparar', 'Porque las manos hablan como personas'], 'Porque dice que las manos son ramas, sin usar «como»', 'La metáfora identifica una cosa con otra.', 'analizar')],
 [4, TAP('Tocá las DOS palabras vagas: «El cuarto era lindo y tenía cosas en la pared.»', ['El cuarto', 'era', 'lindo', 'y tenía', 'cosas', 'en la pared.'], [2, 4], 'Lindo y cosas no muestran nada concreto.', 'error')],
 [4, ORD('Ordená los pasos para revisar una descripción.', ['Releer con preguntas', 'Marcar lo vago', 'Reemplazar por lo concreto', 'Sumar sentidos y revisar el orden'], 'Un paso por vez.', 'recordar')],
 [4, MC('Entre dos versiones de una descripción, ¿cuál es mejor?', ['La que tiene detalles mejor elegidos', 'La más larga', 'La que repite más adjetivos'], 'La que tiene detalles mejor elegidos', 'No gana la más larga, sino la más precisa.', 'analizar')],
 [4, KW('Describí en dos oraciones un lugar que conozcas: usá un conector de lugar y al menos dos sentidos.', 'Ubicá los elementos y sumá olores, sonidos o texturas.', [['junto a', 'al fondo', 'detrás', 'sobre', 'frente', 'a la derecha', 'a la izquierda', 'cerca', 'lejos', 'arriba', 'abajo', 'al entrar'], ['olía', 'olor', 'perfume', 'aroma', 'sonaba', 'ruido', 'se oía', 'se escuchaba', 'frío', 'tibi*', 'suave', 'áspero', 'calor', 'gusto']], 2, 'Por ejemplo: «Al entrar al club, se oye el rebote de las pelotas. Junto a la cancha, el buffet huele a café».', 'aplicar')],
]

def ajustes(M):
    M['act'] = A
    M['examen'] = EX
    M['practica'] = 'Actividades generales'
    M['actualizar_preguntas'] = True

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-8/mision-8.json', L, ajustes=ajustes)
