# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 6 · Del campo a mi mesa: las 4 clases animadas.
Metáfora: el viaje de un tomate hasta la mesa. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-soc1-m6-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = '67d2ad89-caaa-4e82-8d25-8bbb08147818'
TEMA = 6
TIT = {1: 'La manzana, el tomate y la yerba mate', 2: 'Las etapas de producir un alimento', 3: 'Herramientas y técnicas de cultivo', 4: 'Trabajos para todas las personas'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍎", "lineas": ["Sofi come una manzana.", "Se pregunta de dónde viene.", "¡Empezó en el campo!"], "titulo": "DEL CAMPO", "sub": "a mi mesa",
  "voz": ["Sofi come una *manzana*.", "Se pregunta de dónde viene.", "¡Empezó en el *campo*!", "Hoy: *la manzana, el tomate y la yerba*."]},
 {"t": "matriz", "titulo": "¿DE DÓNDE VIENEN?", "celdas": [{"cab": "🍎 MANZANA", "txt": "ÁRBOL"}, {"cab": "🍅 TOMATE", "txt": "PLANTA"}, {"cab": "🧉 YERBA", "txt": "HOJAS DE UN ARBUSTO"}, {"cab": "🥕 ZANAHORIA", "txt": "RAÍZ"}],
  "voz": ["Cada alimento viene de una *planta*.", "La manzana, de un *árbol*.", "El tomate, de una *planta* baja.", "La yerba, de las *hojas* de un arbusto.", "¡La zanahoria es una *raíz*!"]},
 {"t": "antesdespues", "antes": {"cab": "VERDE", "emoji": "🟢", "texto": "Todavía no"}, "despues": {"cab": "ROJO", "emoji": "🍅", "texto": "¡Listo para cosechar!"},
  "voz": ["Primero el tomate está *verde*.", "Cuando madura, se pone *rojo*: ¡a cosechar!"]},
 {"t": "pregunta", "pregunta": "¿De qué parte sale la yerba?", "opciones": ["RAÍZ", "HOJAS", "FLOR"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en la yerba mate.", "¿De qué parte de la planta sale?", "¡De las *hojas*!"]},
 {"t": "consejo", "titulo": "LAVÁ LA FRUTA", "texto": "Siempre antes de comerla", "emoji": "🚰",
  "voz": ["Truco: *lavá* la fruta antes de comerla."]},
 {"t": "resumen", "items": [["MANZANA", "del árbol"], ["TOMATE", "de una planta"], ["YERBA", "hojas secas y molidas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *manzana* viene del árbol.", "El *tomate*, de una planta.", "La *yerba*, de las hojas.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Cómo llegó el tomate a la verdulería?"}, {"yo": True, "txt": "¡HIZO UN VIAJE LARGO!"}, {"yo": False, "txt": "¿Desde dónde?"}], "titulo": "LAS ETAPAS", "sub": "de un alimento",
  "voz": ["Tomi le escribe a Sofi.", "¿Cómo llegó el tomate a la verdulería?", "¡Hizo un *viaje* largo!", "Hoy: *las etapas de producir un alimento*."]},
 {"t": "flujo", "titulo": "EL VIAJE DEL TOMATE", "items": ["SIEMBRO", "CUIDO", "COSECHO", "TRANSPORTO", "VENDO"],
  "voz": ["Primero, se *siembra*.", "Después, se *cuida* la planta.", "Se *cosecha*.", "Se *transporta* en camión.", "Y se *vende* en la verdulería."]},
 {"t": "bloques", "titulo": "QUIÉNES TRABAJAN", "items": [{"cab": "👩‍🌾", "txt": "AGRICULTORA"}, {"cab": "🚚", "txt": "CAMIONERO"}, {"cab": "🧑‍🍳", "txt": "VERDULERA"}],
  "voz": ["En cada etapa trabaja alguien.", "La *agricultora* siembra y cosecha.", "El *camionero* lo lleva.", "La *verdulera* lo vende."]},
 {"t": "pregunta", "pregunta": "¿Qué etapa va primero?", "opciones": ["VENDER", "SEMBRAR", "COMER"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el orden.", "¿Qué va primero?", "¡*Sembrar*!"]},
 {"t": "consejo", "titulo": "UNA CADENA", "texto": "Cada etapa necesita la anterior", "emoji": "🔗",
  "voz": ["Truco: cada etapa necesita *la anterior*."]},
 {"t": "resumen", "items": [["CAMPO", "sembrar, cuidar, cosechar"], ["VIAJE", "transportar"], ["MESA", "vender y comer"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En el *campo*: sembrar y cosechar.", "Después, el *viaje* en camión.", "Y al final, llega a la *mesa*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué máquina ara un campo enorme?", "segundos": 6, "respuesta": "¡EL TRACTOR!", "emoji": "🚜", "titulo": "HERRAMIENTAS", "sub": "y técnicas",
  "voz": ["Desafío: ¿qué máquina ara un campo enorme?", "¡El *tractor*!", "Hoy: *herramientas y técnicas de cultivo*."]},
 {"t": "comparar", "a": {"cab": "ANTES", "texto": "A MANO CON AZADA", "emoji": "🧑‍🌾"}, "b": {"cab": "AHORA", "texto": "CON TRACTOR", "emoji": "🚜"}, "signo": "vs",
  "voz": ["*Antes* se trabajaba a mano.", "*Ahora* hay máquinas como el tractor.", "¡Pero en la huerta seguimos usando la pala!"]},
 {"t": "zoom", "niveles": [{"emoji": "🌾", "txt": "EL CAMPO"}, {"emoji": "〰️", "txt": "LOS SURCOS"}, {"emoji": "🌱", "txt": "LA SEMILLA"}],
  "voz": ["Miramos el *campo*.", "Vemos los *surcos* en la tierra.", "¡Y adentro, una *semilla*!"]},
 {"t": "pregunta", "pregunta": "¿Con qué regás la huerta?", "opciones": ["TRACTOR", "REGADERA", "PALA"], "correcta": 1,
  "voz": ["Ahora vos. Las plantas tienen sed.", "¿Con qué las regás?", "¡Con la *regadera*!"]},
 {"t": "consejo", "titulo": "CON CUIDADO", "texto": "Las herramientas se usan con un adulto", "emoji": "⚠️",
  "voz": ["Importante: las herramientas, *con un adulto*."]},
 {"t": "resumen", "items": [["HERRAMIENTAS", "pala, azada, regadera"], ["ANTES", "a mano"], ["AHORA", "con máquinas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Usamos *herramientas* para cultivar.", "*Antes* se hacía a mano.", "*Ahora* ayudan las máquinas.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡ANA MANEJA EL TRACTOR!", "bajada": "En su chacra cosecha tomates", "emoji": "👩‍🌾", "titulo": "TRABAJOS", "sub": "para todas las personas",
  "voz": ["¡Último momento! *Ana* maneja el tractor.", "En su chacra cosecha tomates.", "Hoy: *trabajos para todas las personas*."]},
 {"t": "causas", "causa": {"txt": "PARA QUE LLEGUE LA MANZANA", "emoji": "🍎"}, "items": ["TRABAJA LA AGRICULTORA", "TRABAJA EL CAMIONERO", "TRABAJA LA VERDULERA"],
  "voz": ["Para que llegue la *manzana* a tu mesa…", "trabaja la *agricultora*.", "Trabaja el *camionero*.", "Y trabaja la *verdulera*."]},
 {"t": "corrige", "titulo": "¿ESTÁ BIEN?", "cambios": [{"antes": "SOLO LOS VARONES MANEJAN", "despues": "TODOS PUEDEN MANEJAR", "motivo": "igualdad"}, {"antes": "SOLO LAS MUJERES COCINAN", "despues": "TODOS PUEDEN COCINAR", "motivo": "igualdad"}],
  "voz": ["Arreglamos frases que están mal.", "*Todos* pueden manejar un tractor.", "Y *todos* pueden cocinar."]},
 {"t": "pregunta", "pregunta": "¿Quién puede cosechar?", "opciones": ["SOLO VARONES", "TODAS LAS PERSONAS", "NADIE"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en la chacra.", "¿Quién puede cosechar?", "¡*Todas las personas*!"]},
 {"t": "consejo", "titulo": "TODOS PUEDEN", "texto": "No hay trabajos de un solo grupo", "emoji": "🤝",
  "voz": ["Recordá: *todos* pueden hacer cualquier trabajo."]},
 {"t": "resumen", "items": [["MUCHOS", "trabajan muchas personas"], ["IGUALDAD", "todos pueden"], ["IMPORTANTES", "todos los trabajos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Trabajan *muchas personas*.", "*Todos* pueden hacer cualquier trabajo.", "Todos los trabajos son *importantes*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Sociales 1", "titulo": TIT[n], "sub": f"Ciencias Sociales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
