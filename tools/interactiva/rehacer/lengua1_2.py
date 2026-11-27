# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 2 · El policial: del enigma al negro (TODO nuevo, sobre el GÉNERO; el libro va en el nivel 5)
# Libro del nivel: «La liga de los pelirrojos», de Arthur Conan Doyle (1891, dominio público).
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD
RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', '..')

# ============================ CLASES ANIMADAS ============================
STEP = {'1': 'a43342fa-65b1-47f7-b044-597883c9a1a2', '2': '35d71616-c7e2-4000-9579-86a55c4f3c7a', '3': 'b70f8efb-7ed8-46e7-a598-caf51740345b', '4': 'af7346be-4827-4ab0-a5c2-13ed09056a5d'}
TIT = {'1': 'El policial y sus personajes', '2': 'Pistas y deducción', '3': 'Las dos historias del policial', '4': 'Del enigma al policial negro'}
CL = {}
CL['1'] = [
 {'t': 'noticia', 'cinta': 'MISTERIO', 'titular': 'Desaparece un trofeo de una vitrina cerrada', 'bajada': 'La llave nunca salió del bolsillo del director', 'emoji': '🏆', 'titulo': 'EL POLICIAL', 'sub': 'un enigma por resolver',
  'voz': ['Un trofeo desaparece de una vitrina cerrada con llave.', 'Y la única llave nunca salió del bolsillo del director.', '¿Cómo pudo pasar? Esa pregunta es el motor de todo *relato policial*.']},
 {'t': 'definicion', 'palabra': 'Relato policial', 'texto': 'Narración que gira alrededor de un enigma, casi siempre un crimen, que alguien investiga hasta descubrir la verdad.', 'emoji': '🔍',
  'voz': ['Un *relato policial* gira alrededor de un *enigma*, casi siempre un crimen.', 'Alguien lo investiga paso a paso hasta descubrir la verdad, y el lector investiga con él.']},
 {'t': 'matriz', 'titulo': 'LOS PERSONAJES', 'celdas': [{'cab': 'Detective', 'txt': 'investiga y razona'}, {'cab': 'Víctima', 'txt': 'sufre el delito'}, {'cab': 'Sospechosos', 'txt': 'pudieron hacerlo'}, {'cab': 'Culpable', 'txt': 'lo hizo y lo oculta'}],
  'voz': ['Todo policial tiene un elenco fijo.', 'El *detective*, que investiga y razona.', 'La *víctima*, que sufre el delito.', 'Los *sospechosos*, que tenían motivos u ocasión.', 'Y el *culpable*, que se esconde entre ellos.']},
 {'t': 'bloques', 'titulo': 'DOS PAPELES MÁS', 'items': [{'cab': 'Ayudante', 'txt': 'acompaña al detective y entiende menos que él'}, {'cab': 'Testigo', 'txt': 'vio u oyó algo y lo cuenta'}],
  'voz': ['Aparecen dos papeles más.', 'El *ayudante*, que acompaña al detective y muchas veces se equivoca, como el lector.', 'Y los *testigos*, que vieron u oyeron algo y dan datos, aunque a veces se confunden.']},
 {'t': 'linea', 'titulo': 'DETECTIVES FAMOSOS', 'eventos': [{'fecha': '1841', 'txt': 'Dupin, de Edgar Allan Poe', 'emoji': '🎩'}, {'fecha': '1887', 'txt': 'Sherlock Holmes, de Conan Doyle', 'emoji': '🔎'}, {'fecha': '1920', 'txt': 'Hércules Poirot, de Agatha Christie', 'emoji': '🥚'}],
  'voz': ['En 1841, Edgar Allan Poe crea a Auguste *Dupin*, el primer gran detective de la literatura.', 'En 1887 aparece *Sherlock Holmes*, el más famoso de todos.', 'Y en 1920, *Hércules Poirot*, el detective belga de Agatha Christie.']},
 {'t': 'datoloco', 'texto': 'Cuando Poe inventó a Dupin, la policía de su ciudad casi no investigaba: el detective literario llegó antes que el real.', 'emoji': '🤯',
  'voz': ['¿Sabías que el detective de las novelas apareció antes que muchos detectives de verdad?', 'Cuando Poe inventó a Dupin, las policías recién empezaban a investigar con método.']},
 {'t': 'quiz4', 'pregunta': 'Una señora vio salir a un hombre de sombrero a medianoche. ¿Qué papel cumple?', 'opciones': ['Detective', 'Testigo', 'Culpable', 'Víctima'], 'correcta': 1,
  'voz': ['Pregunta: una señora vio salir a un hombre de sombrero a medianoche. ¿Qué papel cumple ella en el relato?', 'Pensá qué hace: ¿investiga, sufre el delito o cuenta lo que vio?', 'Es *testigo*: aporta un dato, pero no investiga.']},
 {'t': 'errores', 'items': [{'mal': 'El primer sospechoso es el culpable', 'bien': 'El culpable suele estar escondido entre los menos sospechados'}, {'mal': 'El policial es solo un relato de crímenes', 'bien': 'Lo central es el enigma y la investigación'}],
  'voz': ['Dos errores comunes.', 'El primer sospechoso casi nunca es el culpable: el género juega a esconderlo.', 'Y el policial no es solo violencia: lo central es el *enigma* y cómo se resuelve.']},
 {'t': 'resumen', 'items': [['Relato policial', 'un enigma que se investiga'], ['Detective', 'investiga y razona'], ['Víctima y culpable', 'quien sufre y quien comete el delito'], ['Sospechosos y testigos', 'quienes pudieron hacerlo y quienes vieron algo']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 1'},
  'voz': ['Repasemos.', 'Un policial es un enigma que alguien investiga.', 'El detective.', 'La víctima y el culpable.', 'Los sospechosos y los testigos.', 'Con estos personajes se arma cualquier caso. ¡A practicar!']},
]
CL['2'] = [
 {'t': 'reto', 'texto': 'Un hombre dice que pasó la tarde en su casa, pero sus zapatos tienen arena de playa. ¿Qué pensás?', 'segundos': 5, 'respuesta': 'Que mintió: estuvo en la playa', 'emoji': '👞', 'titulo': 'LEER PISTAS', 'sub': 'pensar como detective',
  'voz': ['Reto: un hombre jura que pasó la tarde en su casa, pero sus zapatos tienen arena de playa.', 'Tenés cinco segundos.', 'Mintió: estuvo en la playa. Acabás de *leer una pista*.']},
 {'t': 'definicion', 'palabra': 'Pista', 'texto': 'Detalle que acerca a la verdad del caso y permite sacar una conclusión.', 'emoji': '🧩',
  'voz': ['Una *pista* es un detalle que acerca a la verdad del caso.', 'Sola no dice mucho; unida a otras, permite sacar una conclusión.']},
 {'t': 'comparar', 'a': {'cab': 'Pista', 'texto': 'el candado se abrió con su propia llave', 'emoji': '🔑'}, 'b': {'cab': 'Falsa pista', 'texto': 'el vecino nuevo tiene cara de malo', 'emoji': '🎭'}, 'signo': '≠',
  'voz': ['Ahora compará.', 'Una *pista*: el candado se abrió con su propia llave. Dice algo concreto sobre quién fue.', 'Una *falsa pista*: el vecino nuevo tiene cara de malo. Distrae, pero no prueba nada.']},
 {'t': 'pasos', 'titulo': 'EL MÉTODO DEL DETECTIVE', 'items': [{'txt': 'Observar', 'emoji': '👀'}, {'txt': 'Relacionar', 'emoji': '🔗'}, {'txt': 'Deducir', 'emoji': '💡'}, {'txt': 'Comprobar', 'emoji': '✅'}],
  'voz': ['El detective de enigma sigue siempre el mismo método.', 'Primero *observa* lo que los demás pasan por alto.', 'Después *relaciona* ese detalle con lo que ya sabe.', 'Entonces *deduce*: saca una conclusión lógica.', 'Y antes de acusar, *comprueba*.']},
 {'t': 'historieta', 'titulo': 'UNA DEDUCCIÓN', 'vinetas': [{'emojis': ['🕵️', '☕'], 'txt': 'Hay dos tazas en la mesa.', 'quien': 'Detective'}, {'emojis': ['🏠'], 'txt': 'Pero la víctima vivía sola.', 'quien': 'Detective'}, {'emojis': ['💡'], 'txt': 'Alguien la visitó esta mañana.', 'quien': 'Detective'}],
  'voz': ['Mirá el método en acción. La detective ve dos tazas de café en la mesa.', 'Lo relaciona con un dato: la víctima vivía sola.', 'Deduce que esa mañana alguien la visitó. Ahora tiene que averiguar quién.']},
 {'t': 'prediccion', 'pregunta': 'Tres sospechosos. Uno estaba en un hospital a la hora del robo, con testigos. ¿Sigue en la lista?', 'a': {'txt': 'Sí, sigue', 'emoji': '🤔'}, 'b': {'txt': 'No, se descarta', 'emoji': '❌'}, 'correcta': 'b', 'resultado': 'Tiene coartada: no pudo estar en dos lugares a la vez.',
  'voz': ['¿Qué creés? Uno de los tres sospechosos estaba en un hospital a la hora del robo, y hay testigos.', 'Pensalo.', 'Se descarta: tiene una *coartada*. Descartar también es investigar.']},
 {'t': 'clasificar', 'cajas': [{'cab': 'Pista', 'emoji': '🧩'}, {'cab': 'Falsa pista', 'emoji': '🎭'}], 'fichas': [{'txt': 'huella de barro', 'caja': 0}, {'txt': 'reloj mojado', 'caja': 0}, {'txt': 'mirada nerviosa', 'caja': 1}, {'txt': 'mala fama', 'caja': 1}],
  'voz': ['Clasifiquemos lo que encontró la detective.', 'Una huella de barro y un reloj mojado son *pistas*: datos que se pueden comprobar.', 'Una mirada nerviosa o la mala fama de alguien son *falsas pistas*: impresiones que no prueban nada.']},
 {'t': 'vof', 'afirmacion': 'El buen detective adivina quién fue y después busca pruebas.', 'emoji': '🕵️', 'verdadero': False, 'explicacion': 'No adivina: cada conclusión sale de pistas que se pueden comprobar.',
  'voz': ['Verdadero o falso: el buen detective adivina quién fue y después busca pruebas.', 'Pensá en el método.', 'Falso: el detective de enigma no adivina. Cada conclusión sale de las pistas.']},
 {'t': 'resumen', 'items': [['Pista', 'detalle que acerca a la verdad'], ['Falsa pista', 'detalle que distrae'], ['Deducción', 'conclusión lógica a partir de pistas'], ['Coartada', 'prueba de que alguien estaba en otro lugar']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 2'},
  'voz': ['Repasemos.', 'Leer como detective es separar lo que sirve de lo que distrae.', 'La pista.', 'La falsa pista.', 'La deducción.', 'Y la coartada, que descarta sospechosos. ¡A practicar!']},
]
CL['3'] = [
 {'t': 'historia', 'personaje': {'nombre': 'Inspectora Lugo', 'emoji': '🕵️‍♀️'}, 'lugar': '🏛️', 'lineas': ['El cuento empieza con el robo ya hecho.', 'La inspectora junta pistas durante días.', 'Recién al final sabemos cómo pasó todo.'], 'titulo': 'DOS HISTORIAS', 'sub': 'en un mismo relato',
  'voz': ['El cuento empieza con el robo del museo ya cometido.', 'Durante días, la inspectora Lugo junta pistas.', 'Y recién en la última página sabemos cómo pasó todo.', 'Es raro: lo primero que ocurrió es lo último que se cuenta. Así funciona el policial.']},
 {'t': 'orden', 'titulo': 'ASÍ PASÓ / ASÍ SE CUENTA', 'items': [{'txt': 'El guardia copia la llave', 'emoji': '🔑'}, {'txt': 'Roba el cuadro de noche', 'emoji': '🖼️'}, {'txt': 'La inspectora investiga', 'emoji': '🕵️‍♀️'}, {'txt': 'Revela al culpable', 'emoji': '💡'}], 'relato': [2, 3, 0, 1],
  'voz': ['Mirá el orden real de los hechos: el guardia copia la llave, roba el cuadro, la inspectora investiga y revela al culpable.', 'Ahora mirá el orden en que se cuenta: primero la investigación y la revelación.', 'La copia de la llave y el robo aparecen al final, cuando la inspectora explica el caso.']},
 {'t': 'definicion', 'palabra': 'Las dos historias', 'texto': 'La del crimen, que pasó antes y queda oculta, y la de la investigación, que el lector sigue paso a paso.', 'emoji': '📚',
  'voz': ['Por eso se dice que todo policial de enigma cuenta *dos historias*.', 'La del *crimen*, que pasó antes y queda oculta, y la de la *investigación*, que leemos paso a paso.']},
 {'t': 'flujo', 'titulo': 'LA ESTRUCTURA', 'items': ['Crimen', 'Investigación', 'Revelación'],
  'voz': ['La estructura tiene tres momentos. Primero, el *crimen* o el hecho misterioso.', 'Después, la *investigación*: pistas, testigos, sospechosos.', 'Y al final, la *revelación*: el detective explica todo y la historia oculta sale a la luz.']},
 {'t': 'dialogo', 'personas': [{'nombre': 'Ayudante', 'emoji': '🧑'}, {'nombre': 'Detective', 'emoji': '🕵️'}], 'lineas': [{'quien': 0, 'txt': 'Yo no veía nada raro en la alfombra.'}, {'quien': 1, 'txt': 'Mirá esa ceniza: no es de este cigarro.'}, {'quien': 0, 'txt': '¡Entonces había alguien más en la sala!'}],
  'voz': ['¿Quién cuenta? Muchas veces, el *ayudante*: «yo no veía nada raro en la alfombra».', 'El detective sí ve: la ceniza no es de ese cigarro.', 'El ayudante entiende tarde, igual que el lector. Es un *narrador testigo*: cuenta con «yo», pero el protagonista es otro.']},
 {'t': 'pregunta', 'pregunta': '¿Por qué conviene que narre el ayudante y no el detective?', 'opciones': ['Para mantener el suspenso', 'Porque el detective no sabe escribir', 'Para contar el final al principio'], 'correcta': 0,
  'voz': ['Pregunta: ¿por qué conviene que narre el ayudante y no el detective?', 'Pensá qué pasaría si contara el que ya sabe la solución.', 'Para mantener el *suspenso*: el ayudante sabe menos, y el lector descubre la verdad con él.']},
 {'t': 'errores', 'items': [{'mal': 'La revelación cuenta algo nuevo que no estaba en el relato', 'bien': 'La revelación une pistas que el lector ya había visto'}, {'mal': 'El narrador testigo es el autor', 'bien': 'Es un personaje inventado que cuenta la historia'}],
  'voz': ['Dos errores para evitar.', 'La revelación no saca un dato nuevo de la galera: une pistas que el lector ya tenía. Eso se llama *juego limpio*.', 'Y el narrador testigo no es el autor: es un personaje inventado.']},
 {'t': 'resumen', 'items': [['Historia del crimen', 'pasó antes y queda oculta'], ['Historia de la investigación', 'la que seguimos'], ['Revelación', 'el detective explica todo'], ['Narrador testigo', 'el ayudante cuenta con «yo»']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 3'},
  'voz': ['Repasemos.', 'Dos historias y un narrador que sabe menos que el detective.', 'La historia del crimen.', 'La de la investigación.', 'La revelación.', 'Y el narrador testigo. ¡A practicar!']},
]
CL['4'] = [
 {'t': 'documental', 'emojis': ['🌃', '🌧️', '🚬'], 'lugar': 'Una ciudad de noche', 'rotulos': [{'txt': 'Estados Unidos, 1929', 'sub': 'gángsters y policías comprados'}, {'txt': 'Otro tipo de detective', 'sub': 'cansado, solo y en la calle'}],
  'voz': ['Estados Unidos, fines de la década de 1920: ciudades con gángsters, contrabando y policías comprados.', 'En los relatos de esa época aparece otro tipo de detective, que no razona tranquilo en un sillón: camina de noche, recibe golpes y desconfía de todos. Nace el *policial negro*.']},
 {'t': 'versus', 'a': {'txt': 'Policial de enigma', 'emoji': '🧩', 'datos': ['un rompecabezas', 'el detective razona', 'el orden vuelve']}, 'b': {'txt': 'Policial negro', 'emoji': '🌃', 'datos': ['una ciudad violenta', 'el detective se arriesga', 'el mal sigue']}, 'gana': 'empate', 'veredicto': 'Dos formas del mismo género',
  'voz': ['Cara a cara. El *policial de enigma*: el crimen es un rompecabezas y el detective lo resuelve con la razón.', 'El *policial negro*: el crimen muestra una ciudad violenta y el detective arriesga el cuerpo.', 'En el de enigma, al final, el orden vuelve. En el negro, se resuelve un caso, pero la corrupción sigue.', 'No hay ganador: son dos formas del mismo género.']},
 {'t': 'tabla', 'titulo': 'QUÉ CAMBIA', 'columnas': ['', 'Enigma', 'Negro'], 'filas': [['¿Quién investiga?', 'genio aficionado', 'detective profesional'], ['¿Dónde?', 'una casa, un tren', 'la calle, los bares'], ['¿Qué importa?', 'quién lo hizo', 'por qué pasa']],
  'voz': ['Mirá qué cambia de un tipo al otro.', 'En el de enigma investiga un genio aficionado; en el negro, un detective profesional que cobra por su trabajo.', 'El de enigma ocurre en lugares cerrados, como una mansión o un tren; el negro, en la calle y en los bares.', 'Y la pregunta cambia: el enigma pregunta *quién lo hizo*; el negro pregunta *por qué pasa*, qué está podrido en esa sociedad.']},
 {'t': 'linea', 'titulo': 'EL GÉNERO VIAJA', 'eventos': [{'fecha': '1929', 'txt': 'Cosecha roja, de Dashiell Hammett', 'emoji': '🇺🇸'}, {'fecha': '1942', 'txt': 'Borges y Bioy: Isidro Parodi', 'emoji': '🇦🇷'}, {'fecha': '1953', 'txt': 'Walsh: Variaciones en rojo', 'emoji': '🇦🇷'}],
  'voz': ['En 1929, Dashiell Hammett publica *Cosecha roja*, una de las primeras novelas negras.', 'En 1942, Borges y Bioy Casares crean a Isidro Parodi, un detective que resuelve casos desde la cárcel, sin moverse.', 'Y en 1953, Rodolfo Walsh publica *Variaciones en rojo*. El policial también se escribe en la Argentina.']},
 {'t': 'dilema', 'situacion': 'Un detective descubre que el asesino trabaja para el político más poderoso de la ciudad.', 'emoji': '🕴️', 'a': {'txt': 'Lo denuncia igual', 'consecuencia': 'arriesga su vida y su trabajo', 'emoji': '⚖️'}, 'b': {'txt': 'Se calla', 'consecuencia': 'cobra, pero el crimen queda impune', 'emoji': '💰'},
  'voz': ['Un dilema típico del policial negro: el detective descubre que el asesino trabaja para el político más poderoso de la ciudad.', 'Si lo denuncia, arriesga la vida y el trabajo.', 'Si se calla, cobra, pero el crimen queda impune. En el negro, el detective siempre tiene que elegir.']},
 {'t': 'quiz4', 'pregunta': 'Fragmento: «Llovía sobre el puerto. Sabía que el comisario también cobraba de la banda.» ¿Qué tipo de policial es?', 'opciones': ['De enigma', 'Negro', 'No es policial'], 'correcta': 1,
  'voz': ['Leé este fragmento: llovía sobre el puerto, y el detective sabía que el comisario también cobraba de la banda.', 'Fijate en el lugar y en lo que muestra de la sociedad.', 'Es *policial negro*: ciudad de noche y corrupción en la propia policía.']},
 {'t': 'logro', 'titulo': '¡Misión cumplida!', 'items': ['El policial y sus personajes', 'Pistas, falsas pistas y deducción', 'Las dos historias y el narrador testigo', 'Del enigma al policial negro'], 'xp': 100,
  'voz': ['¡Terminaste las clases de la misión!', 'Ya reconocés un policial y sus personajes.', 'Sabés separar pistas de falsas pistas.', 'Entendés las dos historias y al narrador testigo.', 'Y distinguís el enigma del policial negro. Ahora, ¡a leer como detective!']},
]
for n, esc in CL.items():
    json.dump({'slug': f'leng1-m2-n{n}', 'step_id': STEP[n], 'materia': 'Lengua y Literatura I', 'titulo': TIT[n], 'sub': f'Lengua y Literatura I · Misión 2 · Nivel {n}', 'escenas': esc},
              open(os.path.join(RAIZ, 'tools/clase/lecciones', f'leng1-m2-n{n}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ============================ LECCIÓN ============================
L = {}
L['1'] = {'temas': [
 T('Qué es un relato policial',
   m('esquema', items=[
     {'nombre': 'El trofeo', 'raiz': 'Enigma: ¿quién sacó el trofeo de una vitrina cerrada?', 'ramas': [['El hecho', ['el trofeo desaparece de noche'], 'Rompe el orden y abre el misterio.'], ['La pregunta', ['¿cómo, si la llave la tenía el director?'], 'Es lo que el relato promete responder.'], ['La investigación', ['la preceptora interroga y busca detalles'], 'Ocupa casi todo el relato.'], ['La solución', ['el portero había hecho una copia de la llave'], 'Responde el enigma al final.']], 'cierre': 'Todo el relato gira alrededor de una pregunta.'},
     {'nombre': 'El collar', 'raiz': 'Enigma: ¿cómo desapareció un collar en plena fiesta?', 'ramas': [['El hecho', ['el collar no está en el joyero'], 'Algo que no tendría que haber pasado.'], ['La pregunta', ['¿quién, si nadie salió de la casa?'], 'El misterio que hay que resolver.'], ['La investigación', ['el inspector revisa a cada invitado'], 'La búsqueda de la verdad.'], ['La solución', ['el sobrino lo escondió en una maceta'], 'Se descubre al final.']], 'cierre': 'Cambia la historia, pero la forma es la misma.'}]),
   m('elegir_x', consigna='¿Cuál de estos argumentos corresponde a un relato policial?', items=[
     {'cons': 'Elegí el argumento policial.', 'ops': ['Una jugadora investiga quién cambió las pelotas del torneo antes de la final', 'Una jugadora entrena todos los días para ganar la final', 'Una jugadora cuenta cómo fue su primer partido'], 'ayuda': 'Buscá el que tiene un enigma y una investigación.'},
     {'cons': 'Elegí el argumento policial.', 'ops': ['En un tren nocturno aparece un pasajero sin vida y un médico interroga a todos', 'Un tren cruza la cordillera y los pasajeros miran el paisaje', 'Un maquinista se jubila después de cuarenta años'], 'ayuda': 'Fijate dónde hay un misterio que alguien investiga.'},
     {'cons': 'Elegí el argumento policial.', 'ops': ['Una bibliotecaria descubre que alguien arranca páginas de los libros y busca al responsable', 'Una bibliotecaria ordena los libros por autor', 'Un chico lee su primera novela en la biblioteca'], 'ayuda': 'Pensá en qué caso hay que responder una pregunta oculta.'}]),
   ('Relato policial', 'El relato policial es una narración que gira alrededor de un enigma, casi siempre un crimen o un hecho misterioso, que un personaje investiga hasta descubrir la verdad.'),
   'Lo que define al género no es la violencia, sino la pregunta: quién lo hizo, cómo o por qué. El relato propone un desafío y el lector lo acepta, porque recibe las mismas pistas que el investigador y puede intentar adelantarse a la solución.',
   ['Un hecho misterioso rompe el orden.', 'Alguien investiga para responder el enigma.', 'Al final, la verdad sale a la luz.']),
 T('Los personajes del policial',
   m('marcar', rotulo='Caso', items=[
     {'nombre': 'La quinta', 'texto': '{{Don Ramiro|Víctima: sufre el robo.}} denuncia que le robaron los ahorros. {{El comisario Ferreyra|Detective: investiga el caso.}} llega con {{su sobrina Ana|Ayudante: lo acompaña y anota todo.}}. {{La cocinera recuerda un auto azul en el portón|Testigo: aporta un dato que vio.}}. Sospechan {{del jardinero y del hijo de don Ramiro|Sospechosos: tenían ocasión de hacerlo.}}, pero {{fue el contador, que nadie había mirado|Culpable: el que menos parecía.}}.', 'cierre': 'Seis papeles que aparecen en casi todos los policiales.'},
     {'nombre': 'El hotel', 'texto': 'En un hotel de montaña {{desaparece la cámara de una turista|Víctima: la turista.}}. {{Una huésped jubilada, maestra de química|Detective: no es policía, pero razona mejor que nadie.}} pregunta a todos. {{El conserje vio a alguien en la escalera|Testigo.}}. {{El botones y un viajante|Sospechosos.}} tienen coartadas débiles, pero {{la ladrona es la recepcionista|Culpable.}}.', 'cierre': 'El detective puede ser un aficionado.'}]),
   m('clasificar_x', consigna='¿Qué papel cumple cada personaje en su relato?', cajas=['Detective', 'Víctima', 'Testigo', 'Culpable'], cuantos=6, items=[
     ['La periodista que reúne las pistas y descubre al estafador', 0], ['El profesor que interroga a los sospechosos del robo del examen', 0], ['El vecino al que le robaron la bicicleta', 1], ['La dueña del collar desaparecido', 1],
     ['El kiosquero que vio a un hombre con capucha', 2], ['La nena que escuchó un golpe a las tres', 2], ['El sobrino que escondió el collar en la maceta', 3], ['La cajera que se quedó con la recaudación', 3]]),
   ('Personajes del policial', 'Los personajes del policial cumplen papeles fijos: el detective investiga, la víctima sufre el delito, los sospechosos pudieron cometerlo, los testigos aportan datos y el culpable se esconde entre ellos.'),
   'Muchas veces el detective tiene un ayudante que lo acompaña y entiende menos que él. Ese personaje es importante: se equivoca como se equivocaría el lector, y así el misterio se mantiene. El culpable, en cambio, suele ser el menos sospechado.',
   ['Detective y ayudante: investigan.', 'Víctima, testigos y sospechosos: el mundo del caso.', 'Culpable: casi nunca el primero que parece.']),
 T('El detective de enigma',
   m('versiones', rotulo='Detective', items=[
     {'nombre': 'Dupin (1841)', 'texto': 'Creado por Edgar Allan Poe. {{Resuelve los casos pensando, casi sin salir de su cuarto|Rasgo clásico: la razón por encima de la acción.}} y {{lo acompaña un amigo que narra|Ayudante y narrador.}}.'},
     {'nombre': 'Holmes (1887)', 'texto': 'Creado por Arthur Conan Doyle. {{Observa detalles mínimos: una mancha, un callo, un barro|Rasgo clásico: la observación.}} y {{tiene costumbres raras: toca el violín a deshora|Es un genio excéntrico.}}. Lo acompaña el doctor Watson.'},
     {'nombre': 'Poirot (1920)', 'texto': 'Creado por Agatha Christie. {{Confía en «las pequeñas células grises» de su cerebro|Rasgo clásico: el razonamiento.}} y {{al final reúne a todos los sospechosos para explicar el caso|La revelación frente a todos.}}.'}]),
   m('elegir_x', consigna='¿Qué rasgo del detective de enigma muestra cada caso?', items=[
     {'cons': 'La detective nota que el reloj del sospechoso marca la hora de otro país.', 'ops': ['Observa detalles que otros no ven', 'Usa la fuerza para que confiese', 'Confía en la suerte'], 'ayuda': 'Pensá qué hace con el reloj.'},
     {'cons': 'Sin moverse del sillón, el detective escucha el relato del cliente y resuelve el caso.', 'ops': ['Razona a partir de lo que sabe', 'Persigue al culpable por la ciudad', 'Espera que alguien confiese'], 'ayuda': 'No sale a buscar: piensa.'},
     {'cons': 'El investigador reúne a todos en el salón y explica paso a paso quién fue y cómo.', 'ops': ['Revela la solución frente a todos', 'Deja el caso sin resolver', 'Le pide ayuda a la policía'], 'ayuda': 'Es el final típico del género.'}]),
   ('Detective de enigma', 'El detective de enigma, o clásico, es un personaje de inteligencia excepcional que resuelve el caso observando detalles y razonando, más que usando la fuerza.'),
   'Suele ser un aficionado, no un policía, y tiene rasgos llamativos que lo hacen inolvidable. La policía oficial casi siempre aparece equivocada o atrasada, para que se luzca su método. Dupin, Holmes y Poirot son los grandes modelos.',
   ['Observa y razona; no usa la fuerza.', 'Suele ser aficionado y excéntrico.', 'Muchas veces lo acompaña un ayudante.'])],
 'recuerda': [
   R('Relato policial', 'es una narración que gira alrededor de un enigma que un personaje investiga hasta descubrir la verdad.', 'Una preceptora investiga quién sacó el trofeo de la vitrina'),
   R('Enigma', 'es la pregunta central del relato policial: quién lo hizo, cómo lo hizo o por qué.', '¿Cómo desapareció el collar si nadie salió de la casa?'),
   R('Detective', 'es el personaje que investiga el caso y lo resuelve, sea policía o aficionado.', 'La maestra jubilada que resuelve el robo del hotel'),
   R('Víctima y culpable', 'la víctima es quien sufre el delito; el culpable, quien lo comete y lo oculta.', 'Don Ramiro y el contador que le robó'),
   R('Sospechosos y testigos', 'los sospechosos pudieron cometer el delito; los testigos vieron u oyeron algo y lo cuentan.', 'El jardinero sospechado y la cocinera que vio un auto'),
   R('Detective de enigma', 'es el investigador clásico que resuelve el caso observando y razonando, sin usar la fuerza.', 'Dupin, Holmes, Poirot')]}

L['2'] = {'temas': [
 T('Pistas y falsas pistas',
   m('marcar', rotulo='Caso', items=[
     {'nombre': 'La bicicleta', 'texto': 'Robaron la bici de Tomi del patio. {{Todos miran al chico nuevo, que llegó tarde y con la ropa sucia|Falsa pista: parece sospechoso, pero llegó tarde por ayudar a su abuela.}}. En cambio, {{el candado se abrió con su propia llave|Pista: quien la llevó sabía dónde estaba la llave.}} y {{la hermana de Tomi tiene una copia|Pista: la verdad empieza a aparecer.}}.', 'cierre': 'La hermana la llevó prestada sin avisar.'},
     {'nombre': 'La torta', 'texto': 'Desapareció media torta de la cocina. {{El perro tiene crema en el hocico|Falsa pista: era crema de su propia comida.}}. Pero {{falta un plato del estante alto|Pista: el perro no llega ahí.}} y {{hay migas en la escalera que va al cuarto del abuelo|Pista: marca un camino.}}.', 'cierre': 'Fue el abuelo, que no resistió la tentación.'}]),
   m('marcar_x', consigna='Tocá solo las pistas verdaderas: las que acercan a la verdad.', items=[
     {'cons': 'Caso: desapareció la recaudación de la cantina del club. Fue la cajera.', 'texto': '[[La cajera pidió cambiar de turno justo ese día|1]] · [[El portero tiene cara de pocos amigos|0]] · [[La caja no fue forzada|1]] · [[Un socio llegó corriendo al vestuario|0]]'},
     {'cons': 'Caso: alguien rompió el vidrio del vestuario. Fue una pelota del entrenamiento de las chicas.', 'texto': '[[Hay una pelota debajo del banco|1]] · [[El encargado estaba de mal humor|0]] · [[Las chicas entrenaban en la cancha de al lado|1]] · [[Llovió a la tarde|0]]'}]),
   ('Pista', 'Una pista es un detalle concreto que acerca a la verdad del caso; una falsa pista es un dato que distrae y hace mirar hacia el lado equivocado.'),
   'Las falsas pistas son parte del juego: el autor las pone a propósito para que el lector sospeche de quien no es. Una buena regla es desconfiar de las impresiones, como una cara de enojo o una mala fama, y confiar en los datos que se pueden comprobar.',
   ['Pista: un dato concreto y comprobable.', 'Falsa pista: una impresión que distrae.', 'El autor esconde la verdad entre las dos.']),
 T('Deducir: de los detalles a la conclusión',
   m('marcar', rotulo='Deducción', items=[
     {'nombre': 'Los zapatos', 'texto': 'La detective {{nota barro rojizo en los zapatos del jardinero|Observar: un detalle que otros no ven.}}. {{Ese barro solo está junto al estanque|Relacionar el detalle con lo que sabe.}}. {{Entonces él estuvo en el estanque, aunque dijo que no salió del galpón|Deducir: sacar una conclusión lógica.}}. {{Revisa el estanque y encuentra la caja escondida|Comprobar antes de acusar.}}.', 'cierre': 'Observar → relacionar → deducir → comprobar.'},
     {'nombre': 'El vidrio', 'texto': 'El inspector {{ve que los vidrios rotos cayeron hacia el jardín|Observar.}}. {{Si alguien hubiera entrado desde afuera, habrían caído adentro|Relacionar con lo que sabe.}}. {{El vidrio se rompió desde adentro: el robo lo fingió alguien de la casa|Deducir.}}. {{No hay huellas en el jardín húmedo|Comprobar.}}.', 'cierre': 'Cada paso se apoya en el anterior.'}]),
   m('ordenar_x', consigna='Ordená los pasos que sigue el detective.', items=[
     {'lista': ['Ve que el reloj del sospechoso está mojado', 'Recuerda que esa noche solo llovió en la costa', 'Deduce que el sospechoso estuvo en la costa y no en el centro', 'Confirma que su auto pasó por el peaje de la costa']},
     {'lista': ['Nota que en la mesa hay dos tazas usadas', 'Recuerda que la víctima vivía sola', 'Deduce que alguien la visitó esa mañana', 'Busca huellas en la segunda taza']}]),
   ('Deducción', 'La deducción es el razonamiento que va de los detalles observados a una conclusión que se sigue de ellos de manera lógica y que después se comprueba.'),
   'El detective de enigma no adivina ni confía en la suerte: observa lo que otros pasan por alto, lo relaciona con lo que ya sabe y recién acusa cuando puede probarlo. Por eso el lector atento puede seguir el razonamiento y llegar a la misma conclusión.',
   ['Observar: el detalle que nadie ve.', 'Relacionar y deducir: la conclusión lógica.', 'Comprobar: recién entonces, acusar.']),
 T('Descartar sospechosos',
   m('marcar', rotulo='Caso', items=[
     {'nombre': 'La medalla', 'texto': 'Desaparece una medalla del club a las 18. {{La tesorera estaba en el banco a esa hora, y hay un recibo|Coartada comprobada: se descarta.}}. {{El utilero dice que estaba en su casa, solo|Coartada sin testigos: sigue en la lista.}}. {{El presidente estaba en la reunión con otras doce personas|Coartada firme: se descarta.}}.', 'cierre': 'Queda un sospechoso: el utilero.'},
     {'nombre': 'El celular', 'texto': 'Un celular desaparece en la sala de profesores a las 10. {{La profesora de Música daba clase a esa hora frente a un curso|Se descarta.}}. {{El preceptor dice que fue a buscar tizas, pero el depósito estaba cerrado|Su coartada no se sostiene.}}.', 'cierre': 'Una coartada que falla es una pista.'}]),
   m('elegir_x', consigna='¿Se descarta o sigue sospechado?', items=[
     {'cons': 'El robo fue a las 21. El sospechoso estaba en una cena con diez invitados que lo vieron toda la noche.', 'ops': ['Se descarta: tiene una coartada firme', 'Sigue sospechado: es el que más se beneficia', 'Es el culpable seguro'], 'ayuda': 'Pensá si pudo estar en dos lugares.'},
     {'cons': 'La sospechosa dice que esa tarde estaba en el cine, pero la película que nombra no se daba ese día.', 'ops': ['Sigue sospechada: su coartada es falsa', 'Se descarta: dijo dónde estaba', 'Es inocente porque le gusta el cine'], 'ayuda': 'Una coartada falsa no descarta: despierta sospechas.'},
     {'cons': 'El sospechoso estaba solo en su casa y nadie puede confirmarlo.', 'ops': ['Sigue en la lista: su coartada no se puede comprobar', 'Se descarta: estaba en su casa', 'Es el culpable: estaba solo'], 'ayuda': 'Sin coartada, ni se descarta ni se condena.'}]),
   ('Coartada', 'La coartada es la prueba de que un sospechoso estaba en otro lugar cuando ocurrió el delito; si se comprueba, ese sospechoso queda descartado.'),
   'Investigar no es solo encontrar al culpable: también es descartar a los inocentes. Cada coartada comprobada achica la lista, y una coartada falsa se convierte en una nueva pista. Así el detective llega a una sola explicación posible.',
   ['Coartada firme: se descarta.', 'Coartada sin testigos: sigue en la lista.', 'Coartada falsa: es una nueva pista.'])],
 'recuerda': [
   R('Pista', 'es un detalle concreto y comprobable que acerca a la verdad del caso.', 'El candado se abrió con su propia llave'),
   R('Falsa pista', 'es un dato que distrae y hace sospechar de quien no es, muchas veces una impresión.', 'El chico nuevo llegó tarde y con la ropa sucia'),
   R('Deducción', 'es llegar a una conclusión lógica a partir de detalles observados, y comprobarla antes de acusar.', 'Barro del estanque en los zapatos → estuvo en el estanque'),
   R('Método del detective', 'consiste en observar, relacionar, deducir y comprobar, en ese orden.', 'Dos tazas → vivía sola → hubo una visita → huellas'),
   R('Coartada', 'es la prueba de que un sospechoso estaba en otro lugar a la hora del delito.', 'La tesorera estaba en el banco y tiene el recibo')]}

L['3'] = {'temas': [
 T('Las dos historias del policial',
   m('linea_tiempo', items=[
     {'nombre': 'El museo', 'hechos': [{'t': 'La inspectora llega al museo: falta un cuadro', 'c': 3}, {'t': 'Interroga al guardia y a la directora', 'c': 4}, {'t': 'Descubre una copia de la llave en el vestuario', 'c': 5}, {'t': 'Explica: el guardia copió la llave un mes antes', 'c': 1, 'flash': 1}, {'t': 'Y la noche del robo desconectó la alarma', 'c': 2, 'flash': 1}],
      'marca': 'La historia del crimen empezó antes, pero se cuenta al final, en la revelación.', 'cierre': 'El orden del relato no es el orden de los hechos.'},
     {'nombre': 'El tren', 'hechos': [{'t': 'Un pasajero denuncia que le robaron un maletín', 'c': 3}, {'t': 'El médico revisa el vagón y habla con todos', 'c': 4}, {'t': 'Explica: el guarda subió el maletín a otro vagón en la estación anterior', 'c': 2, 'flash': 1}, {'t': 'El guarda y su cómplice lo habían planeado en el andén', 'c': 1, 'flash': 1}],
      'marca': 'Lo que pasó primero aparece último.', 'cierre': 'Así se mantiene el misterio hasta el final.'}]),
   m('ordenar_x', consigna='Ordená la historia del crimen como ocurrió en el tiempo (no como se cuenta).', items=[
     {'lista': ['La cajera copia la llave de la caja', 'Pide cambiar de turno', 'Saca la recaudación', 'La detective descubre la copia de la llave']},
     {'lista': ['El sobrino planea quedarse con el collar', 'Lo esconde en una maceta durante la fiesta', 'La dueña denuncia el robo', 'El inspector encuentra el collar y explica el caso']}]),
   ('Las dos historias', 'Todo policial de enigma cuenta dos historias: la del crimen, que ocurrió antes y queda oculta, y la de la investigación, que el lector sigue paso a paso.'),
   'La historia del crimen recién se conoce completa al final, cuando el detective explica cómo lo resolvió. Por eso el orden en que se cuenta no coincide con el orden en que ocurrieron los hechos, y esa diferencia es la que mantiene el misterio.',
   ['Historia del crimen: pasó antes y está oculta.', 'Historia de la investigación: la que leemos.', 'Se unen al final, en la revelación.']),
 T('El narrador testigo',
   m('versiones', rotulo='Narrador', items=[
     {'nombre': 'Testigo', 'texto': '{{Yo no veía nada raro en la alfombra|Cuenta con «yo», pero no es el protagonista.}}; {{mi amigo, en cambio, se agachó y sonrió|El protagonista es el detective.}}. {{Recién en la cena entendí por qué|Sabe menos que el detective, como el lector.}}.'},
     {'nombre': 'Omnisciente', 'texto': 'El detective vio la ceniza y {{supo en ese instante que el mayordomo mentía|Sabe lo que piensa: el misterio se acaba.}}. {{El mayordomo, nervioso, ya pensaba en huir|Sabe también lo que piensa el culpable.}}.'},
     {'nombre': 'Protagonista', 'texto': '{{Vi la ceniza y supe que el mayordomo mentía|El detective cuenta su propio razonamiento.}}. {{Decidí no decir nada hasta la cena|Si lo cuenta todo, el lector ya sabe la solución.}}.'}]),
   m('elegir_x', consigna='Pensá en el narrador y su efecto.', items=[
     {'cons': '«Mi amiga examinó el reloj en silencio; yo no entendía qué buscaba.» ¿Qué tipo de narrador es?', 'ops': ['Testigo', 'Protagonista', 'Omnisciente'], 'ayuda': 'Cuenta con «yo» lo que hace otra persona.'},
     {'cons': 'Si el caso lo contara el detective desde el principio con todo lo que piensa, ¿qué se perdería?', 'ops': ['El suspenso, porque ya sabe la solución', 'Los diálogos', 'Los nombres de los personajes'], 'ayuda': 'El que narra sabe lo que sabe el detective.'},
     {'cons': '¿Por qué el ayudante es un buen narrador para un policial de enigma?', 'ops': ['Ve todo, pero entiende menos que el detective, como el lector', 'Porque siempre es el culpable', 'Porque sabe lo que piensan todos'], 'ayuda': 'El testigo participa, pero no deduce como el detective.'}]),
   ('Narrador testigo', 'El narrador testigo es un personaje que participa de los hechos y los cuenta en primera persona, pero el protagonista de la historia es otro.'),
   'En el policial de enigma suele narrar el ayudante del detective. Ve las mismas pistas que él, pero no las entiende a tiempo, y por eso el lector descubre la verdad junto con él. Si narrara el detective, el misterio se terminaría enseguida.',
   ['Cuenta con «yo», pero no es el protagonista.', 'Sabe menos que el detective.', 'Mantiene el suspenso hasta la revelación.']),
 T('La revelación y el juego limpio',
   m('marcar', rotulo='Final', items=[
     {'nombre': 'Juego limpio', 'texto': 'En la cena, la detective explica: {{«¿Recuerdan que el jardinero tenía barro rojo en los zapatos?»|Retoma una pista que el lector ya había visto.}} {{«Ese barro solo está junto al estanque»|Une la pista con un dato que también se había mencionado.}}. {{«Ahí escondió la caja.»|La solución sale de pistas conocidas.}}', 'cierre': 'El lector tenía todo para resolverlo.'},
     {'nombre': 'Trampa', 'texto': 'En la cena, el detective explica: {{«El culpable es el hermano gemelo del mayordomo»|Un personaje que nunca apareció.}}, {{«que llegó en secreto desde Europa»|Un dato nuevo que el lector no podía saber.}}.', 'cierre': 'Así el final decepciona: el lector no tuvo ninguna oportunidad.'}]),
   m('elegir_x', consigna='¿El final respeta el juego limpio con el lector?', items=[
     {'cons': 'Al final, el detective revela que la culpable es la cocinera, que había mentido sobre la hora en el capítulo dos.', 'ops': ['Sí: la mentira ya estaba en el relato', 'No: la cocinera no aparecía', 'No: el detective adivinó'], 'ayuda': 'Pensá si el lector tenía el dato.'},
     {'cons': 'Al final, el detective dice que el culpable es un ladrón famoso que nunca había sido mencionado.', 'ops': ['No: aparece alguien que el lector no conocía', 'Sí: es un ladrón famoso', 'Sí: el detective siempre tiene razón'], 'ayuda': 'El culpable tiene que estar a la vista.'},
     {'cons': 'La revelación une tres pistas: una huella, un reloj atrasado y una carta, que aparecieron antes.', 'ops': ['Sí: todo estaba en el relato', 'No: son demasiadas pistas', 'No: las pistas se explican al principio'], 'ayuda': 'El juego limpio es dar todas las pistas antes del final.'}]),
   ('Revelación', 'La revelación es el final del policial de enigma, en el que el detective explica cómo resolvió el caso y la historia oculta del crimen sale a la luz.'),
   'Una buena revelación respeta el juego limpio: la solución se arma con pistas que el lector ya había visto, aunque no les haya dado importancia. Si el culpable aparece de la nada o el detective usa un dato que nunca se mostró, el lector se siente engañado.',
   ['El detective explica el razonamiento.', 'La historia del crimen se cuenta completa.', 'Juego limpio: todas las pistas, antes del final.'])],
 'recuerda': [
   R('Historia del crimen', 'es lo que ocurrió antes de la investigación y queda oculto hasta el final.', 'El guardia copió la llave un mes antes'),
   R('Historia de la investigación', 'es la que el lector sigue paso a paso: pistas, testigos y sospechosos.', 'La inspectora interroga y encuentra la copia'),
   R('Narrador testigo', 'participa de los hechos y cuenta en primera persona, pero el protagonista es otro.', '«Yo no veía nada raro; mi amigo sonrió»'),
   R('Efecto del narrador testigo', 'es mantener el suspenso, porque sabe menos que el detective, igual que el lector.', 'Recién en la cena entendí por qué'),
   R('Revelación', 'es el final donde el detective explica cómo resolvió el caso.', 'La detective une el barro, el estanque y la caja'),
   R('Juego limpio', 'es dar al lector todas las pistas antes del final, para que pueda resolver el caso.', 'La mentira de la cocinera ya estaba en el capítulo dos')]}

L['4'] = {'temas': [
 T('El policial negro',
   m('esquema', items=[{'nombre': 'Dos policiales', 'cols': ['', 'Policial de enigma', 'Policial negro'], 'filas': [
       ['El detective', 'un genio aficionado que razona', 'un profesional que se arriesga y cobra'], ['El lugar', 'una casa, un tren, un hotel', 'la ciudad de noche: calles, bares, puertos'],
       ['El crimen', 'un rompecabezas', 'muestra violencia y corrupción'], ['La pregunta', '¿quién lo hizo?', '¿por qué pasa esto?'], ['El final', 'el orden vuelve', 'se resuelve un caso, pero el mal sigue']],
     'cierre': 'Mismo género, dos miradas sobre el delito.'}]),
   m('clasificar_x', consigna='¿Qué tipo de policial es cada fragmento?', cajas=['De enigma', 'Negro'], cuantos=6, items=[
     ['La detective observó la taza y supo enseguida quién había mentido.', 0], ['Reunió a los cinco sospechosos en la biblioteca para explicar el caso.', 0], ['Una sola ceniza en la alfombra alcanzó para resolverlo.', 0],
     ['Caminó bajo la lluvia por el puerto, con miedo de que lo siguieran.', 1], ['Descubrió que el jefe de policía también cobraba a la banda.', 1], ['Cerró el caso, pero sabía que mañana habría otro muerto en esa ciudad.', 1], ['Le partieron el labio en el bar, pero consiguió el nombre.', 1]]),
   ('Policial negro', 'El policial negro es la variante del género en la que el crimen muestra una sociedad violenta y corrupta, y el detective investiga en la calle, arriesgando su propio cuerpo.'),
   'Nació en los Estados Unidos hacia 1930, en una época de mafias y policías comprados. Ya no importa tanto quién lo hizo, sino por qué pasa: el delito aparece ligado al dinero y al poder, y aunque el caso se resuelva, el mundo sigue igual de duro.',
   ['Ciudad de noche, violencia y corrupción.', 'Detective profesional que se arriesga.', 'Pregunta central: ¿por qué pasa?']),
 T('El detective duro',
   m('marcar', rotulo='Fragmento', items=[
     {'nombre': 'La oficina', 'texto': '{{Hacía tres semanas que nadie me pagaba un caso|Detective profesional: vive de su trabajo y está en la mala.}}. Cuando entró la mujer del sombrero, {{supe que traía problemas, y que igual iba a aceptarlos|Tono desencantado: no se hace ilusiones.}}. {{Afuera, la lluvia lavaba la sangre de la vereda|La ciudad violenta como escenario.}}.', 'cierre': 'Primera persona, ironía y ciudad: rasgos del negro.'},
     {'nombre': 'El puerto', 'texto': '{{El comisario me dijo que me olvidara del caso|El poder quiere tapar el crimen.}}. {{Esa noche me esperaron dos tipos en el puerto|El detective arriesga el cuerpo.}}. {{Volví con una costilla rota y un nombre|Paga un precio por la verdad.}}.', 'cierre': 'Investigar es peligroso.'}]),
   m('elegir_x', consigna='¿Qué rasgo del detective duro muestra cada fragmento?', items=[
     {'cons': '«Cobro cincuenta pesos por día, más los gastos. Y no hago preguntas que no me pagan.»', 'ops': ['Es un profesional que vive de su trabajo', 'Es un genio que resuelve desde el sillón', 'Es un policía de uniforme'], 'ayuda': 'Fijate en cómo habla del dinero.'},
     {'cons': '«Me ofrecieron el doble para que dejara el caso. Dije que no y me fui caminando bajo la lluvia.»', 'ops': ['Tiene su propio código moral', 'Hace todo por dinero', 'No le interesa el caso'], 'ayuda': 'Rechaza algo que le conviene.'},
     {'cons': '«En esta ciudad, hasta los semáforos están comprados.»', 'ops': ['Mira la ciudad con ironía y desencanto', 'Admira el orden de la ciudad', 'Describe el tránsito con datos'], 'ayuda': 'Es una exageración amarga.'}]),
   ('Detective duro', 'El detective duro es el investigador del policial negro: un profesional solitario, irónico y desencantado, que se mueve por la ciudad, recibe golpes y se guía por un código moral propio.'),
   'A diferencia del genio de enigma, no es infalible ni elegante: se equivoca, tiene miedo y está siempre corto de plata. Muchas veces narra él mismo, en primera persona, con frases breves y cortantes. Su honestidad, en un mundo corrupto, es lo que lo vuelve un héroe.',
   ['Profesional, solitario y desencantado.', 'Arriesga el cuerpo y se equivoca.', 'Tiene un código moral propio.']),
 T('El policial en la Argentina',
   m('linea_tiempo', items=[
     {'nombre': 'Recorrido', 'hechos': [{'t': '1841 · Poe crea a Dupin en Estados Unidos', 'c': 1}, {'t': '1887 · Conan Doyle crea a Sherlock Holmes en Inglaterra', 'c': 2}, {'t': '1929 · Hammett publica Cosecha roja: nace el negro', 'c': 3}, {'t': '1942 · Borges y Bioy Casares crean a Isidro Parodi', 'c': 4}, {'t': '1953 · Walsh publica Variaciones en rojo', 'c': 5}],
      'marca': 'El género nace en inglés y se reescribe en la Argentina.', 'cierre': 'Los autores argentinos lo adaptan a su propia realidad.'}]),
   m('elegir_x', consigna='Leé el dato y elegí la conclusión correcta.', items=[
     {'cons': 'Isidro Parodi, el detective de Borges y Bioy Casares, está preso y resuelve los casos desde su celda, escuchando a quienes lo visitan.', 'ops': ['Es un detective de enigma: razona sin moverse', 'Es un detective duro: pelea en la calle', 'No es un detective'], 'ayuda': 'Pensá cómo resuelve los casos.'},
     {'cons': 'En los cuentos de Rodolfo Walsh, el detective Daniel Hernández es corrector de pruebas de imprenta y descubre detalles en las palabras.', 'ops': ['Observa detalles mínimos, como los detectives de enigma', 'Usa la fuerza para que confiesen', 'Resuelve por casualidad'], 'ayuda': 'Fijate en qué se apoya para investigar.'},
     {'cons': 'Muchos policiales argentinos muestran que la policía o el poder están del lado del culpable.', 'ops': ['Tienen rasgos del policial negro', 'Son siempre de enigma', 'No son policiales'], 'ayuda': 'La corrupción es un rasgo del negro.'}]),
   ('Policial argentino', 'El policial argentino toma las formas del enigma y del negro y las adapta a su propia sociedad, con detectives y escenarios locales.'),
   'Borges y Bioy Casares jugaron con el enigma clásico y lo llenaron de humor; Rodolfo Walsh empezó con cuentos de enigma y después mostró que, en la realidad, el crimen muchas veces lo cometía el poder. Conocer estas variantes permite reconocer qué tipo de policial estamos leyendo.',
   ['El género viaja y cambia con cada país.', 'Parodi: enigma con humor, desde una celda.', 'Walsh: del enigma a la denuncia.'])],
 'recuerda': [
   R('Policial negro', 'es la variante en la que el crimen muestra una sociedad violenta y corrupta, y el detective investiga en la calle.', 'El jefe de policía cobraba a la banda'),
   R('Policial de enigma', 'presenta el crimen como un rompecabezas que un detective genial resuelve razonando.', 'Una ceniza en la alfombra alcanza para resolverlo'),
   R('Detective duro', 'es un profesional solitario y desencantado que arriesga el cuerpo y tiene un código moral propio.', 'Rechaza el doble de plata y sigue con el caso'),
   R('Pregunta del negro', 'el policial negro no pregunta tanto quién lo hizo, sino por qué pasa.', 'El crimen está ligado al dinero y al poder'),
   R('Policial argentino', 'adapta el enigma y el negro a la sociedad argentina, con detectives propios.', 'Isidro Parodi; Daniel Hernández, de Walsh')]}

# ============================ ACTIVIDADES ============================
A = {
 '1': [
   CLA('¿Qué papel cumple cada personaje del caso «El robo del laboratorio»?', ['Detective', 'Víctima', 'Testigo', 'Culpable'], [('La profesora de Química, a la que le robaron el microscopio', 'Víctima'), ('El portero que vio salir a alguien con una caja', 'Testigo'), ('La preceptora que reúne las pistas y resuelve el caso', 'Detective'), ('El ayudante de laboratorio, que lo vendió', 'Culpable')], 'Cada personaje cumple un papel fijo del género.'),
   MC('¿Cuál es el enigma en este argumento? «En un barco, alguien abre la caja fuerte del capitán sin forzarla. La única combinación la conocían tres personas.»', ['¿Quién abrió la caja fuerte sin forzarla?', '¿Adónde va el barco?', '¿Cuánto dinero tiene el capitán?'], '¿Quién abrió la caja fuerte sin forzarla?', 'El enigma es la pregunta que el relato promete responder.', 'analizar'),
   MC('Un compañero dice: «Este relato no es policial porque no hay ningún muerto». El relato trata de una detective que averigua quién falsificó unas firmas. ¿Qué le contestás?', ['Es policial: lo que lo define es el enigma y la investigación', 'Tiene razón: sin muerto no hay policial', 'Es policial solo si aparece la policía'], 'Es policial: lo que lo define es el enigma y la investigación', 'El género se define por el enigma, no por la violencia.', 'error'),
   MS('En un relato, la detective resuelve el caso sin salir de su casa, observando una foto con lupa. Su sobrino la acompaña y no entiende nada. Elegí los DOS rasgos del detective de enigma que aparecen.', ['Observa detalles mínimos', 'Razona más que actúa', 'Usa la fuerza', 'Es un policía de uniforme'], ['Observa detalles mínimos', 'Razona más que actúa'], 'El detective clásico observa y razona.')],
 '2': [
   CLA('Caso: desaparecieron las llaves del auto de la abuela. Fue el nieto, que quería sacar el auto. ¿Pista o falsa pista?', ['Pista', 'Falsa pista'], [('El asiento del conductor está corrido hacia atrás', 'Pista'), ('El gato estaba durmiendo sobre el capó', 'Falsa pista'), ('El nieto tiene barro fresco en las zapatillas', 'Pista'), ('La vecina tiene cara de enojada', 'Falsa pista')], 'Una pista es un dato que se puede comprobar.'),
   ORD('Ordená el razonamiento de la detective.', ['Ve que el paraguas del sospechoso está seco', 'Recuerda que llovió toda la tarde', 'Deduce que no salió de la casa, aunque dijo que fue al banco', 'Comprueba en el banco que no estuvo ahí'], 'Observar, relacionar, deducir y comprobar.', 'aplicar'),
   UNI('El robo fue a las 22. Uní cada coartada con lo que pasa con ese sospechoso.', [('Estaba en una cena con diez invitados que lo vieron', 'Se descarta'), ('Dice que estaba en un partido que se suspendió por lluvia', 'Su coartada falsa es una pista'), ('Estaba solo en su casa y nadie puede confirmarlo', 'Sigue en la lista')], 'Coartada firme, falsa o sin testigos.', 'analizar'),
   MC('Un investigador acusa al jardinero «porque tiene mirada de culpable». ¿Qué error comete?', ['Se guía por una impresión, no por una pista', 'Acusa demasiado rápido a la víctima', 'Usa demasiadas pistas'], 'Se guía por una impresión, no por una pista', 'Las impresiones son falsas pistas: no prueban nada.', 'error')],
 '3': [
   ORD('Ordená la historia del crimen como ocurrió en el tiempo, aunque el relato la cuente al final.', ['El contador cambia los números del libro de cuentas', 'Saca el dinero de a poco durante un año', 'El dueño nota que falta plata y llama a la detective', 'La detective descubre los números cambiados y lo revela'], 'La historia del crimen empieza antes que la investigación.', 'aplicar'),
   TAP('Es un narrador testigo. Tocá las DOS partes que lo muestran: una dice que el protagonista es otro y la otra, que el narrador sabe menos que él.', ['Mi amigo levantó el sobre', 'a contraluz', 'y sonrió.', 'Yo, como siempre,', 'no entendí nada', 'hasta la noche.'], [0, 4], 'Cuenta con «yo» lo que hace otro y no lo entiende a tiempo: así se mantiene el suspenso.', 'analizar'),
   MC('Al final de un cuento, la detective revela que la culpable es una prima que nunca había sido mencionada. ¿Qué falla?', ['No respeta el juego limpio con el lector', 'La revelación es demasiado larga', 'Falta un narrador testigo'], 'No respeta el juego limpio con el lector', 'La culpable tiene que estar a la vista antes del final.', 'error'),
   UNI('Uní cada momento del policial con su ejemplo.', [('Crimen', 'Desaparece el anillo de la novia en la fiesta'), ('Investigación', 'El detective interroga a los invitados'), ('Revelación', 'Explica que el anillo cayó en la copa del padrino'), ('Historia oculta', 'El padrino lo escondió para pedir rescate')], 'La estructura en tres momentos y la historia oculta.', 'aplicar')],
 '4': [
   CLA('¿Policial de enigma o policial negro?', ['De enigma', 'Negro'], [('El detective reúne a los sospechosos en el salón del hotel', 'De enigma'), ('El detective recibe una paliza en un bar del puerto', 'Negro'), ('Una mancha de tinta alcanza para resolver el caso', 'De enigma'), ('El juez que lleva la causa está comprado por la mafia', 'Negro')], 'Rompecabezas o sociedad corrupta.'),
   ODD('Tres fragmentos son de policial negro y uno es de enigma. ¿Cuál es el de enigma?', ['«Todos los que la buscaban tenían placa de policía.»', '«Me partieron el labio en el bar, pero conseguí el nombre.»', '«Con una lupa, la detective notó que la firma estaba calcada.»', '«En esta ciudad, hasta el juez cobra de la banda.»'], '«Con una lupa, la detective notó que la firma estaba calcada.»', 'Observar un detalle con lupa es propio del detective de enigma; los demás muestran violencia y corrupción.', 'analizar'),
   MC('Una compañera dice que el policial negro se llama así porque los crímenes ocurren de noche. ¿Qué le contestás?', ['El nombre viene de su mirada oscura sobre la sociedad: violencia y corrupción', 'Tiene razón: todo pasa de noche', 'Se llama así porque el detective se viste de negro'], 'El nombre viene de su mirada oscura sobre la sociedad: violencia y corrupción', 'La noche es un escenario típico, pero lo que lo define es la mirada sobre la sociedad.', 'error'),
   KW('Elegí un detective (de enigma o duro) y explicá con tus palabras dos rasgos que lo ubican en ese tipo de policial.', 'Nombrá el tipo y dos rasgos.', [['enigma', 'negro', 'duro', 'clásico'], ['observa*', 'razona*', 'deduc*', 'arriesga*', 'calle', 'ciudad', 'corrup*', 'golpe*', 'pista*']], 2, 'Por ejemplo: Holmes es de enigma porque observa detalles y razona sin usar la fuerza.', 'aplicar')],
 '5': [
   MC('En un relato, una detective descubre que el robo del banco lo organizó el propio gerente, y aunque lo denuncia, el gerente queda libre. ¿Qué tipo de policial es?', ['Negro: el crimen muestra corrupción y el mal sigue', 'De enigma: el orden vuelve al final', 'No es policial'], 'Negro: el crimen muestra corrupción y el mal sigue', 'Final sin orden recuperado y poder corrupto.', 'analizar'),
   CLA('Caso: desapareció la tablet de la biblioteca. ¿Qué es cada dato?', ['Pista', 'Falsa pista', 'Coartada'], [('La funda apareció en la mochila del bibliotecario', 'Pista'), ('El chico nuevo parecía nervioso', 'Falsa pista'), ('La profesora estaba dando clase online frente a 30 alumnos', 'Coartada'), ('El registro muestra que la tablet se conectó desde la casa del bibliotecario', 'Pista')], 'Datos que acercan, impresiones que distraen y pruebas de que alguien estaba en otro lado.', 'analizar'),
   ORD('Ordená cómo se CUENTA un policial de enigma.', ['Aparece el crimen ya cometido', 'El detective investiga y descarta sospechosos', 'El detective reúne pistas y deduce', 'En la revelación se cuenta cómo ocurrió el crimen'], 'Lo que pasó primero se cuenta al final.', 'aplicar'),
   MC('¿Cuál de estos finales respeta el juego limpio?', ['El culpable es el vecino que en el primer capítulo mintió sobre su perro', 'El culpable es un desconocido que llega en el último párrafo', 'El detective adivina el nombre sin explicar cómo'], 'El culpable es el vecino que en el primer capítulo mintió sobre su perro', 'La solución se arma con pistas que el lector ya vio.', 'analizar')],
}

# ============================ LIBRO DEL NIVEL ============================
LIBRO = {'titulo': 'La liga de los pelirrojos', 'act': [
  ORD('Ordená la historia del crimen de «La liga de los pelirrojos» como ocurrió en el tiempo (no como se cuenta).', ['John Clay se emplea con Wilson por la mitad del sueldo', 'Clay y su cómplice inventan la Liga de los Pelirrojos', 'Wilson pasa las mañanas copiando la enciclopedia', 'Clay cava un túnel desde el sótano de Wilson hasta el banco', 'La liga se disuelve y Wilson consulta a Holmes'], 'La historia del crimen empezó mucho antes de que Wilson visitara a Holmes.', 'aplicar'),
  UNI('Uní cada detalle del cuento con lo que le revela a Holmes.', [('El ayudante cobra la mitad de lo normal', 'Le interesa estar en esa casa por otro motivo'), ('Pasa horas en el sótano', 'Hace algo a escondidas'), ('Tiene las rodillas del pantalón gastadas', 'Pasa mucho tiempo arrodillado, cavando'), ('Detrás de la casa hay un banco', 'Ahí está el objetivo del plan')], 'Holmes une detalles pequeños en una sola explicación.', 'analizar'),
  MC('¿Por qué la Liga de los Pelirrojos funciona como una falsa pista en el cuento?', ['Parece el misterio principal, pero solo sirve para vaciar la casa', 'Porque Wilson no es pelirrojo', 'Porque la liga existe de verdad y paga bien'], 'Parece el misterio principal, pero solo sirve para vaciar la casa', 'Lo más llamativo distrae de lo importante: el túnel.', 'analizar'),
  CLA('Ubicá a cada personaje del cuento en su papel dentro del género.', ['Detective', 'Narrador testigo', 'Víctima', 'Culpable'], [('Sherlock Holmes', 'Detective'), ('El doctor Watson', 'Narrador testigo'), ('Jabez Wilson', 'Víctima'), ('John Clay', 'Culpable')], 'Los papeles fijos del policial, en el cuento.', 'aplicar'),
  UNI('Uní cada paso del método del detective con lo que hace Holmes en el cuento.', [('Observar', 'Mira las rodillas gastadas del ayudante'), ('Relacionar', 'Recuerda que detrás de la casa hay un banco'), ('Deducir', 'Concluye que están cavando un túnel hacia el banco'), ('Comprobar', 'Golpea la vereda con el bastón para oír si suena hueco')], 'Holmes sigue el método completo antes de actuar.', 'analizar'),
  KW('¿«La liga de los pelirrojos» es un policial de enigma o negro? Justificá con dos rasgos del cuento.', 'Nombrá el tipo y dos rasgos con ejemplos del cuento.', [['enigma', 'clásico'], ['holmes', 'deduc*', 'razona*', 'observa*', 'pista*', 'watson', 'revela*', 'túnel', 'tunel', 'orden']], 2, 'Es de enigma: Holmes resuelve el caso observando y razonando, y al final el orden vuelve con la captura de Clay.', 'analizar'),
]}

# ============================ EXAMEN ============================
EX = [
 [1, MC('¿Qué define a un relato policial?', ['Un enigma que alguien investiga hasta resolverlo', 'Un policía que patrulla las calles de la ciudad', 'Muchas escenas de peleas, persecuciones y disparos'], 'Un enigma que alguien investiga hasta resolverlo', 'El género se define por el enigma y la investigación.', 'recordar')],
 [1, CLA('¿Qué papel cumple cada uno en el caso del robo en la estancia?', ['Detective', 'Víctima', 'Testigo', 'Culpable'], [('El veterinario que investiga y resuelve el caso', 'Detective'), ('El dueño al que le robaron los caballos', 'Víctima'), ('El peón que vio luces de un camión de noche', 'Testigo'), ('El capataz, que vendió los caballos', 'Culpable')], 'Los papeles fijos del policial.', 'aplicar')],
 [1, MC('Un detective resuelve el caso mirando una foto con lupa y sin salir de su escritorio. ¿Qué tipo de detective es?', ['De enigma: observa y razona', 'Duro: arriesga el cuerpo en la calle', 'No es un detective'], 'De enigma: observa y razona', 'El detective clásico razona más de lo que actúa.', 'analizar')],
 [2, CLA('Caso: alguien se llevó el dinero de la alcancía de la escuela. Fue la tesorera. ¿Pista o falsa pista?', ['Pista', 'Falsa pista'], [('La alcancía se abrió con la llave que tiene la tesorera', 'Pista'), ('El chico de tercero estaba muy callado', 'Falsa pista'), ('La tesorera pagó una deuda grande al día siguiente', 'Pista'), ('El portero no saludó a nadie esa mañana', 'Falsa pista')], 'Datos comprobables frente a impresiones.', 'analizar')],
 [2, ORD('Ordená el método del detective.', ['Observar', 'Relacionar', 'Deducir', 'Comprobar'], 'Ese es el orden del razonamiento.', 'recordar')],
 [2, MC('El sospechoso dice que a la hora del robo estaba en el hospital, y lo confirman dos médicas. ¿Qué pasa con él?', ['Se descarta: tiene una coartada firme', 'Sigue sospechado: es el que más gana', 'Es el culpable'], 'Se descarta: tiene una coartada firme', 'Una coartada comprobada descarta al sospechoso.', 'aplicar')],
 [3, UNI('Uní cada parte del policial de enigma con su descripción.', [('Historia del crimen', 'Pasó antes y queda oculta'), ('Historia de la investigación', 'La que el lector sigue paso a paso'), ('Revelación', 'El detective explica cómo resolvió el caso')], 'Las dos historias se unen en la revelación.', 'recordar')],
 [3, SA('«Mi compañero miró el piso un largo rato; yo me aburría y no veía nada.» ¿Qué tipo de narrador es? Escribí una palabra.', ['testigo', 'narrador testigo', 'un narrador testigo'], 'Cuenta con «yo» lo que hace el protagonista, sin entenderlo.', 'aplicar')],
 [3, MC('Un lector se queja: «El culpable apareció recién en la última página». ¿Qué no respetó el autor?', ['El juego limpio: el culpable tiene que estar a la vista', 'El narrador testigo', 'La historia de la investigación'], 'El juego limpio: el culpable tiene que estar a la vista', 'La solución se arma con lo que el lector ya vio.', 'analizar')],
 [4, CLA('¿Policial de enigma o negro?', ['De enigma', 'Negro'], [('Un genio aficionado reúne a todos en la biblioteca', 'De enigma'), ('El detective camina por el puerto con miedo de que lo sigan', 'Negro'), ('El comisario está pagado por la banda', 'Negro'), ('Una ceniza en la alfombra resuelve el caso', 'De enigma')], 'Rompecabezas o sociedad corrupta.', 'aplicar')],
 [4, MC('¿Qué pregunta importa más en el policial negro?', ['¿Por qué pasa esto en esta sociedad?', '¿Quién tenía la llave?', '¿A qué hora fue el robo?'], '¿Por qué pasa esto en esta sociedad?', 'El negro liga el crimen con el dinero y el poder.', 'recordar')],
 [4, MC('«Me ofrecieron el triple para cerrar el caso. Lo rechacé y esa noche me esperaron en el estacionamiento.» ¿Qué rasgos del detective duro aparecen?', ['Tiene un código moral propio y arriesga el cuerpo', 'Razona desde el sillón y nunca corre peligro', 'Trabaja gratis y la policía lo ayuda'], 'Tiene un código moral propio y arriesga el cuerpo', 'Rechaza el soborno y paga el precio en la calle.', 'analizar')],
 [4, KW('Explicá con tus palabras una diferencia entre el policial de enigma y el policial negro.', 'Nombrá los dos tipos y en qué se diferencian.', [['enigma', 'clásico'], ['negro'], ['razona*', 'rompecabezas', 'deduc*', 'ciudad', 'violen*', 'corrup*', 'calle', 'orden', 'arriesga*', 'por qué', 'quién']], 3, 'Por ejemplo: en el de enigma el detective razona y el orden vuelve; en el negro investiga en una ciudad corrupta y el mal sigue.', 'aplicar')],
]

# ============================ CARPETA del nivel 4 ============================
CARPETA4 = [
 ('Un fragmento dice: «Llovía sobre el puerto y el comisario también cobraba de la banda». ¿Es policial de enigma o negro?', 'aplicar', ['negro', 'policial negro'], 'Negro: la ciudad de noche y la corrupción de la policía son rasgos del negro.'),
 ('Un detective resuelve el robo sin salir del sillón, escuchando el relato de su cliente. ¿Es un detective de enigma o un detective duro?', 'aplicar', ['de enigma', 'enigma'], 'De enigma: razona sin moverse ni arriesgarse.'),
 ('Al final de una novela, el detective descubre al asesino, pero el político que lo protegía sigue en su cargo. ¿Qué rasgo del policial negro muestra ese final?', 'analizar', ['que el mal sigue', 'el mal sigue', 'la corrupción sigue', 'corrupción'], 'Que el mal sigue: se resuelve un caso, pero la sociedad corrupta no cambia.'),
 ('Juli dice que un relato es policial negro porque el crimen ocurre de noche, aunque el detective lo resuelve razonando en una mansión. ¿Qué tipo de policial es en realidad?', 'error', ['de enigma', 'enigma'], 'De enigma: la noche no alcanza; lo define el detective que razona en un lugar cerrado.'),
]

def ajustes(M):
    M['act'] = A
    M['examen'] = EX
    M['libro'] = LIBRO
    M['practica'] = 'Actividades generales'
    M['examen_titulo'] = 'Nivel jefe: el policial'
    M['actualizar_preguntas'] = True
    N = M['niveles'].setdefault('4', {})
    N['carpeta'] = [c for c, _, _, _ in CARPETA4]
    N['carpeta_nivel'] = [t for _, t, _, _ in CARPETA4]
    N['respuestas_carpeta'] = [r for _, _, r, _ in CARPETA4]
    N.setdefault('soluciones', {})['carpeta'] = [s for _, _, _, s in CARPETA4]

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-2/mision-2.json', L, ajustes=ajustes)
