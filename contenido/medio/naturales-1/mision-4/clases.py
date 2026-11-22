# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 4 · Quién vive dónde: las 4 clases animadas.
Metáfora: la excursión a la laguna. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-nat1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0'
TEMA = 4
TIT = {1: 'Ambientes de tierra, de agua y de aire', 2: 'Qué necesitan para vivir', 3: 'Un ambiente y sus habitantes', 4: 'Seres vivos y cosas no vivas'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡EXCURSIÓN A LA NATURALEZA!", "bajada": "¿Quién vive dónde?", "emoji": "🚌", "titulo": "LOS AMBIENTES", "sub": "tierra, agua y aire",
  "voz": ["¡Último momento! Nos vamos de *excursión*.", "Vamos a ver quién vive dónde.", "Hoy: *los ambientes*."]},
 {"t": "matriz", "titulo": "¿DÓNDE VIVEN?", "celdas": [{"cab": "🐄 VACA", "txt": "TIERRA"}, {"cab": "🐟 PEZ", "txt": "AGUA"}, {"cab": "🐦 PÁJARO", "txt": "AIRE"}, {"cab": "🐸 RANA", "txt": "AGUA Y TIERRA"}],
  "voz": ["Cada uno tiene su *ambiente*.", "La vaca vive en la *tierra*.", "El pez vive en el *agua*.", "El pájaro vuela por el *aire*.", "¡La rana vive en el agua *y* en la tierra!"]},
 {"t": "comparar", "a": {"cab": "TIERRA", "texto": "CAMPO, BOSQUE", "emoji": "🌳"}, "b": {"cab": "AGUA", "texto": "MAR, LAGUNA", "emoji": "🌊"}, "signo": "vs",
  "voz": ["Ambientes de *tierra*: el campo, el bosque.", "Ambientes de *agua*: el mar, la laguna.", "¡Cada ambiente tiene sus animales!"]},
 {"t": "pregunta", "pregunta": "¿Dónde vive la ballena?", "opciones": ["TIERRA", "AGUA", "ÁRBOL"], "correcta": 1,
  "voz": ["Ahora vos. La ballena es enorme y nada.", "¿Dónde vive?", "¡En el *agua*, en el mar!"]},
 {"t": "consejo", "titulo": "MIRÁ CÓMO SE MUEVE", "texto": "Nada: agua. Camina: tierra.", "emoji": "💡",
  "voz": ["Truco: fijate cómo se *mueve* el animal."]},
 {"t": "resumen", "items": [["TIERRA", "campo, bosque"], ["AGUA", "mar, laguna"], ["AIRE", "los que vuelan"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Hay ambientes de *tierra*.", "Hay ambientes de *agua*.", "Y los pájaros vuelan por el *aire*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🪴", "lineas": ["Sofi se fue de vacaciones.", "Nadie regó su planta.", "¡Al volver estaba seca!"], "titulo": "QUÉ NECESITAN", "sub": "para vivir",
  "voz": ["Sofi se fue de *vacaciones*.", "Nadie regó su planta.", "¡Al volver estaba *seca*!", "Hoy: *qué necesitan para vivir*."]},
 {"t": "causas", "causa": {"txt": "PARA VIVIR", "emoji": "💚"}, "items": ["AGUA", "ALIMENTO", "AIRE", "UN LUGAR"],
  "voz": ["¿Qué necesita un ser vivo?", "Necesita *agua*.", "Necesita *alimento*.", "Necesita *aire*.", "Y necesita *un lugar* para vivir."]},
 {"t": "antesdespues", "antes": {"cab": "SIN AGUA", "emoji": "🥀", "texto": "Seca"}, "despues": {"cab": "CON AGUA", "emoji": "🌷", "texto": "¡Verde otra vez!"},
  "voz": ["Sin agua, la planta se *secó*.", "Sofi la riega y se pone *verde*."]},
 {"t": "pregunta", "pregunta": "¿Qué necesitan todos los seres vivos?", "opciones": ["UNA PELOTA", "AGUA", "UN AUTO"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en plantas y animales.", "¿Qué necesitan todos?", "¡*Agua*!"]},
 {"t": "consejo", "titulo": "VOS TAMBIÉN", "texto": "Agua, comida, aire y casa", "emoji": "🧒",
  "voz": ["Truco: vos también necesitás *lo mismo*."]},
 {"t": "resumen", "items": [["AGUA", "todos la necesitan"], ["ALIMENTO Y AIRE", "para vivir"], ["LUGAR", "su ambiente"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Todos necesitan *agua*.", "También *alimento* y *aire*.", "Y un *lugar* para vivir.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Llegaste a la laguna?"}, {"yo": True, "txt": "¡SÍ! HAY PATOS Y RANAS"}, {"yo": False, "txt": "¿Y qué más?"}], "titulo": "LA LAGUNA", "sub": "y sus habitantes",
  "voz": ["Tomi le escribe a Sofi.", "¿Llegaste a la laguna?", "¡Sí! Hay patos y ranas.", "Hoy: *un ambiente y sus habitantes*."]},
 {"t": "partes", "emoji": "🏞️", "titulo": "LA LAGUNA", "partes": [{"txt": "PATO", "x": 0.4, "y": -0.3}, {"txt": "PEZ", "x": -0.2, "y": 0.4}, {"txt": "RANA", "x": 0.5, "y": 0.5}, {"txt": "JUNCOS", "x": -0.6, "y": -0.2}],
  "voz": ["Miramos la *laguna*.", "Nada un *pato*.", "Abajo del agua, un *pez*.", "En la orilla, una *rana*.", "Y crecen los *juncos*: ¡son plantas!"]},
 {"t": "venn", "a": "EN EL AGUA", "b": "EN LA ORILLA", "itemsA": ["PEZ"], "itemsB": ["JUNCO"], "ambos": ["RANA", "PATO"],
  "voz": ["¿Dónde está cada habitante?", "El *pez*, en el agua.", "El *junco*, en la orilla.", "¡La rana y el pato, en los *dos*!"]},
 {"t": "pregunta", "pregunta": "¿Cuál no es un habitante?", "opciones": ["PATO", "BARRO", "JUNCO"], "correcta": 1,
  "voz": ["Ahora vos. Pato, barro, junco.", "¿Cuál no es un ser vivo?", "¡El *barro*!"]},
 {"t": "consejo", "titulo": "PLANTAS TAMBIÉN", "texto": "Las plantas también son habitantes", "emoji": "🌾",
  "voz": ["Truco: las *plantas* también son habitantes."]},
 {"t": "resumen", "items": [["AMBIENTE", "la laguna"], ["HABITANTES", "pato, pez, rana, junco"], ["LUGAR", "agua u orilla"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La laguna es un *ambiente*.", "Tiene muchos *habitantes*.", "Cada uno en su *lugar*.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "¿Está viva una piedra?", "segundos": 6, "respuesta": "¡NO! NO CRECE", "emoji": "🪨", "titulo": "VIVO", "sub": "o no vivo",
  "voz": ["Desafío: ¿está viva una piedra?", "¡No! No nace ni *crece*.", "Hoy: *seres vivos y cosas no vivas*."]},
 {"t": "clasificar", "cajas": [{"cab": "VIVOS", "emoji": "💚"}, {"cab": "NO VIVOS", "emoji": "🪨"}], "fichas": [{"txt": "GATO", "caja": 0}, {"txt": "PIEDRA", "caja": 1}, {"txt": "ÁRBOL", "caja": 0}, {"txt": "PELOTA", "caja": 1}],
  "voz": ["Separamos en dos cajas.", "En una, los *seres vivos*.", "En la otra, las *cosas no vivas*."]},
 {"t": "comparar", "a": {"cab": "PERRO", "texto": "Nace y crece", "emoji": "🐶"}, "b": {"cab": "AUTO", "texto": "Se mueve, no crece", "emoji": "🚗"}, "signo": "vs",
  "voz": ["El perro nace y *crece*: está vivo.", "El auto se mueve, pero *no crece*.", "¡Moverse *no alcanza*!"]},
 {"t": "ciclo", "titulo": "LA VIDA DE UNA PLANTA", "items": ["NACE", "CRECE", "DA SEMILLAS", "SE MUERE"],
  "voz": ["Los seres vivos tienen un *ciclo*.", "La planta *nace*.", "*Crece*.", "Da *semillas*.", "Y un día *se muere*."]},
 {"t": "pregunta", "pregunta": "¿Cuál es un ser vivo?", "opciones": ["SILLA", "ÁRBOL", "ROCA"], "correcta": 1,
  "voz": ["Ahora vos. Silla, árbol, roca.", "¿Cuál nace y crece?", "¡El *árbol*!"]},
 {"t": "resumen", "items": [["VIVOS", "nacen y crecen"], ["NO VIVOS", "no crecen"], ["OJO", "moverse no alcanza"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los seres vivos *nacen y crecen*.", "Las cosas no vivas *no crecen*.", "Y moverse *no alcanza*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Naturales 1", "titulo": TIT[n], "sub": f"Ciencias Naturales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
