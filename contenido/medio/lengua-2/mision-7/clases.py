# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 7 · Textos informativos: las 4 clases animadas.
Vía fonológica: la voz no nombra letras. Metáfora: el cuaderno viajero de Sofi con la lámina del hornero.
Genera tools/medio/clase/lecciones/medio-leng2-m7-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '8e9b3dbb-49ca-4b6c-ac9a-77f6fd061726', 2: 'b10bb7f5-9e77-4eaa-8638-b8e832475c35', 3: 'af02cf02-a6c5-4f61-bbb6-64ffebe524e4', 4: 'b878486b-349f-4cb4-9be7-f94f067ab45c'}
TIT = {1: 'Títulos e imágenes', 2: 'Leer un texto informativo', 3: 'Subrayar datos importantes', 4: 'Responder por escrito'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "noticia", "cinta": "CUADERNO VIAJERO", "titular": "¡Sofi pegó una lámina nueva!", "bajada": "Tiene título, imagen y texto", "emoji": "📰", "titulo": "TÍTULOS", "sub": "e imágenes",
  "voz": ["¡Noticia: Sofi pegó una lámina en su cuaderno!", "Tiene un título, una imagen y un texto.", "Hoy: *títulos e imágenes*."]},
 {"t": "documental", "emojis": ["🐦", "🏠"], "lugar": "🇦🇷", "rotulos": [{"txt": "EL HORNERO", "sub": "el título"}, {"txt": "🐦", "sub": "la imagen"}, {"txt": "El hornero en su nido", "sub": "el epígrafe"}],
  "voz": ["Arriba está el *título*: el hornero.", "Después, la *imagen*: muestra cómo es.", "Debajo, el *epígrafe*: una frase de la imagen."]},
 {"t": "definicion", "palabra": "Título", "texto": "Dice de qué trata el texto", "emoji": "🏷️",
  "voz": ["El *título* dice de qué trata el texto.", "Lo leemos primero."]},
 {"t": "prediccion", "pregunta": "Título: LA VACA. ¿De qué trata?", "a": {"txt": "De un animal", "emoji": "🐄"}, "b": {"txt": "De un auto", "emoji": "🚗"}, "correcta": "a", "resultado": "¡Trata de la vaca, un animal!",
  "voz": ["El título dice: la vaca. ¿De qué trata?", "Pensá antes de leer…", "¡De un *animal*! El título nos avisó."]},
 {"t": "memoria", "titulo": "LAS PARTES DE LA LÁMINA", "items": ["TÍTULO", "IMAGEN", "EPÍGRAFE", "TEXTO"], "falta": 2,
  "voz": ["Mirá las partes de la lámina.", "Se tapan… ¡y una desapareció!", "¡Faltaba el *epígrafe*!"]},
 {"t": "resumen", "items": [["TÍTULO", "de qué trata"], ["IMAGEN", "cómo es"], ["EPÍGRAFE", "debajo de la imagen"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *título* dice de qué trata.", "La *imagen* muestra cómo es.", "El *epígrafe* va debajo de la imagen.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📚", "lineas": ["Sofi tiene dos textos.", "Uno es un cuento.", "El otro da datos."], "titulo": "LEER", "sub": "un texto informativo",
  "voz": ["Sofi tiene *dos textos*.", "Uno es un *cuento*.", "El otro da *datos* reales.", "Hoy: *leer un texto informativo*."]},
 {"t": "versus", "titulo": "¿CUENTO O INFORMATIVO?", "a": {"txt": "CUENTO", "emoji": "🧚", "datos": ["inventa una historia"]}, "b": {"txt": "INFORMATIVO", "emoji": "🐦", "datos": ["da datos reales"]}, "gana": "empate", "veredicto": "¡Los dos sirven para cosas distintas!",
  "voz": ["Comparamos dos textos.", "El *cuento* inventa una historia.", "El *informativo* da datos reales.", "¡Los dos sirven para cosas distintas!"]},
 {"t": "datoloco", "texto": "El nido del hornero parece un horno de barro", "emoji": "🏠",
  "voz": ["¿Sabías qué?", "¡El nido del hornero parece un *horno* de barro!"]},
 {"t": "vof", "afirmacion": "El hornero habla con los gatos", "emoji": "🐦", "verdadero": False, "explicacion": "Eso es de cuento",
  "voz": ["¿Verdadero o falso? El hornero habla con los gatos.", "Pensá: ¿pasa de verdad?", "¡*Falso*! Eso es de cuento, no es un dato."]},
 {"t": "consejo", "titulo": "¿PASA DE VERDAD?", "texto": "Si es real, es un dato", "emoji": "✅",
  "voz": ["Truco: si pasa de verdad, es un *dato*."]},
 {"t": "resumen", "items": [["CUENTO", "historia inventada"], ["INFORMATIVO", "datos reales"], ["DATO", "algo que es verdad"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *cuento* inventa una historia.", "El *informativo* da datos reales.", "Un *dato* es algo que es verdad.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué palabra es la más importante? HACE SU NIDO CON BARRO", "segundos": 8, "respuesta": "BARRO", "emoji": "🖍️", "titulo": "SUBRAYAR", "sub": "datos importantes",
  "voz": ["Desafío: ¿cuál es la palabra más importante?", "¡*Barro*! Dice con qué hace el nido.", "Hoy: *subrayar datos importantes*."]},
 {"t": "pizarra", "titulo": "EL HORNERO", "lineas": [{"txt": "Es un pájaro", "marca": "subraya"}, {"txt": "Hace su nido con barro", "marca": "subraya", "color": "coral"}, {"txt": "Come bichitos", "marca": "subraya", "color": "verde"}],
  "voz": ["Subrayamos: es un *pájaro*.", "Hace su nido con *barro*.", "Come *bichitos*."]},
 {"t": "patron", "titulo": "PALABRAS CLAVE", "items": ["PÁJARO", "BARRO", "HORNO", "BICHITOS"], "falta": 2, "regla": "Las palabras subrayadas",
  "voz": ["Leemos solo lo subrayado: pájaro, barro…", "¿Qué palabra falta?", "¡*Horno*! Con estas palabras recordamos todo."]},
 {"t": "contrarreloj", "titulo": "¿LA SUBRAYO?", "segundos": 20, "items": [{"p": "BICHITOS", "r": "SÍ"}, {"p": "EL", "r": "NO"}, {"p": "BARRO", "r": "SÍ"}],
  "voz": ["¡Ronda rápida! ¿La subrayo o no?", "Bichitos: *sí*, es importante.", "El: *no*, no dice nada solo.", "Barro: *sí*, es clave."]},
 {"t": "consejo", "titulo": "POCO Y BIEN", "texto": "Subrayá pocas palabras, las más importantes", "emoji": "🖍️",
  "voz": ["Truco: subrayá *pocas* palabras, las más importantes."]},
 {"t": "resumen", "items": [["SUBRAYAR", "marcar lo importante"], ["POCAS", "palabras clave"], ["REPASAR", "leer lo subrayado"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Subrayar* es marcar lo importante.", "Marcamos *pocas* palabras clave.", "Después *leemos* lo subrayado.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Con qué hace el nido el hornero? 🤔"}, {"yo": True, "txt": "¡Lo busco en mi lámina!"}], "titulo": "RESPONDER", "sub": "por escrito",
  "voz": ["Tomi pregunta: ¿con qué hace el nido el hornero?", "Sofi responde: ¡lo busco en mi lámina!", "Hoy: *responder por escrito*."]},
 {"t": "pasos", "titulo": "CÓMO RESPONDO", "items": [{"txt": "Leo la pregunta", "emoji": "❓"}, {"txt": "Busco en el texto", "emoji": "🔎"}, {"txt": "Escribo una oración", "emoji": "✏️"}],
  "voz": ["¿Cómo respondemos?", "Leemos la *pregunta*.", "Buscamos en el *texto*.", "Escribimos una *oración*."]},
 {"t": "tipeo", "titulo": "LA RESPUESTA DE SOFI", "items": [{"p": "¿Con qué hace el nido?", "r": "El hornero hace su nido con barro."}],
  "voz": ["Sofi escribe: el hornero hace su nido con barro."]},
 {"t": "corrige", "titulo": "TOMI REVISA", "cambios": [{"antes": "el hornero come bichitos", "despues": "El hornero come bichitos.", "motivo": "mayúscula y punto"}],
  "voz": ["Tomi escribió su respuesta. ¿Está bien?", "Le faltaba *mayúscula* al principio y *punto* al final."]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Preguntón", "emoji": "👾"}, "preguntas": [{"p": "¿Qué es el hornero?", "r": "Es un pájaro."}, {"p": "¿A qué se parece el nido?", "r": "A un horno."}],
  "voz": ["¡Apareció el *Monstruo Preguntón*!", "Respondemos con la lámina.", "¿Qué es el hornero? *Es un pájaro*.", "¿A qué se parece el nido? ¡*A un horno*! ¡Ganamos!"]},
 {"t": "resumen", "items": [["LEER", "la pregunta"], ["BUSCAR", "en el texto"], ["ESCRIBIR", "con mayúscula y punto"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Leemos* la pregunta.", "*Buscamos* en el texto.", "*Escribimos* con mayúscula y punto.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m7-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 7 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
