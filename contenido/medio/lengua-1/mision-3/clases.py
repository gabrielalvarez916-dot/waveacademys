# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 3 · Letras M y P: las 4 clases animadas.
Metáfora: la familia de Sofi (MAMÁ y PAPÁ). Regla de primeros años y de variedad del banco.
Genera tools/medio/clase/lecciones/medio-leng1-m3-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'f71fee4b-4cd6-425e-9b2d-06e34dde3b9a', 2: '707333ca-99be-4f80-b758-a4ecb3eb65c7', 3: '2006e2b7-0d9b-4abf-ad6e-1145da5fb15f', 4: '1481f210-5907-437f-be8a-0f9bcf6044ea'}
TIT = {1: 'Conocer la M y la P', 2: 'Leer sílabas con M y P', 3: 'Leer palabras con M y P', 4: 'Escribir palabras con M y P'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🏠", "lineas": ["Sofi escribe una carta.", "Es para su mamá y su papá.", "¡Usa dos letras nuevas!"], "titulo": "LA M Y LA P", "sub": "letras nuevas",
  "voz": ["Sofi escribe una *carta*.", "Es para su *mamá* y su *papá*.", "¡Usa dos letras nuevas!", "Hoy: *conocer la M y la P*."]},
 {"t": "comparar", "a": {"cab": "M", "texto": "de MAMÁ · mmm", "emoji": "👩"}, "b": {"cab": "P", "texto": "de PAPÁ · p", "emoji": "👨"}, "signo": "y",
  "voz": ["La *M* de mamá suena mmm.", "La *P* de papá suena p.", "¡Para las dos juntamos los labios!"]},
 {"t": "fichas", "fichas": ["M", "A", "M", "Á"], "grande": "MAMÁ", "etiqueta": "M · A · M · Á",
  "voz": ["Sofi escribe M, A, M, A.", "Las letras forman *MAMÁ*.", "¡Tiene dos M!"]},
 {"t": "definicion", "palabra": "CONSONANTE", "texto": "Necesita una vocal para sonar", "emoji": "🤝",
  "voz": ["La M y la P son *consonantes*.", "Necesitan una *vocal* para sonar."]},
 {"t": "pregunta", "pregunta": "¿Qué palabra empieza con P?", "opciones": ["MESA", "PATO", "OSO"], "correcta": 1,
  "voz": ["Ahora vos. Escuchá cada palabra.", "¿Cuál empieza con *P*?", "¡*PATO*! P de pato."]},
 {"t": "errores", "items": [{"mal": "Confundir la P con la B", "bien": "P de PAPÁ, B de BEBÉ"}],
  "voz": ["Ojo con este error.", "La *P* de papá no es la B de bebé."]},
 {"t": "resumen", "items": [["M", "de MAMÁ"], ["P", "de PAPÁ"], ["CONSONANTES", "necesitan vocales"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *M* de mamá.", "La *P* de papá.", "Son *consonantes*: necesitan vocales.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Cómo suenan juntas la M y la A?", "segundos": 6, "respuesta": "¡MA!", "emoji": "🔊", "titulo": "SÍLABAS", "sub": "con M y P",
  "voz": ["Desafío: ¿cómo suenan juntas la M y la A?", "¡*MA*!", "Hoy: *leer sílabas con M y P*."]},
 {"t": "silabas", "palabra": "MAMÁ", "silabas": ["MA", "MÁ"], "tonica": 1, "tipo": "2 SÍLABAS",
  "voz": ["Esta palabra es *MAMÁ*.", "La cortamos en pedacitos: MA, MÁ.", "¡Tiene *2 sílabas*!"]},
 {"t": "matriz", "titulo": "LA M CON LAS VOCALES", "celdas": [{"cab": "MA", "txt": "M + A"}, {"cab": "ME", "txt": "M + E"}, {"cab": "MI", "txt": "M + I"}, {"cab": "MO", "txt": "M + O"}],
  "voz": ["La M se junta con cada vocal.", "M con A: *MA*.", "M con E: *ME*.", "M con I: *MI*.", "M con O: *MO*. ¡Y MU!"]},
 {"t": "tabla", "titulo": "LA P CON LAS VOCALES", "columnas": ["SÍLABA", "SE LEE"], "filas": [["PA", "P + A"], ["PE", "P + E"], ["PI", "P + I"], ["PO", "P + O"], ["PU", "P + U"]],
  "voz": ["Ahora la P con cada vocal.", "*PA*.", "*PE*.", "*PI*.", "*PO*.", "*PU*."]},
 {"t": "pregunta", "pregunta": "¿Cómo se lee P con O?", "opciones": ["OP", "PO", "MO"], "correcta": 1,
  "voz": ["Ahora vos. Juntá la P y la O.", "¿Cómo se lee?", "¡*PO*!"]},
 {"t": "consejo", "titulo": "DE UN GOLPE", "texto": "Leé la consonante y la vocal juntas", "emoji": "⚡",
  "voz": ["Truco: leé las dos letras *de un golpe*."]},
 {"t": "resumen", "items": [["SÍLABA", "de un golpe"], ["CON M", "MA, ME, MI, MO, MU"], ["CON P", "PA, PE, PI, PO, PU"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *sílaba* se dice de un golpe.", "*MA, ME, MI, MO, MU*.", "*PA, PE, PI, PO, PU*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Papá", "emoji": "👨"}, "mensajes": [{"yo": False, "txt": "¿Leíste mi mensaje?"}, {"yo": True, "txt": "Dice MAPA"}, {"yo": False, "txt": "¡Muy bien, Sofi!"}], "titulo": "LEER", "sub": "palabras con M y P",
  "voz": ["Papá le escribe a Sofi.", "Le pregunta si leyó su mensaje.", "¡Sofi lee *MAPA*!", "Hoy: *leer palabras con M y P*."]},
 {"t": "silabas", "palabra": "PUMA", "silabas": ["PU", "MA"], "tonica": 0, "tipo": "2 SÍLABAS",
  "voz": ["Leemos esta palabra.", "Sílaba por sílaba: PU, MA.", "¡Todo junto: *PUMA*!"]},
 {"t": "bloques", "titulo": "PALABRAS DE LA FAMILIA", "items": [{"cab": "MAPA", "txt": "MA + PA"}, {"cab": "PIPA", "txt": "PI + PA"}, {"cab": "MIMO", "txt": "MI + MO"}],
  "voz": ["Leemos más palabras.", "MA y PA: *MAPA*.", "PI y PA: *PIPA*.", "MI y MO: *MIMO*."]},
 {"t": "antesdespues", "antes": {"cab": "DE A PEDACITOS", "emoji": "🧩", "texto": "PE · PE"}, "despues": {"cab": "TODO JUNTO", "emoji": "🗣️", "texto": "PEPE"},
  "voz": ["Primero leemos *de a pedacitos*: PE, PE.", "Después *todo junto*: ¡PEPE!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra forman MA y PA?", "opciones": ["PAMA", "MAPA", "PAPA"], "correcta": 1,
  "voz": ["Ahora vos. Juntá MA y PA.", "¿Qué palabra se forma?", "¡*MAPA*!"]},
 {"t": "resumen", "items": [["SÍLABAS", "MA + PA"], ["JUNTAR", "MAPA"], ["LEER", "todo junto"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Leemos las *sílabas*.", "Las *juntamos*.", "Y *leemos* todo junto.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "CARTA DE SOFI", "titular": "¡SOFI ESCRIBE SOLA!", "bajada": "Palabras con M y P", "emoji": "✉️", "titulo": "ESCRIBIR", "sub": "palabras con M y P",
  "voz": ["¡Noticia! Sofi escribe *sola*.", "Escribe palabras con M y P.", "Hoy: *escribir palabras con M y P*."]},
 {"t": "flujo", "titulo": "CÓMO ESCRIBIR", "items": [{"txt": "Digo la palabra", "emoji": "🗣️"}, {"txt": "Escribo cada sílaba", "emoji": "✍️"}, {"txt": "Leo y reviso", "emoji": "👀"}],
  "voz": ["Primero *digo* la palabra.", "Después *escribo* sílaba por sílaba.", "Al final *leo* y reviso."]},
 {"t": "orden", "titulo": "ARMAMOS PUMA", "items": [{"txt": "P", "emoji": "1️⃣"}, {"txt": "U", "emoji": "2️⃣"}, {"txt": "M", "emoji": "3️⃣"}, {"txt": "A", "emoji": "4️⃣"}], "relato": [2, 3, 0, 1],
  "voz": ["Las letras de PUMA se mezclaron.", "Las ponemos en *orden*.", "P, U, M, A: ¡*PUMA*!"]},
 {"t": "fichas", "fichas": ["M", "A", "P", "A"], "grande": "MAPA", "etiqueta": "¡NO FALTA NINGUNA!",
  "voz": ["Sofi escribe MA y después PA.", "Revisa: M, A, P, A: *MAPA*.", "¡No le falta ninguna letra!"]},
 {"t": "pregunta", "pregunta": "¿Qué letra falta? MA_A", "opciones": ["M", "P", "S"], "correcta": 1,
  "voz": ["Ahora vos. M, A, hueco, A.", "¿Qué letra falta?", "¡La *P*! MAPA."]},
 {"t": "resumen", "items": [["ESCUCHAR", "PU-MA"], ["ESCRIBIR", "sílaba por sílaba"], ["REVISAR", "leer lo escrito"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Escuchamos* la palabra.", "*Escribimos* sílaba por sílaba.", "Y *revisamos* leyendo.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m3-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 3 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
