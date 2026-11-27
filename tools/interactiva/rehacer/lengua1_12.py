# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 12 · El verbo: tiempos y modos del indicativo (TODO nuevo: clases, lección, actividades, examen y carpeta)
# Las clases van en los slugs leng1-m3-n1..4 porque son los que apuntan a los pasos de video de esta misión.
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD
RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', '..')

# ============================ CLASES ANIMADAS ============================
STEP = {'1': '73870d75-773f-4a42-a65a-c28b296d5281', '2': 'c3a38f12-93bb-45de-8f7e-89956607b7b8', '3': 'b2bdf1f6-5fa4-49cb-8e22-a7b819bd22f1', '4': '4254c521-afcf-4d4d-8125-959ea313785a'}
TIT = {'1': 'Raíz y desinencia', '2': 'Tiempos simples del indicativo', '3': 'Tiempos compuestos', '4': 'Los pretéritos en el relato'}
CL = {}
CL['1'] = [
 {'t': 'reto', 'texto': 'Sin ver el resto de la palabra: ¿quién hace la acción y cuándo? «…ábamos»', 'segundos': 7, 'respuesta': 'Nosotros, en el pasado', 'emoji': '🔎', 'titulo': 'RAÍZ Y DESINENCIA', 'sub': 'las dos partes del verbo',
  'voz': ['Reto: te muestro solo el final de un verbo, «ábamos». ¿Quién hace la acción y cuándo?', 'Siete segundos.', 'Nosotros, en el pasado: caminábamos, saltábamos, mirábamos. La terminación sola ya lo dice. Hoy vemos las dos partes del verbo: la *raíz* y la *desinencia*.']},
 {'t': 'definicion', 'palabra': 'Raíz y desinencia', 'texto': 'La raíz guarda el significado del verbo; la desinencia es la terminación que indica persona, número y tiempo.', 'emoji': '🌱',
  'voz': ['Todo verbo conjugado tiene dos partes. La *raíz* guarda el significado: en caminábamos, «camin» nos dice que se trata de caminar.', 'La *desinencia* es la terminación que cambia: indica quién hace la acción, si es uno o son varios, y cuándo ocurre.']},
 {'t': 'transforma', 'titulo': 'SEPARAMOS UN VERBO', 'pasos': [{'txt': 'caminábamos'}, {'txt': 'camin + ábamos', 'nota': 'raíz + desinencia'}, {'txt': 'camin = caminar', 'nota': 'el significado'}, {'txt': 'ábamos = nosotros, pasado', 'nota': 'la información'}],
  'voz': ['Hagamos el análisis paso a paso con la forma caminábamos.', 'Primero buscamos la raíz: sacamos la terminación ar del infinitivo, caminar, y nos queda «camin». Lo que sigue, «ábamos», es la desinencia.', 'La raíz aporta el significado: la acción de caminar.', 'Y la desinencia aporta la información: primera persona del plural, nosotros, en tiempo pasado.']},
 {'t': 'tabla', 'titulo': 'TRES CONJUGACIONES', 'columnas': ['Infinitivo', 'Conjugación', 'Ejemplos'], 'filas': [['-ar', 'primera', 'cantar, saltar'], ['-er', 'segunda', 'comer, temer'], ['-ir', 'tercera', 'vivir, partir']],
  'voz': ['El infinitivo es el nombre del verbo, como aparece en el diccionario. Según cómo termina, el verbo pertenece a una de tres conjugaciones.', 'Los que terminan en ar forman la primera conjugación: cantar, saltar.', 'Los que terminan en er, la segunda: comer, temer.', 'Y los que terminan en ir, la tercera: vivir, partir. Cada conjugación tiene sus propias desinencias.']},
 {'t': 'texto', 'oracion': 'Nosotros caminábamos y ellos corrían por la plaza.', 'marcas': [{'desde': 1, 'hasta': 1, 'etiqueta': '1.ª PLURAL'}, {'desde': 4, 'hasta': 4, 'etiqueta': '3.ª PLURAL'}],
  'voz': ['La desinencia también dice la *persona* y el *número*. Mirá esta oración.', '*Caminábamos*: primera persona, la de quien habla, en plural.', '*Corrían*: tercera persona, la de quienes no participan de la conversación, también en plural. Por eso, muchas veces, ni hace falta nombrar el sujeto.']},
 {'t': 'versus', 'a': {'txt': 'Regular', 'emoji': '🧱', 'datos': ['la raíz no cambia', 'cant-o, cant-é, cant-aré']}, 'b': {'txt': 'Irregular', 'emoji': '🔀', 'datos': ['la raíz cambia', 'pued-o, pud-e, podr-é']}, 'gana': 'empate', 'veredicto': 'Mirá la raíz',
  'voz': ['Ahora, dos clases de verbos.', 'Los *regulares* mantienen la raíz en todas sus formas: cant-o, cant-é, cant-aré.', 'Los *irregulares* la cambian: el verbo poder dice pued-o, pud-e, podr-é.', 'Para saber de qué tipo es un verbo, conjugalo en presente, pasado y futuro y mirá si la raíz se mantiene.']},
 {'t': 'quiz4', 'pregunta': '«Tuvimos» es una forma de un verbo irregular. ¿Cuál es su infinitivo?', 'opciones': ['tener', 'tuver', 'tuvir', 'tomar'], 'correcta': 0,
  'voz': ['Pregunta: tuvimos es una forma de un verbo irregular. ¿Cuál es su infinitivo?', 'Pensá cómo diría la oración en presente: yo…', '*Tener*. La raíz cambia de ten a tuv, y por eso cuesta reconocerlo. Tuver o tuvir no existen.']},
 {'t': 'bloques', 'titulo': 'FORMAS NO PERSONALES', 'items': [{'cab': 'Infinitivo', 'txt': 'saltar, temer, vivir'}, {'cab': 'Gerundio', 'txt': 'saltando, viviendo'}, {'cab': 'Participio', 'txt': 'saltado, vivido'}],
  'voz': ['Hay tres formas del verbo que no tienen persona ni tiempo: las *formas no personales*.', 'El *infinitivo*, terminado en ar, er o ir: es el nombre del verbo.', 'El *gerundio*, terminado en ando o iendo: muestra una acción en curso.', 'Y el *participio*, terminado en ado o ido: lo vamos a necesitar para armar los tiempos compuestos.']},
 {'t': 'errores', 'items': [{'mal': '«Corriendo» dice quién corre', 'bien': 'El gerundio no tiene persona'}, {'mal': 'La raíz es lo que cambia', 'bien': 'Cambia la desinencia'}],
  'voz': ['Dos confusiones frecuentes.', 'Creer que corriendo dice quién corre: el gerundio no indica persona; puede ser yo, vos o ellos.', 'Y creer que la raíz es la parte que cambia: lo que cambia es la desinencia. En los irregulares también cambia la raíz, y por eso se llaman así.']},
 {'t': 'resumen', 'items': [['Raíz', 'guarda el significado'], ['Desinencia', 'persona, número y tiempo'], ['Regular e irregular', 'según cambie o no la raíz'], ['No personales', 'infinitivo, gerundio, participio']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 1'},
  'voz': ['Repasemos.', 'Cada forma verbal se puede desarmar en dos partes.', 'La raíz guarda el significado.', 'La desinencia dice persona, número y tiempo.', 'Los regulares no cambian la raíz; los irregulares sí.', 'Y las formas no personales son el infinitivo, el gerundio y el participio. ¡A practicar!']},
]
CL['2'] = [
 {'t': 'chat', 'contacto': {'nombre': 'Tomás', 'emoji': '🧑'}, 'mensajes': [{'yo': False, 'txt': '¿Venís al partido?'}, {'yo': True, 'txt': 'Ayer jugué, hoy descanso, el sábado iré seguro'}], 'titulo': 'TIEMPOS SIMPLES', 'sub': 'del modo indicativo',
  'voz': ['Tomás pregunta si venís al partido.', 'La respuesta usa tres tiempos en una sola línea: ayer jugué, hoy descanso, el sábado iré.', 'Pasado, presente y futuro. Hoy vemos los *tiempos simples* del modo indicativo: el modo de los hechos que se presentan como reales.']},
 {'t': 'definicion', 'palabra': 'Tiempo verbal', 'texto': 'Forma del verbo que ubica la acción en el presente, el pasado o el futuro respecto del momento en que se habla.', 'emoji': '⏱️',
  'voz': ['El *tiempo verbal* ubica la acción respecto del momento en que hablamos: antes, ahora o después.', 'Los tiempos *simples* son los que se arman con una sola palabra, como canto, canté o cantaré.']},
 {'t': 'linea', 'titulo': 'CINCO TIEMPOS SIMPLES', 'eventos': [{'fecha': 'Antes', 'txt': 'canté / cantaba', 'emoji': '⏪'}, {'fecha': 'Ahora', 'txt': 'canto', 'emoji': '🎤'}, {'fecha': 'Después', 'txt': 'cantaré', 'emoji': '⏩'}, {'fecha': 'Si…', 'txt': 'cantaría', 'emoji': '🤔'}],
  'voz': ['En el pasado hay dos tiempos: el pretérito perfecto simple, canté, y el pretérito imperfecto, cantaba.', 'En el momento en que hablamos, el presente: canto.', 'Lo que todavía no pasó, el futuro: cantaré.', 'Y lo que pasaría si se cumpliera una condición, el condicional: cantaría. Cinco tiempos simples en total.']},
 {'t': 'tabla', 'titulo': 'YO, CON EL VERBO COMER', 'columnas': ['Tiempo', 'Forma'], 'filas': [['Presente', 'como'], ['Perfecto simple', 'comí'], ['Imperfecto', 'comía'], ['Futuro', 'comeré'], ['Condicional', 'comería']],
  'voz': ['Veamos los cinco tiempos con el verbo comer, en primera persona.', 'Presente: como.', 'Pretérito perfecto simple: comí.', 'Pretérito imperfecto: comía.', 'Futuro: comeré.', 'Condicional: comería. Fijate el truco del futuro y el condicional: se arman agregando la terminación al infinitivo entero: comer, más é; comer, más ía.']},
 {'t': 'comparar', 'a': {'cab': 'Perfecto simple', 'texto': 'una acción terminada: llovió', 'emoji': '⚡'}, 'b': {'cab': 'Imperfecto', 'texto': 'algo que duraba: llovía', 'emoji': '🌧️'}, 'signo': '≠',
  'voz': ['Los dos pretéritos no son intercambiables.', 'El *perfecto simple* cuenta una acción terminada, que pasó de una vez: anoche llovió.', 'El *imperfecto* muestra algo que duraba o se repetía: llovía toda la noche. Lo vamos a usar mucho al narrar.']},
 {'t': 'pizarra', 'titulo': 'USOS DEL PRESENTE', 'lineas': [{'txt': 'Ahora: leo el diario', 'color': 'azul'}, {'txt': 'Siempre: el agua hierve', 'color': 'verde'}, {'txt': 'Historia: en 1816 declaran', 'color': 'sol', 'marca': 'subraya'}],
  'voz': ['El presente no sirve solo para lo que pasa ahora: leo el diario.', 'También dice lo que siempre es verdad o se repite: el agua hierve a cien grados.', 'Y puede contar hechos pasados para acercarlos al lector: en 1816 los diputados declaran la independencia. Es el *presente histórico*.']},
 {'t': 'prediccion', 'pregunta': '«Si tuviera tiempo, ___ más libros.» ¿Qué forma va?', 'a': {'txt': 'leería', 'emoji': '📖'}, 'b': {'txt': 'leeré', 'emoji': '📅'}, 'correcta': 'a', 'resultado': 'Depende de una condición: condicional.',
  'voz': ['¿Qué creés? Si tuviera tiempo, ¿leería o leeré más libros?', 'Pensá si es seguro o si depende de algo.', '*Leería*: la acción depende de una condición que no se cumple, tener tiempo. Ese es el trabajo del condicional.']},
 {'t': 'vof', 'afirmacion': 'Futuro y condicional se arman sobre el infinitivo.', 'emoji': '🧩', 'verdadero': True, 'explicacion': 'vivir + é = viviré · vivir + ía = viviría',
  'voz': ['Verdadero o falso: el futuro y el condicional se pueden formar agregando una terminación al infinitivo entero.', 'Probá con vivir.', 'Verdadero: vivir más é, viviré; vivir más ía, viviría. En los otros tiempos, en cambio, se parte de la raíz.']},
 {'t': 'errores', 'items': [{'mal': 'Vos cantastes', 'bien': 'Vos cantaste'}, {'mal': 'Si podría, iría', 'bien': 'Si pudiera, iría'}],
  'voz': ['Dos errores muy comunes.', 'Agregar una ese al perfecto simple: no es cantastes, es cantaste.', 'Y poner condicional después de «si»: no se dice si podría, iría, sino si pudiera, iría. El condicional va en la otra parte de la oración.']},
 {'t': 'resumen', 'items': [['Presente', 'ahora, siempre, histórico'], ['Perfecto simple', 'acción terminada'], ['Imperfecto', 'lo que duraba o se repetía'], ['Futuro y condicional', 'lo que pasará o pasaría']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 2'},
  'voz': ['Repasemos.', 'El indicativo tiene cinco tiempos simples.', 'El presente y sus usos.', 'El perfecto simple, para lo terminado.', 'El imperfecto, para lo que duraba.', 'Y el futuro y el condicional, que se arman sobre el infinitivo. ¡A practicar!']},
]
CL['3'] = [
 {'t': 'noticia', 'cinta': 'ÚLTIMO MOMENTO', 'titular': 'Llegaron los bomberos, pero el fuego ya se había apagado', 'bajada': 'Un vecino lo había controlado con un matafuegos', 'emoji': '🚒', 'titulo': 'TIEMPOS COMPUESTOS', 'sub': 'haber + participio',
  'voz': ['Último momento: cuando llegaron los bomberos, el fuego ya se había apagado.', 'Un vecino lo había controlado con un matafuegos.', 'Fijate en «se había apagado»: son dos palabras y cuentan algo que pasó antes de otro hecho. Hoy vemos los *tiempos compuestos*.']},
 {'t': 'definicion', 'palabra': 'Tiempo compuesto', 'texto': 'Tiempo verbal formado por el auxiliar haber conjugado más el participio del verbo principal.', 'emoji': '🧩',
  'voz': ['Un *tiempo compuesto* se arma con dos palabras: el verbo *haber* conjugado y el *participio* del verbo que lleva el significado.', 'Haber se encarga de la persona, el número y el tiempo; el participio no cambia nunca.']},
 {'t': 'pasos', 'titulo': 'CÓMO SE ARMA', 'items': [{'txt': 'Elegí el tiempo de haber: había', 'emoji': '1️⃣'}, {'txt': 'Sumá el participio: cantado', 'emoji': '2️⃣'}, {'txt': 'Listo: había cantado', 'emoji': '✅'}],
  'voz': ['Armemos uno paso a paso.', 'Primero conjugamos haber en el tiempo y la persona que necesitamos: yo había.', 'Después sumamos el participio del verbo principal, terminado en ado o ido: cantado.', 'Resultado: había cantado. Si cambiamos la persona, cambia solo haber: habíamos cantado.']},
 {'t': 'tabla', 'titulo': 'CADA SIMPLE, SU COMPUESTO', 'columnas': ['Simple', 'Compuesto'], 'filas': [['canto', 'he cantado'], ['cantaba', 'había cantado'], ['cantaré', 'habré cantado'], ['cantaría', 'habría cantado']],
  'voz': ['Cada tiempo simple tiene su compuesto, y el nombre sale del tiempo en que está haber.', 'Haber en presente, he cantado: pretérito perfecto compuesto.', 'Haber en imperfecto, había cantado: pretérito pluscuamperfecto.', 'Haber en futuro, habré cantado: futuro perfecto.', 'Y haber en condicional, habría cantado: condicional perfecto.']},
 {'t': 'orden', 'titulo': 'ASÍ PASÓ / ASÍ SE CUENTA', 'items': [{'txt': 'Apagan el fuego', 'emoji': '🧯'}, {'txt': 'Llegan los bomberos', 'emoji': '🚒'}, {'txt': 'Todo está apagado', 'emoji': '✅'}], 'relato': [1, 2, 0],
  'voz': ['Mirá el orden real de los hechos: primero un vecino apaga el fuego, después llegan los bomberos y encuentran todo apagado.', 'Pero la noticia empieza contando la llegada de los bomberos.', 'Lo que pasó antes aparece al final, con el pluscuamperfecto: el fuego se había apagado. Los compuestos marcan *anterioridad*.']},
 {'t': 'unir', 'titulo': 'PARTICIPIOS IRREGULARES', 'pares': [['escribir', 'escrito'], ['romper', 'roto'], ['volver', 'vuelto'], ['decir', 'dicho'], ['hacer', 'hecho']],
  'voz': ['Algunos participios no terminan en ado ni en ido. Hay que aprenderlos.', 'Escribir: escrito.', 'Romper: roto, nunca rompido.', 'Volver: vuelto.', 'Decir: dicho.', 'Y hacer: hecho, con hache.']},
 {'t': 'pistas', 'problema': '¿Cómo se llama el tiempo de «habremos terminado»?', 'pistas': ['Tiene haber + participio: es compuesto', '«Habremos» es haber en futuro'], 'respuesta': 'Futuro perfecto',
  'voz': ['Un problema con pistas: ¿cómo se llama el tiempo de habremos terminado?', 'Primera pista: tiene haber más un participio, así que es un tiempo compuesto.', 'Segunda pista: habremos es el verbo haber en futuro, como cantaremos.', 'Respuesta: *futuro perfecto*. Cuenta algo que va a estar terminado antes de un momento futuro: para el viernes, habremos terminado.']},
 {'t': 'quiz4', 'pregunta': '¿Cuál está bien escrita?', 'opciones': ['Había roto el vaso', 'Había rompido el vaso', 'Hube rompí el vaso'], 'correcta': 0,
  'voz': ['Pregunta: ¿cuál de estas oraciones está bien escrita?', 'Acordate de los participios irregulares.', '*Había roto el vaso*. Rompido no existe, y con haber siempre va el participio, no una forma conjugada.']},
 {'t': 'errores', 'items': [{'mal': 'Ha rompido', 'bien': 'Ha roto'}, {'mal': 'Había ya llegado', 'bien': 'Ya había llegado'}],
  'voz': ['Dos errores para evitar.', 'Usar participios regulares inventados: no es ha rompido, es ha roto.', 'Y meter palabras entre haber y el participio: no conviene decir había ya llegado; lo natural es ya había llegado. Las dos piezas del compuesto van juntas.']},
 {'t': 'resumen', 'items': [['Tiempo compuesto', 'haber + participio'], ['Haber', 'lleva persona y tiempo'], ['Pluscuamperfecto', 'había + participio: lo anterior'], ['Irregulares', 'roto, escrito, vuelto, dicho']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 3'},
  'voz': ['Repasemos.', 'Los tiempos compuestos cuentan lo que ya estaba terminado.', 'Se arman con haber y el participio.', 'Haber es el que cambia.', 'El pluscuamperfecto cuenta lo anterior a otro pasado.', 'Y hay participios irregulares que conviene saber de memoria. ¡A practicar!']},
]
CL['4'] = [
 {'t': 'historia', 'personaje': {'nombre': 'La narradora', 'emoji': '👩'}, 'lugar': '🌧️', 'lineas': ['Era tarde y llovía sin parar.', 'De pronto, alguien golpeó la puerta.'], 'titulo': 'LOS PRETÉRITOS', 'sub': 'en el relato',
  'voz': ['Escuchá cómo empieza este relato: era tarde y llovía sin parar.', 'De pronto, alguien golpeó la puerta.', 'Dos oraciones, dos pretéritos distintos, y cada uno cumple una tarea. Hoy vemos cómo se usan los *pretéritos al narrar*.']},
 {'t': 'texto', 'oracion': 'Era tarde y llovía cuando alguien golpeó la puerta.', 'marcas': [{'desde': 0, 'hasta': 0, 'etiqueta': 'FONDO'}, {'desde': 3, 'hasta': 3, 'etiqueta': 'FONDO'}, {'desde': 6, 'hasta': 6, 'etiqueta': 'ACCIÓN'}],
  'voz': ['Analicemos la oración verbo por verbo.', '*Era*: imperfecto. Describe el momento, arma el escenario.', '*Llovía*: imperfecto. Algo que duraba mientras pasaban las otras cosas.', '*Golpeó*: perfecto simple. Una acción que pasa de una vez e interrumpe la escena: la historia avanza.']},
 {'t': 'consejo', 'titulo': 'Preguntá: ¿duraba o pasó?', 'texto': 'Si duraba o se repetía, imperfecto. Si pasó de una vez y terminó, perfecto simple.', 'emoji': '💡',
  'voz': ['Un truco para elegir: preguntate si la acción duraba o si pasó de una vez. Si duraba, se repetía o describe, va en imperfecto; si ocurrió y terminó, va en perfecto simple.']},
 {'t': 'matriz', 'titulo': 'QUÉ TIEMPO USAR', 'celdas': [{'cab': 'Perfecto simple', 'txt': 'acciones que avanzan'}, {'cab': 'Imperfecto', 'txt': 'fondo y costumbres'}, {'cab': 'Pluscuamperfecto', 'txt': 'lo que pasó antes'}, {'cab': 'Presente histórico', 'txt': 'acerca lo pasado'}],
  'voz': ['Cada tiempo tiene su trabajo en un relato.', 'El *perfecto simple* cuenta las acciones que hacen avanzar la historia.', 'El *imperfecto* describe el fondo y las costumbres: todos los veranos, el abuelo preparaba dulce.', 'El *pluscuamperfecto* vuelve atrás: cuenta lo que había pasado antes.', 'Y el *presente histórico* cuenta hechos pasados como si ocurrieran ahora, para acercarlos al lector.']},
 {'t': 'flujo', 'titulo': 'UN RELATO, TRES PRETÉRITOS', 'items': ['La casa estaba vacía', 'Ana abrió la puerta', 'Alguien había entrado antes'],
  'voz': ['Mirá cómo trabajan juntos en un relato breve. Primero, el fondo en imperfecto: la casa estaba vacía.', 'Después, la acción en perfecto simple: Ana abrió la puerta.', 'Y al final, lo anterior en pluscuamperfecto: alguien había entrado antes. Con tres tiempos el lector entiende la escena, lo que pasa y lo que ya había pasado.']},
 {'t': 'prediccion', 'pregunta': '«Todos los veranos, el abuelo ___ dulce de higos.»', 'a': {'txt': 'preparaba', 'emoji': '🔁'}, 'b': {'txt': 'preparó', 'emoji': '1️⃣'}, 'correcta': 'a', 'resultado': 'Una costumbre que se repetía: imperfecto.',
  'voz': ['¿Qué creés? Todos los veranos, el abuelo ¿preparaba o preparó dulce de higos?', 'Mirá la expresión «todos los veranos».', '*Preparaba*: es una costumbre que se repetía. Si dijéramos «un verano, el frasco explotó», ahí sí iría el perfecto simple.']},
 {'t': 'corrige', 'titulo': 'CORREGIMOS UN RELATO', 'cambios': [{'antes': 'Entró y ve la carta', 'despues': 'Entró y vio la carta', 'motivo': 'no saltar al presente'}, {'antes': 'Mientras leí, sonó', 'despues': 'Mientras leía, sonó', 'motivo': 'lo que dura: imperfecto'}],
  'voz': ['Corrijamos dos errores típicos de un relato.', 'Entró y ve la carta: el relato salta al presente sin motivo. Se corrige con el pasado: entró y vio la carta.', 'Mientras leí, sonó el timbre: leer duraba de fondo, así que va en imperfecto. Mientras leía, sonó el timbre.']},
 {'t': 'causas', 'causa': {'txt': 'Mezclar tiempos sin motivo', 'emoji': '🌀'}, 'items': ['el lector se pierde', 'no se sabe qué pasó antes', 'la historia pierde fuerza'],
  'voz': ['¿Qué pasa cuando un relato mezcla tiempos sin motivo?', 'El lector se pierde: no sabe si la historia ocurre ahora o ya ocurrió.', 'Tampoco queda claro qué pasó antes y qué después.', 'Y la historia pierde fuerza. Por eso, al revisar un texto, conviene hacer una pasada solo para mirar los verbos.']},
 {'t': 'quiz4', 'pregunta': '«Cuando llegué a la estación, el tren ya ___.»', 'opciones': ['había salido', 'salía', 'sale', 'saldrá'], 'correcta': 0,
  'voz': ['Pregunta final: cuando llegué a la estación, el tren ya… ¿qué?', 'Pensá qué pasó primero.', '*Había salido*: el tren salió antes de que yo llegara, y eso lo marca el pluscuamperfecto.']},
 {'t': 'logro', 'titulo': '¡Misión cumplida!', 'items': ['Raíz y desinencia', 'Tiempos simples del indicativo', 'Tiempos compuestos', 'Los pretéritos en el relato'], 'xp': 100,
  'voz': ['¡Terminaste las clases de la misión del verbo!', 'Sabés separar la raíz y la desinencia.', 'Conocés los cinco tiempos simples del indicativo.', 'Armás los tiempos compuestos con haber y el participio.', 'Y elegís el pretérito justo para cada parte de un relato. ¡A practicar!']},
]
for n, esc in CL.items():
    json.dump({'slug': f'leng1-m3-n{n}', 'step_id': STEP[n], 'materia': 'Lengua y Literatura I', 'titulo': TIT[n], 'sub': f'Lengua y Literatura I · Misión 12 · Nivel {n}', 'escenas': esc},
              open(os.path.join(RAIZ, 'tools/clase/lecciones', f'leng1-m3-n{n}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ============================ LECCIÓN ============================
VERB = ['caminar', 'saltar', 'comer', 'correr', 'vivir', 'escribir']
L = {}
L['1'] = {'temas': [
 T('Raíz y desinencia',
   m('formacion', items=[
     {'palabra': 'caminábamos', 'partes': [['camin', 'raíz', 'guarda el significado de caminar'], ['ábamos', 'desinencia', 'dice nosotros y tiempo pasado']], 'significado': 'nosotros, en el pasado', 'cierre': 'La raíz dice qué acción es; la desinencia, quién y cuándo.'},
     {'palabra': 'escribirán', 'partes': [['escrib', 'raíz', 'la idea de escribir'], ['irán', 'desinencia', 'dice ellos y tiempo futuro']], 'significado': 'ellos, en el futuro', 'cierre': 'Cambiando solo la desinencia, cambian la persona y el tiempo.'},
     {'palabra': 'temés', 'partes': [['tem', 'raíz', 'la idea de temer'], ['és', 'desinencia', 'dice vos y tiempo presente']], 'significado': 'vos, en el presente', 'cierre': 'La desinencia del voseo también lleva tilde: temés, cantás, vivís.'}]),
   m('elegir_x', consigna='¿Cuál es la raíz de cada forma verbal?', items=[
     {'cons': '¿Cuál es la raíz de «saltábamos»?', 'ops': ['salt-', 'saltá-', '-ábamos'], 'ayuda': 'Sacale al infinitivo saltar la terminación -ar.'},
     {'cons': '¿Cuál es la raíz de «corrieron»?', 'ops': ['corr-', 'corri-', '-ieron'], 'ayuda': 'Infinitivo correr menos -er.'},
     {'cons': '¿Cuál es la raíz de «partiremos»?', 'ops': ['part-', 'partir-', '-emos'], 'ayuda': 'Infinitivo partir menos -ir.'},
     {'cons': '¿Cuál es la desinencia de «mirás»?', 'ops': ['-ás', 'mir-', 'mirá-'], 'ayuda': 'La desinencia es la terminación que dice vos y presente.'}]),
   ('Raíz y desinencia', 'La raíz es la parte del verbo que guarda su significado y no cambia; la desinencia es la terminación que cambia para indicar persona, número y tiempo.'),
   'Para encontrar la raíz, sacale al infinitivo la terminación -ar, -er o -ir: de «caminar» queda «camin-». Todo lo que viene después de la raíz en una forma conjugada es la desinencia, y es la parte que da la información gramatical: quién hace la acción, cuántos son y cuándo ocurre.',
   ['Raíz: el infinitivo sin -ar, -er o -ir.', 'Desinencia: la terminación que cambia.', 'La desinencia dice persona, número y tiempo.']),
 T('Persona y número',
   m('conjugador', verbos=VERB, tiempos=['presente']),
   m('unir_x', consigna='Uní cada forma del presente con su persona.', items=[
     {'pares': [['caminamos', 'nosotros'], ['caminás', 'vos'], ['caminan', 'ellos / ellas'], ['camino', 'yo']]},
     {'pares': [['comés', 'vos'], ['comen', 'ellos / ellas'], ['come', 'él / ella'], ['comemos', 'nosotros']]},
     {'pares': [['vivís', 'vos'], ['vivo', 'yo'], ['vive', 'él / ella'], ['vivimos', 'nosotros']]}]),
   ('Persona y número', 'La persona indica quién realiza la acción: el que habla, a quien se habla o de quien se habla; el número indica si es uno solo o son varios.'),
   'Las personas del singular son yo, vos y él o ella; las del plural, nosotros, ustedes y ellos. En la Argentina usamos «vos», con desinencias propias como -ás, -és o -ís. Como la desinencia ya dice la persona, muchas veces el sujeto no se nombra: en «Salimos temprano» sabemos que fuimos nosotros.',
   ['Primera: quien habla (yo, nosotros).', 'Segunda: a quien se habla (vos, ustedes).', 'Tercera: de quien se habla (él, ellos).']),
 T('Verbos regulares e irregulares',
   m('transformar', items=[
     {'nombre': 'Cantar (regular)', 'antes': 'cantar', 'pasos': [{'v': '{{cant}}o', 'txt': 'Presente: la raíz es la misma que en el infinitivo.'}, {'v': '{{cant}}é', 'txt': 'Pretérito: sigue igual.'}, {'v': '{{cant}}aré', 'txt': 'Futuro: la raíz no cambia nunca.'}], 'cierre': 'Regular: siempre cant-.'},
     {'nombre': 'Poder (irregular)', 'antes': 'poder', 'pasos': [{'v': '{{pued}}o', 'txt': 'Presente: la raíz cambia a pued-.'}, {'v': '{{pud}}e', 'txt': 'Pretérito: ahora es pud-.'}, {'v': '{{podr}}é', 'txt': 'Futuro: otra raíz distinta.'}], 'cierre': 'Irregular: la raíz cambia.'},
     {'nombre': 'Tener (irregular)', 'antes': 'tener', 'pasos': [{'v': '{{teng}}o', 'txt': 'Presente: aparece una g.'}, {'v': '{{tuv}}e', 'txt': 'Pretérito: tuv-.'}, {'v': '{{tendr}}é', 'txt': 'Futuro: tendr-.'}], 'cierre': 'Tener cambia la raíz en los tres tiempos.'}]),
   m('clasificar_x', consigna='Conjugado en presente, pretérito y futuro: ¿regular o irregular?', cajas=['Regular', 'Irregular'], cuantos=6, items=[
     ['camino, caminé, caminaré', 0], ['como, comí, comeré', 0], ['vivo, viví, viviré', 0], ['salto, salté, saltaré', 0],
     ['puedo, pude, podré', 1], ['tengo, tuve, tendré', 1], ['hago, hice, haré', 1], ['digo, dije, diré', 1]]),
   ('Verbo irregular', 'Un verbo irregular es el que cambia su raíz, o se aparta de las desinencias del modelo, en alguna de sus formas conjugadas.'),
   'Para saber si un verbo es regular, conjugalo en presente, en pretérito y en futuro y mirá la raíz. Si se mantiene igual que en el infinitivo, como en cant-o, cant-é, cant-aré, es regular. Muchos de los verbos más usados son irregulares: ser, ir, tener, hacer, poder o decir.',
   ['Regular: la raíz no cambia.', 'Irregular: la raíz cambia (pued-o, pud-e).', 'Probalo en presente, pretérito y futuro.']),
 T('Las formas no personales',
   m('esquema', items=[{'nombre': 'Verboides', 'cols': ['Forma', 'Ejemplo', 'Para qué se usa'], 'filas': [
       ['Infinitivo (-ar, -er, -ir)', 'saltar', 'nombra el verbo'], ['Gerundio (-ando, -iendo)', 'saltando', 'acción en curso'], ['Participio (-ado, -ido)', 'saltado', 'tiempos compuestos']],
     'cierre': 'Ninguna de las tres dice quién hace la acción ni cuándo.'}]),
   m('clasificar_x', consigna='¿Qué forma no personal es cada palabra?', cajas=['Infinitivo', 'Gerundio', 'Participio'], cuantos=6, items=[
     ['escribir', 0], ['correr', 0], ['subir', 0], ['escribiendo', 1], ['corriendo', 1], ['bailando', 1], ['escrito', 2], ['corrido', 2], ['bailado', 2]]),
   ('Formas no personales', 'Las formas no personales, también llamadas verboides, son el infinitivo, el gerundio y el participio: no indican persona, número ni tiempo.'),
   'Por eso no pueden decir solas quién hace la acción: «corriendo» puede ser yo, vos o ellos. Suelen acompañar a otro verbo, como en «Está corriendo» o «Había corrido». El participio es clave para el nivel 3, porque con él se arman los tiempos compuestos. Algunos son irregulares: escrito, roto, dicho, hecho.',
   ['Infinitivo: -ar, -er, -ir.', 'Gerundio: -ando, -iendo.', 'Participio: -ado, -ido, y algunos irregulares.'])],
 'recuerda': [
   R('Raíz', 'es la parte del verbo que guarda su significado; se obtiene quitando -ar, -er o -ir al infinitivo.', 'camin- en caminábamos'),
   R('Desinencia', 'es la terminación del verbo que cambia para indicar persona, número y tiempo.', '-ábamos: nosotros, en pasado'),
   R('Conjugaciones', 'son los tres grupos de verbos según su infinitivo: primera en -ar, segunda en -er y tercera en -ir.', 'cantar, comer, vivir'),
   R('Persona y número', 'indican quién hace la acción, el que habla, a quien se habla o de quien se habla, y si son uno o varios.', 'comemos: primera persona plural'),
   R('Verbo irregular', 'es el que cambia su raíz en alguna de sus formas conjugadas.', 'poder: puedo, pude, podré'),
   R('Formas no personales', 'son el infinitivo, el gerundio y el participio, que no indican persona ni tiempo.', 'saltar, saltando, saltado')]}

L['2'] = {'temas': [
 T('El presente y sus usos',
   m('marcar', rotulo='Oraciones', items=[
     {'nombre': 'Tres presentes', 'texto': '{{Ahora leo|Presente actual: ocurre en este momento.}} el diario. {{Todos los días camino|Presente habitual: algo que se repite.}} hasta la plaza. {{El agua hierve|Presente atemporal: algo que siempre es verdad.}} a cien grados.', 'cierre': 'El mismo tiempo verbal, tres usos distintos.'},
     {'nombre': 'Presente histórico', 'texto': 'En 1816, {{el Congreso declara|Presente histórico: un hecho pasado contado en presente.}} la independencia en Tucumán y {{los diputados firman|El presente acerca el hecho al lector.}} el acta.', 'cierre': 'Muy usado en biografías y libros de Historia.'}]),
   m('clasificar_x', consigna='¿Qué uso del presente tiene cada oración?', cajas=['Actual', 'Habitual', 'Atemporal', 'Histórico'], cuantos=6, items=[
     ['Ahora llueve fuerte', 0], ['En este momento escribo un mensaje', 0], ['Los sábados juego al fútbol', 1], ['Mi tía viaja cada verano', 1],
     ['La Tierra gira alrededor del Sol', 2], ['Dos más dos son cuatro', 2], ['En 1492 Colón llega a América', 3], ['En 1810 se forma la Primera Junta', 3]]),
   ('Presente', 'El presente del indicativo expresa acciones que ocurren en el momento en que se habla, que se repiten o que siempre son verdad.'),
   'Además, puede contar hechos pasados para acercarlos al lector: es el presente histórico, muy usado en biografías y libros de Historia. Por eso, para saber qué uso tiene, no alcanza con mirar el verbo: hay que mirar las palabras que lo acompañan, como «ahora», «todos los días» o una fecha.',
   ['Actual: ahora leo.', 'Habitual: todos los días camino.', 'Atemporal e histórico: el agua hierve; en 1816 declaran.']),
 T('Los pretéritos y el futuro',
   m('conjugador', verbos=VERB, tiempos=['pretérito perfecto simple', 'pretérito imperfecto', 'futuro']),
   m('conjugar_x', verbos=VERB, tiempos=['pretérito perfecto simple', 'pretérito imperfecto', 'futuro']),
   ('Pretéritos y futuro', 'El pretérito perfecto simple cuenta acciones pasadas y terminadas, el pretérito imperfecto describe lo que duraba o se repetía en el pasado, y el futuro anuncia lo que todavía no ocurrió.'),
   'Los dos pretéritos tienen desinencias muy distintas: el perfecto simple termina en -é, -aste, -ó o en -í, -iste, -ió; el imperfecto, en -aba o en -ía. Para formar el futuro hay un truco: al infinitivo entero, sin quitarle nada, se le agrega -é, -ás, -á, -emos o -án, como en cantar-é, comer-ás o vivir-emos.',
   ['Perfecto simple: canté, comí.', 'Imperfecto: cantaba, comía.', 'Futuro: infinitivo + é (cantaré).']),
 T('El condicional',
   m('conjugador', verbos=VERB, tiempos=['condicional', 'futuro']),
   m('completar_x', consigna='Elegí la forma que corresponde.', items=[
     {'texto': 'Si tuviera tiempo, [[leería/leeré/leía]] todos los días.'},
     {'texto': 'Me dijo que [[vendría/vino/viene]] a la fiesta, pero no apareció.'},
     {'texto': '¿[[Podrías/Podrás/Pudiste]] alcanzarme la sal, por favor?'},
     {'texto': 'Si [[pudiera/podría/podré]], [[viajaría/viajaré/viajé]] a Salta.'}]),
   ('Condicional', 'El condicional expresa acciones posibles que dependen de una condición; para formarlo, al infinitivo entero se le agrega -ía, -ías, -íamos o -ían.'),
   'Tiene tres usos frecuentes: lo que pasaría si se cumpliera algo («Si tuviera tiempo, leería»), lo que alguien anunció en el pasado sobre el futuro («Dijo que vendría») y los pedidos amables («¿Podrías ayudarme?»). Ojo: después de «si» no va condicional; se dice «si pudiera», nunca «si podría».',
   ['Condición: si tuviera, leería.', 'Futuro visto desde el pasado: dijo que vendría.', 'Cortesía: ¿podrías ayudarme?'])],
 'recuerda': [
   R('Tiempo verbal', 'es la forma del verbo que ubica la acción antes, durante o después del momento en que se habla.', 'canté, canto, cantaré'),
   R('Presente', 'expresa lo que ocurre ahora, lo que se repite o lo que siempre es verdad.', 'Todos los días camino hasta la plaza'),
   R('Presente histórico', 'es el uso del presente para contar hechos pasados y acercarlos al lector.', 'En 1816, el Congreso declara la independencia'),
   R('Pretérito perfecto simple', 'cuenta acciones pasadas que ocurrieron de una vez y ya terminaron.', 'Anoche llovió'),
   R('Pretérito imperfecto', 'describe lo que duraba o se repetía en el pasado y arma el fondo de un relato.', 'Llovía toda la noche'),
   R('Futuro', 'anuncia lo que todavía no ocurrió; se forma agregando -é, -ás, -á, -emos o -án al infinitivo entero.', 'vivir + é = viviré'),
   R('Condicional', 'expresa lo que pasaría si se cumpliera una condición, y también pedidos amables.', 'Si tuviera tiempo, leería')]}

L['3'] = {'temas': [
 T('Cómo se forma un tiempo compuesto',
   m('formacion', items=[
     {'palabra': 'había cantado', 'partes': [['había', 'auxiliar haber', 'en imperfecto: lleva persona y tiempo'], ['cantado', 'participio', 'lleva el significado: cantar']], 'significado': 'algo anterior a otro hecho del pasado', 'cierre': 'Haber cambia; el participio queda igual.'},
     {'palabra': 'hemos comido', 'partes': [['hemos', 'auxiliar haber', 'en presente: nosotros'], ['comido', 'participio', 'de comer']], 'significado': 'algo terminado que llega hasta hoy', 'cierre': 'Haber en presente forma el perfecto compuesto.'},
     {'palabra': 'habrán vuelto', 'partes': [['habrán', 'auxiliar haber', 'en futuro: ellos'], ['vuelto', 'participio irregular', 'de volver']], 'significado': 'algo terminado antes de un momento futuro', 'cierre': 'Volver tiene participio irregular: vuelto, no volvido.'}]),
   m('completar_x', consigna='Elegí el participio correcto.', items=[
     {'texto': 'Todavía no hemos [[terminado/terminando/terminar]] la tarea.'},
     {'texto': 'Cuando llegué, ya habían [[roto/rompido/rompiendo]] el vidrio.'},
     {'texto': 'Mi prima me había [[escrito/escribido/escribiendo]] una carta larguísima.'},
     {'texto': '¿Ya han [[vuelto/volvido/volviendo]] de las vacaciones?'}]),
   ('Tiempo compuesto', 'Un tiempo compuesto se forma con el verbo auxiliar haber conjugado más el participio del verbo principal, como «había cantado».'),
   'El auxiliar haber es el que cambia: lleva la persona, el número y el tiempo. El participio queda siempre igual y aporta el significado. Hay que cuidar los participios irregulares, que no terminan en -ado ni en -ido: se dice «había roto», «ha escrito», «hemos vuelto», «habían dicho» y «has hecho».',
   ['Haber conjugado + participio.', 'Haber cambia; el participio no.', 'Irregulares: roto, escrito, vuelto, dicho, hecho.']),
 T('Cada simple con su compuesto',
   m('esquema', items=[{'nombre': 'Correlación', 'cols': ['Haber en…', 'Tiempo compuesto', 'Ejemplo'], 'filas': [
       ['presente (he)', 'pretérito perfecto compuesto', 'he cantado'], ['imperfecto (había)', 'pretérito pluscuamperfecto', 'había cantado'],
       ['futuro (habré)', 'futuro perfecto', 'habré cantado'], ['condicional (habría)', 'condicional perfecto', 'habría cantado'], ['perfecto simple (hube)', 'pretérito anterior', 'hube cantado']],
     'cierre': 'El nombre del compuesto sale del tiempo en que está haber.'}]),
   m('unir_x', consigna='Uní cada forma con el nombre de su tiempo.', items=[
     {'pares': [['he cantado', 'pretérito perfecto compuesto'], ['había cantado', 'pretérito pluscuamperfecto'], ['habré cantado', 'futuro perfecto'], ['habría cantado', 'condicional perfecto']]},
     {'pares': [['hemos salido', 'pretérito perfecto compuesto'], ['habían salido', 'pretérito pluscuamperfecto'], ['habrás salido', 'futuro perfecto'], ['habríamos salido', 'condicional perfecto']]}]),
   ('Correlación de tiempos', 'Cada tiempo simple del indicativo tiene su compuesto: se conjuga el auxiliar haber en ese tiempo simple y se le suma el participio.'),
   'Para nombrar un tiempo compuesto, mirá en qué tiempo está haber. Si está en presente («he»), es pretérito perfecto compuesto; en imperfecto («había»), pluscuamperfecto; en futuro («habré»), futuro perfecto; en condicional («habría»), condicional perfecto. El pretérito anterior («hube cantado») casi no se usa hoy.',
   ['he → perfecto compuesto.', 'había → pluscuamperfecto.', 'habré → futuro perfecto; habría → condicional perfecto.']),
 T('Qué expresan: lo anterior',
   m('linea_tiempo', items=[
     {'nombre': 'Los bomberos', 'hechos': [{'t': 'Cuando llegaron los bomberos', 'c': 2}, {'t': 'un vecino ya había apagado el fuego', 'c': 1}, {'t': 'y se fueron enseguida', 'c': 3}],
      'marca': 'El pluscuamperfecto cuenta lo que pasó antes de otro hecho pasado.', 'cierre': 'Primero se apagó el fuego; después llegaron los bomberos.'},
     {'nombre': 'El examen', 'hechos': [{'t': 'Mañana a las diez', 'c': 2}, {'t': 'ya habré terminado el examen', 'c': 1}, {'t': 'y saldré a festejar', 'c': 3}],
      'marca': 'El futuro perfecto cuenta lo que estará terminado antes de un momento futuro.', 'cierre': 'Terminar el examen ocurre antes de las diez.'}]),
   m('elegir_x', consigna='Elegí la forma que expresa lo que corresponde.', items=[
     {'cons': '«Cuando llegué al cine, la película ya ___.» (empezó antes de que llegara)', 'ops': ['había empezado', 'empezaba', 'empezará'], 'ayuda': 'Anterior a otro hecho pasado: pluscuamperfecto.'},
     {'cons': '«Para el viernes, ya ___ el libro.» (terminado antes de un momento futuro)', 'ops': ['habré leído', 'leí', 'había leído'], 'ayuda': 'Futuro perfecto: habré + participio.'},
     {'cons': '«Este año ___ tres novelas.» (un período que llega hasta hoy)', 'ops': ['he leído', 'había leído', 'habré leído'], 'ayuda': '«Este año» llega hasta el presente: perfecto compuesto.'}]),
   ('Anterioridad', 'Los tiempos compuestos expresan acciones terminadas antes de otro momento: el presente, otro hecho pasado o un momento futuro.'),
   'El pluscuamperfecto cuenta lo que pasó antes de otro hecho pasado: «Cuando llegaron, ya había salido». El futuro perfecto, lo que estará terminado antes de un momento futuro. El perfecto compuesto une el pasado con el presente: «Este año he leído tres novelas». En la Argentina solemos reemplazarlo por el perfecto simple: «Este año leí tres novelas».',
   ['Pluscuamperfecto: antes de otro pasado.', 'Futuro perfecto: antes de un momento futuro.', 'Perfecto compuesto: pasado unido al presente.'])],
 'recuerda': [
   R('Tiempo compuesto', 'se forma con el auxiliar haber conjugado y el participio del verbo principal.', 'había cantado'),
   R('Auxiliar haber', 'es la parte del tiempo compuesto que cambia y lleva la persona, el número y el tiempo.', 'he, había, habré, habría'),
   R('Participios irregulares', 'son los que no terminan en -ado ni en -ido y hay que aprender de memoria.', 'roto, escrito, vuelto, dicho, hecho'),
   R('Pretérito pluscuamperfecto', 'cuenta una acción terminada antes de otro hecho del pasado.', 'Cuando llegaron, el fuego ya se había apagado'),
   R('Futuro perfecto', 'cuenta una acción que estará terminada antes de un momento futuro.', 'Mañana a las diez ya habré terminado'),
   R('Pretérito perfecto compuesto', 'une una acción pasada con el presente de quien habla.', 'Este año he leído tres novelas')]}

L['4'] = {'temas': [
 T('Acción y fondo',
   m('marcar', rotulo='Relato', items=[
     {'nombre': 'La tormenta', 'texto': '{{Era|Imperfecto: describe el momento.}} tarde y {{llovía|Imperfecto: algo que duraba, el fondo.}} sin parar. De pronto, alguien {{golpeó|Perfecto simple: una acción que irrumpe.}} la puerta y Ana {{corrió|Perfecto simple: la historia avanza.}} a abrir.', 'cierre': 'El imperfecto pinta el escenario; el perfecto simple hace avanzar la historia.'},
     {'nombre': 'El abuelo', 'texto': 'Todos los veranos, mi abuelo {{preparaba|Imperfecto: una costumbre que se repetía.}} dulce de higos. Un día, un frasco {{explotó|Perfecto simple: un hecho único que rompe la rutina.}} en la cocina.', 'cierre': 'Costumbre en imperfecto; el hecho único, en perfecto simple.'}]),
   m('completar_x', consigna='Elegí el pretérito que corresponde.', items=[
     {'texto': 'Mientras [[cocinaba/cociné/cocino]], sonó el teléfono.'},
     {'texto': 'La casa [[estaba/estuvo/está]] vacía y [[hacía/hizo/hace]] mucho frío.'},
     {'texto': 'De repente, la luz se [[apagó/apagaba/apaga]].'},
     {'texto': 'Cada mañana, mi hermana [[salía/salió/sale]] a correr antes del desayuno.'}]),
   ('Acción y fondo', 'En un relato, el pretérito perfecto simple cuenta las acciones que hacen avanzar la historia y el pretérito imperfecto describe el fondo: escenarios, estados y costumbres.'),
   'Una buena pregunta para elegir es: ¿duraba o pasó? Si algo duraba, se repetía o describe cómo eran las cosas, va en imperfecto. Si ocurrió de una vez y terminó, va en perfecto simple. Muchas veces aparecen juntos: el imperfecto arma la escena y el perfecto simple la interrumpe con un hecho.',
   ['Imperfecto: era, llovía, preparaba.', 'Perfecto simple: golpeó, corrió, explotó.', 'Pregunta clave: ¿duraba o pasó?']),
 T('El pluscuamperfecto: volver atrás',
   m('linea_tiempo', items=[
     {'nombre': 'La carta', 'hechos': [{'t': 'Lucía abrió el buzón', 'c': 2}, {'t': 'y encontró una carta', 'c': 3}, {'t': 'que su abuela le había mandado hacía años', 'c': 1}],
      'marca': 'El pluscuamperfecto vuelve atrás en el tiempo.', 'cierre': 'La abuela mandó la carta mucho antes de que Lucía la encontrara.'},
     {'nombre': 'El viaje', 'hechos': [{'t': 'Cuando el tren arrancó', 'c': 2}, {'t': 'Tomás se dio cuenta', 'c': 3}, {'t': 'de que había olvidado la valija', 'c': 1}],
      'marca': 'Olvidar la valija pasó antes que todo lo demás.', 'cierre': 'Primero olvidó la valija, después arrancó el tren y recién ahí se dio cuenta.'}]),
   m('elegir_x', consigna='Elegí la forma que cuenta lo que pasó antes.', items=[
     {'cons': '«Cuando llegué a la estación, el tren ya ___.»', 'ops': ['había salido', 'salía', 'sale'], 'ayuda': 'Salió antes de que llegaras: pluscuamperfecto.'},
     {'cons': '«Encontré el anillo que mi madre ___ años atrás.»', 'ops': ['había perdido', 'pierde', 'perderá'], 'ayuda': 'Lo perdió antes de que lo encontraras.'},
     {'cons': '«Ana no quiso comer porque ya ___ en lo de su tía.»', 'ops': ['había almorzado', 'almuerza', 'almorzará'], 'ayuda': 'Almorzó antes de no querer comer.'}]),
   ('Pluscuamperfecto en el relato', 'El pretérito pluscuamperfecto permite al narrador contar un hecho anterior a otro hecho del pasado, es decir, volver atrás en la historia.'),
   'Es el tiempo de los recuerdos y las explicaciones: el relato avanza en perfecto simple y, cuando necesita contar algo que había pasado antes, cambia a «había» más participio. Así el lector entiende el orden real de los hechos aunque se cuenten en otro orden.',
   ['Se forma con había + participio.', 'Cuenta lo anterior a otro pasado.', 'Sirve para recuerdos y explicaciones.']),
 T('La coherencia de los tiempos',
   m('transformar', items=[
     {'nombre': 'El salto al presente', 'antes': 'Entró a la casa y ve una carta sobre la mesa.', 'pasos': [{'v': 'Entró a la casa y {{ve}} una carta sobre la mesa.', 'txt': '«Entró» está en pasado, pero «ve» salta al presente.'}, {'v': 'Entró a la casa y {{vio}} una carta sobre la mesa.', 'txt': 'Corregido: las dos acciones en perfecto simple.'}], 'cierre': 'Si el relato está en pasado, se mantiene en pasado.'},
     {'nombre': 'El fondo mal elegido', 'antes': 'Mientras leí, sonó el timbre.', 'pasos': [{'v': 'Mientras {{leí}}, sonó el timbre.', 'txt': 'Leer duraba de fondo: no va en perfecto simple.'}, {'v': 'Mientras {{leía}}, sonó el timbre.', 'txt': 'Imperfecto para lo que dura; perfecto simple para lo que interrumpe.'}], 'cierre': '«Mientras» casi siempre pide imperfecto.'},
     {'nombre': 'Lo anterior', 'antes': 'Llegó tarde porque perdió el colectivo antes.', 'pasos': [{'v': 'Llegó tarde porque {{perdió}} el colectivo antes.', 'txt': 'Se entiende, pero hace falta «antes» para aclarar el orden.'}, {'v': 'Llegó tarde porque {{había perdido}} el colectivo.', 'txt': 'El pluscuamperfecto ya marca lo anterior.'}], 'cierre': 'Cada pretérito en su lugar.'}]),
   m('marcar_x', consigna='Tocá los verbos que rompen el pasado del relato.', items=[
     {'cons': 'Relato: «Ana salió temprano. Camina hasta la plaza y se sentó en un banco.»', 'texto': '[[Ana|0]] [[salió|0]] [[temprano.|0]] [[Camina|1]] [[hasta|0]] [[la|0]] [[plaza|0]] [[y|0]] [[se|0]] [[sentó|0]] [[en|0]] [[un|0]] [[banco.|0]]'},
     {'cons': 'Relato: «El perro ladró, abrí la puerta y encuentro a mi vecino, que me saluda.»', 'texto': '[[El|0]] [[perro|0]] [[ladró,|0]] [[abrí|0]] [[la|0]] [[puerta|0]] [[y|0]] [[encuentro|1]] [[a|0]] [[mi|0]] [[vecino,|0]] [[que|0]] [[me|0]] [[saluda.|1]]'},
     {'cons': 'Relato: «Hacía frío. Los chicos jugaban en la vereda cuando empieza a nevar.»', 'texto': '[[Hacía|0]] [[frío.|0]] [[Los|0]] [[chicos|0]] [[jugaban|0]] [[en|0]] [[la|0]] [[vereda|0]] [[cuando|0]] [[empieza|1]] [[a|0]] [[nevar.|0]]'}]),
   ('Coherencia temporal', 'La coherencia temporal es mantener a lo largo del relato el tiempo elegido para narrar, sin saltar al presente ni mezclar pretéritos sin motivo.'),
   'Cuando un relato está en pasado, sus verbos se ordenan alrededor de los pretéritos: perfecto simple para las acciones, imperfecto para el fondo y pluscuamperfecto para lo anterior. Si un verbo salta al presente sin razón, el lector se confunde. Al revisar un texto propio, conviene hacer una pasada solo para mirar los verbos.',
   ['Elegí un tiempo y sostenelo.', 'No saltes al presente sin motivo.', 'Revisá los verbos en una pasada propia.'])],
 'recuerda': [
   R('Perfecto simple en el relato', 'cuenta las acciones que pasan de una vez y hacen avanzar la historia.', 'Alguien golpeó la puerta'),
   R('Imperfecto en el relato', 'describe el fondo: el escenario, los estados y las costumbres que se repetían.', 'Era tarde y llovía'),
   R('Pluscuamperfecto en el relato', 'vuelve atrás para contar un hecho anterior a otro hecho del pasado.', 'Se dio cuenta de que había olvidado la valija'),
   R('Coherencia temporal', 'es sostener el tiempo elegido para narrar sin saltar al presente ni mezclar pretéritos sin motivo.', 'Entró y vio la carta, no entró y ve'),
   R('¿Duraba o pasó?', 'es la pregunta que ayuda a elegir entre imperfecto, para lo que duraba, y perfecto simple, para lo que pasó.', 'Mientras leía, sonó el timbre')]}

# ============================ ACTIVIDADES ============================
A = {
 '1': [
   UNI('Uní cada forma verbal con su persona y número.', [('caminábamos', 'primera persona plural'), ('comés', 'segunda persona singular'), ('viven', 'tercera persona plural'), ('escribí', 'primera persona singular')], 'La desinencia dice quién hace la acción.', 'aplicar'),
   CLA('Conjugados en presente, pretérito y futuro: ¿regulares o irregulares?', ['Regular', 'Irregular'], [('saltar: salto, salté, saltaré', 'Regular'), ('poder: puedo, pude, podré', 'Irregular'), ('vivir: vivo, viví, viviré', 'Regular'), ('hacer: hago, hice, haré', 'Irregular')], 'Mirá si la raíz se mantiene igual que en el infinitivo.', 'aplicar'),
   SA('¿Cuál es la raíz del verbo «escribíamos»? Escribila sin guion.', ['escrib', 'escrib-'], 'Infinitivo escribir, menos -ir: escrib-.', 'aplicar'),
   MC('Martín dice que en la palabra «corriendo» se sabe quién está corriendo. ¿Qué le falta entender?', ['Que el gerundio es una forma no personal', 'Que «corriendo» está en futuro', 'Que «corriendo» es un sustantivo'], 'Que el gerundio es una forma no personal', 'Puede ser yo, vos o ellos: el gerundio no indica persona.', 'error')],
 '2': [
   CLA('¿Qué uso del presente tiene cada oración?', ['Habitual', 'Atemporal', 'Histórico'], [('Los domingos almorzamos con mis abuelos', 'Habitual'), ('El agua hierve a cien grados', 'Atemporal'), ('En 1816 se declara la independencia', 'Histórico'), ('Mi primo entrena tres veces por semana', 'Habitual')], 'Mirá las palabras que acompañan al verbo.', 'aplicar'),
   UNI('Uní cada forma del verbo cantar con su tiempo.', [('cantaba', 'pretérito imperfecto'), ('cantó', 'pretérito perfecto simple'), ('cantará', 'futuro'), ('cantaría', 'condicional')], 'Cada tiempo tiene su desinencia.', 'aplicar'),
   SA('Conjugá el verbo «vivir» en condicional, primera persona del singular (yo).', ['viviría'], 'Infinitivo vivir + -ía: viviría.', 'aplicar'),
   MC('Sofi escribió: «Si podría, iría al recital». ¿Cómo queda bien escrita la oración?', ['Si pudiera, iría al recital', 'Si podré, iría al recital', 'Si podía, iré al recital'], 'Si pudiera, iría al recital', 'Después de «si» no va condicional.', 'error')],
 '3': [
   UNI('Uní cada forma compuesta con el nombre de su tiempo.', [('he comido', 'pretérito perfecto compuesto'), ('había comido', 'pretérito pluscuamperfecto'), ('habré comido', 'futuro perfecto'), ('habría comido', 'condicional perfecto')], 'Mirá en qué tiempo está haber.', 'aplicar'),
   TAP('En «Cuando llegamos, ya habían cerrado la puerta», tocá las dos palabras que forman el tiempo compuesto.', ['Cuando', 'llegamos,', 'ya', 'habían', 'cerrado', 'la', 'puerta'], [3, 4], 'Haber conjugado + participio.', 'analizar'),
   SA('Completá con el participio de «romper»: «Alguien había ___ la ventana».', ['roto'], 'Participio irregular: roto, no rompido.', 'aplicar'),
   MC('«A las ocho ya habré terminado la tarea.» ¿Qué expresa el futuro perfecto en esta oración?', ['Algo terminado antes de un momento futuro', 'Una costumbre del pasado', 'Una acción que ocurre ahora'], 'Algo terminado antes de un momento futuro', 'Terminar ocurre antes de las ocho.', 'analizar')],
 '4': [
   CLA('¿Fondo o acción? Clasificá cada parte del relato.', ['Fondo (imperfecto)', 'Acción (perfecto simple)'], [('La casa estaba en silencio', 'Fondo (imperfecto)'), ('De pronto, sonó el timbre', 'Acción (perfecto simple)'), ('Llovía desde la mañana', 'Fondo (imperfecto)'), ('Ana abrió la puerta', 'Acción (perfecto simple)')], '¿Duraba o pasó?', 'aplicar'),
   ORD('Ordená los hechos como ocurrieron en el tiempo: «Cuando el tren arrancó, Tomás se dio cuenta de que había olvidado la valija.»', ['Tomás olvidó la valija', 'El tren arrancó', 'Tomás se dio cuenta'], 'El pluscuamperfecto marca lo que pasó primero.', 'analizar'),
   TAP('Tocá el verbo que rompe la coherencia temporal del relato.', ['Salió', 'de', 'casa,', 'caminó', 'dos', 'cuadras', 'y', 've', 'un', 'perro.'], [7], 'El relato está en pasado: debería decir «vio».', 'analizar'),
   KW('Explicá por qué en un relato conviene usar el imperfecto para el fondo y el perfecto simple para las acciones. Escribí un ejemplo.', 'Decí qué hace cada tiempo y armá una oración con los dos.', [['imperfecto', 'fondo', 'descri*', 'duraba', 'escenario', 'costumbre*'], ['perfecto simple', 'acci*', 'avanza*', 'terminad*', 'pasó', 'interrump*']], 2, 'Por ejemplo: «Llovía cuando alguien golpeó la puerta»: llovía es el fondo; golpeó, la acción.', 'analizar')],
 '5': [
   CLA('Analizá cada forma del verbo cantar: ¿tiempo simple, tiempo compuesto o forma no personal?', ['Tiempo simple', 'Tiempo compuesto', 'Forma no personal'], [('cantaríamos', 'Tiempo simple'), ('habíamos cantado', 'Tiempo compuesto'), ('cantando', 'Forma no personal'), ('cantaremos', 'Tiempo simple')], 'Una palabra con persona, haber + participio, o sin persona.', 'analizar'),
   ODD('Tres formas están en el mismo tiempo y una no. ¿Cuál no?', ['comía', 'vivíamos', 'saltaban', 'corrieron'], 'corrieron', 'Las otras tres son pretérito imperfecto; corrieron es perfecto simple.', 'analizar'),
   MS('«Cuando llegué, mi hermano ya había cocinado y la casa olía a pan.» Elegí las DOS afirmaciones correctas.', ['«Había cocinado» cuenta algo anterior a «llegué»', '«Olía» describe el fondo de la escena', '«Llegué» está en pretérito imperfecto', '«Había cocinado» está en futuro'], ['«Había cocinado» cuenta algo anterior a «llegué»', '«Olía» describe el fondo de la escena'], 'Pluscuamperfecto para lo anterior; imperfecto para el fondo.'),
   MC('«Era de noche. Juan ___ la ventana y ___ un ruido.» ¿Qué opción mantiene la coherencia del relato?', ['abrió / escuchó', 'abre / escuchó', 'abría / escucha'], 'abrió / escuchó', 'Dos acciones puntuales en pasado: perfecto simple.', 'analizar')],
}

EX = [
 [1, SA('¿Cuál es la desinencia de «cantábamos»? Escribila sin guion.', ['ábamos', 'abamos'], 'Raíz cant- + desinencia -ábamos.', 'aplicar')],
 [1, CLA('¿Regular o irregular?', ['Regular', 'Irregular'], [('partir: parto, partí, partiré', 'Regular'), ('decir: digo, dije, diré', 'Irregular'), ('mirar: miro, miré, miraré', 'Regular')], 'Mirá si cambia la raíz.', 'aplicar')],
 [1, MC('¿Qué tienen en común el infinitivo, el gerundio y el participio?', ['No indican persona ni tiempo', 'Siempre están en futuro', 'Son sustantivos'], 'No indican persona ni tiempo', 'Son formas no personales.', 'recordar')],
 [2, UNI('Uní cada forma del verbo comer con su tiempo.', [('comíamos', 'pretérito imperfecto'), ('comimos', 'pretérito perfecto simple'), ('comeremos', 'futuro'), ('comeríamos', 'condicional')], 'Cada tiempo tiene su desinencia.', 'aplicar')],
 [2, MC('«En 1810 se forma la Primera Junta.» ¿Qué uso del presente tiene esta oración?', ['Presente histórico', 'Presente habitual', 'Presente actual'], 'Presente histórico', 'Un hecho pasado contado en presente.', 'analizar')],
 [2, SA('Conjugá el verbo «escribir» en condicional, primera persona del plural (nosotros).', ['escribiríamos'], 'escribir + -íamos.', 'aplicar')],
 [3, UNI('Uní cada tiempo compuesto con su nombre.', [('hemos jugado', 'pretérito perfecto compuesto'), ('habían jugado', 'pretérito pluscuamperfecto'), ('habrás jugado', 'futuro perfecto')], 'El tiempo de haber da el nombre.', 'aplicar')],
 [3, SA('Completá con el participio de «volver»: «Todavía no han ___ de viaje».', ['vuelto'], 'Participio irregular: vuelto.', 'aplicar')],
 [3, MC('¿Con qué verbo auxiliar se forman los tiempos compuestos?', ['haber', 'ser', 'estar'], 'haber', 'Haber conjugado + participio.', 'recordar')],
 [4, CLA('¿Fondo o acción?', ['Fondo (imperfecto)', 'Acción (perfecto simple)'], [('El cielo estaba gris', 'Fondo (imperfecto)'), ('Un rayo cayó sobre el árbol', 'Acción (perfecto simple)'), ('Los perros ladraban', 'Fondo (imperfecto)')], '¿Duraba o pasó?', 'aplicar')],
 [4, TAP('Tocá el verbo que rompe la coherencia temporal del relato.', ['Llegamos', 'al', 'campo,', 'armamos', 'la', 'carpa', 'y', 'prendemos', 'el', 'fuego.'], [7], 'El relato está en pasado: debería ser «prendimos».', 'analizar')],
 [4, ORD('Ordená los hechos como ocurrieron: «Cuando abrí la heladera, vi que alguien se había comido la torta».', ['Alguien se comió la torta', 'Abrí la heladera', 'Vi que la torta no estaba'], 'El pluscuamperfecto marca lo que pasó primero.', 'analizar')],
 [4, KW('Explicá para qué sirve el pluscuamperfecto en un relato y escribí una oración que lo use.', 'Decí qué cuenta y armá un ejemplo con «había» + participio.', [['antes', 'anterior', 'previo', 'atrás', 'primero'], ['había', 'habían', 'habías', 'habíamos']], 2, 'Por ejemplo: cuenta algo anterior a otro pasado: «Cuando llegué, ya habían cenado».', 'aplicar')],
]

CARP = {
 '1': [
  ('En la forma verbal «caminábamos», la raíz es «camin-». ¿Cuál es la desinencia, la parte que cambia?', 'aplicar', ['ábamos', '-ábamos', 'abamos'], 'La desinencia es -ábamos: indica nosotros y tiempo pasado.'),
  ('Conjugamos el verbo «tener» en tres tiempos: tengo, tuve, tendré. ¿Es un verbo regular o irregular?', 'aplicar', ['irregular', 'es irregular'], 'Irregular: la raíz cambia (teng-, tuv-, tendr-).'),
  ('La forma «escribiendo» termina en -iendo y no dice quién realiza la acción. ¿Qué forma no personal es?', 'analizar', ['gerundio', 'el gerundio', 'es un gerundio'], 'Gerundio: termina en -ando o -iendo.'),
  ('Juli dice que la raíz es la parte del verbo que cambia según la persona. ¿Qué parte cambia en realidad?', 'error', ['la desinencia', 'desinencia'], 'La desinencia; la raíz guarda el significado.'),
 ],
 '2': [
  ('En la oración «La Tierra gira alrededor del Sol», el verbo está en presente. ¿Qué uso del presente tiene?', 'aplicar', ['atemporal', 'presente atemporal'], 'Atemporal: algo que siempre es verdad.'),
  ('Conjugá el verbo «comer» en pretérito imperfecto del indicativo, primera persona del plural (nosotros).', 'aplicar', ['comíamos', 'comiamos'], 'Comíamos: com- + -íamos.'),
  ('En la oración «Si tuviera plata, viajaría a Salta», la forma «viajaría» depende de una condición. ¿En qué tiempo está?', 'analizar', ['condicional', 'en condicional', 'el condicional'], 'Condicional: lo que pasaría si se cumpliera algo.'),
  ('Nico escribió «Si podría, te ayudaría». Después de «si» no va condicional. ¿Qué forma reemplaza a «podría»?', 'error', ['pudiera', 'si pudiera'], '«Si pudiera, te ayudaría».'),
 ],
 '3': [
  ('En «Cuando llegaste, ya habíamos comido», el tiempo compuesto tiene un auxiliar y un participio. ¿Cuál es el verbo auxiliar?', 'recordar', ['haber', 'el verbo haber', 'habíamos'], 'Haber, conjugado en «habíamos».'),
  ('El participio del verbo «escribir» es irregular y no termina en -ido. Completá: «Ya había ___ la carta».', 'aplicar', ['escrito'], 'Escrito: «Ya había escrito la carta».'),
  ('En «Para el lunes ya habré terminado el trabajo», el auxiliar «habré» está en futuro. ¿Cómo se llama ese tiempo?', 'analizar', ['futuro perfecto', 'el futuro perfecto'], 'Futuro perfecto: habré + participio.'),
  ('Tomi escribió «El vaso se había rompido». El participio de «romper» es irregular. ¿Cuál es el participio correcto?', 'error', ['roto'], 'Roto: «El vaso se había roto».'),
 ],
 '4': [
  ('En el relato «Llovía sin parar cuando alguien golpeó la puerta», ¿qué verbo describe el fondo de la escena?', 'aplicar', ['llovía', 'llovia'], 'Llovía: imperfecto, algo que duraba.'),
  ('En «Cuando llegué a la estación, el tren ya había salido», ¿qué pasó primero: mi llegada o la salida del tren?', 'analizar', ['la salida del tren', 'salió el tren', 'que salió el tren', 'el tren', 'la salida'], 'Primero salió el tren: lo marca el pluscuamperfecto.'),
  ('Completá con el pretérito adecuado para algo que duraba de fondo: «Mientras ___ (leer), sonó el timbre».', 'aplicar', ['leía'], 'Leía: imperfecto para lo que duraba.'),
  ('Un relato dice: «Entró a la cocina y ve una carta sobre la mesa». ¿Cómo debería escribirse el verbo «ve»?', 'error', ['vio'], 'Vio: el relato está en pasado.'),
 ],
}

def ajustes(M):
    M['act'] = A
    M['examen'] = EX
    M['practica'] = 'Actividades generales'
    M['examen_titulo'] = 'Nivel jefe: el verbo'
    M['actualizar_preguntas'] = True
    for k, items in CARP.items():
        N = M['niveles'].setdefault(k, {})
        N['carpeta'] = [c for c, _, _, _ in items]; N['carpeta_nivel'] = [t for _, t, _, _ in items]
        N['respuestas_carpeta'] = [r for _, _, r, _ in items]; N.setdefault('soluciones', {})['carpeta'] = [s for _, _, _, s in items]

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-12/mision-12.json', L, ajustes=ajustes)
