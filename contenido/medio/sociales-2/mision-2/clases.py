# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 2 · Artesanía e industria: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (investiga cómo se hacen los alfajores).
Genera tools/medio/clase/lecciones/medio-soc2-m2-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'c2488d48-cfd5-40eb-8fd5-6904e733dd40', 2: 'b34afa42-a2b7-4e47-b84e-5016c3b6f568', 3: '988519b4-33a5-4caa-8c38-3027a464c0de', 4: '8e033fee-b026-4515-980b-48977bab2714'}
TIT = {1: 'Hacer un alfajor a mano', 2: 'Hacer miles de alfajores en una fábrica', 3: 'Herramientas y máquinas', 4: 'El mismo producto en distintos lugares'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
LOLA = {"nombre": "Lola", "emoji": "👧🎤"}

N1 = [
 {"t": "historia", "personaje": LOLA, "lugar": "🏠", "lineas": ["Lola visita a Doña Elsa.", "Hace alfajores en su cocina.", "¡Todo a mano!"], "titulo": "UN ALFAJOR", "sub": "a mano",
  "voz": ["Lola visita a *Doña Elsa*.", "Hace alfajores en su *cocina*.", "¡Todo a *mano*!", "Hoy: *un alfajor a mano*."]},
 {"t": "zoom", "niveles": [{"emoji": "🏠", "txt": "LA COCINA"}, {"emoji": "🙌", "txt": "LAS MANOS DE DOÑA ELSA"}, {"emoji": "🍪", "txt": "¡UNA TAPITA DE ALFAJOR!"}],
  "voz": ["Miramos la *cocina*.", "Más cerca: las *manos* de Doña Elsa.", "¡Una *tapita* de alfajor!"]},
 {"t": "transforma", "titulo": "LOS PASOS", "pasos": [{"txt": "MASA 🥣", "nota": "amasa"}, {"txt": "TAPITAS 🍪", "nota": "corta y hornea"}, {"txt": "ALFAJOR 😋", "nota": "¡con dulce de leche!"}],
  "voz": ["Primero, la *masa*.", "Después, corta y hornea las *tapitas*.", "¡Le pone *dulce de leche*: un alfajor!"]},
 {"t": "vof", "afirmacion": "Doña Elsa hace miles de alfajores por día", "emoji": "🍪", "verdadero": False, "explicacion": "A mano se hacen pocos",
  "voz": ["¿Verdadero o falso? Hace miles por día.", "Pensá: lo hace a mano…", "¡*Falso*! A mano se hacen *pocos*."]},
 {"t": "consejo", "titulo": "MIRÁ LAS MANOS", "texto": "Hecho a mano: artesanal", "emoji": "🙌",
  "voz": ["Truco: si se hace a mano, es *artesanal*."]},
 {"t": "resumen", "items": [["ARTESANAL", "hecho a mano"], ["POCOS", "de a poco"], ["HERRAMIENTAS", "simples"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Artesanal* es hecho a mano.", "Se hacen *pocos*, de a poco.", "Con *herramientas* simples.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "REPORTAJE", "titular": "¡Lola entra a una fábrica de alfajores!", "bajada": "Hacen miles por día", "emoji": "🏭", "titulo": "MILES", "sub": "en una fábrica",
  "voz": ["¡Noticia: Lola entra a una *fábrica* de alfajores!", "¡Hacen *miles* por día!", "Hoy: *la industria*."]},
 {"t": "escala", "titulo": "¿CUÁNTOS POR DÍA?", "items": [{"txt": "A MANO", "emoji": "🙌", "valor": 1}, {"txt": "TALLER CHICO", "emoji": "🏠", "valor": 4}, {"txt": "FÁBRICA", "emoji": "🏭", "valor": 10}],
  "voz": ["*A mano*: pocos alfajores.", "En un *taller* chico: algunos más.", "En la *fábrica*: ¡miles!"]},
 {"t": "versus", "titulo": "MANO O FÁBRICA", "a": {"txt": "A MANO", "emoji": "🙌", "datos": ["pocos", "distintos"]}, "b": {"txt": "FÁBRICA", "emoji": "🏭", "datos": ["miles", "iguales"]}, "gana": "empate", "veredicto": "¡Los dos son trabajo!",
  "voz": ["Comparamos dos formas de hacer.", "*A mano*: pocos y distintos.", "En la *fábrica*: miles e iguales.", "¡Los dos son *trabajo*!"]},
 {"t": "pregunta", "pregunta": "¿En la fábrica trabajan personas?", "opciones": ["SÍ, MUCHAS", "NO, NINGUNA"], "correcta": 0,
  "voz": ["Ahora vos: ¿en la fábrica trabajan personas?", "Pensá en las máquinas.", "¡*Sí*! Muchas personas."]},
 {"t": "consejo", "titulo": "MIRÁ CUÁNTOS", "texto": "Muchos e iguales: industria", "emoji": "🔢",
  "voz": ["Truco: muchos e iguales, es *industria*."]},
 {"t": "resumen", "items": [["INDUSTRIA", "fábrica con máquinas"], ["MILES", "muchos productos"], ["IGUALES", "todos parecidos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *industria* usa máquinas.", "Hace *miles* de productos.", "Todos *iguales*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué diferencia hay entre un palote y una batidora?", "segundos": 8, "respuesta": "¡La batidora tiene motor!", "emoji": "⚙️", "titulo": "HERRAMIENTAS", "sub": "y máquinas",
  "voz": ["Desafío: ¿palote o *batidora*?", "¡La batidora tiene *motor*!", "Hoy: *herramientas y máquinas*."]},
 {"t": "pistas", "problema": "¿Qué es?", "pistas": ["Tiene motor", "Bate los huevos", "Va enchufada"], "respuesta": "¡LA BATIDORA! 🌀",
  "voz": ["Adivinanza: ¿qué es?", "Pista uno: tiene motor.", "Pista dos: bate los huevos.", "Pista tres: va enchufada.", "¡La *batidora*! Es una máquina."]},
 {"t": "unir", "titulo": "¿HERRAMIENTA O MÁQUINA?", "pares": [["PALOTE", "herramienta"], ["BATIDORA", "máquina"], ["CUCHILLO", "herramienta"]], "mezclar": True,
  "voz": ["Unimos cada objeto.", "El palote: *herramienta*.", "La batidora: *máquina*.", "El cuchillo: *herramienta*."]},
 {"t": "pregunta", "pregunta": "¿Qué es más rápido?", "opciones": ["LA MÁQUINA", "LA MANO"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué es más rápido?", "Pensá en el motor.", "¡La *máquina*!"]},
 {"t": "consejo", "titulo": "¿TIENE MOTOR?", "texto": "Con motor: máquina", "emoji": "🔌",
  "voz": ["Truco: con *motor*, es máquina."]},
 {"t": "resumen", "items": [["HERRAMIENTA", "se usa a mano"], ["MÁQUINA", "tiene motor"], ["RÁPIDO", "la máquina"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *herramienta* se usa a mano.", "La *máquina* tiene motor.", "La máquina es más *rápida*.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tío Beto", "emoji": "👨"}, "mensajes": [{"yo": False, "txt": "¡Te traje alfajores de mi pueblo! 🍪"}, {"yo": True, "txt": "¡Son distintos a los de acá!"}], "titulo": "EL MISMO PRODUCTO", "sub": "en distintos lugares",
  "voz": ["El tío escribe: ¡te traje alfajores de mi *pueblo*!", "Lola responde: ¡son *distintos*!", "Hoy: *el mismo producto en distintos lugares*."]},
 {"t": "matriz", "titulo": "ALFAJORES", "celdas": [{"cab": "DE MAICENA 🥥", "txt": "con coco"}, {"cab": "DE CHOCOLATE 🍫", "txt": "bañado"}, {"cab": "CON MERENGUE ☁️", "txt": "blanco y dulce"}],
  "voz": ["Hay alfajores de muchos tipos.", "*De maicena*, con coco.", "*De chocolate*, bañados.", "*Con merengue*, blanco y dulce."]},
 {"t": "memoria", "titulo": "LUGARES", "items": ["PUEBLO", "CIUDAD", "FAMILIA", "FÁBRICA"], "falta": 3,
  "voz": ["Mirá las palabras.", "Se tapan… ¡y una desapareció!", "¡Faltaba *fábrica*!"]},
 {"t": "pregunta", "pregunta": "En el pueblo, ¿quién hace los alfajores?", "opciones": ["UNA FAMILIA", "UNA CINTA"], "correcta": 0,
  "voz": ["Ahora vos: ¿quién los hace en el pueblo?", "Pensá: a mano.", "¡Una *familia*!"]},
 {"t": "consejo", "titulo": "CADA LUGAR", "texto": "Cada lugar tiene su receta", "emoji": "📍",
  "voz": ["Truco: cada lugar tiene su *receta*."]},
 {"t": "resumen", "items": [["PUEBLO", "familia y a mano"], ["CIUDAD", "fábrica y máquinas"], ["DISTINTOS", "cada uno con su receta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En el *pueblo*, una familia, a mano.", "En la *ciudad*, una fábrica.", "Cada lugar tiene su *receta*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc2-m2-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Sociales 2", "titulo": TIT[n], "sub": f"Ciencias Sociales 2 · Misión 2 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
