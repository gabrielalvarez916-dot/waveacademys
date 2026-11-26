# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misiones 1 y 2: lección interactiva (escrita en sesión), 4 actividades por nivel y examen.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from armar import *

def MC(p, o, c, e, n='aplicar'): return {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": c}, "e": e, "n": n}
def TF(p, c, e, n='recordar'): return {"t": "true_false", "p": p, "o": ["Verdadero", "Falso"], "r": {"correcta": c}, "e": e, "n": n}
def ORD(p, orden, e, n='aplicar'): return {"t": "ordering", "p": p, "o": orden[1:] + orden[:1] if len(orden) > 2 else orden[::-1], "r": {"orden": orden}, "e": e, "n": n}
def UNI(p, pares, e, n='aplicar'): return {"t": "matching", "p": p, "o": {"izquierda": [a for a, b in pares], "derecha": [b for a, b in pares][::-1]}, "r": {"pares": dict(pares)}, "e": e, "n": n}
def CLA(p, cats, el, e, n='aplicar'): return {"t": "classify", "p": p, "o": {"elementos": [a for a, b in el], "categorias": cats}, "r": {"categorias": dict(el)}, "e": e, "n": n}
def TAP(p, seg, tocar, e, n='analizar'): return {"t": "tap_text", "p": p, "o": {"segmentos": seg, "modo": "palabras"}, "r": {"tocar": tocar}, "e": e, "n": n}
def MS(p, o, cs, e, n='analizar'): return {"t": "multi_select", "p": p, "o": o, "r": {"correctas": cs}, "e": e, "n": n}
def SA(p, acepta, e, n='aplicar'): return {"t": "short_answer", "p": p, "r": {"acepta": acepta}, "e": e, "n": n}
def KW(p, ayuda, grupos, minimo, e, n='aplicar'): return {"t": "keywords", "p": p, "o": {"ayuda": ayuda}, "r": {"grupos": grupos, "minimo": minimo}, "e": e, "n": n}
def FB(p, huecos, e, n='aplicar'): return {"t": "fill_blank", "p": p, "r": {"huecos": huecos}, "e": e, "n": n}
def ODD(p, o, c, e, n='analizar'): return {"t": "odd_one_out", "p": p, "o": o, "r": {"correcta": c}, "e": e, "n": n}

# =====================================================================================================
# MISIÓN 1 · Punto de partida: leer, reconocer géneros, escribir y elegir libros
# =====================================================================================================
L1 = {}
L1['1'] = {'temas': [
 T('Antes de leer: el paratexto',
   m('marcar', rotulo='Libro', items=[
     {'nombre': 'Contratapa 1', 'texto': '{{Los que nadan de noche|El título promete algo misterioso que pasa en el agua.}} · Novela juvenil. Cuando el río crece, {{Mateo ve luces en el muelle abandonado del pueblo|La contratapa adelanta el conflicto: algo raro rompe la calma.}}. {{¿Quién se mete en el agua a medianoche, y para qué?|Termina con una pregunta: invita a leer sin contar el final.}}', 'cierre': 'Hipótesis: un misterio en un pueblo junto al río.'},
     {'nombre': 'Contratapa 2', 'texto': '{{El último vagón|El título hace pensar en un tren y en algo que queda atrás.}} · Cuentos. {{Siete historias que ocurren en trenes nocturnos|Anticipa que es un libro de varios relatos breves.}}, donde {{nadie es quien dice ser|Sugiere engaños y personajes con secretos.}}.', 'cierre': 'Hipótesis: cuentos de suspenso con personajes que mienten.'}]),
   m('elegir_x', consigna='Mirá el paratexto y elegí la hipótesis más razonable.', items=[
     {'cons': 'Tapa: una chica con linterna frente a una puerta entreabierta. Título: «Lo que guarda el altillo».', 'ops': ['Un relato de misterio dentro de una casa', 'Un manual para ordenar la casa', 'Una noticia sobre mudanzas'], 'ayuda': 'La linterna, la puerta entreabierta y el altillo sugieren algo oculto.'},
     {'cons': 'Contratapa: «Un perro callejero, una nena que se muda y un verano para hacerse amigos».', 'ops': ['Una historia de amistad entre una nena y un perro', 'Un libro sobre razas de perros', 'Una obra de teatro sobre veterinarios'], 'ayuda': 'La contratapa nombra a los personajes y lo que les pasa.'},
     {'cons': 'Índice: «1. La nave despega · 2. Rumbo a Titán · 3. La señal desconocida».', 'ops': ['Una aventura en el espacio', 'Un cuento de hadas', 'Un libro de recetas'], 'ayuda': 'Los capítulos hablan de una nave y de una luna de Saturno.'}]),
   ('Paratexto', 'El paratexto es todo lo que rodea al texto principal y lo presenta: tapa, título, autor, ilustraciones, contratapa e índice.'),
   'Mirarlo antes de empezar permite armar una hipótesis de lectura, es decir, una idea de qué vamos a encontrar. La hipótesis no tiene que acertar: se confirma o se corrige mientras leemos, y eso nos mantiene atentos.',
   ['El título y la imagen de tapa dan la primera pista.', 'La contratapa adelanta el conflicto sin contar el final.', 'El índice muestra cómo está organizado el libro.']),
 T('Inferir: leer lo que no está escrito',
   m('marcar', rotulo='Texto', items=[
     {'nombre': 'Sofía', 'texto': 'Sofía entró {{con el pelo chorreando|Pista 1: viene de afuera y está empapada.}} y dejó {{el paraguas dado vuelta en la entrada|Pista 2: hubo viento fuerte.}}. {{Se frotaba las manos sin parar|Pista 3: tiene frío.}}', 'cierre': 'Se infiere: afuera hay una tormenta fría y con viento.'},
     {'nombre': 'Joaquín', 'texto': 'Joaquín {{miró el reloj por quinta vez|Pista 1: espera algo o a alguien.}}, {{se acomodó la camisa planchada|Pista 2: se preparó con cuidado.}} y {{ensayó en voz baja un «hola»|Pista 3: está nervioso por un encuentro.}}', 'cierre': 'Se infiere: espera a alguien importante para él y está nervioso.'}]),
   m('elegir_x', consigna='¿Qué se puede inferir? Elegí la opción que se apoya en las pistas.', items=[
     {'cons': '«Martina abrió la heladera, suspiró y volvió a cerrarla. Después agarró la billetera y las llaves.»', 'ops': ['Va a salir a comprar comida', 'Está enojada con su hermano', 'Se va de vacaciones'], 'ayuda': 'La heladera vacía y la billetera son las pistas.'},
     {'cons': '«El abuelo dejó la pala, se secó la frente y se sentó a la sombra del nogal.»', 'ops': ['Estuvo trabajando al sol y está cansado', 'Está por llover', 'Perdió algo en el jardín'], 'ayuda': 'Secarse la frente y buscar sombra dicen mucho.'},
     {'cons': '«Cuando sonó el timbre del recreo, Tomás guardó la carta en la mochila y se puso colorado.»', 'ops': ['La carta es algo que le da vergüenza mostrar', 'La carta está en blanco', 'Tomás no sabe leer'], 'ayuda': 'Esconderla y ponerse colorado son las pistas.'}]),
   ('Inferencia', 'Inferir es sacar una conclusión que el texto no dice con todas las letras, uniendo las pistas del texto con lo que ya sabemos.'),
   'Los autores no explican todo: dejan detalles para que el lector complete el sentido. Una inferencia válida siempre se puede apoyar en una pista concreta; si no hay ninguna que la sostenga, es un invento del lector.',
   ['Fijate en gestos, objetos y reacciones de los personajes.', 'Preguntate qué explicación une todas las pistas.', 'Volvé al texto para comprobarla.']),
 T('Cómo se arma un relato',
   m('esquema', items=[
     {'nombre': 'Luna', 'raiz': 'La perra perdida', 'ramas': [['Situación inicial', ['Nico y su perra Luna viven en una chacra tranquila'], 'Presentamos personajes, lugar y cómo están.'], ['Conflicto', ['una noche Luna no vuelve y Nico la busca con una linterna'], 'Un hecho rompe la calma: empieza la historia.'], ['Desenlace', ['la encuentra en el galpón, cuidando a sus cachorros recién nacidos'], 'Se resuelve el problema y la situación cambia.']], 'cierre': 'Al final la chacra tiene tres perros más.'},
     {'nombre': 'El partido', 'raiz': 'La final del barrio', 'ramas': [['Situación inicial', ['el equipo de Abril entrena para la final'], 'Quiénes son y qué quieren.'], ['Conflicto', ['el día del partido se lesiona la arquera'], 'Algo sale mal y hay que resolverlo.'], ['Desenlace', ['Abril ataja por primera vez y empatan'], 'Cómo termina: no siempre es un final feliz completo.']], 'cierre': 'El desenlace muestra qué cambió en los personajes.'}]),
   m('ordenar_x', consigna='Ordená los momentos del relato: situación inicial, conflicto y desenlace.', items=[
     {'lista': ['Un pescador vive solo en una isla del Paraná', 'Una crecida se lleva su bote', 'Los vecinos de la costa le construyen uno nuevo']},
     {'lista': ['Ema guarda sus ahorros en una lata para comprar una bici', 'Su hermano usa la plata sin avisar', 'El hermano trabaja todo el verano y se la devuelve']},
     {'lista': ['El circo llega al pueblo y todos van a la función', 'El elefante se escapa durante el show', 'Un nene lo calma con una canción y vuelve a la carpa']}]),
   ('Estructura narrativa', 'La mayoría de los relatos se organizan en tres momentos: situación inicial, conflicto y desenlace, que muestran cómo cambia la historia.'),
   'Reconocer los tres momentos sirve para resumir una historia y para entender por qué pasa cada cosa. El conflicto es el motor del relato: sin un problema que rompa la calma, no habría nada que contar.',
   ['Situación inicial: quiénes son, dónde están y cómo viven.', 'Conflicto: un hecho rompe ese equilibrio.', 'Desenlace: el problema se resuelve, bien o mal.']),
 T('Quién cuenta: el narrador',
   m('versiones', rotulo='Versión', items=[
     {'nombre': 'Primera persona', 'texto': '{{Yo|Un personaje cuenta lo que le pasa: primera persona.}} abrí la caja y {{me temblaron las manos|Solo sabe lo que siente él.}}.'},
     {'nombre': 'Tercera persona', 'texto': '{{Lucas|Cuenta alguien de afuera: tercera persona.}} abrió la caja y {{le temblaron las manos|Ve lo que se nota desde afuera.}}.'},
     {'nombre': 'Omnisciente', 'texto': 'Lucas abrió la caja; {{temía que fuera otra broma de su primo|Sabe lo que piensa el personaje: narrador omnisciente.}}, aunque {{el primo, escondido detrás de la puerta, ya estaba arrepentido|También sabe lo que piensa otro personaje.}}.'}]),
   m('clasificar_x', consigna='¿Qué narrador cuenta cada fragmento?', cajas=['Primera persona', 'Tercera, desde afuera', 'Tercera omnisciente'], cuantos=5, items=[
     ['Corrí hasta la esquina y no vi a nadie.', 0], ['Nunca me animé a contarle la verdad a mi abuela.', 0], ['Cuando llegamos, la casa estaba a oscuras.', 0],
     ['La mujer cruzó la plaza y se sentó en un banco.', 1], ['El chico tocó el timbre dos veces y esperó.', 1], ['Los perros ladraron cuando el cartero abrió la reja.', 1],
     ['Ana sonreía, pero por dentro sentía que todo iba a salir mal.', 2], ['El viejo recordaba a su hermano cada vez que veía el río.', 2], ['Pedro creía que nadie lo había visto; la vecina, en cambio, lo había reconocido.', 2]]),
   ('Narrador', 'El narrador es la voz que cuenta la historia dentro del relato; no es el autor, que es la persona real que la escribió.'),
   'Según quién cuente, el lector sabe más o menos cosas. Un narrador en primera persona solo conoce lo que vive y piensa él mismo; uno omnisciente puede entrar en la cabeza de todos los personajes.',
   ['Primera persona: un personaje cuenta con «yo» o «nosotros».', 'Tercera persona: cuenta desde afuera, con «él» o «ella».', 'Omnisciente: además sabe lo que piensan y sienten.'])],
 'recuerda': [
   R('Paratexto', 'es todo lo que acompaña al texto y lo presenta: tapa, título, contratapa, índice e imágenes.', 'Título «Lo que guarda el altillo» → hipótesis: misterio'),
   R('Hipótesis de lectura', 'es lo que anticipamos antes de leer y que después confirmamos o corregimos.', 'Contratapa con luces en el muelle → algo raro en el río'),
   R('Inferir', 'es sacar una conclusión que el texto no dice, apoyada en pistas concretas.', 'Pelo chorreando y paraguas roto → hay tormenta'),
   R('Estructura del relato', 'tiene situación inicial, conflicto que rompe la calma y desenlace que lo resuelve.', 'Chacra tranquila → la perra no vuelve → aparece con cachorros'),
   R('Narrador', 'es la voz que cuenta la historia y no se confunde con el autor que la escribió.', '«Yo abrí la caja» → primera persona'),
   R('Narrador omnisciente', 'cuenta en tercera persona y conoce lo que piensan y sienten todos los personajes.', '«Lucas temía que fuera otra broma»')]}

L1['2'] = {'temas': [
 T('Las grandes familias de textos',
   m('esquema', items=[{'nombre': 'Géneros', 'cols': ['Género', 'Cómo se reconoce', 'Ejemplo'], 'filas': [
       ['Narrativo', 'cuenta hechos con un narrador', 'una novela de aventuras'], ['Poético', 'versos, ritmo e imágenes', 'un poema sobre el mar'],
       ['Teatral', 'diálogos y acotaciones para actuar', 'una obra para el acto escolar'], ['No literario', 'informa o explica hechos reales', 'una nota de enciclopedia']],
     'cierre': 'La forma y el propósito definen la familia.'}]),
   m('clasificar_x', consigna='¿A qué género pertenece cada fragmento?', cajas=['Narrativo', 'Poético', 'Teatral', 'No literario'], cuantos=5, items=[
     ['Había una vez un herrero que no sabía decir que no.', 0], ['Aquella tarde, el tren llegó con tres horas de atraso.', 0],
     ['Tus pasos en la arena / se los lleva la marea', 1], ['Luna de los techos, / vigilás mi sueño', 1],
     ['ROSA. —¡No abras esa puerta! (Se interpone, asustada.)', 2], ['(Entra el cartero con un paquete enorme.) CARTERO. —¿Vive acá la señora Ruiz?', 2],
     ['El yacaré overo vive en esteros y lagunas del noreste argentino.', 3], ['Mañana el servicio de colectivos funcionará con horario reducido.', 3]]),
   ('Género', 'Un género es una familia de textos que se parecen en la forma en que están escritos y en lo que buscan provocar en el lector.'),
   'Reconocer el género antes de leer prepara la lectura: no se lee igual un poema que una noticia. Los tres primeros son literarios porque inventan mundos; el último trabaja con hechos reales.',
   ['Narrativo: un narrador cuenta una historia.', 'Poético: versos que transmiten emociones.', 'Teatral: diálogos pensados para ser actuados.']),
 T('Subgéneros narrativos',
   m('marcar', rotulo='Fragmento', items=[
     {'nombre': 'Ciencia ficción', 'texto': '{{En el año 2190|Un tiempo futuro.}}, la ingeniera abrió la compuerta de {{la estación orbital|Tecnología que hoy no existe.}} y {{el robot de limpieza le negó el paso|Máquinas con voluntad propia.}}.', 'cierre': 'Futuro + ciencia y tecnología → ciencia ficción.'},
     {'nombre': 'Maravilloso', 'texto': 'La princesa {{guardó en el bolsillo la piedra que hablaba|Un objeto mágico.}} y {{montó al dragón|Un ser fantástico.}} {{sin que a nadie le pareciera raro|En ese mundo la magia es normal.}}.', 'cierre': 'Magia aceptada por todos → maravilloso.'},
     {'nombre': 'Terror', 'texto': 'Cuando apagó la luz, {{algo rasguñó la puerta del placard|Un hecho amenazante y sin explicación.}}. {{Se quedó quieto, sin respirar|El relato busca que el lector sienta miedo.}}.', 'cierre': 'Lo que asusta es el centro del relato → terror.'}]),
   m('clasificar_x', consigna='Ubicá cada argumento en su subgénero.', cajas=['Maravilloso', 'Ciencia ficción', 'Policial', 'Terror', 'Realista'], cuantos=5, items=[
     ['Un hada concede tres deseos a un zapatero', 0], ['Un chico descubre que su gato es un mago', 0],
     ['Colonos de Marte pierden contacto con la Tierra', 1], ['Una máquina permite viajar al pasado', 1],
     ['Una detective investiga el robo de un cuadro', 2], ['Desaparece un collar durante una fiesta y hay cinco sospechosos', 2],
     ['Una muñeca cambia de lugar cada noche', 3], ['En la casa abandonada se oyen pasos', 3],
     ['Dos amigas se pelean por un malentendido en la escuela', 4], ['Una familia se muda a otra provincia y empieza de cero', 4]]),
   ('Subgénero', 'Dentro del género narrativo, cada subgénero reúne relatos que comparten un tipo de mundo, de personajes y de efecto sobre el lector.'),
   'El subgénero se descubre por las pistas del mundo que se cuenta: si hay magia aceptada, si hay tecnología del futuro o si hay un enigma por resolver. Un mismo libro puede mezclar dos, como un policial con fantasmas.',
   ['Maravilloso: magia que nadie discute. Ciencia ficción: futuro y tecnología.', 'Policial: un enigma y alguien que lo investiga.', 'Terror: busca el miedo. Realista: hechos que podrían pasar.']),
 T('Relatos tradicionales',
   m('esquema', items=[{'nombre': 'Relatos tradicionales', 'cols': ['Relato', 'Personajes', 'Qué busca'], 'filas': [
       ['Mito', 'dioses y héroes', 'explicar el origen del mundo o de la humanidad'], ['Leyenda', 'personas de un pueblo, en un lugar real', 'explicar el origen de algo de esa región'],
       ['Fábula', 'animales que hablan y actúan como personas', 'dejar una enseñanza, la moraleja']], 'cierre': 'Nacieron contados de boca en boca, antes de escribirse.'}]),
   m('elegir_x', consigna='¿Qué tipo de relato tradicional es?', items=[
     {'cons': 'Un dios del fuego roba la luz del sol para regalársela a los primeros humanos.', 'ops': ['Mito', 'Leyenda', 'Fábula'], 'ayuda': 'Hay dioses y se explica un origen de toda la humanidad.'},
     {'cons': 'Una hormiga trabajadora y un grillo que solo canta: cuando llega el invierno, el grillo no tiene qué comer.', 'ops': ['Fábula', 'Mito', 'Leyenda'], 'ayuda': 'Animales que hablan y una enseñanza al final.'},
     {'cons': 'Los pobladores de un cerro de Jujuy cuentan por qué sus piedras tienen siete colores.', 'ops': ['Leyenda', 'Fábula', 'Mito'], 'ayuda': 'Explica algo de un lugar real.'},
     {'cons': 'Un zorro engaña a un cuervo para quedarse con su queso, y el cuervo aprende a no creer en halagos.', 'ops': ['Fábula', 'Leyenda', 'Mito'], 'ayuda': 'Animales que hablan y una moraleja.'}]),
   ('Relato tradicional', 'Los relatos tradicionales son historias anónimas que los pueblos transmitieron oralmente durante siglos antes de que alguien las escribiera.'),
   'Por eso existen muchas versiones de un mismo relato. Para distinguirlos conviene mirar dos cosas: qué personajes aparecen y qué quiere explicar o enseñar la historia.',
   ['Mito: dioses y orígenes del mundo.', 'Leyenda: un lugar real y el origen de algo de allí.', 'Fábula: animales y una moraleja.'])],
 'recuerda': [
   R('Género', 'es una familia de textos que comparten la forma en que se escriben y su propósito.', 'Diálogos con acotaciones → teatral'),
   R('Texto no literario', 'informa o explica sobre hechos reales, sin inventar mundos ni personajes.', 'Una nota de enciclopedia sobre el yacaré'),
   R('Subgénero narrativo', 'agrupa relatos según el tipo de mundo y el efecto que buscan en el lector.', 'Año 2190 y estación orbital → ciencia ficción'),
   R('Mito', 'es un relato con dioses o héroes que explica el origen del mundo o de la humanidad.', 'Un dios regala el fuego a los humanos'),
   R('Leyenda', 'explica el origen de algo de un lugar real, con personajes de un pueblo.', 'Por qué un cerro de Jujuy tiene siete colores'),
   R('Fábula', 'es un relato breve con animales que hablan y una moraleja al final.', 'La hormiga y el grillo')]}

L1['3'] = {'temas': [
 T('Escribir en pasos',
   m('revision', items=[
     {'nombre': 'Mi mascota', 'borrador': 'mi gata se llama Pimienta es naranja. le gusta dormir en la ventana y tambien le gusta dormir en la ventana del comedor', 'criterios': [['Empieza con mayúscula', False, '«mi» → «Mi»'], ['Cada oración termina en punto', False, 'falta punto después de «Pimienta»'], ['No repite ideas', False, '«dormir en la ventana» aparece dos veces'], ['Las tildes están', False, '«tambien» → «también»']], 'final': 'Mi gata se llama Pimienta y es naranja. Le gusta dormir al sol, en la ventana del comedor.'},
     {'nombre': 'Mi barrio', 'borrador': 'En mi barrio hay una plaza grande. los domingos hay feria. me gusta ir con mi abuela porque compramos pan casero', 'criterios': [['Empieza con mayúscula', True], ['Cada oración empieza con mayúscula', False, '«los» y «me»'], ['Termina en punto', False, 'falta el punto final'], ['Usa conectores', True, '«porque»']], 'final': 'En mi barrio hay una plaza grande. Los domingos hay feria. Me gusta ir con mi abuela porque compramos pan casero.'}]),
   m('ordenar_x', consigna='Ordená lo que hace Valentina para escribir sobre su viaje.', items=[
     {'lista': ['Anota en una lista lo que quiere contar del viaje', 'Escribe una primera versión de corrido', 'Relee, tacha repeticiones y agrega lo que falta', 'Copia la versión corregida, prolija']},
     {'lista': ['Decide contar el día que conoció el mar y en qué orden', 'Escribe el texto sin frenar a corregir', 'Lo lee en voz alta y marca lo que suena raro', 'Pasa en limpio la versión final']}]),
   ('Proceso de escritura', 'Escribir bien no sale de una vez: es un proceso con pasos de planificación, borrador, revisión y versión final.'),
   'Separar los pasos alivia: en el borrador se escribe sin miedo a equivocarse, y recién después se corrige. Revisar no es solo buscar faltas; también es ver si se entiende y si sobra o falta algo.',
   ['Planificar: qué quiero decir y en qué orden.', 'Borrador y revisión: escribir, releer, corregir.', 'Pasar en limpio: la versión para otros.']),
 T('Oración y párrafo',
   m('marcar', rotulo='Párrafo', items=[
     {'nombre': 'La tormenta', 'texto': '{{El|Mayúscula: empieza una oración.}} cielo se puso negro de golpe{{.|Punto seguido: termina una oración y la idea sigue.}} En diez minutos se cortó la luz en todo el barrio{{.|Punto y aparte: se cierra la idea del párrafo.}}', 'cierre': 'Un párrafo = varias oraciones sobre una misma idea.'},
     {'nombre': 'El recreo', 'texto': '{{En|Mayúscula al empezar.}} el recreo jugamos al quemado{{.|Punto seguido.}} {{Siempre|Después del punto, mayúscula otra vez.}} gana el equipo de Lautaro{{.|Punto y aparte: terminó el párrafo.}}', 'cierre': 'Cada oración tiene sentido completo.'}]),
   m('puntuar_x', consigna='Tocá entre las palabras para poner el punto donde termina cada oración.', signos=['', '.'], items=[
     {'texto': 'Mi hermano tiene un loro verde[[.]] El loro repite todo lo que oye[[.]]'},
     {'texto': 'Ayer fuimos al río[[.]] El agua estaba helada[[.]] Igual nos metimos[[.]]'},
     {'texto': 'La biblioteca abre temprano[[.]] Los martes hay lectura de cuentos[[.]]'}]),
   ('Oración y párrafo', 'La oración es un conjunto de palabras con sentido completo, que empieza con mayúscula y termina en punto; el párrafo agrupa oraciones sobre una misma idea.'),
   'El punto seguido separa oraciones que siguen hablando de lo mismo. El punto y aparte avisa que esa idea terminó y que el texto cambia de tema, por eso conviene empezar el párrafo nuevo con sangría.',
   ['Mayúscula al empezar cada oración.', 'Punto seguido: la idea continúa.', 'Punto y aparte: empieza otra idea.']),
 T('Conectores: unir ideas',
   m('conectores', items=[
     {'relacion': 'adición', 'a': 'Juego al vóley', 'b': 'voy a clases de guitarra', 'ok': ['y', 'además'], 'mal': ['porque'], 'porque_mal': 'No hay ninguna causa entre las dos cosas.'},
     {'relacion': 'oposición', 'a': 'Me encanta leer', 'b': 'este libro no lo pude terminar', 'ok': ['pero', 'sin embargo'], 'mal': ['por eso'], 'porque_mal': 'Haría pensar que no terminarlo es consecuencia de que te guste leer.'},
     {'relacion': 'causa', 'a': 'Llegué tarde', 'b': 'se rompió el colectivo', 'ok': ['porque', 'ya que'], 'mal': ['pero'], 'porque_mal': 'Las ideas no se oponen: una explica la otra.'},
     {'relacion': 'consecuencia', 'a': 'Ensayamos todos los días', 'b': 'la obra salió perfecta', 'ok': ['por eso', 'entonces'], 'mal': ['aunque'], 'porque_mal': 'El buen resultado no se opone al ensayo: es su efecto.'}]),
   m('relacion_x', relaciones=['adición', 'oposición', 'causa', 'consecuencia'], items=[
     {'a': 'Estudié toda la semana', 'b': 'la prueba me salió muy bien', 'relacion': 'consecuencia', 'ok': ['por eso', 'entonces'], 'mal': ['pero', 'porque']},
     {'a': 'El perro ladró toda la noche', 'b': 'había un gato en el techo', 'relacion': 'causa', 'ok': ['porque', 'ya que'], 'mal': ['por eso', 'además']},
     {'a': 'Hacía mucho frío', 'b': 'salimos a andar en bici', 'relacion': 'oposición', 'ok': ['pero', 'sin embargo'], 'mal': ['porque', 'entonces']},
     {'a': 'La casa tiene patio', 'b': 'tiene una huerta al fondo', 'relacion': 'adición', 'ok': ['y', 'además'], 'mal': ['pero', 'porque']}]),
   ('Conector', 'Un conector es una palabra o expresión que une ideas y muestra qué relación hay entre ellas: suma, oposición, causa o consecuencia.'),
   'Elegir mal el conector cambia el sentido del texto. Antes de escribirlo hay que preguntarse cómo se relacionan las dos ideas: si una explica la otra, si se oponen o si simplemente se agregan.',
   ['Sumar: y, también, además.', 'Oponer: pero, sin embargo. Causa: porque, ya que.', 'Consecuencia: por eso, entonces.'])],
 'recuerda': [
   R('Proceso de escritura', 'tiene cuatro pasos: planificar, escribir el borrador, revisar y pasar en limpio.', 'Lista de ideas → borrador → correcciones → versión final'),
   R('Revisar', 'es releer el borrador para corregir errores y ver si se entiende, sobra o falta algo.', '«tambien» → «también»; sacar una repetición'),
   R('Oración', 'es un grupo de palabras con sentido completo que empieza con mayúscula y termina en punto.', 'El cielo se puso negro de golpe.'),
   R('Párrafo', 'reúne oraciones sobre una misma idea y termina con punto y aparte.', 'Dos oraciones sobre la tormenta del barrio'),
   R('Conector', 'une dos ideas y muestra si se suman, se oponen o una es causa de la otra.', 'Llegué tarde porque se rompió el colectivo.')]}

L1['4'] = {'temas': [
 T('Elegir qué leer',
   m('marcar', rotulo='Libro', items=[
     {'nombre': 'Un libro', 'texto': 'Tapa: {{«El faro del fin del mundo» · Julio Verne|Título y autor: un clásico de aventuras.}} · Contratapa: {{Tres guardianes de un faro en la Isla de los Estados enfrentan a una banda de piratas|De qué trata, sin contar el final.}} · Índice: {{15 capítulos|Cuánto lleva leerlo.}}', 'cierre': 'Si te gustan las aventuras y tenés tiempo, es una buena elección.'},
     {'nombre': 'Otro libro', 'texto': 'Tapa: {{«Cuentos para leer en la oscuridad»|El título anticipa el subgénero: terror.}} · Contratapa: {{Nueve relatos breves para leer de a uno|Son cuentos cortos: sirven si hay poco tiempo.}} · Recomendación: {{«Mi prima no pudo dormir», dice Uma|Alguien lo recomienda y sabemos por qué.}}', 'cierre': 'Ideal para quien busca miedo en lecturas cortas.'}]),
   m('elegir_x', consigna='¿Qué libro le conviene a cada lector?', items=[
     {'cons': 'Bruno tiene poco tiempo esta semana y le gusta el misterio.', 'ops': ['Un libro de cuentos policiales breves', 'Una novela de aventuras de 400 páginas', 'Un libro de poemas de amor'], 'ayuda': 'Pensá en el género que le gusta y en el largo.'},
     {'cons': 'A Pilar le encantan los dragones y los hechizos, y tiene todo el verano.', 'ops': ['Una novela larga del subgénero maravilloso', 'Un manual de ciencias', 'Una obra de teatro realista'], 'ayuda': 'Dragones y hechizos: maravilloso. Tiene mucho tiempo.'},
     {'cons': 'Leo leyó la primera página de una novela y no le enganchó nada.', 'ops': ['Probar otro libro', 'Obligarse a terminarla igual', 'Dejar de leer por un tiempo'], 'ayuda': 'Si un libro no engancha, se puede cambiar.'}]),
   ('Elegir un libro', 'Para elegir un libro conviene combinar lo que dice el paratexto con lo que uno tiene ganas de leer y el tiempo disponible.'),
   'La tapa y la contratapa muestran el género y el conflicto; una recomendación cuenta la experiencia de otro lector. Leer la primera página es la mejor prueba: si no engancha, está bien cambiar.',
   ['¿De qué género tengo ganas?', '¿Quién me lo recomendó y por qué?', '¿Me engancha la primera página y me da el tiempo?']),
 T('La ficha bibliográfica',
   m('transformar', items=[
     {'nombre': 'Verne', 'antes': 'Datos sueltos: Julio Verne — Ediciones del Sur — El faro del fin del mundo — 2019', 'pasos': [
       {'v': '{{Verne, Julio.}}', 'txt': 'Primero el autor: apellido, coma y nombre.'},
       {'v': 'Verne, Julio. {{El faro del fin del mundo.}}', 'txt': 'Después el título, tal como figura en la tapa.'},
       {'v': 'Verne, Julio. El faro del fin del mundo. {{Ediciones del Sur,}}', 'txt': 'Sigue la editorial, que figura en la portada.'},
       {'v': 'Verne, Julio. El faro del fin del mundo. Ediciones del Sur, {{2019.}}', 'txt': 'Al final, el año de la edición.'}], 'cierre': 'Así cualquiera puede encontrar ese libro.'},
     {'nombre': 'Montes', 'antes': 'Datos sueltos: 2022 — Graciela Montes — Loqueleo — Doña Clementina Queridita', 'pasos': [
       {'v': '{{Montes, Graciela.}}', 'txt': 'El apellido va primero.'},
       {'v': 'Montes, Graciela. {{Doña Clementina Queridita.}}', 'txt': 'Después el título.'},
       {'v': 'Montes, Graciela. Doña Clementina Queridita. {{Loqueleo, 2022.}}', 'txt': 'Editorial y año cierran la ficha.'}], 'cierre': 'El orden es siempre el mismo.'}]),
   m('armar_x', consigna='Armá la ficha bibliográfica con las piezas en orden.', items=[
     {'cons': 'Libro: «Las aventuras de Pinocho», de Carlo Collodi, editorial Colihue, edición 2015.', 'piezas': ['Collodi, Carlo.', 'Las aventuras de Pinocho.', 'Colihue,', '2015.'], 'extra': ['Carlo Collodi.']},
     {'cons': 'Libro: «Cuentos de la selva», de Horacio Quiroga, editorial Losada, edición 2018.', 'piezas': ['Quiroga, Horacio.', 'Cuentos de la selva.', 'Losada,', '2018.'], 'extra': ['Horacio Quiroga.']},
     {'cons': 'Libro: «Mujercitas», de Louisa May Alcott, editorial Gárgola, edición 2020.', 'piezas': ['Alcott, Louisa May.', 'Mujercitas.', 'Gárgola,', '2020.'], 'extra': ['Louisa May Alcott.']}]),
   ('Ficha bibliográfica', 'La ficha bibliográfica registra los datos de un libro en un orden fijo: autor, título, editorial y año de edición.'),
   'Sirve para recordar qué leímos y para que otra persona pueda encontrar exactamente el mismo libro. El autor se escribe con el apellido primero porque así se ordenan los libros en las bibliotecas.',
   ['Autor: apellido, nombre.', 'Título tal como aparece en la tapa.', 'Editorial y año, al final.'])],
 'recuerda': [
   R('Elegir un libro', 'es combinar el género que tengo ganas de leer, las recomendaciones, la primera página y el tiempo.', 'Poco tiempo y gusto por el misterio → cuentos policiales'),
   R('Contratapa', 'cuenta de qué trata el libro y presenta el conflicto, sin revelar cómo termina.', 'Tres guardianes de un faro enfrentan a unos piratas'),
   R('Ficha bibliográfica', 'registra autor, título, editorial y año, siempre en ese orden.', 'Verne, Julio. El faro del fin del mundo. Ediciones del Sur, 2019.'),
   R('El autor en la ficha', 'se escribe con el apellido primero, una coma y después el nombre.', 'Montes, Graciela')]}

A1 = {
 '1': [
   ORD('Ordená los momentos de este relato: «Un nene que vive en la costa sueña con navegar. Una tormenta hunde el bote de su papá. Juntos arman uno nuevo con maderas del puerto».',
       ['Un nene de la costa sueña con navegar', 'Una tormenta hunde el bote de su papá', 'Juntos arman uno nuevo con maderas del puerto'], 'Situación inicial, conflicto y desenlace.'),
   MC('«Camila llegó a casa, tiró la mochila, se encerró en su cuarto y no quiso cenar.» ¿Qué se puede inferir?', ['Le pasó algo que la puso mal', 'Está muy contenta con el día', 'Tiene mucha hambre'], 'Le pasó algo que la puso mal', 'Encerrarse y no cenar son pistas de que algo la afectó.', 'analizar'),
   CLA('Clasificá cada fragmento según su narrador.', ['Primera persona', 'Tercera persona'], [('Me desperté y la casa estaba vacía.', 'Primera persona'), ('Nunca supe quién dejó la nota.', 'Primera persona'), ('El cartero dejó la caja en la vereda.', 'Tercera persona'), ('Ana subió al tren sin mirar atrás.', 'Tercera persona')], 'Con «yo» cuenta un personaje; con «él» o «ella», alguien de afuera.'),
   MC('Un compañero dice: «En "Yo subí corriendo la escalera", el narrador es el autor del libro». ¿Qué le contestás?', ['Es un narrador en primera persona, no el autor', 'Tiene razón: el que dice «yo» es el autor', 'Es un narrador omnisciente'], 'Es un narrador en primera persona, no el autor', 'El narrador es una voz dentro del relato, aunque diga «yo».', 'error')],
 '2': [
   CLA('Clasificá cada texto en su género.', ['Narrativo', 'Poético', 'Teatral', 'No literario'], [('Érase una vez un pueblo sin relojes.', 'Narrativo'), ('Verde la hoja, / verde el río', 'Poético'), ('JUAN. —¿Quién anda ahí? (Apaga la vela.)', 'Teatral'), ('El colibrí bate sus alas unas 50 veces por segundo.', 'No literario')], 'Forma y propósito definen el género.'),
   CLA('¿De qué subgénero es cada argumento?', ['Maravilloso', 'Ciencia ficción', 'Policial', 'Terror'], [('Un hechicero convierte al rey en sapo', 'Maravilloso'), ('Una nave encuentra vida en una luna helada', 'Ciencia ficción'), ('Una inspectora busca al ladrón de un banco', 'Policial'), ('Una voz llama desde el pozo cada noche', 'Terror')], 'Cada subgénero tiene su tipo de mundo.'),
   MC('Un relato de Misiones cuenta por qué el picaflor vuela de flor en flor: era un joven que buscaba a su amada. ¿Qué es?', ['Leyenda', 'Fábula', 'Mito'], 'Leyenda', 'Explica el origen de algo en un lugar real; no hay moraleja ni dioses creadores.', 'analizar'),
   ODD('¿Cuál NO es un relato tradicional?', ['Un mito sobre el origen del fuego', 'Una fábula de un zorro y un cuervo', 'Una leyenda del cerro de siete colores', 'Una noticia sobre una inundación'], 'Una noticia sobre una inundación', 'La noticia es un texto no literario sobre hechos reales.')],
 '3': [
   ORD('Ordená el proceso de escritura de Iván, que escribe sobre su abuelo.', ['Anota recuerdos de su abuelo y decide el orden', 'Escribe el borrador sin frenar', 'Relee y corrige mayúsculas, puntos y repeticiones', 'Pasa en limpio la versión final'], 'Planificar, borrador, revisar y pasar en limpio.'),
   FB('Completá con el conector que corresponde: «Ensayamos toda la semana, ___ la obra salió muy bien. Me encanta bailar, ___ hoy estoy muy cansada.»', [['por eso', 'entonces'], ['pero', 'sin embargo']], 'El primero indica consecuencia; el segundo, oposición.'),
   TAP('Tocá las dos palabras que deberían empezar con mayúscula: «el perro ladró toda la noche. nadie pudo dormir.»', ['el', 'perro', 'ladró', 'toda', 'la', 'noche.', 'nadie', 'pudo', 'dormir.'], [0, 6], 'Cada oración empieza con mayúscula.', 'error'),
   KW('Escribí un párrafo de tres oraciones sobre un libro o una historia que te haya gustado. Usá al menos un conector que explique por qué te gustó (porque, ya que, por eso).', 'Mayúscula al empezar, punto al terminar cada oración y un conector de causa.', [['porque', 'ya que', 'por eso'], ['gust*', 'me encant*']], 2, 'El párrafo cuenta qué historia te gustó y por qué, con conectores.')],
 '4': [
   UNI('Uní cada parte del libro con lo que te dice.', [('Tapa', 'Título y autor'), ('Contratapa', 'De qué trata, sin el final'), ('Índice', 'Cómo está organizado'), ('Primera página', 'Si te engancha')], 'Cada parte del paratexto da una pista distinta.'),
   ORD('Ordená los datos de la ficha bibliográfica de «Cuentos de la selva», de Horacio Quiroga (Losada, 2018).', ['Quiroga, Horacio.', 'Cuentos de la selva.', 'Losada,', '2018.'], 'Autor, título, editorial y año.'),
   MC('Un compañero armó esta ficha: «Horacio Quiroga. Cuentos de la selva. Losada, 2018.» ¿Qué tiene mal?', ['El autor va con el apellido primero', 'Falta el color de la tapa', 'El año va antes del título'], 'El autor va con el apellido primero', 'Se escribe «Quiroga, Horacio».', 'error'),
   MC('Delfina tiene una semana, le gustan los relatos de miedo y la novela que empezó no le engancha. ¿Qué le conviene?', ['Cambiar por un libro de cuentos de terror breves', 'Terminar la novela aunque no le guste', 'Leer un manual de ciencias'], 'Cambiar por un libro de cuentos de terror breves', 'Gusto, tiempo y primera página: los tres criterios apuntan a cambiar.', 'analizar')],
}

EX1 = [
 [1, MC('«Al ver el boletín, Lautaro lo guardó en el fondo de la mochila y dijo que no le habían dado nada.» ¿Qué se infiere?', ['Le fue mal y no quiere mostrarlo', 'Le fue excelente', 'Perdió la mochila'], 'Le fue mal y no quiere mostrarlo', 'Esconderlo y mentir son las pistas.', 'analizar')],
 [1, MC('«Nadie sabía que la vecina, desde su ventana, había visto todo y pensaba callarlo.» ¿Qué narrador es?', ['Tercera persona omnisciente', 'Primera persona', 'Tercera persona que solo cuenta desde afuera'], 'Tercera persona omnisciente', 'Conoce lo que la vecina piensa hacer.', 'analizar')],
 [1, ORD('Ordená: «Una golondrina se queda sola cuando su bandada parte al norte. Un chico la cuida todo el invierno. En primavera vuelve a volar con las demás».', ['Una golondrina se queda sola cuando su bandada parte', 'Un chico la cuida todo el invierno', 'En primavera vuelve a volar con las demás'], 'Situación inicial, conflicto y desenlace.')],
 [1, TF('El narrador y el autor de un cuento son siempre la misma persona.', 'Falso', 'El autor escribe; el narrador es una voz dentro del relato.')],
 [2, CLA('Clasificá cada fragmento según su género.', ['Narrativo', 'Poético', 'Teatral', 'No literario'], [('La niña encontró una llave en el barro.', 'Narrativo'), ('Duerme el río / bajo la luna', 'Poético'), ('MARTA. —¡Volviste! (Lo abraza.)', 'Teatral'), ('El tero vive en pastizales y lagunas.', 'No literario')], 'Forma y propósito.')],
 [2, MC('En un relato, los dioses del cielo y del mar se pelean y de esa pelea nacen las islas. ¿Qué es?', ['Un mito', 'Una fábula', 'Una leyenda'], 'Un mito', 'Dioses y origen del mundo.', 'analizar')],
 [2, SA('Un cuento transcurre en el año 2300, en una ciudad bajo el mar con robots. ¿De qué subgénero narrativo es?', ['ciencia ficcion', 'ciencia ficción', 'de ciencia ficción', 'de ciencia ficcion'], 'Futuro y tecnología: ciencia ficción.')],
 [3, FB('Completá con el conector justo: «Se cortó la luz, ___ cenamos con velas. Quería ir al cine, ___ no había entradas.»', [['por eso', 'entonces'], ['pero', 'sin embargo']], 'Consecuencia y oposición.')],
 [3, TAP('Tocá la palabra que debería empezar con mayúscula: «Fuimos a la plaza. después tomamos un helado.»', ['Fuimos', 'a', 'la', 'plaza.', 'después', 'tomamos', 'un', 'helado.'], [4], 'Después del punto, mayúscula.', 'error')],
 [3, ORD('Ordená el proceso de escritura de Lola, que escribe una carta a su prima.', ['Decide qué le va a contar y en qué orden', 'Escribe el borrador', 'Relee y corrige', 'Pasa la carta en limpio'], 'Planificar, borrador, revisar y pasar en limpio.')],
 [3, MC('«Me encanta el fútbol, por eso hoy no fui al partido.» ¿Qué problema tiene la oración?', ['El conector debería ser de oposición, como «pero»', 'Le falta la mayúscula inicial', 'No tiene ningún problema'], 'El conector debería ser de oposición, como «pero»', 'No ir no es consecuencia de que te guste.', 'error')],
 [4, ORD('Ordená la ficha bibliográfica de «Mujercitas», de Louisa May Alcott (Gárgola, 2020).', ['Alcott, Louisa May.', 'Mujercitas.', 'Gárgola,', '2020.'], 'Autor, título, editorial y año.')],
 [4, MC('Rodrigo tiene solo los fines de semana para leer y quiere aventuras. ¿Qué mira primero para decidir?', ['La contratapa y la cantidad de páginas', 'El código de barras', 'El color del lomo'], 'La contratapa y la cantidad de páginas', 'La contratapa muestra el género y el conflicto; las páginas, el largo.', 'analizar')],
]

def ajustes1(M):
    for q in M['act']['5']:
        if q['p'].startswith('Relámpago. "Yo encontré'): q['o'] = ['Primera persona', 'Tercera persona', 'Narrador omnisciente']
    for q in M['act']['5']: q.setdefault('n', 'recordar')
    M['examen'] = EX1

# =====================================================================================================
# MISIÓN 2 · El cuento policial: «La liga de los pelirrojos»
# =====================================================================================================
L2 = {}
L2['1'] = {'temas': [
 T('El cuento policial',
   m('marcar', rotulo='Caso', items=[
     {'nombre': 'La medalla', 'texto': '{{Desaparece la medalla de oro del club|El crimen: el hecho que rompe el orden.}}. {{¿Quién la sacó de la vitrina cerrada con llave?|El enigma: la pregunta que mueve el relato.}} {{La entrenadora Ríos|La detective: investiga y razona.}} interroga {{al utilero, al presidente y a una jugadora|Los sospechosos.}}, y encuentra {{una llave copiada en el vestuario|Una pista.}}.', 'cierre': 'Crimen, enigma, detective, sospechosos y pistas.'},
     {'nombre': 'El cuadro', 'texto': 'En el museo {{cambiaron un cuadro por una copia|El crimen.}}. {{¿Cómo, si las cámaras no muestran a nadie?|El enigma.}} {{El inspector Lugo|El detective.}} descubre que {{la copia tiene la pintura todavía fresca|La pista que lo lleva a la solución.}}.', 'cierre': 'Todo gira alrededor de resolver el enigma.'}]),
   m('unir_x', consigna='Uní cada elemento del policial con su ejemplo.', items=[
     {'pares': [['Crimen', 'Roban el trofeo del colegio'], ['Enigma', '¿Quién tenía la llave de la vitrina?'], ['Detective', 'La preceptora que investiga'], ['Pista', 'Una huella de barro junto a la vitrina']]},
     {'pares': [['Crimen', 'Desaparece un collar en la fiesta'], ['Sospechoso', 'El mozo que salió temprano'], ['Pista', 'Una perla en el bolsillo de un saco'], ['Ayudante', 'El sobrino que acompaña a la detective']]}]),
   ('Cuento policial', 'El cuento policial es un relato que gira en torno a un enigma, casi siempre un crimen, que un detective investiga hasta descubrir la verdad.'),
   'Su atractivo está en que el lector también investiga: recibe las mismas pistas que el detective y trata de adelantarse a la solución. El género nació en el siglo diecinueve con los relatos de Edgar Allan Poe.',
   ['Un crimen o hecho misterioso rompe el orden.', 'Un detective y, a veces, un ayudante investigan.', 'Hay sospechosos, pistas y una solución final.']),
 T('Dos tipos de policial',
   m('esquema', items=[{'nombre': 'Enigma y negro', 'cols': ['', 'Policial de enigma', 'Policial negro'], 'filas': [
       ['El detective', 'razona desde su escritorio o la escena del crimen', 'recorre calles peligrosas y se arriesga'], ['El crimen', 'es un rompecabezas que hay que armar', 'muestra una sociedad violenta o corrupta'],
       ['El final', 'la verdad sale a la luz y el orden vuelve', 'se resuelve el caso, pero el mundo sigue igual de duro']], 'cierre': 'Sherlock Holmes es el gran detective del policial de enigma.'}]),
   m('clasificar_x', consigna='¿Qué tipo de policial es cada fragmento?', cajas=['De enigma', 'Negro'], cuantos=5, items=[
     ['La detective observó la taza y supo enseguida quién había mentido.', 0], ['Reunió a los cinco sospechosos en la biblioteca para explicar el caso.', 0], ['Una sola pista, una ceniza en la alfombra, alcanzó para resolverlo.', 0],
     ['El investigador caminó bajo la lluvia por el puerto, con miedo de que lo siguieran.', 1], ['Descubrió que el jefe de policía también cobraba a la banda.', 1], ['Cerró el caso, pero sabía que mañana habría otro muerto en esa ciudad.', 1]]),
   ('Policial de enigma', 'El policial de enigma, o clásico, presenta el crimen como un rompecabezas que el detective resuelve usando la razón.'),
   'El policial negro, en cambio, pone al detective en una ciudad peligrosa donde el delito muestra los problemas de toda la sociedad. Distinguirlos ayuda a saber qué esperar del final.',
   ['Enigma: deducción y orden recuperado.', 'Negro: violencia, riesgo y corrupción.', 'Holmes, Poirot y Dupin son detectives de enigma.']),
 T('El método del detective',
   m('marcar', rotulo='Deducción', items=[
     {'nombre': 'Los zapatos', 'texto': 'La detective {{nota barro rojizo en los zapatos del jardinero|Observar: un detalle que otros no ven.}}. {{Ese barro solo está junto al estanque|Relacionar el detalle con lo que sabe.}}. {{Entonces él estuvo en el estanque, aunque dijo que no salió del galpón|Deducir: sacar una conclusión lógica.}}. {{Revisa el estanque y encuentra la caja escondida|Comprobar antes de acusar.}}.', 'cierre': 'Observar → relacionar → deducir → comprobar.'},
     {'nombre': 'La taza', 'texto': 'El inspector {{ve dos tazas de café en la mesa|Observar.}}. {{La víctima vivía sola|Relacionar con un dato conocido.}}. {{Alguien la visitó esa mañana|Deducir.}}. {{Busca huellas en la segunda taza|Comprobar.}}.', 'cierre': 'Nunca adivina: cada paso se apoya en el anterior.'}]),
   m('ordenar_x', consigna='Ordená los pasos que sigue la detective.', items=[
     {'lista': ['Observa que la ventana tiene el vidrio roto hacia afuera', 'Relaciona: un vidrio que cae afuera se rompió desde adentro', 'Deduce que el robo lo simuló alguien de la casa', 'Comprueba que no hay huellas en el jardín']},
     {'lista': ['Ve que el reloj del sospechoso está mojado', 'Recuerda que esa noche solo llovió en la costa', 'Deduce que él estuvo en la costa y no en el centro', 'Confirma que su auto pasó por el peaje de la costa']}]),
   ('Deducción', 'La deducción es el razonamiento que va de los detalles observados a una conclusión que se sigue de ellos de manera lógica.'),
   'El detective clásico no adivina ni confía en la suerte: observa lo que otros pasan por alto, lo relaciona con lo que sabe y recién acusa cuando puede comprobarlo. Sherlock Holmes es el modelo de este método.',
   ['Observar cada detalle.', 'Relacionar las pistas y deducir.', 'Comprobar antes de acusar.'])],
 'recuerda': [
   R('Cuento policial', 'es un relato con un enigma, casi siempre un crimen, que un detective investiga.', 'Desaparece la medalla del club y la entrenadora investiga'),
   R('Enigma', 'es la pregunta central del policial: quién lo hizo, cómo o por qué.', '¿Quién sacó la medalla de una vitrina con llave?'),
   R('Policial de enigma', 'presenta el crimen como un rompecabezas que el detective resuelve razonando.', 'Una ceniza en la alfombra alcanza para resolverlo'),
   R('Policial negro', 'muestra un detective en una ciudad peligrosa y un crimen que revela una sociedad corrupta.', 'El jefe de policía cobraba a la banda'),
   R('Deducción', 'es llegar a una conclusión lógica a partir de detalles observados, y comprobarla.', 'Barro del estanque en los zapatos → estuvo en el estanque')]}

L2['2'] = {'temas': [
 T('Pistas y falsas pistas',
   m('marcar', rotulo='Caso', items=[
     {'nombre': 'La bicicleta', 'texto': 'Robaron la bici de Tomi del patio. {{Todos miran al chico nuevo, que llegó tarde y con la ropa sucia|Falsa pista: parece sospechoso, pero llegó tarde por ayudar a su abuela.}}. En cambio, {{el candado está abierto con su propia llave|Pista: quien la llevó sabía dónde estaba la llave.}} y {{la hermana de Tomi tiene esa llave|Pista: la verdad empieza a aparecer.}}.', 'cierre': 'La hermana la llevó prestada sin avisar.'},
     {'nombre': 'El pastel', 'texto': 'Desapareció medio pastel de la cocina. {{El perro tiene crema en el hocico|Falsa pista: la crema era de su comida.}}. Pero {{falta un plato del armario alto|Pista: el perro no llega ahí.}} y {{hay migas en la escalera hacia el cuarto del abuelo|Pista: marca un camino.}}.', 'cierre': 'Fue el abuelo, que no resistió la tentación.'}]),
   m('marcar_x', consigna='Tocá solo las pistas verdaderas: las que acercan a la verdad.', items=[
     {'cons': 'Caso: desapareció la recaudación del kiosco escolar. Fue la cajera.', 'texto': '[[La cajera pidió cambiar de turno ese día|1]] · [[El portero tiene cara de enojado|0]] · [[La caja no fue forzada|1]] · [[Un alumno llegó corriendo al recreo|0]]'},
     {'cons': 'Caso: alguien rompió el vidrio del aula. Fue la pelota de un chico de sexto.', 'texto': '[[Hay una pelota debajo del pupitre|1]] · [[La directora estaba de mal humor|0]] · [[Sexto tenía educación física en el patio de al lado|1]] · [[Llovió a la tarde|0]]'}]),
   ('Pista', 'Una pista es un dato que acerca a la verdad del caso; una falsa pista es un dato que distrae y hace mirar hacia el lado equivocado.'),
   'Los autores de policiales usan falsas pistas a propósito para que el lector sospeche de quien no es. Por eso un buen lector, como un buen detective, desconfía de lo que parece demasiado evidente.',
   ['La pista verdadera se puede comprobar.', 'La falsa pista parece importante, pero tiene otra explicación.', 'Lo evidente no siempre es lo cierto.']),
 T('Tipos de pistas',
   m('esquema', items=[{'nombre': 'Tipos de pistas', 'raiz': 'Pistas', 'ramas': [
       ['Materiales', ['un objeto o una marca: una huella, un botón, barro'], 'Se pueden ver y tocar.'], ['Testimonios', ['lo que dicen los testigos y sospechosos'], 'Hay que comprobar si dicen la verdad.'],
       ['Contradicciones', ['dos datos que no encajan entre sí'], 'Alguien dijo que dormía, pero tiene las zapatillas mojadas.'], ['Ausencias', ['algo que debería estar o pasar y no está'], 'La alarma no sonó: quien entró conocía la clave.']],
     'cierre': 'La coartada es un testimonio que el detective pone a prueba.'}]),
   m('clasificar_x', consigna='¿Qué tipo de pista es cada una?', cajas=['Material', 'Testimonio', 'Contradicción', 'Ausencia'], cuantos=6, items=[
     ['Un pelo rubio en el sillón', 0], ['Una colilla junto a la ventana', 0], ['La vecina dice que oyó un portazo a las diez', 1], ['El chofer cuenta que vio un auto gris', 1],
     ['Dice que no sabe nadar, pero tiene una medalla de natación', 2], ['Asegura que estuvo en casa, pero su celular estaba en el centro', 2], ['El perro guardián no ladró esa noche', 3], ['Falta la foto que siempre estaba en la repisa', 3]]),
   ('Coartada', 'La coartada es la prueba de que un sospechoso estaba en otro lugar cuando ocurrió el crimen; el detective siempre la pone a prueba.'),
   'Clasificar las pistas ayuda a pensar qué hacer con cada una: un objeto se analiza, un testimonio se contrasta con otros y una contradicción delata a quien miente. La ausencia es la más difícil de ver.',
   ['Materiales: objetos y marcas.', 'Testimonios: lo que dicen las personas.', 'Contradicciones y ausencias: lo que no encaja o falta.']),
 T('Las pistas de «La liga de los pelirrojos»',
   m('marcar', rotulo='Detalle', items=[
     {'nombre': 'El ayudante', 'texto': 'El ayudante de Wilson {{acepta trabajar por poca plata|Contradicción: alguien hábil no se conforma con eso, salvo que busque otra cosa.}} y {{baja todo el tiempo al sótano|Pista: hace algo a escondidas.}}. Además, {{sus pantalones están gastados en las rodillas|Pista material: pasa horas arrodillado.}}.', 'cierre': 'El ayudante tiene un plan propio en esa casa.'},
     {'nombre': 'La liga', 'texto': '{{Un trabajo raro y bien pagado|Falsa pista: parece el misterio principal.}} saca a Wilson de su casa {{todas las mañanas|Pista: alguien necesita la casa vacía.}}. {{Cuando ya no hace falta, la liga desaparece|Pista: era solo una excusa.}}.', 'cierre': 'La liga es la gran distracción del cuento.'}]),
   m('unir_x', consigna='Uní cada detalle del cuento con lo que revela.', items=[
     {'pares': [['El ayudante cobra la mitad de lo normal', 'Le interesa estar en la casa por otro motivo'], ['Pasa horas en el sótano', 'Hace algo a escondidas'], ['Tiene las rodillas gastadas', 'Excava'], ['Detrás de la casa hay un banco', 'Ahí está el objetivo del plan']]}]),
   ('Lectura de pistas', 'Leer un policial como detective es preguntarse, ante cada detalle raro, qué explicación lo une con los demás.'),
   'En «La liga de los pelirrojos», lo más llamativo, un trabajo absurdo y bien pagado, no es el crimen sino la manera de vaciar la casa. Las pistas verdaderas están en detalles pequeños del ayudante de Wilson.',
   ['Lo llamativo puede ser una distracción.', 'Los detalles chicos suelen ser las pistas.', 'Todas las pistas deben encajar en una explicación.'])],
 'recuerda': [
   R('Pista', 'es un dato que acerca a la verdad y que se puede comprobar.', 'El candado se abrió con su propia llave'),
   R('Falsa pista', 'es un dato que distrae y hace sospechar de quien no es.', 'El chico nuevo llegó tarde y con la ropa sucia'),
   R('Contradicción', 'son dos datos que no pueden ser ciertos a la vez y delatan una mentira.', 'Dice que no sabe nadar y tiene una medalla de natación'),
   R('Pista de ausencia', 'es algo que debería estar o pasar y no está, y por eso llama la atención.', 'El perro guardián no ladró esa noche'),
   R('Coartada', 'es la prueba de que un sospechoso estaba en otro lugar cuando ocurrió el crimen.', 'Estaba en el cine: lo dice la entrada con la hora'),
   R('La gran distracción', 'en «La liga de los pelirrojos» es el trabajo raro que saca a Wilson de su casa.', 'Copiar libros por un sueldo alto')]}

L2['3'] = {'temas': [
 T('Unir las pistas',
   m('esquema', items=[
     {'nombre': 'El túnel', 'raiz': 'Conclusión: un túnel hacia el banco', 'ramas': [
       ['Pista 1', ['el ayudante pasa horas en el sótano'], 'Hace algo bajo tierra.'], ['Pista 2', ['tiene las rodillas gastadas'], 'Excava arrodillado.'],
       ['Pista 3', ['la vereda suena hueca al golpearla'], 'Hay un espacio vacío debajo.'], ['Pista 4', ['detrás de la casa hay un banco'], 'El túnel tiene un destino.']], 'cierre': 'Ninguna pista sola alcanza; juntas, explican todo.'},
     {'nombre': 'El kiosco', 'raiz': 'Conclusión: fue la cajera', 'ramas': [
       ['Pista 1', ['la caja no fue forzada'], 'Quien la abrió tenía la llave.'], ['Pista 2', ['la cajera pidió cambiar de turno'], 'Quería estar sola.'], ['Pista 3', ['compró una campera cara al día siguiente'], 'Tuvo plata de golpe.']], 'cierre': 'La conclusión tiene que explicar todas las pistas.'}]),
   m('elegir_x', consigna='¿Qué conclusión explica TODAS las pistas?', items=[
     {'cons': 'Pistas: la puerta no fue forzada · el perro no ladró · falta la llave de repuesto de la cocina.', 'ops': ['Entró alguien conocido que tenía la llave', 'Un desconocido rompió la ventana', 'Nadie entró y el objeto se perdió'], 'ayuda': 'El perro no ladra a quien conoce, y la llave explica la puerta.'},
     {'cons': 'Pistas: el sospechoso tiene arena en los zapatos · dice que estuvo en la ciudad · su auto pasó por el peaje de la playa.', 'ops': ['Mintió: estuvo en la playa', 'Dice la verdad: estuvo en la ciudad', 'Le prestó el auto a otra persona'], 'ayuda': 'La arena y el peaje coinciden; su testimonio no.'}]),
   ('Unir pistas', 'Resolver un enigma es encontrar la única explicación que une todas las pistas, sin dejar ninguna afuera.'),
   'Cada pista por separado puede tener muchas explicaciones; juntas, solo encajan en una. Por eso el detective no se apura: si una pista no entra en su conclusión, la conclusión está mal y vuelve a pensar.',
   ['Reunir todas las pistas.', 'Buscar la explicación que las une.', 'Si una pista no encaja, revisar la conclusión.']),
 T('El narrador testigo',
   m('versiones', rotulo='Versión', items=[
     {'nombre': 'Testigo', 'texto': '{{Yo|Watson cuenta en primera persona.}} no entendía por qué Holmes golpeaba la vereda con el bastón; {{él no me explicó nada|El testigo sabe menos que el detective: el lector tampoco sabe.}}.'},
     {'nombre': 'Detective', 'texto': '{{Golpeé la vereda para saber si había un túnel debajo|Si narrara Holmes, revelaría su plan enseguida.}}; {{sonó hueca, como esperaba|Se perdería el suspenso.}}.'},
     {'nombre': 'Omnisciente', 'texto': 'Holmes golpeó la vereda {{buscando el túnel que Clay cavaba en ese momento|El omnisciente sabe todo: revelaría al culpable antes de tiempo.}}.'}]),
   m('elegir_x', consigna='Pensá en el efecto del narrador.', items=[
     {'cons': 'Si «La liga de los pelirrojos» la contara Holmes en primera persona, ¿qué se perdería?', 'ops': ['El suspenso, porque él sabe la solución', 'Los diálogos', 'El nombre de los personajes'], 'ayuda': 'El que narra sabe lo que sabe el detective.'},
     {'cons': '¿Por qué Watson es un buen narrador para un policial de enigma?', 'ops': ['Ve todo pero entiende menos que Holmes, como el lector', 'Porque él es el culpable', 'Porque sabe lo que piensan todos'], 'ayuda': 'El testigo participa pero no deduce como el detective.'},
     {'cons': 'Un narrador cuenta: «Mi amigo examinó la alfombra en silencio; yo no veía nada raro». ¿Qué tipo de narrador es?', 'ops': ['Testigo', 'Protagonista', 'Omnisciente'], 'ayuda': 'Cuenta lo que hace otro, el protagonista, y sabe menos que él.'}]),
   ('Narrador testigo', 'El narrador testigo participa de los hechos y los cuenta en primera persona, pero el protagonista de la historia es otro personaje.'),
   'En los cuentos de Sherlock Holmes narra el doctor Watson, que acompaña al detective y entiende menos que él. Así el lector descubre la verdad al mismo tiempo que Watson y el suspenso dura hasta el final.',
   ['Cuenta con «yo», pero no es el protagonista.', 'Sabe menos que el detective.', 'Mantiene el suspenso hasta la revelación.']),
 T('Las dos historias y la revelación',
   m('linea_tiempo', items=[
     {'nombre': 'La liga', 'hechos': [{'t': 'Wilson consulta a Holmes por la liga que desapareció', 'c': 3}, {'t': 'Holmes investiga la casa y la vereda', 'c': 4}, {'t': 'Esperan de noche en la bóveda del banco', 'c': 5}, {'t': 'Holmes explica que Clay cavaba un túnel desde hacía semanas', 'c': 1, 'flash': 1}, {'t': 'La liga saca a Wilson de su casa cada mañana', 'c': 2, 'flash': 1}],
      'marca': 'La historia del crimen (el túnel) empezó antes, pero se cuenta al final, en la revelación.', 'cierre': 'El crimen se reconstruye al final: así se mantiene el misterio.'}]),
   m('ordenar_x', consigna='Ordená la historia del crimen como ocurrió en el tiempo (no como se cuenta).', items=[
     {'lista': ['La cajera copia la llave de la caja', 'Pide cambiar de turno', 'Saca la recaudación', 'La detective descubre la copia de la llave']},
     {'lista': ['El sobrino planea quedarse con el collar', 'Esconde el collar en la maceta durante la fiesta', 'La dueña denuncia el robo', 'El inspector encuentra el collar y explica el caso']}]),
   ('Dos historias', 'Todo policial de enigma cuenta dos historias: la del crimen, que pasó antes y queda oculta, y la de la investigación, que leemos paso a paso.'),
   'La historia del crimen recién se cuenta completa al final, en la revelación, cuando el detective explica cómo lo dedujo. Por eso el orden del relato no coincide con el orden en que ocurrieron los hechos.',
   ['Historia del crimen: oculta hasta el final.', 'Historia de la investigación: la que seguimos.', 'Revelación: el detective explica todo.'])],
 'recuerda': [
   R('Resolver un enigma', 'es encontrar la única explicación que une todas las pistas sin dejar ninguna afuera.', 'Sótano + rodillas gastadas + vereda hueca + banco → túnel'),
   R('Narrador testigo', 'participa y cuenta en primera persona, pero el protagonista es otro.', 'Watson narra los casos de Holmes'),
   R('Efecto del narrador testigo', 'es mantener el suspenso, porque sabe menos que el detective, igual que el lector.', '«Yo no entendía por qué golpeaba la vereda»'),
   R('Las dos historias', 'son la del crimen, oculta, y la de la investigación, que se lee paso a paso.', 'Clay cava el túnel / Holmes reúne pistas'),
   R('Revelación', 'es el final donde el detective explica cómo resolvió el caso.', 'Holmes explica el plan del túnel después de atrapar a Clay')]}

L2['4'] = {'temas': [
 T('Planificar un enigma',
   m('esquema', items=[
     {'nombre': 'La guitarra', 'raiz': 'Mi policial', 'ramas': [
       ['Misterio', ['desaparece la guitarra del acto escolar'], 'Primero se decide qué pasó y quién fue.'], ['Detective', ['Nina, la más observadora de primero'], 'Alguien con un rasgo que lo ayude a investigar.'],
       ['Pistas', ['verdaderas: cuerdas nuevas en la mochila del profe de música; resina en sus manos', 'falsa: el portero estaba nervioso'], 'Dos o más verdaderas y una falsa.'], ['Revelación', ['el profe la llevó a arreglar y se olvidó de avisar'], 'Se explica con las pistas ya dadas.']], 'cierre': 'Se planifica al revés: primero la solución, después las pistas.'},
     {'nombre': 'El gato', 'raiz': 'Mi policial', 'ramas': [
       ['Misterio', ['el gato de la vecina aparece cada noche con un moño nuevo'], 'El enigma no tiene que ser un crimen.'], ['Detective', ['Bauti y su hermana'], 'Pueden ser dos.'],
       ['Pistas', ['verdaderas: lana en el patio del fondo; la señora del fondo teje', 'falsa: un camión de mudanzas'], 'Cada pista se puede comprobar.'], ['Revelación', ['la señora del fondo le teje moños al gato'], 'Una solución sorprendente pero lógica.']], 'cierre': 'Con el plan listo, se escribe sin perderse.'}]),
   m('completar_x', consigna='Completá el plan del policial con la opción que corresponde.', items=[
     {'texto': 'Misterio: desaparecen las llaves del gimnasio. Solución: las tomó [[la preceptora/una paloma/nadie]]. Pista verdadera: [[ella cerró el gimnasio ese día/hacía calor/hubo un acto]]. Falsa pista: [[un alumno se fue temprano/la preceptora tenía la llave/la puerta estaba cerrada]].'},
     {'texto': 'Misterio: alguien comió las galletas del concurso. Solución: fue [[el abuelo jurado/el perro/la lluvia]]. Pista verdadera: [[tenía azúcar en la corbata/era martes/sonó el timbre]]. Falsa pista: [[el perro ladraba cerca de la mesa/el abuelo tenía azúcar/faltaban galletas]].'}]),
   ('Planificar un policial', 'Planificar un policial es decidir primero la solución del enigma y después las pistas que llevan a ella y las que distraen.'),
   'Si se empieza a escribir sin saber quién lo hizo, las pistas no encajan y el final parece inventado. Con el plan armado, cada escena puede dejar una pista en su lugar sin que el lector lo note.',
   ['Primero la solución: qué pasó y quién fue.', 'Después el detective y las pistas, con una falsa.', 'Por último, cómo será la revelación.']),
 T('Escribir con juego limpio',
   m('revision', items=[
     {'nombre': 'La guitarra', 'borrador': 'La guitarra del acto desapareció. Nina buscó por toda la escuela. Al final un nene confesó que la había escondido porque sí.', 'criterios': [['El enigma aparece al principio', True], ['Hay pistas antes de la solución', False, 'no hay ninguna pista'], ['Hay una falsa pista', False], ['La solución sale de las pistas', False, 'la confesión aparece de golpe']], 'final': 'La guitarra del acto desapareció. Nina notó resina en las manos del profe de música y cuerdas nuevas en su mochila; el portero, nervioso, parecía culpable, pero solo había perdido sus anteojos. Al final, Nina reveló que el profe la había llevado a arreglar.'},
     {'nombre': 'El gato', 'borrador': 'El gato de la vecina tenía moños. Bauti vio lana en el patio. La señora del fondo teje. Era la señora del fondo.', 'criterios': [['El enigma aparece al principio', True], ['Hay pistas antes de la solución', True], ['Hay una falsa pista', False, 'agregar el camión de mudanzas'], ['La revelación explica el caso', False, 'falta contar cómo lo dedujo']], 'final': 'Cada noche, el gato de la vecina volvía con un moño nuevo. Bauti sospechó de los de la mudanza, pero encontró lana en el patio del fondo. Como la señora del fondo tejía, la esperaron una noche y la vieron atándole un moño rojo.'}]),
   m('escribir_x', items=[
     {'cons': 'Escribí el comienzo de un cuento policial: presentá el misterio y dejá una primera pista.', 'criterios': [{'txt': 'Al menos 30 palabras', 'min': 30}, {'txt': 'Plantea qué desapareció o qué pasó', 're': 'desapareci|robaron|faltaba|alguien|nadie sab'}, {'txt': 'Deja una pista (huella, marca, objeto, testigo…)', 're': 'huella|marca|barro|testigo|vio|encontr|pista|mancha'}], 'modelo': 'El lunes a la mañana, la copa del torneo desapareció de la vitrina de la dirección. Nadie sabía quién tenía la llave, pero Nina encontró una huella de barro junto a la puerta y una servilleta del bar de la esquina.'}]),
   ('Juego limpio', 'El juego limpio es la regla del policial de enigma según la cual el lector recibe todas las pistas necesarias antes de la revelación.'),
   'Así el lector puede competir con el detective. Una solución que aparece de golpe, por casualidad o por una confesión sin pistas previas, decepciona: parece que el autor hizo trampa.',
   ['Inicio: aparece el enigma.', 'Desarrollo: la investigación, pista por pista.', 'Desenlace: la revelación usa las pistas ya dadas.'])],
 'recuerda': [
   R('Planificar al revés', 'significa decidir primero la solución y después las pistas que llevan a ella.', 'Solución: el profe llevó la guitarra a arreglar'),
   R('Pistas del plan', 'son dos o más verdaderas que se pueden comprobar y al menos una falsa que distrae.', 'Resina en las manos del profe / el portero nervioso'),
   R('Estructura del policial', 'tiene un inicio con el enigma, un desarrollo con la investigación y un desenlace con la revelación.', 'Desaparece la guitarra → Nina investiga → explica el caso'),
   R('Juego limpio', 'es dar al lector todas las pistas antes de la revelación, sin resolver por casualidad.', 'La solución sale de la resina y las cuerdas, no de una confesión')]}

A2 = {
 '1': [
   UNI('Uní cada elemento del policial con su ejemplo en un caso nuevo.', [('Crimen', 'Desaparece el anillo de la abuela'), ('Enigma', '¿Quién entró al cuarto con la puerta cerrada?'), ('Detective', 'La nieta que observa todo'), ('Pista', 'Un pétalo de rosa en la alfombra')], 'Son los elementos del policial.'),
   CLA('¿Policial de enigma o negro?', ['De enigma', 'Negro'], [('El detective resuelve el caso con una sola deducción en la sala', 'De enigma'), ('Todos los sospechosos reunidos escuchan la explicación final', 'De enigma'), ('El investigador se esconde de una banda en el puerto', 'Negro'), ('El caso revela que el intendente protegía a los ladrones', 'Negro')], 'Enigma: razonamiento. Negro: riesgo y corrupción.'),
   ORD('Ordená el método de la detective en este caso: «Ve tierra húmeda en las botas del sobrino, recuerda que solo se regó el jardín de atrás, deduce que estuvo allí y lo confirma encontrando sus huellas».', ['Ve tierra húmeda en las botas del sobrino', 'Recuerda que solo se regó el jardín de atrás', 'Deduce que él estuvo en ese jardín', 'Lo confirma encontrando sus huellas'], 'Observar, relacionar, deducir y comprobar.'),
   MC('Un compañero dice: «Holmes resuelve los casos porque tiene suerte y adivina quién fue». ¿Qué le contestás?', ['No: observa, deduce y comprueba antes de acusar', 'Sí: los detectives siempre adivinan', 'No: siempre confiesa el culpable solo'], 'No: observa, deduce y comprueba antes de acusar', 'El método del detective clásico es la deducción.', 'error')],
 '2': [
   TAP('Caso: desapareció el celular de la profe y lo tomó el preceptor. Tocá las DOS pistas verdaderas: «El preceptor tenía la llave de la sala · Un alumno estaba muy nervioso · El celular sonó en el armario del preceptor · Llovía mucho esa tarde».', ['El preceptor tenía la llave de la sala', 'Un alumno estaba muy nervioso', 'El celular sonó en el armario del preceptor', 'Llovía mucho esa tarde'], [0, 2], 'Las otras distraen: no se relacionan con el robo.'),
   CLA('Clasificá cada pista.', ['Material', 'Testimonio', 'Contradicción', 'Ausencia'], [('Una huella de zapatilla en el barro', 'Material'), ('El kiosquero dice que lo vio pasar a las ocho', 'Testimonio'), ('Dice que estaba enfermo, pero subió fotos jugando al fútbol', 'Contradicción'), ('La alarma no sonó esa noche', 'Ausencia')], 'Cada tipo de pista se trabaja distinto.'),
   UNI('Uní cada detalle de «La liga de los pelirrojos» con lo que revela.', [('Un ayudante hábil que cobra poco', 'Quiere estar en esa casa por otra razón'), ('Las horas en el sótano', 'Hace algo a escondidas'), ('Las rodillas gastadas', 'Excava'), ('El trabajo absurdo de la liga', 'Saca a Wilson de su casa')], 'Las pistas apuntan al plan del túnel.'),
   MC('Un sospechoso dice que estaba en el cine cuando ocurrió el robo y muestra la entrada con la hora. ¿Qué es eso?', ['Su coartada, que hay que comprobar', 'Una falsa pista', 'La revelación del caso'], 'Su coartada, que hay que comprobar', 'La coartada es la prueba de que estaba en otro lugar.', 'aplicar')],
 '3': [
   MC('Pistas: no hay ventanas rotas · el perro no ladró · falta la copia de la llave que guardaba la tía. ¿Qué conclusión explica todas las pistas?', ['Entró alguien de confianza que usó la copia', 'Entró un ladrón por la ventana', 'El perro abrió la puerta'], 'Entró alguien de confianza que usó la copia', 'La conclusión tiene que explicar todas las pistas a la vez.', 'analizar'),
   ORD('Ordená la historia del crimen como ocurrió en el tiempo: el sobrino esconde el collar en la maceta, la dueña denuncia el robo, el sobrino planea el robo, el inspector lo descubre.', ['El sobrino planea el robo', 'El sobrino esconde el collar en la maceta', 'La dueña denuncia el robo', 'El inspector lo descubre'], 'El crimen ocurre antes de la investigación.'),
   MC('«Mi amiga revisó el reloj del muerto y sonrió; yo no entendí qué había visto.» ¿Qué narrador es y qué efecto logra?', ['Testigo: mantiene el suspenso', 'Omnisciente: revela todo', 'Protagonista: es la detective'], 'Testigo: mantiene el suspenso', 'Cuenta lo que hace otra y sabe menos que ella.', 'analizar'),
   SA('Al final de un policial, la detective reúne a todos y explica cómo descubrió al culpable. ¿Cómo se llama esa parte del relato?', ['revelacion', 'revelación', 'la revelación', 'la revelacion'], 'Es la revelación.', 'aplicar')],
 '4': [
   ORD('Ordená los pasos para planificar un cuento policial.', ['Decidir qué pasó y quién fue', 'Elegir al detective', 'Pensar las pistas verdaderas y una falsa', 'Decidir cómo será la revelación'], 'Se planifica empezando por la solución.'),
   MC('En el cuento de Marcos, la detective no encuentra ninguna pista y al final el culpable confiesa porque sí. ¿Qué regla no cumple?', ['El juego limpio', 'El narrador testigo', 'La ficha bibliográfica'], 'El juego limpio', 'La solución tiene que salir de pistas que el lector ya vio.', 'error'),
   CLA('Plan: «Desaparece la torta del cumpleaños; fue el tío». Clasificá cada dato.', ['Pista verdadera', 'Falsa pista'], [('El tío tiene crema en el bigote', 'Pista verdadera'), ('El tío pidió quedarse solo en la cocina', 'Pista verdadera'), ('El perro ladraba cerca de la mesa', 'Falsa pista'), ('La prima llegó tarde y despeinada', 'Falsa pista')], 'Las verdaderas llevan al tío; las falsas distraen.'),
   KW('Escribí en tres o cuatro oraciones el plan de un cuento policial: qué pasó, quién investiga, una pista verdadera, una falsa pista y cómo se resuelve.', 'Nombrá el misterio, el detective, las pistas y la revelación.', [['desapareci*', 'robo', 'robaron', 'falta*'], ['detective', 'investig*'], ['pista*'], ['falsa', 'distrae*'], ['revela*', 'descubr*', 'resuelv*']], 4, 'El plan tiene misterio, detective, pistas verdaderas y falsas, y revelación.')],
}

EX2 = [
 [1, MC('En un relato, desaparece un violín antes del concierto y una música lo busca interrogando a la orquesta. ¿Qué es el enigma?', ['¿Quién tomó el violín y por qué?', 'La música que investiga', 'El concierto de la orquesta'], '¿Quién tomó el violín y por qué?', 'El enigma es la pregunta central.', 'analizar')],
 [1, CLA('¿Policial de enigma o negro?', ['De enigma', 'Negro'], [('Una deducción en la biblioteca resuelve el caso', 'De enigma'), ('El detective arriesga su vida en los callejones', 'Negro'), ('El orden se recupera al final', 'De enigma'), ('El crimen muestra la corrupción de la ciudad', 'Negro')], 'Razonamiento vs. riesgo y corrupción.')],
 [1, ORD('Ordená el método del detective.', ['Observar los detalles', 'Relacionar las pistas', 'Deducir una conclusión', 'Comprobar antes de acusar'], 'El detective nunca adivina.')],
 [1, TF('Sherlock Holmes es un detective del policial negro.', 'Falso', 'Pertenece al policial de enigma, o clásico.')],
 [2, TAP('Caso: se perdió la llave del aula y la tenía el delegado. Tocá la pista verdadera: «El delegado cerró el aula el viernes · La directora estaba apurada · Hubo viento a la tarde».', ['El delegado cerró el aula el viernes', 'La directora estaba apurada', 'Hubo viento a la tarde'], [0], 'Es la única que se relaciona con la llave.')],
 [2, MC('El sospechoso dice que no salió de su casa en toda la noche, pero su auto tiene barro fresco del camino de tierra. ¿Qué tipo de pista es?', ['Contradicción', 'Ausencia', 'Testimonio confirmado'], 'Contradicción', 'Dos datos que no pueden ser ciertos a la vez.', 'analizar')],
 [2, MC('En «La liga de los pelirrojos», ¿para qué sirve en realidad la liga?', ['Para sacar a Wilson de su casa', 'Para pagarle bien a Wilson', 'Para enseñarle a copiar libros'], 'Para sacar a Wilson de su casa', 'Es la gran distracción del cuento.', 'recordar')],
 [3, MS('Pistas del cuento: elegí TODAS las que llevan a la conclusión del túnel.', ['El ayudante pasa horas en el sótano', 'Tiene las rodillas gastadas', 'La vereda suena hueca', 'Wilson es pelirrojo', 'Detrás de la casa hay un banco'], ['El ayudante pasa horas en el sótano', 'Tiene las rodillas gastadas', 'La vereda suena hueca', 'Detrás de la casa hay un banco'], 'El pelo de Wilson es la excusa, no una pista del túnel.')],
 [3, MC('¿Por qué conviene que Watson, y no Holmes, narre los casos?', ['Sabe menos y así dura el suspenso', 'Es el culpable de los crímenes', 'Conoce los pensamientos de todos'], 'Sabe menos y así dura el suspenso', 'Es un narrador testigo.', 'analizar')],
 [3, ORD('Ordená la historia del crimen de «La liga» como ocurrió en el tiempo.', ['Clay se emplea como ayudante de Wilson', 'La liga saca a Wilson de su casa', 'Clay cava el túnel hacia el banco', 'Holmes lo atrapa en la bóveda'], 'Así ocurrieron los hechos; el cuento los revela al final.')],
 [4, MC('En el cuento de Sol, la detective resuelve el caso porque ve al culpable por casualidad en la última página, sin pistas previas. ¿Qué falla?', ['No hay juego limpio', 'No tiene narrador', 'No tiene título'], 'No hay juego limpio', 'La solución tiene que salir de pistas ya dadas.', 'error')],
 [4, FB('Completá: «Para planificar un policial, primero se decide la ___ del caso y después las ___ que llevan a ella.»', [['solucion', 'solución'], ['pistas']], 'Se planifica al revés.')],
 [4, KW('Escribí la revelación de este caso en dos o tres oraciones: «Desapareció el trofeo; pistas: barro en las zapatillas del capitán y la llave de la vitrina en su campera».', 'Explicá quién fue y cómo lo prueban las pistas.', [['capitan', 'capitán'], ['barro'], ['llave']], 3, 'La revelación explica el caso usando las pistas.', 'aplicar')],
]

def ajustes2(M):
    for q in M['act']['5']: q.setdefault('n', 'recordar')
    M['examen'] = EX2

def reemplazar(acts):
    def f(M):
        for k, v in acts.items(): M['act'][k] = v
    return f

if __name__ == '__main__':
    ok1 = guardar('contenido/lengua-1/mision-1/mision-1.json', L1, ajustes=lambda M: (reemplazar(A1)(M), ajustes1(M)))
    # ok2 = guardar('contenido/lengua-1/mision-2/mision-2.json', L2, ajustes=lambda M: (reemplazar(A2)(M), ajustes2(M)))
