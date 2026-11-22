# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 9 · Ordenar el tiempo: las 4 clases animadas.
Metáfora: el calendario mágico de Sofi. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-soc1-m9-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = '67d2ad89-caaa-4e82-8d25-8bbb08147818'
TEMA = 9
TIT = {1: 'Ayer, hoy y mañana en mi día', 2: 'Los días y los meses del calendario escolar', 3: 'Mi línea de tiempo personal', 4: 'Huellas del pasado en fotos y objetos'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📅", "lineas": ["Ayer Sofi fue a la plaza.", "Hoy está en la escuela.", "¡Mañana va a un cumple!"], "titulo": "AYER, HOY", "sub": "y mañana",
  "voz": ["*Ayer* Sofi fue a la plaza.", "*Hoy* está en la escuela.", "¡*Mañana* va a un cumple!", "Hoy: *ayer, hoy y mañana*."]},
 {"t": "linea", "titulo": "LOS DÍAS DE SOFI", "eventos": [{"fecha": "AYER", "txt": "PLAZA", "emoji": "🛝"}, {"fecha": "HOY", "txt": "ESCUELA", "emoji": "🏫"}, {"fecha": "MAÑANA", "txt": "CUMPLE", "emoji": "🎂"}],
  "voz": ["*Ayer*: ya pasó.", "*Hoy*: es ahora.", "*Mañana*: todavía no llegó."]},
 {"t": "ciclo", "titulo": "MI DÍA", "items": ["MAÑANA", "TARDE", "NOCHE"],
  "voz": ["El día tiene *partes*.", "A la *mañana*, voy a la escuela.", "A la *tarde*, juego.", "A la *noche*, duermo. ¡Y otra vez!"]},
 {"t": "pregunta", "pregunta": "Lo que ya pasó es…", "opciones": ["MAÑANA", "AYER", "HOY"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en lo que ya pasó.", "¿Cómo se llama?", "¡*Ayer*!"]},
 {"t": "consejo", "titulo": "ANTES Y DESPUÉS", "texto": "Esas palabras ordenan lo que pasa", "emoji": "⏳",
  "voz": ["Truco: *antes* y *después* ordenan lo que pasa."]},
 {"t": "resumen", "items": [["AYER", "ya pasó"], ["HOY", "ahora"], ["MAÑANA", "todavía no llegó"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Ayer* ya pasó.", "*Hoy* es ahora.", "*Mañana* todavía no llegó.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Mañana hay escuela?"}, {"yo": True, "txt": "¡NO! ¡ES SÁBADO!"}, {"yo": False, "txt": "¡Qué bueno!"}], "titulo": "EL CALENDARIO", "sub": "días y meses",
  "voz": ["Tomi le escribe a Sofi.", "¿Mañana hay escuela?", "¡No! ¡Es *sábado*!", "Hoy: *los días y los meses*."]},
 {"t": "bloques", "titulo": "LA SEMANA", "items": [{"cab": "🏫 5 DÍAS", "txt": "LUNES A VIERNES"}, {"cab": "🏠 2 DÍAS", "txt": "SÁBADO Y DOMINGO"}],
  "voz": ["La semana tiene *7 días*.", "De lunes a viernes, *escuela*.", "Sábado y domingo, *descanso*."]},
 {"t": "barras", "titulo": "MI SEMANA", "unidad": "días", "items": [{"txt": "CON ESCUELA", "valor": 5}, {"txt": "SIN ESCUELA", "valor": 2}],
  "voz": ["Contamos los días.", "Con escuela: *5* días.", "Sin escuela: *2* días."]},
 {"t": "pregunta", "pregunta": "¿Cuántos meses tiene el año?", "opciones": ["7", "12", "30"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el calendario.", "¿Cuántos meses tiene el año?", "¡*12* meses!"]},
 {"t": "consejo", "titulo": "CANTALOS", "texto": "Decí los días como una canción", "emoji": "🎵",
  "voz": ["Truco: decí los días como una *canción*."]},
 {"t": "resumen", "items": [["SEMANA", "7 días"], ["AÑO", "12 meses"], ["CALENDARIO", "clases y vacaciones"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *semana* tiene 7 días.", "El *año* tiene 12 meses.", "El *calendario* marca clases y vacaciones.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué pasó primero: naciste o fuiste al jardín?", "segundos": 6, "respuesta": "¡NACÍ!", "emoji": "👶", "titulo": "MI LÍNEA", "sub": "de tiempo",
  "voz": ["Desafío: ¿qué pasó primero?", "¡Primero *naciste*!", "Hoy: *mi línea de tiempo*."]},
 {"t": "orden", "titulo": "ORDENAMOS LAS FOTOS", "items": [{"txt": "NACÍ", "emoji": "👶"}, {"txt": "CAMINÉ", "emoji": "🚶"}, {"txt": "JARDÍN", "emoji": "🎨"}, {"txt": "PRIMER GRADO", "emoji": "🎒"}], "relato": [3, 0, 2, 1],
  "voz": ["Las fotos de Sofi se *mezclaron*.", "Las ponemos en *orden*.", "¡De antes a ahora!"]},
 {"t": "linea", "titulo": "LA LÍNEA DE SOFI", "eventos": [{"fecha": "1", "txt": "NACÍ", "emoji": "👶"}, {"fecha": "2", "txt": "CAMINÉ", "emoji": "🚶"}, {"fecha": "3", "txt": "JARDÍN", "emoji": "🎨"}, {"fecha": "4", "txt": "PRIMER GRADO", "emoji": "🎒"}],
  "voz": ["Primero, Sofi *nació*.", "Después, *caminó*.", "Fue al *jardín*.", "¡Y ahora está en *primer grado*!"]},
 {"t": "pregunta", "pregunta": "¿Qué va al final de la línea?", "opciones": ["NACÍ", "PRIMER GRADO", "CAMINÉ"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en la línea.", "¿Qué va al final?", "¡*Primer grado*: es lo de ahora!"]},
 {"t": "consejo", "titulo": "PREGUNTÁ EN CASA", "texto": "Tu familia recuerda cuándo pasó", "emoji": "👪",
  "voz": ["Truco: preguntá en casa *cuándo* pasó cada cosa."]},
 {"t": "resumen", "items": [["LÍNEA", "hechos en orden"], ["ANTES", "a la izquierda"], ["AHORA", "a la derecha"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *línea de tiempo* ordena los hechos.", "Lo de *antes* va primero.", "Lo de *ahora* va al final.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡UNA CAJA DE FOTOS VIEJAS!", "bajada": "Sofi la encontró en lo de la abuela", "emoji": "📦", "titulo": "HUELLAS", "sub": "del pasado",
  "voz": ["¡Último momento! Sofi encontró fotos *viejas*.", "Estaban en lo de la abuela.", "Hoy: *huellas del pasado*."]},
 {"t": "zoom", "niveles": [{"emoji": "📦", "txt": "LA CAJA"}, {"emoji": "🖼️", "txt": "UNA FOTO VIEJA"}, {"emoji": "🐎", "txt": "UNA CARRETA"}],
  "voz": ["Abrimos la *caja*.", "Sacamos una *foto vieja*.", "¡Se ve una *carreta*! Es de hace mucho."]},
 {"t": "causas", "causa": {"txt": "UNA FOTO VIEJA NOS CUENTA", "emoji": "🖼️"}, "items": ["QUIÉNES ESTABAN", "DÓNDE ERA", "CÓMO SE VESTÍAN"],
  "voz": ["¿Qué nos cuenta una *foto vieja*?", "*Quiénes* estaban.", "*Dónde* era.", "Y *cómo* se vestían."]},
 {"t": "pregunta", "pregunta": "¿Cuál es una huella del pasado?", "opciones": ["CELULAR NUEVO", "FOTO VIEJA", "TELE NUEVA"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en lo viejo.", "¿Cuál es una huella del pasado?", "¡La *foto vieja*!"]},
 {"t": "consejo", "titulo": "CON CUIDADO", "texto": "Las fotos viejas se tocan despacio", "emoji": "🤲",
  "voz": ["Truco: las fotos viejas se tocan con *cuidado*."]},
 {"t": "resumen", "items": [["HUELLA", "cuenta cómo era antes"], ["FOTOS", "quiénes, dónde, cómo"], ["OBJETOS", "juguetes, cartas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *huella* nos cuenta el pasado.", "Las *fotos* nos dicen quiénes y dónde.", "Los *objetos* viejos también cuentan.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Sociales 1", "titulo": TIT[n], "sub": f"Ciencias Sociales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
