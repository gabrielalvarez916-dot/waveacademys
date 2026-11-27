# -*- coding: utf-8 -*-
# Lengua y Literatura I · Misión 7 · Ortografía en uso (la clase animada queda; lección, actividades y examen nuevos)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))
from armar import *
from lengua1_1_2 import MC, TF, ORD, UNI, CLA, TAP, MS, SA, KW, FB, ODD

L = {}
L['1'] = {'temas': [
 T('La sílaba tónica',
   m('palabra', items=[{'s': ['ven', 'ta', 'na'], 't': 1}, {'s': ['ra', 'tón'], 't': 1}, {'s': ['sá', 'ba', 'do'], 't': 0}, {'s': ['ca', 'mión'], 't': 1}]),
   m('clasificar_x', consigna='Decí cada palabra en voz alta y clasificala según su sílaba tónica.', cajas=['Aguda', 'Grave', 'Esdrújula'], cuantos=6, items=[
     ['ratón', 0], ['reloj', 0], ['jardín', 0], ['ventana', 1], ['mesa', 1], ['cárcel', 1], ['sábado', 2], ['pájaro', 2], ['brújula', 2]]),
   ('Sílaba tónica', 'La sílaba tónica es la que se pronuncia con más fuerza dentro de una palabra; según su lugar, la palabra es aguda, grave o esdrújula.'),
   'Para encontrarla, conviene decir la palabra en voz alta, como si llamaras a alguien desde lejos: la sílaba que se estira es la tónica. Después se cuenta desde el final: si es la última, la palabra es aguda; si es la penúltima, grave; si es la antepenúltima, esdrújula.',
   ['Aguda: fuerza en la última sílaba.', 'Grave: en la penúltima.', 'Esdrújula: en la antepenúltima.']),
 T('Las reglas de la tilde',
   m('palabra', items=[{'s': ['co', 'li', 'brí'], 't': 2}, {'s': ['co', 'lor'], 't': 1}, {'s': ['dé', 'bil'], 't': 0}, {'s': ['jo', 'ven'], 't': 0}, {'s': ['re', 'lám', 'pa', 'go'], 't': 1}]),
   m('tilde_x', items=[
     {'s': ['sa', 'lón'], 'ayuda': 'Aguda terminada en n: lleva tilde.'}, {'s': ['pa', 'red'], 'ayuda': 'Aguda terminada en d: no lleva.'}, {'s': ['fá', 'cil'], 'ayuda': 'Grave terminada en l: lleva tilde.'},
     {'s': ['li', 'bro'], 'ayuda': 'Grave terminada en vocal: no lleva.'}, {'s': ['mú', 'si', 'co'], 'ayuda': 'Esdrújula: siempre lleva tilde.'}, {'s': ['an', 'dén'], 'ayuda': 'Aguda terminada en n: lleva tilde.'}]),
   ('Reglas de tildación', 'Las reglas de tildación indican qué palabras llevan tilde según su sílaba tónica y su letra final: agudas en n, s o vocal; graves que no terminan en n, s o vocal; y todas las esdrújulas.'),
   'Las reglas parecen al revés entre agudas y graves, pero tienen una lógica: en español, la mayoría de las palabras terminadas en vocal, n o s son graves, y las demás son agudas. La tilde se pone justo en los casos que se salen de esa costumbre, para avisarle al lector dónde va la fuerza.',
   ['Aguda: tilde si termina en n, s o vocal.', 'Grave: tilde si NO termina en n, s o vocal.', 'Esdrújula: tilde siempre.']),
 T('Cuando la tilde cambia el sentido',
   m('versiones', rotulo='Palabra', items=[
     {'nombre': 'Término', 'texto': '{{Llegamos al término del viaje.|Esdrújula: sustantivo, «el final».}}'},
     {'nombre': 'Termino', 'texto': '{{Yo termino la tarea a las seis.|Grave: verbo en presente.}}'},
     {'nombre': 'Terminó', 'texto': '{{Ella terminó la tarea ayer.|Aguda: verbo en pasado.}}'}]),
   m('completar_x', consigna='Elegí la forma correcta según el sentido.', items=[
     {'texto': 'Ayer mi hermano [[practicó/practico/práctico]] dos horas de guitarra.', 'ayuda': 'Es pasado: la fuerza va al final.'},
     {'texto': 'Todos los días yo [[practico/practicó/práctico]] media hora.', 'ayuda': 'Es presente, primera persona.'},
     {'texto': 'Es un consejo muy [[práctico/practico/practicó]] para la vida diaria.', 'ayuda': 'Es un adjetivo: esdrújula.'},
     {'texto': 'El [[público/publico/publicó]] aplaudió de pie al final del show.', 'ayuda': 'Sustantivo: la gente que mira.'}]),
   ('Tilde y sentido', 'En algunas palabras, cambiar el lugar de la sílaba tónica cambia el significado, y la tilde es lo único que lo muestra por escrito.'),
   'Por eso la tilde no es un adorno: «público», «publico» y «publicó» son tres palabras distintas. Cuando escribas, decí la palabra en voz alta dentro de la oración; la fuerza de la voz te va a indicar cuál de las tres necesitás.',
   ['Esdrújula: suele ser sustantivo o adjetivo.', 'Grave: verbo en presente (yo).', 'Aguda: verbo en pasado (él, ella).'])],
 'recuerda': [
   R('Sílaba tónica', 'es la sílaba que se pronuncia con más fuerza dentro de una palabra.', 'En «ventana», la fuerza cae en «ta»'),
   R('Palabra aguda', 'tiene la sílaba tónica en la última sílaba y lleva tilde si termina en n, s o vocal.', 'colibrí, salón, pero color'),
   R('Palabra grave', 'tiene la sílaba tónica en la penúltima y lleva tilde si no termina en n, s o vocal.', 'débil, fácil, pero joven'),
   R('Palabra esdrújula', 'tiene la sílaba tónica en la antepenúltima y lleva tilde siempre, sin excepción.', 'sábado, relámpago'),
   R('Tilde y sentido', 'en algunas palabras la tilde distingue significados, porque cambia la sílaba tónica.', 'término / termino / terminó')]}

L['2'] = {'temas': [
 T('El diptongo',
   m('vocales', items=[{'s': ['pei', 'ne'], 'g': 'ei', 'tipo': 'diptongo'}, {'s': ['sue', 'lo'], 'g': 'ue', 'tipo': 'diptongo'}, {'s': ['viu', 'do'], 'g': 'iu', 'tipo': 'diptongo', 'regla': 'Dos cerradas juntas (i, u) también forman diptongo.'}]),
   m('clasificar_x', consigna='¿Las vocales marcadas forman diptongo? Separá la palabra en sílabas para decidir.', cajas=['Diptongo', 'No es diptongo'], cuantos=6, items=[
     ['aire', 0], ['nieve', 0], ['causa', 0], ['ruido', 0], ['poeta', 1], ['león', 1], ['caos', 1], ['tío', 1]]),
   ('Diptongo', 'El diptongo es la unión de dos vocales que se pronuncian en una misma sílaba: una abierta y una cerrada sin tilde, o dos cerradas distintas.'),
   'Las vocales se dividen en abiertas (a, e, o) y cerradas (i, u). Cuando una cerrada sin tilde se junta con una abierta, o dos cerradas entre sí, la voz las pronuncia de un solo golpe: forman diptongo y quedan en la misma sílaba, como en «pei-ne» o «viu-do».',
   ['Abiertas: a, e, o. Cerradas: i, u.', 'Abierta + cerrada sin tilde: diptongo.', 'Dos cerradas distintas: diptongo.']),
 T('El hiato',
   m('vocales', items=[{'s': ['po', 'e', 'ta'], 'g': 'oe', 'tipo': 'hiato', 'regla': 'Dos abiertas nunca van juntas en una sílaba.'}, {'s': ['bú', 'ho'], 'g': 'úo', 'tipo': 'hiato', 'regla': 'La cerrada tónica (ú) se separa de la abierta.'}, {'s': ['ma', 'íz'], 'g': 'aí', 'tipo': 'hiato'}]),
   m('silabas_x', consigna='Separá en sílabas. Fijate si las vocales juntas quedan en la misma sílaba o en sílabas distintas.', items=['po-e-ta', 'pei-ne', 'ma-íz', 'cau-sa', 'le-ón', 'cue-va', 'ba-úl', 'rui-do']),
   ('Hiato', 'El hiato es el encuentro de dos vocales que se pronuncian en sílabas distintas: dos abiertas, o una cerrada tónica junto a una abierta.'),
   'El hiato puede darse de dos maneras. En la primera se juntan dos vocales abiertas, como en «po-e-ta» o «le-ón», y se separan siempre. En la segunda, una vocal cerrada lleva la fuerza de la voz, como en «ma-íz», y se separa de la abierta. Separar en sílabas en voz alta es la mejor manera de distinguirlo del diptongo.',
   ['Dos abiertas: hiato.', 'Cerrada tónica + abierta: hiato.', 'Para decidir, separá en sílabas.']),
 T('La tilde en diptongos y hiatos',
   m('marcar', rotulo='Palabra', items=[
     {'nombre': 'Diptongo', 'texto': '{{camión|Diptongo «io»: sigue las reglas generales. Aguda en n → tilde.}} · {{puerta|Diptongo «ue»: grave en vocal → sin tilde.}} · {{huésped|Diptongo «ue»: grave en d → tilde, y va en la abierta.}}', 'cierre': 'El diptongo sigue las reglas de siempre; la tilde va en la vocal abierta.'},
     {'nombre': 'Hiato', 'texto': '{{grúa|Hiato con cerrada tónica: lleva tilde aunque sea grave en vocal.}} · {{baúl|Hiato con cerrada tónica: lleva tilde.}} · {{océano|Hiato de dos abiertas: sigue las reglas; esdrújula → tilde.}}', 'cierre': 'La cerrada tónica en hiato lleva tilde siempre.'}]),
   m('tilde_x', consigna='Tocá la sílaba que lleva tilde, o «No lleva tilde».', items=[
     {'s': ['grú', 'a'], 'ayuda': 'Hiato con cerrada tónica: lleva tilde siempre.'}, {'s': ['ba', 'úl'], 'ayuda': 'Hiato con u tónica: lleva tilde.'}, {'s': ['cue', 'va'], 'ayuda': 'Diptongo, grave en vocal: no lleva.'},
     {'s': ['ac', 'ción'], 'ayuda': 'Diptongo, aguda en n: lleva tilde.'}, {'s': ['ra', 'íz'], 'ayuda': 'Hiato con i tónica: lleva tilde.'}, {'s': ['sue', 'lo'], 'ayuda': 'Diptongo, grave en vocal: no lleva.'}]),
   ('Tilde en el hiato', 'Las palabras con hiato de vocal cerrada tónica llevan tilde siempre en esa vocal, aunque las reglas generales digan lo contrario.'),
   'Los diptongos y los hiatos de dos abiertas siguen las reglas generales de agudas, graves y esdrújulas. La excepción es el hiato con i o u tónica: la tilde es obligatoria, porque marca que esas vocales se separan. Sin ella, «grúa» se leería «grua», en una sola sílaba.',
   ['Diptongo: reglas generales.', 'Dos abiertas: reglas generales.', 'Cerrada tónica en hiato: tilde siempre.'])],
 'recuerda': [
   R('Vocales abiertas y cerradas', 'las abiertas son a, e, o, y las cerradas son i, u; su encuentro decide diptongo o hiato.', 'a-e-o / i-u'),
   R('Diptongo', 'son dos vocales juntas que se pronuncian en una misma sílaba: abierta con cerrada átona, o dos cerradas.', 'pei-ne, viu-do'),
   R('Hiato', 'son dos vocales juntas que se pronuncian en sílabas distintas: dos abiertas o cerrada tónica con abierta.', 'po-e-ta, ma-íz'),
   R('Tilde en el diptongo', 'sigue las reglas generales y, si lleva, va en la vocal abierta.', 'camión, huésped'),
   R('Tilde en el hiato', 'la vocal cerrada tónica que forma hiato lleva tilde siempre.', 'grúa, baúl, raíz')]}

L['3'] = {'temas': [
 T('B o V',
   m('marcar', rotulo='Regla', items=[
     {'nombre': 'Pasado en -aba', 'texto': 'Cuando era chica, mi abuela {{jugaba|Terminación -aba del pretérito imperfecto: siempre con b.}} en la vereda y {{saltaba|-aba: con b.}} la soga mientras su hermano {{miraba|-aba: con b.}}.', 'cierre': 'Todos los verbos terminados en -ar forman este pasado con -aba.'},
     {'nombre': 'Bl y br', 'texto': 'El {{cable|Antes de l, siempre b.}} del {{brazo|Antes de r, siempre b.}} mecánico se {{rompió|(Sin b ni v: control.)}} durante la {{obra|br.}}.', 'cierre': 'Las combinaciones bl y br se escriben siempre con b.'},
     {'nombre': 'Verbo ir', 'texto': 'Mañana {{voy|El verbo ir va con v.}} al club; ayer {{fuimos|Pretérito del verbo ir: sin v ni b.}} al cine y siempre {{vamos|v.}} juntos.', 'cierre': 'Las formas del verbo ir que empiezan con ese sonido van con v.'}]),
   m('completar_x', consigna='Completá con b o v.', items=[
     {'texto': 'Cuando era chico, mi primo [[b/v]]ailaba y can[[t/d]]aba en todas las fiestas. Siempre lle[[v/b]]aba su guitarra.', 'ayuda': 'Pensá: «bailar» lleva b; «llevaba» viene de llevar (con v) y termina en -aba.'},
     {'texto': 'Se rompió el ca[[b/v]]le de la lámpara y la [[b/v]]ruja del cuento no podía [[v/b]]er nada.', 'ayuda': 'Bl y br van con b; «ver» va con v.'},
     {'texto': 'Mañana [[v/b]]amos al río. Mi hermana nada[[b/v]]a muy bien el verano pasado.', 'ayuda': 'Verbo ir con v; pretérito en -aba con b.'}]),
   ('B y V', 'La b y la v suenan igual en el español de la Argentina, por eso hay reglas: se escribe b en el pretérito terminado en -aba y antes de l o r, y v en las formas del verbo ir.'),
   'Como el oído no ayuda, la memoria y las reglas son las herramientas. Una pista útil es pensar en la familia de palabras: «llevaba» va con v porque viene de «llevar», aunque la terminación -aba lleve b. Ante la duda, el diccionario siempre tiene la última palabra.',
   ['-aba del pretérito: b (cantaba, jugaba).', 'bl y br: siempre b (cable, brazo).', 'Verbo ir: v (voy, vamos).']),
 T('G o J',
   m('marcar', rotulo='Regla', items=[
     {'nombre': 'Verbos en -ger y -gir', 'texto': 'Hay que {{proteger|Verbo terminado en -ger: con g.}} las plantas y {{elegir|Terminado en -gir: con g.}} bien la tierra. Ayer {{escogí|Mantiene la g del infinitivo «escoger».}} las semillas.', 'cierre': 'Excepciones conocidas: tejer y crujir.'},
     {'nombre': 'Palabras en -aje', 'texto': 'Hicimos un {{viaje|Terminación -aje: con j.}} largo con mucho {{equipaje|-aje: con j.}}, y el {{paisaje|-aje: con j.}} era hermoso.', 'cierre': 'Las palabras terminadas en -aje se escriben con j.'}]),
   m('clasificar_x', consigna='¿Se escribe con g o con j?', cajas=['Con g', 'Con j'], cuantos=6, items=[
     ['prote_er', 0], ['diri_ir', 0], ['reco_er', 0], ['ele_ir', 0], ['pasa_e', 1], ['cora_e', 1], ['mensa_e', 1], ['te_er', 1]]),
   ('G y J', 'Ante e o i, la g y la j pueden sonar igual; por eso se escriben con g los verbos terminados en -ger y -gir, y con j las palabras terminadas en -aje.'),
   'Estas reglas ayudan con muchas palabras, pero hay excepciones famosas: «tejer» y «crujir» se escriben con j aunque terminen en -er e -ir. También conviene recordar que los verbos conservan su letra al conjugarse: «elegir» da «elegimos», con g.',
   ['-ger y -gir: g (proteger, elegir).', '-aje: j (viaje, paisaje).', 'Excepciones: tejer, crujir.']),
 T('Palabras que suenan igual',
   m('versiones', rotulo='Palabra', items=[
     {'nombre': 'Hecho / echo', 'texto': '{{Ya está hecho el trabajo.|«Hecho», de hacer: con h.}} {{Echo la carta en el buzón.|«Echo», de echar: sin h.}}'},
     {'nombre': 'Hay / ahí / ay', 'texto': '{{Hay pan en la mesa.|«Hay», de haber: existir.}} {{Dejalo ahí, al lado de la puerta.|«Ahí»: un lugar.}} {{¡Ay, me pisaste!|«Ay»: una queja.}}'},
     {'nombre': 'A ver / haber', 'texto': '{{A ver qué dice la carta.|«A ver»: mirar, averiguar.}} {{Puede haber lluvia mañana.|«Haber»: el verbo, existir.}}'}]),
   m('completar_x', consigna='Elegí la forma correcta.', items=[
     {'texto': '[[Hay/Ahí/Ay]] tres libros en la mochila; dejala [[ahí/hay/ay]], en la silla.', 'ayuda': 'Hay = existir; ahí = lugar.'},
     {'texto': 'Ya está [[hecho/echo]] el dibujo. Ahora lo [[echo/hecho]] al sobre.', 'ayuda': 'Hecho, de hacer; echo, de echar.'},
     {'texto': '[[A ver/Haber]] si mañana sale el sol. Tiene que [[haber/a ver]] un error en la cuenta.', 'ayuda': 'A ver = averiguar; haber = existir.'}]),
   ('Homófonos', 'Los homófonos son palabras que suenan igual pero se escriben distinto y tienen significados diferentes, como hecho y echo, o hay, ahí y ay.'),
   'Con los homófonos no hay regla de sonido que ayude: hay que pensar el significado. Una estrategia útil es reemplazar: si podés poner «existe», va «hay»; si podés poner «en ese lugar», va «ahí»; si podés poner «averiguar», va «a ver».',
   ['Hecho (hacer) / echo (echar).', 'Hay (existe) / ahí (lugar) / ay (queja).', 'A ver (averiguar) / haber (existir).']),
 T('Por qué, porque y porqué',
   m('marcar', rotulo='Uso', items=[
     {'nombre': 'Pregunta y respuesta', 'texto': '—{{¿Por qué|Separado y con tilde: pregunta.}} llegaste tarde? —{{Porque|Junto y sin tilde: da la causa.}} se rompió el colectivo.', 'cierre': 'Por qué pregunta; porque responde.'},
     {'nombre': 'Sustantivo', 'texto': 'Nadie sabe {{el porqué|Junto y con tilde, con artículo: significa «el motivo».}} de su enojo, ni {{por qué|Pregunta indirecta: separado y con tilde.}} se fue.', 'cierre': 'El porqué es un sustantivo: lleva artículo.'}]),
   m('completar_x', consigna='Completá con por qué, porque o porqué.', items=[
     {'texto': '¿[[Por qué/Porque/Porqué]] no viniste? —[[Porque/Por qué/Porqué]] estaba enfermo.', 'ayuda': 'Pregunta separado; respuesta junto.'},
     {'texto': 'Quiero saber [[por qué/porque/porqué]] cerraron la biblioteca. Nadie explicó el [[porqué/por qué/porque]].', 'ayuda': 'Pregunta indirecta: separado y con tilde; con artículo: el porqué.'},
     {'texto': 'Me quedé en casa [[porque/por qué/porqué]] llovía.', 'ayuda': 'Da la causa: junto y sin tilde.'}]),
   ('Por qué, porque, porqué', '«Por qué» pregunta, «porque» explica la causa y «porqué» es un sustantivo que significa «el motivo» y va con artículo.'),
   'El error más común es escribir «porque» en las preguntas. Una prueba rápida: si la oración pregunta, aunque no tenga signos de interrogación («no sé por qué se fue»), va separado y con tilde. Si se puede reemplazar por «el motivo», es el sustantivo: «el porqué».',
   ['¿Por qué? → pregunta (también indirecta).', 'Porque → causa, en la respuesta.', 'El porqué → el motivo.'])],
 'recuerda': [
   R('B en -aba', 'los verbos en pretérito imperfecto terminados en -aba se escriben siempre con b.', 'jugaba, saltaba, llevaba'),
   R('Bl y br', 'antes de l y de r se escribe siempre b, nunca v.', 'cable, brazo, obra'),
   R('G en -ger y -gir', 'los verbos terminados en -ger y -gir se escriben con g, salvo tejer y crujir.', 'proteger, elegir'),
   R('J en -aje', 'las palabras terminadas en -aje se escriben con j.', 'viaje, equipaje, paisaje'),
   R('Homófonos', 'son palabras que suenan igual y se escriben distinto; se eligen por el significado.', 'hay / ahí / ay'),
   R('Por qué / porque / porqué', 'por qué pregunta, porque da la causa y el porqué es el motivo.', '¿Por qué? Porque llovió.')]}

L['4'] = {'temas': [
 T('Revisar en pasadas',
   m('revision', items=[
     {'nombre': 'El correo', 'borrador': 'hola profe, le escrivo porque no entendi la tarea. ¿porque hay que hacer el resumen dos veses?', 'criterios': [['Se entiende lo que pide', True, 'Primera pasada: el sentido.'], ['Las tildes están bien', False, 'entendí, por qué'], ['Las letras están bien', False, 'escribo, veces'], ['Mayúsculas y puntuación', False, 'Hola, Profe y ¿Por']],
      'final': 'Hola, profe. Le escribo porque no entendí la tarea. ¿Por qué hay que hacer el resumen dos veces?'},
     {'nombre': 'La nota', 'borrador': 'el sabado vamos al museo. ay que llevar abrigo y la autorizacion firmada.', 'criterios': [['Se entiende lo que pide', True, 'El mensaje es claro.'], ['Las tildes están bien', False, 'sábado, autorización'], ['Las letras están bien', False, 'hay (existir)'], ['Mayúsculas y puntuación', False, 'El al comienzo']],
      'final': 'El sábado vamos al museo. Hay que llevar abrigo y la autorización firmada.'}]),
   m('marcar_x', consigna='Tocá las palabras que tienen un error de ortografía.', items=[
     {'cons': 'Revisá esta oración en una sola pasada de letras.', 'texto': '[[Mi|0]] [[hermano|0]] [[jugava|1]] [[en|0]] [[el|0]] [[jardin|1]] [[con|0]] [[su|0]] [[perro|0]] [[blanco|0]].'},
     {'cons': 'Revisá esta oración buscando tildes y letras.', 'texto': '[[Ayer|0]] [[eligimos|0]] [[el|0]] [[mejor|0]] [[paisage|1]] [[para|0]] [[la|0]] [[foto|0]] [[del|0]] [[viaje|0]] [[al|0]] [[Peru|1]].'}]),
   ('Revisión', 'Revisar es volver a leer un texto propio para corregirlo, mejor en varias pasadas: una para el sentido y otras para tildes, letras, mayúsculas y puntuación.'),
   'Cuando uno busca todos los errores a la vez, se le escapan muchos, porque la atención se reparte. Si en cada pasada se busca una sola cosa, el ojo se concentra y encuentra más. Leer en voz alta ayuda: se escucha lo que falta o lo que suena raro.',
   ['1.ª pasada: que se entienda.', 'Después: tildes, letras, mayúsculas y puntos.', 'Leer en voz alta ayuda a encontrar errores.']),
 T('El diccionario contra la duda',
   m('marcar', rotulo='Consulta', items=[
     {'nombre': 'La duda', 'texto': 'Lucía no sabe si se escribe {{«exelente» o «excelente»|Duda de letras: el oído no alcanza.}}. {{Busca en el diccionario en línea de la Real Academia|Consulta una fuente confiable.}} y {{encuentra «excelente», con xc|La duda queda resuelta.}}.', 'cierre': 'Ante la duda, consultar es mejor que adivinar.'},
     {'nombre': 'El corrector', 'texto': 'El corrector del celular {{no marcó «echo»|Existe la palabra (de echar), por eso no la marca.}} en la frase {{«ya está echo»|Pero acá corresponde «hecho», de hacer.}}. {{Mateo la corrige pensando en el significado|El corrector no entiende el sentido; el que escribe sí.}}.', 'cierre': 'El corrector automático ayuda, pero no reemplaza la revisión.'}]),
   m('elegir_x', consigna='¿Qué conviene hacer en cada caso?', items=[
     {'cons': 'No sabés si «vaca» va con b o con v, y no hay ninguna regla que lo resuelva.', 'ops': ['Buscarla en el diccionario', 'Escribirla como suena', 'Elegir la letra al azar'], 'ayuda': 'Cuando no hay regla, se consulta.'},
     {'cons': 'El corrector no marca ningún error en «Hay viene el colectivo».', 'ops': ['Revisar igual: «hay» no corresponde, va «ahí»', 'Confiar en el corrector', 'Agregar más palabras'], 'ayuda': 'El corrector no entiende el sentido.'},
     {'cons': 'Terminaste un texto largo a último momento.', 'ops': ['Releerlo aunque sea una vez en voz alta', 'Entregarlo sin mirar', 'Borrar la mitad'], 'ayuda': 'Una relectura rápida encuentra los errores más visibles.'}]),
   ('Diccionario', 'El diccionario es la herramienta que resuelve las dudas de ortografía que el oído y las reglas no alcanzan a resolver.'),
   'Los correctores automáticos ayudan, pero solo detectan palabras que no existen: si escribís «echo» en lugar de «hecho», no lo marcan, porque las dos palabras existen. Por eso la revisión final la hace siempre el que escribe, pensando en el significado de cada palabra.',
   ['Si no hay regla, el diccionario.', 'El corrector no entiende el sentido.', 'La última revisión la hacés vos.']),
 T('El dictado',
   m('marcar', rotulo='Estrategia', items=[
     {'nombre': 'Antes de escribir', 'texto': '{{Escucho la oración completa antes de empezar|Así entiendo el sentido y elijo bien los homófonos.}}. {{La repito en voz baja|La memoria guarda la frase entera.}}.', 'cierre': 'Primero entender, después escribir.'},
     {'nombre': 'Después de escribir', 'texto': '{{Releo buscando tildes|Pasada de tildes.}}, {{después las letras dudosas: b, v, g, j, h|Pasada de letras.}} y {{al final los puntos y las mayúsculas|Pasada de puntuación.}}.', 'cierre': 'El dictado también se revisa en pasadas.'}]),
   m('dictado_x', consigna='Escuchá la oración y escribila. Después revisá tildes y letras.', items=[
     {'texto': 'El sábado jugábamos en el jardín hasta que oscurecía.'}, {'texto': 'Hay que proteger el paisaje del parque.'},
     {'texto': 'Mi tío vive en una casa con un árbol enorme.'}, {'texto': '¿Por qué no vino el camión con el equipaje?'}]),
   ('Dictado', 'El dictado es un ejercicio en el que se escribe un texto que otro lee en voz alta; sirve para practicar la ortografía en uso, con palabras dentro de oraciones reales.'),
   'En el dictado se juntan todas las reglas de la misión: tildes, diptongos y hiatos, letras que confunden y homófonos. La clave es no apurarse: escuchar la oración entera, escribirla y después revisarla en pasadas, igual que cualquier texto propio.',
   ['Escuchar la oración completa.', 'Escribir pensando el significado.', 'Revisar en pasadas al final.'])],
 'recuerda': [
   R('Revisión', 'es volver a leer un texto propio para corregirlo, mejor en varias pasadas.', 'sentido → tildes → letras → puntuación'),
   R('Pasadas', 'consisten en buscar un solo tipo de error por vez para que la atención no se reparta.', 'Una lectura solo para las tildes'),
   R('Leer en voz alta', 'ayuda a escuchar lo que falta, lo que sobra o lo que suena raro en un texto.', 'Se nota la palabra repetida'),
   R('Diccionario', 'resuelve las dudas de ortografía que las reglas y el oído no alcanzan a resolver.', '¿vaca o baca? → vaca'),
   R('Corrector automático', 'solo marca palabras que no existen, por eso no reemplaza la revisión del que escribe.', 'No marca «echo» en lugar de «hecho»')]}

A = {
 '1': [
   CLA('Clasificá cada palabra según su sílaba tónica.', ['Aguda', 'Grave', 'Esdrújula'], [('café', 'Aguda'), ('pared', 'Aguda'), ('cárcel', 'Grave'), ('mesa', 'Grave'), ('miércoles', 'Esdrújula'), ('lámpara', 'Esdrújula')], 'Decí cada palabra en voz alta.', 'aplicar'),
   CLA('¿Lleva tilde o no? Aplicá las reglas.', ['Con tilde', 'Sin tilde'], [('jabón', 'Con tilde'), ('reloj', 'Sin tilde'), ('azúcar', 'Con tilde'), ('casa', 'Sin tilde'), ('brújula', 'Con tilde'), ('joven', 'Sin tilde')], 'Clasificá primero y fijate en la última letra.', 'aplicar'),
   TAP('Tocá las DOS palabras a las que les falta la tilde: «El jueves compre un lapiz azul y una goma.»', ['El', 'jueves', 'compre', 'un', 'lapiz', 'azul', 'y', 'una', 'goma.'], [2, 4], 'Compré: aguda en vocal. Lápiz: grave en z.', 'error'),
   MC('¿Qué palabra completa bien la oración «Ayer el equipo ___ el campeonato»?', ['ganó', 'gano', 'gáno'], 'ganó', 'Es pasado: la fuerza va al final y es aguda en vocal.', 'analizar')],
 '2': [
   CLA('¿Diptongo o hiato? Separá en sílabas para decidir.', ['Diptongo', 'Hiato'], [('cielo', 'Diptongo'), ('cuerda', 'Diptongo'), ('ciudad', 'Diptongo'), ('poeta', 'Hiato'), ('día', 'Hiato'), ('león', 'Hiato')], 'Misma sílaba o sílabas distintas.', 'aplicar'),
   UNI('Uní cada palabra con su separación en sílabas.', [('baúl', 'ba-úl'), ('peine', 'pei-ne'), ('teatro', 'te-a-tro'), ('fuego', 'fue-go')], 'En el hiato las vocales se separan.', 'aplicar'),
   MC('¿Por qué «grúa» lleva tilde, si es grave y termina en vocal?', ['Porque la u tónica forma hiato con la a', 'Porque todas las graves llevan tilde', 'Porque es una palabra muy corta'], 'Porque la u tónica forma hiato con la a', 'La cerrada tónica en hiato lleva tilde siempre.', 'analizar'),
   TAP('Tocá las DOS palabras mal escritas: «Mi tio guardó la ropa en el baul del auto.»', ['Mi', 'tio', 'guardó', 'la', 'ropa', 'en', 'el', 'baul', 'del', 'auto.'], [1, 7], 'Tío y baúl: hiatos con cerrada tónica.', 'error')],
 '3': [
   CLA('¿Con b o con v?', ['Con b', 'Con v'], [('cant_aba', 'Con b'), ('ha_lar', 'Con b'), ('_razo', 'Con b'), ('_amos (de ir)', 'Con v'), ('_oy (de ir)', 'Con v'), ('mir_aba', 'Con b')], 'Pretérito en -aba, bl y br: b. Verbo ir: v.', 'aplicar'),
   UNI('Uní cada palabra con su significado.', [('hay', 'existe'), ('ahí', 'en ese lugar'), ('ay', 'una queja'), ('hecho', 'del verbo hacer')], 'Los homófonos se distinguen por el significado.', 'aplicar'),
   SA('Completá con la forma correcta: «Nadie sabe el ___ de su enojo».', ['porqué'], 'Con artículo y significando «el motivo»: porqué, junto y con tilde.', 'aplicar'),
   MC('Juli escribió: «No fui a la clase por qué estaba enferma». ¿Qué error cometió?', ['Va «porque», porque da la causa', 'Va «porqué», porque es un sustantivo', 'No hay ningún error'], 'Va «porque», porque da la causa', 'Porque, junto y sin tilde, explica la causa.', 'error')],
 '4': [
   ORD('Ordená las pasadas para revisar un texto.', ['Leer para ver si se entiende', 'Revisar las tildes', 'Revisar las letras que confunden', 'Revisar mayúsculas y puntuación'], 'Primero el sentido, después lo demás, una cosa por vez.', 'aplicar'),
   TAP('Revisá en una pasada de letras y tildes. Tocá los TRES errores: «Ayer elejimos un lugar para el viaje: un jardin con un arbol enorme.»', ['Ayer', 'elejimos', 'un', 'lugar', 'para', 'el', 'viaje:', 'un', 'jardin', 'con', 'un', 'arbol', 'enorme.'], [1, 8, 11], 'Elegimos (de elegir), jardín (aguda en n), árbol (grave en l).', 'error'),
   MC('El corrector del celular no marcó nada en «Ya está echo el trabajo». ¿Qué conviene hacer?', ['Revisar igual: va «hecho», de hacer', 'Confiar: el corrector no se equivoca', 'Cambiar la frase entera'], 'Revisar igual: va «hecho», de hacer', 'El corrector solo marca palabras que no existen.', 'analizar'),
   MC('Mateo revisa su texto una sola vez buscando todos los errores juntos y se le escapan varios. ¿Qué le recomendás?', ['Revisar en pasadas, una cosa por vez', 'Escribir más rápido', 'No revisar nada'], 'Revisar en pasadas, una cosa por vez', 'Si la atención se reparte, se escapan errores.', 'analizar')],
 '5': [
   CLA('¿Qué regla explica cada palabra?', ['Esdrújula', 'Hiato', 'Pretérito en -aba', 'Verbo en -ger'], [('pájaro', 'Esdrújula'), ('maíz', 'Hiato'), ('saltaba', 'Pretérito en -aba'), ('proteger', 'Verbo en -ger')], 'Repasá las reglas de la misión.', 'analizar'),
   TAP('Tocá los TRES errores: «Cuando eramos chicos, mi abuelo nos contava historias debajo del arbol.»', ['Cuando', 'eramos', 'chicos,', 'mi', 'abuelo', 'nos', 'contava', 'historias', 'debajo', 'del', 'arbol.'], [1, 6, 10], 'Éramos (esdrújula), contaba (-aba con b), árbol (grave en l).', 'error'),
   UNI('Uní cada oración con la palabra que la completa.', [('___ un error en la cuenta', 'Hay'), ('Dejalo ___, sobre la mesa', 'ahí'), ('¿___ no viniste?', 'Por qué'), ('No vine ___ llovía', 'porque')], 'Pensá el significado de cada hueco.', 'aplicar'),
   ORD('Ordená los pasos para decidir si una palabra lleva tilde.', ['Separarla en sílabas', 'Encontrar la sílaba tónica', 'Clasificarla en aguda, grave o esdrújula', 'Aplicar la regla según la última letra'], 'Así se decide cualquier tilde.', 'aplicar')],
}

EX = [
 [1, CLA('Clasificá según la sílaba tónica.', ['Aguda', 'Grave', 'Esdrújula'], [('canción', 'Aguda'), ('lápiz', 'Grave'), ('teléfono', 'Esdrújula'), ('reloj', 'Aguda')], 'Contá desde el final.', 'aplicar')],
 [1, SA('Escribí con su tilde la palabra que completa: «Ayer mi mamá ___ (cocinar) ravioles».', ['cocinó'], 'Pasado, aguda terminada en vocal: cocinó.', 'aplicar')],
 [1, TF('Todas las palabras esdrújulas llevan tilde.', 'Verdadero', 'Es la única regla sin excepciones.', 'recordar')],
 [2, CLA('¿Diptongo o hiato?', ['Diptongo', 'Hiato'], [('nieve', 'Diptongo'), ('río', 'Hiato'), ('cuota', 'Diptongo'), ('poema', 'Hiato')], 'Separá en sílabas.', 'aplicar')],
 [2, MC('¿Cuál está bien escrita?', ['raíz', 'raiz', 'ráiz'], 'raíz', 'Hiato con i tónica: tilde en la i.', 'aplicar')],
 [2, TF('En un diptongo, la tilde siempre va en la vocal cerrada.', 'Falso', 'En el diptongo, si lleva tilde, va en la vocal abierta: camión, huésped.', 'recordar')],
 [3, CLA('¿B o v?', ['Con b', 'Con v'], [('pase_aba', 'Con b'), ('ha_lar', 'Con b'), ('_amos (de ir)', 'Con v'), ('_rújula', 'Con b')], 'Pretérito en -aba, bl, br; verbo ir.', 'aplicar')],
 [3, MC('¿Cuál completa «Ya está ___ la tarea»?', ['hecha', 'echa', 'hacha'], 'hecha', 'Es del verbo hacer: con h.', 'aplicar')],
 [3, UNI('Uní cada palabra con su uso.', [('por qué', 'pregunta'), ('porque', 'da la causa'), ('porqué', 'el motivo')], 'Tres formas, tres usos.', 'recordar')],
 [4, ORD('Ordená las pasadas de revisión.', ['Que se entienda', 'Tildes', 'Letras', 'Mayúsculas y puntuación'], 'Una cosa por vez.', 'recordar')],
 [4, TAP('Tocá los DOS errores: «Mañana vamos haber la pelicula en el cine.»', ['Mañana', 'vamos', 'haber', 'la', 'pelicula', 'en', 'el', 'cine.'], [2, 4], 'A ver (mirar) y película (esdrújula).', 'error')],
 [4, MC('¿Por qué el corrector del celular no marca «echo» en «ya está echo»?', ['Porque «echo» existe, aunque no corresponda', 'Porque está bien escrito en esa frase', 'Porque los correctores no revisan nada'], 'Porque «echo» existe, aunque no corresponda', 'El corrector no entiende el significado.', 'analizar')],
 [4, KW('Explicá con tus palabras cómo revisarías un texto antes de entregarlo.', 'Nombrá las pasadas y al menos una herramienta.', [['pasada*', 'varias veces', 'releer', 'rele*', 'de a una', 'por vez'], ['tilde*', 'letra*', 'puntua*', 'mayúscula*', 'sentido', 'entienda'], ['diccionario', 'voz alta', 'corrector']], 3, 'Por ejemplo: lo releo en pasadas (sentido, tildes, letras, puntuación), en voz alta, y uso el diccionario ante la duda.', 'aplicar')],
]

def ajustes(M):
    M['act'] = A
    M['examen'] = EX
    M['practica'] = 'Actividades generales'
    M['actualizar_preguntas'] = True

if __name__ == '__main__':
    guardar('contenido/lengua-1/mision-7/mision-7.json', L, ajustes=ajustes)
