# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 7 · Conflictos del pasado: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (investiga desacuerdos de antes y de hoy).
VARIANTE: la clase 1 lleva su parte "neutro"; las otras son iguales para todos ("sin_variante").
Genera tools/medio/clase/lecciones/medio-soc2-m7-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '85dc4ed7-c0dd-4d6f-addc-6086e8436362', 2: '286edde1-d491-4253-8bc4-511f051384dc', 3: '61e96492-9c23-4e94-bde9-73ea79525c9c', 4: '51c199e5-0d8c-4724-a46d-3dab15c78e15'}
TIT = {1: 'Conflictos por el uso de un territorio', 2: 'Reclamos de las personas que trabajaban', 3: 'Cómo se resolvía un conflicto antes', 4: 'Cómo resolvemos conflictos hoy'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
LOLA = {"nombre": "Lola", "emoji": "👧🎤"}

N1 = [
 {"t": "reto", "texto": "¿Qué pasa si dos chicos quieren la misma pelota?", "segundos": 8, "respuesta": "¡Hay un conflicto!", "emoji": "⚽", "titulo": "CONFLICTOS", "sub": "por el territorio",
  "voz": ["Desafío: ¿y si dos quieren la misma *pelota*?", "¡Hay un *conflicto*: no están de acuerdo!", "Hoy: *conflictos por el territorio*."]},
 {"t": "historieta", "titulo": "HACE MUCHO TIEMPO", "vinetas": [{"emojis": ["🏕️", "🌽"], "txt": "Vivían los pueblos originarios"}, {"emojis": ["⛵", "🐴"], "txt": "Llegaron los españoles"}, {"emojis": ["⚔️", "🌄"], "txt": "Querían la misma tierra"}],
  "voz": ["Aquí vivían los *pueblos originarios*: cazaban y sembraban.", "Un día llegaron los *españoles* en barco.", "Querían la misma tierra: ¡hubo *luchas*!"],
  "neutro": {"voz": ["En América vivían los *pueblos originarios*: cazaban y sembraban.", "Un día llegaron los *españoles* en barco.", "Querían la misma tierra: ¡hubo *luchas*!"]}},
 {"t": "definicion", "palabra": "Territorio", "texto": "Un lugar de tierra que un grupo usa para vivir", "emoji": "🗺️",
  "voz": ["Un *territorio* es la tierra que usa un grupo.", "Para vivir, cazar o *sembrar*."]},
 {"t": "vof", "afirmacion": "Antes nadie vivía en estas tierras", "emoji": "🏕️", "verdadero": False, "explicacion": "Vivían los pueblos originarios",
  "voz": ["¿Verdadero o falso? Antes nadie vivía acá.", "Pensá en la historieta…", "¡*Falso*! Vivían los pueblos originarios."]},
 {"t": "pasos", "titulo": "UN CONFLICTO", "items": [{"txt": "Dos quieren lo mismo", "emoji": "🙋"}, {"txt": "No se ponen de acuerdo", "emoji": "😠"}, {"txt": "¡Conflicto!", "emoji": "⚡"}],
  "voz": ["¿Cómo empieza un conflicto? Veamos.", "Dos personas o grupos *quieren lo mismo*.", "No se ponen de *acuerdo*.", "¡Y aparece un *conflicto*!"]},
 {"t": "consejo", "titulo": "¿QUIEREN LO MISMO?", "texto": "Ahí puede haber conflicto", "emoji": "🤔",
  "voz": ["Truco: si dos quieren *lo mismo*, puede haber conflicto."]},
 {"t": "resumen", "items": [["CONFLICTO", "no estar de acuerdo"], ["TERRITORIO", "tierra para vivir"], ["ANTES", "luchas por la tierra"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *conflicto* es no estar de acuerdo.", "El *territorio* es la tierra de un grupo.", "Antes hubo *luchas* por la tierra.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "VIAJE AL PASADO", "titular": "¡Los obreros hacen huelga!", "bajada": "Piden menos horas de trabajo", "emoji": "🪧", "titulo": "RECLAMOS", "sub": "de los trabajadores",
  "voz": ["¡Noticia del pasado: los obreros hacen *huelga*!", "Piden trabajar *menos horas*.", "Hoy: *reclamos de los trabajadores*."]},
 {"t": "pistas", "problema": "¿Qué es?", "pistas": ["Muchos trabajadores", "Se unen", "Reclaman juntos"], "respuesta": "¡EL SINDICATO! 🤝",
  "voz": ["Adivinanza: ¿qué es?", "Pista uno: muchos trabajadores.", "Pista dos: se unen.", "Pista tres: reclaman juntos.", "¡El *sindicato*!"]},
 {"t": "prediccion", "pregunta": "¿Se escucha más un reclamo de uno o de muchos?", "a": {"txt": "DE MUCHOS", "emoji": "👥"}, "b": {"txt": "DE UNO SOLO", "emoji": "👤"}, "correcta": "a", "resultado": "Juntos, los reclamos se escuchan más",
  "voz": ["¿Se escucha más el reclamo de *uno* o de *muchos*?", "Pensá…", "¡De *muchos*! Juntos se escucha más."]},
 {"t": "pasos", "titulo": "UN RECLAMO", "items": [{"txt": "Trabajan sin descanso", "emoji": "😓"}, {"txt": "Se juntan", "emoji": "🤝"}, {"txt": "Hacen carteles", "emoji": "🪧"}, {"txt": "Consiguen leyes", "emoji": "📜"}],
  "voz": ["Seguimos un reclamo, paso a paso.", "Los obreros trabajan *sin descanso*.", "Se *juntan* en el sindicato.", "Hacen *carteles* y marchan por la calle.", "Con el tiempo, consiguen *leyes* que los cuidan."]},
 {"t": "pregunta", "pregunta": "¿Qué es una huelga?", "opciones": ["DEJAR DE TRABAJAR JUNTOS", "IRSE DE VACACIONES"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué es una huelga?", "Pensá en el reclamo.", "¡Dejar de trabajar *juntos* para reclamar!"]},
 {"t": "consejo", "titulo": "SIN LASTIMAR", "texto": "Se reclama sin lastimar a nadie", "emoji": "🕊️",
  "voz": ["Truco: se reclama sin *lastimar* a nadie."]},
 {"t": "resumen", "items": [["RECLAMO", "pedir lo justo"], ["HUELGA", "dejar de trabajar juntos"], ["SINDICATO", "trabajadores unidos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *reclamo* es pedir lo justo.", "La *huelga* es dejar de trabajar juntos.", "El *sindicato* une a los trabajadores.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Abuelo Tito", "emoji": "👴"}, "mensajes": [{"yo": False, "txt": "Antes, muchas peleas terminaban mal 😔"}, {"yo": True, "txt": "¿Cómo se resolvían?"}], "titulo": "CÓMO SE RESOLVÍA", "sub": "antes",
  "voz": ["El abuelo escribe: antes, muchas peleas terminaban mal.", "Lola pregunta: ¿cómo se *resolvían*?", "Hoy: *cómo se resolvía un conflicto antes*."]},
 {"t": "linea", "titulo": "ANTES", "eventos": [{"fecha": "1", "txt": "con peleas", "emoji": "⚔️"}, {"fecha": "2", "txt": "ganaba el más fuerte", "emoji": "💪"}, {"fecha": "3", "txt": "decidía el que mandaba", "emoji": "👑"}],
  "voz": ["Antes, muchos conflictos se resolvían con *peleas*.", "Muchas veces ganaba el *más fuerte*.", "O decidía el que *mandaba*, sin preguntar."]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Forzudo", "emoji": "👹"}, "preguntas": [{"p": "¿Ser fuerte da la razón?", "r": "NO"}, {"p": "¿Hay que escuchar a todos?", "r": "SÍ"}],
  "voz": ["¡Apareció el *Monstruo Forzudo*!", "Cree que por ser fuerte tiene razón.", "¿Ser fuerte da la razón? ¡*No*!", "¿Hay que escuchar a todos? ¡*Sí*! ¡Ganamos!"]},
 {"t": "pasos", "titulo": "UN CONFLICTO DE ANTES", "items": [{"txt": "Querían un río", "emoji": "🏞️"}, {"txt": "No hablaron", "emoji": "🤐"}, {"txt": "Se pelearon", "emoji": "⚔️"}, {"txt": "Ganó el más fuerte", "emoji": "💪"}],
  "voz": ["Veamos un conflicto de antes, paso a paso.", "Dos grupos querían el mismo *río*.", "No se sentaron a *hablar*.", "Se *pelearon*.", "Y ganó el más fuerte, aunque no tuviera razón."]},
 {"t": "pregunta", "pregunta": "¿Antes podían opinar todos?", "opciones": ["NO, MUCHOS NO PODÍAN", "SÍ, TODOS"], "correcta": 0,
  "voz": ["Ahora vos: ¿antes opinaban todos?", "Pensá en las mujeres y los pobres.", "¡*No*! Muchos no podían opinar."]},
 {"t": "consejo", "titulo": "LA FUERZA NO DA LA RAZÓN", "texto": "Hay que escuchar a todos", "emoji": "👂",
  "voz": ["Truco: la *fuerza* no da la razón."]},
 {"t": "resumen", "items": [["PELEAS", "así se resolvía"], ["EL MÁS FUERTE", "muchas veces ganaba"], ["INJUSTO", "no opinaban todos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Antes se resolvía con *peleas*.", "Muchas veces ganaba el más *fuerte*.", "Era *injusto*: no opinaban todos.", CIERRE]},
]
N4 = [
 {"t": "dialogo", "personas": [{"nombre": "ANA", "emoji": "👧"}, {"nombre": "LUIS", "emoji": "👦"}], "lineas": [{"quien": 0, "txt": "Yo quiero jugar al fútbol."}, {"quien": 1, "txt": "Y yo, a la mancha."}, {"quien": 0, "txt": "¡Hoy fútbol y mañana mancha!"}, {"quien": 1, "txt": "¡Trato hecho!"}],
  "voz": ["Yo quiero jugar al fútbol.", "Y yo, a la mancha.", "¡Hoy fútbol y mañana mancha!", "¡Trato hecho!"]},
 {"t": "definicion", "palabra": "Acuerdo", "texto": "Cuando todos aceptan una solución después de hablar", "emoji": "🤝",
  "voz": ["Ana y Luis hicieron un *acuerdo*.", "Hablaron, se escucharon y aceptaron una *solución*."]},
 {"t": "escape", "titulo": "LA SALA DEL ACUERDO", "candados": [{"p": "¿Qué hago primero?", "r": "DIGO LO QUE PASA"}, {"p": "¿Y después?", "r": "ESCUCHO AL OTRO"}],
  "voz": ["¡Para salir de la sala, abrimos los candados!", "Primero, *digo* lo que pasa.", "Después, *escucho* al otro.", "¡Salimos con un acuerdo!"]},
 {"t": "pasos", "titulo": "VOTAR", "items": [{"txt": "Hay varias ideas", "emoji": "💡"}, {"txt": "Cada uno elige", "emoji": "✋"}, {"txt": "Contamos", "emoji": "🔢"}, {"txt": "Gana la más elegida", "emoji": "🏆"}],
  "voz": ["Si somos muchos, podemos *votar*.", "Hay *varias ideas* para elegir.", "Cada uno levanta la mano por *una*.", "*Contamos* las manos.", "¡Gana la idea más elegida!"]},
 {"t": "pregunta", "pregunta": "¿Cómo resolvemos un conflicto hoy?", "opciones": ["HABLANDO Y ESCUCHANDO", "PELEANDO"], "correcta": 0,
  "voz": ["Ahora vos: ¿cómo resolvemos hoy?", "Pensá en Ana y Luis.", "¡*Hablando* y escuchando!"]},
 {"t": "consejo", "titulo": "TURNOS", "texto": "Uno habla y el otro escucha", "emoji": "🗣️",
  "voz": ["Truco: uno *habla* y el otro escucha."]},
 {"t": "resumen", "items": [["HABLAR", "digo lo que pasa"], ["ESCUCHAR", "sin interrumpir"], ["ACUERDO O VOTO", "para decidir"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero *hablamos*.", "Después *escuchamos* sin interrumpir.", "Decidimos con un *acuerdo* o votando.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc2-m7-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Sociales 2", "titulo": TIT[n], "sub": f"Ciencias Sociales 2 · Misión 7 · Nivel {n}", "estilo": "primeros", "escenas": E}
    if n > 1: L["sin_variante"] = True
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
