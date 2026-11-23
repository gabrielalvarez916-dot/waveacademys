# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 12 · Las letras que faltan: las 4 clases animadas.
Vía fonológica: la VOZ dice sonidos y palabras ancla («como en yoyo», «la que no suena»), nunca nombres de letras.
Metáfora: el álbum del abecedario de Sofi. Genera tools/medio/clase/lecciones/medio-leng1-m12-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '846e1a8d-044a-4abd-a795-1b3c625403fc', 2: 'be82999d-330e-46ad-b510-797de78d8084', 3: '62e19cf0-e9ff-430d-8862-3101bd153d35', 4: '95cf7e47-5aac-4b9c-831f-2221e6347363'}
TIT = {1: 'Conocer la Y y la Z', 2: 'Conocer la H y la Q', 3: 'Conocer la K y la X', 4: 'Leer y escribir palabras con todas las letras'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📒", "lineas": ["Sofi tiene un álbum de letras.", "¡Le faltan seis!", "Hoy busca dos."], "titulo": "Y · Z", "sub": "letras nuevas",
  "voz": ["Sofi tiene un *álbum* de letras.", "¡Le faltan seis figuritas!", "Hoy busca dos.", "Hoy: *dos letras nuevas*."]},
 {"t": "silabas", "palabra": "YOYO", "silabas": ["YO", "YO"], "tonica": 0, "tipo": "grave",
  "voz": ["Escuchá: yo… yo.", "Esta letra nueva suena como en *yoyo*.", "Y como en *yema*: ya, ye, yo."]},
 {"t": "silabas", "palabra": "ZAPATO", "silabas": ["ZA", "PA", "TO"], "tonica": 1, "tipo": "grave",
  "voz": ["Escuchá: za… pa… to.", "Esta otra suena sss, como en *zapato*.", "Za, zo, zu."]},
 {"t": "memoria", "titulo": "PALABRAS NUEVAS", "items": ["YOYO", "YEMA", "ZAPATO", "ZORRO"], "falta": 3,
  "voz": ["Mirá estas palabras.", "Se tapan… ¡y una desapareció!", "¡Faltaba *zorro*!"]},
 {"t": "quiz4", "pregunta": "¿Cuál empieza como ZAPATO?", "opciones": ["YOYO", "ZORRO", "PATO", "MESA"], "correcta": 1,
  "voz": ["¿Cuál empieza igual que zapato?", "Mirá la primera letra.", "¡*Zorro*!"]},
 {"t": "resumen", "items": [["YOYO", "ya, ye, yo"], ["ZAPATO", "za, zo, zu"], ["¡DOS MÁS!", "para el álbum"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La letra de *yoyo*: ya, ye, yo.", "La letra de *zapato*: za, zo, zu.", "¡Dos figuritas más para el álbum!", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "MISTERIO", "titular": "¡Una letra que no suena!", "bajada": "Sofi la encontró en HUEVO", "emoji": "🥚", "titulo": "H · Q", "sub": "letras nuevas",
  "voz": ["¡Misterio: una letra que *no suena*!", "Sofi la encontró en *huevo*.", "Hoy: *dos letras nuevas*."]},
 {"t": "definicion", "palabra": "La letra callada", "texto": "La H se escribe pero no suena", "emoji": "🤫",
  "voz": ["En *huevo*, *hada* y *hoja* hay una letra callada.", "Se escribe, pero no se escucha."]},
 {"t": "vof", "afirmacion": "En HUEVO, la primera letra suena", "emoji": "🥚", "verdadero": False, "explicacion": "La H no suena",
  "voz": ["¿Verdadero o falso? En huevo, la primera letra suena.", "Escuchá: hue… vo.", "¡*Falso*! Es la letra callada."]},
 {"t": "definicion", "palabra": "Siempre con U", "texto": "QUE, QUI: la U no suena", "emoji": "🧀",
  "voz": ["En *queso* y *quince* hay otra letra nueva.", "Siempre va con una amiga que no suena: que, qui."]},
 {"t": "completa", "antes": "", "despues": "UESO", "opciones": ["Q", "H"], "correcta": 0,
  "voz": ["Completá: …ueso.", "¿Cuál va en queso?", "¡La de *queso*! Que, qui."]},
 {"t": "resumen", "items": [["HUEVO", "la letra callada"], ["QUESO", "que, qui"], ["¡DOS MÁS!", "para el álbum"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La de *huevo* no suena.", "La de *queso*: que, qui.", "¡Dos figuritas más para el álbum!", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué fruta es verde por dentro y peluda por fuera?", "segundos": 8, "respuesta": "¡El KIWI!", "emoji": "🥝", "titulo": "K · X", "sub": "letras nuevas",
  "voz": ["Desafío: ¿qué fruta es verde por dentro?", "¡El *kiwi*!", "Hoy: *las dos últimas letras*."]},
 {"t": "pistas", "problema": "¿Qué animal es?", "pistas": ["Vive en los árboles", "Es gris y peludo", "Empieza como KIWI"], "respuesta": "KOALA 🐨",
  "voz": ["Adivinanza: ¿qué animal es?", "Pista uno: vive en los árboles.", "Pista dos: es gris y peludo.", "Pista tres: empieza como *kiwi*.", "¡El *koala*!"]},
 {"t": "silabas", "palabra": "TAXI", "silabas": ["TA", "XI"], "tonica": 0, "tipo": "grave",
  "voz": ["Escuchá: ta… xi.", "Esta letra suena *ks*, dos sonidos juntos.", "Como en *taxi* y *examen*."]},
 {"t": "unir", "titulo": "¿CUÁL VA?", "pares": [["KIWI", "K"], ["TAXI", "X"], ["KOALA", "K"]],
  "voz": ["Unimos cada palabra con su letra.", "Kiwi: la de *kiwi*.", "Taxi: la que suena *ks*.", "Koala: la de *kiwi*."]},
 {"t": "consejo", "titulo": "POCAS PALABRAS", "texto": "Con K y X hay pocas palabras", "emoji": "🔎",
  "voz": ["Truco: con estas dos letras hay *muy pocas* palabras."]},
 {"t": "resumen", "items": [["KIWI", "ka, ki, ko"], ["TAXI", "suena ks"], ["¡COMPLETO!", "el álbum"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La de *kiwi*: suena como en casa.", "La de *taxi*: suena ks.", "¡El álbum está *completo*!", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Completaste el álbum? 📒"}, {"yo": True, "txt": "¡Sí! ¡Las 27 letras!"}], "titulo": "LEER", "sub": "y escribir",
  "voz": ["Tomi pregunta: ¿completaste el álbum?", "Sofi responde: ¡sí, las 27 letras!", "Hoy: *leer y escribir con todas*."]},
 {"t": "tipeo", "titulo": "LEEMOS", "items": [{"p": "HE · LA · DO", "r": "HELADO"}, {"p": "ZO · RRO", "r": "ZORRO"}, {"p": "QUE · SO", "r": "QUESO"}],
  "voz": ["He… la… do: *helado*.", "Zo… rro: *zorro*.", "Que… so: *queso*."]},
 {"t": "escape", "titulo": "LA PUERTA DEL ÁLBUM", "candados": [{"p": "_ADA", "r": "H"}, {"p": "_APATO", "r": "Z"}, {"p": "_IWI", "r": "K"}],
  "voz": ["¡Para cerrar el álbum, abrimos los candados!", "Hada: la letra *callada*.", "Zapato: la que suena *sss*.", "Kiwi: la de *kiwi*.", "¡Escapamos!"]},
 {"t": "errores", "items": [{"mal": "QESO", "bien": "QUESO"}, {"mal": "UEVO", "bien": "HUEVO"}],
  "voz": ["Cuidado con estos errores.", "Queso lleva su *amiga* que no suena.", "Huevo lleva la letra *callada*."]},
 {"t": "consejo", "titulo": "LEÉ DESPACIO", "texto": "Juntá las sílabas de a una", "emoji": "🐢",
  "voz": ["Truco: juntá las sílabas *de a una*."]},
 {"t": "resumen", "items": [["YOYO · ZAPATO", "dos letras"], ["HUEVO · QUESO", "dos más"], ["KIWI · TAXI", "¡y las últimas!"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las de *yoyo* y *zapato*.", "Las de *huevo* y *queso*.", "¡Y las de *kiwi* y *taxi*!", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m12-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 12 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
