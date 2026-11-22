# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 10 · Cuidamos nuestro entorno: las 4 clases animadas.
Metáfora: los guardianes del patio. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-nat1-m10-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0'
TEMA = 10
TIT = {1: 'Observo el patio de la escuela', 2: 'Qué cuida y qué daña a un ambiente', 3: 'Armamos carteles de cuidado', 4: 'Mostramos lo que aprendimos'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "reto", "texto": "¿Qué hay en el patio de tu escuela?", "segundos": 6, "respuesta": "¡ÁRBOLES, BANCOS Y BICHITOS!", "emoji": "🏫", "titulo": "MI PATIO", "sub": "lo observo",
  "voz": ["Desafío: ¿qué hay en el patio de tu escuela?", "¡Árboles, bancos y *bichitos*!", "Hoy: *observo el patio*."]},
 {"t": "partes", "emoji": "🏫", "titulo": "EL PATIO", "partes": [{"txt": "ÁRBOL", "x": -0.6, "y": -0.4}, {"txt": "CANTERO", "x": 0.5, "y": 0.5}, {"txt": "TACHO", "x": 0.6, "y": -0.2}, {"txt": "BANCO", "x": -0.4, "y": 0.6}],
  "voz": ["Miramos el *patio* de la escuela.", "Hay un *árbol* grande.", "Hay un *cantero* con plantas.", "Hay un *tacho* para la basura.", "Y un *banco* para sentarse."]},
 {"t": "barras", "titulo": "LO QUE CONTÓ SOFI", "unidad": "cosas", "items": [{"txt": "ÁRBOLES", "valor": 3}, {"txt": "TACHOS", "valor": 2}, {"txt": "PAPELES", "valor": 8}],
  "voz": ["Sofi cuenta y anota.", "*3* árboles.", "*2* tachos.", "¡Y *8* papeles en el piso!"]},
 {"t": "pregunta", "pregunta": "¿Cuál es un ser vivo del patio?", "opciones": ["SUELO", "ÁRBOL", "AGUA"], "correcta": 1,
  "voz": ["Ahora vos. Suelo, árbol, agua.", "¿Cuál es un ser vivo?", "¡El *árbol*!"]},
 {"t": "consejo", "titulo": "MIRÁ SIN ROMPER", "texto": "Observar es mirar con cuidado", "emoji": "👀",
  "voz": ["Truco: observá *sin romper* nada."]},
 {"t": "resumen", "items": [["ENTORNO", "lo que nos rodea"], ["VIVOS", "árboles, bichitos"], ["REGISTRAR", "contar y anotar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *entorno* es lo que nos rodea.", "Hay *seres vivos* y lo inerte.", "Contamos y *anotamos*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🌳", "lineas": ["Tomi ve papeles en el patio.", "Un pajarito pica un envoltorio.", "¡Eso lo puede lastimar!"], "titulo": "CUIDA O DAÑA", "sub": "al ambiente",
  "voz": ["Tomi ve *papeles* en el patio.", "Un pajarito pica un envoltorio.", "¡Eso lo puede *lastimar*!", "Hoy: *qué cuida y qué daña*."]},
 {"t": "causas", "causa": {"txt": "BASURA EN EL PISO", "emoji": "🗑️"}, "items": ["ENSUCIA EL PATIO", "LASTIMA A LOS ANIMALES", "TAPA LAS PLANTAS"],
  "voz": ["¿Qué pasa con la *basura en el piso*?", "*Ensucia* el patio.", "Puede *lastimar* a los animales.", "Y *tapa* las plantas."]},
 {"t": "antesdespues", "antes": {"cab": "ANTES", "emoji": "🗑️", "texto": "Patio sucio"}, "despues": {"cab": "DESPUÉS", "emoji": "🌻", "texto": "¡Patio limpio!"},
  "voz": ["Antes, el patio estaba *sucio*.", "El grado juntó papeles: ¡quedó *limpio*!"]},
 {"t": "clasificar", "cajas": [{"cab": "CUIDA", "emoji": "💚"}, {"cab": "DAÑA", "emoji": "❌"}], "fichas": [{"txt": "REGAR", "caja": 0}, {"txt": "ROMPER RAMAS", "caja": 1}, {"txt": "USAR EL TACHO", "caja": 0}, {"txt": "CANILLA ABIERTA", "caja": 1}],
  "voz": ["Separamos en dos cajas.", "Lo que *cuida* el ambiente.", "Y lo que lo *daña*."]},
 {"t": "pregunta", "pregunta": "¿Qué cuida el ambiente?", "opciones": ["TIRAR PAPELES", "USAR EL TACHO", "PISAR EL CANTERO"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el patio.", "¿Qué lo cuida?", "¡*Usar el tacho*!"]},
 {"t": "resumen", "items": [["DAÑA", "basura, romper, gastar"], ["CUIDA", "tacho, regar, cerrar"], ["VOS", "podés ayudar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La basura y romper *dañan*.", "El tacho y regar *cuidan*.", "¡*Vos* podés ayudar!", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Hacemos un cartel para el patio?"}, {"yo": True, "txt": "¡SÍ! QUE DIGA: USÁ EL TACHO"}, {"yo": False, "txt": "¡Genial!"}], "titulo": "CARTELES", "sub": "de cuidado",
  "voz": ["Tomi le escribe a Sofi.", "¿Hacemos un cartel para el patio?", "¡Sí! Que diga: usá el tacho.", "Hoy: *armamos carteles de cuidado*."]},
 {"t": "bloques", "titulo": "PARTES DEL CARTEL", "items": [{"cab": "1", "txt": "TÍTULO"}, {"cab": "2", "txt": "DIBUJO"}, {"cab": "3", "txt": "MENSAJE"}],
  "voz": ["Un cartel tiene *tres* partes.", "Arriba, el *título*.", "En el medio, un *dibujo*.", "Abajo, el *mensaje* corto."]},
 {"t": "corrige", "titulo": "REVISAMOS EL CARTEL", "cambios": [{"antes": "CUIDÁ LAS PLANTA", "despues": "CUIDÁ LAS PLANTAS", "motivo": "faltaba una letra"}, {"antes": "USÁELTACHO", "despues": "USÁ EL TACHO", "motivo": "espacios"}],
  "voz": ["Revisamos los carteles.", "En *plantas* faltaba una letra.", "Y separamos con *espacios*."]},
 {"t": "pregunta", "pregunta": "¿Cuál es un buen mensaje?", "opciones": ["HOLA", "USÁ EL TACHO", "ME GUSTA EL HELADO"], "correcta": 1,
  "voz": ["Ahora vos. Mirá los mensajes.", "¿Cuál cuida el ambiente?", "¡*Usá el tacho*!"]},
 {"t": "consejo", "titulo": "LETRAS GRANDES", "texto": "Para que se lea de lejos", "emoji": "🔠",
  "voz": ["Truco: escribí con letras *grandes*."]},
 {"t": "resumen", "items": [["TÍTULO", "arriba"], ["DIBUJO", "ayuda a entender"], ["MENSAJE", "corto y claro"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *título* va arriba.", "El *dibujo* ayuda a entender.", "El *mensaje* es corto y claro.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡GRAN MUESTRA DE CIENCIAS!", "bajada": "Primer grado cuenta lo que aprendió", "emoji": "🎉", "titulo": "LO QUE", "sub": "aprendimos",
  "voz": ["¡Último momento! Hay una *muestra de ciencias*.", "Primer grado cuenta lo que aprendió.", "Hoy: *mostramos lo que aprendimos*."]},
 {"t": "matriz", "titulo": "ESTE AÑO VIMOS", "celdas": [{"cab": "🧍", "txt": "MI CUERPO"}, {"cab": "🐾", "txt": "ANIMALES"}, {"cab": "🌱", "txt": "PLANTAS"}, {"cab": "🌙", "txt": "EL CIELO"}],
  "voz": ["¡Aprendimos un montón!", "Conocimos nuestro *cuerpo*.", "Miramos los *animales*.", "Exploramos las *plantas*.", "Y observamos el *cielo*."]},
 {"t": "ciclo", "titulo": "PARA CUIDAR", "items": ["USAR MENOS", "REUTILIZAR", "SEPARAR"],
  "voz": ["Tres ideas para *cuidar*.", "*Usar menos* cosas.", "*Reutilizar*: usar otra vez.", "Y *separar* la basura."]},
 {"t": "pregunta", "pregunta": "¿Qué es reutilizar?", "opciones": ["TIRAR TODO", "USAR OTRA VEZ", "ROMPER"], "correcta": 1,
  "voz": ["Ahora vos. Tenés una botella vacía.", "¿Qué es reutilizarla?", "¡*Usarla otra vez*! Como maceta."]},
 {"t": "consejo", "titulo": "FUERTE Y CLARO", "texto": "Mirá a los que te escuchan", "emoji": "🎤",
  "voz": ["Truco: en la muestra, hablá *fuerte y claro*."]},
 {"t": "resumen", "items": [["APRENDIMOS", "cuerpo, animales, plantas, cielo"], ["CUIDAR", "usar menos, reutilizar"], ["MOSTRAR", "contar a otros"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Vimos el cuerpo, animales, plantas y *cielo*.", "Sabemos *cuidar* el ambiente.", "¡Y lo *mostramos* a todos!", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Naturales 1", "titulo": TIT[n], "sub": f"Ciencias Naturales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
