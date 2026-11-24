# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 7 · El ciclo del agua: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (mira el cielo un día de lluvia).
Genera tools/medio/clase/lecciones/medio-nat2-m7-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'dbae7eee-d25b-41d4-9325-34b060b98223', 2: '0fbfa7e9-071d-4f76-a479-0cad44c35754', 3: '914a6b32-cc42-4e5f-8944-66830153a1c7', 4: '50615502-010f-4f9d-95af-15c725826eb8'}
TIT = {1: 'Lluvia y nubes', 2: 'Ríos, lagos y mares', 3: 'El agua vuelve al cielo', 4: 'Medimos la lluvia'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "🧑‍🔬"}

N1 = [
 {"t": "historieta", "titulo": "UN DÍA DE LLUVIA", "vinetas": [{"emojis": ["☁️", "☁️"], "txt": "Hay nubes grises"}, {"emojis": ["💧", "💧"], "txt": "Las gotitas se juntan"}, {"emojis": ["🌧️", "☂️"], "txt": "¡Llueve!"}],
  "voz": ["Tomi mira el cielo: hay nubes grises.", "Adentro, las *gotitas* se juntan y pesan.", "¡Llueve! Hoy: *lluvia y nubes*."]},
 {"t": "definicion", "palabra": "Nube", "texto": "Muchas gotitas de agua juntas, allá arriba", "emoji": "☁️",
  "voz": ["Una *nube* son muchas gotitas de agua.", "Cuando se hacen pesadas, ¡caen!"]},
 {"t": "quiz4", "pregunta": "¿Qué cae cuando hace mucho frío arriba?", "opciones": ["GRANIZO", "HOJAS", "ARENA", "FLORES"], "correcta": 0,
  "voz": ["¿Qué cae cuando hace mucho *frío* arriba?", "Pensá en piedritas de hielo.", "¡El *granizo*! O la nieve."]},
 {"t": "pregunta", "pregunta": "¿De qué son las nubes?", "opciones": ["DE AGUA", "DE ALGODÓN"], "correcta": 0,
  "voz": ["Ahora vos: ¿de qué son las nubes?", "Pensá en la lluvia.", "¡De *agua*!"]},
 {"t": "consejo", "titulo": "NUBES GRISES", "texto": "Las nubes oscuras traen lluvia", "emoji": "🌧️",
  "voz": ["Truco: las nubes *oscuras* traen lluvia."]},
 {"t": "resumen", "items": [["NUBE", "gotitas juntas"], ["LLUVIA", "gotitas que caen"], ["FRÍO", "granizo o nieve"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *nube* son gotitas juntas.", "La *lluvia* son gotitas que caen.", "Con mucho *frío*: granizo o nieve.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "VIAJE", "titular": "¡Tomi llegó al río Paraná!", "bajada": "Y después al mar", "emoji": "🌊", "titulo": "RÍOS, LAGOS", "sub": "y mares",
  "voz": ["¡Noticia: Tomi llegó al río *Paraná*!", "Y después, al *mar*.", "Hoy: *ríos, lagos y mares*."]},
 {"t": "matriz", "titulo": "DÓNDE HAY AGUA", "celdas": [{"cab": "RÍO 🏞️", "txt": "corre, agua dulce"}, {"cab": "LAGO 💧", "txt": "quieto, agua dulce"}, {"cab": "LAGUNA 🦆", "txt": "lago chiquito"}, {"cab": "MAR 🌊", "txt": "grande y salado"}],
  "voz": ["El agua está en muchos lugares.", "El *río*: corre, con agua dulce.", "El *lago*: quieto, con agua dulce.", "La *laguna*: un lago chiquito.", "El *mar*: grande y salado."]},
 {"t": "memoria", "titulo": "LUGARES CON AGUA", "items": ["RÍO", "LAGO", "LAGUNA", "MAR"], "falta": 3,
  "voz": ["Mirá los lugares con agua.", "Se tapan… ¡y uno desapareció!", "¡Faltaba el *mar*!"]},
 {"t": "pregunta", "pregunta": "¿Dónde hay agua salada?", "opciones": ["EN EL MAR", "EN EL RÍO"], "correcta": 0,
  "voz": ["Ahora vos: ¿dónde hay agua salada?", "Pensá en las olas.", "¡En el *mar*!"]},
 {"t": "consejo", "titulo": "CON UN ADULTO", "texto": "Cerca del agua, siempre acompañados", "emoji": "🧑‍🧒",
  "voz": ["Truco: cerca del agua, siempre con un *adulto*."]},
 {"t": "resumen", "items": [["RÍO", "corre, dulce"], ["LAGO", "quieto, dulce"], ["MAR", "salado y grande"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *río* corre y es dulce.", "El *lago* es quieto y dulce.", "El *mar* es salado y grande.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Adónde va el charco cuando sale el sol?", "segundos": 8, "respuesta": "¡Sube al cielo como vapor!", "emoji": "☀️", "titulo": "EL AGUA", "sub": "vuelve al cielo",
  "voz": ["Desafío: ¿adónde va el charco cuando sale el sol?", "¡Sube al cielo como *vapor*!", "Hoy: *el ciclo del agua*."]},
 {"t": "ciclo", "titulo": "EL CICLO DEL AGUA", "items": ["EL SOL CALIENTA ☀️", "EL VAPOR SUBE ♨️", "SE FORMAN NUBES ☁️", "LLUEVE 🌧️"],
  "voz": ["El agua hace un *viaje* que no termina.", "El *sol* calienta el agua.", "El *vapor* sube.", "Arriba se forman *nubes*.", "¡Y *llueve*! Después, vuelve a empezar."]},
 {"t": "vof", "afirmacion": "El agua del charco se pierde para siempre", "emoji": "💧", "verdadero": False, "explicacion": "Sube y vuelve a caer como lluvia",
  "voz": ["¿Verdadero o falso? El charco se pierde para siempre.", "Pensá en el ciclo…", "¡*Falso*! Sube y vuelve a caer."]},
 {"t": "pregunta", "pregunta": "¿Qué empieza el ciclo del agua?", "opciones": ["EL SOL", "LA LUNA"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué empieza el ciclo?", "Pensá en el calor.", "¡El *sol*!"]},
 {"t": "consejo", "titulo": "UN CÍRCULO", "texto": "El ciclo vuelve a empezar", "emoji": "🔄",
  "voz": ["Truco: el ciclo es un *círculo*: vuelve a empezar."]},
 {"t": "resumen", "items": [["EVAPORA", "el sol calienta"], ["CONDENSA", "forma nubes"], ["LLUEVE", "y vuelve a empezar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El agua se *evapora* con el sol.", "Se *condensa* y forma nubes.", "*Llueve* y vuelve a empezar.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Seño Ana", "emoji": "👩‍🏫"}, "mensajes": [{"yo": False, "txt": "¿Cuánto llovió ayer? 🌧️"}, {"yo": True, "txt": "¡Lo voy a medir!"}], "titulo": "MEDIMOS", "sub": "la lluvia",
  "voz": ["La seño pregunta: ¿cuánto llovió ayer?", "Tomi responde: ¡lo voy a *medir*!", "Hoy: *medimos la lluvia*."]},
 {"t": "medidor", "titulo": "MI PLUVIÓMETRO", "tipo": "probeta", "min": 0, "max": 10, "valor": 5, "unidad": "cm", "nota": "El miércoles llovió 5 cm",
  "voz": ["Este es el *pluviómetro* de Tomi.", "Junta el agua de la lluvia.", "¡El miércoles llovió *cinco* centímetros!"]},
 {"t": "linea", "titulo": "LO QUE ANOTÓ TOMI", "eventos": [{"fecha": "LUNES", "txt": "2 cm", "emoji": "🌦️"}, {"fecha": "MIÉRCOLES", "txt": "5 cm", "emoji": "🌧️"}, {"fecha": "VIERNES", "txt": "nada", "emoji": "☀️"}],
  "voz": ["El *lunes*: dos centímetros.", "El *miércoles*: ¡cinco centímetros!", "El *viernes*: nada, hubo sol."]},
 {"t": "pregunta", "pregunta": "¿Qué día llovió más?", "opciones": ["MIÉRCOLES", "LUNES"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué día llovió más?", "Compará los números.", "¡El *miércoles*!"]},
 {"t": "consejo", "titulo": "VACIÁ LA BOTELLA", "texto": "Después de anotar, para la próxima lluvia", "emoji": "🫙",
  "voz": ["Truco: después de anotar, *vaciá* la botella."]},
 {"t": "resumen", "items": [["PLUVIÓMETRO", "junta la lluvia"], ["MEDIR", "con una regla"], ["ANOTAR", "cada lluvia"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *pluviómetro* junta la lluvia.", "*Medimos* con una regla.", "*Anotamos* cada lluvia.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat2-m7-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Naturales 2", "titulo": TIT[n], "sub": f"Ciencias Naturales 2 · Misión 7 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
