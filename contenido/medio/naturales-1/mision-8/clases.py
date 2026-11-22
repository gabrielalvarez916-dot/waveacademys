# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 8 · El tiempo atmosférico: las 4 clases animadas.
Metáfora: Sofi, la presentadora del pronóstico. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-nat1-m8-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0'
TEMA = 8
TIT = {1: 'Nubes y lluvia', 2: 'El viento y sus efectos', 3: 'Medimos la temperatura', 4: 'Calendario del tiempo'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📺", "lineas": ["Sofi presenta el pronóstico.", "Señala unas nubes grises.", "¡Hoy va a llover!"], "titulo": "NUBES", "sub": "y lluvia",
  "voz": ["Sofi presenta el *pronóstico* del tiempo.", "Señala unas nubes *grises*.", "¡Hoy va a *llover*!", "Hoy: *nubes y lluvia*."]},
 {"t": "antesdespues", "antes": {"cab": "DESPEJADO", "emoji": "☀️", "texto": "Sin nubes"}, "despues": {"cab": "NUBLADO", "emoji": "🌧️", "texto": "Nubes grises"},
  "voz": ["A la mañana, el cielo estaba *despejado*.", "A la tarde se llenó de nubes *grises*."]},
 {"t": "ciclo", "titulo": "ASÍ LLUEVE", "items": ["GOTITAS EN LA NUBE", "SE JUNTAN", "CAEN", "QUEDAN CHARCOS"],
  "voz": ["La lluvia tiene su *camino*.", "En la nube hay *gotitas*.", "Las gotitas se *juntan*.", "Se ponen pesadas y *caen*.", "Y quedan *charcos*."]},
 {"t": "pregunta", "pregunta": "¿Qué nubes traen lluvia?", "opciones": ["BLANCAS", "GRISES", "ROSADAS"], "correcta": 1,
  "voz": ["Ahora vos. Mirá el color.", "¿Qué nubes traen lluvia?", "¡Las *grises*!"]},
 {"t": "consejo", "titulo": "CON TORMENTA", "texto": "Si hay rayos, quedate adentro", "emoji": "⛈️",
  "voz": ["Importante: con *tormenta*, quedate adentro."]},
 {"t": "resumen", "items": [["NUBES", "gotitas de agua"], ["GRISES", "traen lluvia"], ["LLUVIA", "las gotas caen"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *nubes* son gotitas de agua.", "Las *grises* traen lluvia.", "Las gotas *caen*: llueve.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué no se ve pero mueve las hojas?", "segundos": 6, "respuesta": "¡EL VIENTO!", "emoji": "🍃", "titulo": "EL VIENTO", "sub": "y sus efectos",
  "voz": ["Desafío: ¿qué no se ve pero mueve las hojas?", "¡El *viento*!", "Hoy: *el viento y sus efectos*."]},
 {"t": "causas", "causa": {"txt": "EL VIENTO", "emoji": "💨"}, "items": ["MUEVE LAS HOJAS", "VUELA EL BARRILETE", "SECA LA ROPA"],
  "voz": ["¿Qué hace el *viento*?", "*Mueve* las hojas.", "Hace *volar* el barrilete.", "Y *seca* la ropa de la soga."]},
 {"t": "experimento", "titulo": "¿HAY VIENTO?", "variable": "EL VIENTO", "a": {"cab": "ADENTRO", "emojis": ["🏠", "🎡"], "txt": "Sin viento", "res": "EL MOLINETE QUIETO"}, "b": {"cab": "EN EL PATIO", "emojis": ["🌳", "🎡"], "txt": "Con viento", "res": "¡GIRA RÁPIDO!"},
  "voz": ["Sofi prueba su molinete *adentro*.", "Después lo lleva al *patio*.", "¡Afuera gira rápido: hay *viento*!"]},
 {"t": "pregunta", "pregunta": "La bandera flamea. ¿Qué pasa?", "opciones": ["LLUEVE", "HAY VIENTO", "ES DE NOCHE"], "correcta": 1,
  "voz": ["Ahora vos. La bandera se mueve mucho.", "¿Qué está pasando?", "¡Hay *viento*!"]},
 {"t": "consejo", "titulo": "MIRÁ LOS ÁRBOLES", "texto": "Si las hojas se mueven, hay viento", "emoji": "🌳",
  "voz": ["Truco: mirá las *hojas* de los árboles."]},
 {"t": "resumen", "items": [["VIENTO", "aire que se mueve"], ["MUEVE", "hojas y barriletes"], ["FUERZA", "brisa o ventarrón"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *viento* es aire que se mueve.", "*Mueve* hojas y barriletes.", "Puede ser *brisa* o *ventarrón*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Llevo campera hoy?"}, {"yo": True, "txt": "¡MIRÁ EL TERMÓMETRO!"}, {"yo": False, "txt": "Marca 10… ¡sí!"}], "titulo": "LA TEMPERATURA", "sub": "calor o frío",
  "voz": ["Tomi le escribe a Sofi.", "¿Llevo campera hoy?", "Sofi le dice: ¡mirá el *termómetro*!", "Hoy: *medimos la temperatura*."]},
 {"t": "medidor", "titulo": "EL TERMÓMETRO", "tipo": "termometro", "min": 0, "max": 40, "valor": 30, "unidad": "grados", "nota": "¡HACE CALOR!",
  "voz": ["Este es un *termómetro*.", "La rayita llega al *30*.", "¡Número alto: hace *calor*!"]},
 {"t": "comparar", "a": {"cab": "CALOR", "texto": "LA RAYITA SUBE", "emoji": "🥵"}, "b": {"cab": "FRÍO", "texto": "LA RAYITA BAJA", "emoji": "🥶"}, "signo": "vs",
  "voz": ["Con *calor*, la rayita sube.", "Con *frío*, la rayita baja.", "¡Así sabemos qué ropa ponernos!"]},
 {"t": "pregunta", "pregunta": "Marca 10. ¿Qué te ponés?", "opciones": ["MALLA", "CAMPERA", "OJOTAS"], "correcta": 1,
  "voz": ["Ahora vos. El termómetro marca *10*.", "¿Qué te ponés?", "¡Una *campera*: hace frío!"]},
 {"t": "consejo", "titulo": "CON UN ADULTO", "texto": "El termómetro se lee acompañado", "emoji": "🧑",
  "voz": ["Truco: leé el termómetro *con un adulto*."]},
 {"t": "resumen", "items": [["CALOR", "la rayita sube"], ["FRÍO", "la rayita baja"], ["TERMÓMETRO", "mide la temperatura"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Con *calor*, la rayita sube.", "Con *frío*, baja.", "El *termómetro* mide la temperatura.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "EL PRONÓSTICO", "titular": "¡SOFI ARMA SU CALENDARIO!", "bajada": "Anota el tiempo cada día", "emoji": "📅", "titulo": "CALENDARIO", "sub": "del tiempo",
  "voz": ["¡Sofi arma su *calendario del tiempo*!", "Anota cómo está el cielo cada día.", "Hoy: *el calendario del tiempo*."]},
 {"t": "linea", "titulo": "MI SEMANA", "eventos": [{"fecha": "LUNES", "txt": "SOL", "emoji": "☀️"}, {"fecha": "MARTES", "txt": "SOL", "emoji": "☀️"}, {"fecha": "MIÉRCOLES", "txt": "LLUVIA", "emoji": "🌧️"}, {"fecha": "JUEVES", "txt": "NUBE", "emoji": "☁️"}, {"fecha": "VIERNES", "txt": "SOL", "emoji": "☀️"}],
  "voz": ["El *lunes*: sol.", "El *martes*: sol.", "El *miércoles*: lluvia.", "El *jueves*: nublado.", "El *viernes*: sol otra vez."]},
 {"t": "barras", "titulo": "LA SEMANA DE SOFI", "unidad": "días", "items": [{"txt": "SOL", "valor": 3}, {"txt": "NUBE", "valor": 1}, {"txt": "LLUVIA", "valor": 1}],
  "voz": ["Contamos los días.", "De *sol*: 3 días.", "*Nublados*: 1 día.", "De *lluvia*: 1 día."]},
 {"t": "pregunta", "pregunta": "¿Qué tiempo hubo más veces?", "opciones": ["LLUVIA", "SOL", "NUBE"], "correcta": 1,
  "voz": ["Ahora vos. Mirá las barras.", "¿Qué tiempo hubo más veces?", "¡*Sol*! Tres días."]},
 {"t": "consejo", "titulo": "A LA MISMA HORA", "texto": "Mirá el cielo siempre a la misma hora", "emoji": "⏰",
  "voz": ["Truco: mirá el cielo a la *misma hora*."]},
 {"t": "resumen", "items": [["OBSERVAR", "cada día"], ["ANOTAR", "con dibujos"], ["CONTAR", "al final de la semana"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Observamos* el cielo cada día.", "*Anotamos* con dibujos.", "Y *contamos* al final.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Naturales 1", "titulo": TIT[n], "sub": f"Ciencias Naturales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
