# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 10 · Adjetivos: las 4 clases animadas.
Vía fonológica: la voz no nombra letras. Metáfora: el cuaderno viajero de Sofi.
Genera tools/medio/clase/lecciones/medio-leng2-m10-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '1d4d4cae-b0d3-49e2-8d96-d637c419c37a', 2: '2f9499fd-6700-45c0-855a-a1acd221027e', 3: '3d28bb30-724f-4bed-bd14-c681a1e7cb60', 4: '2d39854b-6847-4a7f-9e66-daba12c96dcb'}
TIT = {1: 'Palabras que dicen cómo es', 2: 'Adjetivos para personajes', 3: 'Adjetivos para lugares', 4: 'Escribir descripciones con adjetivos'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🦆", "lineas": ["Sofi ve un pato en la laguna.", "Escribe: EL PATO.", "¡Pero quiere decir cómo es!"], "titulo": "ADJETIVOS", "sub": "dicen cómo es",
  "voz": ["Sofi ve un pato en la laguna.", "En su cuaderno escribe: el pato.", "¡Pero quiere decir *cómo es*!", "Hoy: *palabras que dicen cómo es*."]},
 {"t": "definicion", "palabra": "Adjetivo", "texto": "Palabra que dice cómo es algo", "emoji": "🎨",
  "voz": ["Sofi escribe: el pato *blanco*.", "*Blanco* es un adjetivo: dice cómo es."]},
 {"t": "escala", "titulo": "ADJETIVOS DE TAMAÑO", "items": [{"txt": "CHIQUITO", "emoji": "🐭", "valor": 1}, {"txt": "MEDIANO", "emoji": "🐱", "valor": 3}, {"txt": "GRANDE", "emoji": "🐶", "valor": 6}, {"txt": "ENORME", "emoji": "🐘", "valor": 10}],
  "voz": ["El ratón es *chiquito*.", "El gato es *mediano*.", "El perro es *grande*.", "¡Y el elefante es *enorme*!"]},
 {"t": "quiz4", "pregunta": "¿Cuál es un adjetivo?", "opciones": ["MESA", "PELUDO", "CORRE", "GATO"], "correcta": 1,
  "voz": ["¿Cuál de estas palabras dice *cómo es*?", "Pensá: ¿cómo es el gato?", "¡*Peludo*! Es un adjetivo."]},
 {"t": "consejo", "titulo": "PREGUNTÁ ¿CÓMO ES?", "texto": "La respuesta es un adjetivo", "emoji": "❓",
  "voz": ["Truco: preguntá *¿cómo es?* La respuesta es un adjetivo."]},
 {"t": "resumen", "items": [["ADJETIVO", "dice cómo es"], ["DICE", "tamaño, color, forma"], ["VA JUNTO", "al sustantivo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *adjetivo* dice cómo es algo.", "Dice el *tamaño*, el *color* o la forma.", "Va junto al *sustantivo*.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "CUENTOS", "titular": "¡Los personajes quieren saber cómo son!", "bajada": "Sofi los va a describir", "emoji": "📖", "titulo": "ADJETIVOS", "sub": "para personajes",
  "voz": ["¡Noticia: los personajes quieren saber cómo son!", "Sofi los va a *describir*.", "Hoy: *adjetivos para personajes*."]},
 {"t": "versus", "titulo": "¿CÓMO SON?", "a": {"txt": "CENICIENTA", "emoji": "👸", "datos": ["buena", "trabajadora"]}, "b": {"txt": "MADRASTRA", "emoji": "🦹‍♀️", "datos": ["mala", "mandona"]}, "gana": "a", "veredicto": "¡Gana la bondad!",
  "voz": ["Comparamos dos personajes.", "Cenicienta es *buena* y *trabajadora*.", "La madrastra es *mala* y *mandona*.", "¡Gana la bondad!"]},
 {"t": "unir", "titulo": "CADA UNO CON SU ADJETIVO", "pares": [["RINRÍN", "elegante"], ["LOBO", "feroz"], ["CHANCHITO", "trabajador"]], "mezclar": True,
  "voz": ["Unimos cada personaje con su adjetivo.", "Rinrín es *elegante*.", "El lobo es *feroz*.", "El chanchito es *trabajador*."]},
 {"t": "errores", "items": [{"mal": "SOPLÓ es adjetivo", "bien": "SOPLÓ dice lo que hace"}],
  "voz": ["Cuidado con este error.", "Sopló dice lo que *hace*, no cómo es."]},
 {"t": "consejo", "titulo": "POR FUERA Y POR DENTRO", "texto": "Grande, elegante… buena, mala", "emoji": "🪞",
  "voz": ["Truco: describí cómo es *por fuera* y *por dentro*."]},
 {"t": "resumen", "items": [["POR FUERA", "grande, elegante"], ["POR DENTRO", "buena, mala"], ["PERSONAJES", "con adjetivos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Por fuera*: grande, elegante.", "*Por dentro*: buena, mala.", "Así describimos a los *personajes*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Cómo es la selva?", "segundos": 8, "respuesta": "¡Verde, húmeda y enorme!", "emoji": "🌳", "titulo": "ADJETIVOS", "sub": "para lugares",
  "voz": ["Desafío: ¿cómo es la selva?", "¡*Verde*, *húmeda* y *enorme*!", "Hoy: *adjetivos para lugares*."]},
 {"t": "documental", "emojis": ["🌳", "🐆", "🦜"], "lugar": "🇦🇷", "rotulos": [{"txt": "LA SELVA", "sub": "verde y húmeda"}, {"txt": "EL CASTILLO", "sub": "alto y brillante"}, {"txt": "LA PLAZA", "sub": "grande y ruidosa"}],
  "voz": ["La selva es *verde* y *húmeda*.", "El castillo es *alto* y *brillante*.", "La plaza es *grande* y *ruidosa*."]},
 {"t": "pasos", "titulo": "CON LOS SENTIDOS", "items": [{"txt": "¿Cómo se ve?", "emoji": "👀"}, {"txt": "¿Cómo suena?", "emoji": "👂"}, {"txt": "¿Cómo se siente?", "emoji": "✋"}],
  "voz": ["Para describir un lugar usamos los sentidos.", "¿Cómo se *ve*?", "¿Cómo *suena*?", "¿Cómo se *siente*?"]},
 {"t": "completa", "antes": "La laguna es", "despues": ".", "opciones": ["FRÍA", "CORRE"], "correcta": 0,
  "voz": ["Completá: la laguna es…", "¿Fría o corre?", "¡*Fría*! Dice cómo es."]},
 {"t": "consejo", "titulo": "USÁ LOS SENTIDOS", "texto": "Mirá, escuchá y tocá", "emoji": "🖐️",
  "voz": ["Truco: mirá, escuchá y tocá para describir."]},
 {"t": "resumen", "items": [["LUGARES", "con adjetivos"], ["SENTIDOS", "ver, oír, sentir"], ["EJEMPLOS", "selva verde"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los *lugares* también se describen.", "Usamos los *sentidos*.", "Como la *selva verde*.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Cómo es tu gato Michi? 🐈"}, {"yo": True, "txt": "¡Te lo describo!"}], "titulo": "DESCRIBIR", "sub": "con adjetivos",
  "voz": ["Tomi pregunta: ¿cómo es tu gato Michi?", "Sofi responde: ¡te lo describo!", "Hoy: *escribir descripciones con adjetivos*."]},
 {"t": "transforma", "titulo": "SUMAMOS ADJETIVOS", "pasos": [{"txt": "EL GATO"}, {"txt": "EL GATO NEGRO", "nota": "+ color"}, {"txt": "EL GATO NEGRO Y CHIQUITO", "nota": "+ tamaño"}],
  "voz": ["Empezamos con: el gato.", "Sumamos un color: el gato *negro*.", "Sumamos el tamaño: negro y *chiquito*."]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Aburrido", "emoji": "😴"}, "preguntas": [{"p": "LA MANZANA…", "r": "ROJA Y REDONDA"}, {"p": "EL GLOBO…", "r": "AZUL Y LIVIANO"}],
  "voz": ["¡Apareció el *Monstruo Aburrido*! No le gustan las descripciones.", "Le ganamos con adjetivos.", "La manzana *roja y redonda*.", "¡El globo *azul y liviano*! ¡Ganamos!"]},
 {"t": "errores", "items": [{"mal": "LINDO, LINDO Y LINDO", "bien": "LINDO, MIMOSO Y JUGUETÓN"}],
  "voz": ["Cuidado con este error.", "No repetimos: usamos adjetivos *distintos*."]},
 {"t": "consejo", "titulo": "NO REPITAS", "texto": "Usá adjetivos distintos", "emoji": "🔁",
  "voz": ["Truco: usá adjetivos *distintos* en cada oración."]},
 {"t": "resumen", "items": [["ELEGIR", "qué describir"], ["SUMAR", "adjetivos"], ["ESCRIBIR", "oraciones claras"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Elegimos* qué describir.", "*Sumamos* adjetivos.", "*Escribimos* oraciones claras.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m10-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 10 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
