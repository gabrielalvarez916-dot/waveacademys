# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 1 · La comunicación y el lenguaje (TODO nuevo: 4 clases animadas, lección, actividades, generales y examen)
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD
RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', '..')

# ============================ CLASES ANIMADAS ============================
STEP = {'1': '766837fd-f800-48a1-b11f-57f3dc3c4e91', '2': 'e969a044-144e-4bab-afb6-eba01650594e', '3': '2c60844b-9366-4fd2-9030-09182b5a8160', '4': 'f2d9ec97-73bc-45e2-ada0-f517606d334a'}
TIT = {'1': 'El circuito de la comunicación', '2': 'Texto y contexto', '3': 'Funciones del lenguaje', '4': 'Códigos verbales y no verbales'}
CL = {}
CL['1'] = [
 {'t': 'chat', 'contacto': {'nombre': 'Mamá', 'emoji': '👩'}, 'mensajes': [{'yo': False, 'txt': '¿Comiste?'}, {'yo': True, 'txt': 'Sí 👍'}, {'yo': False, 'txt': 'Bien. Llego a las 8'}], 'titulo': 'COMUNICARNOS', 'sub': 'todo el tiempo',
  'voz': ['Mamá te escribe: *¿comiste?*', 'Vos contestás con un sí y un pulgar.', 'Ella avisa a qué hora llega.', 'En diez segundos se *comunicaron* dos personas. Hoy vemos cómo funciona eso.']},
 {'t': 'definicion', 'palabra': 'Comunicación', 'texto': 'Intercambio de información entre personas mediante un código que todos comparten.', 'emoji': '🔄',
  'voz': ['Comunicarse es *intercambiar información* entre personas.', 'Para que funcione, tienen que compartir un mismo *código*, como el idioma.']},
 {'t': 'flujo', 'titulo': 'EL CIRCUITO', 'items': ['Emisor', 'Mensaje', 'Receptor'],
  'voz': ['El *emisor* es quien produce el mensaje: en el chat, tu mamá.', 'El *mensaje* es lo que se dice: ¿comiste?', 'El *receptor* es quien lo recibe e interpreta: vos.']},
 {'t': 'bloques', 'titulo': 'Y ADEMÁS…', 'items': [{'cab': 'Código', 'txt': 'el idioma español escrito'}, {'cab': 'Canal', 'txt': 'el celular, por internet'}, {'cab': 'Referente', 'txt': 'de qué se habla: la comida'}, {'cab': 'Contexto', 'txt': 'mediodía, ella en el trabajo'}],
  'voz': ['Pero hay más elementos.', 'El *código*: el sistema de signos. Acá, el español escrito.', 'El *canal*: el medio físico por donde viaja. Acá, el celular.', 'El *referente*: de qué se habla. La comida.', 'Y el *contexto*: la situación. Es mediodía y ella está trabajando.']},
 {'t': 'frase', 'texto': '¿Y si se corta internet?', 'emoji': '📵', 'color': '#F4B63F', 'voz': ['Ahora imaginá que justo se corta internet. ¿Qué pasa con el mensaje?']},
 {'t': 'definicion', 'palabra': 'Ruido', 'texto': 'Todo lo que interfiere y hace que el mensaje no llegue o llegue mal.', 'emoji': '📶',
  'voz': ['Eso es un *ruido*: cualquier cosa que interfiere en la comunicación.', 'Puede ser técnico, como mala señal, o del código, como una palabra que no conocés.']},
 {'t': 'clasificar', 'cajas': [{'cab': 'Ruido del canal', 'emoji': '📶'}, {'cab': 'Ruido del código', 'emoji': '🔤'}], 'fichas': [{'txt': 'audio cortado', 'caja': 0}, {'txt': 'pantalla trabada', 'caja': 0}, {'txt': 'otro idioma', 'caja': 1}, {'txt': 'sigla rara', 'caja': 1}],
  'voz': ['Separemos: unos ruidos vienen del *canal* y otros del *código*.', 'Audio entrecortado o pantalla congelada: falla el canal.', 'Una palabra en otro idioma o una sigla desconocida: falla el código.']},
 {'t': 'vof', 'afirmacion': 'En una videollamada, el emisor y el receptor nunca cambian de lugar.', 'emoji': '💻', 'verdadero': False, 'explicacion': 'Se turnan: cuando contestás, pasás a ser emisor.',
  'voz': ['Verdadero o falso: en una videollamada, emisor y receptor nunca cambian.', 'Pensalo.', 'Falso: cuando vos respondés, pasás a ser *emisor*. Los papeles se turnan.']},
 {'t': 'errores', 'items': [{'mal': 'El canal es el idioma', 'bien': 'El canal es el medio: celular, aire, papel'}, {'mal': 'El referente es quien habla', 'bien': 'El referente es de qué se habla'}],
  'voz': ['Dos confusiones típicas.', 'El canal no es el idioma: el idioma es el *código*; el canal es el medio.', 'Y el referente no es una persona: es el *tema* del mensaje.']},
 {'t': 'resumen', 'items': [['Emisor y receptor', 'quien produce y quien interpreta'], ['Mensaje', 'lo que se dice'], ['Código y canal', 'el sistema de signos y el medio'], ['Referente y contexto', 'de qué se habla y en qué situación'], ['Ruido', 'lo que interfiere']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 1'},
  'voz': ['Repasemos el circuito.', 'Siete elementos y un enemigo.', 'Emisor y receptor.', 'El mensaje.', 'Código y canal.', 'Referente y contexto.', 'Y el ruido, que lo interrumpe. ¡A practicar!']},
]
CL['2'] = [
 {'t': 'historia', 'personaje': {'nombre': 'Tomi', 'emoji': '👦'}, 'lugar': '🏠', 'lineas': ['Tomi escribe «¡qué genio!»', 'A su amigo, que hizo un gol.', 'Y a su hermano, que rompió la tele.'], 'titulo': 'LA MISMA FRASE', 'sub': 'dos sentidos',
  'voz': ['Tomi escribe *¡qué genio!*', 'Se lo manda a su amigo, que acaba de hacer un gol.', 'Y se lo manda a su hermano, que rompió la tele.', 'Mismas palabras, sentidos opuestos. ¿Qué cambió? El *contexto*.']},
 {'t': 'definicion', 'palabra': 'Texto', 'texto': 'Unidad de comunicación completa, oral o escrita, que tiene una intención y se entiende en una situación.', 'emoji': '📝',
  'voz': ['Un *texto* es cualquier unidad de comunicación completa, oral o escrita.', 'Un chat, un aviso o un cuento: todos son textos, porque buscan algo y se entienden en una situación.']},
 {'t': 'matriz', 'titulo': 'LA SITUACIÓN COMUNICATIVA', 'celdas': [{'cab': '¿Quién?', 'txt': 'el emisor'}, {'cab': '¿A quién?', 'txt': 'el destinatario'}, {'cab': '¿Dónde y cuándo?', 'txt': 'el lugar y el momento'}, {'cab': '¿Para qué?', 'txt': 'la intención'}],
  'voz': ['El contexto se arma con cuatro preguntas.', '¿Quién habla?', '¿A quién le habla?', '¿Dónde y cuándo?', 'Y la más importante: *¿para qué?*']},
 {'t': 'tabla', 'titulo': 'INTENCIONES', 'columnas': ['Intención', 'Ejemplo'], 'filas': [['Informar', 'Mañana no hay clases'], ['Convencer', 'Votá por mi lista'], ['Pedir', '¿Me prestás el cargador?'], ['Expresar', '¡Qué nervios tengo!']],
  'voz': ['Cada texto tiene una *intención*.', 'Informar: dar un dato.', 'Convencer: que el otro piense como vos.', 'Pedir: que el otro haga algo.', 'Expresar: mostrar lo que sentís.']},
 {'t': 'comparar', 'a': {'cab': 'A la directora', 'texto': 'Estimada directora: le escribo para solicitar…', 'emoji': '🏫'}, 'b': {'cab': 'A un amigo', 'texto': 'Che, ¿me pasás la tarea?', 'emoji': '🧑'}, 'signo': '≠',
  'voz': ['Mismo pedido, distinto destinatario.', 'A la directora, un texto cuidado y respetuoso.', 'A un amigo, uno corto e informal. El contexto *cambia cómo escribimos*.']},
 {'t': 'dilema', 'situacion': 'Le querés avisar a tu profe que no vas a poder entregar la tarea.', 'emoji': '✉️', 'a': {'txt': '«ntp mañana la mando»', 'consecuencia': 'no se entiende y suena descortés', 'emoji': '😬'}, 'b': {'txt': '«Profe, no llego a entregarla hoy. ¿Puedo mandarla mañana?»', 'consecuencia': 'se entiende y queda bien', 'emoji': '👍'},
  'voz': ['Tenés que avisarle a tu profe que no llegás con la tarea.', 'Opción A: ntp mañana la mando. No se entiende y suena descortés.', 'Opción B: un mensaje claro y amable. Eso es *tener en cuenta el contexto*.']},
 {'t': 'quiz4', 'pregunta': '«¿Me abrís la puerta?» ¿Qué intención tiene?', 'opciones': ['Informar', 'Pedir', 'Expresar', 'Convencer'], 'correcta': 1,
  'voz': ['Rápido: *¿me abrís la puerta?* ¿Qué intención tiene?', 'Pensá qué quiere lograr quien habla.', '*Pedir*: quiere que el otro haga algo.']},
 {'t': 'resumen', 'items': [['Texto', 'unidad completa con intención'], ['Contexto', 'quién, a quién, dónde, cuándo'], ['Intención', 'informar, convencer, pedir, expresar'], ['Adecuarse', 'el contexto cambia cómo decimos']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 2'},
  'voz': ['Resumen.', 'Un texto es una unidad completa con una intención.', 'Texto.', 'Contexto.', 'Intención.', 'Y adecuarse: según el contexto, cambia cómo lo decimos.']},
]
CL['3'] = [
 {'t': 'reto', 'texto': '«¡Uy, qué frío!» ¿Para qué sirve esta frase?', 'segundos': 5, 'respuesta': 'Para expresar lo que sentís', 'emoji': '🥶', 'titulo': 'PARA QUÉ HABLAMOS', 'sub': 'funciones',
  'voz': ['Reto: *¡uy, qué frío!* ¿Para qué sirve esta frase?', 'Cinco segundos.', 'Sirve para *expresar* lo que sentís. Esa es una función del lenguaje.']},
 {'t': 'definicion', 'palabra': 'Función del lenguaje', 'texto': 'Para qué se usa el lenguaje en un mensaje: informar, expresar, ordenar, jugar con las palabras…', 'emoji': '🎯',
  'voz': ['Una *función del lenguaje* es el uso que le damos en un mensaje.', 'Un mismo idioma sirve para informar, expresar, ordenar o jugar con las palabras.']},
 {'t': 'versus', 'a': {'txt': 'Referencial', 'emoji': '📊', 'datos': ['informa datos', 'objetiva', '«Hoy hace 3 grados»']}, 'b': {'txt': 'Expresiva', 'emoji': '😍', 'datos': ['muestra emociones', 'subjetiva', '«¡Me muero de frío!»']}, 'gana': 'empate', 'veredicto': 'Mismo tema, distinta función',
  'voz': ['Cara a cara: la función *referencial*, que informa datos de manera objetiva.', 'Contra la *expresiva*, que muestra lo que siente quien habla.', 'Hoy hace tres grados, contra: ¡me muero de frío!', 'Mismo tema, distinta función.']},
 {'t': 'bloques', 'titulo': 'DOS FUNCIONES MÁS', 'items': [{'cab': 'Apelativa', 'txt': 'busca que el otro haga algo: «Abrigate»'}, {'cab': 'Poética', 'txt': 'juega con la forma: «Frío, frío, como el agua del río»'}],
  'voz': ['Dos funciones más.', 'La *apelativa*: busca que el otro haga algo. Abrigate.', 'La *poética*: pone el foco en cómo suena y se ve el mensaje, como en las rimas y las canciones.']},
 {'t': 'bloques', 'titulo': 'Y DOS QUE PASAN DESAPERCIBIDAS', 'items': [{'cab': 'Fática', 'txt': 'abre o controla el canal: «¿Me escuchás?»'}, {'cab': 'Metalingüística', 'txt': 'habla del idioma: «¿Frío lleva tilde?»'}],
  'voz': ['Y dos que usamos sin darnos cuenta.', 'La *fática*: sirve para abrir o comprobar el canal. ¿Me escuchás? en una videollamada.', 'La *metalingüística*: usa el idioma para hablar del idioma. ¿Frío lleva tilde?']},
 {'t': 'datoloco', 'texto': 'Un mismo mensaje puede tener varias funciones a la vez, pero siempre hay una que manda.', 'emoji': '🤯',
  'voz': ['¿Sabías que un mensaje puede tener varias funciones a la vez?', 'Pero siempre hay una que *predomina*: la que explica para qué se dijo.']},
 {'t': 'unir', 'titulo': 'UNÍ', 'pares': [['«El tren sale a las 9»', 'referencial'], ['«¡Qué alegría verte!»', 'expresiva'], ['«Apagá la luz»', 'apelativa'], ['«¿Hola? ¿Se corta?»', 'fática']],
  'voz': ['Ahora uní cada frase con su función.', 'El tren sale a las nueve: informa, *referencial*.', 'Qué alegría verte: *expresiva*.', 'Apagá la luz: *apelativa*.', '¿Se corta?: controla el canal, *fática*.']},
 {'t': 'errores', 'items': [{'mal': 'Toda pregunta es apelativa', 'bien': '«¿Me escuchás?» es fática: controla el canal'}, {'mal': 'Solo los poemas tienen función poética', 'bien': 'También los eslóganes y las canciones'}],
  'voz': ['Ojo con dos errores.', 'No toda pregunta es apelativa: ¿me escuchás? es *fática*.', 'Y la poética no es solo de los poemas: aparece en eslóganes y canciones.']},
 {'t': 'resumen', 'items': [['Referencial', 'informa'], ['Expresiva', 'muestra emociones'], ['Apelativa', 'busca que el otro haga algo'], ['Poética', 'juega con la forma'], ['Fática', 'controla el canal'], ['Metalingüística', 'habla del idioma']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 3'},
  'voz': ['Las seis funciones.', 'Siempre preguntate: *¿para qué se dijo?*', 'Referencial.', 'Expresiva.', 'Apelativa.', 'Poética.', 'Fática.', 'Y metalingüística. ¡A practicar!']},
]
CL['4'] = [
 {'t': 'noticia', 'cinta': 'ÚLTIMO MOMENTO', 'titular': 'Un chat sin una sola palabra', 'bajada': 'Dos amigos se pusieron de acuerdo solo con emojis', 'emoji': '📱', 'titulo': 'SIN PALABRAS', 'sub': 'códigos no verbales',
  'voz': ['Último momento: dos amigos se pusieron de acuerdo para ir a la plaza sin escribir *una sola palabra*.', 'Solo con emojis: pelota, plaza, reloj, pulgar.', '¿Cómo puede ser? Porque además de las palabras hay *otros códigos*.']},
 {'t': 'comparar', 'a': {'cab': 'Código verbal', 'texto': 'usa palabras, orales o escritas', 'emoji': '🗣️'}, 'b': {'cab': 'Código no verbal', 'texto': 'usa imágenes, gestos, colores o sonidos', 'emoji': '🚦'}, 'signo': 'vs',
  'voz': ['El *código verbal* usa palabras: habladas o escritas.', 'El *no verbal* usa otros signos: imágenes, gestos, colores, sonidos.', 'Un semáforo no dice nada, pero todos lo entendemos.']},
 {'t': 'tabla', 'titulo': 'CÓDIGOS NO VERBALES', 'columnas': ['Tipo', 'Ejemplos'], 'filas': [['Visual', 'señales de tránsito, íconos'], ['Gestual', 'saludar con la mano, un pulgar'], ['Sonoro', 'una sirena, un timbre']],
  'voz': ['Los no verbales se agrupan según el sentido.', 'Visuales: señales e íconos.', 'Gestuales: el cuerpo y la cara.', 'Sonoros: una sirena, el timbre del recreo.']},
 {'t': 'definicion', 'palabra': 'Texto mixto', 'texto': 'Mensaje que combina palabras con imágenes, colores o sonidos para comunicar.', 'emoji': '🖼️',
  'voz': ['Muchos mensajes *combinan* los dos códigos.', 'Un afiche, un meme o un video con subtítulos son *textos mixtos*.']},
 {'t': 'clasificar', 'cajas': [{'cab': 'Verbal', 'emoji': '🔤'}, {'cab': 'No verbal', 'emoji': '🚦'}, {'cab': 'Mixto', 'emoji': '🖼️'}], 'fichas': [{'txt': 'un audio', 'caja': 0}, {'txt': 'una carta', 'caja': 0}, {'txt': 'un semáforo', 'caja': 1}, {'txt': 'un aplauso', 'caja': 1}, {'txt': 'un afiche', 'caja': 2}, {'txt': 'un meme', 'caja': 2}],
  'voz': ['Clasifiquemos.', 'Un audio y una carta: verbales.', 'Un semáforo y un aplauso: no verbales.', 'Un afiche con dibujo y texto, o un meme: mixtos.']},
 {'t': 'prediccion', 'pregunta': 'El emoji 🙏, ¿significa lo mismo en todo el mundo?', 'a': {'txt': 'Sí, es universal', 'emoji': '🌍'}, 'b': {'txt': 'No, depende de la cultura', 'emoji': '🤔'}, 'correcta': 'b', 'resultado': 'Para unos es «gracias», para otros «por favor» o un choque de manos.',
  'voz': ['¿Qué creés? El emoji de las manos juntas, ¿significa lo mismo en todos lados?', 'Pensalo.', 'No: para unos es gracias, para otros por favor. Los códigos no verbales también *dependen del contexto*.']},
 {'t': 'consejo', 'titulo': 'UN CONSEJO', 'texto': 'En mensajes importantes, no confíes solo en un emoji: aclaralo con palabras.', 'emoji': '💡',
  'voz': ['Un consejo: en un mensaje importante, no dejes todo en un emoji. Aclaralo con palabras.']},
 {'t': 'logro', 'titulo': '¡Misión cumplida!', 'items': ['El circuito de la comunicación', 'Texto, contexto e intención', 'Las funciones del lenguaje', 'Códigos verbales, no verbales y mixtos'], 'xp': 100,
  'voz': ['¡Terminaste la misión!', 'Ya conocés el circuito de la comunicación.', 'El texto, el contexto y la intención.', 'Las funciones del lenguaje.', 'Y los códigos verbales y no verbales. ¡A practicar!']},
]
for n, esc in CL.items():
    json.dump({'slug': f'leng1-m1-n{n}', 'step_id': STEP[n], 'materia': 'Lengua y Literatura I', 'titulo': TIT[n], 'sub': f'Lengua y Literatura I · Misión 1 · Nivel {n}', 'escenas': esc},
              open(os.path.join(RAIZ, 'tools/clase/lecciones', f'leng1-m1-n{n}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ============================ LECCIÓN ============================
L = {}
L['1'] = {'temas': [
 T('Los elementos del circuito',
   m('esquema', items=[
     {'nombre': 'El chat', 'raiz': 'Mensaje: «Llego a las 8»', 'ramas': [['Emisor', ['tu tía, que escribe'], 'Quien produce el mensaje.'], ['Receptor', ['vos, que lo leés'], 'Quien lo recibe e interpreta.'], ['Código', ['el español escrito'], 'El sistema de signos que comparten.'], ['Canal', ['el celular e internet'], 'El medio por donde viaja.'], ['Referente', ['la hora de llegada'], 'De qué se habla.'], ['Contexto', ['un viernes a la tarde, ella en el colectivo'], 'La situación en que ocurre.']], 'cierre': 'Si falla cualquiera de estos elementos, la comunicación se complica.'},
     {'nombre': 'El aviso', 'raiz': 'Mensaje: «Atención pasajeros: el vuelo se demora»', 'ramas': [['Emisor', ['la empleada del aeropuerto'], 'Quien habla.'], ['Receptor', ['los pasajeros'], 'Quienes escuchan.'], ['Código', ['el español oral'], 'El idioma.'], ['Canal', ['el aire y los parlantes'], 'Por donde viaja la voz.'], ['Referente', ['la demora del vuelo'], 'El tema.'], ['Contexto', ['la sala de espera, de noche'], 'La situación.']], 'cierre': 'Los mismos elementos aparecen en cualquier mensaje.'}]),
   m('unir_x', consigna='Mensaje: el profe graba un audio para el grupo: «La prueba es el lunes». Uní cada elemento con su ejemplo.', items=[
     {'pares': [['Emisor', 'el profe'], ['Receptor', 'los alumnos del grupo'], ['Canal', 'el celular'], ['Referente', 'la fecha de la prueba']]},
     {'pares': [['Código', 'el español oral'], ['Mensaje', '«La prueba es el lunes»'], ['Contexto', 'un jueves, antes del fin de semana'], ['Emisor', 'el profe']]}]),
   ('Circuito de la comunicación', 'El circuito de la comunicación es el conjunto de elementos que intervienen cuando alguien transmite un mensaje a otra persona: emisor, receptor, mensaje, código, canal, referente y contexto.'),
   'Conviene no confundir dos pares que se parecen: el código es el sistema de signos, como el idioma, mientras que el canal es el medio físico por donde viaja, como el aire o el celular. Y el referente no es una persona, sino aquello de lo que se habla.',
   ['Emisor y receptor: quien produce y quien interpreta.', 'Código y canal: el sistema de signos y el medio.', 'Referente y contexto: el tema y la situación.']),
 T('Cuando el mensaje no llega: el ruido',
   m('marcar', rotulo='Situación', items=[
     {'nombre': 'La videollamada', 'texto': 'Lucía explica la tarea, pero {{la imagen se congela|Ruido del canal: falla el medio.}} y {{su voz llega entrecortada|Otro ruido del canal.}}. Al final dice: «{{Es para el ASAP|Ruido del código: una sigla en inglés que Juan no conoce.}}».', 'cierre': 'Juan no entendió la consigna por culpa del ruido.'},
     {'nombre': 'La radio', 'texto': 'En la radio anuncian el pronóstico, pero {{la señal se pierde en el túnel|Ruido del canal.}}. Cuando vuelve, el locutor habla de una «{{ciclogénesis|Ruido del código: una palabra técnica que muchos no entienden.}}».', 'cierre': 'Los dos tipos de ruido pueden aparecer juntos.'}]),
   m('clasificar_x', consigna='¿Qué tipo de ruido es?', cajas=['Ruido del canal', 'Ruido del código'], cuantos=6, items=[
     ['El micrófono no funciona', 0], ['Hay mucho viento y no se escucha', 0], ['La batería del celular se agota', 0], ['El mensaje está escrito en alemán', 1], ['El médico usa palabras que no conocemos', 1], ['La letra es imposible de leer', 1]]),
   ('Ruido', 'El ruido es todo lo que interfiere en la comunicación y hace que el mensaje no llegue o llegue mal al receptor.'),
   'Hay ruidos que vienen del canal, como una mala señal o un audio entrecortado, y otros que vienen del código, como una palabra que el receptor no conoce. En una escuela online los dos son frecuentes, por eso conviene comprobar que el otro entendió.',
   ['Del canal: falla el medio (señal, sonido, pantalla).', 'Del código: el receptor no comparte el idioma o las palabras.', 'Para evitarlo: comprobar, repetir, aclarar.'])],
 'recuerda': [
   R('Emisor', 'es quien produce el mensaje; el receptor es quien lo recibe y lo interpreta.', 'tu tía escribe / vos leés'),
   R('Código', 'es el sistema de signos que emisor y receptor comparten, como un idioma.', 'el español escrito'),
   R('Canal', 'es el medio físico por donde viaja el mensaje desde el emisor hasta el receptor.', 'el celular, el aire, el papel'),
   R('Referente', 'es aquello de lo que trata el mensaje, el tema del que se habla.', 'la hora de llegada'),
   R('Contexto', 'es la situación en que ocurre la comunicación: lugar, momento y circunstancias.', 'un viernes, en el colectivo'),
   R('Ruido', 'es cualquier interferencia que impide que el mensaje llegue bien, del canal o del código.', 'un audio entrecortado')]}

L['2'] = {'temas': [
 T('La situación comunicativa',
   m('marcar', rotulo='Mensaje', items=[
     {'nombre': 'El cartel', 'texto': 'Cartel en la puerta de una farmacia: {{«Cerrado por inventario.|¿Quién? La farmacia. ¿A quién? A los clientes.}} {{Abrimos mañana a las 9»|¿Para qué? Para informar. ¿Dónde? En la puerta, donde lo ven quienes llegan.}}', 'cierre': 'Las cuatro preguntas arman la situación comunicativa.'},
     {'nombre': 'El audio', 'texto': 'Audio de una abuela al nieto, un domingo a la mañana: {{«Hola, mi amor|¿A quién? A su nieto: por eso el tono cariñoso.}}, {{¿venís a comer los ravioles?»|¿Para qué? Para invitar, es decir, pedir algo.}}', 'cierre': 'El tono cambia según a quién le hablamos.'}]),
   m('elegir_x', consigna='Leé la situación y elegí la respuesta.', items=[
     {'cons': 'Un club publica en sus redes: «Inscripciones abiertas para fútbol infantil». ¿A quién va dirigido?', 'ops': ['A familias con chicos que quieran jugar', 'A los jugadores profesionales del club', 'A los vecinos que se quejan del ruido'], 'ayuda': 'Pensá quién puede inscribirse.'},
     {'cons': 'Un mensaje dice «¡Perdón por llegar tarde!». ¿Para qué se escribió?', 'ops': ['Para disculparse con alguien', 'Para informar el horario del tren', 'Para convencer de comprar algo'], 'ayuda': 'Pensá qué busca quien lo escribe.'},
     {'cons': 'La misma frase, «Ya está», la dice un médico al terminar una vacuna. ¿Qué significa en ese contexto?', 'ops': ['Que la vacuna terminó', 'Que el paciente debe irse enojado', 'Que la vacuna no se pudo aplicar'], 'ayuda': 'El contexto le da el sentido a la frase.'}]),
   ('Situación comunicativa', 'La situación comunicativa es el conjunto de circunstancias en que se produce un texto: quién lo dice, a quién, dónde, cuándo y para qué.'),
   'El contexto le da el sentido a lo que decimos: «¡qué genio!» puede ser un elogio o una burla según la situación. Por eso, para entender un texto, no alcanza con leer las palabras: hay que preguntarse en qué situación se produjo.',
   ['¿Quién habla y a quién?', '¿Dónde y cuándo?', '¿Para qué lo dice?']),
 T('La intención del texto',
   m('versiones', rotulo='Intención', items=[
     {'nombre': 'Informar', 'texto': '{{Mañana llueve todo el día.|Da un dato: intención de informar.}}'},
     {'nombre': 'Pedir', 'texto': '{{¿Me prestás tu paraguas mañana?|Busca que el otro haga algo: pedir.}}'},
     {'nombre': 'Convencer', 'texto': '{{Mejor quedémonos: con lluvia el parque es un barrial.|Da una razón para que el otro piense igual: convencer.}}'},
     {'nombre': 'Expresar', 'texto': '{{¡Odio los días de lluvia!|Muestra un sentimiento: expresar.}}'}]),
   m('clasificar_x', consigna='¿Qué intención tiene cada texto?', cajas=['Informar', 'Pedir', 'Convencer', 'Expresar'], cuantos=6, items=[
     ['El museo abre de martes a domingo.', 0], ['El agua hierve a cien grados.', 0], ['¿Me pasás la sal?', 1], ['Por favor, cerrá la puerta.', 1],
     ['Comprá esta zapatilla: dura el doble.', 2], ['Tenemos que reciclar, porque la basura no para de crecer.', 2], ['¡Estoy feliz de verte!', 3], ['Qué tristeza que te vayas.', 3]]),
   ('Intención comunicativa', 'La intención comunicativa es lo que quien produce un texto busca lograr con él: informar, pedir, convencer o expresar lo que siente.'),
   'Un mismo tema puede servir para cosas muy distintas: la lluvia puede ser un dato, un pedido, un argumento o una queja. Reconocer la intención ayuda a entender el texto y también a escribir mejor, porque cada intención pide una forma distinta.',
   ['Informar: dar datos.', 'Pedir: que el otro haga algo. Convencer: que piense como vos.', 'Expresar: mostrar lo que sentís.']),
 T('Adecuar el texto al contexto',
   m('transformar', items=[
     {'nombre': 'A la profe', 'antes': 'Che, no llego con la tarea, la mando mañana.', 'pasos': [{'v': '{{Hola, profe.}} No llego con la tarea, la mando mañana.', 'txt': 'Un saludo adecuado al destinatario.'}, {'v': 'Hola, profe. {{No llego a terminar la tarea hoy. ¿Puedo enviarla mañana?}}', 'txt': 'Se pide, no se impone.'}, {'v': 'Hola, profe. No llego a terminar la tarea hoy. ¿Puedo enviarla mañana? {{Gracias.}}', 'txt': 'Un cierre cordial.'}], 'cierre': 'Mismo mensaje, adecuado a la situación.'}]),
   m('elegir_x', consigna='¿Qué mensaje es el adecuado para esta situación?', items=[
     {'cons': 'Le escribís al club para preguntar el horario de natación.', 'ops': ['Buenas tardes, quería consultar el horario de natación. Gracias.', 'Ey, ¿a qué hora es pile?', 'Natación horario ya.'], 'ayuda': 'Es una institución y no te conocen.'},
     {'cons': 'Le avisás a tu mejor amiga que llegás tarde a la plaza.', 'ops': ['Llego 10 min tarde, ¡esperame! 🙏', 'Estimada amiga: le informo que me retrasaré.', 'Por medio de la presente comunico mi demora.'], 'ayuda': 'Con una amiga, lo formal suena raro.'}]),
   ('Adecuación', 'Adecuar un texto es elegir las palabras y el tono según a quién le hablamos y en qué situación, para que el mensaje cumpla su intención.'),
   'No hay una forma correcta para todas las ocasiones: un mensaje informal es perfecto con un amigo y es un error con una institución. La pregunta que ordena todo es siempre la misma: ¿quién me va a leer y para qué le escribo?',
   ['Con desconocidos o instituciones: saludo, respeto y claridad.', 'Con amigos: más breve y relajado.', 'Siempre: que se entienda lo que querés.'])],
 'recuerda': [
   R('Texto', 'es toda unidad de comunicación completa, oral o escrita, que tiene una intención.', 'un chat, un cartel, un cuento'),
   R('Situación comunicativa', 'son las circunstancias de un texto: quién, a quién, dónde, cuándo y para qué.', 'cartel de la farmacia para los clientes'),
   R('Intención comunicativa', 'es lo que se busca lograr con el texto: informar, pedir, convencer o expresar.', '¿Me prestás tu paraguas? → pedir'),
   R('Adecuación', 'es ajustar las palabras y el tono al destinatario y a la situación.', 'Hola, profe… ¿Puedo enviarla mañana?')]}

L['3'] = {'temas': [
 T('Funciones referencial y expresiva',
   m('marcar', rotulo='Mensaje', items=[
     {'nombre': 'El frío', 'texto': '{{«Hoy la temperatura mínima fue de 2 grados.»|Referencial: informa un dato objetivo.}} {{«¡Me congelo, no siento los dedos!»|Expresiva: muestra lo que siente quien habla.}}', 'cierre': 'Mismo tema, distinta función.'},
     {'nombre': 'El partido', 'texto': '{{«Boca ganó 2 a 1.»|Referencial: el resultado.}} {{«¡Qué partidazo, estoy feliz!»|Expresiva: la emoción del hincha.}}', 'cierre': 'La referencial informa; la expresiva siente.'}]),
   m('clasificar_x', consigna='¿Función referencial o expresiva?', cajas=['Referencial', 'Expresiva'], cuantos=6, items=[
     ['La Luna tarda 28 días en dar la vuelta a la Tierra.', 0], ['El colectivo 60 pasa cada diez minutos.', 0], ['Córdoba tiene sierras.', 0], ['¡Qué miedo me dan las tormentas!', 1], ['Uf, estoy agotado.', 1], ['Me encanta este lugar.', 1]]),
   ('Función del lenguaje', 'Una función del lenguaje es el uso principal que se le da a un mensaje, según aquello en lo que se pone el foco: el tema, quien habla, quien escucha o el propio mensaje.'),
   'La función referencial pone el foco en el tema e informa de manera objetiva, por eso predomina en las noticias y en los textos de estudio. La expresiva pone el foco en quien habla: muestra emociones y opiniones, y suele tener exclamaciones y la primera persona.',
   ['Referencial: datos objetivos sobre el tema.', 'Expresiva: emociones de quien habla.', 'Pista expresiva: exclamaciones, «yo», «me».']),
 T('Funciones apelativa y poética',
   m('marcar', rotulo='Mensaje', items=[
     {'nombre': 'Apelativa', 'texto': '{{«Lavate las manos antes de comer.»|Apelativa: busca que el receptor haga algo.}} {{«¿Me ayudás con la mudanza?»|También apelativa: un pedido.}}', 'cierre': 'Foco en el receptor: órdenes, pedidos, consejos.'},
     {'nombre': 'Poética', 'texto': '{{«Agua que no has de beber, déjala correr.»|Poética: el ritmo y la rima llaman la atención.}} {{«Mi casa es tu casa.»|Poética: la repetición hace que se recuerde.}}', 'cierre': 'Foco en la forma del mensaje.'}]),
   m('clasificar_x', consigna='Clasificá cada mensaje según su función principal.', cajas=['Referencial', 'Expresiva', 'Apelativa', 'Poética'], cuantos=6, items=[
     ['El Paraná es uno de los ríos más largos de América.', 0], ['¡Qué emoción, me eligieron!', 1], ['No te olvides de cargar la SUBE.', 2], ['Respondé el formulario antes del viernes.', 2],
     ['Más vale pájaro en mano que cien volando.', 3], ['Lento, lento, viene el viento.', 3], ['Estoy tan cansada…', 1], ['El museo cierra a las 18.', 0]]),
   ('Apelativa y poética', 'La función apelativa busca que el receptor haga, piense o sienta algo, y la poética llama la atención sobre la forma del mensaje: su ritmo, su sonido o sus imágenes.'),
   'La apelativa aparece en órdenes, pedidos, consejos y publicidades, muchas veces con verbos en imperativo. La poética no es solo de los poemas: también está en refranes, canciones, trabalenguas y eslóganes, que se recuerdan justamente por cómo suenan.',
   ['Apelativa: «hacé», «¿podés…?», publicidades.', 'Poética: rima, ritmo, repetición.', 'Refranes y eslóganes también son poéticos.']),
 T('Funciones fática y metalingüística',
   m('marcar', rotulo='Diálogo', items=[
     {'nombre': 'La videollamada', 'texto': '—{{¿Me escuchan? ¿Se ve la pantalla?|Fática: comprueba que el canal funcione.}} —Sí, profe. —Bien. {{¿Alguien sabe qué significa «inferir»?|Metalingüística: usa el idioma para hablar de una palabra.}}', 'cierre': 'Una controla el canal; la otra habla del idioma.'},
     {'nombre': 'El teléfono', 'texto': '—{{¿Hola? ¿Hola? ¿Estás ahí?|Fática: abre y verifica el contacto.}} —Sí. Che, {{¿«haber» va con hache?|Metalingüística: pregunta sobre la lengua.}}', 'cierre': 'Funciones que usamos sin darnos cuenta.'}]),
   m('elegir_x', consigna='¿Qué función predomina?', items=[
     {'cons': '«¿Se escucha bien? Si no, avísenme en el chat.»', 'ops': ['Fática', 'Metalingüística', 'Poética'], 'ayuda': 'Comprueba si el canal funciona.'},
     {'cons': '«"Hiato" es el encuentro de dos vocales que van en sílabas distintas.»', 'ops': ['Metalingüística', 'Fática', 'Expresiva'], 'ayuda': 'Usa el idioma para explicar un término del idioma.'},
     {'cons': '«Bueno… eh… ¿me seguís?»', 'ops': ['Fática', 'Referencial', 'Apelativa'], 'ayuda': 'Mantiene el contacto con quien escucha.'},
     {'cons': '«¿Cuál es el plural de "lápiz"?»', 'ops': ['Metalingüística', 'Fática', 'Poética'], 'ayuda': 'Pregunta sobre la lengua.'}]),
   ('Fática y metalingüística', 'La función fática sirve para abrir, mantener o comprobar el contacto entre emisor y receptor, y la metalingüística usa el idioma para hablar del propio idioma.'),
   'La fática casi no transmite información: «¿hola?», «¿me escuchás?», «eh…» solo aseguran que el canal esté abierto. La metalingüística aparece cada vez que preguntamos qué significa una palabra o cómo se escribe. Un mensaje puede tener varias funciones, pero siempre hay una que predomina.',
   ['Fática: «¿hola?», «¿se escucha?».', 'Metalingüística: «¿qué significa…?», «¿lleva tilde?».', 'Siempre preguntate: ¿para qué se dijo?'])],
 'recuerda': [
   R('Función referencial', 'pone el foco en el tema e informa datos de manera objetiva.', 'El colectivo pasa cada diez minutos.'),
   R('Función expresiva', 'pone el foco en quien habla y muestra sus emociones.', '¡Qué miedo me dan las tormentas!'),
   R('Función apelativa', 'busca que el receptor haga, piense o sienta algo, con órdenes, pedidos o consejos.', 'No te olvides de cargar la SUBE.'),
   R('Función poética', 'llama la atención sobre la forma del mensaje: ritmo, sonido o imágenes.', 'Lento, lento, viene el viento.'),
   R('Función fática', 'abre, mantiene o comprueba el contacto entre quienes se comunican.', '¿Me escuchan?'),
   R('Función metalingüística', 'usa el idioma para hablar del propio idioma, por ejemplo sobre palabras o reglas.', '¿«Haber» va con hache?')]}

L['4'] = {'temas': [
 T('Códigos verbales y no verbales',
   m('esquema', items=[{'nombre': 'Códigos', 'cols': ['Código', 'Usa', 'Ejemplos'], 'filas': [
       ['Verbal oral', 'palabras habladas', 'un audio, una charla'], ['Verbal escrito', 'palabras escritas', 'un mail, un libro'],
       ['No verbal visual', 'imágenes, colores, formas', 'un semáforo, un ícono'], ['No verbal gestual', 'el cuerpo y la cara', 'un pulgar arriba, un guiño'], ['No verbal sonoro', 'sonidos', 'una sirena, un timbre']],
     'cierre': 'Verbal = palabras; no verbal = cualquier otro signo.'}]),
   m('clasificar_x', consigna='¿Qué código usa cada mensaje?', cajas=['Verbal', 'No verbal'], cuantos=6, items=[
     ['un mensaje de texto', 0], ['una canción que escuchás', 0], ['una carta', 0], ['la luz roja del semáforo', 1], ['un aplauso', 1], ['la sirena de una ambulancia', 1], ['un guiño de ojo', 1]]),
   ('Código verbal', 'El código verbal usa palabras, habladas o escritas, mientras que el código no verbal comunica con otros signos, como imágenes, colores, gestos o sonidos.'),
   'Los signos no verbales se entienden porque los aprendimos en nuestra cultura: el rojo del semáforo significa «pará» por un acuerdo, no por naturaleza. Por eso un gesto o un emoji puede significar cosas distintas en otro país.',
   ['Verbal: oral o escrito.', 'No verbal: visual, gestual o sonoro.', 'Los dos se aprenden en una cultura.']),
 T('Textos mixtos',
   m('marcar', rotulo='Texto', items=[
     {'nombre': 'El afiche', 'texto': 'Afiche: {{un dibujo de una botella tachada|No verbal: la imagen ya dice «no».}} y {{la frase «Menos plástico, más planeta»|Verbal: explica y convence.}} {{en letras verdes|No verbal: el color se asocia con la naturaleza.}}.', 'cierre': 'Los dos códigos juntos refuerzan el mensaje.'},
     {'nombre': 'El chat', 'texto': 'Mensaje: {{«Salimos a las 5»|Verbal: el dato.}} {{⚽🌳|No verbal: adónde y para qué.}} {{👍|No verbal: confirma.}}', 'cierre': 'En los chats mezclamos códigos todo el tiempo.'}]),
   m('elegir_x', consigna='Leé el texto mixto y elegí la interpretación correcta.', items=[
     {'cons': 'Cartel: dibujo de un perro con una bolsita y la frase «Tu perro, tu responsabilidad».', 'ops': ['Pide que juntes lo que tu perro ensucia', 'Prohíbe los perros en la plaza', 'Vende bolsas para perros'], 'ayuda': 'Uní la imagen con la frase.'},
     {'cons': 'Mensaje: «¿Venís al cumple?» Respuesta: 😢🤒', 'ops': ['No va porque está enfermo', 'Va pero llega tarde', 'Está feliz de ir'], 'ayuda': 'Los emojis responden sin palabras.'},
     {'cons': 'Señal: un rectángulo azul con una cama blanca dibujada, al costado de la ruta.', 'ops': ['Hay un hotel o alojamiento cerca', 'Está prohibido dormir', 'Hay una mueblería'], 'ayuda': 'Es un código visual que se aprende.'}]),
   ('Texto mixto', 'Un texto mixto combina el código verbal con códigos no verbales, como imágenes, colores o sonidos, para comunicar un mensaje.'),
   'Afiches, publicidades, historietas, memes y videos son textos mixtos. Para entenderlos hay que leer las dos partes juntas: muchas veces la imagen dice algo que las palabras no dicen, o le cambia el sentido a la frase.',
   ['Afiches, memes, historietas, videos.', 'La imagen y la palabra se completan.', 'Leé siempre las dos partes juntas.'])],
 'recuerda': [
   R('Código verbal', 'es el que usa palabras, ya sea de forma oral o escrita.', 'un audio, una carta'),
   R('Código no verbal', 'comunica con signos que no son palabras: imágenes, colores, gestos o sonidos.', 'el semáforo, un aplauso'),
   R('Signos culturales', 'los signos no verbales se entienden por un acuerdo de cada cultura y pueden cambiar.', '🙏: gracias o por favor'),
   R('Texto mixto', 'combina palabras con imágenes, colores o sonidos para comunicar un mismo mensaje.', 'un afiche con dibujo y frase')]}

A = {
 '1': [
   UNI('Situación: tu prima te manda un audio desde Mendoza contándote que nevó. Uní cada elemento.', [('Emisor', 'tu prima'), ('Canal', 'el celular'), ('Referente', 'la nevada'), ('Código', 'el español oral')], 'Cada elemento cumple una función.'),
   CLA('¿Ruido del canal o del código?', ['Canal', 'Código'], [('Se corta la luz en medio de la clase online', 'Canal'), ('El texto usa palabras en latín', 'Código'), ('Se escucha un eco que tapa la voz', 'Canal'), ('El manual está en japonés', 'Código')], 'Medio físico o sistema de signos.'),
   MC('Un compañero dice: «En una carta, el canal es el español». ¿Qué le contestás?', ['El español es el código; el canal es el papel', 'Tiene razón', 'El canal es quien la escribe'], 'El español es el código; el canal es el papel', 'Código: sistema de signos; canal: medio.', 'error'),
   MC('Durante una videollamada, Juan pregunta: «¿Qué es una "consigna"?» y la profe se lo explica. ¿Qué ruido se resolvió?', ['Un ruido del código', 'Un ruido del canal', 'No había ruido'], 'Un ruido del código', 'Juan no conocía la palabra: el problema estaba en el código.', 'analizar')],
 '2': [
   CLA('¿Qué intención tiene cada mensaje?', ['Informar', 'Pedir', 'Convencer', 'Expresar'], [('La biblioteca cierra a las 19.', 'Informar'), ('¿Me ayudás con la valija?', 'Pedir'), ('Adoptá un perro: te va a cambiar la vida.', 'Convencer'), ('¡Estoy nerviosísima!', 'Expresar')], 'Pensá qué busca cada uno.'),
   MC('La frase «¡Qué inteligente!» dicha a alguien que acaba de chocar con una puerta, ¿qué sentido tiene?', ['Es una burla: dice lo contrario', 'Es un elogio sincero', 'Es un pedido'], 'Es una burla: dice lo contrario', 'El contexto le da el sentido a la frase.', 'analizar'),
   TAP('Tocá las dos palabras que no son adecuadas en este mensaje a la directora: «Hola, che, quería pedirle una reunión, porfa».', ['Hola,', 'che,', 'quería', 'pedirle', 'una', 'reunión,', 'porfa'], [1, 6], 'Con una directora no van «che» ni «porfa».', 'error'),
   KW('Escribí un mensaje para pedirle al club de tu barrio información sobre los horarios de básquet. Tiene que ser adecuado: saludo, pedido claro y despedida.', 'Pensá quién te va a leer.', [['hola', 'buenas', 'buen día', 'buenas tardes'], ['horario*'], ['gracias', 'saludos', 'atentamente']], 3, 'Saludo, pedido claro y cierre cordial.', 'aplicar')],
 '3': [
   CLA('¿Qué función predomina?', ['Referencial', 'Expresiva', 'Apelativa', 'Poética'], [('El Sol es una estrella.', 'Referencial'), ('¡Te extraño mucho!', 'Expresiva'), ('Apagá la compu ya.', 'Apelativa'), ('Tres tristes tigres tragaban trigo.', 'Poética')], 'Tema, emisor, receptor o forma.'),
   UNI('Uní cada frase con su función.', [('¿Me escuchás bien?', 'fática'), ('¿«Hay» lleva hache?', 'metalingüística'), ('Llevá abrigo.', 'apelativa'), ('Hoy hay 30 grados.', 'referencial')], 'Pensá para qué se dijo cada una.'),
   MC('Sofía dice que «¿Hola? ¿Se corta?» tiene función apelativa porque es una pregunta. ¿Tiene razón?', ['No: es fática, comprueba el canal', 'Sí: toda pregunta es apelativa', 'No: es poética'], 'No: es fática, comprueba el canal', 'No pide que el otro haga algo: verifica el contacto.', 'error'),
   MS('El eslogan «Pensá verde, viví verde» repite palabras para que se recuerde y además invita a actuar. Elegí las DOS funciones que tiene.', ['Poética', 'Apelativa', 'Referencial', 'Fática'], ['Poética', 'Apelativa'], 'La repetición es poética; la invitación, apelativa.')],
 '4': [
   CLA('Clasificá cada mensaje.', ['Verbal', 'No verbal', 'Mixto'], [('un audio de voz', 'Verbal'), ('un semáforo', 'No verbal'), ('un meme con imagen y frase', 'Mixto'), ('un pulgar arriba con la mano', 'No verbal')], 'Palabras, otros signos o las dos cosas.'),
   MC('Cartel: un cigarrillo tachado con un círculo rojo. ¿Qué código usa y qué dice?', ['No verbal visual: prohibido fumar', 'Verbal escrito: venta de cigarrillos', 'No verbal sonoro: alarma'], 'No verbal visual: prohibido fumar', 'El círculo rojo tachado es un signo aprendido de prohibición.', 'analizar'),
   MC('Un chico de otro país interpreta el gesto de «pulgar arriba» como un insulto. ¿Qué muestra eso?', ['Que los signos no verbales dependen de la cultura', 'Que el chico no sabe comunicarse', 'Que los gestos no comunican nada'], 'Que los signos no verbales dependen de la cultura', 'Los signos no verbales son acuerdos culturales.', 'analizar'),
   KW('Describí un texto mixto que hayas visto hoy (un afiche, un meme, un cartel): qué dice con palabras y qué agrega la imagen o el color.', 'Nombrá las dos partes.', [['imagen', 'dibujo', 'foto', 'color', 'emoji'], ['dice', 'frase', 'palabra*', 'texto']], 2, 'Un texto mixto se lee uniendo palabra e imagen.', 'aplicar')],
 '5': [
   MC('En «¿Me escuchan? Hoy vemos el circuito de la comunicación», ¿qué función tiene la primera pregunta?', ['Fática', 'Apelativa', 'Expresiva'], 'Fática', 'Comprueba el canal.', 'analizar'),
   CLA('Mandás un audio de WhatsApp a tu abuela. Clasificá cada cosa según su papel en el circuito.', ['Canal', 'Código'], [('el celular', 'Canal'), ('el idioma español', 'Código'), ('internet', 'Canal'), ('las palabras que usás', 'Código')], 'Medio o sistema de signos.', 'analizar'),
   UNI('Uní cada situación con su intención.', [('Un cartel de «Prohibido pasar»', 'pedir u ordenar'), ('Un parte meteorológico', 'informar'), ('Una publicidad de zapatillas', 'convencer'), ('Un mensaje de «¡te quiero!»', 'expresar')], 'La intención es lo que se busca.'),
   MC('Un afiche muestra una canilla goteando y dice «Cada gota cuenta». ¿Qué tipo de texto es y qué intención tiene?', ['Mixto, para convencer de cuidar el agua', 'Verbal, para informar el precio del agua', 'No verbal, para expresar tristeza'], 'Mixto, para convencer de cuidar el agua', 'Imagen y frase juntas, con intención de convencer.', 'analizar')],
}

EX = [
 [1, UNI('Situación: la radio anuncia «Alerta por tormentas en Entre Ríos». Uní cada elemento.', [('Emisor', 'el locutor'), ('Receptor', 'los oyentes'), ('Canal', 'las ondas de radio'), ('Referente', 'las tormentas')], 'Cada elemento del circuito.')],
 [1, MC('Un médico le explica a un paciente su diagnóstico con palabras técnicas y el paciente no entiende. ¿Qué pasó?', ['Hubo un ruido del código', 'Hubo un ruido del canal', 'Faltó el referente'], 'Hubo un ruido del código', 'El paciente no comparte esas palabras.', 'analizar')],
 [1, TF('El canal es el sistema de signos que comparten emisor y receptor.', 'Falso', 'Ese es el código; el canal es el medio físico.')],
 [2, CLA('¿Qué intención tiene cada texto?', ['Informar', 'Pedir', 'Convencer', 'Expresar'], [('El tren a Tigre sale cada 15 minutos.', 'Informar'), ('¿Podés bajar la música?', 'Pedir'), ('Elegí nuestra pizza: es la más rica del barrio.', 'Convencer'), ('¡Qué lindo día!', 'Expresar')], 'Lo que busca quien habla.')],
 [2, MC('¿Cuál es el mensaje adecuado para pedirle a la bibliotecaria de la escuela un libro?', ['Buenos días, ¿tiene «La liga…»? Gracias.', 'Pasame el libro ese que tenés ahí.', 'Necesito el libro ya mismo, dámelo.'], 'Buenos días, ¿tiene «La liga…»? Gracias.', 'Adecuado al destinatario y a la situación.', 'aplicar')],
 [2, TF('La frase «Ya está» significa siempre lo mismo, sin importar la situación en que se dice.', 'Falso', 'El contexto le da el sentido: terminar, aceptar, resignarse…', 'analizar')],
 [3, CLA('¿Qué función predomina?', ['Referencial', 'Expresiva', 'Apelativa', 'Poética'], [('El agua se congela a cero grados.', 'Referencial'), ('¡Qué susto me diste!', 'Expresiva'), ('Cerrá la ventana.', 'Apelativa'), ('Al que madruga, Dios lo ayuda.', 'Poética')], 'Para qué se dijo cada una.')],
 [3, SA('¿Qué función del lenguaje predomina en «¿Qué significa la palabra "efímero"?»?', ['metalingüística', 'metalinguistica', 'la metalingüística', 'funcion metalinguistica', 'función metalingüística'], 'Usa el idioma para hablar del idioma.', 'aplicar')],
 [3, MC('Un compañero dice que la función poética solo aparece en los poemas. ¿Qué le contestás?', ['También aparece en refranes, canciones y eslóganes', 'Tiene razón', 'Solo aparece en las noticias'], 'También aparece en refranes, canciones y eslóganes', 'Donde la forma del mensaje llama la atención.', 'error')],
 [4, CLA('¿Verbal, no verbal o mixto?', ['Verbal', 'No verbal', 'Mixto'], [('una carta escrita a mano', 'Verbal'), ('el timbre de la casa', 'No verbal'), ('una historieta', 'Mixto'), ('un saludo con la mano', 'No verbal')], 'Palabras, otros signos o ambos.')],
 [4, MC('Te mandan 🙏 después de que hiciste un favor. ¿Qué significa en ese contexto?', ['Gracias', 'Por favor, ayudame', 'Estoy rezando'], 'Gracias', 'El contexto define el sentido del signo.', 'analizar')],
 [4, TF('Los signos no verbales significan lo mismo en todas las culturas.', 'Falso', 'Son acuerdos culturales y pueden cambiar de un país a otro.')],
 [4, KW('Explicá con tus palabras por qué un meme es un texto mixto y qué hay que hacer para entenderlo.', 'Nombrá los dos códigos.', [['imagen', 'foto', 'dibujo'], ['palabra*', 'texto', 'frase', 'verbal'], ['junt*', 'las dos', 'ambos', 'combin*']], 3, 'Combina imagen y palabras, y hay que leerlas juntas.', 'aplicar')],
]

def ajustes(M):
    M['act'] = A
    M['examen'] = EX
    M['practica'] = 'Actividades generales'
    M['examen_titulo'] = 'Nivel jefe: la comunicación y el lenguaje'
    M['actualizar_preguntas'] = True

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-1/mision-1.json', L, ajustes=ajustes)
