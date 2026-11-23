# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 13 · Cartas y mensajes para otros: las 4 clases animadas.
Vía fonológica: la voz no nombra letras. Metáfora: el cuaderno viajero de Sofi lleva una carta.
Genera tools/medio/clase/lecciones/medio-leng2-m13-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'c04851d0-4d81-403c-aeab-92c2b32d9ace', 2: 'ed884142-6205-4172-8141-f0f97ed646f7', 3: '1e36adfb-998a-4719-a729-5334e5258d4a', 4: 'f739ae92-f58c-46fe-9f12-005df396ab95'}
TIT = {1: 'Partes de una carta', 2: 'Escribir una carta a un compañero', 3: 'Un mensaje de correo electrónico', 4: 'Responder una carta'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "✉️", "lineas": ["Sofi quiere contarle algo a Tomi.", "Pero Tomi está de viaje.", "¡Le escribe una carta!"], "titulo": "LA CARTA", "sub": "y sus partes",
  "voz": ["Sofi quiere contarle algo a Tomi.", "Pero Tomi está de viaje.", "¡Le escribe una *carta*!", "Hoy: *las partes de una carta*."]},
 {"t": "zoom", "niveles": [{"emoji": "📅", "txt": "LUGAR Y FECHA"}, {"emoji": "👋", "txt": "SALUDO"}, {"emoji": "📝", "txt": "CUERPO"}, {"emoji": "🤗", "txt": "DESPEDIDA"}, {"emoji": "✍️", "txt": "FIRMA"}],
  "voz": ["Arriba: el *lugar y la fecha*.", "Después, el *saludo*: querido Tomi.", "En el medio, el *cuerpo*: lo que contamos.", "Después, la *despedida*: un abrazo.", "Al final, la *firma*: Sofi."]},
 {"t": "memoria", "titulo": "LAS PARTES DE LA CARTA", "items": ["LUGAR Y FECHA", "SALUDO", "CUERPO", "DESPEDIDA", "FIRMA"], "falta": 4,
  "voz": ["Mirá las cinco partes.", "Se tapan… ¡y una desapareció!", "¡Faltaba la *firma*!"]},
 {"t": "pregunta", "pregunta": "«Un abrazo» es…", "opciones": ["EL SALUDO", "LA DESPEDIDA"], "correcta": 1,
  "voz": ["Un abrazo, ¿qué parte es?", "Pensá: ¿va al principio o al final?", "¡La *despedida*! Va antes de la firma."]},
 {"t": "consejo", "titulo": "DE ARRIBA A ABAJO", "texto": "Fecha, saludo, cuerpo, despedida, firma", "emoji": "⬇️",
  "voz": ["Truco: fecha, saludo, cuerpo, despedida y firma."]},
 {"t": "resumen", "items": [["ARRIBA", "lugar, fecha y saludo"], ["MEDIO", "el cuerpo"], ["FINAL", "despedida y firma"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Arriba*: lugar, fecha y saludo.", "En el *medio*: el cuerpo.", "Al *final*: despedida y firma.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué pensás antes de escribir una carta?", "segundos": 8, "respuesta": "¡A quién y qué le cuento!", "emoji": "🤔", "titulo": "ESCRIBIR", "sub": "una carta",
  "voz": ["Desafío: ¿qué pensamos antes de escribir una carta?", "¡*A quién* le escribo y *qué* le cuento!", "Hoy: *escribir una carta a un compañero*."]},
 {"t": "pizarra", "titulo": "LA CARTA DE SOFI", "lineas": [{"txt": "Córdoba, lunes 15", "color": "azul"}, {"txt": "Querido Tomi:", "marca": "circulo", "color": "coral"}, {"txt": "Fui a la plaza y vi un hornero.", "color": "verde"}, {"txt": "Un abrazo,", "color": "lila"}, {"txt": "Sofi", "marca": "subraya"}],
  "voz": ["Sofi escribe el lugar y la fecha.", "El saludo: querido Tomi.", "El cuerpo: fui a la plaza y vi un hornero.", "La despedida: un abrazo.", "Y la firma: Sofi."]},
 {"t": "mazo", "titulo": "IDEAS PARA LA CARTA", "items": [{"frente": "Saludos", "dorso": "QUERIDO · HOLA", "emoji": "👋"}, {"frente": "Despedidas", "dorso": "UN ABRAZO · BESOS · CHAU", "emoji": "🤗"}, {"frente": "¿Qué cuento?", "dorso": "ALGO QUE ME PASÓ", "emoji": "📝"}],
  "voz": ["Para saludar: *querido* u *hola*.", "Para despedirse: *un abrazo*, *besos*, *chau*.", "Para el cuerpo: algo que nos *pasó*."]},
 {"t": "errores", "items": [{"mal": "Carta sin firma", "bien": "Firmar con tu nombre"}],
  "voz": ["Cuidado con este error.", "¡No te olvides de *firmar*!"]},
 {"t": "consejo", "titulo": "PENSÁ ANTES", "texto": "¿A quién le escribo? ¿Qué le cuento?", "emoji": "💭",
  "voz": ["Truco: antes de escribir, pensá *a quién* y *qué*."]},
 {"t": "resumen", "items": [["PENSAR", "a quién y qué"], ["ESCRIBIR", "cada parte en su lugar"], ["REVISAR", "las cinco partes"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Pensamos* a quién y qué contar.", "*Escribimos* cada parte en su lugar.", "*Revisamos* que estén las cinco.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¡Mandame tu ficha! 📧"}, {"yo": True, "txt": "¡Te la mando por correo!"}], "titulo": "CORREO", "sub": "electrónico",
  "voz": ["Tomi le pide a Sofi: ¡mandame tu ficha!", "Sofi responde: ¡te la mando por correo!", "Hoy: *el correo electrónico*."]},
 {"t": "definicion", "palabra": "Correo electrónico", "texto": "Carta que se manda por computadora o celular", "emoji": "💻",
  "voz": ["El *correo electrónico* es una carta por computadora.", "¡Llega en un ratito!"]},
 {"t": "matriz", "titulo": "LAS PARTES DEL CORREO", "celdas": [{"cab": "PARA", "txt": "a quién va"}, {"cab": "ASUNTO", "txt": "de qué trata"}, {"cab": "MENSAJE", "txt": "lo que contamos"}, {"cab": "ENVIAR", "txt": "el botón para mandarlo"}],
  "voz": ["El correo tiene sus partes.", "*Para*: a quién va.", "*Asunto*: de qué trata.", "*Mensaje*: lo que contamos.", "*Enviar*: el botón para mandarlo."]},
 {"t": "vof", "afirmacion": "El correo electrónico necesita estampilla", "emoji": "📮", "verdadero": False, "explicacion": "Se manda por computadora",
  "voz": ["¿Verdadero o falso? El correo necesita estampilla.", "Pensá: ¿cómo se manda?", "¡*Falso*! Se manda por computadora o celular."]},
 {"t": "consejo", "titulo": "CON UN ADULTO", "texto": "Usá el correo siempre acompañado", "emoji": "🧑‍🧒",
  "voz": ["Truco: usá el correo siempre con un *adulto*."]},
 {"t": "resumen", "items": [["CORREO", "carta por computadora"], ["PARA", "a quién va"], ["ASUNTO", "de qué trata"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *correo* es una carta por computadora.", "*Para* dice a quién va.", "El *asunto* dice de qué trata.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "CORREO", "titular": "¡Tomi recibió la carta de Sofi!", "bajada": "Y ahora le va a responder", "emoji": "📬", "titulo": "RESPONDER", "sub": "una carta",
  "voz": ["¡Noticia: Tomi recibió la carta de Sofi!", "Y ahora le va a *responder*.", "Hoy: *responder una carta*."]},
 {"t": "pistas", "problema": "¿Qué tiene que hacer Tomi?", "pistas": ["Leer la carta entera", "Buscar si hay una pregunta", "Contestar y contar algo suyo"], "respuesta": "¡Responder la carta! ✉️",
  "voz": ["¿Qué tiene que hacer Tomi para responder?", "Primero, *leer* la carta entera.", "Después, buscar si hay una *pregunta*.", "Al final, *contestar* y contar algo suyo.", "¡Así se responde una carta!"]},
 {"t": "tipeo", "titulo": "LA RESPUESTA DE TOMI", "items": [{"p": "Saludo", "r": "Querida Sofi:"}, {"p": "Respuesta", "r": "¡Sí! Vi un hornero en el campo."}],
  "voz": ["Tomi saluda: querida Sofi.", "Y contesta: ¡sí! Vi un hornero en el campo."]},
 {"t": "errores", "items": [{"mal": "No contestar la pregunta", "bien": "Contestar lo que preguntan"}],
  "voz": ["Cuidado con este error.", "Si la carta pregunta algo, lo *contestamos*."]},
 {"t": "consejo", "titulo": "BUSCÁ LA PREGUNTA", "texto": "Si te preguntan algo, contestalo", "emoji": "❓",
  "voz": ["Truco: buscá la *pregunta* y contestala."]},
 {"t": "resumen", "items": [["LEER", "la carta entera"], ["CONTESTAR", "la pregunta"], ["ESCRIBIR", "con todas las partes"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Leemos* la carta entera.", "*Contestamos* la pregunta.", "*Escribimos* con todas las partes.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m13-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 13 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
