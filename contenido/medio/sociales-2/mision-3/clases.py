# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 3 · Normas que protegen: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (investiga las reglas que nos cuidan).
Genera tools/medio/clase/lecciones/medio-soc2-m3-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '596ad46a-0f19-4831-af95-7182db211e25', 2: '768d7797-8325-4e18-81ad-3ff27a137d84', 3: '564a729e-fab5-46cd-ad55-e1457c9f040f', 4: 'd663578e-597b-4f13-b208-2f82dbf59ee9'}
TIT = {1: 'Normas de seguridad en el trabajo', 2: 'Etiquetas y fechas de vencimiento', 3: 'Derechos de los consumidores', 4: 'Trabajos con y sin descanso'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."

N1 = [
 {"t": "reto", "texto": "¿Por qué el albañil usa casco?", "segundos": 8, "respuesta": "¡Para cuidar su cabeza!", "emoji": "⛑️", "titulo": "NORMAS", "sub": "de seguridad",
  "voz": ["Desafío: ¿por qué el albañil usa *casco*?", "¡Para cuidar su *cabeza*!", "Hoy: *normas de seguridad*."]},
 {"t": "zoom", "niveles": [{"emoji": "🏗️", "txt": "UNA OBRA"}, {"emoji": "👷", "txt": "UN ALBAÑIL"}, {"emoji": "⛑️", "txt": "¡SU CASCO LO CUIDA!"}],
  "voz": ["Miramos una *obra*.", "Más cerca: un *albañil*.", "¡Su *casco* lo cuida!"]},
 {"t": "unir", "titulo": "¿QUÉ SE PONE?", "pares": [["ALBAÑIL", "casco"], ["BOMBERA", "traje especial"], ["COCINERO", "gorro"]], "mezclar": True,
  "voz": ["Unimos cada trabajo con su protección.", "El albañil: *casco*.", "La bombera: *traje especial*.", "El cocinero: *gorro*."]},
 {"t": "vof", "afirmacion": "Las normas de seguridad no sirven", "emoji": "⚠️", "verdadero": False, "explicacion": "Cuidan a los trabajadores",
  "voz": ["¿Verdadero o falso? Las normas no sirven.", "Pensá en el casco…", "¡*Falso*! Cuidan a los trabajadores."]},
 {"t": "pasos", "titulo": "PEDRO EN LA OBRA", "items": [{"txt": "Se pone el casco", "emoji": "⛑️"}, {"txt": "Se pone guantes", "emoji": "🧤"}, {"txt": "Usa botas fuertes", "emoji": "🥾"}, {"txt": "Lee los carteles", "emoji": "🚧"}],
  "voz": ["Pedro es albañil. Así se cuida, paso a paso.", "Se pone el *casco*: cuida su cabeza.", "Se pone *guantes*: cuida sus manos.", "Usa *botas* fuertes: cuida sus pies.", "Y lee los *carteles* de peligro."]},
 {"t": "consejo", "titulo": "MIRÁ LOS CARTELES", "texto": "Avisan peligros y salidas", "emoji": "🚧",
  "voz": ["Truco: mirá los *carteles*: avisan peligros."]},
 {"t": "resumen", "items": [["NORMA", "regla para todos"], ["SEGURIDAD", "cuida a las personas"], ["PROTECCIÓN", "casco, gorro, guantes"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *norma* es una regla para todos.", "La *seguridad* cuida a las personas.", "Nos protegen el casco y los *guantes*.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "INVESTIGACIÓN", "titular": "¡Lola lee la etiqueta del yogur!", "bajada": "Tiene mucha información", "emoji": "🏷️", "titulo": "ETIQUETAS", "sub": "y vencimiento",
  "voz": ["¡Noticia: Lola lee la *etiqueta* del yogur!", "Tiene mucha información.", "Hoy: *etiquetas y vencimiento*."]},
 {"t": "partes", "emoji": "🥛", "titulo": "LA ETIQUETA", "partes": [{"txt": "NOMBRE", "x": 0, "y": -0.8}, {"txt": "INGREDIENTES", "x": -0.7, "y": 0}, {"txt": "PESO", "x": 0.7, "y": 0}, {"txt": "VENCIMIENTO", "x": 0, "y": 0.8}],
  "voz": ["Miramos la etiqueta del yogur.", "El *nombre* del producto.", "Los *ingredientes*: lo que tiene.", "El *peso*: cuánto trae.", "Y la fecha de *vencimiento*."]},
 {"t": "pistas", "problema": "¿Qué parte de la etiqueta es?", "pistas": ["Es una fecha", "Dice hasta cuándo comer", "Si pasó, no se come"], "respuesta": "¡EL VENCIMIENTO! 📅",
  "voz": ["Adivinanza: ¿qué parte de la etiqueta es?", "Pista uno: es una fecha.", "Pista dos: dice hasta cuándo comer.", "Pista tres: si pasó, no se come.", "¡El *vencimiento*!"]},
 {"t": "pregunta", "pregunta": "¿Un producto vencido se come?", "opciones": ["NO", "SÍ"], "correcta": 0,
  "voz": ["Ahora vos: ¿un producto vencido se come?", "Pensá en la fecha.", "¡*No*! Puede hacer mal."]},
 {"t": "datoloco", "texto": "Si un producto está vencido, puede hacernos mal", "emoji": "⚠️",
  "voz": ["¿Sabías qué?", "Un producto *vencido* puede hacernos mal a la panza."]},
 {"t": "consejo", "titulo": "MIRÁ LA FECHA", "texto": "Antes de comer, mirá el vencimiento", "emoji": "📅",
  "voz": ["Truco: antes de comer, mirá el *vencimiento*."]},
 {"t": "resumen", "items": [["ETIQUETA", "información"], ["INGREDIENTES", "lo que tiene"], ["VENCIMIENTO", "hasta cuándo se come"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *etiqueta* tiene información.", "Los *ingredientes* dicen lo que tiene.", "El *vencimiento*, hasta cuándo se come.", CIERRE]},
]
N3 = [
 {"t": "dialogo", "personas": [{"nombre": "LOLA", "emoji": "👧"}, {"nombre": "ALMACENERO", "emoji": "👨‍🍳"}], "lineas": [{"quien": 0, "txt": "Este yogur vino vencido. Acá está el ticket."}, {"quien": 1, "txt": "¡Perdón! Te lo cambio ya."}, {"quien": 0, "txt": "¡Muchas gracias!"}],
  "voz": ["Este yogur vino *vencido*. Acá está el ticket.", "¡Perdón! Te lo *cambio* ya.", "¡Muchas gracias!"]},
 {"t": "definicion", "palabra": "Consumidor", "texto": "La persona que compra y usa un producto", "emoji": "🛒",
  "voz": ["Lola es una *consumidora*: compra y usa.", "Y tiene *derechos*."]},
 {"t": "escape", "titulo": "EL ALMACÉN", "candados": [{"p": "¿Qué llevo para reclamar?", "r": "EL TICKET"}, {"p": "¿Cómo reclamo?", "r": "CON RESPETO"}],
  "voz": ["¡Para salir del almacén, abrimos los candados!", "Para reclamar, llevo el *ticket*.", "Reclamo *con respeto*.", "¡Salimos!"]},
 {"t": "pregunta", "pregunta": "Si el juguete vino roto, ¿puedo reclamar?", "opciones": ["SÍ", "NO"], "correcta": 0,
  "voz": ["Ahora vos: ¿si vino roto, puedo reclamar?", "Pensá en los derechos.", "¡*Sí*! Es mi derecho."]},
 {"t": "pasos", "titulo": "CÓMO RECLAMAR", "items": [{"txt": "Busco el ticket", "emoji": "🧾"}, {"txt": "Vuelvo al negocio", "emoji": "🏪"}, {"txt": "Explico con respeto", "emoji": "🗣️"}, {"txt": "Me lo cambian", "emoji": "🔄"}],
  "voz": ["¿Cómo se reclama? Veamos paso a paso.", "Primero busco el *ticket* de la compra.", "Vuelvo al *negocio* con el producto.", "Explico el problema con *respeto*, sin gritar.", "¡Y me lo *cambian*!"]},
 {"t": "consejo", "titulo": "GUARDÁ EL TICKET", "texto": "Muestra que lo compraste ahí", "emoji": "🧾",
  "voz": ["Truco: guardá el *ticket* de lo que comprás."]},
 {"t": "resumen", "items": [["CONSUMIDOR", "quien compra"], ["DERECHOS", "se respetan"], ["RECLAMAR", "con respeto"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *consumidor* es quien compra.", "Tiene *derechos* que se respetan.", "Puede *reclamar*, con respeto.", CIERRE]},
]
N4 = [
 {"t": "antesdespues", "antes": {"cab": "ANTES", "emoji": "😓", "texto": "Trabajaban todo el día sin descanso"}, "despues": {"cab": "AHORA", "emoji": "😊", "texto": "Horario, descanso y vacaciones"},
  "voz": ["*Antes*, muchos trabajaban sin descanso.", "*Ahora*, hay horario, descanso y *vacaciones*."]},
 {"t": "matriz", "titulo": "DERECHOS DEL TRABAJADOR", "celdas": [{"cab": "HORARIO ⏰", "txt": "hora de entrar y salir"}, {"cab": "DESCANSO ☕", "txt": "para comer y parar"}, {"cab": "VACACIONES 🏖️", "txt": "días libres"}],
  "voz": ["Hoy las leyes cuidan a los trabajadores.", "Tienen *horario*: hora de entrar y salir.", "Tienen *descanso* para comer.", "Y *vacaciones*: días libres."]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Sin Pausa", "emoji": "🤖"}, "preguntas": [{"p": "¿Los trabajadores descansan?", "r": "SÍ"}, {"p": "¿Los chicos trabajan?", "r": "NO"}],
  "voz": ["¡Apareció el *Monstruo Sin Pausa*!", "Quiere que todos trabajen sin parar.", "¿Los trabajadores descansan? ¡*Sí*!", "¿Los chicos trabajan? ¡*No*! ¡Ganamos!"]},
 {"t": "pregunta", "pregunta": "¿Qué tienen derecho a hacer los chicos?", "opciones": ["ESTUDIAR Y JUGAR", "TRABAJAR"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué hacen los chicos?", "Pensá en los derechos.", "¡*Estudiar* y jugar!"]},
 {"t": "pasos", "titulo": "CÓMO SE GANARON LOS DERECHOS", "items": [{"txt": "Trabajaban sin descanso", "emoji": "😓"}, {"txt": "Se juntaron a pedir", "emoji": "🤝"}, {"txt": "Se hicieron leyes", "emoji": "📜"}],
  "voz": ["¿Cómo llegaron estos derechos? Veamos.", "Antes, muchos trabajaban *sin descanso*.", "Los trabajadores se *juntaron* para pedir mejoras.", "Con el tiempo, se hicieron *leyes* que los cuidan."]},
 {"t": "consejo", "titulo": "LEYES", "texto": "Las leyes cuidan a los trabajadores", "emoji": "📜",
  "voz": ["Truco: las *leyes* cuidan a los trabajadores."]},
 {"t": "resumen", "items": [["ANTES", "sin descanso"], ["AHORA", "horario y vacaciones"], ["CHICOS", "estudian y juegan"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Antes*, sin descanso.", "*Ahora*, horario y vacaciones.", "Los *chicos* estudian y juegan.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc2-m3-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Sociales 2", "titulo": TIT[n], "sub": f"Ciencias Sociales 2 · Misión 3 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
