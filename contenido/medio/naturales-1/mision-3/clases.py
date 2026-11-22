# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 3 · Plantas por fuera: las 4 clases animadas.
Metáfora: el paseo por la plaza. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-nat1-m3-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0'
TEMA = 3
TIT = {1: 'Las hojas, formas y bordes', 2: 'Árboles, arbustos y hierbas', 3: 'Dónde crecen mejor', 4: 'Mi cuaderno de campo'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🌳", "lineas": ["Sofi pasea por la plaza.", "Junta hojas del suelo.", "¡Ninguna es igual a otra!"], "titulo": "LAS HOJAS", "sub": "formas y bordes",
  "voz": ["Sofi pasea por la *plaza*.", "Junta hojas del suelo.", "¡Ninguna es igual a otra!", "Hoy: *formas y bordes de las hojas*."]},
 {"t": "zoom", "niveles": [{"emoji": "🌳", "txt": "UN ÁRBOL"}, {"emoji": "🍃", "txt": "UNA HOJA"}, {"emoji": "🔍", "txt": "SU BORDE"}],
  "voz": ["Miramos un *árbol*.", "Nos acercamos a una *hoja*.", "¡Y miramos su *borde*!"]},
 {"t": "comparar", "a": {"cab": "BORDE LISO", "texto": "Como un limón", "emoji": "🍋"}, "b": {"cab": "CON DIENTES", "texto": "Como una sierra", "emoji": "🌹"}, "signo": "vs",
  "voz": ["La hoja del limonero tiene borde *liso*.", "La hoja de la rosa tiene *dientes*.", "¡Pasá el dedo y sentilo!"]},
 {"t": "pregunta", "pregunta": "¿Cómo es el borde de la hoja de la rosa?", "opciones": ["LISO", "CON DIENTES", "DE PLUMAS"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en la rosa.", "¿Cómo es el borde de su hoja?", "¡Con *dientes*, como una sierra!"]},
 {"t": "consejo", "titulo": "DEL SUELO", "texto": "Juntá las hojas que ya cayeron", "emoji": "🍂",
  "voz": ["Truco: juntá las hojas del *suelo*."]},
 {"t": "resumen", "items": [["FORMA", "redonda, alargada"], ["BORDE", "liso o con dientes"], ["CUIDAR", "juntar del suelo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las hojas tienen *formas* distintas.", "El *borde* es liso o con dientes.", "Juntamos las del *suelo*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Qué plantas hay en la plaza?"}, {"yo": True, "txt": "¡UN PINO, UN ROSAL Y PASTO!"}, {"yo": False, "txt": "¿Y son iguales?"}], "titulo": "ÁRBOLES", "sub": "arbustos y hierbas",
  "voz": ["Tomi le escribe a Sofi.", "¿Qué plantas hay en la plaza?", "Un pino, un rosal y pasto.", "Hoy: *árboles, arbustos y hierbas*."]},
 {"t": "bloques", "titulo": "TRES TIPOS", "items": [{"cab": "🌲 ÁRBOL", "txt": "ALTO, TRONCO DURO"}, {"cab": "🌹 ARBUSTO", "txt": "MEDIANO, MUCHOS TALLOS"}, {"cab": "🌱 HIERBA", "txt": "BAJITA, TALLO BLANDO"}],
  "voz": ["Hay tres tipos de plantas.", "El *árbol* es alto y tiene tronco.", "El *arbusto* es mediano, con muchos tallos.", "La *hierba* es bajita y blanda."]},
 {"t": "barras", "titulo": "¿QUÉ TAN ALTAS?", "unidad": "chicos parados", "items": [{"txt": "HIERBA", "valor": 1}, {"txt": "ARBUSTO", "valor": 2}, {"txt": "ÁRBOL", "valor": 8}],
  "voz": ["Las medimos con *chicos parados*.", "La hierba: menos de *1*.", "El arbusto: como *2*.", "¡El árbol: como *8*!"]},
 {"t": "pregunta", "pregunta": "¿Qué es el pasto?", "opciones": ["ÁRBOL", "ARBUSTO", "HIERBA"], "correcta": 2,
  "voz": ["Ahora vos. El pasto es bajito y blando.", "¿Qué tipo de planta es?", "¡Una *hierba*!"]},
 {"t": "consejo", "titulo": "MIRÁ EL TALLO", "texto": "¿Duro o blando?", "emoji": "🔍",
  "voz": ["Truco: tocá el *tallo*. ¿Es duro o blando?"]},
 {"t": "resumen", "items": [["ÁRBOL", "alto, tronco"], ["ARBUSTO", "mediano"], ["HIERBA", "bajita, blanda"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *árbol* es alto, con tronco.", "El *arbusto* es mediano.", "La *hierba* es bajita y blanda.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué necesita una planta para crecer?", "segundos": 6, "respuesta": "¡LUZ, AGUA Y TIERRA!", "emoji": "🌱", "titulo": "DÓNDE CRECEN", "sub": "mejor",
  "voz": ["Desafío: ¿qué necesita una planta para crecer?", "¡*Luz*, *agua* y *tierra*!", "Hoy: *dónde crecen mejor*."]},
 {"t": "experimento", "titulo": "¿CON LUZ O SIN LUZ?", "variable": "LA LUZ", "a": {"cab": "EN LA VENTANA", "emojis": ["🪴", "☀️"], "txt": "Con luz", "res": "VERDE Y FUERTE"}, "b": {"cab": "EN EL PLACARD", "emojis": ["🪴", "🌑"], "txt": "Sin luz", "res": "AMARILLA Y DÉBIL"},
  "voz": ["Sofi pone una planta en la *ventana*.", "Y otra igual en el *placard*.", "¡La de la ventana quedó verde y fuerte!"]},
 {"t": "causas", "causa": {"txt": "UNA PLANTA SANA", "emoji": "🪴"}, "items": ["LUZ", "AGUA JUSTA", "TIERRA"],
  "voz": ["¿Qué hace falta para una planta *sana*?", "Necesita *luz*.", "Necesita agua, pero *justa*.", "Y necesita *tierra* para sus raíces."]},
 {"t": "pregunta", "pregunta": "¿Dónde ponés tu planta?", "opciones": ["EN EL PLACARD", "EN LA VENTANA", "EN LA HELADERA"], "correcta": 1,
  "voz": ["Ahora vos. Tenés una planta nueva.", "¿Dónde crece mejor?", "¡En la *ventana*, con sol!"]},
 {"t": "consejo", "titulo": "AGUA JUSTA", "texto": "Mucha agua también hace mal", "emoji": "💧",
  "voz": ["Truco: regá *poquito*, no de más."]},
 {"t": "resumen", "items": [["LUZ", "la pone verde"], ["AGUA", "justa"], ["TIERRA", "para las raíces"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *luz* la pone verde.", "El *agua*, justa.", "Y la *tierra*, para las raíces.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡SOFI ES CIENTÍFICA!", "bajada": "Arma su cuaderno de campo", "emoji": "📓", "titulo": "MI CUADERNO", "sub": "de campo",
  "voz": ["¡Último momento! Sofi es *científica*.", "Arma su cuaderno de campo.", "Hoy: *mi cuaderno de campo*."]},
 {"t": "flujo", "titulo": "CÓMO LO HAGO", "items": ["SALGO", "OBSERVO", "DIBUJO", "ANOTO"],
  "voz": ["Primero, *salgo* al patio o la plaza.", "Después, *observo* una planta.", "La *dibujo* en mi cuaderno.", "Y *anoto* su nombre y el lugar."]},
 {"t": "partes", "emoji": "🍃", "titulo": "LA HOJA", "partes": [{"txt": "PARTE ANCHA", "x": 0.3, "y": -0.4}, {"txt": "NERVADURAS", "x": -0.3, "y": 0.0}, {"txt": "PECÍOLO", "x": 0.4, "y": 0.6}],
  "voz": ["Miramos las partes de la *hoja*.", "Tiene una *parte ancha*.", "Tiene rayitas: las *nervaduras*.", "Y un palito: el *pecíolo*."]},
 {"t": "pregunta", "pregunta": "¿Qué se dibuja en el cuaderno?", "opciones": ["LO QUE IMAGINO", "LO QUE VEO", "UN CUENTO"], "correcta": 1,
  "voz": ["Ahora vos. Sofi va a dibujar.", "¿Qué tiene que dibujar?", "¡*Lo que ve*!"]},
 {"t": "consejo", "titulo": "ANOTÁ EL LUGAR", "texto": "¿Dónde viste la planta?", "emoji": "📍",
  "voz": ["Truco: anotá *dónde* viste la planta."]},
 {"t": "resumen", "items": [["OBSERVAR", "mirar con atención"], ["DIBUJAR Y ANOTAR", "en el cuaderno"], ["PARTES", "nervaduras y pecíolo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Observamos* con atención.", "*Dibujamos* y *anotamos*.", "Conocimos las *partes* de la hoja.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Naturales 1", "titulo": TIT[n], "sub": f"Ciencias Naturales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
