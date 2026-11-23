# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 11 · Ortografía: R y RR: las 4 clases animadas.
Vía fonológica: la VOZ dice sonidos (suave como en «pera», fuerte rrr como en «perro») y «una letra / dos letras»,
nunca nombres de letras; la pantalla muestra las letras. Metáfora: Sofi, detective de palabras.
Genera tools/medio/clase/lecciones/medio-leng2-m11-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '96102e83-f3b5-4493-97cd-ad1d8a5ca770', 2: '8c9adf29-c3da-4542-b98c-e3e6a4b93690', 3: '832e96c3-69ca-4d80-9ebb-317af99a4807', 4: 'bf88bb75-4c86-45b8-9071-d561cdb44acb'}
TIT = {1: 'Sonido suave y sonido fuerte', 2: 'Palabras con R inicial', 3: 'Palabras con RR', 4: 'Dictado con R y RR'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "🕵️‍♀️"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🔍", "lineas": ["La detective Sofi escucha.", "PERA y PERRO.", "¡Suenan distinto!"], "titulo": "SUAVE", "sub": "y fuerte",
  "voz": ["La detective Sofi escucha con atención.", "Pera… perro.", "¡Suenan *distinto*!", "Hoy: *sonido suave y sonido fuerte*."]},
 {"t": "comparar", "a": {"cab": "PERA", "texto": "sonido suave", "emoji": "🍐"}, "b": {"cab": "PERRO", "texto": "sonido fuerte", "emoji": "🐶"}, "signo": "≠", "def": {"cab": "LA PISTA", "texto": "suave: R · fuerte en el medio: RR"},
  "voz": ["En *pera*, el sonido es suave.", "En *perro*, es fuerte: rrr.", "¡Suenan distinto y se escriben distinto!", "Suave, una letra. Fuerte en el medio, dos letras."]},
 {"t": "prediccion", "pregunta": "¿CARO y CARRO son la misma palabra?", "a": {"txt": "Sí, son iguales", "emoji": "🟰"}, "b": {"txt": "No, cambian", "emoji": "🚗"}, "correcta": "b", "resultado": "CARO es costoso. CARRO es un auto.",
  "voz": ["¿Caro y carro son la misma palabra?", "Escuchá: caro… carro.", "¡No! Caro es *costoso*. Carro es un *auto*."]},
 {"t": "pregunta", "pregunta": "TORRE: ¿suave o fuerte?", "opciones": ["SUAVE", "FUERTE"], "correcta": 1,
  "voz": ["Ahora vos: torre.", "¿Suena suave o fuerte?", "¡*Fuerte*! Torre: rrr."]},
 {"t": "consejo", "titulo": "DECILO EN VOZ ALTA", "texto": "El sonido fuerte vibra más", "emoji": "🗣️",
  "voz": ["Truco: decí la palabra en voz alta. El fuerte *vibra*."]},
 {"t": "resumen", "items": [["SUAVE", "PERA, LORO"], ["FUERTE", "PERRO, TORRE"], ["CUIDADO", "cambia la palabra"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Suave*, como en pera y loro.", "*Fuerte*, como en perro y torre.", "Si cambia el sonido, cambia la palabra.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¡Vi un RRATÓN! 🐭"}, {"yo": True, "txt": "Mmm… ¿así se escribe?"}], "titulo": "R", "sub": "al principio",
  "voz": ["Tomi le escribe a Sofi: ¡vi un ratón!", "La detective mira la palabra… ¿así se escribe?", "Hoy: *palabras que empiezan con sonido fuerte*."]},
 {"t": "definicion", "palabra": "La pista", "texto": "Al principio suena fuerte, pero va una sola R", "emoji": "🔎",
  "voz": ["Al principio de la palabra, el sonido es fuerte.", "¡Pero se escribe con *una sola letra*!"]},
 {"t": "memoria", "titulo": "EMPIEZAN CON R", "items": ["RATÓN", "RANA", "ROSA", "RUEDA", "REGALO"], "falta": 3,
  "voz": ["Mirá estas palabras: todas empiezan fuerte.", "Se tapan… ¡y una desapareció!", "¡Faltaba *rueda*!"]},
 {"t": "mazo", "titulo": "¿CÓMO SE ESCRIBE?", "items": [{"frente": "🐭", "dorso": "RATÓN", "emoji": "🐭"}, {"frente": "😂", "dorso": "RISA", "emoji": "😂"}, {"frente": "⏰", "dorso": "RELOJ", "emoji": "⏰"}],
  "voz": ["*Ratón*: una sola letra al principio.", "*Risa*: también una sola.", "*Reloj*: ¡una sola!"]},
 {"t": "errores", "items": [{"mal": "RRATÓN", "bien": "RATÓN"}],
  "voz": ["Cuidado con este error.", "Nunca empezamos con dos letras: *ratón*."]},
 {"t": "resumen", "items": [["AL PRINCIPIO", "suena fuerte"], ["SE ESCRIBE", "una sola R"], ["EJEMPLOS", "RATÓN, ROSA"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Al principio*, el sonido es fuerte.", "Pero va *una sola letra*.", "Como en *ratón* y *rosa*.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "CASO NUEVO", "titular": "¡Un sonido fuerte en el medio!", "bajada": "La detective investiga PERRO", "emoji": "🐶", "titulo": "RR", "sub": "en el medio",
  "voz": ["¡Caso nuevo: un sonido fuerte en el medio!", "La detective investiga la palabra *perro*.", "Hoy: *palabras con dos letras juntas*."]},
 {"t": "definicion", "palabra": "La pista", "texto": "Fuerte entre dos vocales: RR", "emoji": "🔎",
  "voz": ["Si suena fuerte en el medio, entre vocales…", "¡se escribe con *dos letras juntas*!"]},
 {"t": "pistas", "problema": "¿Qué palabra con RR es?", "pistas": ["Es un animal", "Tiene orejas largas", "Hace iii-aaa"], "respuesta": "BURRO",
  "voz": ["Adivinanza: ¿qué palabra es?", "Pista uno: es un animal.", "Pista dos: tiene orejas largas.", "Pista tres: hace iii-aaa.", "¡El *burro*! Fuerte en el medio."]},
 {"t": "vof", "afirmacion": "PERO y PERRO se escriben igual", "emoji": "🐶", "verdadero": False, "explicacion": "PERO suave, PERRO fuerte",
  "voz": ["¿Verdadero o falso? Pero y perro se escriben igual.", "Escuchá: pero… perro.", "¡*Falso*! Pero es suave. Perro es fuerte."]},
 {"t": "clasificar", "cajas": [{"cab": "R (suave)", "emoji": "🍐"}, {"cab": "RR (fuerte)", "emoji": "🐶"}], "fichas": [{"txt": "PERA", "caja": 0}, {"txt": "LORO", "caja": 0}, {"txt": "TORRE", "caja": 1}, {"txt": "GORRA", "caja": 1}],
  "voz": ["Separamos las palabras.", "Pera y loro suenan suave: una letra.", "Torre y gorra suenan fuerte: dos letras."]},
 {"t": "resumen", "items": [["RR", "fuerte entre vocales"], ["R", "suave entre vocales"], ["EJEMPLOS", "PERRO, TORRE"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Fuerte en el medio: *dos letras*.", "Suave en el medio: *una letra*.", "Como en *perro* y *torre*.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "Escribí en tu carpeta: BURRO", "segundos": 8, "respuesta": "BURRO, con RR", "emoji": "✏️", "titulo": "DICTADO", "sub": "con R y RR",
  "voz": ["Desafío: escribí en tu carpeta *burro*.", "¡Burro! Fuerte en el medio: dos letras.", "Hoy: *dictado*."]},
 {"t": "pasos", "titulo": "CÓMO DECIDO", "items": [{"txt": "¿Suena suave? → R", "emoji": "🍐"}, {"txt": "¿Fuerte al principio? → R", "emoji": "🐭"}, {"txt": "¿Fuerte en el medio? → RR", "emoji": "🐶"}],
  "voz": ["¿Cómo decide la detective?", "Si suena *suave*: una letra.", "Si es fuerte *al principio*: una letra.", "Si es fuerte *en el medio*: dos letras."]},
 {"t": "tipeo", "titulo": "DICTADO", "items": [{"p": "El animal que ladra", "r": "PERRO"}, {"p": "La flor con espinas", "r": "ROSA"}, {"p": "El pájaro que habla", "r": "LORO"}],
  "voz": ["Primera palabra: *perro*.", "Segunda palabra: *rosa*.", "Tercera palabra: *loro*."]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "GO_A", "r": "RR"}, {"p": "_ISA", "r": "R"}, {"p": "PE_A (fruta)", "r": "R"}],
  "voz": ["¡Ronda rápida de la detective!", "Gorra: *dos letras*.", "Risa: *una letra*.", "Pera: *una letra*."]},
 {"t": "corrige", "titulo": "LA DETECTIVE CORRIGE", "cambios": [{"antes": "RRISA", "despues": "RISA", "motivo": "al principio, una R"}, {"antes": "TORE", "despues": "TORRE", "motivo": "fuerte en el medio"}],
  "voz": ["¡Encontramos errores en el dictado!", "Risa: al principio, *una sola letra*.", "Torre: fuerte en el medio, *dos letras*."]},
 {"t": "resumen", "items": [["SUAVE", "una R"], ["FUERTE AL PRINCIPIO", "una R"], ["FUERTE EN EL MEDIO", "RR"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Suave*: una letra.", "Fuerte *al principio*: una letra.", "Fuerte *en el medio*: dos letras.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m11-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 11 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
