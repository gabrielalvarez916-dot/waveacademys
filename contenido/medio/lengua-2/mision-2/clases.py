# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 2 · Letra cursiva: las 4 clases animadas.
Usa la plantilla «cursiva» (letra escolar Playwrite Argentina). Vía fonológica: la voz dice sonidos, no nombres de letras.
Metáfora: el cuaderno viajero de Sofi. Genera tools/medio/clase/lecciones/medio-leng2-m2-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'b34026dd-cb13-440c-b6f5-1f5f8c28cf43', 2: 'cdc501cc-7e44-4ade-96b4-6b9be002aed8', 3: '5e2a2145-aec5-44c9-8ed6-a7f8df552937', 4: '4fa4cbd8-75f2-4209-9f1c-12f6bc64cd5e'}
TIT = {1: 'Trazos para escribir en cursiva', 2: 'Cursiva con vocales', 3: 'Cursiva con las primeras consonantes', 4: 'Copiar mi nombre en cursiva'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "✏️", "lineas": ["Sofi ya escribe en imprenta.", "Ahora quiere escribir de corrido.", "¡Como su mamá!"], "titulo": "LA CURSIVA", "sub": "trazos",
  "voz": ["Sofi ya escribe en *imprenta*.", "Ahora quiere escribir *de corrido*.", "¡Como escribe su mamá!", "Hoy: *trazos para la cursiva*."]},
 {"t": "comparar", "a": {"cab": "IMPRENTA", "texto": "letras separadas", "emoji": "🔠"}, "b": {"cab": "CURSIVA", "texto": "letras unidas", "emoji": "✍️"}, "signo": "≠",
  "voz": ["En *imprenta*, las letras van separadas.", "En *cursiva*, las letras van unidas.", "¡Sin levantar el lápiz!"]},
 {"t": "trazos", "texto": "llllll", "nota": "Bucles: subo, giro y bajo", "titulo": "BUCLES",
  "voz": ["Primer trazo: los *bucles*. Mirá el modelo.", "Repasamos: subo, giro arriba y bajo.", "¡Como una montaña rusa!"]},
 {"t": "trazos", "texto": "mmmmm", "nota": "Puentes: arriba y abajo", "titulo": "PUENTES",
  "voz": ["Segundo trazo: los *puentes*.", "Repasamos: subo, hago una curvita y bajo.", "¡Uno detrás del otro!"]},
 {"t": "trazos", "texto": "uuuuu", "nota": "Ondas: como el mar", "titulo": "ONDAS",
  "voz": ["Tercer trazo: las *ondas*.", "Repasamos: bajo, subo, bajo, subo.", "¡Como las olas del mar!"]},
 {"t": "quiz4", "pregunta": "En cursiva, ¿cómo van las letras?", "opciones": ["Unidas", "Separadas"], "correcta": 0,
  "voz": ["Ahora vos.", "En cursiva, ¿cómo van las letras?", "¡*Unidas*!"]},
 {"t": "resumen", "items": [["CURSIVA", "letras unidas"], ["TRAZOS", "bucles, puentes, ondas"], ["EL LÁPIZ", "no se levanta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *cursiva* tiene letras unidas.", "Practicamos *bucles, puentes y ondas*.", "¡Sin levantar el *lápiz*!", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Cómo se escriben las vocales en cursiva?"}, {"yo": True, "txt": "¡Te muestro!"}, {"yo": False, "txt": "¡Dale!"}], "titulo": "CURSIVA", "sub": "con vocales",
  "voz": ["Tomi le escribe a Sofi.", "¿Cómo se escriben las vocales en cursiva?", "Sofi le dice: ¡te muestro!", "Hoy: *cursiva con vocales*."]},
 {"t": "cursiva", "imprenta": "A  E  I  O  U", "texto": "a e i o u", "titulo": "LAS VOCALES",
  "voz": ["Estas son las cinco vocales.", "En cursiva: a, e, i, o, u.", "¡Cada una tiene una colita de *salida*!"]},
 {"t": "cursiva", "texto": "ae io ua", "nota": "La salida de una es la entrada de la otra", "titulo": "UNIMOS VOCALES",
  "voz": ["Ahora unimos las vocales.", "La salida de una es la *entrada* de la otra.", "¡Sin levantar el lápiz!"]},
 {"t": "vof", "afirmacion": "El punto de la i se pone al terminar", "emoji": "✏️", "verdadero": True, "explicacion": "Así no levantamos el lápiz",
  "voz": ["¿Verdadero o falso? El punto va al terminar.", "Pensá: ¿cuándo levantamos el lápiz?", "¡*Verdadero*! El punto va al final."]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["a", "e", "i", "o"], "falta": "u", "regla": "Las cinco vocales",
  "voz": ["Mirá: a, e, i, o…", "¿Qué vocal sigue?", "¡La *u*!"]},
 {"t": "resumen", "items": [["VOCALES", "a, e, i, o, u"], ["SALIDA", "una colita"], ["UNIR", "la salida es la entrada"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *vocales*: a, e, i, o, u.", "Cada una tiene una *salida*.", "La salida es la *entrada* de la otra.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué palabra se forma con me + sa?", "segundos": 5, "respuesta": "¡MESA!", "emoji": "🪑", "titulo": "CURSIVA", "sub": "primeras consonantes",
  "voz": ["Desafío: ¿qué palabra se forma con me y sa?", "¡*Mesa*!", "Hoy: *palabras en cursiva*."]},
 {"t": "cursiva", "imprenta": "MA  LO  SA  PE  TU", "texto": "ma lo sa pe tu", "titulo": "SÍLABAS",
  "voz": ["Unimos consonantes con vocales.", "ma, lo, sa, pe, tu.", "¡Todo unido, sin levantar el lápiz!"]},
 {"t": "cursiva", "imprenta": "MESA", "texto": "mesa", "nota": "me + sa = mesa", "titulo": "UNA PALABRA",
  "voz": ["Escribimos me…", "…y sin levantar, sa: ¡mesa!", "Toda la palabra va *unida*."]},
 {"t": "cursiva", "imprenta": "SAPO", "texto": "sapo", "nota": "sa + po = sapo", "titulo": "OTRA PALABRA",
  "voz": ["Ahora sa…", "…y po: ¡sapo!", "¡Muy bien unida!"]},
 {"t": "unir", "titulo": "SÍLABAS Y PALABRAS", "pares": [["me + sa", "mesa"], ["sa + po", "sapo"], ["pa + to", "pato"]],
  "voz": ["Uní las sílabas con su palabra.", "Me y sa: *mesa*.", "Sa y po: *sapo*.", "Pa y to: *pato*."]},
 {"t": "pregunta", "pregunta": "¿Qué palabra se forma con pa + to?", "opciones": ["Pato", "Topa", "Sapo"], "correcta": 0,
  "voz": ["Ahora vos: pa y to.", "¿Qué palabra se forma?", "¡*Pato*!"]},
 {"t": "resumen", "items": [["CONSONANTE", "se une a la vocal"], ["SÍLABA", "ma, lo, sa"], ["PALABRA", "toda unida"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La consonante se *une* a la vocal.", "Así salen las *sílabas*.", "Y la palabra va *toda unida*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Sofi firma en cursiva!", "bajada": "Su primer dibujo firmado", "emoji": "🖍️", "titulo": "MI NOMBRE", "sub": "en cursiva",
  "voz": ["¡Último momento: Sofi firmó en cursiva!", "Escribió su nombre en su dibujo.", "Hoy: *copiar mi nombre en cursiva*."]},
 {"t": "cursiva", "imprenta": "Sofi", "texto": "Sofi", "nota": "Empieza con mayúscula", "titulo": "LA FIRMA DE SOFI",
  "voz": ["Sofi escribe su nombre.", "Primero la *mayúscula*, grande y con adorno. Después ofi, unido.", "¡Los nombres empiezan con mayúscula!"]},
 {"t": "cursiva", "imprenta": "Tomi", "texto": "Tomi", "titulo": "LA FIRMA DE TOMI",
  "voz": ["Ahora Tomi escribe su nombre.", "La mayúscula, y después omi, todo unido.", "¡Qué linda firma!"]},
 {"t": "pasos", "titulo": "CÓMO ESCRIBO MI NOMBRE", "items": [{"txt": "Lo miro en imprenta", "emoji": "👀"}, {"txt": "Empiezo con mayúscula", "emoji": "🅰️"}, {"txt": "Sigo todo unido", "emoji": "✍️"}],
  "voz": ["¿Cómo escribo mi nombre en cursiva?", "Primero lo *miro* en imprenta.", "Empiezo con la *mayúscula*.", "Y sigo *todo unido*."]},
 {"t": "memoria", "titulo": "NOMBRES DEL GRADO", "items": ["Sofi", "Tomi", "Ana", "Lola"], "falta": 2,
  "voz": ["Mirá los nombres del grado: todos con mayúscula.", "Se tapan… ¡y uno desapareció!", "¡Faltaba *Ana*!"]},
 {"t": "pregunta", "pregunta": "¿Con qué empieza un nombre?", "opciones": ["Con mayúscula", "Con minúscula"], "correcta": 0,
  "voz": ["Ahora vos.", "¿Con qué empieza un nombre?", "¡Con *mayúscula*!"]},
 {"t": "resumen", "items": [["MAYÚSCULA", "al principio"], ["UNIDO", "todo el nombre"], ["FIRMAR", "en tus trabajos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El nombre empieza con *mayúscula*.", "Después va todo *unido*.", "¡Ahora podés *firmar* tus trabajos!", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m2-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 2 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
