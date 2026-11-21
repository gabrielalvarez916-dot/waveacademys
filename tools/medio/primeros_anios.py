# -*- coding: utf-8 -*-
"""MÁQUINA DEL NIVEL MEDIO (separada de la del Avanzado, que vive en tools/clase y tools/pdf y no se toca).
Regla de los PRIMEROS AÑOS (Nivel Medio, años 1, 2 y 3): chicos que recién aprenden a leer.
La usan tools/medio/clase (armar.py, voz_edge.py, revisar_contenido.py) y tools/medio/pdf (render_leccion.py, generar.py).

Qué cambia para estas materias:
- PDF: todo en IMPRENTA MAYÚSCULA, letra grande, frases cortas y un dibujo por sección.
- Clase animada: textos y subtítulos en IMPRENTA MAYÚSCULA, de a 2 palabras, frases cortas y voz más lenta.

Se aplica sola si la materia está en la lista de abajo (por nombre o por id), o si el contenido trae "estilo": "primeros".
Si se agrega una materia nueva de 1.º a 3.º del Nivel Medio, sumarla acá."""
import re

MATERIAS = {  # nombre exacto de la materia (subjects.name) -> id
    'Matemática 1': '37dacb79-7f3f-4f6f-a520-5dd41b97ebb3',
    'Lengua 1': 'eee219b3-9188-4e94-be06-223054ed5a57',
    'Ciencias Naturales 1': 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0',
    'Ciencias Sociales 1': '67d2ad89-caaa-4e82-8d25-8bbb08147818',
    'Inglés 1': 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664',
    'Matemática 2': '1a53eca0-e27f-4ab1-9ab6-b23941c7d920',
    'Lengua 2': '71a9ccdf-909e-4fbd-84e4-a68e9be813c8',
    'Ciencias Naturales 2': '255a306f-d137-43b8-a9ce-c621b75c890a',
    'Ciencias Sociales 2': 'dda5fe04-3df1-47cd-bcb6-a27259db9f3d',
    'Inglés 2': '1019f74a-dc31-49c2-baef-582e1936bfa8',
    'Matemática 3': '651eda34-d09a-45f2-82bf-e28abcc0c9ae',
    'Lengua 3': '7eb3b4aa-2c61-4c92-8846-1ba7a4568825',
    'Ciencias Naturales 3': '6d524570-8953-4105-9fc4-f937d67f13b3',
    'Ciencias Sociales 3': 'e6a7513a-517a-45cf-b91c-f94b9a2d7c92',
    'Ciencias Sociales Argentina 3': '194f5c97-b2a2-4217-accb-8812d331fad9',
    'Inglés 3': 'c140537f-29e4-4e80-8a8e-6bc4b82744d2',
    'Tecnología 1': 'f198d718-4519-4e66-a1c8-457fbfd06378',
}
IDS = set(MATERIAS.values())

# 4.º a 6.º del Nivel Medio: usan esta misma máquina, pero SIN la regla de mayúscula (letra y frases normales)
OTRAS_MEDIO = {
    'Ciencias Naturales 4': 'e16182e3-694c-408e-aa9d-a4ed9cd704b2', 'Ciencias Sociales 4': 'd6a785d2-30f8-4192-b5eb-4687743ad561',
    'Ciencias Sociales Argentina 4': 'de024e82-b14d-4b78-9e7c-bc357499a548', 'Inglés 4': '48847a5b-3bdd-4856-b480-4264d4e87d7f',
    'Lengua 4': '25c3a7a5-618e-4433-97d6-bc7ab02d3592', 'Matemática 4': '9fdd8a59-dca2-4598-b54c-67541ef50d63', 'Tecnología 2': '08a987b6-a126-4f17-8f36-fa4af82eb20b',
    'Ciencias Naturales 5': '06dd61d2-a4bf-4d6d-b91a-dabb8bb63555', 'Ciencias Sociales 5': '79e73cb6-893a-4c24-8d5f-17d8554124ac',
    'Ciencias Sociales Argentina 5': 'b9c2e232-3612-4bd1-b7fa-9927387b185b', 'Formación Ciudadana 1': '3b0eeb51-e5a9-4058-9459-561c055f062e',
    'Inglés 5': '92a8a872-d23f-42ba-871a-b5ae139afe4e', 'Lengua 5': '1ed0e028-df26-4ac1-9d6d-0f222a60861f', 'Matemática 5': '3e41dddf-0994-43a9-9640-d89a868228c6',
    'Tecnología 3': '98f059f0-35ad-43dc-8993-bf3428ba80d8', 'Ciencias Naturales 6': '456b2700-f6c4-41d9-af69-ba03d6c0f50c',
    'Ciencias Sociales 6': '3abb7786-f01d-43ef-8d82-35af22174712', 'Ciencias Sociales Argentina 6': 'bf372985-3143-4445-b673-9e3d1b1def86',
    'Formación Ciudadana 2': '88aad778-42c6-4500-ae77-3832ef6f774c', 'Inglés 6': 'b3257571-0703-4625-883e-dc819bf84113',
    'Lengua 6': 'e7ecd6a3-f6a2-446a-a77f-9a8ebe678874', 'Matemática 6': 'cd9135ff-8ef3-43be-bc4c-8723ae81c937', 'Tecnología 4': '93298bbb-163b-4653-9802-115cab703953',
}
MATERIAS_MEDIO = set(MATERIAS) | set(OTRAS_MEDIO)  # todo lo que arma la máquina del Nivel Medio (las demás materias son del Avanzado)


def es_medio(materia):
    return (materia or '').strip() in MATERIAS_MEDIO

RATE = '-8%'            # voz de la clase: pausada (los grandes van a +25 %)
PITCH = '+6Hz'          # tono un poco más alto: más alegre y expresiva
VOZ = 'es-AR-ElenaNeural'        # voz cálida para chicos (versión argentina)
VOZ_NEUTRA = 'es-MX-DaliaNeural'  # versión neutra (alumnos de otros países)
MAX_PALABRAS_VOZ = 10   # cada frase de la clase
MAX_PALABRAS_PDF = 12   # cada oración del PDF
MAX_ESCENAS = 10        # clase de 3 a 4 minutos


def es_primeros(materia=None, subject_id=None, contenido=None):
    if isinstance(contenido, dict) and contenido.get('estilo') == 'primeros':
        return True
    return (materia or '').strip() in MATERIAS or (subject_id or '') in IDS


def mayus(s):
    """IMPRENTA MAYÚSCULA respetando las marcas <b>…</b> y las entidades (&amp;). Los subíndices (₂) y los emojis no cambian."""
    partes = re.split(r'(<[^>]+>|&[a-z]+;|&#\d+;)', str(s))
    return ''.join(p if (p.startswith('<') or p.startswith('&')) else p.upper() for p in partes)


# claves del contenido del PDF que NO son texto para mostrar (no se pasan a mayúscula)
NO_TEXTO = {'tipo', 'imagen_tipo', 'png_base64', 'archivo', 'url', 'estilo', 'iguales', 'etapa', 'respuestas_carpeta', 'neutro_de'}


def mayus_contenido(x, clave=None):
    if clave in NO_TEXTO: return x
    if isinstance(x, str): return mayus(x)
    if isinstance(x, list): return [mayus_contenido(v) for v in x]
    if isinstance(x, dict): return {k: mayus_contenido(v, k) for k, v in x.items()}
    return x


def oraciones(s):
    s = re.sub(r'<[^>]+>', '', str(s))
    return [o.strip() for o in re.split(r'(?<=[.!?…:])\s+', s) if o.strip()]


def palabras(s):
    return len(re.findall(r'\d+(?:[.,]\d+)*|[^\W\d_]+', re.sub(r'<[^>]+>', '', str(s))))  # 1.000 cuenta como una palabra
