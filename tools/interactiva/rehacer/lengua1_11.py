# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 11 · La ciencia ficción (TODO nuevo, sin libro: fragmentos y argumentos de obras de dominio público, contados con palabras propias)
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD
RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', '..')

# ============================ CLASES ANIMADAS ============================
STEP = {'1': 'be53950a-a3e7-4ca1-932f-ecd2d657b98e', '2': 'c0284020-79da-452d-a4a3-0839c75df444', '3': '73cdc080-b436-4934-a959-071f22710e5a', '4': '3f322f49-dfce-457f-b2ae-fda9c2419a59'}
TIT = {'1': 'Qué es la ciencia ficción', '2': 'Mundos posibles', '3': 'Ciencia, tecnología y sociedad', '4': 'Viajes en el tiempo y el espacio'}
CL = {}
CL['1'] = [
 {'t': 'reto', 'texto': '¿Qué pasaría si las personas pudieran borrar sus recuerdos tristes con una pastilla?', 'segundos': 8, 'respuesta': 'Esa pregunta ya es el comienzo de un relato de ciencia ficción', 'emoji': '💊', 'titulo': 'CIENCIA FICCIÓN', 'sub': '¿qué pasaría si…?',
  'voz': ['Reto: ¿qué pasaría si las personas pudieran borrar sus recuerdos tristes con una pastilla?', 'Ocho segundos para imaginar.', 'Seguro pensaste en ventajas y en peligros. Esa pregunta ya es el comienzo de un relato de *ciencia ficción*.']},
 {'t': 'definicion', 'palabra': 'Ciencia ficción', 'texto': 'Género que imagina, con una base científica o tecnológica, cómo cambiarían las personas y el mundo ante un avance o un descubrimiento.', 'emoji': '🚀',
  'voz': ['La *ciencia ficción* imagina cómo cambiarían las personas y el mundo ante un avance científico o tecnológico.', 'Lo que la distingue es que intenta explicar lo extraordinario con la ciencia, aunque sea una ciencia inventada.']},
 {'t': 'comparar', 'a': {'cab': 'Maravilloso', 'texto': 'una varita mágica convierte el agua en vino', 'emoji': '🪄'}, 'b': {'cab': 'Ciencia ficción', 'texto': 'una máquina reordena las moléculas del agua', 'emoji': '🔬'}, 'signo': '≠',
  'voz': ['Compará dos relatos donde pasa algo imposible.', 'En el *maravilloso*, una varita mágica lo hace, y nadie pide explicaciones.', 'En la *ciencia ficción*, una máquina lo logra reordenando moléculas: hay una explicación que suena científica.']},
 {'t': 'linea', 'titulo': 'LOS PIONEROS', 'eventos': [{'fecha': '1818', 'txt': 'Mary Shelley: Frankenstein', 'emoji': '⚡'}, {'fecha': '1865', 'txt': 'Julio Verne: De la Tierra a la Luna', 'emoji': '🌕'}, {'fecha': '1875', 'txt': 'Holmberg: un viaje a Marte, en Buenos Aires', 'emoji': '🇦🇷'}, {'fecha': '1895', 'txt': 'H. G. Wells: La máquina del tiempo', 'emoji': '⏳'}],
  'voz': ['En 1818, Mary Shelley imagina a un científico que da vida a un ser hecho de partes de cadáveres: *Frankenstein*.', 'En 1865, Julio Verne cuenta un viaje a la Luna en una enorme bala de cañón, casi cien años antes de que llegara el primer astronauta.', 'En 1875, el argentino Eduardo Holmberg publica el viaje de un porteño a Marte.', 'Y en 1895, H. G. Wells inventa *La máquina del tiempo*.']},
 {'t': 'pizarra', 'titulo': 'LA FÓRMULA', 'lineas': [{'txt': '¿Qué pasaría si…?', 'color': 'sol', 'marca': 'subraya'}, {'txt': '+ una explicación científica', 'color': 'azul', 'marca': ''}, {'txt': '= consecuencias para las personas', 'color': 'verde', 'marca': 'circulo'}],
  'voz': ['Casi todo relato de ciencia ficción parte de una pregunta: *¿qué pasaría si…?*', 'Le suma una explicación que suene científica, para que el lector lo crea posible.', 'Y lo importante viene después: las *consecuencias* que ese cambio tiene para las personas.']},
 {'t': 'quiz4', 'pregunta': 'Un cuento: una nena descubre que su perro habla porque un hada lo tocó. ¿Es ciencia ficción?', 'opciones': ['Sí', 'No: es maravilloso', 'Es un policial', 'Es épica'], 'correcta': 1,
  'voz': ['Pregunta: un cuento cuenta que un perro habla porque un hada lo tocó. ¿Es ciencia ficción?', 'Fijate cómo se explica lo imposible.', 'No: lo explica la magia, así que es *maravilloso*. Si un chip le diera el habla, sí sería ciencia ficción.']},
 {'t': 'errores', 'items': [{'mal': 'Basta con extraterrestres', 'bien': 'Importa la explicación científica'}, {'mal': 'Habla solo del futuro', 'bien': 'Habla de lo que nos preocupa hoy'}],
  'voz': ['Dos ideas equivocadas.', 'No alcanza con poner extraterrestres: lo central es la explicación científica y sus consecuencias.', 'Y aunque transcurra en el futuro, la ciencia ficción habla del *presente*: de lo que hoy nos ilusiona o nos preocupa.']},
 {'t': 'resumen', 'items': [['Ciencia ficción', 'avances imaginados y sus consecuencias'], ['¿Qué pasaría si…?', 'la pregunta que la pone en marcha'], ['Explicación científica', 'la distingue del maravilloso'], ['Pioneros', 'Shelley, Verne, Holmberg, Wells']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 1'},
  'voz': ['Repasemos.', 'La ciencia ficción es el género de las preguntas sobre el futuro.', 'Qué es.', 'La pregunta que la pone en marcha.', 'La explicación científica.', 'Y sus pioneros. ¡A practicar!']},
]
CL['2'] = [
 {'t': 'noticia', 'cinta': 'AÑO 2190', 'titular': 'En Neo Córdoba está prohibido estar triste', 'bajada': 'Un sensor en la muñeca avisa a las autoridades', 'emoji': '🙂', 'titulo': 'MUNDOS POSIBLES', 'sub': 'utopías y distopías',
  'voz': ['Noticia del año 2190: en la ciudad de Neo Córdoba está prohibido estar triste.', 'Un sensor en la muñeca de cada habitante avisa a las autoridades si alguien deja de sonreír.', '¿Es un mundo perfecto o una pesadilla? La ciencia ficción construye *mundos posibles* para hacernos esa pregunta.']},
 {'t': 'definicion', 'palabra': 'Mundo posible', 'texto': 'Lugar imaginado, con sus propias reglas, tecnologías y costumbres, donde ocurre un relato de ciencia ficción.', 'emoji': '🌐',
  'voz': ['Un *mundo posible* es el lugar imaginado donde transcurre el relato: con sus propias reglas, tecnologías y costumbres.', 'Puede ser la Tierra dentro de mil años, otro planeta o una ciudad bajo el mar.']},
 {'t': 'versus', 'a': {'txt': 'Utopía', 'emoji': '🌈', 'datos': ['sociedad ideal', 'todos viven en armonía']}, 'b': {'txt': 'Distopía', 'emoji': '🏭', 'datos': ['sociedad opresiva', 'el control parece perfecto']}, 'gana': 'empate', 'veredicto': 'Dos caras del futuro',
  'voz': ['Hay dos grandes tipos de mundos posibles.', 'La *utopía*: una sociedad ideal, donde todos viven en armonía.', 'La *distopía*: una sociedad que parece perfecta, pero en realidad controla y oprime a las personas.', 'Neo Córdoba, con su sensor de sonrisas, es una distopía.']},
 {'t': 'bloques', 'titulo': 'CÓMO SE ARMA UN MUNDO', 'items': [{'cab': 'Las reglas', 'txt': 'qué se permite, qué se prohíbe'}, {'cab': 'La tecnología', 'txt': 'qué inventos cambian la vida'}, {'cab': 'Las costumbres', 'txt': 'cómo viven y se relacionan'}],
  'voz': ['¿Cómo se construye un mundo posible?', 'Con sus *reglas*: qué está permitido y qué prohibido.', 'Con su *tecnología*: los inventos que cambiaron la vida.', 'Y con sus *costumbres*: cómo se visten, se comunican y se relacionan.']},
 {'t': 'prediccion', 'pregunta': 'En un mundo sin gravedad, un personaje deja caer un vaso y se rompe contra el piso. ¿Funciona el relato?', 'a': {'txt': 'Sí, da igual', 'emoji': '🤷'}, 'b': {'txt': 'No: rompe sus propias reglas', 'emoji': '❌'}, 'correcta': 'b', 'resultado': 'Un mundo posible tiene que ser coherente con las reglas que planteó.',
  'voz': ['¿Qué creés? En un relato ambientado en un mundo sin gravedad, alguien deja caer un vaso y se rompe contra el piso.', 'Pensalo.', 'No funciona: el relato rompe sus propias reglas. Un mundo posible tiene que ser *coherente*.']},
 {'t': 'vof', 'afirmacion': 'Las distopías parecen perfectas, pero controlan a todos.', 'emoji': '👁️', 'verdadero': True, 'explicacion': 'La apariencia de perfección esconde la falta de libertad.',
  'voz': ['Verdadero o falso: las distopías suelen parecer perfectas, aunque esconden un control opresivo.', 'Pensá en Neo Córdoba.', 'Verdadero: muchas veces el protagonista es el primero en darse cuenta de que algo anda mal.']},
 {'t': 'errores', 'items': [{'mal': 'Cambiar las reglas cuando conviene', 'bien': 'Ser coherente de principio a fin'}, {'mal': 'Distopía es un mundo triste', 'bien': 'Es control disfrazado de ideal'}],
  'voz': ['Dos errores comunes.', 'Cambiar las reglas del mundo cuando conviene: el lector deja de creer.', 'Y llamar distopía a cualquier mundo triste: la distopía es una sociedad de *control* que se presenta como ideal.']},
 {'t': 'resumen', 'items': [['Mundo posible', 'lugar imaginado con sus reglas'], ['Utopía', 'sociedad ideal'], ['Distopía', 'sociedad opresiva que parece perfecta'], ['Coherencia', 'respetar las propias reglas']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 2'},
  'voz': ['Repasemos.', 'Los mundos posibles son espejos de nuestro mundo.', 'El mundo posible.', 'La utopía.', 'La distopía.', 'Y la coherencia. ¡A practicar!']},
]
CL['3'] = [
 {'t': 'chat', 'contacto': {'nombre': 'Asistente IA', 'emoji': '🤖'}, 'mensajes': [{'yo': True, 'txt': '¿Me hacés la tarea?'}, {'yo': False, 'txt': 'Puedo ayudarte a entenderla. ¿Por dónde empezamos?'}], 'titulo': 'CIENCIA Y SOCIEDAD', 'sub': 'robots, inventos y advertencias',
  'voz': ['Hoy hablar con una inteligencia artificial es algo común, pero hace cien años era pura ciencia ficción.', 'Fijate que la máquina no hace la tarea: propone ayudar a entenderla.', 'El género lleva más de un siglo preguntándose qué pasa cuando las máquinas piensan. Hoy vemos cómo la ciencia ficción discute la relación entre *tecnología y sociedad*.']},
 {'t': 'datoloco', 'texto': 'La palabra «robot» la inventó un escritor: Karel Čapek, en una obra de teatro de 1920. Viene de una palabra checa que significa «trabajo forzado».', 'emoji': '🤖',
  'voz': ['¿Sabías que la palabra *robot* la inventó un escritor?', 'Fue el checo Karel Čapek, en una obra de teatro de 1920. Viene de una palabra que significa «trabajo forzado», y en su obra los robots terminan rebelándose.']},
 {'t': 'pasos', 'titulo': 'LAS LEYES DE LOS ROBOTS', 'items': ['No dañar a ningún ser humano', 'Obedecer a los humanos', 'Protegerse a sí mismo'],
  'voz': ['A mediados del siglo veinte, el escritor Isaac Asimov imaginó tres leyes que todo robot debía cumplir, en este orden.', 'Primera: no dañar a ningún ser humano.', 'Segunda: obedecer a los humanos, salvo que eso dañe a alguien.', 'Tercera: protegerse a sí mismo, siempre que no rompa las otras dos. Sus cuentos muestran qué pasa cuando esas leyes chocan.']},
 {'t': 'causas', 'causa': {'txt': 'Un invento nuevo', 'emoji': '💡'}, 'items': ['cambia el trabajo', 'cambia las relaciones', 'trae nuevos peligros'],
  'voz': ['La ciencia ficción se pregunta por las *consecuencias* de un invento.', 'Puede cambiar el trabajo: ¿quién hace lo que hacen las máquinas?', 'Puede cambiar las relaciones: ¿cómo nos comunicamos?', 'Y puede traer peligros nuevos que nadie había previsto.']},
 {'t': 'comparar', 'a': {'cab': 'Anticipación', 'texto': 'imagina inventos que después existen', 'emoji': '🔭'}, 'b': {'cab': 'Advertencia', 'texto': 'muestra los riesgos de un avance', 'emoji': '⚠️'}, 'signo': '+',
  'voz': ['Por eso el género cumple dos funciones.', 'La *anticipación*: Verne imaginó submarinos y viajes a la Luna antes de que existieran.', 'La *advertencia*: muchas historias muestran los riesgos de un avance para que lo pensemos antes de que ocurra.']},
 {'t': 'pregunta', 'pregunta': 'Un cuento muestra una ciudad donde las máquinas deciden todo y nadie sabe ya cómo funcionan. ¿Qué función cumple?', 'opciones': ['Advertencia', 'Anticipación', 'Ninguna'], 'correcta': 0,
  'voz': ['Pregunta: un cuento muestra una ciudad donde las máquinas deciden todo y nadie sabe ya cómo funcionan. ¿Qué función cumple?', 'Pensá qué quiere que pensemos.', '*Advertencia*: nos muestra un riesgo de depender por completo de la tecnología.']},
 {'t': 'errores', 'items': [{'mal': 'La ciencia ficción está en contra de la tecnología', 'bien': 'Muestra posibilidades y riesgos para pensarlos'}, {'mal': 'Si un invento del relato no existe, el relato falló', 'bien': 'Lo que importa es lo que el invento dice de las personas'}],
  'voz': ['Dos errores para evitar.', 'La ciencia ficción no está en contra de la tecnología: muestra posibilidades y riesgos para que los pensemos.', 'Y no importa si el invento existe o no: importa lo que dice sobre las personas.']},
 {'t': 'resumen', 'items': [['Robot', 'palabra inventada por Čapek en 1920'], ['Leyes de Asimov', 'no dañar, obedecer, protegerse'], ['Anticipación', 'imaginar inventos antes de que existan'], ['Advertencia', 'mostrar riesgos de un avance']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 3'},
  'voz': ['Repasemos.', 'La ciencia ficción piensa la tecnología y sus efectos.', 'El robot.', 'Las leyes de Asimov.', 'La anticipación.', 'Y la advertencia. ¡A practicar!']},
]
CL['4'] = [
 {'t': 'historia', 'personaje': {'nombre': 'El viajero', 'emoji': '🧑‍🔬'}, 'lugar': '⏳', 'lineas': ['Un científico sube a su máquina y viaja al año 802.701.', 'Encuentra una humanidad dividida en dos especies.'], 'titulo': 'VIAJES', 'sub': 'en el tiempo y el espacio',
  'voz': ['En La máquina del tiempo, de Wells, un científico sube a su invento y viaja al año 802.701.', 'Allí encuentra a la humanidad dividida en dos especies: unos viven en la superficie sin trabajar, y otros, bajo tierra, haciendo funcionar las máquinas.', 'El viaje le sirve al autor para preguntarse adónde nos llevan las diferencias sociales. Hoy vemos los grandes *viajes* de la ciencia ficción.']},
 {'t': 'definicion', 'palabra': 'Paradoja temporal', 'texto': 'Contradicción que surge cuando un viaje al pasado cambia algo que hace imposible el propio viaje.', 'emoji': '🌀',
  'voz': ['Los viajes en el tiempo traen un problema famoso: la *paradoja temporal*.', 'Es la contradicción que aparece cuando un viajero cambia el pasado de tal forma que su propio viaje ya no podría haber ocurrido.']},
 {'t': 'ciclo', 'titulo': 'LA PARADOJA', 'items': ['Viaja al pasado', 'Impide que se conozcan sus padres', 'No nace', '¿Quién viajó entonces?'],
  'voz': ['Mirá el círculo imposible.', 'Alguien viaja al pasado.', 'Por accidente, impide que sus padres se conozcan.', 'Entonces nunca nace.', 'Pero si nunca nació, ¿quién viajó al pasado? Los relatos juegan con estas preguntas sin respuesta.']},
 {'t': 'zoom', 'niveles': [{'emoji': '🌍', 'txt': 'la Tierra: el punto de partida'}, {'emoji': '🔴', 'txt': 'la Luna y Marte: los primeros destinos'}, {'emoji': '🌌', 'txt': 'otras galaxias: lo desconocido'}],
  'voz': ['Los viajes espaciales empiezan en la Tierra, muchas veces desde lugares reales que el autor conocía.', 'Los primeros destinos imaginados fueron la Luna y Marte, como en Verne y Holmberg.', 'Después, otras galaxias. Pero lo importante no es el lugar: es lo que el viaje le muestra al personaje, y al lector, sobre la humanidad.']},
 {'t': 'dilema', 'situacion': 'Una nave llega a un planeta habitado. Los tripulantes pueden presentarse o esconderse.', 'emoji': '👽', 'a': {'txt': 'Presentarse', 'consecuencia': 'arriesgarse a un encuentro desconocido', 'emoji': '🤝'}, 'b': {'txt': 'Esconderse', 'consecuencia': 'observar sin ser vistos, pero sin conocer de verdad', 'emoji': '🫣'},
  'voz': ['Un dilema clásico: una nave llega a un planeta habitado.', 'Si los tripulantes se presentan, arriesgan un encuentro con lo desconocido.', 'Si se esconden, observan sin ser vistos, pero nunca conocen de verdad al otro. El encuentro con extraterrestres es, en el fondo, una pregunta sobre cómo tratamos a quien es distinto.']},
 {'t': 'quiz4', 'pregunta': 'En La guerra de los mundos (1898), los marcianos invasores son vencidos al final por…', 'opciones': ['Las bacterias terrestres', 'Un ejército de robots', 'Un superhéroe', 'Una tormenta'], 'correcta': 0,
  'voz': ['Pregunta: en La guerra de los mundos, de Wells, los marcianos invaden la Tierra. ¿Qué los vence al final?', 'Pensá en algo diminuto.', '*Las bacterias terrestres*: los invasores no tienen defensas contra ellas. La victoria no la logran los humanos, sino la naturaleza.']},
 {'t': 'logro', 'titulo': '¡Misión cumplida!', 'items': ['Qué es la ciencia ficción', 'Mundos posibles: utopías y distopías', 'Ciencia, tecnología y sociedad', 'Viajes en el tiempo y el espacio'], 'xp': 100,
  'voz': ['¡Terminaste las clases de la misión!', 'Ya sabés qué es la ciencia ficción.', 'Conocés los mundos posibles, las utopías y las distopías.', 'Pensaste la relación entre tecnología y sociedad.', 'Y viajaste en el tiempo y el espacio. ¡A practicar!']},
]
for n, esc in CL.items():
    json.dump({'slug': f'leng1-m11-n{n}', 'step_id': STEP[n], 'materia': 'Lengua y Literatura I', 'titulo': TIT[n], 'sub': f'Lengua y Literatura I · Misión 11 · Nivel {n}', 'escenas': esc},
              open(os.path.join(RAIZ, 'tools/clase/lecciones', f'leng1-m11-n{n}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ============================ LECCIÓN ============================
L = {}
L['1'] = {'temas': [
 T('Qué es la ciencia ficción',
   m('esquema', items=[
     {'nombre': 'De la Tierra a la Luna', 'raiz': 'el francés Verne, De la Tierra a la Luna (1865)', 'ramas': [['La pregunta', ['¿qué pasaría si pudiéramos llegar a la Luna?'], 'El punto de partida.'], ['La explicación', ['un cañón gigante dispara una cápsula con pasajeros'], 'Una solución que suena científica.'], ['Las consecuencias', ['los viajeros enfrentan el vacío, el frío y la falta de gravedad'], 'Lo que el invento cambia.'], ['El efecto', ['el lector cree que es posible'], 'La verosimilitud científica.']], 'cierre': 'Pregunta, explicación y consecuencias: la base del género.'},
     {'nombre': 'Frankenstein', 'raiz': 'Mary Shelley, Frankenstein (1818)', 'ramas': [['La pregunta', ['¿qué pasaría si un científico creara vida?'], 'El punto de partida.'], ['La explicación', ['la electricidad y la química del siglo diecinueve'], 'La ciencia de su época.'], ['Las consecuencias', ['la criatura es rechazada y el creador no se hace cargo'], 'El costo humano del experimento.'], ['El efecto', ['el lector se pregunta por la responsabilidad del científico'], 'Una reflexión que sigue vigente.']], 'cierre': 'Para muchos, la primera novela de ciencia ficción.'}]),
   m('elegir_x', consigna='¿Cuál de estos argumentos es de ciencia ficción?', items=[
     {'cons': 'Elegí el argumento de ciencia ficción.', 'ops': ['Un chip permite leer la mente de los demás y nadie puede guardar secretos', 'Una princesa es hechizada por una bruja y duerme cien años', 'Un detective descubre quién robó un collar en un tren'], 'ayuda': 'Buscá un avance científico o tecnológico.'},
     {'cons': 'Elegí el argumento de ciencia ficción.', 'ops': ['Una sonda encuentra agua en una luna de Júpiter y algo se mueve debajo del hielo', 'Un dragón protege un tesoro en una montaña', 'Dos amigos se pelean por un partido de fútbol'], 'ayuda': 'Fijate cuál se explica con ciencia.'},
     {'cons': 'Elegí el argumento de ciencia ficción.', 'ops': ['Una empresa vende robots que cuidan a los abuelos, pero empiezan a decidir por ellos', 'Un hada madrina convierte una calabaza en carruaje', 'Un caballero desterrado recupera su honor'], 'ayuda': 'Tecnología y sus consecuencias.'}]),
   ('Ciencia ficción', 'La ciencia ficción es el género que imagina, con una base científica o tecnológica, cómo cambiarían las personas y el mundo ante un avance o un descubrimiento.'),
   'Todo relato del género parte de una pregunta del tipo «¿qué pasaría si…?» y la responde con una explicación que suena científica, aunque sea inventada. Lo que más le interesa no es el invento en sí, sino lo que les pasa a las personas: cómo cambian su vida, sus relaciones y sus decisiones.',
   ['Parte de un «¿qué pasaría si…?».', 'Explica lo extraordinario con ciencia.', 'Se interesa por las consecuencias humanas.']),
 T('Ciencia ficción y maravilloso',
   m('versiones', rotulo='Relato', items=[
     {'nombre': 'Maravilloso', 'texto': '{{Un hada tocó al perro con su varita y el perro empezó a hablar.|Lo imposible se explica con magia: nadie se sorprende.}}'},
     {'nombre': 'Ciencia ficción', 'texto': '{{La veterinaria le implantó al perro un traductor neuronal y el perro empezó a hablar.|Lo imposible se explica con tecnología: suena posible.}}'},
     {'nombre': 'Maravilloso', 'texto': '{{El mago abrió una puerta en el aire y apareció en otro reino.|Magia.}}'},
     {'nombre': 'Ciencia ficción', 'texto': '{{El túnel de energía de la estación abrió un paso hacia otra galaxia.|Una máquina, aunque inventada, lo explica.}}'}]),
   m('clasificar_x', consigna='¿Ciencia ficción o maravilloso? Fijate en cómo se explica lo imposible.', cajas=['Ciencia ficción', 'Maravilloso'], cuantos=6, items=[
     ['Una cápsula congela a los viajeros para un viaje de doscientos años', 0], ['Un androide aprende a sentir celos', 0], ['Una vacuna permite respirar bajo el agua', 0],
     ['Un genio de la lámpara concede tres deseos', 1], ['Una bruja convierte al príncipe en sapo', 1], ['Un anillo mágico vuelve invisible a quien lo usa', 1]]),
   ('Verosimilitud científica', 'La verosimilitud científica es la apariencia de posibilidad que logra la ciencia ficción al explicar lo extraordinario con leyes, máquinas o descubrimientos, aunque sean inventados.'),
   'El maravilloso no necesita explicar nada: los hechizos y las hadas forman parte de su mundo. La ciencia ficción, en cambio, se esfuerza para que lo imposible parezca posible, y por eso usa términos científicos, inventos y datos. Esa diferencia está en cómo se explica lo extraordinario, no en lo extraordinario mismo.',
   ['Maravilloso: magia, sin explicación.', 'Ciencia ficción: ciencia, aunque inventada.', 'La diferencia está en cómo se explica.']),
 T('Los pioneros del género',
   m('linea_tiempo', items=[
     {'nombre': 'Pioneros', 'hechos': [{'t': '1818 · Mary Shelley publica Frankenstein', 'c': 1}, {'t': '1865 · Verne imagina un viaje a la Luna', 'c': 2}, {'t': '1875 · Eduardo Holmberg cuenta el viaje de un porteño a Marte', 'c': 3}, {'t': '1895 · Wells inventa La máquina del tiempo', 'c': 4}, {'t': '1898 · Wells imagina una invasión marciana', 'c': 5}],
      'marca': 'En menos de cien años nacen los grandes temas del género.', 'cierre': 'Vida artificial, viajes espaciales, tiempo y extraterrestres.'}]),
   m('unir_x', consigna='Uní cada obra con el tema de ciencia ficción que inaugura.', items=[
     {'pares': [['Frankenstein', 'la creación de vida artificial'], ['De la Tierra a la Luna', 'el viaje espacial'], ['La máquina del tiempo', 'el viaje temporal'], ['La guerra de los mundos', 'la invasión extraterrestre']]}]),
   ('Pioneros de la ciencia ficción', 'Los pioneros de la ciencia ficción son los autores del siglo diecinueve que crearon los grandes temas del género, como Mary Shelley, el francés Verne, Eduardo Holmberg y el inglés Wells.'),
   'Escribieron en una época de enormes cambios: trenes, electricidad, fábricas, telescopios cada vez más potentes. Imaginaron hacia dónde podía llevar todo eso, con entusiasmo y también con miedo. El argentino Holmberg muestra que el género también se escribió muy temprano en nuestro país.',
   ['Siglo diecinueve: época de inventos.', 'Shelley, Verne, Holmberg, Wells.', 'Crearon los grandes temas del género.'])],
 'recuerda': [
   R('Ciencia ficción', 'es el género que imagina, con base científica, cómo cambiarían las personas ante un avance o descubrimiento.', 'Un cañón gigante lleva viajeros a la Luna'),
   R('¿Qué pasaría si…?', 'es la pregunta que pone en marcha un relato de ciencia ficción.', '¿Qué pasaría si un científico creara vida?'),
   R('Verosimilitud científica', 'es la apariencia de posibilidad que se logra explicando lo extraordinario con ciencia.', 'Un traductor neuronal hace hablar al perro'),
   R('Maravilloso', 'es el relato donde lo imposible se explica con magia y no necesita justificación.', 'El hada toca al perro con su varita'),
   R('Pioneros', 'son los autores del siglo diecinueve que crearon los grandes temas del género.', 'Shelley, Verne, Holmberg y Wells')]}

L['2'] = {'temas': [
 T('El mundo posible',
   m('marcar', rotulo='Mundo', items=[
     {'nombre': 'Ciudad Abismo', 'texto': 'En el año 2400, {{la ciudad de Abismo flota a doscientos metros bajo el mar|El lugar: un escenario imaginado.}}. {{Sus habitantes respiran gracias a branquias implantadas al nacer|La tecnología que cambia la vida.}} y {{está prohibido subir a la superficie|Una regla de ese mundo.}}, porque {{se considera que allí arriba el aire es veneno|Una creencia o costumbre de sus habitantes.}}.', 'cierre': 'Lugar, tecnología, reglas y costumbres: un mundo completo.'},
     {'nombre': 'La colonia', 'texto': '{{En Marte, la colonia Esperanza vive bajo una cúpula de cristal|El lugar.}}. {{El agua se fabrica a partir del hielo de los polos|La tecnología.}}, {{cada familia tiene un cupo de agua por día|Una regla que organiza la vida.}} y {{la fiesta más importante celebra la primera lluvia artificial|Una costumbre propia.}}.', 'cierre': 'Los detalles hacen creíble el mundo.'}]),
   m('clasificar_x', consigna='¿Qué aspecto del mundo posible describe cada dato?', cajas=['Tecnología', 'Reglas', 'Costumbres'], cuantos=6, items=[
     ['Los autos vuelan guiados por satélite', 0], ['Un implante traduce todos los idiomas', 0], ['Está prohibido tener más de un robot por casa', 1],
     ['Los menores de 15 no pueden usar el teletransporte', 1], ['Para saludar, se tocan las palmas de las manos', 2], ['Cada año se celebra el día en que llegaron a Marte', 2]]),
   ('Mundo posible', 'El mundo posible es el escenario imaginado de un relato de ciencia ficción, con su propio lugar, tecnología, reglas y costumbres.'),
   'Un buen mundo posible no se describe todo de golpe: el lector lo va conociendo a través de detalles que aparecen en la historia, como un objeto, una prohibición o una fiesta. Cuantos más detalles coherentes tiene, más creíble resulta.',
   ['Lugar, tecnología, reglas y costumbres.', 'Se conoce de a poco, por detalles.', 'Más detalles coherentes, más credibilidad.']),
 T('Utopía y distopía',
   m('versiones', rotulo='Sociedad', items=[
     {'nombre': 'Utopía', 'texto': '{{En la isla, nadie pasa hambre: la comida se reparte según lo que cada uno necesita|Una sociedad ideal y justa.}}, {{y las decisiones se toman entre todos|Libertad y participación.}}.'},
     {'nombre': 'Distopía', 'texto': '{{En la ciudad, nadie pasa hambre: cada uno recibe la misma pastilla nutritiva|Parece ideal.}}, pero {{quien se queja pierde su ración y una cámara vigila cada casa|Detrás de la perfección, el control.}}.'}]),
   m('clasificar_x', consigna='¿Rasgo de una utopía o de una distopía?', cajas=['Utopía', 'Distopía'], cuantos=6, items=[
     ['Todos pueden opinar y decidir', 0], ['No existe la pobreza y nadie pasa necesidad', 0], ['Las personas viven en armonía con la naturaleza', 0],
     ['Un gobierno vigila cada conversación', 1], ['Está prohibido leer libros', 1], ['Las emociones se controlan con medicamentos obligatorios', 1]]),
   ('Utopía y distopía', 'La utopía es una sociedad imaginada como ideal y justa; la distopía es una sociedad imaginada que parece perfecta pero controla y oprime a las personas.'),
   'Las distopías son muy frecuentes en la ciencia ficción porque funcionan como advertencias: toman algo que ya existe, como la vigilancia o la desigualdad, y lo llevan al extremo. Muchas veces el protagonista es alguien que empieza a dudar y descubre lo que hay detrás de la apariencia perfecta.',
   ['Utopía: sociedad ideal.', 'Distopía: perfección aparente y control.', 'La distopía advierte sobre el presente.']),
 T('La coherencia del mundo',
   m('marcar', rotulo='Fragmento', items=[
     {'nombre': 'Coherente', 'texto': '{{En Kepler-9 la gravedad es la mitad que en la Tierra|La regla del mundo.}}. Por eso {{los chicos juegan al vóley con redes de seis metros|Una consecuencia coherente.}} y {{los ancianos usan botas con plomo para no tropezar en los saltos|Otra consecuencia que respeta la regla.}}.', 'cierre': 'Cada detalle se desprende de la regla.'},
     {'nombre': 'Incoherente', 'texto': '{{En la estación espacial no hay gravedad|La regla.}}. {{Lía se sirvió un vaso de agua, que se quedó quieto sobre la mesa|Rompe la regla: sin gravedad, el agua flotaría.}}.', 'cierre': 'Un error así hace que el lector deje de creer.'}]),
   m('elegir_x', consigna='¿Es coherente con las reglas del mundo?', items=[
     {'cons': 'En una ciudad donde la electricidad está prohibida, la protagonista lee de noche con una linterna eléctrica.', 'ops': ['No: rompe la regla del mundo', 'Sí: es un detalle sin importancia', 'Sí: las linternas no usan electricidad'], 'ayuda': 'Pensá en la regla principal.'},
     {'cons': 'En un planeta donde siempre es de noche, los habitantes tienen ojos enormes y piel muy pálida.', 'ops': ['Sí: es una consecuencia de vivir sin luz', 'No: debería haber sol', 'No: los ojos no tienen relación'], 'ayuda': 'Los detalles se desprenden de la regla.'},
     {'cons': 'En un mundo donde nadie puede mentir, un personaje engaña a todos sin explicación.', 'ops': ['No: contradice la regla si no se explica', 'Sí: es un giro sorpresa', 'Sí: mentir es normal'], 'ayuda': 'Una excepción necesita explicación.'}]),
   ('Coherencia interna', 'La coherencia interna es la cualidad de un mundo posible que respeta sus propias reglas a lo largo de todo el relato.'),
   'El lector de ciencia ficción acepta casi cualquier punto de partida, pero exige que después todo sea coherente con él. Si una regla se rompe, tiene que haber una explicación, y esa ruptura suele convertirse en el conflicto de la historia.',
   ['El lector acepta el punto de partida.', 'Exige coherencia con las reglas.', 'Una regla rota debe explicarse.'])],
 'recuerda': [
   R('Mundo posible', 'es el escenario imaginado de la ciencia ficción, con su lugar, tecnología, reglas y costumbres.', 'Abismo, una ciudad bajo el mar'),
   R('Utopía', 'es una sociedad imaginada como ideal y justa, donde las personas viven en armonía.', 'Nadie pasa hambre y todos deciden'),
   R('Distopía', 'es una sociedad imaginada que parece perfecta pero controla y oprime a las personas.', 'Una cámara vigila cada casa'),
   R('Coherencia interna', 'es respetar las reglas del mundo posible durante todo el relato.', 'Sin gravedad, el agua flota')]}

L['3'] = {'temas': [
 T('Robots e inteligencias artificiales',
   m('marcar', rotulo='Relato', items=[
     {'nombre': 'Los robots de Čapek', 'texto': 'En la obra de teatro de Karel Čapek (1920), {{una fábrica produce obreros artificiales para hacer todo el trabajo|El invento: los primeros «robots».}}. {{Los humanos dejan de trabajar y dependen de ellos|Una consecuencia social.}}, hasta que {{los robots se rebelan|El conflicto: la creación se vuelve contra el creador.}}.', 'cierre': 'La palabra «robot» nació en la literatura.'},
     {'nombre': 'La niñera', 'texto': '{{Una familia compra un robot para cuidar a su hija|El invento.}}. {{La nena lo quiere más que a nadie|La relación humana con la máquina.}}, y {{la madre se pregunta si está bien que una máquina ocupe ese lugar|El dilema que plantea el relato.}}.', 'cierre': 'La pregunta no es técnica, es humana.'}]),
   m('elegir_x', consigna='¿Qué pregunta plantea cada relato sobre la tecnología?', items=[
     {'cons': 'Un robot debe elegir entre obedecer una orden o salvar a una persona en peligro.', 'ops': ['¿Qué pasa cuando las reglas de una máquina entran en conflicto?', '¿Cuánto cuesta un robot?', '¿De qué metal está hecho?'], 'ayuda': 'Pensá en el dilema.'},
     {'cons': 'Una inteligencia artificial escribe las tareas de todos los chicos de una ciudad.', 'ops': ['¿Qué pasa con el aprendizaje si las máquinas piensan por nosotros?', '¿Qué color tiene la pantalla?', '¿Cuántas tareas hay?'], 'ayuda': 'Las consecuencias humanas.'},
     {'cons': 'Un androide pide que lo traten como a una persona.', 'ops': ['¿Qué nos hace humanos?', '¿Cuánto pesa un androide?', '¿Quién lo fabricó?'], 'ayuda': 'La pregunta de fondo.'}]),
   ('Robot', 'El robot es una máquina capaz de realizar tareas por sí misma; la palabra fue inventada por Karel Čapek en 1920 y viene de un término checo que significa trabajo forzado.'),
   'Los relatos de robots e inteligencias artificiales casi nunca hablan de cables y engranajes: hablan de nosotros. Preguntan qué pasa con el trabajo, con los vínculos y con la responsabilidad cuando las máquinas pueden decidir. Por eso siguen siendo actuales, aunque algunos tengan más de cien años.',
   ['«Robot»: palabra de Čapek, 1920.', 'Preguntan por el trabajo y los vínculos.', 'En el fondo: ¿qué nos hace humanos?']),
 T('Las leyes de la robótica',
   m('esquema', items=[{'nombre': 'Tres leyes', 'cols': ['Ley', 'Qué dice', 'Qué conflicto puede traer'], 'filas': [
       ['Primera', 'un robot no puede dañar a un ser humano', '¿y si al no actuar alguien sale herido?'], ['Segunda', 'debe obedecer a los humanos, salvo que eso dañe a alguien', '¿y si dos humanos dan órdenes opuestas?'],
       ['Tercera', 'debe protegerse, salvo que eso rompa las anteriores', '¿y si salvarse pone en riesgo una misión?']], 'cierre': 'Isaac Asimov las imaginó para crear historias a partir de sus contradicciones.'}]),
   m('elegir_x', consigna='¿Qué ley de la robótica aplica cada robot?', items=[
     {'cons': 'Un robot se niega a empujar a una persona aunque su dueño se lo ordena.', 'ops': ['La primera: no dañar a un humano está por encima de obedecer', 'La tercera: protegerse', 'Ninguna'], 'ayuda': 'El orden de las leyes importa.'},
     {'cons': 'Un robot entra en un edificio en llamas para sacar a un chico, aunque se puede dañar.', 'ops': ['La primera: proteger al humano está por encima de protegerse', 'La tercera: debe cuidarse siempre', 'La segunda: nadie se lo ordenó'], 'ayuda': 'Proteger a un humano va primero.'},
     {'cons': 'Un robot de limpieza deja de barrer cuando su dueña le pide que se detenga.', 'ops': ['La segunda: obedecer a los humanos', 'La primera: no dañar', 'La tercera: protegerse'], 'ayuda': 'Es una orden sin riesgo para nadie.'}]),
   ('Leyes de la robótica', 'Las leyes de la robótica son tres reglas imaginadas por el escritor Isaac Asimov: un robot no puede dañar a un humano, debe obedecerlo y debe protegerse, en ese orden de importancia.'),
   'Asimov las inventó para un mundo de ficción, pero las usó con astucia: sus cuentos muestran casos donde las leyes chocan entre sí o donde una orden es ambigua. Así la ciencia ficción convierte una regla tecnológica en un problema ético que el lector tiene que pensar.',
   ['1: no dañar a un humano.', '2: obedecer, salvo que dañe.', '3: protegerse, salvo que rompa las otras.']),
 T('Anticipación y advertencia',
   m('marcar', rotulo='Relato', items=[
     {'nombre': 'Anticipación', 'texto': 'En una novela de 1870, Verne {{describe un submarino eléctrico que recorre los océanos durante meses|Un invento que todavía no existía.}}. {{Décadas después, los submarinos se volvieron reales|La ficción se adelantó a la ciencia.}}.', 'cierre': 'Imaginar antes de que exista.'},
     {'nombre': 'Advertencia', 'texto': '{{En una ciudad imaginada, las pantallas registran cada movimiento de sus habitantes|Lleva al extremo algo que ya existe.}}. {{Nadie se atreve a pensar distinto|La consecuencia que el relato quiere mostrar.}}.', 'cierre': 'Mostrar un riesgo para pensarlo a tiempo.'}]),
   m('clasificar_x', consigna='¿El relato funciona sobre todo como anticipación o como advertencia?', cajas=['Anticipación', 'Advertencia'], cuantos=6, items=[
     ['Un escritor del siglo diecinueve imagina videollamadas', 0], ['Una novela antigua describe un viaje a la Luna en una cápsula', 0], ['Un cuento imagina teléfonos que caben en el bolsillo', 0],
     ['Una ciudad donde las máquinas deciden quién puede trabajar', 1], ['Un mundo donde está prohibido desconectarse de internet', 1], ['Una sociedad que destruyó los bosques y ahora compra aire', 1]]),
   ('Anticipación y advertencia', 'La anticipación es la capacidad de la ciencia ficción de imaginar inventos antes de que existan; la advertencia es su función de mostrar los riesgos de un avance llevándolo al extremo.'),
   'No importa tanto si la ciencia ficción acierta o no con el futuro. Lo valioso es que nos obliga a pensar qué queremos hacer con la tecnología: aprovechar sus posibilidades sin perder la libertad, los vínculos ni el cuidado del planeta.',
   ['Anticipación: imaginar antes de que exista.', 'Advertencia: mostrar riesgos al extremo.', 'Invita a pensar qué hacemos con la tecnología.'])],
 'recuerda': [
   R('Robot', 'es una máquina que realiza tareas por sí misma; la palabra la inventó Karel Čapek en 1920.', 'Los obreros artificiales que se rebelan'),
   R('Leyes de la robótica', 'son tres reglas imaginadas por Asimov: no dañar a un humano, obedecerlo y protegerse.', 'El robot no empuja a nadie aunque se lo ordenen'),
   R('Anticipación', 'es la capacidad de imaginar inventos o situaciones antes de que existan en la realidad.', 'El submarino eléctrico de Verne'),
   R('Advertencia', 'es mostrar los riesgos de un avance llevándolo al extremo para pensarlo a tiempo.', 'Pantallas que registran cada movimiento'),
   R('Pregunta de fondo', 'la ciencia ficción, al hablar de máquinas, suele preguntarse qué nos hace humanos.', 'El androide que pide ser tratado como persona')]}

L['4'] = {'temas': [
 T('El viaje en el tiempo',
   m('marcar', rotulo='Relato', items=[
     {'nombre': 'La máquina del tiempo', 'texto': 'En la novela de Wells (1895), {{un científico construye una máquina que viaja por el tiempo|El invento que hace posible el viaje.}}. {{Llega al año 802.701|Un futuro lejanísimo.}} y {{encuentra a la humanidad dividida entre quienes viven en la superficie sin trabajar y quienes trabajan bajo tierra|Lo que el viaje revela: una crítica a la desigualdad de su época.}}.', 'cierre': 'El futuro sirve para hablar del presente.'}]),
   m('elegir_x', consigna='¿Para qué sirve el viaje en el tiempo en cada relato?', items=[
     {'cons': 'Una chica viaja cien años al futuro y descubre que su ciudad quedó bajo el agua.', 'ops': ['Para advertir sobre las consecuencias del cambio climático', 'Para mostrar cómo era la ciudad antes', 'Para contar una historia de amor medieval'], 'ayuda': 'Lo que ve en el futuro es un aviso.'},
     {'cons': 'Un historiador viaja al pasado para presenciar la Revolución de Mayo y entender qué pasó.', 'ops': ['Para conocer el pasado desde adentro', 'Para advertir sobre los robots', 'Para crear una distopía'], 'ayuda': 'Va a observar la historia.'},
     {'cons': 'Un científico viaja al futuro y encuentra a la humanidad dividida en dos especies.', 'ops': ['Para criticar la desigualdad de su propia época', 'Para mostrar un invento de cocina', 'Para escapar de un examen'], 'ayuda': 'Pensá en Wells.'}]),
   ('Viaje en el tiempo', 'El viaje en el tiempo es un tema de la ciencia ficción en el que un personaje se traslada al pasado o al futuro, generalmente gracias a una máquina o un descubrimiento.'),
   'Viajar al futuro permite mostrar adónde nos llevan las decisiones de hoy; viajar al pasado, preguntarse si se puede cambiar la historia. En los dos casos, el tiempo funciona como una lente para mirar el presente desde otro lugar.',
   ['Al futuro: adónde nos llevan nuestras decisiones.', 'Al pasado: ¿se puede cambiar la historia?', 'El tiempo es una lente para mirar el presente.']),
 T('Las paradojas temporales',
   m('linea_tiempo', items=[
     {'nombre': 'La paradoja', 'hechos': [{'t': 'En 2080, Leo construye una máquina del tiempo', 'c': 3}, {'t': 'Viaja a 2040 y, sin querer, impide que sus padres se conozcan', 'c': 4}, {'t': 'En 2040, sus padres iban a conocerse en una estación de tren', 'c': 1}, {'t': 'Si sus padres no se conocen, Leo no nace en 2055', 'c': 2}, {'t': '¿Quién construyó entonces la máquina en 2080?', 'c': 5}],
      'marca': 'El viaje destruye la causa del propio viaje.', 'cierre': 'Una contradicción sin salida: una paradoja.'}]),
   m('elegir_x', consigna='¿Hay paradoja temporal en cada caso?', items=[
     {'cons': 'Una viajera va al pasado y le da a un inventor la idea del motor que después usará su propia máquina del tiempo.', 'ops': ['Sí: la idea no tiene origen, viene del futuro', 'No: es un viaje común', 'No: los inventores no existen'], 'ayuda': '¿Quién inventó primero el motor?'},
     {'cons': 'Un turista del futuro visita el año 1900, saca fotos y vuelve sin tocar nada.', 'ops': ['No: no cambia nada del pasado', 'Sí: siempre hay paradoja', 'Sí: sacó fotos'], 'ayuda': 'La paradoja aparece si se altera el pasado.'},
     {'cons': 'Un chico viaja al pasado y evita el accidente que lo hizo querer construir la máquina.', 'ops': ['Sí: si no hay accidente, no hay motivo para el viaje', 'No: es un final feliz', 'No: nadie viaja'], 'ayuda': 'El viaje elimina su propia causa.'}]),
   ('Paradoja temporal', 'La paradoja temporal es la contradicción lógica que surge cuando un viaje al pasado altera los hechos que hicieron posible ese mismo viaje.'),
   'Los relatos resuelven las paradojas de distintas maneras: algunos dicen que el pasado no se puede cambiar, otros inventan líneas de tiempo paralelas. Para el lector, la gracia está en seguir el razonamiento y descubrir dónde está la contradicción.',
   ['Un viaje que destruye su propia causa.', 'Algunas historias: el pasado no cambia.', 'Otras: líneas de tiempo paralelas.']),
 T('Viajes espaciales y encuentros',
   m('marcar', rotulo='Relato', items=[
     {'nombre': 'La guerra de los mundos', 'texto': 'En la novela de Wells (1898), {{los marcianos llegan a Inglaterra con máquinas de guerra imposibles de detener|El encuentro como invasión.}}. {{Los humanos no logran vencerlos|La tecnología terrestre fracasa.}}, pero {{los invasores mueren por las bacterias de la Tierra, contra las que no tienen defensas|Un giro: la naturaleza decide.}}.', 'cierre': 'Wells escribió en plena época de conquistas coloniales: ¿y si ahora los invadidos fuéramos nosotros?'},
     {'nombre': 'El viaje a Marte', 'texto': 'En la novela de Holmberg (1875), {{un porteño viaja a Marte|El viaje espacial.}} y {{encuentra una sociedad con costumbres que le sirven para mirar con otros ojos la Buenos Aires de su tiempo|El otro planeta como espejo.}}.', 'cierre': 'Ir lejos para ver mejor lo propio.'}]),
   m('clasificar_x', consigna='¿Qué tipo de encuentro con extraterrestres plantea cada relato?', cajas=['Amenaza', 'Diálogo'], cuantos=6, items=[
     ['Naves gigantes atacan las capitales del mundo', 0], ['Unos visitantes secuestran el ganado de una estancia', 0], ['Una especie quiere quedarse con el agua de la Tierra', 0],
     ['Una científica aprende el idioma de los visitantes para entenderlos', 1], ['Unos extraterrestres piden ayuda porque su planeta se apaga', 1], ['Un chico se hace amigo de un ser que cayó en su campo', 1]]),
   ('Encuentro con el otro', 'El encuentro con extraterrestres es un tema de la ciencia ficción que, más allá de los seres de otros planetas, plantea cómo reaccionamos frente a quien es distinto: con miedo o con diálogo.'),
   'El viaje espacial y el contacto con otros seres permiten mirar a la humanidad desde afuera. Algunas historias muestran invasiones y miedo; otras, intentos de comunicación. En todos los casos, el otro planeta funciona como un espejo de nuestras propias costumbres y temores.',
   ['El viaje espacial muestra la Tierra desde afuera.', 'El encuentro puede ser amenaza o diálogo.', 'El otro planeta es un espejo de lo nuestro.'])],
 'recuerda': [
   R('Viaje en el tiempo', 'es el tema en que un personaje se traslada al pasado o al futuro gracias a una máquina o un descubrimiento.', 'La máquina del tiempo, de Wells'),
   R('Paradoja temporal', 'es la contradicción que surge cuando un viaje al pasado altera lo que hizo posible ese viaje.', 'Leo impide que sus padres se conozcan'),
   R('Viaje espacial', 'es el tema que lleva a los personajes a otros planetas y permite mirar la Tierra desde afuera.', 'Un porteño viaja a Marte'),
   R('Encuentro con el otro', 'es el contacto con seres de otros planetas, que plantea cómo reaccionamos ante lo distinto.', 'Los marcianos de La guerra de los mundos')]}

# ============================ ACTIVIDADES ============================
A = {
 '1': [
   CLA('¿Ciencia ficción o maravilloso? Fijate en cómo se explica lo imposible.', ['Ciencia ficción', 'Maravilloso'], [('Un traje con nanotecnología permite volar', 'Ciencia ficción'), ('Una escoba mágica permite volar', 'Maravilloso'), ('Una cámara criogénica congela a un astronauta', 'Ciencia ficción'), ('Un hechizo duerme a la princesa cien años', 'Maravilloso')], 'Ciencia o magia.', 'aplicar'),
   UNI('Uní cada pionero con su obra.', [('Mary Shelley', 'Frankenstein'), ('Julio Verne', 'De la Tierra a la Luna'), ('H. G. Wells', 'La máquina del tiempo'), ('Eduardo Holmberg', 'el viaje de un porteño a Marte')], 'Los grandes nombres del siglo diecinueve.', 'recordar'),
   MC('Un cuento empieza con la pregunta: «¿Qué pasaría si las personas pudieran vivir doscientos años?». ¿Qué rasgo del género muestra?', ['Parte de un «¿qué pasaría si…?» sobre un avance posible', 'Explica todo con magia', 'Cuenta un hecho histórico real'], 'Parte de un «¿qué pasaría si…?» sobre un avance posible', 'La pregunta pone en marcha el relato.', 'analizar'),
   MC('Un compañero dice que todo relato con extraterrestres es ciencia ficción, aunque los extraterrestres lleguen por un hechizo. ¿Qué le contestás?', ['Lo que define al género es la explicación científica', 'Tiene razón: alcanza con extraterrestres', 'Solo es ciencia ficción si pasa en el futuro'], 'Lo que define al género es la explicación científica', 'Si lo explica la magia, es maravilloso.', 'error')],
 '2': [
   CLA('¿Utopía o distopía?', ['Utopía', 'Distopía'], [('Todos deciden juntos y nadie pasa hambre', 'Utopía'), ('Las emociones se controlan con pastillas obligatorias', 'Distopía'), ('Las personas viven en armonía con la naturaleza', 'Utopía'), ('Una cámara vigila cada casa', 'Distopía')], 'Sociedad ideal o control disfrazado.', 'aplicar'),
   CLA('¿Qué aspecto del mundo posible es?', ['Tecnología', 'Reglas', 'Costumbres'], [('Los autos se manejan solos', 'Tecnología'), ('Está prohibido salir de la cúpula', 'Reglas'), ('Se saludan tocándose las palmas', 'Costumbres'), ('Un implante traduce idiomas', 'Tecnología')], 'Las piezas de un mundo posible.', 'aplicar'),
   MC('En un relato, la ciudad no tiene agua y todos la reciben racionada. En una escena, la protagonista llena una pileta para nadar sin explicación. ¿Qué falla?', ['La coherencia: rompe la regla del mundo sin explicarlo', 'Nada: es un detalle sin importancia', 'La pileta es una utopía'], 'La coherencia: rompe la regla del mundo sin explicarlo', 'Una regla rota necesita explicación.', 'analizar'),
   MC('Lucía dice que una distopía es cualquier relato triste. ¿Qué le falta entender?', ['Que la distopía es una sociedad de control que parece perfecta', 'Que las distopías son siempre alegres', 'Que la distopía es un tipo de robot'], 'Que la distopía es una sociedad de control que parece perfecta', 'Lo que la define es el control disfrazado de perfección.', 'error')],
 '3': [
   CLA('¿El relato funciona como anticipación o como advertencia?', ['Anticipación', 'Advertencia'], [('Un escritor de 1870 imagina un submarino eléctrico', 'Anticipación'), ('Una ciudad donde las máquinas deciden quién trabaja', 'Advertencia'), ('Una novela antigua imagina videollamadas', 'Anticipación'), ('Un mundo donde comprar aire es obligatorio', 'Advertencia')], 'Imaginar antes o mostrar un riesgo.', 'aplicar'),
   ORD('Ordená las tres leyes de la robótica de Asimov, de la más importante a la menos importante.', ['No dañar a un ser humano', 'Obedecer a los humanos', 'Protegerse a sí mismo'], 'El orden decide qué ley gana cuando chocan.', 'aplicar'),
   MC('Un robot recibe la orden de abrir una puerta, pero detrás hay una persona que se golpearía. No la abre. ¿Qué ley aplica?', ['La primera: no dañar a un humano está por encima de obedecer', 'La segunda: siempre hay que obedecer', 'La tercera: debe protegerse'], 'La primera: no dañar a un humano está por encima de obedecer', 'Las leyes tienen un orden de importancia.', 'analizar'),
   KW('¿Por qué decimos que los relatos de robots hablan, en el fondo, de los seres humanos? Explicalo con un ejemplo.', 'Pensá en las preguntas que plantean.', [['human*', 'persona*', 'nosotros', 'vínculo*', 'trabajo', 'sentir', 'emoci*'], ['robot*', 'máquina*', 'androide*', 'inteligencia artificial', 'ia']], 2, 'Por ejemplo: un androide que pide ser tratado como persona nos hace preguntar qué nos hace humanos.', 'analizar')],
 '4': [
   UNI('Uní cada relato con su tema.', [('Un científico viaja al año 802.701', 'viaje en el tiempo'), ('Marcianos invaden Inglaterra', 'encuentro con extraterrestres'), ('Un porteño viaja a Marte', 'viaje espacial'), ('Un chico impide que sus padres se conozcan', 'paradoja temporal')], 'Los grandes temas del nivel.', 'aplicar'),
   ORD('Ordená la paradoja de Leo como ocurre en el tiempo.', ['En 2040 sus padres iban a conocerse', 'Leo nace en 2055', 'En 2080 construye la máquina', 'Viaja a 2040 e impide que sus padres se conozcan'], 'Por qué el viaje se vuelve imposible.', 'analizar'),
   SA('En La guerra de los mundos, los marcianos no son vencidos por las armas humanas. ¿Qué los vence?', ['las bacterias', 'bacterias', 'las bacterias de la tierra', 'los microbios', 'microbios'], 'Un giro: la naturaleza decide.', 'aplicar'),
   MC('Un relato muestra a una científica que aprende el idioma de unos visitantes para entenderlos. ¿Qué tipo de encuentro plantea?', ['Un encuentro de diálogo con el otro', 'Una invasión amenazante', 'Una paradoja temporal'], 'Un encuentro de diálogo con el otro', 'Comunicarse en lugar de pelear.', 'analizar')],
 '5': [
   CLA('¿Qué tema de la ciencia ficción aparece?', ['Robots', 'Distopía', 'Viaje en el tiempo', 'Viaje espacial'], [('Una máquina que obedece y cuida a una nena', 'Robots'), ('Una ciudad perfecta donde todo se vigila', 'Distopía'), ('Un viajero llega al siglo XXX', 'Viaje en el tiempo'), ('Una nave llega a una luna de Júpiter', 'Viaje espacial')], 'Repasá los temas de la misión.', 'analizar'),
   ODD('Tres argumentos son de ciencia ficción y uno no. ¿Cuál no?', ['Un chip permite grabar los sueños', 'Una colonia vive bajo una cúpula en Marte', 'Un robot aprende a mentir', 'Un hada concede tres deseos'], 'Un hada concede tres deseos', 'La magia es del maravilloso.', 'analizar'),
   MS('Una novela muestra una ciudad donde nadie trabaja porque todo lo hacen los robots, y la gente ya no sabe hacer nada. Elegí las DOS cosas que hace el relato.', ['Advierte sobre depender de la tecnología', 'Imagina las consecuencias sociales de un invento', 'Explica todo con magia', 'Cuenta un hecho histórico real'], ['Advierte sobre depender de la tecnología', 'Imagina las consecuencias sociales de un invento'], 'Advertencia y consecuencias humanas.'),
   MC('¿Por qué decimos que la ciencia ficción habla del presente, aunque transcurra en el futuro?', ['Porque lleva al extremo preocupaciones y posibilidades de hoy', 'Porque siempre ocurre en la actualidad', 'Porque no tiene inventos'], 'Porque lleva al extremo preocupaciones y posibilidades de hoy', 'El futuro es una lente para mirar el presente.', 'analizar')],
}

EX = [
 [1, MC('¿Qué distingue a la ciencia ficción del relato maravilloso?', ['Explica lo extraordinario con ciencia, aunque sea inventada', 'Tiene personajes imaginarios', 'Ocurre siempre en otro planeta'], 'Explica lo extraordinario con ciencia, aunque sea inventada', 'La diferencia está en la explicación.', 'recordar')],
 [1, CLA('¿Ciencia ficción o maravilloso?', ['Ciencia ficción', 'Maravilloso'], [('Un implante permite hablar con los animales', 'Ciencia ficción'), ('Un hada convierte una calabaza en carruaje', 'Maravilloso'), ('Una cápsula viaja a la Luna disparada por un cañón', 'Ciencia ficción')], 'Ciencia o magia.', 'aplicar')],
 [1, UNI('Uní cada pionero con su obra.', [('Mary Shelley', 'Frankenstein'), ('Julio Verne', 'De la Tierra a la Luna'), ('H. G. Wells', 'La máquina del tiempo')], 'Los pioneros del género.', 'recordar')],
 [2, CLA('¿Utopía o distopía?', ['Utopía', 'Distopía'], [('Nadie pasa hambre y todos deciden', 'Utopía'), ('Está prohibido leer libros', 'Distopía'), ('Un gobierno escucha cada conversación', 'Distopía')], 'Sociedad ideal o control.', 'aplicar')],
 [2, MC('En un mundo sin gravedad, un personaje apoya un vaso de agua en la mesa y el agua queda quieta. ¿Qué problema tiene el relato?', ['Rompe su coherencia interna', 'Es una distopía', 'No tiene ningún problema'], 'Rompe su coherencia interna', 'Sin gravedad, el agua flotaría.', 'analizar')],
 [2, SA('¿Cómo se llama la sociedad imaginada que parece perfecta pero controla y oprime a las personas?', ['distopía', 'distopia', 'una distopía'], 'La distopía.', 'recordar')],
 [3, ORD('Ordená las leyes de la robótica de Asimov por orden de importancia.', ['No dañar a un humano', 'Obedecer', 'Protegerse'], 'El orden decide cuál gana.', 'aplicar')],
 [3, CLA('¿Anticipación o advertencia?', ['Anticipación', 'Advertencia'], [('Imaginar submarinos antes de que existan', 'Anticipación'), ('Mostrar una ciudad donde todo se vigila', 'Advertencia'), ('Imaginar viajes a la Luna en 1865', 'Anticipación')], 'Imaginar antes o mostrar riesgos.', 'aplicar')],
 [3, MC('¿De dónde viene la palabra «robot»?', ['De una obra de teatro de Karel Čapek (1920)', 'De un invento de Julio Verne', 'De un laboratorio de Estados Unidos'], 'De una obra de teatro de Karel Čapek (1920)', 'Nació en la literatura.', 'recordar')],
 [4, MC('Un viajero va al pasado y evita el accidente que lo llevó a construir su máquina del tiempo. ¿Qué se produce?', ['Una paradoja temporal', 'Una utopía', 'Un encuentro con extraterrestres'], 'Una paradoja temporal', 'El viaje elimina su propia causa.', 'analizar')],
 [4, CLA('¿Encuentro de amenaza o de diálogo?', ['Amenaza', 'Diálogo'], [('Naves atacan las capitales del mundo', 'Amenaza'), ('Una científica aprende el idioma de los visitantes', 'Diálogo'), ('Unos seres piden ayuda porque su planeta se apaga', 'Diálogo')], 'Cómo reaccionamos ante lo distinto.', 'aplicar')],
 [4, MC('¿Para qué le sirve a Wells el viaje al año 802.701 en La máquina del tiempo?', ['Para criticar la desigualdad de su propia época', 'Para explicar cómo funciona un reloj', 'Para mostrar un futuro sin cambios'], 'Para criticar la desigualdad de su propia época', 'El futuro como lente del presente.', 'analizar')],
 [4, KW('Explicá con tus palabras qué es la ciencia ficción y por qué decimos que habla del presente aunque ocurra en el futuro.', 'Definí el género y explicá la relación con el presente.', [['ciencia', 'científic*', 'tecnolog*', 'invento*', 'avance*'], ['futuro'], ['presente', 'hoy', 'actual*', 'nuestra época', 'advert*', 'preocup*']], 3, 'Por ejemplo: imagina avances científicos y sus consecuencias; aunque ocurra en el futuro, muestra preocupaciones de hoy.', 'aplicar')],
]

CARP = {
 '1': [
  ('Un cuento imagina que una vacuna permite a las personas respirar bajo el agua. ¿Es ciencia ficción o maravilloso?', 'aplicar', ['ciencia ficción', 'ciencia ficcion'], 'Ciencia ficción: lo imposible se explica con un avance científico.'),
  ('En otro cuento, un hada convierte a un chico en pez para que pueda respirar bajo el agua. ¿Qué tipo de relato es?', 'aplicar', ['maravilloso', 'relato maravilloso', 'el maravilloso'], 'Maravilloso: lo explica la magia.'),
  ('Casi todo relato de ciencia ficción parte de una pregunta que empieza siempre igual, como «¿… si pudiéramos llegar a la Luna?». ¿Con qué palabras empieza?', 'analizar', ['qué pasaría si', 'que pasaria si', '¿qué pasaría si?', 'qué pasaría'], '«¿Qué pasaría si…?»: la pregunta que pone en marcha el relato.'),
  ('Lucas dice que la ciencia ficción solo habla del futuro y no tiene nada que ver con nuestra vida. ¿De qué época habla en realidad?', 'error', ['del presente', 'presente', 'de hoy'], 'Del presente: lleva al extremo lo que hoy nos preocupa o entusiasma.'),
 ],
 '2': [
  ('En una ciudad imaginada, nadie pasa hambre, todos deciden juntos y la naturaleza está cuidada. ¿Es una utopía o una distopía?', 'aplicar', ['utopía', 'utopia', 'una utopía'], 'Utopía: una sociedad ideal y justa.'),
  ('En otra ciudad, todos sonríen porque un sensor castiga a quien está triste. ¿Es una utopía o una distopía?', 'aplicar', ['distopía', 'distopia', 'una distopía'], 'Distopía: parece perfecta, pero controla a las personas.'),
  ('En un planeta donde siempre es de noche, los habitantes tienen ojos enormes. ¿Por qué ese detalle hace creíble el mundo?', 'analizar', ['es coherente', 'coherencia', 'respeta las reglas', 'coherente con la regla'], 'Es coherente con la regla del mundo: sin luz, los ojos se adaptan.'),
  ('Tomi dice que un mundo posible puede cambiar sus reglas cuando le conviene al autor. ¿Qué tiene que respetar un mundo posible?', 'error', ['sus reglas', 'la coherencia', 'coherencia', 'sus propias reglas'], 'Sus propias reglas: si las rompe, el lector deja de creer.'),
 ],
 '3': [
  ('Un robot se niega a empujar a una persona, aunque su dueño se lo ordena. ¿Qué ley de la robótica aplica?', 'aplicar', ['la primera', 'primera', '1', 'la primera ley'], 'La primera: no dañar a un humano está por encima de obedecer.'),
  ('En 1870, Verne describió un submarino eléctrico que todavía no existía. ¿Qué función de la ciencia ficción muestra?', 'aplicar', ['anticipación', 'anticipacion', 'la anticipación'], 'Anticipación: imaginar un invento antes de que exista.'),
  ('Un cuento muestra una ciudad donde las máquinas deciden todo y nadie sabe pensar solo. ¿Qué función cumple?', 'analizar', ['advertencia', 'la advertencia', 'advertir'], 'Advertencia: muestra un riesgo llevándolo al extremo.'),
  ('Mica dice que la ciencia ficción está en contra de la tecnología. ¿Qué muestra en realidad sobre los avances?', 'error', ['posibilidades y riesgos', 'sus riesgos y posibilidades', 'riesgos', 'posibilidades'], 'Posibilidades y riesgos, para que los pensemos.'),
 ],
 '4': [
  ('Un científico viaja al futuro en una máquina y descubre a la humanidad dividida en dos especies. ¿Qué tema de la ciencia ficción es?', 'aplicar', ['viaje en el tiempo', 'el viaje en el tiempo', 'viajes en el tiempo'], 'El viaje en el tiempo, como en la novela de Wells.'),
  ('Leo viaja al pasado y, sin querer, impide que sus padres se conozcan. ¿Qué contradicción se produce?', 'analizar', ['paradoja temporal', 'una paradoja', 'paradoja'], 'Una paradoja temporal: si no nace, no pudo viajar.'),
  ('En La guerra de los mundos, los marcianos invasores no son vencidos por las armas. ¿Qué los vence?', 'recordar', ['las bacterias', 'bacterias', 'las bacterias de la tierra'], 'Las bacterias de la Tierra, contra las que no tienen defensas.'),
  ('Sofi dice que los relatos de extraterrestres solo cuentan batallas. ¿Qué otro tipo de encuentro pueden plantear?', 'error', ['de diálogo', 'diálogo', 'dialogo', 'comunicación', 'amistad'], 'De diálogo: intentar comunicarse y entender al otro.'),
 ],
}

def ajustes(M):
    M['act'] = A
    M['examen'] = EX
    M['practica'] = 'Actividades generales'
    M['examen_titulo'] = 'Nivel jefe: la ciencia ficción'
    M['actualizar_preguntas'] = True
    for k, items in CARP.items():
        N = M['niveles'].setdefault(k, {})
        N['carpeta'] = [c for c, _, _, _ in items]; N['carpeta_nivel'] = [t for _, t, _, _ in items]
        N['respuestas_carpeta'] = [r for _, _, r, _ in items]; N.setdefault('soluciones', {})['carpeta'] = [s for _, _, _, s in items]

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-11/mision-11.json', L, ajustes=ajustes)
