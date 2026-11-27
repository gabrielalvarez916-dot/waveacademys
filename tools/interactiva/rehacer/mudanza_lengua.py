# -*- coding: utf-8 -*-
"""26/11/2026 · Mudanza de Lengua I y II al mapa nuevo (docs/lengua-misiones-de-genero.md).
Lo que sirve para otra misión va a la clave "mudado" del archivo destino (material para escribir esa misión; las máquinas no lo cargan).
Lo que no sirve va a contenido/_archivo/lengua/ y sale de la misión."""
import json, os, copy, shutil
R = os.path.join(os.path.dirname(__file__), '..', '..', '..')
C = lambda L, k: os.path.join(R, f'contenido/lengua-{L}/mision-{k}/mision-{k}.json')
ARCH = os.path.join(R, 'contenido/_archivo/lengua'); os.makedirs(ARCH, exist_ok=True)
cache = {}
def M(L, k):
    if (L, k) not in cache:
        p = C(L, k)
        cache[(L, k)] = json.load(open(p)) if os.path.exists(p) else None
    return cache[(L, k)]
def destino(L, k):
    if M(L, k) is None:
        base = M(L, 4) if L in (1, 2) else None
        cache[(L, k)] = {'subject_id': (base or {}).get('subject_id'), 'tema': k, 'niveles': {}, 'act': {}, 'examen': []}
    return cache[(L, k)]
def nivel(L, k, n):
    m = M(L, k); return {'niveles': m['niveles'].get(n), 'act': m['act'].get(n, []), 'examen': [e for e in m.get('examen', []) if str(e[0]) == n]}
def mudar(origen, n, L2, k2, para, nota):
    L, k = origen
    destino(L2, k2).setdefault('mudado', []).append({'de': f'Lengua {L} · misión {k} · nivel {n}', 'para': para, 'nota': nota, **copy.deepcopy(nivel(L, k, n))})
def mudar_tema(origen, n, i, L2, k2, para, nota):
    L, k = origen; t = M(L, k)['niveles'][n]['leccion']['temas'][i]
    destino(L2, k2).setdefault('mudado', []).append({'de': f'Lengua {L} · misión {k} · nivel {n} · pantalla «{t["titulo"]}»', 'para': para, 'nota': nota, 'tema': copy.deepcopy(t)})
def archivar(L, k, que, contenido):
    p = os.path.join(ARCH, f'lengua-{L}-mision-{k}.json')
    a = json.load(open(p)) if os.path.exists(p) else []
    a.append({'que': que, 'contenido': copy.deepcopy(contenido)}); json.dump(a, open(p, 'w'), ensure_ascii=False, indent=1)
def vaciar(L, k):
    m = M(L, k); archivar(L, k, 'misión completa antes de la mudanza', {x: m.get(x) for x in ('niveles', 'act', 'examen', 'practica', 'examen_titulo')})
    m['niveles'] = {}; m['act'] = {}; m['examen'] = []; m.pop('actualizar_preguntas', None)
def quitar_nivel(L, k, n, motivo):
    m = M(L, k); archivar(L, k, f'nivel {n}: {motivo}', nivel(L, k, n))
    m['niveles'].pop(n, None); m['act'].pop(n, None); m['examen'] = [e for e in m.get('examen', []) if str(e[0]) != n]

# ---------- Lengua I ----------
m12, m3 = copy.deepcopy(M(1, 12)), copy.deepcopy(M(1, 3))
# Clases de palabras: la misión 12 entera pasa a la 3
archivar(1, 3, 'misión completa antes de la mudanza (Narrar con orden)', {x: m3.get(x) for x in ('niveles', 'act', 'examen')})
mudar((1, 3), '2', 1, 12, 'nivel 4 «Los pretéritos en el relato»', 'pretérito perfecto simple e imperfecto, acción y fondo')
M(1, 3).update({'niveles': m12['niveles'], 'act': m12['act'], 'examen': m12['examen'], 'practica': m12.get('practica'), 'examen_titulo': m12.get('examen_titulo')})
M(1, 12).update({'niveles': {}, 'act': {}, 'examen': []}); M(1, 12).pop('actualizar_preguntas', None)
archivar(1, 12, 'misión completa (Clases de palabras) — se mudó a la misión 3', {x: m12.get(x) for x in ('niveles', 'act', 'examen')})
# Misión 1 (Volver a leer)
mudar_tema((1, 1), '1', 0, 1, 2, 'libro del nivel (nivel 5)', 'paratexto e hipótesis de lectura, para las actividades del libro')
mudar_tema((1, 1), '1', 1, 1, 2, 'libro del nivel (nivel 5)', 'inferir con pistas del texto')
mudar_tema((1, 1), '1', 3, 1, 2, 'nivel 3 «El narrador y las dos historias»', 'narrador y autor; primera, tercera y omnisciente')
mudar_tema((1, 1), '3', 1, 1, 15, 'cohesión', 'oración y párrafo; puntos')
mudar_tema((1, 1), '3', 2, 1, 15, 'cohesión', 'conectores de adición, oposición, causa y consecuencia')
mudar_tema((1, 1), '4', 1, 1, 18, 'cito y armo bibliografía', 'ficha bibliográfica')
vaciar(1, 1)
# Misión 2 (policial): niveles 1 a 3 se quedan; el 4 (escribir un policial) no sirve
mudar_tema((1, 2), '2', 2, 1, 2, 'libro del nivel (nivel 5)', 'las pistas de «La liga de los pelirrojos»')
quitar_nivel(1, 2, '4', 'planificar y escribir un policial (taller de escritor)')
# Misión 6 (Canterville 1) → Parodia y humor
mudar((1, 6), '3', 1, 6, 'parodia y humor', 'ironía, contraste, exageración y parodia en Canterville')
mudar((1, 6), '1', 1, 6, 'libro del nivel (nivel 5): El fantasma de Canterville', 'el cuento, los personajes, el narrador')
mudar((1, 6), '2', 1, 6, 'libro del nivel (nivel 5): El fantasma de Canterville', 'intentos y respuestas, causa y consecuencia')
vaciar(1, 6)
# Misión 9 (Canterville 2) → Épica
mudar((1, 9), '1', 1, 6, 'libro del nivel (nivel 5): El fantasma de Canterville', 'el giro y el final')
mudar((1, 9), '2', 1, 6, 'libro del nivel (nivel 5): El fantasma de Canterville', 'personajes dinámicos y estáticos')
mudar((1, 9), '4', 1, 6, 'libro del nivel (nivel 5): El fantasma de Canterville', 'la reseña (escritura de estudiante)')
mudar((1, 9), '3', 4, 16, 'Cine y literatura', 'adaptación: libro y versión audiovisual')
vaciar(1, 9)
# Misión 11 (Poesía) → Ciencia ficción
mudar((1, 11), '1', 3, 6, 'La gauchesca y la poesía popular', 'verso, estrofa, pausas y entonación')
mudar((1, 11), '3', 3, 6, 'La gauchesca y la poesía popular', 'rima consonante y asonante, verso libre')
mudar((1, 11), '2', 4, 11, 'Las vanguardias poéticas', 'comparación, metáfora y personificación')
vaciar(1, 11)
# ---------- Lengua II ----------
for n in ('1', '2', '3', '4'): mudar((2, 1), n, 1, 6, 'parodia y humor (adaptar a primer año)', 'humor, ironía, parodia y sátira')
vaciar(2, 1)
quitar_nivel(2, 2, '4', 'planificar y escribir un relato de terror (taller de escritor)')
mudar((2, 3), '2', 2, 3, 'nivel 3 «El espacio y la naturaleza»', 'la selva como fondo o personaje')
mudar((2, 3), '3', 2, 3, 'nivel 4 «El final del cuento realista»', 'finales trágicos e indicios')
vaciar(2, 3)
for n, nota in (('1', 'la autora y el desafío'), ('2', 'el científico y la criatura'), ('3', 'relato enmarcado')):
    mudar((2, 6), n, 2, 2, 'terror y gótico / libro del nivel: Frankenstein', nota)
vaciar(2, 6)

for (L, k), m in cache.items():
    p = C(L, k); os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(m, open(p, 'w'), ensure_ascii=False, indent=1)
    print('guardado', p.split('contenido/')[1], '· niveles', sorted(m['niveles']), '· mudado', len(m.get('mudado', [])))
