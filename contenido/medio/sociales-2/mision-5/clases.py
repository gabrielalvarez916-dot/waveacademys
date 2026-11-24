# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 5 · Caminos y transportes: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (viaja del campo a la ciudad).
Genera tools/medio/clase/lecciones/medio-soc2-m5-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '3b1f281f-3ce1-4a75-bfb4-2f3561b9217b', 2: 'daafd614-22fa-469e-9f6b-e0244dc5ef19', 3: '61dc42dd-18a0-4fb5-b08b-21c53673f256', 4: '1988f139-e1ac-41fc-850a-45885ac98640'}
TIT = {1: 'Rutas, caminos y vías', 2: 'Camiones, trenes y barcos de carga', 3: 'Cómo llega la comida a la ciudad', 4: 'Mapas de recorridos'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."

N1 = [
 {"t": "reto", "texto": "¿Cómo se llega de la ciudad al campo?", "segundos": 8, "respuesta": "¡Por rutas y caminos!", "emoji": "🛣️", "titulo": "RUTAS", "sub": "caminos y vías",
  "voz": ["Desafío: ¿cómo se llega al *campo*?", "¡Por *rutas* y caminos!", "Hoy: *rutas, caminos y vías*."]},
 {"t": "partes", "emoji": "🗺️", "titulo": "CAMINOS", "partes": [{"txt": "RUTA", "x": 0, "y": -0.8}, {"txt": "CAMINO DE TIERRA", "x": -0.7, "y": 0}, {"txt": "VÍAS DEL TREN", "x": 0.7, "y": 0}, {"txt": "RÍO", "x": 0, "y": 0.8}],
  "voz": ["Hay muchos caminos para viajar.", "La *ruta*, asfaltada.", "El *camino de tierra*, en el campo.", "Las *vías*, para el tren.", "Y el *río*, para los barcos."]},
 {"t": "vof", "afirmacion": "El tren va por la ruta", "emoji": "🚆", "verdadero": False, "explicacion": "El tren va por las vías",
  "voz": ["¿Verdadero o falso? El tren va por la ruta.", "Pensá en los rieles…", "¡*Falso*! Va por las *vías*."]},
 {"t": "pregunta", "pregunta": "¿Qué camino se llena de barro con lluvia?", "opciones": ["EL DE TIERRA", "LA RUTA"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuál se llena de barro?", "Pensá en la lluvia.", "¡El camino de *tierra*!"]},
 {"t": "definicion", "palabra": "Ruta", "texto": "Camino asfaltado y largo que une pueblos y ciudades", "emoji": "🛣️",
  "voz": ["Una *ruta* es un camino asfaltado y largo.", "Une el *campo* con pueblos y ciudades."]},
 {"t": "datoloco", "texto": "Sin caminos, la comida no llegaría a la ciudad", "emoji": "🥬",
  "voz": ["¿Sabías qué?", "¡Sin caminos, la comida no llegaría a la *ciudad*!"]},
 {"t": "consejo", "titulo": "CUIDADO CON LAS VÍAS", "texto": "Se cruzan solo por el paso a nivel", "emoji": "🚧",
  "voz": ["Truco: cruzá las vías solo por el *paso a nivel*."]},
 {"t": "resumen", "items": [["RUTA", "asfaltada"], ["CAMINO DE TIERRA", "en el campo"], ["VÍAS", "para el tren"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *ruta* es asfaltada.", "El camino de *tierra* está en el campo.", "Las *vías* son para el tren.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "VIAJE", "titular": "¡Lola viaja en un tren de carga!", "bajada": "Lleva granos al puerto", "emoji": "🚂", "titulo": "CAMIONES", "sub": "trenes y barcos",
  "voz": ["¡Noticia: Lola viaja en un tren de *carga*!", "Lleva granos al *puerto*.", "Hoy: *camiones, trenes y barcos*."]},
 {"t": "escala", "titulo": "¿CUÁNTA CARGA LLEVA?", "items": [{"txt": "CAMIÓN", "emoji": "🚚", "valor": 2}, {"txt": "TREN", "emoji": "🚂", "valor": 6}, {"txt": "BARCO", "emoji": "🚢", "valor": 10}],
  "voz": ["El *camión* lleva un poco.", "El *tren* lleva más.", "¡El *barco* lleva muchísimo!"]},
 {"t": "prediccion", "pregunta": "¿Qué transporte cruza el mar?", "a": {"txt": "EL BARCO", "emoji": "🚢"}, "b": {"txt": "EL CAMIÓN", "emoji": "🚚"}, "correcta": "a", "resultado": "El barco lleva la carga a otros países",
  "voz": ["¿Qué transporte cruza el *mar*?", "Pensá…", "¡El *barco*! Lleva carga a otros países."]},
 {"t": "pregunta", "pregunta": "¿Por dónde va el camión?", "opciones": ["POR LA RUTA", "POR EL RÍO"], "correcta": 0,
  "voz": ["Ahora vos: ¿por dónde va el camión?", "Pensá en el asfalto.", "¡Por la *ruta*!"]},
 {"t": "pasos", "titulo": "EL VIAJE DE LA SOJA", "items": [{"txt": "Camión: sale del campo", "emoji": "🚚"}, {"txt": "Tren: va al puerto", "emoji": "🚂"}, {"txt": "Barco: a otro país", "emoji": "🚢"}],
  "voz": ["Veamos un ejemplo: el viaje de la *soja*.", "Un *camión* la saca del campo por la ruta.", "Un *tren* la lleva por las vías hasta el puerto.", "En el puerto la cargan en un *barco* enorme."]},
 {"t": "datoloco", "texto": "Un barco grande lleva más carga que muchísimos camiones", "emoji": "🚢",
  "voz": ["¿Sabías qué?", "¡Un barco lleva más carga que *muchísimos* camiones juntos!"]},
 {"t": "consejo", "titulo": "¿POR DÓNDE VA?", "texto": "Ruta, vías o agua", "emoji": "🧭",
  "voz": ["Truco: mirá por dónde va: *ruta*, vías o agua."]},
 {"t": "resumen", "items": [["CAMIÓN", "por la ruta"], ["TREN", "por las vías"], ["BARCO", "por el agua"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *camión* va por la ruta.", "El *tren*, por las vías.", "El *barco*, por el agua.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Mamá", "emoji": "👩"}, "mensajes": [{"yo": False, "txt": "¿De dónde vino esta lechuga? 🥬"}, {"yo": True, "txt": "¡Voy a averiguarlo!"}], "titulo": "CÓMO LLEGA", "sub": "la comida",
  "voz": ["Mamá pregunta: ¿de dónde vino esta *lechuga*?", "Lola responde: ¡voy a *averiguarlo*!", "Hoy: *cómo llega la comida*."]},
 {"t": "linea", "titulo": "EL VIAJE DE LA LECHUGA", "eventos": [{"fecha": "1", "txt": "quinta", "emoji": "🥬"}, {"fecha": "2", "txt": "camión", "emoji": "🚚"}, {"fecha": "3", "txt": "mercado", "emoji": "🏬"}, {"fecha": "4", "txt": "verdulería", "emoji": "🛒"}],
  "voz": ["La cosechan en la *quinta*.", "Viaja en *camión*.", "Llega al *mercado*.", "¡Y la venden en la *verdulería*!"]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Despistado", "emoji": "👾"}, "preguntas": [{"p": "¿Dónde crece la lechuga?", "r": "EN LA QUINTA"}, {"p": "¿Dónde compran los verduleros?", "r": "EN EL MERCADO"}],
  "voz": ["¡Apareció el *Monstruo Despistado*!", "No sabe de dónde viene la comida.", "La lechuga crece en la *quinta*.", "Los verduleros compran en el *mercado*. ¡Ganamos!"]},
 {"t": "pregunta", "pregunta": "¿Por qué la verdura viaja rápido?", "opciones": ["PARA ESTAR FRESCA", "PARA JUGAR"], "correcta": 0,
  "voz": ["Ahora vos: ¿por qué viaja rápido?", "Pensá en la lechuga.", "¡Para estar *fresca*!"]},
 {"t": "pasos", "titulo": "LAS NARANJAS", "items": [{"txt": "Se cosechan", "emoji": "🍊"}, {"txt": "Viajan en camión", "emoji": "🚚"}, {"txt": "Llegan al mercado", "emoji": "🏬"}, {"txt": "Las compramos", "emoji": "🛒"}],
  "voz": ["Otro ejemplo: las *naranjas*.", "Primero las *cosechan* en el campo.", "Después viajan en *camión* toda la noche.", "Llegan al *mercado* muy temprano.", "¡Y las compramos en la verdulería!"]},
 {"t": "consejo", "titulo": "PREGUNTÁ", "texto": "¿De dónde viene lo que comés?", "emoji": "🎤",
  "voz": ["Truco: preguntá de dónde viene lo que *comés*."]},
 {"t": "resumen", "items": [["QUINTA", "se cosecha"], ["MERCADO", "se vende a negocios"], ["VERDULERÍA", "la compramos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En la *quinta* se cosecha.", "En el *mercado* se vende a los negocios.", "En la *verdulería* la compramos.", CIERRE]},
]
N4 = [
 {"t": "zoom", "niveles": [{"emoji": "🗺️", "txt": "UN MAPA"}, {"emoji": "🏘️", "txt": "EL BARRIO DE LOLA"}, {"emoji": "➡️", "txt": "¡SU RECORRIDO A LA ESCUELA!"}],
  "voz": ["Miramos un *mapa*.", "Más cerca: el *barrio* de Lola.", "¡Su *recorrido* a la escuela! Hoy: *mapas*."]},
 {"t": "dialogo", "personas": [{"nombre": "LOLA", "emoji": "👧"}, {"nombre": "SEÑORA", "emoji": "👵"}], "lineas": [{"quien": 1, "txt": "¿Cómo llego a la escuela?"}, {"quien": 0, "txt": "Siga derecho hasta la plaza."}, {"quien": 0, "txt": "Pase el kiosco: ¡ahí está!"}],
  "voz": ["¿Cómo llego a la escuela?", "Siga derecho hasta la *plaza*.", "Pase el *kiosco*: ¡ahí está!"]},
 {"t": "definicion", "palabra": "Referencias", "texto": "Dibujitos que explican qué es cada cosa en el mapa", "emoji": "🔑",
  "voz": ["Las *referencias* explican el mapa.", "Siempre miralas primero."]},
 {"t": "pregunta", "pregunta": "¿Con qué se marca un recorrido?", "opciones": ["CON UNA LÍNEA", "CON UN SELLO"], "correcta": 0,
  "voz": ["Ahora vos: ¿con qué se marca un recorrido?", "Pensá en el mapa.", "¡Con una *línea* o flechas!"]},
 {"t": "pasos", "titulo": "LEER UN RECORRIDO", "items": [{"txt": "Busco el número 1", "emoji": "1️⃣"}, {"txt": "Sigo la línea", "emoji": "➡️"}, {"txt": "Miro las referencias", "emoji": "🔑"}, {"txt": "Llego al final", "emoji": "🏁"}],
  "voz": ["Leemos el recorrido de Lola, paso a paso.", "Busco el *número uno*: la casa.", "Sigo la *línea*: plaza y kiosco.", "Miro las *referencias* para entender cada dibujito.", "¡Llego al final: la *escuela*!"]},
 {"t": "datoloco", "texto": "Un mapa muestra los lugares vistos desde arriba", "emoji": "🦅",
  "voz": ["¿Sabías qué?", "Un mapa muestra todo desde *arriba*, como si volaras."]},
 {"t": "consejo", "titulo": "SEGUÍ LA LÍNEA", "texto": "Empezá por el número 1", "emoji": "1️⃣",
  "voz": ["Truco: seguí la línea desde el *número uno*."]},
 {"t": "resumen", "items": [["RECORRIDO", "de un lugar a otro"], ["LÍNEA", "marca el camino"], ["REFERENCIAS", "explican el mapa"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *recorrido* va de un lugar a otro.", "La *línea* marca el camino.", "Las *referencias* explican el mapa.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc2-m5-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Sociales 2", "titulo": TIT[n], "sub": f"Ciencias Sociales 2 · Misión 5 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
