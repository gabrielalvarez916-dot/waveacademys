# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 9 · Letras R, G y J: las 4 clases animadas.
Metáfora: la función del circo. Regla de primeros años, vía fonológica (la voz dice rrr, ga, jjj; nunca el nombre de la letra) y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-leng1-m9-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'eee219b3-9188-4e94-be06-223054ed5a57'
TIT = {1: 'Conocer la R', 2: 'Conocer la G y la J', 3: 'Leer palabras con R, G y J', 4: 'Escribir palabras con R, G y J'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🎪", "lineas": ["Sofi va al circo.", "Una rana salta en la pista.", "¡Y un ratón hace rrr!"], "titulo": "UN SONIDO", "sub": "de motor",
  "voz": ["Sofi va al *circo*.", "Una *rana* salta en la pista.", "¡Y un ratón hace *rrr*!", "Hoy: *el sonido de rana*."]},
 {"t": "silabas", "palabra": "RANA", "silabas": ["RA", "NA"], "tonica": 0, "tipo": "2 SÍLABAS",
  "voz": ["Esta palabra es *RANA*.", "La cortamos: ra, na.", "¡Empieza con *rrr*!"]},
 {"t": "zoom", "niveles": [{"emoji": "🐸", "txt": "RANA"}, {"emoji": "🔍", "txt": "RA · NA"}, {"emoji": "🚗", "txt": "RRR"}],
  "voz": ["Miramos *RANA* de cerca.", "Primero escuchamos *ra*.", "¡Suena como un motor: *rrr*!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra empieza como RANA?", "opciones": ["LANA", "ROSA", "PALA"], "correcta": 1,
  "voz": ["Ahora vos. Escuchá: rrr… ana.", "¿Qué palabra empieza igual?", "¡*ROSA*! rrr… osa."]},
 {"t": "consejo", "titulo": "EN EL MEDIO", "texto": "En PERA suena suave", "emoji": "🍐",
  "voz": ["Truco: en el medio suena *suave*: pera."]},
 {"t": "resumen", "items": [["RANA", "rrr fuerte"], ["SÍLABAS", "ra, re, ri, ro, ru"], ["PERA", "suave en el medio"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En rana suena *rrr*.", "*ra, re, ri, ro, ru*.", "En *pera* suena suave.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Qué viste en el circo?"}, {"yo": True, "txt": "UN GATO Y UNA JIRAFA"}, {"yo": False, "txt": "¡Qué lindo!"}], "titulo": "DOS SONIDOS", "sub": "nuevos",
  "voz": ["Tomi le escribe a Sofi.", "¿Qué viste en el circo?", "Sofi vio un *gato* y una *jirafa*.", "Hoy: *los sonidos de gato y jirafa*."]},
 {"t": "comparar", "a": {"cab": "GATO", "texto": "GA · GO · GU", "emoji": "🐱"}, "b": {"cab": "JIRAFA", "texto": "jjj", "emoji": "🦒"}, "signo": "y",
  "voz": ["En *gato*, *goma* y *gusano*: ga, go, gu.", "En *jirafa* y *jugo*: jjj.", "¡Dos sonidos nuevos!"]},
 {"t": "tabla", "titulo": "CON LAS VOCALES", "columnas": ["SÍLABA", "PALABRA"], "filas": [["JA", "JAMÓN"], ["JE", "TEJE"], ["JI", "JIRAFA"], ["JO", "OJO"], ["JU", "JUGO"]],
  "voz": ["Juntamos jjj con cada vocal.", "*ja*.", "*je*.", "*ji*.", "*jo*.", "*ju*."]},
 {"t": "silabas", "palabra": "JUGO", "silabas": ["JU", "GO"], "tonica": 0, "tipo": "2 SÍLABAS",
  "voz": ["Esta palabra es *JUGO*.", "La cortamos: ju, go.", "¡Tiene los *dos sonidos*!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra empieza como GATO?", "opciones": ["JUGO", "GOMA", "ROSA"], "correcta": 1,
  "voz": ["Ahora vos. Escuchá: ga… to.", "¿Qué palabra empieza parecido?", "¡*GOMA*! go… ma."]},
 {"t": "resumen", "items": [["GATO", "ga, go, gu"], ["JIRAFA", "jjj"], ["JUGO", "los dos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En gato: *ga, go, gu*.", "En jirafa: *jjj*.", "Y *jugo* tiene los dos.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Quién saca un conejo del gorro?", "segundos": 6, "respuesta": "¡EL MAGO!", "emoji": "🎩", "titulo": "LEER", "sub": "palabras del circo",
  "voz": ["Desafío: ¿quién saca un conejo del gorro?", "¡El *MAGO*!", "Hoy: *leer palabras del circo*."]},
 {"t": "texto", "oracion": "EL MAGO TOMA JUGO", "marcas": [{"desde": 1, "hasta": 1, "etiqueta": "MA-GO", "color": "sol"}, {"desde": 2, "hasta": 2, "etiqueta": "TO-MA", "color": "sol"}, {"desde": 3, "hasta": 3, "etiqueta": "JU-GO", "color": "sol"}],
  "voz": ["Leemos: el mago toma jugo.", "*MAGO*: ma, go.", "*TOMA*: to, ma.", "*JUGO*: ju, go."]},
 {"t": "venn", "a": "CON R", "b": "CON J", "itemsA": ["RANA", "PERA"], "itemsB": ["OJO", "JUGO"], "ambos": ["JIRAFA", "ROJO"],
  "voz": ["Separamos palabras por su sonido.", "*RANA* y *PERA* suenan con ra.", "*OJO* y *JUGO* suenan con jjj.", "¡*JIRAFA* y *ROJO* tienen los dos!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra forman LA y GO?", "opciones": ["GOLA", "LAGO", "MAGO"], "correcta": 1,
  "voz": ["Ahora vos. Juntá la y go.", "¿Qué palabra se forma?", "¡*LAGO*!"]},
 {"t": "consejo", "titulo": "LEÉ DOS VECES", "texto": "Primero despacio, después más rápido", "emoji": "🔁",
  "voz": ["Truco: leé *dos veces*, la segunda más rápido."]},
 {"t": "resumen", "items": [["SÍLABAS", "JI-RA-FA"], ["PALABRAS", "MAGO, RANA"], ["ORACIÓN", "EL MAGO TOMA JUGO"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Leemos *sílabas*.", "Formamos *palabras*.", "Y leemos *oraciones*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "DIARIO DEL CIRCO", "titular": "¡SOFI ARMA UN CARTEL!", "bajada": "Con palabras del circo", "emoji": "🎪", "titulo": "ESCRIBIR", "sub": "palabras del circo",
  "voz": ["¡Sofi arma un *cartel* para el circo!", "Usa palabras con sonidos nuevos.", "Hoy: *escribir palabras del circo*."]},
 {"t": "fichas", "fichas": ["M", "A", "G", "O"], "grande": "MAGO", "etiqueta": "MA · GO",
  "voz": ["Sofi dice despacio: mmm… a… go.", "Escribe y se forma *MAGO*.", "¡La primera palabra del cartel!"]},
 {"t": "orden", "titulo": "ARMAMOS ROJO", "items": [{"txt": "R", "emoji": "1️⃣"}, {"txt": "O", "emoji": "2️⃣"}, {"txt": "J", "emoji": "3️⃣"}, {"txt": "O", "emoji": "4️⃣"}], "relato": [2, 0, 3, 1],
  "voz": ["Las letras de ROJO se mezclaron.", "Las ponemos en *orden*.", "rrr… o… jjj… o: ¡*ROJO*!"]},
 {"t": "antesdespues", "antes": {"cab": "PALA", "emoji": "🪣", "texto": "La lengua quieta"}, "despues": {"cab": "PERA", "emoji": "🍐", "texto": "La lengua tiembla"},
  "voz": ["En *pala*, la lengua queda quieta.", "En *pera*, la lengua *tiembla*."]},
 {"t": "pregunta", "pregunta": "¿Qué letra falta? LO_O", "opciones": ["L", "R", "J"], "correcta": 1,
  "voz": ["Ahora vos. lll… o… hueco… o.", "¿Qué falta para decir LORO?", "¡Falta *ro*! LO-RO."]},
 {"t": "resumen", "items": [["ESCUCHAR", "MA-GO"], ["PALA O PERA", "la lengua tiembla"], ["REVISAR", "leer lo escrito"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Escuchamos* cada sonido.", "Sentimos si la *lengua tiembla*.", "Y *revisamos* leyendo.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m9-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": 9, "nivel": n}, "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 9 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
