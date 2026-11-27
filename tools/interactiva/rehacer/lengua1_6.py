# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 6 · Parodia y humor literario (TODO nuevo, sobre el GÉNERO; el libro va en el nivel 5)
# Libro del nivel: «El fantasma de Canterville», de Oscar Wilde (1887, dominio público).
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD
RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', '..')

# ============================ CLASES ANIMADAS ============================
STEP = {'1': '037ca438-4ffc-4546-bac5-2d85e92fa42b', '2': '7c8e4668-4fda-412e-96a7-7706c24e7ec7', '3': '0505a6fd-24ea-4323-9560-fc64e1ae3d6e', '4': '5498e671-fda5-4d3e-af28-4376a962cc96'}
TIT = {'1': 'Cómo funciona el humor', '2': 'La ironía', '3': 'La parodia', '4': 'La sátira'}
CL = {}
CL['1'] = [
 {'t': 'chat', 'contacto': {'nombre': 'Lucas', 'emoji': '🧑'}, 'mensajes': [{'yo': False, 'txt': 'Anoté todo en un papel para no olvidarme de nada'}, {'yo': True, 'txt': '¡Bien organizado!'}, {'yo': False, 'txt': 'Ahora no me acuerdo dónde dejé el papel 🤦'}], 'titulo': 'EL HUMOR', 'sub': 'por qué nos reímos',
  'voz': ['Lucas cuenta que anotó todo en un papel para no olvidarse de nada.', 'Vos lo felicitás por organizado.', 'Y él responde que no se acuerda dónde dejó el papel.', 'Te reíste, ¿no? Hoy vemos *por qué*: el humor tiene mecanismos que se pueden reconocer.']},
 {'t': 'definicion', 'palabra': 'Incongruencia', 'texto': 'Choque entre lo que esperábamos y lo que finalmente pasa. Es el motor de casi todo el humor.', 'emoji': '💥',
  'voz': ['El papel tenía que resolver el problema y terminó empeorándolo. Ese choque se llama *incongruencia*.', 'Es el motor de casi todo el humor: el texto arma una expectativa y después la rompe.']},
 {'t': 'antesdespues', 'antes': {'cab': 'Lo que esperamos', 'emoji': '🦸', 'texto': 'El héroe entra al castillo, desenvaina la espada y…'}, 'despues': {'cab': 'Lo que pasa', 'emoji': '🤧', 'texto': '…estornuda por el polvo y se le cae la espada.'},
  'voz': ['Mirá cómo se arma. El héroe entra al castillo, desenvaina la espada, y esperamos una gran batalla.', 'Pero estornuda por el polvo y se le cae la espada. La expectativa se rompe, y aparece la risa.']},
 {'t': 'bloques', 'titulo': 'TRES RECURSOS DEL HUMOR', 'items': [{'cab': 'Lo inesperado', 'txt': 'un final que rompe lo previsto'}, {'cab': 'La exageración', 'txt': 'agrandar algo hasta lo absurdo'}, {'cab': 'Doble sentido', 'txt': 'el juego de palabras'}],
  'voz': ['Los textos humorísticos usan tres recursos principales.', '*Lo inesperado*: un final que rompe lo previsto.', 'La *exageración*: agrandar algo hasta volverlo absurdo.', 'Y el *juego de palabras*: aprovechar que una palabra tiene dos sentidos.']},
 {'t': 'escala', 'titulo': 'LA EXAGERACIÓN', 'items': [{'txt': 'Tengo hambre', 'emoji': '🍽️', 'valor': 1}, {'txt': 'Me comería una vaca', 'emoji': '🐄', 'valor': 3}, {'txt': 'Me comería la cordillera con mostaza', 'emoji': '🏔️', 'valor': 6}],
  'voz': ['Mirá cómo crece una exageración. «Tengo hambre» es un dato.', '«Me comería una vaca» ya exagera.', 'Y «me comería la cordillera con mostaza» lleva la exageración al absurdo, y por eso da risa.']},
 {'t': 'quiz4', 'pregunta': '«—¿Tu perro muerde? —No. —(El perro lo muerde.) —¡Este no es mi perro!» ¿Qué recurso usa?', 'opciones': ['Exageración', 'Lo inesperado', 'Juego de palabras', 'Ninguno'], 'correcta': 1,
  'voz': ['Un clásico: alguien pregunta si el perro muerde, le dicen que no, el perro lo muerde, y el otro responde: «¡este no es mi perro!».', 'Pensá qué recurso hace reír.', '*Lo inesperado*: el final cambia todo lo que creíamos.']},
 {'t': 'errores', 'items': [{'mal': 'El humor es solo para chistes', 'bien': 'También aparece en cuentos, novelas y obras de teatro'}, {'mal': 'Si no me río, no hay humor', 'bien': 'El recurso está aunque a vos no te cause gracia'}],
  'voz': ['Dos ideas equivocadas.', 'El humor no es solo cosa de chistes: hay cuentos, novelas y obras enteras construidas con humor.', 'Y que a vos algo no te haga reír no significa que no haya humor: el recurso está ahí y se puede analizar.']},
 {'t': 'resumen', 'items': [['Incongruencia', 'lo que esperamos choca con lo que pasa'], ['Lo inesperado', 'un final que sorprende'], ['Exageración', 'agrandar hasta lo absurdo'], ['Juego de palabras', 'el doble sentido']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 1'},
  'voz': ['Repasemos.', 'El humor nace de un choque entre lo esperado y lo que pasa.', 'La incongruencia.', 'Lo inesperado.', 'La exageración.', 'Y el juego de palabras. ¡A practicar!']},
]
CL['2'] = [
 {'t': 'reto', 'texto': 'Está diluviando y tu hermana dice: «¡Qué lindo día para ir a la playa!». ¿Qué quiere decir?', 'segundos': 5, 'respuesta': 'Lo contrario: que es un día horrible', 'emoji': '🌧️', 'titulo': 'LA IRONÍA', 'sub': 'decir lo contrario',
  'voz': ['Reto: está diluviando y tu hermana dice: «¡qué lindo día para ir a la playa!».', 'Cinco segundos: ¿qué quiere decir en realidad?', 'Lo contrario: que es un día horrible. Eso es *ironía*.']},
 {'t': 'definicion', 'palabra': 'Ironía', 'texto': 'Recurso que consiste en decir lo contrario de lo que se piensa, esperando que el otro entienda el verdadero sentido.', 'emoji': '😏',
  'voz': ['La *ironía* consiste en decir lo contrario de lo que se piensa.', 'Funciona solo si el otro se da cuenta: el que habla confía en que vamos a entender el verdadero sentido.']},
 {'t': 'comparar', 'a': {'cab': 'Lo que dice', 'texto': '«¡Qué puntual!»', 'emoji': '💬'}, 'b': {'cab': 'Lo que quiere decir', 'texto': 'llegaste una hora tarde', 'emoji': '⏰'}, 'signo': '≠',
  'voz': ['Separemos las dos capas.', 'Lo que se dice: «¡qué puntual!».', 'Lo que se quiere decir: llegaste una hora tarde. En la ironía, esas dos capas no coinciden.']},
 {'t': 'pistas', 'problema': '¿Cómo sé que «¡Me encanta lavar platos!» es irónico?', 'pistas': ['Contexto: una pila de platos', 'Tono: suspira al decirlo', 'Exageración: «me encanta»'], 'respuesta': 'Piensa lo contrario',
  'voz': ['¿Cómo nos damos cuenta de que alguien es irónico? Por ejemplo, alguien dice: «¡me encanta lavar platos!».', 'Por las pistas. Primera pista: el *contexto*, porque hay una pila enorme de platos.', 'Segunda: el *tono*, porque suspira mientras lo dice.', 'Tercera: la *exageración*: nadie dice «me encanta» de algo tan aburrido.', 'Las pistas muestran que piensa lo contrario de lo que dice.']},
 {'t': 'personaje', 'personaje': {'nombre': 'El narrador', 'emoji': '📖'}, 'lineas': [{'txt': 'El rey era tan valiente…', 'animo': 'feliz'}, {'txt': '…que se escondía bajo la cama cada vez que tronaba.', 'animo': 'ojo'}],
  'voz': ['En los textos literarios, a veces el que es irónico es el *narrador*: «el rey era tan valiente»…', '«…que se escondía bajo la cama cada vez que tronaba». El narrador elogia, pero en realidad se burla del rey.']},
 {'t': 'versus', 'a': {'txt': 'Ironía verbal', 'emoji': '💬', 'datos': ['está en lo que se dice', '«¡Qué día hermoso!» bajo la lluvia']}, 'b': {'txt': 'Ironía de situación', 'emoji': '🎭', 'datos': ['está en lo que pasa', 'el bombero cuya casa se incendia']}, 'gana': 'empate', 'veredicto': 'Dos tipos de ironía',
  'voz': ['Hay dos tipos de ironía. La *verbal* está en lo que se dice: elogiar un día de lluvia.', 'La *de situación* está en lo que pasa: lo contrario de lo esperable, como un bombero al que se le incendia la casa.', 'Una depende de las palabras; la otra, de los hechos.', 'Las dos rompen lo que esperamos.']},
 {'t': 'vof', 'afirmacion': 'Si una frase irónica se lee al pie de la letra, se entiende igual.', 'emoji': '📏', 'verdadero': False, 'explicacion': 'Al pie de la letra se entiende lo contrario de lo que se quiso decir.',
  'voz': ['Verdadero o falso: si una frase irónica se lee al pie de la letra, se entiende igual.', 'Pensalo con el ejemplo del día de playa.', 'Falso: leída al pie de la letra, se entiende justo lo contrario.']},
 {'t': 'resumen', 'items': [['Ironía', 'decir lo contrario de lo que se piensa'], ['Pistas', 'contexto, tono y exageración'], ['Ironía verbal', 'está en lo que se dice'], ['Ironía de situación', 'está en lo que pasa']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 2'},
  'voz': ['Repasemos.', 'La ironía pide un lector atento.', 'Decir lo contrario de lo que se piensa.', 'Reconocerla por el contexto, el tono y la exageración.', 'La ironía verbal.', 'Y la de situación. ¡A practicar!']},
]
CL['3'] = [
 {'t': 'noticia', 'cinta': 'INSÓLITO', 'titular': 'Un fantasma pide que no lo asusten', 'bajada': 'La familia nueva le ofreció aceite para sus cadenas', 'emoji': '👻', 'titulo': 'LA PARODIA', 'sub': 'imitar para burlarse',
  'voz': ['Insólito: un fantasma se queja de que la familia nueva del castillo no le tiene miedo.', 'Y encima, le ofrecieron aceite para que sus cadenas no hagan ruido.', 'Conocemos tanto las historias de fantasmas que, cuando se dan vuelta, nos reímos. Eso es una *parodia*.']},
 {'t': 'definicion', 'palabra': 'Parodia', 'texto': 'Imitación burlesca de una obra, un estilo o un género conocido, que copia su forma pero cambia el tono para hacer reír.', 'emoji': '🎭',
  'voz': ['Una *parodia* imita una obra, un estilo o un género conocido.', 'Copia su forma, pero cambia el tono: lo que era serio se vuelve ridículo.']},
 {'t': 'versus', 'a': {'txt': 'Relato de fantasmas', 'emoji': '🏚️', 'datos': ['castillo oscuro', 'el fantasma asusta', 'los vivos huyen']}, 'b': {'txt': 'Su parodia', 'emoji': '😂', 'datos': ['el mismo castillo', 'la familia asusta al fantasma', 'el fantasma huye']}, 'gana': 'empate', 'veredicto': 'Misma forma, tono invertido',
  'voz': ['Compará. En el relato de fantasmas tradicional hay un castillo oscuro, el fantasma asusta y los vivos huyen.', 'En la parodia, el castillo es el mismo, pero la familia asusta al fantasma, y el que huye es él.', 'La forma se mantiene; lo que se invierte es el *tono*.', 'Por eso para disfrutar una parodia hay que conocer el original.']},
 {'t': 'historieta', 'titulo': 'UNA ESCENA PARÓDICA', 'vinetas': [{'emojis': ['👻', '⛓️'], 'txt': '¡Uuuh! ¡Temblad, mortales!', 'quien': 'Fantasma'}, {'emojis': ['🧒', '🧴'], 'txt': 'Señor, ¿quiere aceite para esas cadenas?', 'quien': 'Niño'}, {'emojis': ['👻', '😤'], 'txt': '¡Esto es una falta de respeto!', 'quien': 'Fantasma'}],
  'voz': ['Mirá la escena. El fantasma aparece arrastrando cadenas y grita con voz terrorífica.', 'Un nene, sin miedo, le ofrece aceite para que las cadenas no rechinen.', 'Y el fantasma se ofende. Todos los elementos del terror están, pero dados vuelta.']},
 {'t': 'tabla', 'titulo': 'CÓMO SE ARMA UNA PARODIA', 'columnas': ['Recurso', 'Qué hace'], 'filas': [['Imitar', 'copia la forma del original'], ['Exagerar', 'agranda sus rasgos típicos'], ['Invertir', 'da vuelta lo esperado']],
  'voz': ['Tres recursos arman una parodia.', '*Imitar*: copiar la forma reconocible del original.', '*Exagerar*: agrandar sus rasgos típicos hasta volverlos ridículos.', '*Invertir*: dar vuelta lo que el lector espera.']},
 {'t': 'prediccion', 'pregunta': 'Alguien que nunca leyó un cuento de caballeros lee una parodia de caballeros. ¿La disfruta igual?', 'a': {'txt': 'Sí, igual', 'emoji': '😄'}, 'b': {'txt': 'Se pierde gran parte', 'emoji': '🤷'}, 'correcta': 'b', 'resultado': 'Sin conocer el original, no reconoce qué se imita ni qué se da vuelta.',
  'voz': ['¿Qué creés? Alguien que nunca leyó historias de caballeros lee una parodia de caballeros. ¿La disfruta igual?', 'Pensalo.', 'Se pierde gran parte: sin conocer el original, no reconoce qué se imita ni qué se da vuelta.']},
 {'t': 'errores', 'items': [{'mal': 'Una parodia es una copia', 'bien': 'Imita la forma, pero cambia el tono para hacer reír'}, {'mal': 'La parodia se burla de las personas', 'bien': 'Se burla de una obra, un estilo o un género'}],
  'voz': ['Dos confusiones.', 'Una parodia no es una copia: imita la forma, pero cambia el tono.', 'Y su blanco es una obra, un estilo o un género, no una persona.']},
 {'t': 'resumen', 'items': [['Parodia', 'imitación burlesca de algo conocido'], ['Imitar', 'copiar la forma'], ['Exagerar e invertir', 'agrandar y dar vuelta lo típico'], ['Lector', 'tiene que conocer el original']], 'fin': {'titulo': '¡A practicar!', 'sub': 'Nivel 3'},
  'voz': ['Repasemos.', 'La parodia es un juego entre dos textos: el original y su imitación.', 'La parodia.', 'Imitar.', 'Exagerar e invertir.', 'Y un lector que conoce el original. ¡A practicar!']},
]
CL['4'] = [
 {'t': 'historia', 'personaje': {'nombre': 'Doña Elvira', 'emoji': '👵'}, 'lugar': '🏙️', 'lineas': ['En un cuento, una ciudad prohíbe la lluvia por decreto.', 'Los funcionarios cobran multas a las nubes.'], 'titulo': 'LA SÁTIRA', 'sub': 'reírse para criticar',
  'voz': ['En un cuento, el intendente de una ciudad prohíbe la lluvia por decreto.', 'Y sus funcionarios salen a cobrarles multas a las nubes.', 'Nos reímos, pero el cuento también dice algo: se burla de los gobernantes que creen que todo se arregla con un papel. Eso es *sátira*.']},
 {'t': 'definicion', 'palabra': 'Sátira', 'texto': 'Texto que usa el humor para criticar defectos de las personas, las costumbres o la sociedad.', 'emoji': '🎯',
  'voz': ['La *sátira* usa el humor para criticar.', 'Su blanco son los defectos de las personas, las costumbres o la sociedad: la risa tiene una intención.']},
 {'t': 'matriz', 'titulo': 'BLANCOS DE LA SÁTIRA', 'celdas': [{'cab': 'Costumbres', 'txt': 'las modas, el qué dirán'}, {'cab': 'Autoridades', 'txt': 'los que mandan y abusan'}, {'cab': 'Defectos', 'txt': 'la avaricia, la vanidad'}, {'cab': 'Grupos sociales', 'txt': 'los nuevos ricos, los snobs'}],
  'voz': ['¿De qué se burla la sátira?', 'De las *costumbres*: las modas, el qué dirán.', 'De las *autoridades* que abusan de su poder.', 'De *defectos* humanos, como la avaricia o la vanidad.', 'Y de *grupos sociales* que se creen superiores.']},
 {'t': 'venn', 'a': 'Parodia', 'b': 'Sátira', 'itemsA': ['imita una obra o género'], 'itemsB': ['critica la sociedad'], 'ambos': ['usan el humor', 'exageran'],
  'voz': ['Parodia y sátira se parecen, pero no son lo mismo.', 'La parodia imita una obra o un género.', 'La sátira critica a la sociedad o a las personas.', 'Las dos usan el humor y la exageración, y muchas veces aparecen juntas en el mismo texto.']},
 {'t': 'quiz4', 'pregunta': 'Un cuento muestra a un millonario que compra un castillo y quiere arreglar todo con productos de marca. ¿Qué critica?', 'opciones': ['La confianza ciega en el dinero', 'Los castillos antiguos', 'La lluvia', 'Nada: es solo un cuento'], 'correcta': 0,
  'voz': ['Pregunta: un cuento muestra a un millonario que compra un castillo y cree que todo se arregla con productos de marca. ¿Qué critica?', 'Pensá de qué se burla.', 'La confianza ciega en el dinero: esa es la *crítica* detrás del humor.']},
 {'t': 'consejo', 'titulo': 'PARA LEER SÁTIRA', 'texto': 'Después de reírte, preguntate: ¿de qué se está burlando este texto y por qué?', 'emoji': '💡',
  'voz': ['Un consejo para leer sátira: después de reírte, preguntate de qué se está burlando el texto y por qué.']},
 {'t': 'logro', 'titulo': '¡Misión cumplida!', 'items': ['Los recursos del humor', 'La ironía', 'La parodia', 'La sátira'], 'xp': 100,
  'voz': ['¡Terminaste las clases de la misión!', 'Ya reconocés los recursos del humor.', 'Sabés leer la ironía.', 'Entendés cómo funciona una parodia.', 'Y descubrís la crítica que esconde la sátira. ¡A practicar!']},
]
for n, esc in CL.items():
    json.dump({'slug': f'leng1-m6-n{n}', 'step_id': STEP[n], 'materia': 'Lengua y Literatura I', 'titulo': TIT[n], 'sub': f'Lengua y Literatura I · Misión 6 · Nivel {n}', 'escenas': esc},
              open(os.path.join(RAIZ, 'tools/clase/lecciones', f'leng1-m6-n{n}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ============================ LECCIÓN ============================
L = {}
L['1'] = {'temas': [
 T('Lo inesperado: la incongruencia',
   m('marcar', rotulo='Escena', items=[
     {'nombre': 'El héroe', 'texto': '{{El caballero entró al castillo, levantó la espada y gritó: «¡Que salga el dragón!»|Expectativa: todo anuncia una gran batalla.}} {{Salió una lagartija, lo miró y se fue a tomar sol|Giro: lo que pasa no tiene nada que ver con lo esperado.}}.', 'cierre': 'El choque entre lo anunciado y lo que pasa produce la risa.'},
     {'nombre': 'La mudanza', 'texto': '{{Para no perder nada en la mudanza, Ana guardó todo en cajas numeradas y anotó cada número en una lista|Expectativa: el orden va a resolver el problema.}}. {{Lo único que perdió fue la lista|Giro: la solución se vuelve el problema.}}.', 'cierre': 'El texto prepara una expectativa y la rompe al final.'}]),
   m('elegir_x', consigna='¿Dónde está el giro que hace reír?', items=[
     {'cons': '«El mago anunció su mejor truco: iba a hacer desaparecer un elefante. Lo único que desapareció fue el público.»', 'ops': ['En que desaparece el público y no el elefante', 'En que el mago tiene un elefante', 'En que el mago anuncia un truco'], 'ayuda': 'Buscá lo que no coincide con lo anunciado.'},
     {'cons': '«Después de un mes de dieta estricta, Raúl festejó los dos kilos perdidos con una torta de chocolate entera.»', 'ops': ['En que festeja la dieta comiendo una torta', 'En que hizo dieta durante un mes', 'En que bajó dos kilos'], 'ayuda': 'Pensá qué esperabas que hiciera.'},
     {'cons': '«El guardia más atento del museo vigiló toda la noche la puerta principal. El ladrón entró por la ventana.»', 'ops': ['En que tanta vigilancia no sirvió de nada', 'En que el guardia era atento', 'En que el museo tiene una puerta'], 'ayuda': 'La atención termina siendo inútil.'}]),
   ('Incongruencia', 'La incongruencia es el choque entre lo que el lector espera y lo que finalmente ocurre en el texto; es el mecanismo básico del humor.'),
   'Un texto humorístico arma una expectativa con mucho cuidado, a veces con varias oraciones, y la rompe en el último momento. Si el giro llega demasiado pronto o se anuncia antes, el efecto se pierde: por eso el humor depende tanto del orden en que se cuentan las cosas.',
   ['Se arma una expectativa.', 'Se rompe con un giro inesperado.', 'El orden de lo que se cuenta es clave.']),
 T('La exageración',
   m('versiones', rotulo='Versión', items=[
     {'nombre': 'Dato', 'texto': '{{Mi tío habla bastante.|Información sin humor.}}'},
     {'nombre': 'Exagerada', 'texto': '{{Mi tío habla tanto que los loros del barrio le piden que se calle.|La exageración agranda el rasgo hasta lo absurdo.}}'},
     {'nombre': 'Dato', 'texto': '{{La casa era vieja.|Información sin humor.}}'},
     {'nombre': 'Exagerada', 'texto': '{{La casa era tan vieja que los fantasmas se quejaban de las goteras.|El rasgo se lleva al extremo y aparece la risa.}}'}]),
   m('clasificar_x', consigna='¿La frase informa o exagera con humor?', cajas=['Informa', 'Exagera con humor'], cuantos=6, items=[
     ['El colectivo tardó veinte minutos.', 0], ['Mi perro duerme muchas horas por día.', 0], ['La heladera estaba casi vacía.', 0],
     ['El colectivo tardó tanto que llegué con barba.', 1], ['Mi perro duerme tanto que el veterinario lo dio por jubilado.', 1], ['En la heladera había un eco.', 1]]),
   ('Exageración', 'La exageración, o hipérbole, es el recurso que agranda un rasgo, una situación o una cantidad mucho más allá de lo real para producir un efecto, como la risa.'),
   'La exageración humorística no busca engañar: todos saben que nadie llega con barba por esperar un colectivo. Funciona porque el lector reconoce el rasgo real que hay detrás, la demora, y disfruta de verlo llevado al absurdo.',
   ['Agranda un rasgo real.', 'Lo lleva hasta lo imposible.', 'El lector sabe que no es literal.']),
 T('El juego de palabras',
   m('marcar', rotulo='Chiste', items=[
     {'nombre': 'El banco', 'texto': '—¿Por qué fuiste al banco de la plaza a pedir un préstamo? —{{Porque decía «banco»|Juego de palabras: «banco» es un asiento y también una entidad que presta dinero.}}.', 'cierre': 'Una misma palabra, dos sentidos.'},
     {'nombre': 'La planta', 'texto': '—Trabajo en una {{planta|Doble sentido: una fábrica o un vegetal.}}. —¿Y qué hacés? —{{La riego todos los días|El segundo sentido aparece y sorprende.}}.', 'cierre': 'El humor nace del cambio de sentido.'}]),
   m('unir_x', consigna='Uní cada palabra con sus dos sentidos.', items=[
     {'pares': [['Gato', 'animal / herramienta para levantar el auto'], ['Sierra', 'herramienta para cortar / cadena de montañas'], ['Cometa', 'juguete que vuela / astro con cola'], ['Muñeca', 'juguete / parte del brazo']]},
     {'pares': [['Lima', 'fruta / herramienta para limar'], ['Vela', 'objeto que ilumina / tela de un barco'], ['Copa', 'vaso con pie / parte alta de un árbol'], ['Hoja', 'de un árbol / de papel']]}]),
   ('Juego de palabras', 'El juego de palabras es el recurso que aprovecha que una palabra o una frase tiene más de un sentido para producir humor o sorpresa.'),
   'Muchas palabras del español tienen varios significados, y el humor los hace chocar: la frase se entiende de una manera y, de golpe, aparece la otra. Para disfrutarlo hay que conocer los dos sentidos; por eso los juegos de palabras casi nunca se pueden traducir a otro idioma.',
   ['Una palabra con dos sentidos.', 'Se entiende uno y aparece el otro.', 'Es muy difícil de traducir.'])],
 'recuerda': [
   R('Humor', 'es un modo de contar o mirar las cosas que busca provocar risa, casi siempre rompiendo lo esperado.', 'Anoté todo para no olvidarme y perdí el papel'),
   R('Incongruencia', 'es el choque entre lo que el lector espera y lo que finalmente ocurre en el texto.', 'El caballero espera un dragón y sale una lagartija'),
   R('Exageración', 'es agrandar un rasgo o una situación mucho más allá de lo real para producir un efecto.', 'Tardó tanto que llegué con barba'),
   R('Juego de palabras', 'aprovecha que una palabra tiene dos sentidos para sorprender al lector.', 'Pedir un préstamo en el banco de la plaza'),
   R('Giro final', 'es el momento en que el texto rompe la expectativa que había armado, casi siempre al final.', 'Lo único que desapareció fue el público')]}

L['2'] = {'temas': [
 T('Qué es la ironía',
   m('versiones', rotulo='Frase', items=[
     {'nombre': 'Literal', 'texto': '{{«¡Qué rápido llegaste!»|Dicho a alguien que corrió y llegó primero: significa lo que dice.}}'},
     {'nombre': 'Irónica', 'texto': '{{«¡Qué rápido llegaste!»|Dicho a alguien que llegó dos horas tarde: significa lo contrario.}}'},
     {'nombre': 'Literal', 'texto': '{{«Gran idea»|Dicho después de una propuesta que salió bien.}}'},
     {'nombre': 'Irónica', 'texto': '{{«Gran idea»|Dicho después de que alguien propuso un picnic y se largó a llover.}}'}]),
   m('elegir_x', consigna='¿Qué quiere decir en realidad quien habla?', items=[
     {'cons': 'Tu hermano rompió el tercer vaso de la semana y tu mamá le dice: «Muy bien, seguí así».', 'ops': ['Que deje de romper vasos', 'Que siga rompiendo vasos', 'Que está contenta con él'], 'ayuda': 'Pensá en el contexto: tres vasos rotos.'},
     {'cons': 'Llegás empapado y tu amigo te dice: «Veo que trajiste el paraguas».', 'ops': ['Que no trajiste el paraguas', 'Que el paraguas es lindo', 'Que el paraguas funcionó'], 'ayuda': 'Estás empapado: ¿lo trajiste?'},
     {'cons': 'El equipo perdió diez a cero y el técnico dice: «Fue un partido parejo».', 'ops': ['Que fue una paliza', 'Que fue muy equilibrado', 'Que el árbitro ayudó'], 'ayuda': 'Diez a cero no es parejo.'}]),
   ('Ironía', 'La ironía es el recurso que consiste en decir lo contrario de lo que se piensa, confiando en que el oyente o el lector entienda el verdadero sentido.'),
   'La ironía tiene dos capas: lo que se dice y lo que se quiere decir. Si el lector se queda con la primera, entiende justo lo contrario. Por eso es un recurso que pide complicidad: quien la usa confía en que el otro comparte el contexto y se va a dar cuenta.',
   ['Dice lo contrario de lo que piensa.', 'Tiene dos capas: lo dicho y lo querido.', 'Pide un lector cómplice.']),
 T('Cómo se reconoce la ironía',
   m('marcar', rotulo='Texto', items=[
     {'nombre': 'La fiesta', 'texto': '{{Llegamos a la fiesta a las diez y nos fuimos a las diez y cuarto|Contexto: la fiesta duró nada.}}. «{{¡Fue la noche más larga de mi vida!»|Lo dicho choca con el contexto: es irónico.}}, {{dijo Clara, bostezando|Tono: el bostezo muestra aburrimiento.}}.', 'cierre': 'Contexto + tono revelan la ironía.'},
     {'nombre': 'El narrador', 'texto': 'El señor Gómez era {{generosísimo|Exageración: anuncia que algo no cierra.}}: {{una vez por año le prestaba un lápiz a su vecino, y se lo cobraba|Los hechos contradicen el elogio.}}.', 'cierre': 'El narrador elogia, pero los hechos dicen lo contrario.'}]),
   m('marcar_x', consigna='Tocá solo las frases irónicas.', items=[
     {'cons': 'Contexto: es el día más caluroso del año y se cortó la luz.', 'texto': '[[«¡Qué fresquito está hoy!»|1]] · [[«Qué calor insoportable.»|0]] · [[«Justo hoy, ideal para estar sin ventilador.»|1]] · [[«Voy a buscar agua fría.»|0]]'},
     {'cons': 'Contexto: el examen fue dificilísimo y casi nadie aprobó.', 'texto': '[[«Fue un examen regalado.»|1]] · [[«Me costó muchísimo.»|0]] · [[«El profe se lució con su generosidad.»|1]] · [[«Tengo que estudiar más.»|0]]'}]),
   ('Pistas de la ironía', 'Las pistas de la ironía son las señales que avisan que una frase no se debe leer al pie de la letra: el contexto, el tono y la exageración.'),
   'En la conversación, el tono de voz y los gestos ayudan mucho. En la escritura esas pistas desaparecen, y el lector tiene que fijarse en el contexto: si lo que se dice choca con lo que pasa, o si un elogio es tan exagerado que suena falso, probablemente sea ironía.',
   ['Contexto: lo dicho choca con lo que pasa.', 'Tono: un suspiro, un bostezo, un gesto.', 'Exageración: un elogio que suena falso.']),
 T('La ironía de situación',
   m('esquema', items=[
     {'nombre': 'El bombero', 'raiz': 'Ironía de situación: un bombero', 'ramas': [['Lo esperable', ['que sepa evitar los incendios'], 'Es su trabajo.'], ['Lo que pasa', ['se le quema la casa por dejar la pava al fuego'], 'Ocurre justo lo contrario.'], ['El efecto', ['sorpresa y una sonrisa amarga'], 'La situación misma es irónica.']], 'cierre': 'Nadie dice nada irónico: la ironía está en los hechos.'},
     {'nombre': 'El reloj', 'raiz': 'Ironía de situación: el relojero', 'ramas': [['Lo esperable', ['que llegue siempre puntual'], 'Vive de los relojes.'], ['Lo que pasa', ['es el único que llega tarde a todos lados'], 'Lo contrario de lo esperado.'], ['El efecto', ['humor que nace de la situación'], 'No hace falta ningún comentario.']], 'cierre': 'Los hechos contradicen lo esperable.'}]),
   m('clasificar_x', consigna='¿Ironía verbal o ironía de situación?', cajas=['Ironía verbal', 'Ironía de situación'], cuantos=6, items=[
     ['Bajo una tormenta, alguien dice: «Hermoso día para tomar sol».', 0], ['Al ver una nota de 2, el chico dice: «Soy un genio».', 0], ['Ante un plato quemado, la cocinera dice: «Me salió perfecto».', 0],
     ['El profesor de Lengua tiene una falta de ortografía en el cartel de su clase.', 1], ['El ladrón de autos denuncia que le robaron el auto.', 1], ['La campaña contra el ruido se lanza con una banda de música a todo volumen.', 1]]),
   ('Ironía de situación', 'La ironía de situación se produce cuando los hechos resultan lo contrario de lo esperable, aunque nadie diga nada irónico.'),
   'En la ironía verbal, la contradicción está en las palabras; en la de situación, está en lo que pasa. Los cuentos humorísticos usan mucho la ironía de situación: preparan un personaje o un plan y hacen que todo salga al revés, justo de la manera que menos se esperaba.',
   ['Verbal: está en lo que se dice.', 'De situación: está en lo que pasa.', 'Las dos contradicen lo esperable.'])],
 'recuerda': [
   R('Ironía', 'es decir lo contrario de lo que se piensa, confiando en que el otro entienda el verdadero sentido.', '«¡Qué puntual!» a alguien que llegó una hora tarde'),
   R('Pistas de la ironía', 'son el contexto, el tono y la exageración, que avisan que no hay que leer al pie de la letra.', '«¡Fue la noche más larga!», dicho bostezando'),
   R('Ironía verbal', 'es la que está en lo que se dice: las palabras contradicen lo que se piensa.', '«Hermoso día para tomar sol» bajo una tormenta'),
   R('Ironía de situación', 'es la que está en los hechos: ocurre lo contrario de lo esperable.', 'Al bombero se le quema la casa'),
   R('Narrador irónico', 'es el que elogia o comenta algo mientras los hechos muestran lo contrario.', 'El señor Gómez era generosísimo: cobraba el lápiz')]}

L['3'] = {'temas': [
 T('Qué es una parodia',
   m('esquema', items=[{'nombre': 'Original y parodia', 'cols': ['', 'Original', 'Parodia'], 'filas': [
       ['Cuento de hadas', 'el príncipe rescata a la princesa', 'la princesa rescata al príncipe, que se cayó del caballo'], ['Noticiero', 'voz seria y datos importantes', 'voz seria y datos ridículos: «Un gato fue elegido intendente»'],
       ['Relato de terror', 'el monstruo asusta a todos', 'el monstruo le tiene miedo a la oscuridad']],
     'cierre': 'La parodia conserva la forma reconocible y cambia el tono.'}]),
   m('elegir_x', consigna='¿Qué se está parodiando?', items=[
     {'cons': '«Había una vez una princesa que esperó cien años a su príncipe. Cuando llegó, le dijo: "Llegaste tarde, ya me arreglé sola".»', 'ops': ['Los cuentos de hadas', 'Las noticias', 'Las recetas de cocina'], 'ayuda': 'Fijate en la fórmula «había una vez» y en los personajes.'},
     {'cons': '«Último momento: con lágrimas en los ojos, el ministro anunció que la medialuna de grasa será declarada patrimonio nacional.»', 'ops': ['Los noticieros', 'Los poemas de amor', 'Las fábulas'], 'ayuda': 'La forma es la de un informe urgente.'},
     {'cons': '«Ingredientes: un lunes, dos alarmas que no sonaron y una pizca de mal humor. Mezclar todo y servir a las 8.»', 'ops': ['Las recetas de cocina', 'Los cuentos policiales', 'Las cartas formales'], 'ayuda': 'Reconocé la forma del texto.'}]),
   ('Parodia', 'La parodia es la imitación burlesca de una obra, un estilo o un género conocido: copia su forma reconocible, pero cambia el tono para producir humor.'),
   'Para que una parodia funcione, el lector tiene que reconocer el original: la gracia está en ver lo conocido dado vuelta. Por eso las parodias suelen elegir textos o géneros muy famosos, como los cuentos de hadas, los noticieros o las historias de terror.',
   ['Imita una forma conocida.', 'Cambia el tono: de serio a ridículo.', 'El lector tiene que conocer el original.']),
 T('Parodiar un género',
   m('marcar', rotulo='Fragmento', items=[
     {'nombre': 'El castillo', 'texto': '{{Era una noche oscura y tormentosa. En lo alto de la colina se alzaba el castillo maldito|Imita el comienzo típico del relato de terror.}}. {{El fantasma arrastró sus cadenas por el pasillo y lanzó un aullido espantoso|Rasgos del género: cadenas, aullidos, oscuridad.}}. {{Desde un cuarto, una voz soñolienta gritó: «¡Bajá el volumen, que mañana trabajo!»|Inversión: los vivos no se asustan, se molestan.}}.', 'cierre': 'Todo el terror está, pero el efecto es risa.'},
     {'nombre': 'El vampiro', 'texto': '{{El conde abrió el ataúd a medianoche y desplegó su capa negra|Imita el relato de vampiros.}}. {{Se miró en el espejo para arreglarse el peinado y, como siempre, no se vio|Exagera un rasgo del género hasta lo ridículo.}}. {{Salió a la noche despeinado y de mal humor|Lo terrorífico se vuelve cotidiano.}}.', 'cierre': 'El rasgo del vampiro se convierte en problema doméstico.'}]),
   m('clasificar_x', consigna='¿Es un rasgo del relato de terror o un giro paródico?', cajas=['Rasgo del terror', 'Giro paródico'], cuantos=6, items=[
     ['Una casa abandonada en lo alto de una colina', 0], ['Pasos que se oyen en el pasillo a medianoche', 0], ['Un fantasma que arrastra cadenas', 0],
     ['El fantasma pide que le bajen la música', 1], ['La bruja se queja de que su escoba no tiene garantía', 1], ['El hombre lobo va al peluquero todos los meses', 1]]),
   ('Parodia de género', 'La parodia de género imita los rasgos típicos de un tipo de relato, como el terror, el policial o el cuento de hadas, y los exagera o los invierte para hacer reír.'),
   'Cada género tiene rasgos que los lectores ya esperan: el castillo y las cadenas en el terror, el príncipe y el «había una vez» en los cuentos de hadas. La parodia los usa porque son reconocibles, y después los da vuelta. Así, además de hacer reír, muestra cuán repetidos pueden ser esos rasgos.',
   ['Toma los rasgos típicos del género.', 'Los exagera o los invierte.', 'Muestra lo previsible del original.']),
 T('Un clásico paródico: el Quijote',
   m('marcar', rotulo='Episodio', items=[
     {'nombre': 'Los molinos', 'texto': '{{Don Quijote ha leído tantos libros de caballería que decide hacerse caballero andante|Imita al héroe de esos libros.}}. {{Al ver unos molinos de viento, cree que son gigantes y los ataca con su lanza|Exageración: confunde la realidad con las aventuras de los libros.}}. {{Un aspa lo levanta y lo tira al suelo, todo dolorido|Giro: el héroe termina golpeado y ridículo.}}.', 'cierre': 'La novela de Cervantes (1605) parodia los libros de caballería.'},
     {'nombre': 'La dama', 'texto': '{{Como todo caballero necesita una dama a quien dedicar sus hazañas|Imita una regla de los libros de caballería.}}, {{don Quijote elige a una campesina del pueblo vecino y la llama Dulcinea del Toboso|Inversión: la gran dama es una vecina común.}}.', 'cierre': 'Los rasgos del género se vuelven ridículos en el mundo real.'}]),
   m('elegir_x', consigna='Pensá en cómo funciona la parodia en el Quijote.', items=[
     {'cons': '¿Qué género parodia «Don Quijote de la Mancha»?', 'ops': ['Los libros de caballería', 'Las novelas policiales', 'Los relatos de terror'], 'ayuda': 'Don Quijote quiere ser caballero andante.'},
     {'cons': '¿Por qué el ataque a los molinos es paródico?', 'ops': ['Porque el héroe pelea contra enemigos imaginarios y pierde', 'Porque los molinos eran gigantes de verdad', 'Porque don Quijote gana la batalla'], 'ayuda': 'Compará con lo que hace un caballero de los libros.'},
     {'cons': 'Un lector de 1605 que conocía muchos libros de caballería, ¿qué disfrutaba más?', 'ops': ['Reconocer las reglas del género dadas vuelta', 'Aprender a pelear con lanza', 'Conocer los molinos de La Mancha'], 'ayuda': 'La parodia necesita un lector que conozca el original.'}]),
   ('Don Quijote', 'Don Quijote de la Mancha, de Miguel de Cervantes, es una novela de 1605 que parodia los libros de caballería a través de un hidalgo que se cree caballero andante.'),
   'Cervantes imita la forma de esos libros, con el héroe, la dama, los combates y las aventuras, pero los ubica en el mundo real, donde todo sale mal. Lo que empezó como una parodia terminó siendo una de las novelas más importantes de la literatura, porque además de hacer reír muestra el choque entre los sueños y la realidad.',
   ['Imita los libros de caballería.', 'Los pone en el mundo real, donde todo sale mal.', 'Es un clásico de la parodia.'])],
 'recuerda': [
   R('Parodia', 'es la imitación burlesca de una obra, un estilo o un género conocido, que cambia su tono para hacer reír.', 'La princesa rescata al príncipe que se cayó del caballo'),
   R('Imitar', 'es copiar la forma reconocible del original para que el lector la identifique.', '«Era una noche oscura y tormentosa…»'),
   R('Invertir', 'es dar vuelta lo que el lector espera del original, como cambiar quién asusta a quién.', 'El fantasma se asusta de la familia'),
   R('Parodia de género', 'imita los rasgos típicos de un tipo de relato y los exagera o los invierte.', 'El hombre lobo va al peluquero'),
   R('Lector de parodias', 'tiene que conocer el original para reconocer qué se imita y qué se da vuelta.', 'Sin conocer los libros de caballería, el Quijote pierde gracia'),
   R('Don Quijote', 'es la novela de Cervantes de 1605 que parodia los libros de caballería.', 'Ataca molinos creyendo que son gigantes')]}

L['4'] = {'temas': [
 T('Qué es la sátira',
   m('marcar', rotulo='Texto', items=[
     {'nombre': 'El decreto', 'texto': '{{El intendente firmó un decreto que prohibía la lluvia los fines de semana|Exageración absurda.}}. {{Cuando llovió igual, multó a las nubes y anunció que el problema estaba resuelto|Burla de las autoridades que creen que todo se arregla con papeles.}}.', 'cierre': 'Nos reímos, y a la vez el texto critica una forma de gobernar.'},
     {'nombre': 'La selfie', 'texto': '{{Martina se sacó doscientas fotos en el atardecer más lindo del año|Exagera una costumbre actual.}}. {{Cuando terminó de elegir la mejor, ya era de noche y no había visto el atardecer|Critica: por mirar la pantalla, se perdió lo real.}}.', 'cierre': 'La sátira apunta a una costumbre de la sociedad.'}]),
   m('elegir_x', consigna='¿Qué critica cada texto satírico?', items=[
     {'cons': 'En un cuento, un empresario vende aire embotellado «de montaña» y la gente hace fila para comprarlo.', 'ops': ['El consumo de cosas inútiles por moda', 'El cuidado del medio ambiente', 'El turismo en la montaña'], 'ayuda': 'Pensá de quiénes se burla el cuento.'},
     {'cons': 'Una historieta muestra una oficina donde para pedir un formulario hay que presentar el mismo formulario completo.', 'ops': ['Los trámites absurdos y la burocracia', 'El trabajo en oficinas', 'El uso del papel'], 'ayuda': 'La situación es imposible a propósito.'},
     {'cons': 'Un relato cuenta que en un pueblo todos opinan sobre la vida de los vecinos, pero nadie limpia su propia vereda.', 'ops': ['El chisme y la hipocresía', 'La limpieza de las calles', 'La vida en los pueblos'], 'ayuda': 'Fijate en el defecto que muestra.'}]),
   ('Sátira', 'La sátira es el texto o el recurso que usa el humor, sobre todo la exageración y la ironía, para criticar defectos de las personas, las costumbres o la sociedad.'),
   'La sátira se ríe, pero no solo para divertir: quiere mostrar algo que está mal. Por eso, para leerla bien, no alcanza con reírse; hay que preguntarse de qué se está burlando el texto y qué propone pensar. Sus blancos suelen ser las autoridades, las modas y los defectos humanos.',
   ['Usa el humor para criticar.', 'Blancos: autoridades, costumbres, defectos.', 'Preguntá: ¿de qué se burla y por qué?']),
 T('Caricatura y estereotipo',
   m('versiones', rotulo='Personaje', items=[
     {'nombre': 'Realista', 'texto': '{{Don Aurelio es un comerciante cuidadoso con el dinero; ahorra para su vejez y a veces le cuesta gastar.|Un personaje con matices.}}'},
     {'nombre': 'Caricatura', 'texto': '{{Don Aurelio es tan tacaño que apaga la luz para no gastar mientras cuenta las monedas, y las cuenta de memoria para no gastar la vista.|Un solo rasgo, exagerado hasta el absurdo.}}'}]),
   m('clasificar_x', consigna='¿Personaje con matices o caricatura?', cajas=['Con matices', 'Caricatura'], cuantos=6, items=[
     ['Una abuela cariñosa que a veces pierde la paciencia con sus nietos', 0], ['Un profesor exigente que también sabe escuchar', 0], ['Una vecina curiosa, pero solidaria cuando hace falta', 0],
     ['Un millonario que pregunta el precio del aire antes de respirar', 1], ['Una estrella de cine que no sale de su casa sin cinco espejos', 1], ['Un político que promete un puente donde no hay río', 1]]),
   ('Caricatura', 'La caricatura es el retrato de un personaje que exagera uno o dos de sus rasgos hasta volverlo ridículo; la sátira la usa para burlarse de un tipo de persona.'),
   'Muchas veces la caricatura representa un estereotipo: el avaro, el vanidoso, el político mentiroso. No es un personaje complejo, sino un tipo reconocible. Hay que leerla con cuidado: la buena sátira apunta a conductas y a quienes tienen poder, y no a burlarse de alguien por lo que es.',
   ['Exagera uno o dos rasgos.', 'Representa un tipo de persona.', 'La buena sátira apunta a conductas, no a quién es alguien.']),
 T('Parodia y sátira juntas',
   m('esquema', items=[{'nombre': 'Diferencias', 'cols': ['', 'Parodia', 'Sátira'], 'filas': [
       ['¿Qué imita o critica?', 'una obra, un estilo o un género', 'personas, costumbres o la sociedad'], ['¿Para qué?', 'para jugar con lo conocido', 'para mostrar algo que está mal'],
       ['Recursos', 'imitar, exagerar, invertir', 'exagerar, ironía, caricatura'], ['Juntas', 'muchas obras parodian un género…', '…y a la vez critican la sociedad']],
     'cierre': 'Un mismo texto puede ser parodia y sátira a la vez.'}]),
   m('clasificar_x', consigna='¿Parodia, sátira o las dos?', cajas=['Parodia', 'Sátira', 'Las dos'], cuantos=6, items=[
     ['Un cuento de hadas donde el lobo es vegetariano', 0], ['Un poema que imita a un poeta famoso para jugar con su estilo', 0],
     ['Una historieta sobre funcionarios que cobran por no trabajar', 1], ['Un cuento que se burla de los que gastan todo para aparentar', 1],
     ['Un falso noticiero que imita el formato del noticiero para criticar a los políticos', 2], ['Un relato de fantasmas donde una familia rica cree que todo se arregla comprando productos', 2]]),
   ('Parodia y sátira', 'La parodia imita una obra o un género para jugar con él, y la sátira critica a las personas o la sociedad; muchas obras combinan las dos.'),
   'Cuando un texto imita un género conocido y, además, usa esa imitación para burlarse de un grupo social o de una costumbre, es parodia y sátira al mismo tiempo. Reconocer las dos capas permite leer mejor: primero, qué se imita; después, qué se critica.',
   ['Parodia: juega con una obra o género.', 'Sátira: critica a la sociedad.', 'Muchas obras hacen las dos cosas.'])],
 'recuerda': [
   R('Sátira', 'usa el humor, sobre todo la exageración y la ironía, para criticar defectos de las personas o la sociedad.', 'El intendente que multa a las nubes'),
   R('Blancos de la sátira', 'suelen ser las autoridades, las costumbres de una época y los defectos humanos.', 'La burocracia, las modas, la avaricia'),
   R('Caricatura', 'es un retrato que exagera uno o dos rasgos de un personaje hasta volverlo ridículo.', 'El tacaño que cuenta monedas a oscuras'),
   R('Estereotipo', 'es un tipo de persona reconocible y simplificado, como el avaro o el vanidoso.', 'El político que promete un puente sin río'),
   R('Parodia y sátira', 'la parodia imita una obra o un género; la sátira critica a la sociedad, y pueden aparecer juntas.', 'Un falso noticiero que critica a los políticos')]}

# ============================ ACTIVIDADES ============================
A = {
 '1': [
   CLA('¿Qué recurso del humor usa cada frase?', ['Lo inesperado', 'Exageración', 'Juego de palabras'], [('Estudió toda la noche para la prueba y se quedó dormido en el examen', 'Lo inesperado'), ('Mi abuela cocina tanto que los vecinos engordan por el olor', 'Exageración'), ('—¿Tenés hora? —Sí. —¿Me la decís? —No, es mía', 'Juego de palabras'), ('El cerrajero quedó encerrado en su propio negocio', 'Lo inesperado')], 'Pensá qué hace reír en cada caso.', 'aplicar'),
   UNI('Uní cada frase con el rasgo real que exagera.', [('Hacía tanto frío que los pingüinos pedían estufa', 'mucho frío'), ('Habla tan bajo que los susurros le parecen gritos', 'voz muy baja'), ('Es tan alto que saluda a los aviones', 'gran altura'), ('El auto es tan viejo que tiene permiso de los dinosaurios', 'mucha antigüedad')], 'Detrás de cada exageración hay un rasgo verdadero.', 'aplicar'),
   ODD('Tres frases usan humor y una solo informa. ¿Cuál informa?', ['El tren llegó cuarenta minutos tarde.', 'El tren tardó tanto que los pasajeros festejaron cumpleaños.', 'Esperé el tren hasta que me crecieron raíces.', 'El tren era tan lento que lo pasaban los caracoles.'], 'El tren llegó cuarenta minutos tarde.', 'Las otras tres exageran el rasgo hasta el absurdo.', 'analizar'),
   MC('Un compañero dice: «En "Esperé tanto que me salieron canas" hay una mentira, así que es un error del texto». ¿Qué le contestás?', ['Es una exageración: nadie la toma al pie de la letra', 'Tiene razón: es un error del autor', 'Es un juego de palabras con «canas»'], 'Es una exageración: nadie la toma al pie de la letra', 'La exageración humorística no busca engañar.', 'error')],
 '2': [
   CLA('Leé cada situación. ¿La frase es irónica o literal?', ['Irónica', 'Literal'], [('Tu equipo ganó 5 a 0 y decís: «¡Qué partidazo!»', 'Literal'), ('Se te quema la comida y decís: «Soy un chef de primera»', 'Irónica'), ('Sacaste 10 y tu mamá dice: «¡Qué orgullo!»', 'Literal'), ('Llueve en tu cumpleaños al aire libre y decís: «Día perfecto»', 'Irónica')], 'Compará lo dicho con el contexto.', 'aplicar'),
   TAP('Tocá las DOS pistas que muestran que la frase es irónica: «Juan llegó a las once a una cita de las nueve. "¡Siempre tan puntual!", dijo Sara, mirando el reloj y suspirando.»', ['Juan llegó a las once', 'a una cita de las nueve.', '«¡Siempre tan puntual!»,', 'dijo Sara,', 'mirando el reloj', 'y suspirando.'], [0, 5], 'El contexto (llegó dos horas tarde) y el tono (el suspiro).', 'analizar'),
   CLA('¿Ironía verbal o de situación?', ['Verbal', 'De situación'], [('El dentista tiene todos los dientes picados', 'De situación'), ('Ante una nota baja, alguien dice: «Soy un genio»', 'Verbal'), ('La escuela de manejo choca su propio auto', 'De situación'), ('Ante una tormenta, alguien dice: «Lindo día»', 'Verbal')], 'En las palabras o en los hechos.', 'analizar'),
   MC('Sofía lee: «El señor era tan generoso que prestaba su lápiz una vez por año, y lo cobraba». Ella entiende que el señor era muy generoso. ¿Qué no tuvo en cuenta?', ['Que el narrador es irónico: los hechos lo contradicen', 'Que el lápiz era muy caro', 'Que el señor no tenía lápiz'], 'Que el narrador es irónico: los hechos lo contradicen', 'Leyó al pie de la letra un elogio irónico.', 'error')],
 '3': [
   UNI('Uní cada parodia con el género que imita.', [('«Había una vez un dragón que tenía miedo de los caballeros»', 'cuento de hadas'), ('«Último momento: un perro fue elegido presidente del club»', 'noticiero'), ('«Ingredientes: dos lunes y una alarma rota»', 'receta'), ('«Era una noche oscura y el fantasma no encontraba sus cadenas»', 'relato de terror')], 'Reconocé la forma que se imita.', 'aplicar'),
   CLA('En una parodia del relato de vampiros, ¿qué es un rasgo del género y qué es el giro paródico?', ['Rasgo del género', 'Giro paródico'], [('El conde duerme en un ataúd', 'Rasgo del género'), ('El conde no puede dormir porque el ataúd le aprieta', 'Giro paródico'), ('Sale de noche con su capa negra', 'Rasgo del género'), ('La capa se le engancha en la puerta y se cae', 'Giro paródico')], 'Lo que se imita y lo que se da vuelta.', 'analizar'),
   MC('¿Por qué el ataque de don Quijote a los molinos es un buen ejemplo de parodia?', ['Imita los combates de los caballeros, pero sale ridículo', 'Cuenta un combate verdadero de la Edad Media', 'Explica cómo funcionan los molinos de viento'], 'Imita los combates de los caballeros, pero sale ridículo', 'La forma del combate heroico se mantiene y el resultado se invierte.', 'analizar'),
   MC('Lautaro dice que una parodia es lo mismo que copiar un texto. ¿Qué le falta entender?', ['Que la parodia imita la forma, pero cambia el tono', 'Que la parodia nunca imita a nadie', 'Que la parodia siempre es más larga'], 'Que la parodia imita la forma, pero cambia el tono', 'Copiar repite; parodiar transforma para hacer reír.', 'error')],
 '4': [
   UNI('Uní cada texto satírico con lo que critica.', [('Un empresario vende aire embotellado y la gente hace fila', 'el consumo por moda'), ('Para pedir un formulario hay que entregar el mismo formulario', 'la burocracia'), ('Un pueblo donde todos opinan de los vecinos, pero nadie barre su vereda', 'la hipocresía'), ('Un rey que se pone un traje invisible para no admitir que lo engañaron', 'la vanidad del poder')], 'Preguntá de qué se burla cada uno.', 'analizar'),
   CLA('¿Personaje con matices o caricatura?', ['Con matices', 'Caricatura'], [('Una tía exigente que también es muy cariñosa', 'Con matices'), ('Un avaro que cobra entrada para ver su colección de monedas', 'Caricatura'), ('Un vecino tímido que se anima a hablar en la reunión', 'Con matices'), ('Una influencer que no come si no puede sacarle foto al plato', 'Caricatura')], 'Varios rasgos o uno solo exagerado.', 'aplicar'),
   MS('Un falso noticiero imita la voz y el formato del noticiero para burlarse de los políticos que prometen y no cumplen. Elegí las DOS cosas que es.', ['Parodia, porque imita el formato del noticiero', 'Sátira, porque critica a los políticos', 'Un noticiero real', 'Un texto sin humor'], ['Parodia, porque imita el formato del noticiero', 'Sátira, porque critica a los políticos'], 'Imita un género y, a la vez, critica.'),
   KW('Elegí una costumbre de hoy (por ejemplo, mirar el celular todo el tiempo) y explicá cómo la criticaría una sátira: qué exageraría y qué querría mostrar.', 'Nombrá la costumbre, la exageración y la crítica.', [['exager*', 'agrand*', 'absurd*'], ['critic*', 'mostrar', 'burl*', 'mal', 'problema'], ['celular', 'moda', 'costumbre', 'redes', 'consum*', 'foto*', 'pantalla*']], 2, 'Por ejemplo: exageraría a alguien que se pierde un atardecer por sacarle fotos, para mostrar que miramos la pantalla y no la realidad.', 'aplicar')],
 '5': [
   CLA('¿Qué recurso del humor predomina?', ['Exageración', 'Ironía', 'Parodia', 'Sátira'], [('Tenía tanta sed que se tomó el río', 'Exageración'), ('Ante el examen imposible, dijo: «Facilísimo»', 'Ironía'), ('Un cuento de hadas donde la princesa rescata al dragón', 'Parodia'), ('Un relato que critica a los que compran todo para aparentar', 'Sátira')], 'Repasá los cuatro recursos de la misión.', 'analizar'),
   ORD('Ordená cómo se construye el humor en este chiste: «El mago prometió hacer desaparecer un elefante. Desapareció el público».', ['Se presenta la situación: un mago y un truco', 'Se arma la expectativa: un elefante va a desaparecer', 'Llega el giro: desaparece el público', 'El choque entre lo esperado y lo ocurrido produce la risa'], 'Expectativa, giro y risa.', 'aplicar'),
   MC('En un cuento, un ladrón famoso por sus trucos cae preso porque se olvida la billetera con su documento en la escena del robo. ¿Qué tipo de ironía hay?', ['De situación: le pasa lo contrario de lo esperable', 'Verbal: el ladrón dice lo contrario de lo que piensa', 'Ninguna: es un dato sin humor'], 'De situación: le pasa lo contrario de lo esperable', 'La ironía está en los hechos.', 'analizar'),
   TAP('Tocá las DOS partes que muestran que es una parodia del relato de terror: «Era una noche oscura y tormentosa. El fantasma lanzó un aullido. Desde el cuarto, una voz gritó: "¡Bajá el volumen!"».', ['Era una noche oscura y tormentosa.', 'El fantasma lanzó un aullido.', 'Desde el cuarto,', 'una voz gritó:', '«¡Bajá el volumen!»'], [0, 4], 'Imita el comienzo típico del terror y después lo invierte.', 'analizar')],
}

# ============================ LIBRO DEL NIVEL ============================
LIBRO = {'titulo': 'El fantasma de Canterville', 'act': [
  CLA('En «El fantasma de Canterville», ¿qué rasgos vienen del relato de terror y cuáles son el giro paródico?', ['Rasgo del terror', 'Giro paródico'], [('Un castillo inglés antiguo con un fantasma', 'Rasgo del terror'), ('La familia Otis no se asusta del fantasma', 'Giro paródico'), ('Una mancha de sangre que reaparece en el piso', 'Rasgo del terror'), ('La familia limpia la mancha con un quitamanchas', 'Giro paródico'), ('El fantasma arrastra cadenas de noche', 'Rasgo del terror'), ('Le ofrecen aceite para las cadenas', 'Giro paródico')], 'Wilde imita el terror y lo invierte.', 'analizar'),
  UNI('Uní cada personaje de la novela con su papel en la parodia.', [('Sir Simon', 'el fantasma que ya no logra asustar'), ('El señor Otis', 'el norteamericano práctico que todo lo resuelve comprando'), ('Los mellizos', 'los que le hacen bromas al fantasma'), ('Virginia', 'la única que lo trata con compasión')], 'Cada personaje cumple un papel en el humor.', 'aplicar'),
  MC('Los mellizos Otis le preparan trampas a Sir Simon y él termina escondido y asustado. ¿Qué recurso del humor usa Wilde?', ['La inversión: el asustador termina asustado', 'El juego de palabras con «fantasma»', 'La exageración del tamaño del castillo'], 'La inversión: el asustador termina asustado', 'Se dan vuelta los papeles típicos del terror.', 'analizar'),
  MS('En la novela, la familia Otis cree que todo se resuelve con productos comerciales, y los ingleses viven pendientes de sus tradiciones. Elegí las DOS cosas que critica la sátira de Wilde.', ['El pragmatismo de los ricos norteamericanos', 'El apego de la aristocracia inglesa a sus tradiciones', 'La existencia de los fantasmas', 'Los castillos antiguos'], ['El pragmatismo de los ricos norteamericanos', 'El apego de la aristocracia inglesa a sus tradiciones'], 'La sátira apunta a dos grupos sociales.', 'analizar'),
  ORD('Ordená estos momentos de la novela.', ['La familia Otis compra el castillo de Canterville', 'El fantasma intenta asustarlos, sin éxito', 'Los mellizos le hacen bromas y Sir Simon se deprime', 'Virginia lo ayuda a encontrar descanso'], 'El fantasma pasa de asustar a necesitar ayuda.', 'aplicar'),
  KW('Al final, cuando Virginia ayuda a Sir Simon, la novela se vuelve más seria y emotiva. ¿Por qué creés que Wilde cambia el tono después de tanto humor? Justificá con lo aprendido.', 'Pensá en el contraste entre humor y emoción.', [['virginia', 'compasi*', 'ayud*', 'emoci*', 'serio', 'tierno', 'triste'], ['contraste', 'cambi*', 'humor', 'ironía', 'parodia', 'sátira', 'reír', 'risa']], 2, 'Por ejemplo: el contraste hace que el final emocione más, y muestra que detrás de la parodia hay un personaje que sufre.', 'analizar'),
]}

# ============================ EXAMEN ============================
EX = [
 [1, CLA('¿Qué recurso usa cada frase?', ['Lo inesperado', 'Exageración', 'Juego de palabras'], [('El bombero tenía miedo de los fósforos', 'Lo inesperado'), ('Era tan lento que lo pasaban las tortugas', 'Exageración'), ('—¿Por qué el libro de matemática está triste? —Porque tiene muchos problemas', 'Juego de palabras')], 'Los tres recursos del humor.', 'aplicar')],
 [1, MC('¿Qué es la incongruencia?', ['El choque entre lo esperado y lo que ocurre', 'Una palabra que tiene dos significados', 'Un elogio que dice lo contrario'], 'El choque entre lo esperado y lo que ocurre', 'Es el mecanismo básico del humor.', 'recordar')],
 [1, ODD('Tres frases exageran con humor y una no. ¿Cuál no exagera?', ['Hacía frío y me puse una campera.', 'Hacía tanto frío que las palabras se congelaban.', 'El frío era tal que los osos pedían frazadas.', 'Tenía tanto frío que tiritaba hasta mi sombra.'], 'Hacía frío y me puse una campera.', 'Las demás llevan el frío al absurdo.', 'analizar')],
 [2, SA('Llegás empapado por la lluvia y tu amigo dice: «Veo que trajiste paraguas». ¿Qué recurso usa? Escribí una palabra.', ['ironía', 'ironia', 'la ironía', 'ironía verbal'], 'Dice lo contrario de lo que piensa.', 'aplicar')],
 [2, CLA('¿Ironía verbal o de situación?', ['Verbal', 'De situación'], [('El cerrajero queda encerrado en su casa', 'De situación'), ('Ante un plato quemado: «Me salió perfecto»', 'Verbal'), ('El meteorólogo se moja porque no creyó en su pronóstico', 'De situación'), ('Ante una nota de 2: «Soy un genio»', 'Verbal')], 'En las palabras o en los hechos.', 'analizar')],
 [2, TF('Para reconocer la ironía en un texto escrito, hay que fijarse en el contexto, porque no se escucha el tono de voz.', 'Verdadero', 'El contexto y la exageración reemplazan al tono.', 'recordar')],
 [3, MC('¿Qué es una parodia?', ['Una imitación burlesca de una obra o un género', 'Un texto que copia otro sin cambiarlo', 'Una crítica a las autoridades sin humor'], 'Una imitación burlesca de una obra o un género', 'Imita la forma y cambia el tono.', 'recordar')],
 [3, UNI('Uní cada parodia con lo que imita.', [('El lobo es vegetariano y la abuela lo invita a cenar', 'cuento de hadas'), ('El vampiro no se ve en el espejo y sale despeinado', 'relato de terror'), ('Don Quijote ataca molinos creyendo que son gigantes', 'libros de caballería')], 'Reconocé el original.', 'aplicar')],
 [3, MC('Alguien que nunca leyó cuentos de hadas lee una parodia de cuentos de hadas y no le encuentra la gracia. ¿Por qué?', ['Porque no reconoce lo que se imita ni lo que se invierte', 'Porque las parodias no tienen humor', 'Porque los cuentos de hadas son tristes'], 'Porque no reconoce lo que se imita ni lo que se invierte', 'La parodia necesita un lector que conozca el original.', 'analizar')],
 [4, MC('¿En qué se diferencia la sátira de la parodia?', ['La sátira critica a la sociedad; la parodia imita una obra', 'La sátira no tiene humor; la parodia sí', 'La sátira imita géneros; la parodia critica personas'], 'La sátira critica a la sociedad; la parodia imita una obra', 'Pueden aparecer juntas, pero apuntan a cosas distintas.', 'analizar')],
 [4, CLA('¿Parodia, sátira o las dos?', ['Parodia', 'Sátira', 'Las dos'], [('Un cuento de hadas donde el príncipe se cae del caballo', 'Parodia'), ('Una historieta sobre funcionarios que duermen en la oficina', 'Sátira'), ('Un falso noticiero que imita el formato para criticar a los políticos', 'Las dos')], 'Imitar un género, criticar a la sociedad o ambas cosas.', 'analizar')],
 [4, MC('Un personaje es tan vanidoso que no sale de su casa sin cinco espejos. ¿Qué recurso de la sátira es?', ['Una caricatura: exagera un rasgo hasta lo ridículo', 'Un juego de palabras con «espejo»', 'Una ironía verbal del narrador'], 'Una caricatura: exagera un rasgo hasta lo ridículo', 'La caricatura representa un tipo de persona.', 'aplicar')],
 [4, KW('Explicá con tus palabras qué diferencia hay entre parodia y sátira, y da un ejemplo de cada una.', 'Nombrá las dos, qué hace cada una y un ejemplo.', [['parodia'], ['sátira', 'satira'], ['imita*', 'género', 'obra', 'copia*'], ['critic*', 'socie*', 'costumbre*', 'burla*', 'defecto*']], 4, 'Por ejemplo: la parodia imita una obra o un género para jugar con él (un cuento de hadas al revés); la sátira critica a la sociedad (un intendente que multa a las nubes).', 'aplicar')],
]

# ============================ CARPETA ============================
CARP = {
 '1': [
  ('En «Estudió toda la noche para la prueba y se quedó dormido en el examen», ¿qué recurso del humor aparece?', 'aplicar', ['lo inesperado', 'inesperado', 'incongruencia'], 'Lo inesperado: el esfuerzo termina produciendo lo contrario de lo esperado.'),
  ('«Mi hermano come tanto que la heladera le pide vacaciones.» ¿Qué rasgo real exagera esa frase?', 'aplicar', ['que come mucho', 'come mucho', 'el apetito', 'apetito'], 'Que come mucho: la exageración agranda un rasgo verdadero.'),
  ('«—Trabajo en una planta. —¿Y qué hacés? —La riego.» ¿Qué palabra tiene doble sentido en el chiste?', 'analizar', ['planta'], 'Planta: fábrica y vegetal.'),
  ('Tomi dice que «tardó tanto que llegué con barba» es una mentira y por eso está mal escrito. ¿Qué recurso es en realidad?', 'error', ['exageración', 'exageracion', 'una exageración', 'hipérbole'], 'Una exageración: no busca engañar, sino hacer reír.'),
 ],
 '2': [
  ('Afuera llueve a cántaros y tu tío dice: «Ideal para tomar sol en la terraza». ¿Qué recurso usa?', 'aplicar', ['ironía', 'ironia', 'ironía verbal'], 'Ironía: dice lo contrario de lo que piensa.'),
  ('El cerrajero del barrio quedó encerrado en su propio negocio toda la tarde. ¿Qué tipo de ironía es?', 'aplicar', ['de situación', 'situacion', 'situación', 'ironía de situación'], 'De situación: los hechos son lo contrario de lo esperable.'),
  ('Clara dice «¡Qué noche tan divertida!» mientras bosteza en una fiesta aburrida. ¿Qué pista del tono muestra la ironía?', 'analizar', ['el bostezo', 'bosteza', 'que bosteza'], 'El bostezo: muestra aburrimiento y contradice lo que dice.'),
  ('Lucía leyó «el señor era generosísimo: cobraba el lápiz que prestaba» y entendió que era generoso. ¿Qué tendría que haber notado?', 'error', ['la ironía', 'ironía', 'que es irónico', 'ironia'], 'La ironía: los hechos contradicen el elogio.'),
 ],
 '3': [
  ('Un cuento dice: «Había una vez un dragón que se escondía cada vez que veía un caballero». ¿Qué género parodia?', 'aplicar', ['el cuento de hadas', 'cuento de hadas', 'cuentos de hadas', 'los cuentos de hadas'], 'El cuento de hadas: imita la fórmula y da vuelta los papeles.'),
  ('En una parodia, el hombre lobo va al peluquero todos los meses para que no se le note. ¿Qué rasgo del terror se exagera?', 'analizar', ['el pelo', 'que le crece pelo', 'el pelo del hombre lobo'], 'El pelo: un rasgo típico del monstruo se vuelve problema cotidiano.'),
  ('Don Quijote ataca unos molinos de viento porque cree que son gigantes. ¿Qué tipo de libros está parodiando Cervantes?', 'aplicar', ['libros de caballería', 'de caballería', 'caballería', 'caballeria'], 'Los libros de caballería, con sus combates heroicos.'),
  ('Pedro dice que una parodia es copiar un texto tal cual. ¿Qué cambia la parodia respecto del original?', 'error', ['el tono', 'tono'], 'El tono: imita la forma, pero vuelve ridículo lo serio.'),
 ],
 '4': [
  ('Un cuento muestra a un intendente que prohíbe la lluvia por decreto y multa a las nubes. ¿De quiénes se burla la sátira?', 'analizar', ['de las autoridades', 'autoridades', 'de los gobernantes', 'gobernantes'], 'De las autoridades que creen que todo se arregla con papeles.'),
  ('Un personaje es tan tacaño que cuenta las monedas a oscuras para no gastar luz. ¿Cómo se llama ese retrato exagerado?', 'aplicar', ['caricatura', 'una caricatura'], 'Caricatura: exagera un rasgo hasta lo ridículo.'),
  ('Un falso noticiero imita el formato real para burlarse de los políticos que no cumplen. ¿Es parodia, sátira o las dos?', 'analizar', ['las dos', 'ambas', 'parodia y sátira'], 'Las dos: imita un género y critica a la sociedad.'),
  ('Martín dice que la sátira solo sirve para hacer reír. ¿Qué otra intención tiene, además de la risa?', 'error', ['criticar', 'la crítica', 'critica', 'crítica'], 'Criticar: muestra un defecto de las personas o la sociedad.'),
 ],
}

def ajustes(M):
    M['act'] = A
    M['examen'] = EX
    M['libro'] = LIBRO
    M['practica'] = 'Actividades generales'
    M['examen_titulo'] = 'Nivel jefe: parodia y humor'
    M['actualizar_preguntas'] = True
    for k, items in CARP.items():
        N = M['niveles'].setdefault(k, {})
        N['carpeta'] = [c for c, _, _, _ in items]; N['carpeta_nivel'] = [t for _, t, _, _ in items]
        N['respuestas_carpeta'] = [r for _, _, r, _ in items]; N.setdefault('soluciones', {})['carpeta'] = [s for _, _, _, s in items]

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-6/mision-6.json', L, ajustes=ajustes)
