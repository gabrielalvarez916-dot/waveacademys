# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 10 · Cartas, mails y formularios (la clase animada queda; lección, actividades y examen nuevos)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD

L = {}
L['1'] = {'temas': [
 T('Las partes de una carta',
   m('formato', items=[
     {'tipo': 'una carta formal', 'partes': [['Lugar y fecha', 'Paraná, 12 de agosto de 2026', 'text-align:right', 'Arriba a la derecha: dónde y cuándo se escribe.'], ['Destinatario', 'Sra. Directora del Museo Provincial', '', 'A quién va dirigida, con su cargo.'], ['Saludo', 'De mi mayor consideración:', '', 'Un saludo formal, seguido de dos puntos.'], ['Cuerpo', 'Me dirijo a usted para solicitar una visita guiada para un grupo de doce estudiantes…', '', 'El motivo, explicado con claridad.'], ['Despedida', 'Sin otro particular, la saludo atentamente.', '', 'Una fórmula de cierre respetuosa.'], ['Firma', 'Julieta Romero', 'font-style:italic', 'Nombre de quien escribe.']]},
     {'tipo': 'una carta informal', 'partes': [['Lugar y fecha', 'Colón, 3 de marzo', 'text-align:right', 'También aparece, más breve.'], ['Saludo', '¡Hola, Ceci!', '', 'Cercano, con el nombre.'], ['Cuerpo', 'No sabés lo que me pasó en las vacaciones: aprendí a andar a caballo…', '', 'Cuenta con confianza.'], ['Despedida', '¡Escribime pronto! Un abrazo enorme.', '', 'Afectuosa.'], ['Firma', 'Lu', 'font-style:italic', 'Basta con el nombre o un apodo.']]}]),
   m('ordenar_x', consigna='Ordená las partes de la carta formal.', items=[
     {'lista': ['Rosario, 5 de mayo de 2026', 'Sr. Presidente del Club Atlético Sur', 'De mi consideración:', 'Me dirijo a usted para solicitar el uso de la cancha el sábado…', 'Lo saludo atentamente.', 'Martín Gómez']},
     {'lista': ['Salta, 20 de junio de 2026', 'Sra. Bibliotecaria de la Biblioteca Popular', 'Estimada señora:', 'Le escribo para consultar si es posible renovar el préstamo de dos libros…', 'Desde ya, muchas gracias. Saludos cordiales.', 'Valentina Ruiz']}]),
   ('Carta', 'La carta es un texto que se dirige a un destinatario determinado y se organiza en partes fijas: lugar y fecha, destinatario, saludo, cuerpo, despedida y firma.'),
   'Cada parte cumple una función: la fecha ubica el mensaje en el tiempo, el saludo abre el contacto y la despedida lo cierra con cortesía. Aunque hoy se usen menos las cartas en papel, la misma estructura organiza los mails y los mensajes formales que se envían a instituciones.',
   ['Lugar y fecha, destinatario y saludo.', 'Cuerpo: el motivo del mensaje.', 'Despedida y firma.']),
 T('Carta formal y carta informal',
   m('versiones', rotulo='Carta', items=[
     {'nombre': 'Formal', 'texto': '{{Estimado profesor:|Saludo formal.}} {{Le escribo para consultarle|Trato de «usted».}} si sería posible {{entregar el trabajo el lunes|Pedido claro y cortés.}}. {{Lo saludo atentamente.|Despedida formal.}}'},
     {'nombre': 'Informal', 'texto': '{{¡Hola, Tomi!|Saludo cercano.}} {{¿Me pasás|Trato de «vos».}} {{lo que hicieron en Biología?|Pregunta directa.}} {{¡Gracias, genio!|Despedida afectuosa.}}'}]),
   m('clasificar_x', consigna='¿La expresión es propia de una carta formal o de una informal?', cajas=['Formal', 'Informal'], cuantos=6, items=[
     ['De mi mayor consideración:', 0], ['Me dirijo a usted para…', 0], ['Lo saludo atentamente.', 0], ['Quedo a la espera de su respuesta.', 0],
     ['¡Hola, che!', 1], ['Te cuento que…', 1], ['¡Un abrazo grande!', 1], ['Contestame cuando puedas.', 1]]),
   ('Registro de la carta', 'La carta formal se dirige a autoridades o desconocidos con un lenguaje cuidado y trato de usted; la informal se dirige a personas de confianza con un lenguaje cercano.'),
   'Lo que decide si una carta es formal o informal no es el tema, sino la relación con el destinatario: se puede contar una misma noticia a la abuela y a la directora, pero con palabras distintas. Mezclar registros, como poner «che» en una carta a la municipalidad, hace que el mensaje pierda fuerza.',
   ['Formal: autoridades, instituciones, desconocidos.', 'Informal: familia y amigos.', 'Decide la relación, no el tema.']),
 T('La carta de pedido o reclamo',
   m('marcar', rotulo='Carta', items=[
     {'nombre': 'El reclamo', 'texto': '{{Me dirijo a usted, como vecina del barrio San Martín,|Se presenta: quién escribe.}} {{para informarle que el semáforo de la esquina de Belgrano y Moreno no funciona desde hace dos semanas.|Explica el problema con datos concretos.}} {{Varios chicos cruzan por allí para ir a la escuela.|Da una razón que muestra la importancia.}} {{Por eso, le solicito que se repare a la brevedad.|Hace un pedido concreto.}}', 'cierre': 'Presentación, problema, razón y pedido.'}]),
   m('elegir_x', consigna='¿Qué versión del pedido es más eficaz?', items=[
     {'cons': 'Un pedido a la municipalidad por la plaza del barrio.', 'ops': ['Le solicito que se reparen las dos hamacas rotas de la plaza Sarmiento', 'Arreglen la plaza que está horrible', 'La plaza anda mal'], 'ayuda': 'Concreto, cortés y con datos.'},
     {'cons': 'Un reclamo a una empresa de internet.', 'ops': ['Desde el 3 de mayo el servicio se corta varias veces por día; solicito una revisión técnica', 'Su internet es un desastre', 'Quiero que me anden las cosas'], 'ayuda': 'Fecha, problema y pedido.'},
     {'cons': 'Un pedido a la biblioteca.', 'ops': ['Quisiera saber si pueden conseguir el libro «Las aventuras de Tom Sawyer»', 'Necesito un libro', 'Tráiganme libros nuevos ya'], 'ayuda': 'Qué se pide exactamente.'}]),
   ('Carta de pedido', 'La carta de pedido o de reclamo es una carta formal que presenta un problema con datos concretos y solicita una solución a quien puede darla.'),
   'Para que un reclamo tenga resultado, tiene que ser claro y respetuoso: decir quién escribe, cuál es el problema con datos (dónde, desde cuándo), por qué importa y qué se pide exactamente. Los insultos o las quejas vagas hacen que el pedido sea fácil de ignorar.',
   ['Quién escribe y cuál es el problema.', 'Datos concretos: dónde, desde cuándo.', 'Un pedido claro y respetuoso.'])],
 'recuerda': [
   R('Carta', 'es un texto dirigido a un destinatario determinado, organizado en partes fijas.', 'Lugar y fecha, saludo, cuerpo, despedida y firma'),
   R('Carta formal', 'se dirige a autoridades o desconocidos con lenguaje cuidado y trato de usted.', 'De mi mayor consideración: me dirijo a usted…'),
   R('Carta informal', 'se dirige a familiares o amigos con lenguaje cercano y trato de vos.', '¡Hola, Ceci! Te cuento que…'),
   R('Carta de pedido', 'presenta un problema con datos concretos y solicita una solución con respeto.', 'Le solicito que se reparen las hamacas de la plaza'),
   R('Despedida formal', 'es la fórmula de cierre respetuosa que se usa antes de la firma en una carta formal.', 'Lo saludo atentamente.')]}

L['2'] = {'temas': [
 T('Las partes de un mail',
   m('formato', items=[
     {'tipo': 'un mail formal', 'partes': [['Para', 'secretaria@clubsur.org.ar', '', 'La dirección del destinatario, sin errores.'], ['Asunto', 'Consulta: horarios de natación para menores', 'font-weight:700', 'De qué trata, en pocas palabras.'], ['Saludo', 'Buenas tardes:', '', 'Un saludo cortés.'], ['Cuerpo', 'Quisiera saber qué días y horarios hay clases de natación para chicos de 13 años y cuál es el costo mensual.', '', 'El motivo, breve y claro.'], ['Cierre y firma', 'Muchas gracias. Saludos cordiales, Lucas Pereyra', '', 'Agradece y firma con nombre completo.'], ['Adjunto', '(no hace falta)', 'color:#888', 'Solo si se envía un archivo.']]}]),
   m('unir_x', consigna='Uní cada parte del mail con su función.', items=[
     {'pares': [['Para', 'a quién se envía'], ['Asunto', 'de qué trata el mensaje'], ['Cuerpo', 'el mensaje completo'], ['Adjunto', 'un archivo que acompaña']]},
     {'pares': [['CC', 'a quién se envía una copia'], ['Asunto', 'de qué trata el mensaje'], ['Firma', 'quién escribe'], ['Saludo', 'cómo se abre el mensaje']]}]),
   ('Mail', 'El mail, o correo electrónico, es un mensaje escrito que se envía por internet y tiene campos fijos: destinatario, asunto, cuerpo y, si hace falta, archivos adjuntos.'),
   'Aunque se escribe rápido, un mail a una institución o a un profesor es un texto formal: lleva saludo, cuerpo y firma como una carta. La diferencia es que el asunto aparece antes de abrirlo, y de él depende muchas veces que el mail se lea a tiempo.',
   ['Para, asunto, cuerpo y adjunto.', 'Formal con instituciones y profesores.', 'Saludo, cuerpo y firma, como una carta.']),
 T('Un asunto que diga de qué se trata',
   m('versiones', rotulo='Asunto', items=[
     {'nombre': 'Vago', 'texto': '{{Hola|No dice nada: se pierde entre otros mails.}}'},
     {'nombre': 'Vago', 'texto': '{{URGENTE!!!|Exagera y no informa.}}'},
     {'nombre': 'Claro', 'texto': '{{Entrega del trabajo de Historia: pedido de prórroga|Dice el tema y qué se pide.}}'}]),
   m('elegir_x', consigna='Elegí el mejor asunto para cada mail.', items=[
     {'cons': 'Le escribís a tu profesora porque no podés abrir el archivo de la tarea de Lengua.', 'ops': ['No puedo abrir el archivo de la tarea de Lengua', 'Hola profe', 'Problema'], 'ayuda': 'Que se entienda sin abrir el mail.'},
     {'cons': 'Le escribís al club para inscribirte en vóley.', 'ops': ['Inscripción a vóley: consulta', 'Quiero jugar', 'Hola, ¿cómo están?'], 'ayuda': 'Tema y motivo en pocas palabras.'},
     {'cons': 'Le mandás a tu tutora el resumen que te pidió.', 'ops': ['Envío el resumen de Ciencias Naturales', 'Te mando algo', 'Importante!!!'], 'ayuda': 'Qué envías y de qué materia.'}]),
   ('Asunto', 'El asunto es la frase breve que resume de qué trata un mail; es lo primero que ve el destinatario y le permite saber qué es antes de abrirlo.'),
   'Un buen asunto es concreto: nombra el tema y, si corresponde, lo que se pide. «Hola» o «importante» no ayudan, porque no distinguen ese mail de cualquier otro. Pensá que quien lo recibe puede tener decenas de mensajes y va a elegir cuál leer primero por el asunto.',
   ['Concreto: tema y pedido.', 'Breve: pocas palabras.', 'Nada de «Hola» ni «URGENTE».']),
 T('Un cuerpo breve y claro',
   m('transformar', items=[
     {'nombre': 'La consulta', 'antes': 'Hola, bueno, nada, le escribo porque el otro día estaba haciendo la tarea y no entendí bien una parte que no sé si era para el lunes o el martes y además no me acuerdo cuál era el ejercicio.', 'pasos': [{'v': '{{Buenas tardes, profesora:}} le escribo porque no entendí bien una parte de la tarea.', 'txt': 'Saludo formal y motivo al principio.'}, {'v': 'Buenas tardes, profesora: le escribo porque no entendí bien la tarea. {{¿Es para el lunes o para el martes? ¿Qué ejercicio hay que hacer?}}', 'txt': 'Las dudas, ordenadas y concretas.'}, {'v': 'Buenas tardes, profesora: le escribo porque no entendí bien la tarea. ¿Es para el lunes o para el martes? ¿Qué ejercicio hay que hacer? {{Muchas gracias. Saludos, Camila Díaz.}}', 'txt': 'Cierre y firma.'}], 'cierre': 'Mismo mensaje: más corto y más claro.'}]),
   m('completar_x', consigna='Elegí la fórmula adecuada para un mail formal.', items=[
     {'texto': '[[Buenas tardes:/¡Ey!/Holaaa]] Le escribo para consultar por el horario de la biblioteca. [[Muchas gracias./Chau./Besos.]]', 'ayuda': 'Saludo y cierre corteses.'},
     {'texto': '[[Estimada profesora:/Che, profe:/Querida amiga:]] le envío adjunto el trabajo. [[Saludos cordiales./Nos vemos./Abrazo.]]', 'ayuda': 'Es para una profesora.'}]),
   ('Cuerpo del mail', 'El cuerpo del mail es el mensaje principal: debe ir al punto, explicar el motivo al principio y ordenar los pedidos o las preguntas de manera clara.'),
   'Un mail formal no es una charla: conviene decir para qué se escribe en la primera oración y, si hay varias preguntas, separarlas. Antes de enviarlo, una relectura rápida permite revisar que no falte el adjunto, que la dirección sea la correcta y que no haya errores.',
   ['El motivo en la primera oración.', 'Preguntas ordenadas y concretas.', 'Releer antes de enviar.'])],
 'recuerda': [
   R('Mail', 'es un mensaje escrito enviado por internet con campos fijos: destinatario, asunto, cuerpo y adjunto.', 'Para: secretaria@clubsur.org.ar'),
   R('Asunto', 'es la frase breve que resume de qué trata el mail y se ve antes de abrirlo.', 'Inscripción a vóley: consulta'),
   R('Adjunto', 'es el archivo que se envía junto con el mail y que hay que revisar antes de enviarlo.', 'el trabajo de Historia en PDF'),
   R('Cuerpo del mail', 'es el mensaje principal: va al punto y explica el motivo al principio.', '¿Es para el lunes o para el martes?')]}

L['3'] = {'temas': [
 T('Qué es un formulario',
   m('formato', items=[
     {'tipo': 'un formulario de inscripción', 'partes': [['Título', 'Inscripción a la colonia de verano 2026', 'font-weight:700', 'Dice para qué sirve.'], ['Instrucciones', 'Completar con letra clara. Los campos con * son obligatorios.', 'font-size:90%', 'Cómo completarlo: se lee primero.'], ['Datos personales', 'Apellido y nombre*: ____ · DNI*: ____ · Fecha de nacimiento* (dd/mm/aaaa): __/__/____', '', 'Campos que piden datos exactos.'], ['Datos de contacto', 'Teléfono*: ____ · Correo electrónico: ____', '', 'Algunos obligatorios, otros opcionales.'], ['Opciones', '☐ Turno mañana ☐ Turno tarde', '', 'Casillas para marcar.'], ['Firma', 'Firma del adulto responsable: ____', '', 'Confirma que los datos son verdaderos.']]}]),
   m('clasificar_x', consigna='Según el formulario, ¿el campo es obligatorio u opcional?', cajas=['Obligatorio (*)', 'Opcional'], cuantos=6, items=[
     ['Apellido y nombre*', 0], ['DNI*', 0], ['Fecha de nacimiento*', 0], ['Teléfono*', 0], ['Segundo teléfono', 1], ['Correo electrónico', 1], ['Observaciones', 1], ['Apodo', 1]]),
   ('Formulario', 'El formulario es un texto con espacios, llamados campos, que se completan con datos personales para hacer un trámite, una inscripción o un pedido.'),
   'Antes de escribir nada, se leen las instrucciones: ahí se explica qué campos son obligatorios, con qué formato van los datos y si hay que usar mayúsculas. Un formulario mal completado puede hacer que una inscripción no se acepte.',
   ['Primero, leer las instrucciones.', 'El asterisco (*) marca lo obligatorio.', 'Cada campo pide un dato exacto.']),
 T('Datos exactos y formatos',
   m('marcar', rotulo='Formulario', items=[
     {'nombre': 'Bien completado', 'texto': 'Apellido y nombre: {{GÓMEZ, SOFÍA|Primero el apellido, como pide el campo, en mayúsculas.}} · DNI: {{48123456|Sin puntos, si así lo indican.}} · Fecha de nacimiento: {{07/03/2013|Formato dd/mm/aaaa: dos cifras, dos cifras, cuatro cifras.}} · Correo: {{sofia.gomez@mail.com|Sin espacios ni errores.}}', 'cierre': 'Cada dato, en el formato que se pide.'},
     {'nombre': 'Con errores', 'texto': 'Apellido y nombre: {{Sofi|Falta el apellido y usa apodo.}} · DNI: {{no me acuerdo|Un campo obligatorio sin el dato.}} · Fecha de nacimiento: {{7 de marzo|No respeta el formato pedido.}}', 'cierre': 'Este formulario sería rechazado.'}]),
   m('completar_x', consigna='Elegí cómo se completa cada campo.', items=[
     {'texto': 'Fecha de nacimiento (dd/mm/aaaa): [[15/09/2012/15 de septiembre/septiembre 2012]]', 'ayuda': 'Dos cifras, dos cifras y cuatro cifras.'},
     {'texto': 'Apellido y nombre: [[PÉREZ, JUAN/Juan/Juancito P.]]', 'ayuda': 'Apellido primero y sin apodos.'},
     {'texto': 'Edad (en números): [[13/trece/13 años y medio]]', 'ayuda': 'Pide números.'}]),
   ('Datos exactos', 'Completar un formulario con datos exactos es escribir cada dato completo, verdadero y en el formato que pide el campo, sin apodos ni abreviaturas.'),
   'Los formularios suelen procesarse rápido y a veces por computadora: si una fecha no tiene el formato correcto o falta un dato obligatorio, el trámite se traba. Por eso hay que respetar las indicaciones aunque parezcan detalles, como el orden de apellido y nombre o el uso de mayúsculas.',
   ['Completo y verdadero.', 'En el formato pedido.', 'Sin apodos ni abreviaturas.']),
 T('Revisar antes de enviar',
   m('revision', items=[
     {'nombre': 'La inscripción', 'borrador': 'Apellido y nombre: Martina · DNI: — · Fecha de nacimiento: 3/5 · Turno: ☑ mañana ☑ tarde · Firma: —', 'criterios': [['Están todos los campos obligatorios', False, 'faltan el DNI y la firma'], ['El nombre está completo', False, 'falta el apellido'], ['La fecha respeta el formato', False, 'falta el año'], ['Las opciones son coherentes', False, 'marcó los dos turnos']],
      'final': 'Apellido y nombre: LÓPEZ, MARTINA · DNI: 49876543 · Fecha de nacimiento: 03/05/2013 · Turno: ☑ mañana · Firma: (del adulto responsable)'}]),
   m('marcar_x', consigna='Tocá los datos que están mal completados.', items=[
     {'cons': 'Formulario de inscripción a un taller.', 'texto': '[[Apellido y nombre: ROJAS, TOMÁS|0]] · [[DNI: no sé|1]] · [[Fecha de nacimiento: 12/10/2012|0]] · [[Teléfono: el de mi mamá|1]] · [[Correo: tomas.rojas@mail.com|0]]'},
     {'cons': 'Formulario de préstamo de la biblioteca.', 'texto': '[[Nombre: Cami|1]] · [[DNI: 47555222|0]] · [[Fecha: ayer|1]] · [[Libro: Corazón, de Edmondo De Amicis|0]]'}]),
   ('Revisión del formulario', 'Revisar un formulario es releerlo antes de enviarlo para comprobar que no falten campos obligatorios y que cada dato esté completo y bien escrito.'),
   'Un formulario no se puede corregir una vez entregado, así que la revisión final es clave. Conviene repasar campo por campo con preguntas simples: ¿está?, ¿está completo?, ¿respeta el formato?, ¿es coherente con lo demás?',
   ['¿Están todos los obligatorios?', '¿Cada dato está completo y en formato?', '¿Las opciones marcadas son coherentes?'])],
 'recuerda': [
   R('Formulario', 'es un texto con campos que se completan con datos para hacer un trámite o una inscripción.', 'Inscripción a la colonia de verano'),
   R('Campo', 'es cada espacio del formulario donde se escribe un dato determinado.', 'DNI: 48123456, escrito sin puntos'),
   R('Campo obligatorio', 'es el que no se puede dejar vacío y suele estar marcado con un asterisco.', 'Apellido y nombre*'),
   R('Formato del dato', 'es la forma exacta en que hay que escribir un dato, como la fecha en dd/mm/aaaa.', 'Fecha de nacimiento: 07/03/2013'),
   R('Revisión del formulario', 'es releerlo campo por campo antes de enviarlo, porque después no se puede corregir.', 'Falta el DNI: completarlo')]}

L['4'] = {'temas': [
 T('Los registros',
   m('versiones', rotulo='Registro', items=[
     {'nombre': 'Formal', 'texto': '{{¿Podría indicarme el horario de atención, por favor?|Formal: trato de usted, fórmulas de cortesía.}}'},
     {'nombre': 'Neutro', 'texto': '{{¿Cuál es el horario de atención?|Neutro: claro y correcto, sin marcas de confianza ni de distancia.}}'},
     {'nombre': 'Informal', 'texto': '{{Che, ¿a qué hora abren?|Informal: cercano, con palabras de todos los días.}}'}]),
   m('clasificar_x', consigna='¿Qué registro tiene cada frase?', cajas=['Formal', 'Informal'], cuantos=6, items=[
     ['Le solicito que me informe la fecha del examen.', 0], ['Agradecería su pronta respuesta.', 0], ['Me dirijo a ustedes para consultar…', 0],
     ['Pasame la tarea, porfa.', 1], ['¿Qué onda con lo de mañana?', 1], ['Bancame que ya te contesto.', 1]]),
   ('Registro', 'El registro es la manera de usar la lengua según la situación y el destinatario: formal, neutro o informal.'),
   'Todos manejamos varios registros y pasamos de uno a otro sin darnos cuenta: no hablamos igual con un amigo que con una médica. El registro formal usa trato de usted y fórmulas de cortesía; el informal, palabras cotidianas y trato de vos; el neutro, un lenguaje claro que sirve para casi cualquier lector.',
   ['Formal: usted y cortesía.', 'Neutro: claro, sin marcas.', 'Informal: vos y lenguaje cotidiano.']),
 T('Adecuar el mensaje al destinatario',
   m('transformar', items=[
     {'nombre': 'Al club', 'antes': 'Che, ¿cuánto sale la cuota? Pasame el dato.', 'pasos': [{'v': '{{Buenas tardes.}} ¿Cuánto sale la cuota? Pasame el dato.', 'txt': 'Un saludo adecuado.'}, {'v': 'Buenas tardes. {{Quisiera saber cuál es el valor de la cuota mensual.}}', 'txt': 'El pedido con cortesía y sin «che».'}, {'v': 'Buenas tardes. Quisiera saber cuál es el valor de la cuota mensual. {{Muchas gracias.}}', 'txt': 'Un cierre cordial.'}], 'cierre': 'El mismo pedido, adecuado a una institución.'}]),
   m('transformar_x', consigna='Pasá cada mensaje a un registro formal.', items=[
     {'cons': 'Escribilo para la secretaria de la escuela, sin «che» ni «pasame».', 'texto': 'Che, pasame el horario de los exámenes.', 'pide': ['podría|podrían|quisiera|solicito|agradecería|le pido'], 'prohibe': ['che', 'pasame']},
     {'cons': 'Escribilo para el encargado de la biblioteca, con trato de usted.', 'texto': '¿Me guardás el libro hasta el lunes?', 'pide': ['podría|puede|quisiera|solicito|agradecería'], 'prohibe': ['guardás']}]),
   ('Adecuación', 'La adecuación es la elección del registro, las palabras y el tono que corresponden al destinatario y a la situación, para que el mensaje cumpla su propósito.'),
   'Un pedido informal a una institución puede parecer una falta de respeto y quedar sin respuesta; uno demasiado formal con un amigo suena raro. Antes de escribir, conviene preguntarse a quién le escribo, qué relación tengo con esa persona y qué quiero lograr.',
   ['¿A quién le escribo?', '¿Qué relación tengo con esa persona?', '¿Qué quiero lograr?']),
 T('Fórmulas de tratamiento',
   m('marcar', rotulo='Mensaje', items=[
     {'nombre': 'A una autoridad', 'texto': '{{Sra. Directora:|Abreviatura de «señora» y el cargo: trato respetuoso.}} {{Me dirijo a usted|Pronombre «usted»: distancia y respeto.}} para solicitarle una reunión. {{Quedo a su disposición.|Fórmula de cortesía.}}', 'cierre': 'Fórmulas que muestran respeto.'},
     {'nombre': 'A un amigo', 'texto': '{{Juan:|Solo el nombre.}} {{¿Vos podés|Trato de «vos»: confianza.}} el sábado? {{Avisame.|Pedido directo, sin fórmulas.}}', 'cierre': 'La confianza permite ir al punto.'}]),
   m('elegir_x', consigna='¿Qué fórmula de tratamiento corresponde?', items=[
     {'cons': 'Un mail al presidente de un club al que no conocés.', 'ops': ['Sr. Presidente: me dirijo a usted…', 'Hola, presi, ¿cómo andás?', 'Che, una pregunta…'], 'ayuda': 'No lo conocés y tiene un cargo.'},
     {'cons': 'Un mensaje a tu prima para invitarla al cine.', 'ops': ['Lu, ¿venís al cine el viernes?', 'Estimada señora: me dirijo a usted…', 'De mi mayor consideración:'], 'ayuda': 'Es alguien de confianza.'},
     {'cons': 'Una nota a la médica del centro de salud.', 'ops': ['Dra. Ruiz: le escribo para consultarle…', 'Ey, doc…', 'Querida amiga:'], 'ayuda': '«Dra.» es la abreviatura de doctora.'}]),
   ('Fórmulas de tratamiento', 'Las fórmulas de tratamiento son las expresiones que se usan para dirigirse a alguien según la relación, como usted o vos, señor o señora, y títulos como doctora o profesor.'),
   'Con autoridades y desconocidos se usa usted y, muchas veces, el cargo o el título abreviado: Sr., Sra., Dr., Dra., Prof. Con personas de confianza alcanzan el nombre y el vos. Usar la fórmula correcta desde el saludo marca el tono de todo el mensaje.',
   ['Usted: distancia y respeto.', 'Vos: confianza.', 'Títulos abreviados: Sr., Sra., Dr., Prof.'])],
 'recuerda': [
   R('Registro', 'es la manera de usar la lengua según la situación y el destinatario: formal, neutro o informal.', '¿Podría indicarme…? / Che, ¿a qué hora…?'),
   R('Registro formal', 'usa trato de usted, fórmulas de cortesía y palabras cuidadas.', 'Le solicito que me informe…'),
   R('Registro informal', 'usa trato de vos y palabras cotidianas, con personas de confianza.', 'Pasame la tarea, porfa'),
   R('Adecuación', 'es elegir el registro y el tono según el destinatario y lo que se quiere lograr.', 'Che, ¿cuánto sale? → Quisiera saber el valor'),
   R('Fórmulas de tratamiento', 'son las expresiones para dirigirse a alguien según la relación, como usted, señor o doctora.', 'Sra. Directora: me dirijo a usted')]}

A = {
 '1': [
   ORD('Ordená las partes de la carta.', ['Lugar y fecha', 'Destinatario', 'Saludo', 'Cuerpo', 'Despedida', 'Firma'], 'La estructura fija de la carta.', 'aplicar'),
   CLA('¿Expresión formal o informal?', ['Formal', 'Informal'], [('De mi mayor consideración:', 'Formal'), ('¡Hola, amigo!', 'Informal'), ('Lo saludo atentamente.', 'Formal'), ('¡Un beso enorme!', 'Informal')], 'Pensá a quién se le diría cada una.', 'aplicar'),
   MC('Una carta a la municipalidad dice: «Arreglen la plaza que está horrible». ¿Qué le falta para ser un buen reclamo?', ['Datos concretos y un pedido respetuoso', 'Muchos signos de exclamación juntos', 'Un dibujo grande de la plaza rota'], 'Datos concretos y un pedido respetuoso', 'Un reclamo eficaz es claro y respetuoso.', 'error'),
   KW('Escribí el comienzo de una carta formal al encargado de un museo para pedir una visita guiada: saludo y primera oración del cuerpo.', 'Saludo formal y motivo.', [['estimado', 'estimada', 'de mi consideración', 'de mi mayor consideración', 'señor', 'señora', 'sr.', 'sra.'], ['solicitar', 'solicito', 'pedir', 'quisiera', 'me dirijo', 'consultar'], ['visita']], 3, 'Por ejemplo: «De mi mayor consideración: me dirijo a usted para solicitar una visita guiada…».', 'aplicar')],
 '2': [
   UNI('Uní cada parte del mail con lo que va en ella.', [('Para', 'la dirección del destinatario'), ('Asunto', 'de qué trata, en pocas palabras'), ('Cuerpo', 'el mensaje con saludo y firma'), ('Adjunto', 'un archivo que acompaña')], 'Los campos del mail.', 'aplicar'),
   ODD('Tres asuntos son buenos y uno no. ¿Cuál no?', ['Consulta: horarios de natación', 'Envío el resumen de Historia', 'Hola', 'Pedido de prórroga del trabajo de Lengua'], 'Hola', '«Hola» no dice de qué trata el mail.', 'analizar'),
   MC('Mandaste el trabajo por mail y la profesora te responde que no le llegó nada. ¿Qué te olvidaste, seguramente?', ['Adjuntar el archivo', 'Poner el asunto en mayúsculas', 'Escribir en registro informal'], 'Adjuntar el archivo', 'Antes de enviar, se revisa el adjunto.', 'analizar'),
   TAP('Tocá las DOS partes que no corresponden en este mail a una profesora: «Ey, profe: le mando el trabajo de Lengua. Besotes.»', ['Ey, profe:', 'le mando', 'el trabajo', 'de Lengua.', 'Besotes.'], [0, 4], 'Saludo y despedida demasiado informales para una profesora.', 'error')],
 '3': [
   CLA('¿Dato bien o mal completado? (Fecha en dd/mm/aaaa, apellido primero)', ['Bien', 'Mal'], [('Fecha: 09/04/2013', 'Bien'), ('Fecha: abril', 'Mal'), ('Apellido y nombre: SUÁREZ, ANA', 'Bien'), ('Apellido y nombre: Anita', 'Mal')], 'Datos completos y en formato.', 'aplicar'),
   ORD('Ordená los pasos para completar un formulario.', ['Leer las instrucciones', 'Completar los campos obligatorios', 'Revisar cada dato', 'Firmar y enviar'], 'Leer, completar, revisar y firmar.', 'aplicar'),
   MC('Un formulario dice «Edad (en números)». ¿Cómo se completa?', ['13', 'trece', 'tengo trece años'], '13', 'Se respeta el formato que pide el campo.', 'aplicar'),
   MC('Bruno dejó vacío el campo «DNI*» porque no se lo sabía de memoria. ¿Qué pasa?', ['Es un campo obligatorio: el formulario puede ser rechazado', 'No pasa nada: los campos con asterisco son opcionales', 'Se completa solo'], 'Es un campo obligatorio: el formulario puede ser rechazado', 'El asterisco marca lo obligatorio.', 'error')],
 '4': [
   CLA('¿Qué registro tiene cada frase?', ['Formal', 'Informal'], [('¿Podría enviarme la información?', 'Formal'), ('Mandame la info, porfa', 'Informal'), ('Agradezco su atención.', 'Formal'), ('¡Grosso, gracias!', 'Informal')], 'Usted y cortesía, o vos y lenguaje cotidiano.', 'aplicar'),
   UNI('Uní cada destinatario con el saludo adecuado.', [('La directora de la escuela', 'Sra. Directora:'), ('Tu mejor amiga', '¡Hola, Juli!'), ('Un médico', 'Dr. Martínez:'), ('Una empresa que no conocés', 'De mi consideración:')], 'La relación decide la fórmula.', 'aplicar'),
   MC('Le escribís al encargado del club: «Che, ¿me guardás un lugar en el torneo?». ¿Qué cambio lo adecua mejor?', ['«Buenas tardes, ¿podría reservarme un lugar?»', '«Che, porfa, guardame un lugar ya mismo.»', '«¡¡¡Quiero un lugar en ese torneo!!!»'], '«Buenas tardes, ¿podría reservarme un lugar?»', 'Saludo, usted y cortesía.', 'aplicar'),
   MC('Sofía le escribe a su abuela «De mi mayor consideración: me dirijo a usted…». ¿Qué problema tiene?', ['Es demasiado formal para alguien de confianza', 'Está muy bien: siempre hay que ser formal', 'Le falta el asunto'], 'Es demasiado formal para alguien de confianza', 'La adecuación también evita el exceso de formalidad.', 'error')],
 '5': [
   CLA('¿Qué texto corresponde a cada situación?', ['Carta formal', 'Mail', 'Formulario'], [('Pedirle por escrito al intendente que arregle un semáforo', 'Carta formal'), ('Mandarle el trabajo a la profesora con un archivo', 'Mail'), ('Inscribirse en la colonia de verano', 'Formulario'), ('Consultar rápido al club por un horario', 'Mail')], 'Cada situación pide un texto distinto.', 'analizar'),
   ORD('Ordená las partes del cuerpo de un mail formal.', ['Saludo', 'Motivo del mail', 'Detalle o preguntas', 'Agradecimiento', 'Firma'], 'Del saludo a la firma.', 'aplicar'),
   MS('Querés pedirle a la municipalidad que pongan un tacho de basura en la plaza. Elegí las DOS cosas que tiene que tener tu carta.', ['Datos concretos: qué plaza y por qué', 'Un pedido claro y respetuoso', 'Palabras como «che» y «porfa»', 'Un asunto que diga «URGENTE!!!»'], ['Datos concretos: qué plaza y por qué', 'Un pedido claro y respetuoso'], 'Claridad y respeto.'),
   MC('¿Qué error tiene este formulario? «Apellido y nombre: Tomi · Fecha: 3/5»', ['Falta el apellido y la fecha está incompleta', 'Está todo bien', 'Tiene demasiados datos'], 'Falta el apellido y la fecha está incompleta', 'Datos completos y en formato.', 'analizar')],
}

EX = [
 [1, ORD('Ordená las partes de la carta formal.', ['Lugar y fecha', 'Saludo', 'Cuerpo', 'Despedida', 'Firma'], 'La estructura de la carta.', 'aplicar')],
 [1, CLA('¿Formal o informal?', ['Formal', 'Informal'], [('Me dirijo a usted para…', 'Formal'), ('¡Hola, che!', 'Informal'), ('Lo saludo atentamente.', 'Formal')], 'La relación con el destinatario.', 'aplicar')],
 [1, MC('¿Qué tiene un buen reclamo por escrito?', ['El problema con datos y un pedido claro y respetuoso', 'Muchos insultos para que se note el enojo', 'Solo la firma'], 'El problema con datos y un pedido claro y respetuoso', 'Así el pedido tiene resultado.', 'analizar')],
 [2, UNI('Uní cada campo del mail con su función.', [('Para', 'a quién se envía'), ('Asunto', 'de qué trata'), ('Adjunto', 'un archivo que acompaña')], 'Los campos fijos del mail.', 'aplicar')],
 [2, MC('¿Cuál es el mejor asunto para pedir una prórroga del trabajo de Historia?', ['Prórroga del trabajo de Historia', 'Hola profe, una cosita', 'URGENTE, leer ya mismo'], 'Prórroga del trabajo de Historia', 'Tema y pedido en pocas palabras.', 'aplicar')],
 [2, TF('Antes de enviar un mail conviene revisar el adjunto y la dirección del destinatario.', 'Verdadero', 'Una relectura evita errores difíciles de corregir.', 'recordar')],
 [3, SA('En un formulario, ¿qué signo suele marcar los campos obligatorios?', ['asterisco', 'el asterisco', '*', 'un asterisco'], 'El asterisco (*).', 'recordar')],
 [3, CLA('¿Bien o mal completado? (Fecha en dd/mm/aaaa)', ['Bien', 'Mal'], [('15/08/2012', 'Bien'), ('15 de agosto', 'Mal'), ('agosto', 'Mal')], 'El formato pedido.', 'aplicar')],
 [3, MC('¿Por qué es importante revisar un formulario antes de entregarlo?', ['Porque después no se puede corregir y puede ser rechazado', 'Porque así se ve más lindo', 'Porque los formularios no tienen instrucciones'], 'Porque después no se puede corregir y puede ser rechazado', 'La revisión final evita trabas.', 'analizar')],
 [4, CLA('¿Formal o informal?', ['Formal', 'Informal'], [('¿Podría informarme…?', 'Formal'), ('Pasame la data', 'Informal'), ('Agradecería su respuesta', 'Formal')], 'Usted y cortesía, o vos y lenguaje cotidiano.', 'aplicar')],
 [4, UNI('Uní cada destinatario con el saludo adecuado.', [('Una doctora', 'Dra. Pérez:'), ('Tu primo', '¡Hola, Nacho!'), ('La directora', 'Sra. Directora:')], 'La fórmula de tratamiento según la relación.', 'aplicar')],
 [4, MC('¿Qué es la adecuación?', ['Elegir el registro y el tono según el destinatario y la situación', 'Escribir siempre lo más formal posible', 'Usar solo palabras difíciles'], 'Elegir el registro y el tono según el destinatario y la situación', 'Ni de más ni de menos.', 'recordar')],
 [4, KW('Reescribí en registro formal este mensaje para la secretaría de la escuela: «Che, ¿me pasás el horario de los exámenes?»', 'Saludo, usted y cortesía.', [['buenas', 'buen día', 'estimad*', 'señor*', 'sra', 'sr'], ['podría', 'podrían', 'quisiera', 'solicito', 'agradecería', 'le pido'], ['horario']], 3, 'Por ejemplo: «Buenas tardes. ¿Podría informarme el horario de los exámenes? Muchas gracias».', 'aplicar')],
]

def ajustes(M):
    M['act'] = A
    M['examen'] = EX
    M['practica'] = 'Actividades generales'
    M['actualizar_preguntas'] = True

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-10/mision-10.json', L, ajustes=ajustes)
