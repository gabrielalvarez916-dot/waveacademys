# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 6 · Mezclar y separar: las 4 clases animadas.
Metáfora: la cocina de la abuela. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-nat1-m6-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0'
TEMA = 6
TIT = {1: 'Mezclas de sólidos', 2: 'Mezclas con agua', 3: 'Colar y filtrar', 4: 'Qué se disuelve y qué no'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍲", "lineas": ["Sofi cocina con la abuela.", "Se le cae el arroz en los porotos.", "¡Quedó todo mezclado!"], "titulo": "MEZCLAS", "sub": "de sólidos",
  "voz": ["Sofi cocina con la *abuela*.", "Se le cae el arroz en los porotos.", "¡Quedó todo *mezclado*!", "Hoy: *mezclas de sólidos*."]},
 {"t": "antesdespues", "antes": {"cab": "SEPARADOS", "emoji": "🍚", "texto": "Arroz y porotos"}, "despues": {"cab": "MEZCLADOS", "emoji": "🥣", "texto": "¡Una mezcla!"},
  "voz": ["Antes, el arroz y los porotos estaban *separados*.", "Ahora están juntos: es una *mezcla*."]},
 {"t": "zoom", "niveles": [{"emoji": "🥣", "txt": "LA MEZCLA"}, {"emoji": "🔍", "txt": "DE CERCA"}, {"emoji": "🫘", "txt": "SE VEN LOS GRANOS"}],
  "voz": ["Miramos la *mezcla*.", "Nos acercamos.", "¡Se ven los granos! Los podemos *separar con la mano*."]},
 {"t": "pregunta", "pregunta": "¿Cómo separás botones de fideos?", "opciones": ["CON LA MANO", "CON AGUA", "SOPLANDO"], "correcta": 0,
  "voz": ["Ahora vos. Hay botones y fideos juntos.", "¿Cómo los separás?", "¡*Con la mano*!"]},
 {"t": "consejo", "titulo": "MIRÁ LOS TAMAÑOS", "texto": "Si se ven distintos, se separan", "emoji": "👀",
  "voz": ["Truco: si se ven *distintos*, se pueden separar."]},
 {"t": "resumen", "items": [["MEZCLA", "cosas juntas"], ["SÓLIDOS", "arroz, porotos"], ["SEPARAR", "con la mano"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *mezcla* son cosas juntas.", "Arroz y porotos son *sólidos*.", "Los separamos *con la mano*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¡Puse arena en un vaso con agua!"}, {"yo": True, "txt": "¿Y QUÉ PASÓ?"}, {"yo": False, "txt": "¡Se fue al fondo!"}], "titulo": "MEZCLAS", "sub": "con agua",
  "voz": ["Tomi le escribe a Sofi.", "¡Puse arena en un vaso con agua!", "La arena se fue al *fondo*.", "Hoy: *mezclas con agua*."]},
 {"t": "experimento", "titulo": "¿QUÉ PASA EN EL AGUA?", "variable": "LO QUE PONEMOS", "a": {"cab": "AGUA Y ARENA", "emojis": ["🥛", "🏖️"], "txt": "Ponemos arena", "res": "SE VA AL FONDO"}, "b": {"cab": "AGUA Y ACEITE", "emojis": ["🥛", "🫒"], "txt": "Ponemos aceite", "res": "FLOTA ARRIBA"},
  "voz": ["En un vaso ponemos *arena*.", "En otro vaso ponemos *aceite*.", "¡La arena baja y el aceite *flota*!"]},
 {"t": "matriz", "titulo": "AGUA Y…", "celdas": [{"cab": "🪨 PIEDRA", "txt": "AL FONDO"}, {"cab": "🍾 CORCHO", "txt": "FLOTA"}, {"cab": "🟤 TIERRA", "txt": "BARRO"}, {"cab": "🍹 JUGO", "txt": "SE PINTA"}],
  "voz": ["Probamos con más cosas.", "La *piedra* se va al fondo.", "El *corcho* flota.", "La *tierra* hace barro.", "El *jugo en polvo* pinta el agua."]},
 {"t": "pregunta", "pregunta": "¿Qué hace el corcho en el agua?", "opciones": ["SE HUNDE", "FLOTA", "DESAPARECE"], "correcta": 1,
  "voz": ["Ahora vos. El corcho es liviano.", "¿Qué hace en el agua?", "¡*Flota*!"]},
 {"t": "consejo", "titulo": "CON UN ADULTO", "texto": "Las pruebas, siempre acompañado", "emoji": "🧑‍🔬",
  "voz": ["Truco: hacé las pruebas *con un adulto*."]},
 {"t": "resumen", "items": [["AL FONDO", "arena, piedra"], ["FLOTA", "aceite, corcho"], ["SE PINTA", "jugo en polvo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Algunas cosas van *al fondo*.", "Otras *flotan*.", "Y otras *pintan* el agua.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Cómo saca la abuela los fideos del agua?", "segundos": 6, "respuesta": "¡CON UN COLADOR!", "emoji": "🍝", "titulo": "COLAR", "sub": "y filtrar",
  "voz": ["Desafío: ¿cómo saca la abuela los fideos del agua?", "¡Con un *colador*!", "Hoy: *colar y filtrar*."]},
 {"t": "flujo", "titulo": "CÓMO SE CUELA", "items": ["PONGO EL COLADOR", "VUELCO LA OLLA", "PASA EL AGUA", "QUEDAN LOS FIDEOS"],
  "voz": ["Primero, *pongo* el colador.", "Un adulto *vuelca* la olla.", "El agua *pasa* por los agujeros.", "¡Y quedan los *fideos*!"]},
 {"t": "comparar", "a": {"cab": "COLADOR", "texto": "AGUJEROS GRANDES", "emoji": "🥄"}, "b": {"cab": "FILTRO", "texto": "AGUJERITOS CHIQUITOS", "emoji": "☕"}, "signo": "vs",
  "voz": ["El *colador* tiene agujeros grandes.", "El *filtro* tiene agujeritos chiquitos.", "¡El filtro atrapa cosas muy chiquitas!"]},
 {"t": "pregunta", "pregunta": "¿Qué usás para el agua con tierra?", "opciones": ["COLADOR", "FILTRO", "TENEDOR"], "correcta": 1,
  "voz": ["Ahora vos. La tierra es muy chiquita.", "¿Qué usás para separarla?", "¡Un *filtro*!"]},
 {"t": "consejo", "titulo": "CUIDADO, QUEMA", "texto": "El agua caliente la cuela un adulto", "emoji": "🔥",
  "voz": ["Truco: el agua caliente la cuela *un adulto*."]},
 {"t": "resumen", "items": [["COLADOR", "agujeros grandes"], ["FILTRO", "agujeritos chiquitos"], ["ELEGIR", "según el tamaño"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *colador*, para cosas grandes.", "El *filtro*, para cosas chiquitas.", "Elegimos según el *tamaño*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡DESAPARECIÓ EL AZÚCAR!", "bajada": "Pero el agua quedó dulce", "emoji": "🍬", "titulo": "SE DISUELVE", "sub": "o no se disuelve",
  "voz": ["¡Último momento! Desapareció el *azúcar*.", "Pero el agua quedó *dulce*.", "Hoy: *qué se disuelve y qué no*."]},
 {"t": "experimento", "titulo": "¿SE DISUELVE?", "variable": "LO QUE PONEMOS", "a": {"cab": "AGUA Y AZÚCAR", "emojis": ["🥛", "🍬"], "txt": "Revolvemos", "res": "YA NO SE VE"}, "b": {"cab": "AGUA Y ARENA", "emojis": ["🥛", "🏖️"], "txt": "Revolvemos", "res": "SIGUE AHÍ"},
  "voz": ["En un vaso ponemos *azúcar*.", "En otro vaso ponemos *arena*.", "¡El azúcar se *disolvió*, la arena no!"]},
 {"t": "linea", "titulo": "EL AZÚCAR EN EL AGUA", "eventos": [{"fecha": "1", "txt": "PONGO AZÚCAR", "emoji": "🥄"}, {"fecha": "2", "txt": "REVUELVO", "emoji": "🌀"}, {"fecha": "3", "txt": "YA NO SE VE", "emoji": "✨"}],
  "voz": ["Primero, *pongo* el azúcar.", "Después, *revuelvo*.", "¡Ya no se ve, pero sigue ahí!"]},
 {"t": "clasificar", "cajas": [{"cab": "SE DISUELVE", "emoji": "✨"}, {"cab": "NO SE DISUELVE", "emoji": "🪨"}], "fichas": [{"txt": "SAL", "caja": 0}, {"txt": "ARENA", "caja": 1}, {"txt": "AZÚCAR", "caja": 0}, {"txt": "BOTÓN", "caja": 1}],
  "voz": ["Separamos en dos cajas.", "Los que *se disuelven*.", "Y los que *no se disuelven*."]},
 {"t": "pregunta", "pregunta": "¿Qué se disuelve en el agua?", "opciones": ["PIEDRA", "SAL", "BOTÓN"], "correcta": 1,
  "voz": ["Ahora vos. Piedra, sal, botón.", "¿Cuál se disuelve?", "¡La *sal*!"]},
 {"t": "resumen", "items": [["SE DISUELVE", "azúcar, sal"], ["NO SE DISUELVE", "arena, aceite"], ["REVOLVER", "ayuda"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El azúcar y la sal *se disuelven*.", "La arena *no se disuelve*.", "*Revolver* ayuda.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Naturales 1", "titulo": TIT[n], "sub": f"Ciencias Naturales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
