# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 7 · Servicios que llegan a casa: las 4 clases animadas.
Metáfora: los caminos invisibles que llegan a casa. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-soc1-m7-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = '67d2ad89-caaa-4e82-8d25-8bbb08147818'
TEMA = 7
TIT = {1: 'La luz y el gas en mi casa', 2: 'El recorrido de la basura', 3: 'Cartero, bomberos y policía', 4: 'Quiénes trabajan en los servicios'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¡Se cortó la luz en casa!"}, {"yo": True, "txt": "¿Y LA HELADERA?"}, {"yo": False, "txt": "¡No anda nada!"}], "titulo": "LA LUZ", "sub": "y el gas",
  "voz": ["Tomi le escribe a Sofi.", "¡Se cortó la *luz* en casa!", "¡No anda nada!", "Hoy: *la luz y el gas en mi casa*."]},
 {"t": "partes", "emoji": "🏠", "titulo": "MI CASA", "partes": [{"txt": "LÁMPARA: LUZ", "x": 0.0, "y": -0.7}, {"txt": "COCINA: GAS", "x": -0.6, "y": 0.4}, {"txt": "CANILLA: AGUA", "x": 0.6, "y": 0.4}, {"txt": "ENCHUFE: LUZ", "x": 0.6, "y": -0.2}],
  "voz": ["Miramos una *casa* por dentro.", "La *lámpara* usa luz.", "La *cocina* usa gas.", "La *canilla* trae agua.", "El *enchufe* da luz."]},
 {"t": "causas", "causa": {"txt": "SI SE CORTA LA LUZ", "emoji": "🔌"}, "items": ["NO ANDA LA LÁMPARA", "NO ANDA LA HELADERA", "NO ANDA LA TELE"],
  "voz": ["¿Qué pasa si se corta la *luz*?", "No anda la *lámpara*.", "No anda la *heladera*.", "Y no anda la *tele*."]},
 {"t": "pregunta", "pregunta": "¿Qué usa la cocina?", "opciones": ["LUZ", "GAS", "AGUA"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en la cocina.", "¿Qué servicio usa?", "¡El *gas*!"]},
 {"t": "consejo", "titulo": "CUIDADO", "texto": "Los enchufes no se tocan con las manos mojadas", "emoji": "⚠️",
  "voz": ["Importante: nunca toques un enchufe *mojado*."]},
 {"t": "resumen", "items": [["SERVICIO", "llega a casa"], ["LUZ", "por cables"], ["GAS", "por caños"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los *servicios* llegan a casa.", "La *luz* viene por cables.", "El *gas* viene por caños.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🗑️", "lineas": ["Sofi saca la bolsa a la vereda.", "De noche pasa el camión.", "¿Adónde va la basura?"], "titulo": "LA BASURA", "sub": "su recorrido",
  "voz": ["Sofi saca la bolsa a la *vereda*.", "De noche pasa el *camión*.", "¿Adónde va la basura?", "Hoy: *el recorrido de la basura*."]},
 {"t": "flujo", "titulo": "EL RECORRIDO", "items": ["TACHO", "VEREDA", "CAMIÓN", "PLANTA"],
  "voz": ["Primero, va al *tacho*.", "Después, a la *vereda*.", "La lleva el *camión*.", "Y llega a la *planta*."]},
 {"t": "ciclo", "titulo": "UNA BOTELLA RECICLADA", "items": ["LA USO", "LA SEPARO", "LA FUNDEN", "BOTELLA NUEVA"],
  "voz": ["Una botella puede *reciclarse*.", "Primero, la *uso*.", "Después, la *separo*.", "En la fábrica la *funden*.", "¡Y es una *botella nueva*!"]},
 {"t": "pregunta", "pregunta": "¿Qué se recicla?", "opciones": ["BOTELLA", "CÁSCARA", "TIERRA"], "correcta": 0,
  "voz": ["Ahora vos. Botella, cáscara, tierra.", "¿Cuál se recicla?", "¡La *botella*!"]},
 {"t": "consejo", "titulo": "SEPARÁ", "texto": "Papel, plástico y vidrio por separado", "emoji": "♻️",
  "voz": ["Truco: *separá* la basura en casa."]},
 {"t": "resumen", "items": [["RECORRIDO", "tacho, vereda, camión"], ["SEPARAR", "papel, plástico, vidrio"], ["RECICLAR", "cosas nuevas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La basura hace un *recorrido*.", "La *separamos* en casa.", "Y se puede *reciclar*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Quién trae las cartas a casa?", "segundos": 6, "respuesta": "¡EL CARTERO!", "emoji": "📬", "titulo": "NOS AYUDAN", "sub": "cartero, bomberos, policía",
  "voz": ["Desafío: ¿quién trae las cartas a casa?", "¡El *cartero*!", "Hoy: *cartero, bomberos y policía*."]},
 {"t": "matriz", "titulo": "¿QUÉ HACE CADA UNO?", "celdas": [{"cab": "📬 CARTERO", "txt": "TRAE CARTAS"}, {"cab": "🚒 BOMBEROS", "txt": "APAGAN FUEGO"}, {"cab": "👮 POLICÍA", "txt": "NOS CUIDA"}, {"cab": "🚑 AMBULANCIA", "txt": "LLEVA ENFERMOS"}],
  "voz": ["Muchos nos *ayudan*.", "El *cartero* trae cartas.", "Los *bomberos* apagan el fuego.", "La *policía* nos cuida.", "La *ambulancia* lleva enfermos."]},
 {"t": "antesdespues", "antes": {"cab": "INCENDIO", "emoji": "🔥", "texto": "Se quema un pastizal"}, "despues": {"cab": "APAGADO", "emoji": "🚒", "texto": "¡Los bomberos llegaron!"},
  "voz": ["Se quema un *pastizal*.", "¡Llegan los *bomberos* y lo apagan!"]},
 {"t": "pregunta", "pregunta": "Te perdiste en la plaza. ¿A quién buscás?", "opciones": ["UN DESCONOCIDO", "UN POLICÍA", "NADIE"], "correcta": 1,
  "voz": ["Ahora vos. Te perdiste en la plaza.", "¿A quién buscás?", "¡A un *policía* o a un adulto de confianza!"]},
 {"t": "consejo", "titulo": "AVISÁ", "texto": "En una emergencia, avisá a un adulto", "emoji": "🚨",
  "voz": ["Importante: en una emergencia, avisá a un *adulto*."]},
 {"t": "resumen", "items": [["CARTERO", "trae cartas"], ["BOMBEROS", "apagan fuego"], ["POLICÍA", "cuida"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *cartero* trae cartas.", "Los *bomberos* apagan fuego.", "La *policía* nos cuida.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡VOLVIÓ LA LUZ AL BARRIO!", "bajada": "Gracias a los electricistas", "emoji": "💡", "titulo": "QUIÉNES TRABAJAN", "sub": "en los servicios",
  "voz": ["¡Último momento! Volvió la *luz* al barrio.", "Gracias a los *electricistas*.", "Hoy: *quiénes trabajan en los servicios*."]},
 {"t": "bloques", "titulo": "TRABAJAN PARA TODOS", "items": [{"cab": "⚡", "txt": "ELECTRICISTA: LUZ"}, {"cab": "🔥", "txt": "GASISTA: GAS"}, {"cab": "🗑️", "txt": "RECOLECTOR: BASURA"}, {"cab": "📬", "txt": "CARTERO: CARTAS"}],
  "voz": ["Muchas personas trabajan en los *servicios*.", "El *electricista* arregla la luz.", "El *gasista* arregla el gas.", "El *recolector* junta la basura.", "El *cartero* trae cartas."]},
 {"t": "linea", "titulo": "LA NOCHE DEL RECOLECTOR", "eventos": [{"fecha": "1", "txt": "SALE DE NOCHE", "emoji": "🌙"}, {"fecha": "2", "txt": "RECORRE EL BARRIO", "emoji": "🚛"}, {"fecha": "3", "txt": "DESCARGA", "emoji": "♻️"}, {"fecha": "4", "txt": "VUELVE A CASA", "emoji": "🏠"}],
  "voz": ["El recolector sale de *noche*.", "*Recorre* el barrio.", "*Descarga* la basura.", "Y *vuelve* a su casa."]},
 {"t": "pregunta", "pregunta": "No hay luz en casa. ¿Quién la arregla?", "opciones": ["GASISTA", "ELECTRICISTA", "CARTERO"], "correcta": 1,
  "voz": ["Ahora vos. No hay luz en casa.", "¿Quién la arregla?", "¡El *electricista*!"]},
 {"t": "consejo", "titulo": "GRACIAS", "texto": "Saludá a quienes trabajan en tu barrio", "emoji": "👋",
  "voz": ["Truco: *agradecé* a quienes trabajan."]},
 {"t": "resumen", "items": [["TRABAJOS", "electricista, gasista, recolector"], ["TURNOS", "día y noche"], ["GRACIAS", "nos ayudan a todos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Muchos *trabajan* en los servicios.", "Algunos trabajan de *noche*.", "¡Les decimos *gracias*!", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Sociales 1", "titulo": TIT[n], "sub": f"Ciencias Sociales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
