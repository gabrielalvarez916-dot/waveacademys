# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 8 · Cómo vivían antes: las 4 clases animadas.
Metáfora: la máquina del tiempo de Sofi. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-soc1-m8-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = '67d2ad89-caaa-4e82-8d25-8bbb08147818'
TEMA = 8
TIT = {1: 'Entrevista a una persona mayor', 2: 'Objetos que cambiaron con el tiempo', 3: 'Una familia del antiguo Egipto', 4: 'Qué cambió y qué sigue igual'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Qué hacés?"}, {"yo": True, "txt": "¡ENTREVISTO A MI ABUELA!"}, {"yo": False, "txt": "¿Y qué te cuenta?"}], "titulo": "UNA ENTREVISTA", "sub": "a una persona mayor",
  "voz": ["Tomi le escribe a Sofi.", "¿Qué hacés?", "Sofi *entrevista* a su abuela.", "Hoy: *entrevista a una persona mayor*."]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "ABUELA", "emoji": "👵"}], "lineas": [{"quien": 0, "txt": "¿A QUÉ JUGABAS?"}, {"quien": 1, "txt": "¡A LA RAYUELA!"}, {"quien": 0, "txt": "¿HABÍA TELE?"}, {"quien": 1, "txt": "NO, ESCUCHÁBAMOS LA RADIO."}],
  "voz": ["Sofi pregunta: ¿a qué jugabas?", "La abuela dice: ¡a la *rayuela*!", "Sofi pregunta: ¿había tele?", "No, escuchábamos la *radio*."]},
 {"t": "flujo", "titulo": "CÓMO ENTREVISTO", "items": ["PREPARO", "PREGUNTO", "ESCUCHO", "ANOTO"],
  "voz": ["Primero, *preparo* las preguntas.", "Después, *pregunto*.", "*Escucho* con atención.", "Y *anoto* lo que me cuentan."]},
 {"t": "pregunta", "pregunta": "¿A quién entrevistás para saber cómo era antes?", "opciones": ["UN BEBÉ", "UNA PERSONA MAYOR", "UN PERRO"], "correcta": 1,
  "voz": ["Ahora vos. Querés saber cómo era antes.", "¿A quién le preguntás?", "¡A una persona *mayor*!"]},
 {"t": "consejo", "titulo": "ESCUCHÁ", "texto": "Mirá a la persona y no interrumpas", "emoji": "👂",
  "voz": ["Truco: *escuchá* sin interrumpir."]},
 {"t": "resumen", "items": [["ENTREVISTA", "preguntar y aprender"], ["PASOS", "preparo, pregunto, anoto"], ["ESCUCHAR", "sin interrumpir"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *entrevista* es preguntar y aprender.", "Preparo, pregunto y *anoto*.", "Y *escucho* sin interrumpir.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📦", "lineas": ["Sofi encuentra una caja vieja.", "Adentro hay un teléfono raro.", "¡Tiene un disco con números!"], "titulo": "OBJETOS", "sub": "que cambiaron",
  "voz": ["Sofi encuentra una *caja* vieja.", "Adentro hay un teléfono raro.", "¡Tiene un *disco* con números!", "Hoy: *objetos que cambiaron con el tiempo*."]},
 {"t": "comparar", "a": {"cab": "ANTES", "texto": "TELÉFONO CON CABLE", "emoji": "☎️"}, "b": {"cab": "AHORA", "texto": "CELULAR", "emoji": "📱"}, "signo": "vs",
  "voz": ["*Antes*, el teléfono tenía cable.", "*Ahora*, lo llevamos en el bolsillo.", "¡El teléfono *cambió* mucho!"]},
 {"t": "linea", "titulo": "EL TELÉFONO CAMBIA", "eventos": [{"fecha": "HACE MUCHO", "txt": "CON DISCO", "emoji": "☎️"}, {"fecha": "DESPUÉS", "txt": "CON BOTONES", "emoji": "📞"}, {"fecha": "HOY", "txt": "CELULAR", "emoji": "📱"}],
  "voz": ["Hace mucho, tenía *disco*.", "Después, tuvo *botones*.", "¡Hoy es un *celular*!"]},
 {"t": "pregunta", "pregunta": "¿Qué objeto casi no cambió?", "opciones": ["TELÉFONO", "CUCHARA", "RADIO"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en la cocina.", "¿Qué objeto casi no cambió?", "¡La *cuchara*!"]},
 {"t": "consejo", "titulo": "PREGUNTÁ", "texto": "Los grandes recuerdan cómo eran las cosas", "emoji": "👴",
  "voz": ["Truco: preguntá a los *grandes* cómo eran las cosas."]},
 {"t": "resumen", "items": [["CAMBIOS", "los objetos cambian"], ["TELÉFONO", "disco, botones, celular"], ["IGUAL", "algunos casi no cambian"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los objetos *cambian* con el tiempo.", "El *teléfono* cambió mucho.", "Algunos casi *no cambian*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué río famoso cruza Egipto?", "segundos": 6, "respuesta": "¡EL RÍO NILO!", "emoji": "🏺", "titulo": "EL ANTIGUO EGIPTO", "sub": "una familia",
  "voz": ["Desafío: ¿qué río famoso cruza Egipto?", "¡El río *Nilo*!", "Hoy: *una familia del antiguo Egipto*."]},
 {"t": "zoom", "niveles": [{"emoji": "🌍", "txt": "EL MUNDO"}, {"emoji": "🏜️", "txt": "EGIPTO"}, {"emoji": "🏠", "txt": "CASA DE ADOBE"}],
  "voz": ["Miramos el *mundo*.", "Nos acercamos a *Egipto*.", "¡Vemos una casa de *adobe* junto al río!"]},
 {"t": "matriz", "titulo": "UNA FAMILIA EGIPCIA", "celdas": [{"cab": "🍞 COMIDA", "txt": "PAN Y PESCADO"}, {"cab": "👕 ROPA", "txt": "LINO"}, {"cab": "🪀 JUEGOS", "txt": "MUÑECAS Y PELOTAS"}, {"cab": "📜 ESCRIBÍAN", "txt": "EN PAPIRO"}],
  "voz": ["Así vivía una familia *egipcia*.", "Comían *pan* y pescado.", "Se vestían con *lino*.", "Jugaban con *muñecas* y pelotas.", "Escribían en *papiro*."]},
 {"t": "pregunta", "pregunta": "¿En qué se parecen a vos?", "opciones": ["TENÍAN CELULAR", "TAMBIÉN JUGABAN", "MIRABAN TELE"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en los chicos de Egipto.", "¿En qué se parecen a vos?", "¡*También jugaban*!"]},
 {"t": "consejo", "titulo": "COMPARÁ", "texto": "Buscá qué se parece a tu vida", "emoji": "🔍",
  "voz": ["Truco: buscá qué se *parece* a tu vida."]},
 {"t": "resumen", "items": [["NILO", "vivían junto al río"], ["CASAS", "de adobe"], ["JUEGOS", "muñecas y pelotas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Vivían junto al río *Nilo*.", "Sus casas eran de *adobe*.", "Y jugaban con *muñecas* y pelotas.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡SOFI VIAJA EN EL TIEMPO!", "bajada": "¿Qué cambió y qué sigue igual?", "emoji": "⏳", "titulo": "CAMBIOS", "sub": "y lo que sigue igual",
  "voz": ["¡Último momento! Sofi *viaja* en el tiempo.", "¿Qué cambió y qué sigue igual?", "Hoy: *qué cambió y qué sigue igual*."]},
 {"t": "venn", "a": "ANTES", "b": "AHORA", "itemsA": ["CARRETA", "LÁMPARA DE ACEITE"], "itemsB": ["AUTO", "FOCO"], "ambos": ["FAMILIA", "JUGAR"],
  "voz": ["Comparamos *antes* y *ahora*.", "Antes: carreta y lámpara de aceite.", "Ahora: auto y foco.", "¡En los dos: *familia* y jugar!"]},
 {"t": "antesdespues", "antes": {"cab": "ANTES", "emoji": "🐎", "texto": "En carreta"}, "despues": {"cab": "AHORA", "emoji": "🚗", "texto": "En auto"},
  "voz": ["*Antes* se viajaba en carreta.", "*Ahora* viajamos en auto."]},
 {"t": "pregunta", "pregunta": "¿Qué sigue igual desde siempre?", "opciones": ["EL TELÉFONO", "JUGAR CON AMIGOS", "LA LUZ"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en los abuelos y en vos.", "¿Qué sigue igual?", "¡*Jugar con amigos*!"]},
 {"t": "consejo", "titulo": "DOS LISTAS", "texto": "Cambió y sigue igual", "emoji": "📝",
  "voz": ["Truco: hacé dos listas: *cambió* y *sigue igual*."]},
 {"t": "resumen", "items": [["CAMBIÓ", "teléfono, luz, autos"], ["SIGUE IGUAL", "familia, jugar"], ["COMPARAR", "antes y ahora"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Algunas cosas *cambiaron*.", "Otras *siguen igual*.", "Y aprendimos a *comparar*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Sociales 1", "titulo": TIT[n], "sub": f"Ciencias Sociales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
