# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 8 · Estaciones y orientación: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (mira el cielo y usa la brújula).
Genera tools/medio/clase/lecciones/medio-nat2-m8-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'ce72fa17-580c-4971-97f3-117c7d75a498', 2: '00f8a440-3e0c-4721-9d11-2047c98ec644', 3: 'c800f22f-12d2-43ea-b0a3-1e894f5ee1de', 4: 'b5cf891f-a513-407e-818f-80ac51030686'}
TIT = {1: 'La luna y sus fases', 2: 'Las cuatro estaciones', 3: 'Los puntos cardinales', 4: 'Orientarse con el sol'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "🧑‍🔬"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🌙", "lineas": ["Tomi mira la luna de noche.", "Cada noche se ve distinta.", "¿Por qué cambia?"], "titulo": "LA LUNA", "sub": "y sus fases",
  "voz": ["Tomi mira la *luna* de noche.", "Cada noche se ve *distinta*.", "¿Por qué cambia?", "Hoy: *la luna y sus fases*."]},
 {"t": "ciclo", "titulo": "LAS FASES DE LA LUNA", "items": ["NUEVA 🌑", "CRECIENTE 🌓", "LLENA 🌕", "MENGUANTE 🌗"],
  "voz": ["La luna muestra cuatro *caras*.", "*Nueva*: casi no se ve.", "*Creciente*: va creciendo.", "*Llena*: ¡toda redonda!", "*Menguante*: se achica. Y vuelve a empezar."]},
 {"t": "datoloco", "texto": "La luna no tiene luz propia: la ilumina el sol", "emoji": "☀️",
  "voz": ["¿Sabías qué?", "¡La luna no tiene luz! La ilumina el *sol*."]},
 {"t": "pregunta", "pregunta": "¿Cómo se ve la luna llena?", "opciones": ["TODA REDONDA", "NO SE VE"], "correcta": 0,
  "voz": ["Ahora vos: ¿cómo se ve la luna llena?", "Pensá en un círculo.", "¡Toda *redonda*!"]},
 {"t": "consejo", "titulo": "MIRALA CADA NOCHE", "texto": "Dibujá cómo cambia", "emoji": "✏️",
  "voz": ["Truco: mirá la luna cada noche y *dibujala*."]},
 {"t": "resumen", "items": [["LUNA", "la ilumina el sol"], ["FASES", "cuatro caras"], ["CICLO", "se repiten"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "A la *luna* la ilumina el sol.", "Tiene cuatro *fases*.", "Se repiten en un *ciclo*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Sofi", "emoji": "👧"}, "mensajes": [{"yo": False, "txt": "¡Se cayeron todas las hojas! 🍂"}, {"yo": True, "txt": "¡Llegó el otoño!"}], "titulo": "LAS CUATRO", "sub": "estaciones",
  "voz": ["Sofi escribe: ¡se cayeron todas las hojas!", "Tomi responde: ¡llegó el *otoño*!", "Hoy: *las cuatro estaciones*."]},
 {"t": "mazo", "titulo": "LAS ESTACIONES", "items": [{"frente": "☀️", "dorso": "VERANO: CALOR", "emoji": "☀️"}, {"frente": "🍂", "dorso": "OTOÑO: CAEN LAS HOJAS", "emoji": "🍂"}, {"frente": "❄️", "dorso": "INVIERNO: FRÍO", "emoji": "❄️"}, {"frente": "🌸", "dorso": "PRIMAVERA: FLORES", "emoji": "🌸"}],
  "voz": ["*Verano*: hace calor.", "*Otoño*: caen las hojas.", "*Invierno*: hace frío.", "*Primavera*: ¡salen las flores!"]},
 {"t": "prediccion", "pregunta": "¿Qué ropa usamos en invierno?", "a": {"txt": "CAMPERA Y BUFANDA", "emoji": "🧣"}, "b": {"txt": "MALLA", "emoji": "🩱"}, "correcta": "a", "resultado": "En invierno nos abrigamos",
  "voz": ["¿Qué ropa usamos en *invierno*?", "Pensá…", "¡Campera y *bufanda*! Nos abrigamos."]},
 {"t": "pregunta", "pregunta": "¿En qué estación hay más flores?", "opciones": ["PRIMAVERA", "INVIERNO"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuándo hay más flores?", "Pensá en los árboles.", "¡En *primavera*!"]},
 {"t": "consejo", "titulo": "EN ORDEN", "texto": "Verano, otoño, invierno, primavera", "emoji": "🔄",
  "voz": ["Truco: verano, otoño, invierno, primavera… ¡y otra vez!"]},
 {"t": "resumen", "items": [["VERANO", "calor"], ["OTOÑO", "caen las hojas"], ["INVIERNO Y PRIMAVERA", "frío y flores"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En *verano*, calor.", "En *otoño*, caen las hojas.", "En *invierno*, frío; en *primavera*, flores.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Por dónde sale el sol cada mañana?", "segundos": 8, "respuesta": "¡Por el este!", "emoji": "🌅", "titulo": "LOS PUNTOS", "sub": "cardinales",
  "voz": ["Desafío: ¿por dónde sale el sol?", "¡Por el *este*!", "Hoy: *los puntos cardinales*."]},
 {"t": "partes", "emoji": "🧭", "titulo": "LA BRÚJULA DE TOMI", "partes": [{"txt": "NORTE", "x": 0, "y": -0.8}, {"txt": "ESTE", "x": 0.8, "y": 0}, {"txt": "SUR", "x": 0, "y": 0.8}, {"txt": "OESTE", "x": -0.8, "y": 0}],
  "voz": ["Esta es la *brújula* de Tomi.", "Arriba, el *norte*.", "A la derecha, el *este*.", "Abajo, el *sur*.", "A la izquierda, el *oeste*."]},
 {"t": "comparar", "a": {"cab": "ESTE", "texto": "SALE EL SOL", "emoji": "🌅"}, "b": {"cab": "OESTE", "texto": "SE ESCONDE", "emoji": "🌇"}, "signo": "↔",
  "voz": ["Comparamos dos puntos.", "Por el *este*, sale el sol.", "Por el *oeste*, se esconde."]},
 {"t": "pregunta", "pregunta": "¿Adónde apunta la aguja de la brújula?", "opciones": ["AL NORTE", "AL SUR"], "correcta": 0,
  "voz": ["Ahora vos: ¿adónde apunta la aguja?", "Pensá en la brújula.", "¡Al *norte*!"]},
 {"t": "consejo", "titulo": "CUIDADO", "texto": "Nunca mires el sol directo", "emoji": "😎",
  "voz": ["Truco: nunca mires el sol *directo*."]},
 {"t": "resumen", "items": [["ESTE", "sale el sol"], ["OESTE", "se esconde"], ["BRÚJULA", "apunta al norte"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Por el *este* sale el sol.", "Por el *oeste* se esconde.", "La *brújula* apunta al norte.", CIERRE]},
]
N4 = [
 {"t": "personaje", "personaje": {"nombre": "Sol Solcito", "emoji": "☀️"}, "lineas": [{"txt": "¡Hola! A la mañana salgo por el este.", "animo": "feliz"}, {"txt": "Al mediodía estoy bien alto.", "animo": "sorpresa"}, {"txt": "A la tarde me escondo por el oeste.", "animo": "piensa"}],
  "voz": ["¡Hola! A la mañana salgo por el *este*.", "Al *mediodía* estoy bien alto.", "A la tarde me escondo por el *oeste*."]},
 {"t": "linea", "titulo": "EL VIAJE DEL SOL", "eventos": [{"fecha": "MAÑANA", "txt": "este", "emoji": "🌅"}, {"fecha": "MEDIODÍA", "txt": "arriba", "emoji": "☀️"}, {"fecha": "TARDE", "txt": "oeste", "emoji": "🌇"}],
  "voz": ["A la *mañana*, el sol está al este.", "Al *mediodía*, bien arriba.", "A la *tarde*, se va al oeste."]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Perdido", "emoji": "👾"}, "preguntas": [{"p": "Derecha al este: ¿qué hay adelante?", "r": "EL NORTE"}, {"p": "¿Y atrás?", "r": "EL SUR"}],
  "voz": ["¡Apareció el *Monstruo Perdido*!", "Señalamos con la derecha donde sale el sol.", "Adelante: ¡el *norte*!", "Atrás: ¡el *sur*! ¡Ya no está perdido!"]},
 {"t": "pregunta", "pregunta": "¿Cuándo la sombra es más cortita?", "opciones": ["AL MEDIODÍA", "A LA TARDE"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuándo la sombra es más corta?", "Pensá dónde está el sol.", "¡Al *mediodía*!"]},
 {"t": "consejo", "titulo": "GORRA", "texto": "Al sol, usá gorra", "emoji": "🧢",
  "voz": ["Truco: si estás al sol, usá *gorra*."]},
 {"t": "resumen", "items": [["MAÑANA", "sol al este"], ["TARDE", "sol al oeste"], ["TRUCO", "derecha al este"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "A la *mañana*, el sol está al este.", "A la *tarde*, al oeste.", "Derecha al este: adelante está el *norte*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat2-m8-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Naturales 2", "titulo": TIT[n], "sub": f"Ciencias Naturales 2 · Misión 8 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
