# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 9 · La épica y sus héroes (TODO nuevo, sin libro: fragmentos de epopeyas de dominio público, contados con palabras propias)
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD
RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', '..')

# ============================ CLASES ANIMADAS ============================
STEP = {'1': '94351222-b38d-4ae2-bdd6-915c413fecbc', '2': 'b920ef72-c182-4ebd-87c6-9ffaaa804b76', '3': 'c5cfa4f1-f01d-4846-b1dd-d74d4ada8387', '4': 'a8476b20-35d3-4d28-b1eb-aae7b765ba9b'}
TIT = {'1': 'El héroe épico', '2': 'El viaje y las pruebas', '3': 'Dioses, destino y fama', '4': 'De la epopeya al relato'}
CL = {}
CL['1'] = [
 {'t': 'documental', 'emojis': ['🏛️', '⚔️', '🔥'], 'lugar': 'Troya, hace casi tres mil años', 'rotulos': [{'txt': 'Una guerra de diez años', 'sub': 'griegos contra troyanos'}, {'txt': 'Un relato que se cantó por siglos', 'sub': 'la Ilíada'}],
  'voz': ['Troya, hace casi tres mil años: griegos y troyanos llevan diez años en guerra frente a las murallas de la ciudad.', 'Esa guerra se contó cantando, de generación en generación, durante siglos, hasta que se escribió. Es la *Ilíada*, una de las grandes epopeyas de la historia.']},
 {'t': 'definicion', 'palabra': 'Épica', 'texto': 'Género que narra, casi siempre en verso, las hazañas de un héroe que representa los valores de un pueblo.', 'emoji': '🛡️',
  'voz': ['La *épica* es el género que narra las hazañas de un héroe, casi siempre en verso.', 'Y ese héroe no es cualquiera: representa lo que su pueblo más admira. Cada obra épica se llama *epopeya*.']},
 {'t': 'zoom', 'niveles': [{'emoji': '🏘️', 'txt': 'un pueblo y sus valores'}, {'emoji': '🦸', 'txt': 'un héroe que los encarna'}, {'emoji': '⚔️', 'txt': 'hazañas extraordinarias'}],
  'voz': ['Mirá cómo se arma una epopeya. Primero hay un *pueblo* con sus valores: el valor, la lealtad, el honor.', 'Después, un *héroe* que encarna esos valores mejor que nadie.', 'Y finalmente, sus *hazañas*: acciones extraordinarias que lo vuelven inolvidable.']},
 {'t': 'versus', 'a': {'txt': 'Aquiles', 'emoji': '🗡️', 'datos': ['la fuerza', 'el mejor guerrero', 'Ilíada']}, 'b': {'txt': 'Odiseo', 'emoji': '🧠', 'datos': ['la astucia', 'el más ingenioso', 'Odisea']}, 'gana': 'empate', 'veredicto': 'Dos formas de ser héroe',
  'voz': ['Dos grandes héroes griegos, cara a cara.', '*Aquiles*, el protagonista de la Ilíada, es el guerrero más fuerte y veloz: casi invencible en combate.', '*Odiseo*, el de la Odisea, gana con la *astucia*: engaña, inventa planes y sale de cualquier trampa.', 'No hay ganador: fuerza e ingenio son dos maneras de ser héroe épico.']},
 {'t': 'unir', 'titulo': 'LOS EPÍTETOS', 'pares': [['Aquiles', 'el de los pies ligeros'], ['Odiseo', 'el de muchos recursos'], ['el Cid', 'el que en buena hora nació']],
  'voz': ['Las epopeyas usan *epítetos*: frases fijas que acompañan siempre el nombre del héroe y lo caracterizan.', 'Aquiles es «el de los pies ligeros», por su velocidad.', 'Odiseo, «el de muchos recursos», por su ingenio.', 'Y el Cid, el héroe castellano, «el que en buena hora nació».']},
 {'t': 'quiz4', 'pregunta': '¿Qué tiene que tener un relato para ser épico?', 'opciones': ['Un héroe y sus hazañas', 'Un detective', 'Una historia de amor', 'Un narrador que sea niño'], 'correcta': 0,
  'voz': ['Pregunta: ¿qué tiene que tener un relato para ser épico?', 'Pensá en el centro de la Ilíada.', '*Un héroe y sus hazañas*: ese es el corazón del género.']},
 {'t': 'errores', 'items': [{'mal': 'El héroe épico es un superhéroe con poderes', 'bien': 'Es humano, aunque a veces hijo de un dios, y puede morir'}, {'mal': 'La épica se escribió en prosa', 'bien': 'Las epopeyas clásicas están en verso, para recordarlas y cantarlas'}],
  'voz': ['Dos confusiones comunes.', 'El héroe épico no es un superhéroe: es humano, aunque a veces sea hijo de un dios, y puede sufrir y morir.', 'Y las epopeyas clásicas no están en prosa: están en *verso*, porque se cantaban y había que recordarlas.']},
 {'t': 'resumen', 'items': [['Épica', 'hazañas de un héroe, en verso'], ['Epopeya', 'cada obra del género'], ['Héroe épico', 'encarna los valores de un pueblo'], ['Epíteto', 'frase fija que acompaña al nombre']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 1'},
  'voz': ['Repasemos.', 'La épica es el relato de los grandes héroes.', 'El género.', 'La epopeya.', 'El héroe que encarna los valores de su pueblo.', 'Y el epíteto que lo acompaña. ¡A practicar!']},
]
CL['2'] = [
 {'t': 'historia', 'personaje': {'nombre': 'Odiseo', 'emoji': '⛵'}, 'lugar': '🌊', 'lineas': ['Termina la guerra de Troya.', 'Odiseo quiere volver a su casa, en Ítaca.', 'El viaje le lleva diez años.'], 'titulo': 'EL VIAJE', 'sub': 'y las pruebas del héroe',
  'voz': ['Termina la guerra de Troya.', 'Odiseo solo quiere volver a su isla, Ítaca, con su esposa y su hijo.', 'Pero el viaje, que tendría que durar unas semanas, le lleva *diez años*.', 'Esa vuelta llena de peligros es la *Odisea*. Hoy vemos por qué el viaje es tan importante en la épica.']},
 {'t': 'ciclo', 'titulo': 'EL VIAJE DEL HÉROE', 'items': ['Partida', 'Pruebas', 'Ayudas', 'Regreso'],
  'voz': ['Muchas epopeyas siguen un mismo camino.', 'La *partida*: el héroe deja su lugar.', 'Las *pruebas*: monstruos, tormentas y tentaciones.', 'Las *ayudas*: dioses o personajes que le dan una mano.', 'Y el *regreso*: vuelve transformado, con más sabiduría.']},
 {'t': 'pistas', 'problema': 'Odiseo y sus hombres están encerrados en la cueva de un cíclope gigante. ¿Cómo escapan?', 'pistas': ['Le dice al cíclope que se llama «Nadie»', 'Lo deja ciego mientras duerme'], 'respuesta': 'Cuando el cíclope pide ayuda gritando «¡Nadie me ataca!», nadie viene',
  'voz': ['Una de las pruebas más famosas: Odiseo y sus hombres quedan encerrados en la cueva de Polifemo, un cíclope gigante. ¿Cómo escapan?', 'No pueden ganarle por la fuerza: tienen que pensar.', 'Primera pista: Odiseo le dice al cíclope que su nombre es «Nadie».', 'Segunda: mientras el gigante duerme, lo deja ciego. Cuando Polifemo grita pidiendo ayuda, dice «¡Nadie me ataca!», y nadie viene. La astucia vence a la fuerza.']},
 {'t': 'orden', 'titulo': 'ASÍ PASÓ / ASÍ SE CUENTA', 'items': [{'txt': 'Termina la guerra', 'emoji': '🏛️'}, {'txt': 'Años de viaje y pruebas', 'emoji': '⛵'}, {'txt': 'Odiseo, atrapado en una isla', 'emoji': '🏝️'}, {'txt': 'Vuelve a Ítaca', 'emoji': '🏠'}], 'relato': [2, 0, 1, 3],
  'voz': ['Mirá el orden real: termina la guerra, Odiseo viaja durante años, queda atrapado en una isla y finalmente vuelve.', 'Pero la Odisea no empieza por el principio: arranca con Odiseo ya atrapado en la isla, muchos años después de la guerra.', 'Sus aventuras anteriores las cuenta él mismo más adelante, recordándolas.']},
 {'t': 'definicion', 'palabra': 'In medias res', 'texto': 'Comienzo de un relato en medio de la acción, que después recupera lo que pasó antes.', 'emoji': '⏯️',
  'voz': ['Esa técnica se llama *in medias res*, que en latín significa «en medio del asunto».', 'El relato empieza en plena acción y después vuelve atrás para contar lo anterior. La épica la usa desde hace miles de años.']},
 {'t': 'vof', 'afirmacion': 'En la épica, el héroe vence todas sus pruebas solo con la fuerza.', 'emoji': '💪', 'verdadero': False, 'explicacion': 'También necesita astucia, paciencia y, muchas veces, la ayuda de otros.',
  'voz': ['Verdadero o falso: en la épica, el héroe vence todas sus pruebas solo con la fuerza.', 'Acordate del cíclope.', 'Falso: también necesita astucia, paciencia y, muchas veces, ayuda.']},
 {'t': 'resumen', 'items': [['El viaje', 'partida, pruebas, ayudas y regreso'], ['Las pruebas', 'monstruos, peligros y tentaciones'], ['Astucia', 'a veces vale más que la fuerza'], ['In medias res', 'empezar en medio de la acción']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 2'},
  'voz': ['Repasemos.', 'El viaje pone a prueba al héroe y lo transforma.', 'La estructura del viaje.', 'Las pruebas.', 'La astucia.', 'Y el comienzo in medias res. ¡A practicar!']},
]
CL['3'] = [
 {'t': 'reto', 'texto': 'En plena tormenta, una diosa calma el mar para salvar a un héroe. ¿Quién decide su suerte: él o los dioses?', 'segundos': 6, 'respuesta': 'Los dos: el héroe actúa, los dioses intervienen', 'emoji': '🌩️', 'titulo': 'DIOSES Y DESTINO', 'sub': 'más allá del héroe',
  'voz': ['Reto: en plena tormenta, una diosa calma el mar para salvar a un héroe. ¿Quién decide su suerte: él o los dioses?', 'Seis segundos.', 'Los dos: el héroe actúa, pero en la épica los dioses también intervienen. Hoy vemos cómo.']},
 {'t': 'balanza', 'izq': {'cab': 'Lo ayudan', 'items': ['Atenea lo aconseja', 'Hermes le da un antídoto']}, 'der': {'cab': 'Lo frenan', 'items': ['Poseidón le manda tormentas', 'Circe lo retiene']}, 'gana': 'izq',
  'voz': ['En la Odisea, los dioses se dividen. Atenea, diosa de la sabiduría, lo aconseja y lo protege; Hermes le da un antídoto contra una hechicera.', 'Del otro lado, Poseidón, el dios del mar, lo persigue con tormentas, furioso porque Odiseo dejó ciego a su hijo, el cíclope.', 'Al final pesa más la ayuda: con la protección de Atenea, Odiseo consigue volver.']},
 {'t': 'dilema', 'situacion': 'A Aquiles le anuncian su destino: puede elegir entre dos vidas.', 'emoji': '⚖️', 'a': {'txt': 'Quedarse en su casa', 'consecuencia': 'vida larga, pero nadie lo recordará', 'emoji': '🏡'}, 'b': {'txt': 'Ir a la guerra', 'consecuencia': 'vida corta, pero gloria eterna', 'emoji': '🏆'},
  'voz': ['Un dilema famoso: a Aquiles le anuncian que su destino tiene dos caminos.', 'Si se queda en su casa, tendrá una vida larga, pero nadie lo recordará.', 'Si va a la guerra, morirá joven, pero su gloria será eterna. Aquiles elige la gloria.']},
 {'t': 'definicion', 'palabra': 'Destino', 'texto': 'En la épica, lo que está decidido para cada personaje y que ni los héroes pueden cambiar.', 'emoji': '🧵',
  'voz': ['Esa idea se llama *destino*: lo que está decidido para cada personaje, y que ni siquiera los héroes pueden evitar.', 'Lo que el héroe sí elige es *cómo* enfrentarlo, y en eso muestra su grandeza.']},
 {'t': 'bloques', 'titulo': 'LO QUE BUSCA EL HÉROE', 'items': [{'cab': 'Gloria', 'txt': 'ser recordado por sus hazañas'}, {'cab': 'Honra', 'txt': 'el respeto y la buena fama'}, {'cab': 'Lealtad', 'txt': 'cumplir con su rey y su gente'}],
  'voz': ['¿Qué busca el héroe épico?', 'La *gloria*: que sus hazañas se recuerden después de su muerte.', 'La *honra*: el respeto de los demás. El Cid, desterrado por su rey, pelea para recuperarla.', 'Y la *lealtad*: aun desterrado, el Cid sigue enviándole regalos al rey que lo echó.']},
 {'t': 'pregunta', 'pregunta': '¿Por qué Poseidón persigue a Odiseo?', 'opciones': ['Porque Odiseo dejó ciego a su hijo', 'Porque Odiseo le robó el mar', 'Porque Atenea se lo pidió'], 'correcta': 0,
  'voz': ['Pregunta: ¿por qué Poseidón persigue a Odiseo durante todo el viaje?', 'Pensá en el cíclope.', 'Porque Odiseo dejó ciego a su hijo, Polifemo. Los dioses de la épica tienen pasiones muy humanas.']},
 {'t': 'errores', 'items': [{'mal': 'Si los dioses deciden todo, el héroe no importa', 'bien': 'El héroe elige cómo enfrentar su destino'}, {'mal': 'La honra es lo mismo que la riqueza', 'bien': 'La honra es la buena fama y el respeto'}],
  'voz': ['Dos errores para evitar.', 'Creer que el héroe no importa porque los dioses intervienen: el héroe elige *cómo* enfrenta su destino.', 'Y confundir honra con riqueza: la honra es la *buena fama*, el respeto de los demás.']},
 {'t': 'resumen', 'items': [['Dioses', 'ayudan o castigan al héroe'], ['Destino', 'lo decidido, que no se puede cambiar'], ['Gloria y honra', 'fama y respeto'], ['Lealtad', 'cumplir con su gente']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 3'},
  'voz': ['Repasemos.', 'El héroe épico no está solo: lo rodean fuerzas más grandes.', 'Los dioses.', 'El destino.', 'La gloria y la honra.', 'Y la lealtad. ¡A practicar!']},
]
CL['4'] = [
 {'t': 'personaje', 'personaje': {'nombre': 'El aedo', 'emoji': '🎶'}, 'lineas': [{'txt': 'Canto la cólera de Aquiles…', 'animo': 'feliz'}, {'txt': 'Y la repito cada noche, igual y distinta.', 'animo': 'piensa'}],
  'voz': ['En la antigua Grecia, las epopeyas las cantaban los *aedos*, poetas que recorrían pueblos y palacios. Empezaban invocando a la diosa de la poesía para cantar la cólera de Aquiles.', 'Cada noche repetían el relato de memoria, sin libro, y por eso la épica tiene tantas fórmulas y repeticiones.']},
 {'t': 'definicion', 'palabra': 'Transmisión oral', 'texto': 'Forma de conservar un relato contándolo o cantándolo de memoria, de generación en generación.', 'emoji': '🗣️',
  'voz': ['Eso se llama *transmisión oral*: un relato que se conserva contándolo de memoria, de generación en generación.', 'Los epítetos, el verso y las frases repetidas ayudaban a recordar historias larguísimas.']},
 {'t': 'linea', 'titulo': 'EPOPEYAS DEL MUNDO', 'eventos': [{'fecha': 'Hace +4.000 años', 'txt': 'Gilgamesh, en Mesopotamia', 'emoji': '🏺'}, {'fecha': 'Siglo VIII a. C.', 'txt': 'Ilíada y Odisea, en Grecia', 'emoji': '🏛️'}, {'fecha': 'Edad Media', 'txt': 'Beowulf, en Inglaterra', 'emoji': '🐉'}, {'fecha': 'Hacia 1200', 'txt': 'Cantar de mio Cid, en España', 'emoji': '🐎'}],
  'voz': ['La épica es de todo el mundo. Hace más de cuatro mil años, en Mesopotamia, se contaba la historia de *Gilgamesh*, un rey que busca la inmortalidad.', 'En Grecia, hacia el siglo octavo antes de Cristo, la *Ilíada* y la *Odisea*.', 'En la Inglaterra medieval, *Beowulf*, el guerrero que enfrenta a un monstruo y a un dragón.', 'Y hacia el año 1200, en España, el *Cantar de mio Cid*, que cantaban los juglares.']},
 {'t': 'comparar', 'a': {'cab': 'Héroe épico', 'texto': 'perfecto, representa a su pueblo, busca la gloria', 'emoji': '🛡️'}, 'b': {'cab': 'Héroe de hoy', 'texto': 'con dudas y miedos, busca su propio camino', 'emoji': '🎒'}, 'signo': '→',
  'voz': ['¿Y qué quedó de todo eso?', 'El héroe épico es casi perfecto: representa a su pueblo y busca la gloria.', 'El héroe de los relatos actuales tiene dudas, miedos y defectos, y muchas veces busca su propio camino más que la fama.']},
 {'t': 'prediccion', 'pregunta': 'Una saga actual: un chico deja su pueblo, enfrenta pruebas, recibe ayuda de un mentor y vuelve cambiado. ¿Tiene algo de épica?', 'a': {'txt': 'Nada que ver', 'emoji': '🙅'}, 'b': {'txt': 'Sí: el viaje del héroe', 'emoji': '🗺️'}, 'correcta': 'b', 'resultado': 'Repite la estructura de partida, pruebas, ayuda y regreso.',
  'voz': ['¿Qué creés? En una saga actual, un chico deja su pueblo, enfrenta pruebas, recibe ayuda de un mentor y vuelve cambiado. ¿Tiene algo de épica?', 'Pensá en Odiseo.', 'Sí: repite el *viaje del héroe*. Muchas películas, novelas y videojuegos de hoy usan esa estructura milenaria.']},
 {'t': 'logro', 'titulo': '¡Misión cumplida!', 'items': ['El héroe épico y sus epítetos', 'El viaje y las pruebas', 'Dioses, destino y fama', 'La épica en el tiempo'], 'xp': 100,
  'voz': ['¡Terminaste las clases de la misión!', 'Ya conocés al héroe épico y sus epítetos.', 'El viaje y sus pruebas.', 'El papel de los dioses, el destino y la fama.', 'Y cómo la épica llega hasta los relatos de hoy. ¡A practicar!']},
]
for n, esc in CL.items():
    json.dump({'slug': f'leng1-m9-n{n}', 'step_id': STEP[n], 'materia': 'Lengua y Literatura I', 'titulo': TIT[n], 'sub': f'Lengua y Literatura I · Misión 9 · Nivel {n}', 'escenas': esc},
              open(os.path.join(RAIZ, 'tools/clase/lecciones', f'leng1-m9-n{n}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ============================ LECCIÓN ============================
L = {}
L['1'] = {'temas': [
 T('Qué es la épica',
   m('esquema', items=[
     {'nombre': 'Ilíada', 'raiz': 'La Ilíada (Grecia, siglo VIII a. C.)', 'ramas': [['El héroe', ['Aquiles, el mejor guerrero griego'], 'Encarna el valor y la fuerza.'], ['La hazaña', ['vence a Héctor, el gran defensor de Troya'], 'Una acción extraordinaria.'], ['El pueblo', ['los griegos, en guerra contra Troya'], 'El héroe representa a todo un pueblo.'], ['La forma', ['un largo poema en verso, cantado de memoria'], 'Así se conservaba.']], 'cierre': 'Héroe, hazaña, pueblo y verso: los rasgos de una epopeya.'},
     {'nombre': 'Cantar de mio Cid', 'raiz': 'El Cantar de mio Cid (España, hacia 1200)', 'ramas': [['El héroe', ['Rodrigo Díaz de Vivar, el Cid'], 'Un guerrero castellano real, idealizado.'], ['La hazaña', ['recupera su honra después de ser desterrado'], 'Vence batallas y conquista Valencia.'], ['El pueblo', ['Castilla en la Edad Media'], 'Encarna la lealtad y el valor.'], ['La forma', ['un poema que cantaban los juglares'], 'También para recordar y cantar.']], 'cierre': 'Dos epopeyas separadas por dos mil años, con los mismos rasgos.'}]),
   m('elegir_x', consigna='¿Cuál de estos argumentos corresponde a una epopeya?', items=[
     {'cons': 'Elegí el argumento épico.', 'ops': ['Un rey parte a buscar la planta de la inmortalidad y enfrenta monstruos en su camino', 'Una chica cuenta en su diario su primer día de clases', 'Un detective descubre quién robó un collar'], 'ayuda': 'Buscá un héroe y hazañas extraordinarias.'},
     {'cons': 'Elegí el argumento épico.', 'ops': ['Un guerrero defiende a su pueblo de un monstruo que ataca de noche el salón del rey', 'Dos amigos discuten por un partido de fútbol', 'Una familia se muda a una casa embrujada y se ríe del fantasma'], 'ayuda': 'El héroe defiende a todo un pueblo.'},
     {'cons': 'Elegí el argumento épico.', 'ops': ['Un caballero desterrado gana batallas para recuperar el honor ante su rey', 'Un científico explica cómo funciona un volcán', 'Una vendedora cuenta cómo abrió su negocio'], 'ayuda': 'Honor, batallas y un héroe.'}]),
   ('Épica', 'La épica es el género literario que narra, casi siempre en verso, las hazañas de un héroe que representa los valores de un pueblo; cada obra épica se llama epopeya.'),
   'Las epopeyas nacieron cuando la mayoría de la gente no sabía leer: se cantaban en plazas, palacios y fiestas, y servían para recordar quiénes eran y qué admiraban. Por eso el héroe no es solo un personaje: es el modelo de lo que ese pueblo valoraba.',
   ['Un héroe que realiza hazañas.', 'Representa los valores de un pueblo.', 'En verso, para cantarse y recordarse.']),
 T('Los rasgos del héroe épico',
   m('marcar', rotulo='Héroe', items=[
     {'nombre': 'Aquiles', 'texto': 'Aquiles es {{hijo de una diosa del mar y de un rey|Origen extraordinario: mitad divino.}}. {{En el combate nadie lo iguala en fuerza y velocidad|Fuerza y valor sobrehumanos.}}, pero {{su orgullo herido lo hace retirarse de la guerra y los griegos empiezan a perder|También tiene defectos humanos.}}.', 'cierre': 'Extraordinario, pero humano.'},
     {'nombre': 'Odiseo', 'texto': 'Odiseo es {{rey de una pequeña isla, Ítaca|Origen noble.}}. No es el más fuerte, pero {{es el más ingenioso: idea el caballo de madera que permite entrar en Troya|Su gran virtud es la astucia.}} y {{soporta diez años de viaje para volver con los suyos|Paciencia y resistencia.}}.', 'cierre': 'La inteligencia también es heroica.'}]),
   m('unir_x', consigna='Uní cada héroe con la virtud que más lo caracteriza.', items=[
     {'pares': [['Aquiles', 'la fuerza en el combate'], ['Odiseo', 'la astucia'], ['El Cid', 'la lealtad a su rey'], ['Gilgamesh', 'el deseo de vencer a la muerte']]},
     {'pares': [['Héctor', 'la defensa de su ciudad'], ['Beowulf', 'el valor frente al monstruo'], ['Penélope', 'la fidelidad y el ingenio'], ['Aquiles', 'la búsqueda de gloria']]}]),
   ('Héroe épico', 'El héroe épico es el protagonista de la epopeya: tiene un origen noble o divino, virtudes extraordinarias como la fuerza, el valor o la astucia, y representa los valores de su pueblo.'),
   'Aunque parezca invencible, el héroe épico es humano: se enoja, sufre, se equivoca y puede morir, y eso lo vuelve cercano para quien escucha su historia. Cada epopeya destaca una virtud distinta: la fuerza en Aquiles, la astucia en Odiseo, la lealtad en el Cid.',
   ['Origen noble o divino.', 'Virtudes extraordinarias: fuerza, valor, astucia.', 'Humano: sufre, se equivoca y puede morir.']),
 T('El epíteto épico',
   m('marcar', rotulo='Fragmento', items=[
     {'nombre': 'Ilíada', 'texto': 'Entonces {{Aquiles, el de los pies ligeros|Epíteto: destaca su velocidad.}}, tomó la lanza, y {{Héctor, el domador de caballos|Epíteto del héroe troyano.}}, lo esperó frente a las murallas.', 'cierre': 'Cada vez que aparece un héroe, aparece su epíteto.'},
     {'nombre': 'Cantar de mio Cid', 'texto': 'Salió de Burgos {{el que en buena hora nació|Epíteto del Cid: anuncia su destino glorioso.}}, con sesenta caballeros, y {{su leal Álvar Fáñez|Otro epíteto: la lealtad del compañero.}} cabalgaba a su lado.', 'cierre': 'También en la épica medieval.'}]),
   m('elegir_x', consigna='¿Qué rasgo destaca cada epíteto?', items=[
     {'cons': '«Odiseo, el de muchos recursos»', 'ops': ['Su ingenio para salir de los problemas', 'Su riqueza', 'Su fuerza física'], 'ayuda': 'Los «recursos» son ideas, trucos, soluciones.'},
     {'cons': '«Atenea, la de ojos brillantes»', 'ops': ['Una mirada viva e inteligente', 'Que está siempre enojada', 'Que es muy alta'], 'ayuda': 'Atenea es la diosa de la sabiduría.'},
     {'cons': '«La Aurora, de dedos rosados»', 'ops': ['El color del cielo al amanecer', 'Que tiene las manos lastimadas', 'Que es una mujer anciana'], 'ayuda': 'La aurora es el amanecer.'}]),
   ('Epíteto épico', 'El epíteto épico es una frase fija que acompaña el nombre de un personaje y destaca su rasgo principal, como «Aquiles, el de los pies ligeros».'),
   'Los epítetos se repiten cada vez que aparece el personaje. Para los aedos y juglares, que cantaban de memoria, eran fórmulas que ayudaban a recordar y a completar el verso; para el público, eran una manera de reconocer enseguida a cada héroe.',
   ['Frase fija junto al nombre.', 'Destaca el rasgo principal.', 'Se repite: ayudaba a recordar y cantar.'])],
 'recuerda': [
   R('Épica', 'es el género que narra, casi siempre en verso, las hazañas de un héroe que representa los valores de un pueblo.', 'La Ilíada, el Cantar de mio Cid'),
   R('Epopeya', 'es cada obra extensa del género épico, que cuenta las hazañas de uno o varios héroes.', 'La Odisea'),
   R('Héroe épico', 'tiene origen noble o divino y virtudes extraordinarias, pero sigue siendo humano y puede morir.', 'Aquiles, hijo de una diosa'),
   R('Virtudes heroicas', 'son las cualidades que cada epopeya destaca en su héroe, como la fuerza, la astucia o la lealtad.', 'La astucia de Odiseo'),
   R('Epíteto épico', 'es una frase fija que acompaña el nombre de un personaje y destaca su rasgo principal.', 'Aquiles, el de los pies ligeros')]}

L['2'] = {'temas': [
 T('El viaje del héroe',
   m('linea_tiempo', items=[
     {'nombre': 'Odisea', 'hechos': [{'t': 'Odiseo parte de Troya con sus barcos', 'c': 1}, {'t': 'Enfrenta al cíclope, las sirenas y otras pruebas', 'c': 2}, {'t': 'Atenea y otros lo ayudan a seguir', 'c': 3}, {'t': 'Llega a Ítaca disfrazado de mendigo', 'c': 4}, {'t': 'Recupera su casa y vuelve con Penélope', 'c': 5}],
      'marca': 'Partida, pruebas, ayudas y regreso.', 'cierre': 'El viaje transforma al héroe.'},
     {'nombre': 'Gilgamesh', 'hechos': [{'t': 'Gilgamesh pierde a su amigo Enkidu y teme a la muerte', 'c': 1}, {'t': 'Parte a buscar el secreto de la inmortalidad', 'c': 2}, {'t': 'Cruza montañas y aguas de la muerte', 'c': 3}, {'t': 'Consigue una planta mágica, pero una serpiente se la roba', 'c': 4}, {'t': 'Vuelve a su ciudad y acepta ser mortal', 'c': 5}],
      'marca': 'El regreso trae sabiduría, no premios.', 'cierre': 'La estructura es la misma en epopeyas muy lejanas.'}]),
   m('ordenar_x', consigna='Ordená las etapas del viaje del héroe.', items=[
     {'lista': ['Beowulf deja su tierra para ayudar a un rey vecino', 'Enfrenta al monstruo Grendel en el gran salón', 'Recibe armas y consejos del rey', 'Vuelve a su tierra con gloria']},
     {'lista': ['El Cid sale desterrado de Castilla', 'Gana batallas con pocos hombres', 'Sus fieles caballeros lo acompañan y lo ayudan', 'Conquista Valencia y recupera su honra']}]),
   ('Viaje del héroe', 'El viaje del héroe es la estructura que siguen muchas epopeyas: el héroe parte, enfrenta pruebas, recibe ayudas y regresa transformado.'),
   'El viaje no es solo un traslado de un lugar a otro: es una transformación. El héroe que vuelve no es el mismo que partió; aprendió algo sobre el mundo o sobre sí mismo. Gilgamesh, por ejemplo, no consigue la inmortalidad, pero regresa aceptando su condición humana.',
   ['Partida: deja su lugar.', 'Pruebas y ayudas en el camino.', 'Regreso: vuelve transformado.']),
 T('Las pruebas: fuerza y astucia',
   m('marcar', rotulo='Prueba', items=[
     {'nombre': 'El cíclope', 'texto': 'Encerrados en la cueva de Polifemo, {{los hombres de Odiseo no pueden mover la roca de la entrada|La fuerza no alcanza.}}. Odiseo {{le dice al gigante que se llama «Nadie»|Astucia: prepara la trampa.}} y, cuando lo deja ciego, {{el cíclope grita que «Nadie» lo ataca y nadie viene a ayudarlo|El engaño funciona.}}.', 'cierre': 'Una prueba que se gana pensando.'},
     {'nombre': 'Las sirenas', 'texto': 'Las sirenas atraen a los marineros con su canto hasta hacerlos naufragar. Odiseo {{tapa con cera los oídos de sus hombres|Astucia: anula el peligro.}} y {{se hace atar al mástil para escucharlas sin poder ir hacia ellas|Resiste la tentación.}}.', 'cierre': 'Una prueba de tentación, no de combate.'}]),
   m('clasificar_x', consigna='¿Qué se necesita para superar cada prueba?', cajas=['Fuerza y valor', 'Astucia'], cuantos=6, items=[
     ['Beowulf lucha cuerpo a cuerpo con el monstruo Grendel', 0], ['Aquiles enfrenta a Héctor frente a las murallas', 0], ['El Cid vence a un ejército más numeroso en el campo de batalla', 0],
     ['Odiseo se hace llamar «Nadie» ante el cíclope', 1], ['Los griegos se esconden en un caballo de madera para entrar en Troya', 1], ['Penélope desteje de noche el manto que teje de día para no elegir esposo', 1]]),
   ('Pruebas del héroe', 'Las pruebas son los obstáculos que el héroe enfrenta en su viaje, como monstruos, combates, tempestades o tentaciones, y que muestran sus virtudes.'),
   'Cada prueba está pensada para poner en juego una virtud. Algunas se ganan con fuerza y valor, como los combates; otras, con astucia, como el engaño al cíclope; y otras, con dominio de sí mismo, como resistir el canto de las sirenas.',
   ['Combates: fuerza y valor.', 'Trampas y engaños: astucia.', 'Tentaciones: dominio de sí mismo.']),
 T('Empezar en medio de la acción',
   m('versiones', rotulo='Comienzo', items=[
     {'nombre': 'Cronológico', 'texto': '{{Termina la guerra de Troya y Odiseo parte hacia su casa.|Empieza por el principio: el lector sigue el orden de los hechos.}}'},
     {'nombre': 'In medias res', 'texto': '{{Hace siete años que Odiseo está atrapado en la isla de la ninfa Calipso, llorando frente al mar.|Empieza en medio de la historia: el lector quiere saber cómo llegó ahí.}}'}]),
   m('elegir_x', consigna='¿Empieza in medias res o en orden cronológico?', items=[
     {'cons': '«La espada todavía goteaba cuando el guerrero levantó la vista: el dragón volvía.»', 'ops': ['In medias res', 'Cronológico'], 'ayuda': 'Arranca en plena acción.'},
     {'cons': '«Había una vez, en un reino lejano, un niño que nació la noche de una tormenta.»', 'ops': ['Cronológico', 'In medias res'], 'ayuda': 'Empieza por el nacimiento.'},
     {'cons': '«Llevaban tres días sitiados y el agua se terminaba. Entonces el capitán recordó cómo había empezado todo.»', 'ops': ['In medias res', 'Cronológico'], 'ayuda': 'Empieza en medio y después vuelve atrás.'}]),
   ('In medias res', 'In medias res es la técnica de comenzar un relato en medio de la acción y recuperar después, con recuerdos o relatos de los personajes, lo que pasó antes.'),
   'La Odisea empieza con Odiseo atrapado en una isla, diez años después de la guerra, y sus aventuras anteriores las cuenta él mismo en un banquete. Este comienzo atrapa al lector desde la primera página, porque lo obliga a preguntarse cómo se llegó hasta ahí.',
   ['Empieza en plena acción.', 'Lo anterior se cuenta después.', 'Genera intriga desde el inicio.'])],
 'recuerda': [
   R('Viaje del héroe', 'es la estructura de partida, pruebas, ayudas y regreso que siguen muchas epopeyas.', 'Odiseo vuelve de Troya a Ítaca'),
   R('Pruebas', 'son los obstáculos del viaje que ponen en juego las virtudes del héroe.', 'El cíclope, las sirenas, Grendel'),
   R('Astucia', 'es la inteligencia para engañar o resolver un problema, que a veces vale más que la fuerza.', 'Me llamo Nadie'),
   R('Transformación del héroe', 'es el cambio que produce el viaje: el héroe vuelve distinto de como partió.', 'Gilgamesh acepta que es mortal'),
   R('In medias res', 'es empezar el relato en medio de la acción y contar después lo anterior.', 'La Odisea empieza con Odiseo atrapado en una isla')]}

L['3'] = {'temas': [
 T('Los dioses intervienen',
   m('marcar', rotulo='Episodio', items=[
     {'nombre': 'Atenea', 'texto': 'Cuando Odiseo llega a Ítaca, {{Atenea lo disfraza de mendigo viejo|Un dios ayuda: le da una ventaja.}} para que {{nadie lo reconozca y pueda descubrir quién le es fiel|La ayuda sirve al plan del héroe.}}.', 'cierre': 'La diosa protege a su héroe favorito.'},
     {'nombre': 'Poseidón', 'texto': '{{Poseidón, furioso porque Odiseo dejó ciego a su hijo|Un dios con pasiones humanas: la venganza.}}, {{levanta una tormenta que destroza la balsa del héroe|El dios es un obstáculo.}}.', 'cierre': 'Los dioses ayudan y también castigan.'}]),
   m('clasificar_x', consigna='¿El dios ayuda u obstaculiza al héroe?', cajas=['Ayuda', 'Obstaculiza'], cuantos=6, items=[
     ['Atenea aconseja a Odiseo en sueños', 0], ['Hermes le da una hierba contra los hechizos de Circe', 0], ['Una diosa del mar le presta un velo que lo salva del naufragio', 0],
     ['Poseidón le manda tempestades', 1], ['El dios del sol castiga a los marineros que comieron sus vacas', 1], ['Una diosa enojada favorece a los enemigos del héroe', 1]]),
   ('Intervención divina', 'La intervención divina es la participación de los dioses en la epopeya, ayudando o castigando a los héroes según sus simpatías y enojos.'),
   'Los dioses de la épica griega no son lejanos ni perfectos: se enojan, tienen favoritos y se pelean entre ellos. Por eso el héroe nunca está solo; su suerte depende también de qué dioses lo apoyan y cuáles lo persiguen.',
   ['Los dioses ayudan o castigan.', 'Tienen pasiones humanas: favoritos y enojos.', 'El héroe actúa, pero no controla todo.']),
 T('El destino',
   m('marcar', rotulo='Destino', items=[
     {'nombre': 'Aquiles', 'texto': '{{Su madre le anuncia que tiene dos destinos posibles|El destino está escrito, pero hay una elección.}}: {{una vida larga y olvidada en su casa|Opción segura.}}, o {{una muerte joven en Troya y gloria eterna|Opción heroica.}}. {{Aquiles elige ir a la guerra|Muestra su grandeza en cómo enfrenta el destino.}}.', 'cierre': 'El héroe elige cómo enfrentar lo que está escrito.'},
     {'nombre': 'Héctor', 'texto': '{{Héctor sabe que Troya va a caer|Conoce su destino.}}, pero {{igual sale a defenderla y se despide de su esposa y de su hijo|Cumple con su deber aunque sabe que va a perder.}}.', 'cierre': 'El héroe no huye de su destino.'}]),
   m('elegir_x', consigna='¿Qué muestra cada decisión sobre el héroe?', items=[
     {'cons': 'Aquiles elige una vida corta y gloriosa en lugar de una larga y tranquila.', 'ops': ['Valora más la gloria que la seguridad', 'Tiene miedo a la guerra', 'No conoce su destino'], 'ayuda': 'Pensá qué eligió y qué dejó.'},
     {'cons': 'Héctor sale a pelear sabiendo que Troya caerá.', 'ops': ['Cumple con su deber aunque no pueda ganar', 'Cree que va a ganar fácilmente', 'Quiere escapar de la ciudad'], 'ayuda': 'Sabe el final y sale igual.'},
     {'cons': 'Gilgamesh, después de buscar la inmortalidad, acepta que va a morir.', 'ops': ['Aprende a aceptar su condición humana', 'Consigue vencer a la muerte', 'Se olvida de su viaje'], 'ayuda': 'El viaje le enseñó algo.'}]),
   ('Destino', 'En la épica, el destino es lo que está decidido para cada personaje y que nadie puede cambiar; la grandeza del héroe está en cómo lo enfrenta.'),
   'Que el destino esté escrito no vuelve pasivo al héroe: al contrario, lo que lo hace grande es que lo enfrenta con valor. Aquiles elige la gloria sabiendo que morirá joven, y Héctor defiende Troya sabiendo que caerá. En esas decisiones se ve qué valoraba su pueblo.',
   ['El destino no se puede cambiar.', 'El héroe elige cómo enfrentarlo.', 'Sus decisiones muestran sus valores.']),
 T('Gloria, honra y lealtad',
   m('marcar', rotulo='Episodio', items=[
     {'nombre': 'El destierro del Cid', 'texto': '{{El rey Alfonso destierra al Cid por intrigas de sus enemigos|Pierde la honra: una injusticia.}}. Aun así, {{después de cada victoria, el Cid le envía al rey parte de lo que gana|Lealtad: sigue sirviendo a su rey.}}, hasta que {{el rey lo perdona y le devuelve su lugar|Recupera la honra.}}.', 'cierre': 'La honra se recupera con hechos.'},
     {'nombre': 'Aquiles y la gloria', 'texto': 'Para los guerreros griegos, {{lo peor no era morir, sino ser olvidado|La gloria vale más que la vida.}}. Por eso {{las hazañas se cantaban: para que la fama del héroe durara para siempre|La epopeya misma es la gloria del héroe.}}.', 'cierre': 'Ser recordado: el gran premio del héroe.'}]),
   m('unir_x', consigna='Uní cada valor con el episodio que lo muestra.', items=[
     {'pares': [['Lealtad', 'El Cid le envía regalos al rey que lo desterró'], ['Gloria', 'Aquiles elige una vida corta pero recordada'], ['Honra', 'El Cid gana batallas para recuperar su buen nombre'], ['Fidelidad', 'Penélope espera veinte años a Odiseo']]}]),
   ('Honra y gloria', 'La honra es la buena fama y el respeto que un héroe tiene ante su comunidad; la gloria es el recuerdo de sus hazañas, que lo hace inmortal en la memoria.'),
   'Para el héroe épico, perder la honra es peor que perder la vida, y ser olvidado es la verdadera muerte. Por eso pelea, se sacrifica y cumple con su palabra. La epopeya, al cantar sus hazañas, es justamente la que le da esa gloria.',
   ['Honra: el respeto de su comunidad.', 'Gloria: ser recordado para siempre.', 'Lealtad: cumplir con su rey y su gente.'])],
 'recuerda': [
   R('Intervención divina', 'es la participación de los dioses en la epopeya, que ayudan o castigan al héroe.', 'Atenea disfraza a Odiseo; Poseidón lo persigue'),
   R('Destino', 'es lo que está decidido para cada personaje y que nadie puede cambiar.', 'Héctor sabe que Troya caerá'),
   R('Elección del héroe', 'consiste en decidir cómo enfrentar el destino, y muestra sus valores.', 'Aquiles elige la gloria'),
   R('Honra', 'es la buena fama y el respeto de la comunidad, que el héroe defiende o recupera.', 'El Cid desterrado gana batallas'),
   R('Gloria', 'es el recuerdo eterno de las hazañas, el gran premio del héroe épico.', 'Las hazañas se cantan para que duren')]}

L['4'] = {'temas': [
 T('La transmisión oral',
   m('marcar', rotulo='Recurso', items=[
     {'nombre': 'Fórmulas', 'texto': 'En la Odisea, cada mañana empieza igual: {{«Cuando apareció la Aurora, de dedos rosados»|Fórmula fija: se repite muchas veces.}}. Y cada vez que habla un héroe, {{«le respondió así el divino Odiseo»|Otra fórmula que ayuda a encadenar el relato.}}.', 'cierre': 'Las fórmulas eran ladrillos que el cantor ya tenía armados.'},
     {'nombre': 'El juglar', 'texto': 'El juglar se dirigía al público: {{«¡Oíd, señores, lo que hizo el Cid!»|Llamado al público: se cantaba frente a gente.}}, y {{repetía los nombres y los epítetos de los héroes|Repeticiones que ayudaban a recordar y a seguir el relato.}}.', 'cierre': 'Huellas de un relato pensado para ser escuchado.'}]),
   m('elegir_x', consigna='¿Para qué servía cada recurso en una epopeya que se cantaba de memoria?', items=[
     {'cons': 'El verso con ritmo regular.', 'ops': ['Ayudaba a memorizar y a cantar el relato', 'Hacía el relato más corto', 'Servía para que solo lo entendieran los reyes'], 'ayuda': 'Pensá en una canción que sabés de memoria.'},
     {'cons': 'Las fórmulas que se repiten, como «la Aurora, de dedos rosados».', 'ops': ['Daban al cantor partes ya armadas para improvisar', 'Mostraban que el autor no tenía ideas', 'Eran errores de copia'], 'ayuda': 'El cantor no tenía el texto escrito.'},
     {'cons': 'Los llamados al público, como «¡Oíd, señores!».', 'ops': ['Mantenían la atención de quienes escuchaban', 'Indicaban el final del libro', 'Servían para cambiar de idioma'], 'ayuda': 'El relato se cantaba frente a gente.'}]),
   ('Transmisión oral', 'La transmisión oral es la forma de conservar un relato contándolo o cantándolo de memoria, de generación en generación, antes de ser escrito.'),
   'Los aedos en Grecia y los juglares en la Edad Media cantaban epopeyas enteras sin leerlas. Para lograrlo usaban el verso, los epítetos, las fórmulas repetidas y los llamados al público. Cuando esas historias por fin se escribieron, esas huellas de la oralidad quedaron en el texto.',
   ['Aedos y juglares cantaban de memoria.', 'Verso, fórmulas y epítetos ayudaban a recordar.', 'Esas marcas quedaron en el texto escrito.']),
 T('El héroe épico y el héroe de hoy',
   m('esquema', items=[{'nombre': 'Dos héroes', 'cols': ['', 'Héroe épico', 'Héroe de relatos actuales'], 'filas': [
       ['¿Cómo es?', 'casi perfecto, de origen noble o divino', 'común, con dudas, miedos y defectos'], ['¿A quién representa?', 'a todo su pueblo', 'muchas veces, solo a sí mismo'],
       ['¿Qué busca?', 'gloria y honra', 'su lugar en el mundo, justicia, a su familia'], ['¿Cómo termina?', 'con fama eterna, aunque muera', 'transformado, no siempre famoso']],
     'cierre': 'El modelo cambia, pero el viaje del héroe sigue.'}]),
   m('clasificar_x', consigna='¿Rasgo del héroe épico o del héroe de relatos actuales?', cajas=['Héroe épico', 'Héroe actual'], cuantos=6, items=[
     ['Es hijo de una diosa y nadie lo vence en combate', 0], ['Pelea para que su nombre sea recordado para siempre', 0], ['Representa el valor de todo su pueblo', 0],
     ['Es una chica común que duda de si podrá lograrlo', 1], ['Se equivoca, pide perdón y aprende de sus errores', 1], ['Busca salvar a su familia más que ganar fama', 1]]),
   ('Héroe actual', 'El héroe de muchos relatos actuales es una persona común, con dudas y defectos, que enfrenta pruebas y se transforma, sin buscar necesariamente la gloria.'),
   'Los valores cambian con las épocas, y los héroes también. Hoy valoramos que un personaje tenga miedo y lo supere, que se equivoque y aprenda. Aun así, muchas historias actuales conservan el esquema épico: un viaje, pruebas, ayudas y un regreso transformado.',
   ['Épico: casi perfecto, busca gloria.', 'Actual: común, con dudas y defectos.', 'El viaje del héroe se mantiene.']),
 T('Huellas de la épica hoy',
   m('marcar', rotulo='Relato actual', items=[
     {'nombre': 'La saga', 'texto': 'En una saga de fantasía, {{un chico huérfano deja la granja de sus tíos|Partida: deja su mundo conocido.}}, {{un viejo sabio le enseña a usar sus poderes|Ayuda: el mentor, como Atenea con Odiseo.}}, {{enfrenta a un villano que amenaza a todos|Prueba: el gran combate.}} y {{vuelve cambiado, más seguro de sí|Regreso transformado.}}.', 'cierre': 'El viaje del héroe, miles de años después.'},
     {'nombre': 'El videojuego', 'texto': 'En muchos videojuegos, {{el personaje sale de su aldea|Partida.}}, {{supera niveles cada vez más difíciles|Pruebas.}}, {{recibe objetos de personajes que lo ayudan|Ayudas.}} y {{enfrenta al jefe final|La gran prueba.}}.', 'cierre': 'La estructura épica también organiza los juegos.'}]),
   m('elegir_x', consigna='¿Qué elemento épico aparece en cada caso?', items=[
     {'cons': 'En una película, una vieja maestra entrena a la protagonista antes de la batalla final.', 'ops': ['La ayuda de un mentor', 'El epíteto', 'La transmisión oral'], 'ayuda': 'Pensá en Atenea y Odiseo.'},
     {'cons': 'Una novela empieza con la heroína escondida en un túnel, y después cuenta cómo llegó ahí.', 'ops': ['El comienzo in medias res', 'La intervención divina', 'El verso'], 'ayuda': 'Empieza en plena acción.'},
     {'cons': 'Al final de una serie, el protagonista vuelve a su pueblo, pero ya no es el mismo.', 'ops': ['El regreso transformado', 'El destierro', 'La fórmula repetida'], 'ayuda': 'La última etapa del viaje.'}]),
   ('Huellas de la épica', 'Las huellas de la épica son los elementos del género, como el viaje del héroe, el mentor o el comienzo in medias res, que siguen apareciendo en relatos actuales.'),
   'Reconocer esas huellas permite leer mejor películas, novelas y videojuegos: cuando aparece un mentor, sabemos que viene una prueba; cuando el héroe parte, esperamos su regreso transformado. La épica no desapareció: cambió de forma y sigue organizando muchas de las historias que nos gustan.',
   ['Viaje del héroe en sagas y videojuegos.', 'El mentor, heredero de los dioses que ayudan.', 'In medias res y regreso transformado.'])],
 'recuerda': [
   R('Transmisión oral', 'es conservar un relato contándolo o cantándolo de memoria, de generación en generación.', 'Aedos y juglares cantaban epopeyas'),
   R('Fórmulas', 'son frases fijas que se repiten en la epopeya y ayudaban al cantor a recordar e improvisar.', '«La Aurora, de dedos rosados»'),
   R('Aedo y juglar', 'son los cantores que recitaban epopeyas: el aedo en Grecia y el juglar en la Edad Media.', '«¡Oíd, señores, lo que hizo el Cid!»'),
   R('Héroe actual', 'es una persona común, con dudas y defectos, que se transforma sin buscar necesariamente la gloria.', 'Una chica que duda y aprende'),
   R('Huellas de la épica', 'son elementos del género que siguen en relatos de hoy, como el viaje del héroe o el mentor.', 'El sabio que entrena al protagonista')]}

# ============================ ACTIVIDADES ============================
A = {
 '1': [
   UNI('Uní cada epopeya con su héroe.', [('Ilíada', 'Aquiles'), ('Odisea', 'Odiseo'), ('Cantar de mio Cid', 'Rodrigo Díaz de Vivar'), ('Beowulf', 'un guerrero que vence a un monstruo')], 'Cada epopeya gira alrededor de un héroe.', 'recordar'),
   CLA('¿Rasgo del héroe épico o no?', ['Rasgo del héroe épico', 'No es un rasgo épico'], [('Tiene un origen noble o divino', 'Rasgo del héroe épico'), ('Representa los valores de su pueblo', 'Rasgo del héroe épico'), ('Resuelve un robo interrogando sospechosos', 'No es un rasgo épico'), ('Es un personaje de una historieta de humor', 'No es un rasgo épico')], 'Repasá qué hace épico a un héroe.', 'aplicar'),
   MC('En «Odiseo, el de muchos recursos», ¿qué función cumple la frase «el de muchos recursos»?', ['Es un epíteto: destaca su ingenio', 'Es el título de la epopeya', 'Es el nombre de su barco'], 'Es un epíteto: destaca su ingenio', 'Frase fija que acompaña el nombre y lo caracteriza.', 'analizar'),
   MC('Un compañero dice que Aquiles no es un héroe porque se enoja y abandona la guerra. ¿Qué le contestás?', ['El héroe épico es extraordinario, pero también humano y con defectos', 'Tiene razón: un héroe nunca se enoja', 'Aquiles no aparece en ninguna epopeya'], 'El héroe épico es extraordinario, pero también humano y con defectos', 'La humanidad del héroe es parte del género.', 'error')],
 '2': [
   ORD('Ordená el viaje de Odiseo.', ['Parte de Troya hacia su casa', 'Enfrenta al cíclope y a las sirenas', 'Recibe la ayuda de Atenea', 'Llega a Ítaca y recupera su hogar'], 'Partida, pruebas, ayudas y regreso.', 'aplicar'),
   CLA('¿Fuerza o astucia?', ['Fuerza y valor', 'Astucia'], [('Beowulf vence a Grendel cuerpo a cuerpo', 'Fuerza y valor'), ('Odiseo se hace llamar «Nadie»', 'Astucia'), ('Aquiles enfrenta a Héctor', 'Fuerza y valor'), ('El caballo de madera para entrar en Troya', 'Astucia')], 'Qué virtud pone en juego cada prueba.', 'analizar'),
   MC('La Odisea empieza con Odiseo atrapado en una isla, años después de la guerra. ¿Qué técnica usa?', ['In medias res', 'Orden cronológico', 'Narrador testigo'], 'In medias res', 'Empieza en medio de la historia y después vuelve atrás.', 'aplicar'),
   MC('¿Por qué Odiseo se hace atar al mástil frente a las sirenas?', ['Para escuchar su canto sin poder ir hacia ellas', 'Para pelear mejor contra ellas', 'Porque sus hombres querían castigarlo'], 'Para escuchar su canto sin poder ir hacia ellas', 'Es una prueba de tentación que supera con astucia.', 'analizar')],
 '3': [
   CLA('¿El dios ayuda u obstaculiza a Odiseo?', ['Ayuda', 'Obstaculiza'], [('Atenea lo disfraza de mendigo', 'Ayuda'), ('Poseidón le manda una tormenta', 'Obstaculiza'), ('Hermes le da una hierba contra hechizos', 'Ayuda'), ('El dios del sol castiga a su tripulación', 'Obstaculiza')], 'Los dioses tienen favoritos y enojos.', 'aplicar'),
   UNI('Uní cada valor con el episodio que lo muestra.', [('Gloria', 'Aquiles elige morir joven pero ser recordado'), ('Honra', 'El Cid gana batallas para recuperar su buen nombre'), ('Lealtad', 'El Cid envía regalos al rey que lo desterró'), ('Deber', 'Héctor defiende Troya sabiendo que caerá')], 'Los valores que mueven al héroe.', 'analizar'),
   MC('Si el destino de Héctor ya estaba escrito, ¿por qué es un héroe?', ['Porque enfrenta su destino con valor en lugar de huir', 'Porque logra cambiar su destino', 'Porque los dioses pelean por él'], 'Porque enfrenta su destino con valor en lugar de huir', 'La grandeza está en cómo se enfrenta lo inevitable.', 'analizar'),
   MC('Lola dice que «honra» y «riqueza» significan lo mismo en el Cantar de mio Cid. ¿Qué le falta entender?', ['Que la honra es la buena fama y el respeto, no el dinero', 'Que la honra es el nombre de un castillo', 'Que en la épica no existe la honra'], 'Que la honra es la buena fama y el respeto, no el dinero', 'El Cid gana riquezas, pero lo que busca es recuperar la honra.', 'error')],
 '4': [
   UNI('Uní cada recurso de la oralidad con su función.', [('Epíteto repetido', 'reconocer enseguida al personaje'), ('Verso con ritmo', 'memorizar y cantar'), ('«¡Oíd, señores!»', 'llamar la atención del público'), ('Fórmula fija', 'tener partes ya armadas para recitar')], 'Recursos de un relato pensado para cantarse.', 'aplicar'),
   CLA('¿Héroe épico o héroe actual?', ['Héroe épico', 'Héroe actual'], [('Hijo de una diosa, invencible en combate', 'Héroe épico'), ('Un chico común que tiene miedo y lo supera', 'Héroe actual'), ('Pelea para que su nombre dure para siempre', 'Héroe épico'), ('Se equivoca, pide perdón y aprende', 'Héroe actual')], 'Compará los dos modelos.', 'analizar'),
   ODD('Tres de estos elementos de una película vienen de la épica y uno no. ¿Cuál no?', ['Un mentor que entrena al protagonista', 'Un viaje lleno de pruebas', 'El regreso del héroe transformado', 'Un detective que interroga sospechosos'], 'Un detective que interroga sospechosos', 'El detective es propio del policial, no de la épica.', 'analizar'),
   KW('Elegí una película, serie, novela o videojuego que conozcas y explicá qué elementos del viaje del héroe tiene.', 'Nombrá la obra y al menos dos etapas: partida, pruebas, ayuda, regreso.', [['parte', 'partida', 'sale', 'deja', 'viaje*'], ['prueba*', 'enfrenta*', 'lucha*', 'pelea*', 'monstruo*', 'villano*', 'nivel*'], ['ayuda*', 'mentor', 'maestr*', 'vuelve', 'regres*', 'cambi*', 'transform*']], 2, 'Por ejemplo: el protagonista deja su pueblo, un maestro lo entrena, enfrenta al villano y vuelve cambiado.', 'aplicar')],
 '5': [
   CLA('¿A qué aspecto de la épica corresponde cada ejemplo?', ['El héroe', 'El viaje', 'Los dioses', 'La oralidad'], [('Aquiles, hijo de una diosa', 'El héroe'), ('Las sirenas y el cíclope', 'El viaje'), ('Poseidón persigue a Odiseo', 'Los dioses'), ('«La Aurora, de dedos rosados» se repite', 'La oralidad')], 'Repasá los cuatro niveles.', 'analizar'),
   ORD('Ordená la historia de Gilgamesh.', ['Pierde a su amigo Enkidu y teme a la muerte', 'Parte a buscar la inmortalidad', 'Consigue una planta mágica, pero una serpiente se la roba', 'Vuelve a su ciudad y acepta ser mortal'], 'El viaje transforma al héroe.', 'aplicar'),
   MS('En el Cantar de mio Cid, el héroe desterrado gana batallas y sigue enviando regalos al rey. Elegí los DOS valores que muestra.', ['Lealtad', 'Búsqueda de honra', 'Cobardía', 'Deseo de venganza contra el rey'], ['Lealtad', 'Búsqueda de honra'], 'Cumple con su rey y quiere recuperar su buen nombre.'),
   MC('¿Por qué las epopeyas antiguas tienen tantas repeticiones?', ['Porque se cantaban de memoria y las repeticiones ayudaban a recordar', 'Porque los autores escribían apurados', 'Porque estaban pensadas para leerse en silencio'], 'Porque se cantaban de memoria y las repeticiones ayudaban a recordar', 'Son huellas de la transmisión oral.', 'analizar')],
}

EX = [
 [1, MC('¿Qué es la épica?', ['El género que narra las hazañas de un héroe que representa a un pueblo', 'El género que cuenta crímenes y su investigación', 'El género que se burla de otros textos'], 'El género que narra las hazañas de un héroe que representa a un pueblo', 'Héroe, hazañas y pueblo.', 'recordar')],
 [1, UNI('Uní cada héroe con su virtud principal.', [('Aquiles', 'la fuerza'), ('Odiseo', 'la astucia'), ('El Cid', 'la lealtad')], 'Cada epopeya destaca una virtud.', 'recordar')],
 [1, SA('En «Aquiles, el de los pies ligeros», ¿cómo se llama la frase «el de los pies ligeros»?', ['epíteto', 'epiteto', 'un epíteto', 'epíteto épico'], 'Frase fija que destaca el rasgo principal.', 'aplicar')],
 [2, ORD('Ordená las etapas del viaje del héroe.', ['Partida', 'Pruebas', 'Ayudas', 'Regreso'], 'La estructura de muchas epopeyas.', 'recordar')],
 [2, CLA('¿Fuerza o astucia?', ['Fuerza', 'Astucia'], [('Beowulf lucha con Grendel', 'Fuerza'), ('El caballo de Troya', 'Astucia'), ('Odiseo se llama «Nadie»', 'Astucia')], 'Qué virtud gana cada prueba.', 'aplicar')],
 [2, MC('Un relato empieza: «La flecha ya volaba hacia el rey cuando el guardia saltó». ¿Qué técnica usa?', ['In medias res', 'Orden cronológico', 'Epíteto'], 'In medias res', 'Empieza en plena acción.', 'aplicar')],
 [3, CLA('¿El dios ayuda u obstaculiza?', ['Ayuda', 'Obstaculiza'], [('Atenea aconseja a Odiseo', 'Ayuda'), ('Poseidón le manda tormentas', 'Obstaculiza'), ('Hermes le da una hierba protectora', 'Ayuda')], 'Los dioses toman partido.', 'aplicar')],
 [3, MC('Aquiles elige una vida corta y gloriosa. ¿Qué valor muestra esa elección?', ['Valora la gloria más que la seguridad', 'Tiene miedo a la guerra', 'Quiere ser rico'], 'Valora la gloria más que la seguridad', 'Ser recordado era el gran premio del héroe.', 'analizar')],
 [3, TF('Para el héroe épico, la honra es la buena fama y el respeto de su comunidad.', 'Verdadero', 'Perder la honra era peor que perder la vida.', 'recordar')],
 [4, MC('¿Por qué la épica usa verso, epítetos y fórmulas repetidas?', ['Porque se transmitía de memoria y eso ayudaba a recordar', 'Porque así se ahorraba papel', 'Porque era un texto para leer en silencio'], 'Porque se transmitía de memoria y eso ayudaba a recordar', 'Huellas de la transmisión oral.', 'analizar')],
 [4, CLA('¿Héroe épico o héroe actual?', ['Héroe épico', 'Héroe actual'], [('Busca la gloria eterna', 'Héroe épico'), ('Tiene dudas y miedos que supera', 'Héroe actual'), ('Representa a todo su pueblo', 'Héroe épico'), ('Es una persona común', 'Héroe actual')], 'Dos modelos de héroe.', 'analizar')],
 [4, ODD('Tres elementos vienen de la épica y uno no. ¿Cuál no?', ['El mentor que ayuda al héroe', 'El viaje con pruebas', 'El comienzo in medias res', 'La revelación del culpable'], 'La revelación del culpable', 'La revelación es propia del policial.', 'analizar')],
 [4, KW('Explicá con tus palabras qué es el viaje del héroe y por qué decimos que sigue presente en relatos de hoy.', 'Nombrá las etapas y un ejemplo actual.', [['parti*', 'sale', 'deja'], ['prueba*', 'obstáculo*', 'enfrenta*', 'peligro*'], ['regres*', 'vuelve', 'transform*', 'cambi*'], ['película*', 'serie*', 'novela*', 'videojuego*', 'saga*', 'hoy', 'actual*']], 3, 'Por ejemplo: el héroe parte, enfrenta pruebas, recibe ayuda y vuelve transformado; muchas sagas y videojuegos siguen ese esquema.', 'aplicar')],
]

CARP = {
 '1': [
  ('Un poema antiguo cuenta cómo un guerrero defiende a su pueblo de un monstruo que ataca de noche. ¿A qué género pertenece?', 'aplicar', ['épica', 'epica', 'la épica', 'género épico', 'epopeya'], 'A la épica: hazañas de un héroe que defiende a su pueblo.'),
  ('En «Héctor, el domador de caballos», ¿cómo se llama la frase que acompaña al nombre?', 'aplicar', ['epíteto', 'epiteto', 'un epíteto'], 'Epíteto: frase fija que destaca un rasgo del héroe.'),
  ('Odiseo no es el más fuerte de los griegos, pero idea el caballo de madera para entrar en Troya. ¿Qué virtud muestra?', 'analizar', ['astucia', 'la astucia', 'ingenio', 'inteligencia'], 'La astucia: gana con inteligencia, no con fuerza.'),
  ('Tomi dice que Aquiles no puede ser un héroe porque se enoja y llora. ¿Qué tiene el héroe épico además de virtudes extraordinarias?', 'error', ['defectos humanos', 'es humano', 'humanidad', 'defectos'], 'Es humano: tiene defectos, sufre y puede morir.'),
 ],
 '2': [
  ('Un héroe deja su tierra, enfrenta monstruos, recibe ayuda de un sabio y vuelve cambiado. ¿Cómo se llama esa estructura?', 'aplicar', ['viaje del héroe', 'el viaje del héroe'], 'El viaje del héroe: partida, pruebas, ayudas y regreso.'),
  ('Encerrado con un cíclope, Odiseo dice que se llama «Nadie» y así logra escapar. ¿Con qué virtud supera la prueba?', 'analizar', ['astucia', 'la astucia', 'ingenio'], 'Con astucia: cuando el cíclope grita, nadie lo ayuda.'),
  ('La Odisea empieza con el héroe atrapado en una isla, muchos años después de la guerra. ¿Qué técnica de comienzo usa?', 'aplicar', ['in medias res'], 'In medias res: empieza en medio de la historia.'),
  ('Juli dice que el viaje del héroe es solo ir de un lugar a otro. ¿Qué le pasa además al héroe cuando regresa?', 'error', ['se transforma', 'cambia', 'vuelve cambiado', 'transformado'], 'Se transforma: vuelve distinto de como partió.'),
 ],
 '3': [
  ('En la Odisea, Poseidón persigue a Odiseo con tormentas porque dejó ciego a su hijo. ¿El dios lo ayuda o lo obstaculiza?', 'aplicar', ['lo obstaculiza', 'obstaculiza'], 'Lo obstaculiza: los dioses también castigan.'),
  ('Aquiles sabe que si va a la guerra morirá joven, pero será recordado para siempre, y va igual. ¿Qué busca?', 'analizar', ['la gloria', 'gloria', 'fama'], 'La gloria: ser recordado por sus hazañas.'),
  ('Desterrado injustamente, el Cid gana batallas y le envía regalos a su rey. ¿Qué valor muestra con los regalos?', 'analizar', ['lealtad', 'la lealtad'], 'Lealtad: sigue sirviendo al rey que lo echó.'),
  ('Lucas cree que, como el destino de Héctor estaba escrito, Héctor no tiene mérito. ¿Qué elige el héroe frente a su destino?', 'error', ['cómo enfrentarlo', 'como enfrentarlo', 'enfrentarlo con valor'], 'Cómo enfrentarlo: Héctor defiende Troya aunque sabe que caerá.'),
 ],
 '4': [
  ('En Grecia, las epopeyas las cantaban de memoria unos poetas que recorrían pueblos y palacios. ¿Cómo se llamaban?', 'recordar', ['aedos', 'los aedos', 'aedo'], 'Aedos: en la Edad Media, juglares.'),
  ('En la Odisea, cada amanecer se nombra igual: «la Aurora, de dedos rosados». ¿Para qué servían esas repeticiones?', 'analizar', ['para recordar', 'recordar', 'memorizar', 'ayudar a recordar'], 'Para recordar: el relato se cantaba de memoria.'),
  ('En una película, un viejo maestro entrena a la protagonista antes de la batalla final. ¿Qué elemento épico es?', 'aplicar', ['el mentor', 'mentor', 'la ayuda', 'ayuda'], 'El mentor: la ayuda que recibe el héroe, como Atenea con Odiseo.'),
  ('Sofi dice que el héroe de hoy es igual al épico. ¿Qué tiene el héroe actual que el épico casi no muestra?', 'error', ['dudas y miedos', 'dudas', 'miedos', 'defectos'], 'Dudas, miedos y defectos: es una persona común.'),
 ],
}

def ajustes(M):
    M['act'] = A
    M['examen'] = EX
    M['practica'] = 'Actividades generales'
    M['examen_titulo'] = 'Nivel jefe: la épica'
    M['actualizar_preguntas'] = True
    for k, items in CARP.items():
        N = M['niveles'].setdefault(k, {})
        N['carpeta'] = [c for c, _, _, _ in items]; N['carpeta_nivel'] = [t for _, t, _, _ in items]
        N['respuestas_carpeta'] = [r for _, _, r, _ in items]; N.setdefault('soluciones', {})['carpeta'] = [s for _, _, _, s in items]

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-9/mision-9.json', L, ajustes=ajustes)
