# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 12 · Fábulas de Esopo y Samaniego: las 4 clases animadas.
Vía fonológica: la voz no nombra letras. Las fábulas se cuentan con palabras simples (dominio público, sin copiar versos).
Genera tools/medio/clase/lecciones/medio-leng2-m12-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'a2a06e6b-3414-49da-b7fb-1aa32a25c840', 2: 'e4ea53de-3f0a-48cb-9147-808bb18adaa4', 3: '998f89b7-7d2c-4e03-94d4-fbdf93af85cf', 4: 'c5cb1a7d-49ad-4c02-91f5-8e589f0f5fb3'}
TIT = {1: 'Leer La zorra y las uvas', 2: 'Leer La liebre y la tortuga', 3: 'Qué enseña cada fábula', 4: 'Escribir una moraleja'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."

N1 = [
 {"t": "historieta", "titulo": "LA ZORRA Y LAS UVAS", "vinetas": [{"emojis": ["🦊", "😋"], "txt": "Una zorra tenía hambre"}, {"emojis": ["🍇", "⬆️"], "txt": "Vio unas uvas muy altas"}, {"emojis": ["🦊", "💨"], "txt": "Saltó y saltó… ¡no llegó!"}, {"emojis": ["🦊", "😒"], "txt": "¡Bah! Están verdes", "quien": "Zorra"}],
  "voz": ["Una zorra tenía mucha hambre.", "Vio unas uvas muy altas.", "Saltó y saltó… ¡pero no llegó!", "Dijo: ¡bah, están verdes! Y se fue. Hoy: *una fábula*."]},
 {"t": "definicion", "palabra": "Fábula", "texto": "Cuento corto con animales y una enseñanza", "emoji": "🦊",
  "voz": ["Esta historia es una *fábula*: tiene animales y una enseñanza.", "La contaron *Esopo* y *Samaniego*."]},
 {"t": "quiz4", "pregunta": "¿Las uvas estaban verdes?", "opciones": ["SÍ, DE VERDAD", "NO, FUE UNA EXCUSA", "NO HABÍA UVAS", "ERAN DE PLÁSTICO"], "correcta": 1,
  "voz": ["¿Las uvas estaban verdes de verdad?", "Pensá: ¿por qué lo dijo la zorra?", "¡Fue una *excusa*! No pudo alcanzarlas."]},
 {"t": "consejo", "titulo": "ANIMALES QUE HABLAN", "texto": "En las fábulas los animales hablan y piensan", "emoji": "🗣️",
  "voz": ["Truco: en las fábulas, los animales *hablan* y *piensan*."]},
 {"t": "errores", "items": [{"mal": "Las uvas estaban verdes", "bien": "La zorra no las alcanzó"}],
  "voz": ["Cuidado con este error.", "Las uvas no estaban verdes: la zorra *no llegó*."]},
 {"t": "resumen", "items": [["FÁBULA", "animales y enseñanza"], ["AUTORES", "Esopo y Samaniego"], ["LA ZORRA", "puso una excusa"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *fábula* tiene animales y una enseñanza.", "La contaron *Esopo* y *Samaniego*.", "La *zorra* puso una excusa.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "GRAN CARRERA", "titular": "¡La liebre contra la tortuga!", "bajada": "¿Quién ganará?", "emoji": "🏁", "titulo": "LA LIEBRE", "sub": "y la tortuga",
  "voz": ["¡Gran carrera: la liebre contra la tortuga!", "¿Quién ganará?", "Hoy: *la liebre y la tortuga*."]},
 {"t": "versus", "titulo": "LA CARRERA", "a": {"txt": "LIEBRE", "emoji": "🐇", "datos": ["muy rápida", "se confió y se durmió"]}, "b": {"txt": "TORTUGA", "emoji": "🐢", "datos": ["muy lenta", "caminó sin parar"]}, "gana": "b", "veredicto": "¡Ganó la tortuga!",
  "voz": ["La liebre salió *muy rápido*… y se burlaba.", "Se *confió* y se durmió una siesta.", "La tortuga caminó despacio, *sin parar*.", "¡Ganó la *tortuga*!"]},
 {"t": "unir", "titulo": "¿QUIÉN LO HIZO?", "pares": [["Se durmió", "liebre"], ["No paró", "tortuga"], ["Se burlaba", "liebre"]], "mezclar": True,
  "voz": ["Unimos cada acción con su personaje.", "Se durmió: la *liebre*.", "No paró: la *tortuga*.", "Se burlaba: la *liebre*."]},
 {"t": "pregunta", "pregunta": "¿Por qué perdió la liebre?", "opciones": ["SE CONFIÓ", "ERA LENTA"], "correcta": 0,
  "voz": ["¿Por qué perdió la liebre, si era rápida?", "Pensá en la siesta…", "¡Porque se *confió*!"]},
 {"t": "consejo", "titulo": "MIRÁ EL FINAL", "texto": "El final muestra la enseñanza", "emoji": "🏁",
  "voz": ["Truco: el *final* de la fábula muestra la enseñanza."]},
 {"t": "resumen", "items": [["LIEBRE", "rápida, se confió"], ["TORTUGA", "lenta, no paró"], ["FINAL", "ganó la tortuga"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *liebre* era rápida, pero se confió.", "La *tortuga* era lenta, pero no paró.", "¡Ganó la *tortuga*!", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué aprendemos de la tortuga?", "segundos": 8, "respuesta": "Despacio y sin parar se llega lejos", "emoji": "🐢", "titulo": "LA MORALEJA", "sub": "qué enseña",
  "voz": ["Desafío: ¿qué aprendemos de la tortuga?", "¡Despacio y *sin parar* se llega lejos!", "Hoy: *qué enseña cada fábula*."]},
 {"t": "personaje", "personaje": {"nombre": "Esopo", "emoji": "🧔"}, "lineas": [{"txt": "¡Hola! Yo conté muchas fábulas.", "animo": "feliz"}, {"txt": "Al final, siempre dejo una enseñanza.", "animo": "piensa"}, {"txt": "¡Se llama moraleja!", "animo": "ojo"}],
  "voz": ["¡Hola! Soy Esopo. Conté muchas fábulas.", "Al final, siempre dejo una *enseñanza*.", "¡Se llama *moraleja*!"]},
 {"t": "escape", "titulo": "LA PUERTA DE LAS FÁBULAS", "candados": [{"p": "La zorra enseña…", "r": "NO PONER EXCUSAS"}, {"p": "La tortuga enseña…", "r": "DESPACIO Y SIN PARAR"}],
  "voz": ["¡Para salir, decimos las moralejas!", "La zorra enseña: no poner *excusas*.", "La tortuga enseña: despacio y *sin parar*.", "¡Escapamos!"]},
 {"t": "errores", "items": [{"mal": "Moraleja: la liebre se durmió", "bien": "Moraleja: no te confíes"}],
  "voz": ["Cuidado con este error.", "No cuenta lo que pasó: dice lo que *aprendemos*."]},
 {"t": "consejo", "titulo": "PREGUNTÁ ¿QUÉ APRENDO?", "texto": "La respuesta es la moraleja", "emoji": "💡",
  "voz": ["Truco: preguntá *¿qué aprendo?* Esa es la moraleja."]},
 {"t": "resumen", "items": [["MORALEJA", "la enseñanza"], ["ZORRA", "no poner excusas"], ["TORTUGA", "despacio y sin parar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *moraleja* es la enseñanza.", "La *zorra*: no poner excusas.", "La *tortuga*: despacio y sin parar.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": {"nombre": "Sofi", "emoji": "👧"}, "lugar": "🦁", "lineas": ["Sofi lee otra fábula.", "Un ratón salva a un león.", "¿Qué enseñará?"], "titulo": "ESCRIBIR", "sub": "una moraleja",
  "voz": ["Sofi lee otra fábula.", "Un ratoncito salva a un león atrapado.", "¿Qué enseñará?", "Hoy: *escribir una moraleja*."]},
 {"t": "transforma", "titulo": "DE LA HISTORIA A LA MORALEJA", "pasos": [{"txt": "El ratón salvó al león", "nota": "¿qué pasó?"}, {"txt": "Aunque era chiquito, pudo ayudar", "nota": "¿qué aprendo?"}, {"txt": "Todos podemos ayudar", "nota": "moraleja"}],
  "voz": ["¿Qué pasó? El ratón salvó al león.", "¿Qué aprendo? Aunque era chiquito, pudo ayudar.", "Moraleja: ¡*todos podemos ayudar*!"]},
 {"t": "completa", "antes": "La hormiga guardó comida. Es bueno", "despues": ".", "opciones": ["PREPARARSE", "DORMIR"], "correcta": 0,
  "voz": ["Otra fábula: la hormiga guardó comida para el invierno.", "¿Qué aprendemos? Es bueno…", "¡*Prepararse*!"]},
 {"t": "pasos", "titulo": "CÓMO ESCRIBO UNA MORALEJA", "items": [{"txt": "Pienso qué pasó", "emoji": "🤔"}, {"txt": "Pienso qué aprendo", "emoji": "💡"}, {"txt": "Escribo una oración corta", "emoji": "✏️"}],
  "voz": ["¿Cómo escribimos una moraleja?", "Pensamos *qué pasó*.", "Pensamos *qué aprendemos*.", "Escribimos una *oración corta*."]},
 {"t": "consejo", "titulo": "CORTA Y PARA TODOS", "texto": "La moraleja sirve para cualquiera", "emoji": "🌍",
  "voz": ["Truco: la moraleja es *corta* y sirve para todos."]},
 {"t": "resumen", "items": [["¿QUÉ PASÓ?", "pensar la historia"], ["¿QUÉ APRENDO?", "la enseñanza"], ["ESCRIBIR", "una oración corta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Pensamos *qué pasó*.", "Pensamos *qué aprendemos*.", "Escribimos una *oración corta*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m12-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 12 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
