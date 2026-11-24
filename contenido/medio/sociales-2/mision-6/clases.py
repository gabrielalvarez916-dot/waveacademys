# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 6 · Vida cotidiana en la época colonial: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (viaja con la imaginación a la época colonial).
Genera tools/medio/clase/lecciones/medio-soc2-m6-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'ea541bea-84f0-461d-900f-5637037eee5f', 2: '2235151b-a1f7-487c-97e5-d30cb5dba95d', 3: 'a09a1353-2e32-49a5-bbbc-9e9d38700b57', 4: 'a07cbbaf-b16b-4cd0-8e96-e5966f7ad0f4'}
TIT = {1: 'Cómo era una casa colonial', 2: 'Velas y faroles para alumbrarse', 3: 'Trabajos y jerarquías de una época', 4: 'Comparamos con la vida de hoy'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
LOLA = {"nombre": "Lola", "emoji": "👧🎤"}

N1 = [
 {"t": "historia", "personaje": LOLA, "lugar": "🏛️", "lineas": ["Lola visita un museo.", "Hay una casa muy vieja.", "¡Es de la época colonial!"], "titulo": "LA CASA", "sub": "colonial",
  "voz": ["Lola visita un *museo*.", "Adentro hay una casa muy vieja.", "¡Es de la *época colonial*, hace más de doscientos años!", "Hoy: *cómo era una casa colonial*."]},
 {"t": "partes", "emoji": "🏠", "titulo": "LA CASA COLONIAL", "partes": [{"txt": "ZAGUÁN", "x": 0, "y": 0.8}, {"txt": "PATIO", "x": 0, "y": 0}, {"txt": "HABITACIONES", "x": -0.7, "y": -0.6}, {"txt": "ALJIBE", "x": 0.7, "y": -0.6}],
  "voz": ["Recorremos la casa con Lola.", "Entramos por el *zaguán*, un pasillo largo.", "En el medio está el *patio*, con plantas.", "Alrededor del patio están las *habitaciones*.", "Y en el patio, el *aljibe* con el agua."]},
 {"t": "documental", "emojis": ["🧱", "🪣", "🏚️"], "lugar": "🏛️", "rotulos": [{"txt": "PAREDES GRUESAS", "sub": "de adobe o ladrillo"}, {"txt": "ALJIBE", "sub": "agua de lluvia"}, {"txt": "RANCHOS", "sub": "casas de los pobres"}],
  "voz": ["Las paredes eran *gruesas*, de adobe o ladrillo.", "El *aljibe* juntaba el agua de la lluvia.", "Las familias pobres vivían en *ranchos* chicos."]},
 {"t": "pasos", "titulo": "SACAR AGUA DEL ALJIBE", "items": [{"txt": "Ir al patio", "emoji": "🚶"}, {"txt": "Bajar el balde", "emoji": "🪣"}, {"txt": "Subir el agua", "emoji": "💧"}],
  "voz": ["¿Cómo sacaban agua? Veamos paso a paso.", "Primero, iban al *patio*.", "Bajaban un *balde* atado con una soga.", "Y subían el *agua* de lluvia, ¡con fuerza!"]},
 {"t": "pregunta", "pregunta": "¿Había canillas en la casa colonial?", "opciones": ["NO, USABAN EL ALJIBE", "SÍ, MUCHAS"], "correcta": 0,
  "voz": ["Ahora vos: ¿había canillas en la casa colonial?", "Pensá en el patio.", "¡*No*! Usaban el aljibe."]},
 {"t": "consejo", "titulo": "MIRÁ EL PATIO", "texto": "Todo daba al patio", "emoji": "🌿",
  "voz": ["Truco: en la casa colonial, todo daba al *patio*."]},
 {"t": "resumen", "items": [["ZAGUÁN", "la entrada"], ["PATIO", "en el medio"], ["ALJIBE", "el agua"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *zaguán* era la entrada.", "El *patio* estaba en el medio.", "El *aljibe* guardaba el agua.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Cómo veían de noche, sin luz eléctrica?", "segundos": 8, "respuesta": "¡Con velas y faroles!", "emoji": "🕯️", "titulo": "VELAS", "sub": "y faroles",
  "voz": ["Desafío: ¿cómo veían de noche, sin electricidad?", "¡Con *velas* y *faroles*!", "Hoy: *velas y faroles*."]},
 {"t": "antesdespues", "antes": {"cab": "ANTES", "emoji": "🕯️", "texto": "Velas de sebo con humo"}, "despues": {"cab": "HOY", "emoji": "💡", "texto": "Lamparitas eléctricas"},
  "voz": ["*Antes*, velas de sebo, que hacían humo y olor.", "*Hoy*, apretamos un botón: ¡lamparitas eléctricas!"]},
 {"t": "personaje", "personaje": {"nombre": "Don Ramón, farolero", "emoji": "🧑‍🦳"}, "lineas": [{"txt": "¡Buenas tardes! Yo soy el farolero.", "animo": "feliz"}, {"txt": "Al atardecer, subo mi escalera.", "animo": "piensa"}, {"txt": "Prendo cada farol de la calle.", "animo": "feliz"}, {"txt": "¡Y a la mañana, los apago!", "animo": "sorpresa"}],
  "voz": ["¡Buenas tardes! Yo soy el *farolero*.", "Al atardecer, subo mi *escalera*.", "Prendo cada *farol* de la calle.", "¡Y a la mañana, los *apago*!"]},
 {"t": "datoloco", "texto": "Las velas se hacían con sebo, la grasa de las vacas", "emoji": "🐄",
  "voz": ["¿Sabías qué?", "¡Las velas eran de *sebo*: grasa de vaca!"]},
 {"t": "pregunta", "pregunta": "¿Quién prendía los faroles de la calle?", "opciones": ["EL FAROLERO", "EL AGUATERO"], "correcta": 0,
  "voz": ["Ahora vos: ¿quién prendía los faroles?", "Pensá en la escalera.", "¡El *farolero*!"]},
 {"t": "pasos", "titulo": "UNA NOCHE COLONIAL", "items": [{"txt": "Se hace de noche", "emoji": "🌙"}, {"txt": "Prenden una vela", "emoji": "🕯️"}, {"txt": "Leen cerca de la luz", "emoji": "📖"}],
  "voz": ["Imaginemos una noche en la época colonial.", "Se hace de *noche* y todo queda oscuro.", "La familia prende una *vela* de sebo.", "Se sientan bien cerca para poder *leer*."]},
 {"t": "consejo", "titulo": "CUIDADO CON EL FUEGO", "texto": "Las velas, solo con un adulto", "emoji": "🔥",
  "voz": ["Truco: las velas se prenden solo con un *adulto*."]},
 {"t": "resumen", "items": [["VELAS", "de sebo"], ["FAROLES", "en la calle"], ["FAROLERO", "los prendía"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *velas* eran de sebo.", "Los *faroles* alumbraban la calle.", "El *farolero* los prendía cada atardecer.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "VIAJE AL PASADO", "titular": "¡Se escuchan gritos en la calle!", "bajada": "Son los vendedores", "emoji": "📣", "titulo": "TRABAJOS", "sub": "de la época colonial",
  "voz": ["¡Noticia: se escuchan gritos en la calle colonial!", "Son los *vendedores*, anunciando lo que venden.", "Hoy: *trabajos de la época colonial*."]},
 {"t": "mazo", "titulo": "VENDEDORES", "items": [{"frente": "💧", "dorso": "AGUATERO: AGUA DEL RÍO", "emoji": "💧"}, {"frente": "🐴", "dorso": "LECHERO: LECHE A CABALLO", "emoji": "🐴"}, {"frente": "🥣", "dorso": "MAZAMORRERA: MAZAMORRA", "emoji": "🥣"}, {"frente": "🕯️", "dorso": "VELERO: VELAS", "emoji": "🕯️"}],
  "voz": ["El *aguatero* vendía agua del río en un carro.", "El *lechero* llegaba a caballo.", "La *mazamorrera* vendía un postre de maíz.", "El *velero* vendía velas."]},
 {"t": "versus", "titulo": "ANTES Y HOY", "a": {"txt": "ANTES", "emoji": "⛓️", "datos": ["no todos libres", "distintos derechos"]}, "b": {"txt": "HOY", "emoji": "🤝", "datos": ["todos libres", "mismos derechos"]}, "gana": "b", "veredicto": "¡Hoy la ley dice que somos iguales!",
  "voz": ["Antes, *no todos* tenían los mismos derechos.", "Había personas esclavizadas: obligadas a trabajar sin pago.", "*Hoy*, la ley dice que todos somos libres.", "¡Y tenemos los *mismos derechos*!"]},
 {"t": "pregunta", "pregunta": "¿Era justo esclavizar personas?", "opciones": ["NO, ERA INJUSTO", "SÍ"], "correcta": 0,
  "voz": ["Ahora vos: ¿era justo esclavizar personas?", "Pensá en los derechos.", "¡*No*! Era muy injusto."]},
 {"t": "pasos", "titulo": "COMPRAR AGUA", "items": [{"txt": "Esperan al aguatero", "emoji": "⏳"}, {"txt": "Llena la tinaja", "emoji": "🏺"}, {"txt": "Le pagan con monedas", "emoji": "🪙"}],
  "voz": ["¿Cómo compraban agua? Veamos paso a paso.", "La familia *espera* al aguatero en la puerta.", "El aguatero llena la *tinaja* con agua del río.", "Y le pagan con *monedas*."]},
 {"t": "consejo", "titulo": "¿QUÉ VENDE?", "texto": "El nombre dice qué vende", "emoji": "🔤",
  "voz": ["Truco: el *nombre* del trabajo dice qué vende."]},
 {"t": "resumen", "items": [["AGUATERO", "vendía agua"], ["MAZAMORRERA", "vendía mazamorra"], ["DERECHOS", "hoy, iguales"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *aguatero* vendía agua.", "La *mazamorrera* vendía mazamorra.", "Hoy todos tenemos los mismos *derechos*.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Abuela Rosa", "emoji": "👵"}, "mensajes": [{"yo": False, "txt": "¿Qué aprendiste del pasado? 🕰️"}, {"yo": True, "txt": "¡Que muchas cosas cambiaron!"}], "titulo": "COMPARAMOS", "sub": "con la vida de hoy",
  "voz": ["La abuela pregunta: ¿qué aprendiste del pasado?", "Lola responde: ¡que muchas cosas *cambiaron*!", "Hoy: *comparamos con la vida de hoy*."]},
 {"t": "matriz", "titulo": "ANTES Y HOY", "celdas": [{"cab": "AGUA 💧", "txt": "aljibe → canilla"}, {"cab": "LUZ 💡", "txt": "vela → lamparita"}, {"cab": "VIAJES 🐴", "txt": "caballo → colectivo"}, {"cab": "COMIDA 🥟", "txt": "¡empanadas igual!"}],
  "voz": ["Comparamos cuatro cosas.", "El *agua*: del aljibe a la canilla.", "La *luz*: de la vela a la lamparita.", "Los *viajes*: del caballo al colectivo.", "¡Pero las *empanadas* siguen igual!"]},
 {"t": "comparar", "a": {"cab": "CAMBIÓ", "texto": "AGUA, LUZ, VIAJES", "emoji": "🔄"}, "b": {"cab": "SIGUE IGUAL", "texto": "FAMILIA, JUEGOS, COMIDAS", "emoji": "🟰"}, "signo": "↔",
  "voz": ["Hacemos dos columnas.", "*Cambió*: el agua, la luz y los viajes.", "*Sigue igual*: la familia, los juegos y las comidas."]},
 {"t": "memoria", "titulo": "DE LA ÉPOCA COLONIAL", "items": ["ALJIBE", "VELA", "FAROL", "ZAGUÁN"], "falta": 1,
  "voz": ["Mirá estas cosas de la época colonial.", "Se tapan… ¡y una desapareció!", "¡Faltaba la *vela*!"]},
 {"t": "pregunta", "pregunta": "¿Comer empanadas cambió o sigue igual?", "opciones": ["SIGUE IGUAL", "CAMBIÓ"], "correcta": 0,
  "voz": ["Ahora vos: ¿comer empanadas cambió?", "Pensá en tu familia.", "¡*Sigue igual*!"]},
 {"t": "consejo", "titulo": "DOS COLUMNAS", "texto": "Cambió y sigue igual", "emoji": "📋",
  "voz": ["Truco: anotá en *dos columnas*: cambió y sigue igual."]},
 {"t": "resumen", "items": [["CAMBIÓ", "agua, luz, viajes"], ["SIGUE IGUAL", "familia y comidas"], ["COMPARAR", "antes y hoy"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Cambiaron* el agua, la luz y los viajes.", "*Siguen igual* la familia y las comidas.", "Comparar nos ayuda a entender el *pasado*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc2-m6-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Sociales 2", "titulo": TIT[n], "sub": f"Ciencias Sociales 2 · Misión 6 · Nivel {n}", "estilo": "primeros", "sin_variante": True, "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
