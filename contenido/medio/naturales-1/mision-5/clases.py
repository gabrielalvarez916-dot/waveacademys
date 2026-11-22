# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 5 · Los objetos y sus materiales: las 4 clases animadas.
Metáfora: el taller del abuelo. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-nat1-m5-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0'
TEMA = 5
TIT = {1: 'Objetos y materiales que los forman', 2: 'Transparente, opaco y translúcido', 3: 'Flexible y rígido', 4: 'Elijo el material adecuado'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "reto", "texto": "¿De qué está hecha tu mesa?", "segundos": 6, "respuesta": "¡DE MADERA!", "emoji": "🪑", "titulo": "LOS MATERIALES", "sub": "de los objetos",
  "voz": ["Desafío: ¿de qué está hecha tu mesa?", "¡De *madera*!", "Hoy: *objetos y materiales*."]},
 {"t": "bloques", "titulo": "EN EL TALLER DEL ABUELO", "items": [{"cab": "🪑 MESA", "txt": "MADERA"}, {"cab": "🥛 VASO", "txt": "VIDRIO"}, {"cab": "🥄 CUCHARA", "txt": "METAL"}, {"cab": "🧴 BOTELLA", "txt": "PLÁSTICO"}],
  "voz": ["El abuelo tiene muchos *objetos*.", "La mesa es de *madera*.", "El vaso es de *vidrio*.", "La cuchara es de *metal*.", "La botella es de *plástico*."]},
 {"t": "zoom", "niveles": [{"emoji": "✏️", "txt": "UN LÁPIZ"}, {"emoji": "🪵", "txt": "MADERA"}, {"emoji": "⚫", "txt": "GRAFITO"}],
  "voz": ["Miramos un *lápiz*.", "Por fuera es de *madera*.", "¡Adentro tiene *grafito*! Dos materiales."]},
 {"t": "pregunta", "pregunta": "¿De qué es la cuchara?", "opciones": ["MADERA", "METAL", "TELA"], "correcta": 1,
  "voz": ["Ahora vos. La cuchara es fría y brilla.", "¿De qué material es?", "¡De *metal*!"]},
 {"t": "consejo", "titulo": "TOCÁ Y MIRÁ", "texto": "¿Frío, duro, liviano?", "emoji": "✋",
  "voz": ["Truco: *tocá* el objeto y te da pistas."]},
 {"t": "resumen", "items": [["OBJETO", "mesa, vaso"], ["MATERIAL", "madera, vidrio, metal"], ["VARIOS", "el lápiz"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los *objetos* están hechos de materiales.", "Madera, *vidrio*, metal, plástico.", "Algunos tienen *varios*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🔦", "lineas": ["Sofi juega con una linterna.", "Alumbra la ventana y la puerta.", "¡Por una pasa la luz!"], "titulo": "LA LUZ", "sub": "¿pasa o no pasa?",
  "voz": ["Sofi juega con una *linterna*.", "Alumbra la ventana y la puerta.", "¡Por una pasa la luz!", "Hoy: *transparente, opaco y translúcido*."]},
 {"t": "comparar", "a": {"cab": "TRANSPARENTE", "texto": "VIDRIO: SE VE", "emoji": "🪟"}, "b": {"cab": "OPACO", "texto": "MADERA: NO SE VE", "emoji": "🚪"}, "signo": "vs",
  "voz": ["Por el vidrio se ve: es *transparente*.", "Por la madera no se ve: es *opaca*.", "¡La luz pasa o no pasa!"]},
 {"t": "experimento", "titulo": "¿PASA LA LUZ?", "variable": "EL MATERIAL", "a": {"cab": "PAPEL DE CALCAR", "emojis": ["🔦", "📄"], "txt": "Papel finito", "res": "PASA UN POCO"}, "b": {"cab": "CARTÓN", "emojis": ["🔦", "📦"], "txt": "Cartón grueso", "res": "NO PASA NADA"},
  "voz": ["Sofi alumbra un *papel de calcar*.", "Después alumbra un *cartón*.", "Por el papel pasa un poco: es *translúcido*."]},
 {"t": "pregunta", "pregunta": "¿Cómo es el cartón?", "opciones": ["TRANSPARENTE", "OPACO", "TRANSLÚCIDO"], "correcta": 1,
  "voz": ["Ahora vos. Por el cartón no pasa la luz.", "¿Cómo es?", "¡*Opaco*!"]},
 {"t": "consejo", "titulo": "MIRÁ A TRAVÉS", "texto": "Poné el objeto frente a tus ojos", "emoji": "👀",
  "voz": ["Truco: poné el objeto frente a tus *ojos*."]},
 {"t": "resumen", "items": [["TRANSPARENTE", "se ve"], ["TRANSLÚCIDO", "pasa poca luz"], ["OPACO", "no pasa luz"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Transparente*: se ve a través.", "*Translúcido*: pasa poca luz.", "*Opaco*: no pasa nada.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¡Doblé mi regla y se rompió!"}, {"yo": True, "txt": "¿ERA DE MADERA?"}, {"yo": False, "txt": "Sí… ¿por qué?"}], "titulo": "FLEXIBLE", "sub": "y rígido",
  "voz": ["Tomi le escribe a Sofi.", "¡Doblé mi regla y se rompió!", "Sofi le pregunta si era de madera.", "Hoy: *flexible y rígido*."]},
 {"t": "antesdespues", "antes": {"cab": "LA DOBLO", "emoji": "➰", "texto": "Goma doblada"}, "despues": {"cab": "LA SUELTO", "emoji": "➖", "texto": "¡No se rompió!"},
  "voz": ["Doblamos una *goma*.", "La soltamos: ¡no se rompió! Es *flexible*."]},
 {"t": "experimento", "titulo": "¿SE DOBLA?", "variable": "EL MATERIAL", "a": {"cab": "REGLA DE PLÁSTICO FINO", "emojis": ["📏", "🤲"], "txt": "La doblo", "res": "SE DOBLA"}, "b": {"cab": "REGLA DE MADERA", "emojis": ["📏", "🤲"], "txt": "La doblo", "res": "NO SE DOBLA"},
  "voz": ["Probamos con una regla de *plástico fino*.", "Y con una regla de *madera*.", "¡La de madera es *rígida*: no se dobla!"]},
 {"t": "clasificar", "cajas": [{"cab": "FLEXIBLE", "emoji": "🧦"}, {"cab": "RÍGIDO", "emoji": "🧱"}], "fichas": [{"txt": "MEDIA", "caja": 0}, {"txt": "LADRILLO", "caja": 1}, {"txt": "PAPEL", "caja": 0}, {"txt": "PIEDRA", "caja": 1}],
  "voz": ["Separamos en dos cajas.", "Los que se doblan: *flexibles*.", "Los que no se doblan: *rígidos*."]},
 {"t": "pregunta", "pregunta": "¿Cuál es flexible?", "opciones": ["PIEDRA", "TELA", "LADRILLO"], "correcta": 1,
  "voz": ["Ahora vos. Piedra, tela, ladrillo.", "¿Cuál se dobla sin romperse?", "¡La *tela*!"]},
 {"t": "resumen", "items": [["FLEXIBLE", "se dobla"], ["RÍGIDO", "no se dobla"], ["PROBAR", "con cuidado"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Flexible*: se dobla sin romperse.", "*Rígido*: no se dobla.", "Probamos siempre con *cuidado*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡UN PARAGUAS DE PAPEL!", "bajada": "Se rompió con la primera lluvia", "emoji": "☔", "titulo": "ELIJO", "sub": "el material",
  "voz": ["¡Último momento! Un paraguas de *papel*.", "Se rompió con la primera lluvia.", "Hoy: *elegir el material adecuado*."]},
 {"t": "matriz", "titulo": "BIEN ELEGIDO", "celdas": [{"cab": "🪟 VENTANA", "txt": "VIDRIO: PARA VER"}, {"cab": "☂️ PARAGUAS", "txt": "PLÁSTICO: NO SE MOJA"}, {"cab": "⚽ PELOTA", "txt": "GOMA: PICA"}, {"cab": "🚪 PUERTA", "txt": "MADERA: FUERTE"}],
  "voz": ["Cada objeto tiene su *mejor* material.", "La ventana, de *vidrio*: para ver.", "El paraguas, de *plástico*: no se moja.", "La pelota, de *goma*: pica.", "La puerta, de *madera*: es fuerte."]},
 {"t": "flujo", "titulo": "CÓMO ELIJO", "items": ["¿PARA QUÉ SIRVE?", "¿QUÉ NECESITA?", "ELIJO", "PRUEBO"],
  "voz": ["Primero pienso: ¿*para qué* sirve?", "Después: ¿qué *necesita*?", "Ahora *elijo* el material.", "Y lo *pruebo*."]},
 {"t": "pregunta", "pregunta": "¿De qué hacés un vaso para ver el jugo?", "opciones": ["MADERA", "VIDRIO", "TELA"], "correcta": 1,
  "voz": ["Ahora vos. Querés ver el jugo.", "¿De qué material hacés el vaso?", "¡De *vidrio*, que es transparente!"]},
 {"t": "consejo", "titulo": "¿PARA QUÉ?", "texto": "Siempre empezá por esa pregunta", "emoji": "🤔",
  "voz": ["Truco: empezá siempre por *¿para qué sirve?*"]},
 {"t": "resumen", "items": [["PENSAR", "para qué sirve"], ["ELEGIR", "el adecuado"], ["PROBAR", "ver si sirve"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Pensamos *para qué* sirve.", "*Elegimos* el material adecuado.", "Y lo *probamos*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Naturales 1", "titulo": TIT[n], "sub": f"Ciencias Naturales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
