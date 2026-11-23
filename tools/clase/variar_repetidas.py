# -*- coding: utf-8 -*-
"""Agrega variedad a clases YA HECHAS solo donde se repiten, sin tocar el contenido ni la voz.
Cambia la forma de mostrar una escena por otra equivalente con LA MISMA cantidad de frases de voz (así no se graba voz nueva):
  tabla (2 columnas) -> unir / bloques / matriz · pregunta -> quiz4 · definicion corta -> pizarra · pasos -> bloques
  clasificar -> bloques / antesdespues · errores -> corrige · bloques (4) <-> matriz
Reglas que hace cumplir (las de revisar_contenido.py): dos clases de una misión no comparten más de la mitad de sus pantallas,
y una misión no repite más del 60 % de las pantallas de la misión anterior. Solo cambia lo necesario.
Uso: python tools/clase/variar_repetidas.py leng1 ciud1 ...   (prefijo de la materia)   [--probar: no guarda, solo muestra]"""
import copy, glob, json, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); LEC = os.path.join(AQUI, 'lecciones')
sys.path.insert(0, AQUI)
import variar
NEU = {'pregunta', 'resumen', 'errores', 'definicion', 'reto', 'noticia', 'gancho', 'historia', 'chat', 'portada', 'frase', 'consejo'}
def S(es): return {e.get('t') for e in es if e.get('t') not in NEU}

def candidatos(slug, es, k):
    """formas alternativas de la escena k (misma cantidad de frases de voz)"""
    e = es[k]; t = e.get('t'); v = e.get('voz') or []; out = []
    if 'neutro' in e: return out  # escenas con versión neutra propia: no se tocan
    if t == 'tabla' and len(e.get('columnas') or []) == 2 and len(v) == len(e['filas']) + 1 and all(len(f) == 2 for f in e['filas']):
        f = e['filas']
        if 2 <= len(f) <= 5 and all(len(str(a)) <= 28 and len(str(b)) <= 28 for a, b in f): out.append({'t': 'unir', 'titulo': e['titulo'], 'pares': [[str(a), str(b)] for a, b in f], 'mezclar': False, 'voz': v})
        if 2 <= len(f) <= 5: out.append({'t': 'bloques', 'titulo': e['titulo'], 'items': [{'cab': str(a).upper(), 'txt': str(b)} for a, b in f], 'voz': v})
        if len(f) == 4: out.append({'t': 'matriz', 'titulo': e['titulo'], 'celdas': [{'cab': str(a).upper(), 'txt': str(b)} for a, b in f], 'voz': v})
    if t == 'pregunta' and isinstance(e.get('opciones'), list) and 2 <= len(e['opciones']) <= 4 and len(v) == 3 and all(len(str(o)) <= 34 for o in e['opciones']):
        tmp = copy.deepcopy({'slug': slug, 'escenas': es}); variar.preparar(tmp); q = tmp['escenas'][k]  # mismo orden y misma frase que ya tiene voz grabada
        if isinstance(q.get('correcta'), int): out.append({'t': 'quiz4', 'pregunta': q['pregunta'], 'opciones': q['opciones'], 'correcta': q['correcta'], 'voz': q['voz']})
    if t == 'definicion' and len(v) == 2 and len(str(e.get('texto', ''))) <= 60 and len(str(e.get('palabra', ''))) <= 30:
        out.append({'t': 'pizarra', 'lineas': [{'txt': e['palabra'], 'color': 'sol', 'marca': 'subraya'}, {'txt': e['texto']}], 'voz': v})
    if t == 'pasos' and 2 <= len(e.get('items') or []) <= 5 and len(v) == len(e['items']) + 1:
        tx = [x['txt'] if isinstance(x, dict) else x for x in e['items']]
        out.append({'t': 'bloques', 'titulo': e['titulo'], 'items': [{'cab': f'PASO {i + 1}', 'txt': s} for i, s in enumerate(tx)], 'voz': v})
    if t == 'clasificar' and 2 <= len(e.get('cajas') or []) <= 4 and len(v) == len(e['cajas']) + 1:
        its = [{'cab': c['cab'], 'txt': ', '.join(f['txt'] for f in e['fichas'] if f.get('caja') == i)} for i, c in enumerate(e['cajas'])]
        if all(i['txt'] for i in its): out.append({'t': 'bloques', 'titulo': 'CÓMO SE CLASIFICA', 'items': its, 'voz': v})
        if len(e['cajas']) == 2 and all(i['txt'] for i in its) and False: pass
    if t == 'errores' and 1 <= len(e.get('items') or []) <= 3 and len(v) == len(e['items']) + 1:
        out.append({'t': 'corrige', 'titulo': 'ERRORES TÍPICOS', 'cambios': [{'antes': i['mal'], 'despues': i['bien'], 'motivo': ''} for i in e['items']], 'voz': v})
    if t == 'bloques' and len(e.get('items') or []) == 4 and len(v) == 5:
        out.append({'t': 'matriz', 'titulo': e['titulo'], 'celdas': e['items'], 'voz': v})
    if t == 'matriz' and len(v) == len(e.get('celdas') or []) + 1:
        out.append({'t': 'bloques', 'titulo': e['titulo'], 'items': e['celdas'], 'voz': v})
    if t == 'pregunta' and isinstance(e.get('opciones'), list) and '___' in str(e.get('pregunta', '')) and str(e['pregunta']).count('___') == 1 and len(v) == 3:
        tmp = copy.deepcopy({'slug': slug, 'escenas': es}); variar.preparar(tmp); q = tmp['escenas'][k]; a, b = str(q['pregunta']).split('___')
        if isinstance(q.get('correcta'), int) and all(len(str(o)) <= 22 for o in q['opciones']) and len(a) + len(b) <= 40: out.append({'t': 'completa', 'antes': a.strip(), 'despues': b.strip(), 'opciones': q['opciones'], 'correcta': q['correcta'], 'voz': q['voz']})
    if t == 'bloques' and 2 <= len(e.get('items') or []) <= 5 and len(v) == len(e['items']) + 1:
        out.append({'t': 'tabla', 'titulo': e['titulo'], 'columnas': ['', ''], 'filas': [[i['cab'], i['txt']] for i in e['items']], 'voz': v})
        out.append({'t': 'pasos', 'titulo': e['titulo'], 'items': [i['cab'].capitalize() + ': ' + i['txt'] for i in e['items']], 'voz': v})
    if t == 'causas' and 2 <= len(e.get('items') or []) <= 4 and len(v) == len(e['items']) + 1:
        out.append({'t': 'bloques', 'titulo': str(e['causa']['txt']).upper(), 'items': [{'cab': f'EFECTO {i + 1}', 'txt': x['txt']} for i, x in enumerate(e['items'])], 'voz': v})
    if t == 'linea' and 2 <= len(e.get('eventos') or []) <= 5 and len(v) == len(e['eventos']):
        out.append({'t': 'flujo', 'titulo': e['titulo'], 'items': [{'txt': f"{x['fecha']}: {x['txt']}", 'emoji': x.get('emoji') or '🔹'} for x in e['eventos']], 'voz': v})
    if t == 'flujo' and 2 <= len(e.get('items') or []) <= 5 and len(v) == len(e['items']):
        out.append({'t': 'linea', 'titulo': e['titulo'], 'eventos': [{'fecha': str(i + 1), 'txt': x['txt'] if isinstance(x, dict) else x, 'emoji': (x.get('emoji') if isinstance(x, dict) else None) or '🔹'} for i, x in enumerate(e['items'])], 'voz': v})
    if t == 'ciclo' and 3 <= len(e.get('items') or []) <= 5 and len(v) == len(e['items']) + 1:
        out.append({'t': 'bloques', 'titulo': e['titulo'], 'items': [{'cab': f'ETAPA {i + 1}', 'txt': x['txt'] if isinstance(x, dict) else x} for i, x in enumerate(e['items'])], 'voz': v})
    if t == 'tarjetas' and len(v) == len(e.get('items') or []):
        out.append({'t': 'vocab', 'items': [{'palabra': i['en'], 'emoji': i.get('emoji') or '🔹', 'trad': i['es']} for i in e['items']], 'voz': v})
    if t == 'vocab' and 1 <= len(e.get('items') or []) <= 4 and len(v) == len(e['items']):
        out.append({'t': 'tarjetas', 'titulo': 'VOCABULARIO', 'items': [{'en': i['palabra'], 'es': i.get('trad', ''), **({'emoji': i['emoji']} if i.get('emoji') else {})} for i in e['items']], 'voz': v})
    if t == 'dato' and len(v) == 2 and str(e.get('numero', '')).replace('.', '').isdigit():
        out.append({'t': 'datoloco', 'texto': e.get('texto', ''), 'emoji': e.get('emoji') or '💡', 'numero': int(str(e['numero']).replace('.', '')), **({'unidad': e['despues']} if e.get('despues') and len(str(e['despues'])) <= 12 else {}), 'voz': v})
    return out

def cargar(pref):
    M = {}
    for f in glob.glob(os.path.join(LEC, pref + '-m*-n*.json')):
        m = re.match(r'.*-m(\d+)-n(\d+)\.json$', f)
        if m and not f.endswith('.neutro.json'): M.setdefault(int(m.group(1)), {})[int(m.group(2))] = (f, json.load(open(f, encoding='utf-8')))
    return M

def mal_pares(cl):
    ns = sorted(cl); out = []
    for i in range(len(ns)):
        for j in range(i + 1, len(ns)):
            A, B = S(cl[ns[i]][1]['escenas']), S(cl[ns[j]][1]['escenas'])
            if A and B and len(A & B) > .5 * min(len(A), len(B)): out.append((ns[i], ns[j], A & B))
    return out

def uso(cl, t): return sum(1 for n in cl if t in {e.get('t') for e in cl[n][1]['escenas']})

def aplicar(pref, cl, n, k, nuevo, log):
    f, L = cl[n]; viejo = L['escenas'][k]['t']; L['escenas'][k] = nuevo
    log.append(f'{pref}-n{n} escena {k}: {viejo} -> {nuevo["t"]}')

def arreglar(pref, cl, prev, log):
    cambiado = set()
    def probar(n, tipos_malos, evitar):
        """cambia una escena de la clase n cuyo tipo esté en tipos_malos por una forma que no esté en evitar"""
        L = cl[n][1]; es = L['escenas']; slug = os.path.basename(cl[n][0])[:-5]
        for k, e in enumerate(es):
            if e.get('t') not in tipos_malos: continue
            for c in candidatos(slug, es, k):
                if c['t'] in evitar or uso(cl, c['t']) >= 3: continue
                aplicar(pref, cl, n, k, c, log); cambiado.add(n); return True
        return False
    # 1) dentro de la misión
    for _ in range(12):
        mp = mal_pares(cl)
        if not mp: break
        a, b, comp = mp[0]
        otras = S(cl[a][1]['escenas'])
        if not (probar(b, comp, otras) or probar(a, comp, S(cl[b][1]['escenas'])) or probar(b, comp | NEU, otras)): break
    # 2) respecto de la misión anterior
    if prev:
        for _ in range(12):
            U = set().union(*[S(cl[n][1]['escenas']) for n in cl])
            if not U or len(U & prev) <= .6 * len(U): break
            hecho = False
            for n in sorted(cl):
                todas = set().union(*[S(cl[m][1]['escenas']) for m in cl if m != n])
                if probar(n, (U & prev) | {'pregunta', 'definicion', 'errores'}, prev | todas): hecho = True; break
            if not hecho:
                for n in sorted(cl):
                    if probar(n, (U & prev) | {'pregunta', 'definicion', 'errores'}, prev): hecho = True; break
            if not hecho: break
    # no dejar dos clases con la misma secuencia
    return cambiado

def main(pref, guardar):
    M = cargar(pref); log = []; total = set(); prev = None
    for m in sorted(M):
        cl = M[m]; c = arreglar(f'{pref}-m{m}', cl, prev, log); total |= {(m, n) for n in c}
        if guardar:
            for n in c: json.dump(cl[n][1], open(cl[n][0], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        prev = set().union(*[S(cl[n][1]['escenas']) for n in cl])
    for l in log: print(l)
    print(f'{pref}: {len(total)} clases modificadas, {len(log)} escenas cambiadas')

if __name__ == '__main__':
    g = '--probar' not in sys.argv
    for p in [a for a in sys.argv[1:] if not a.startswith('--')]: main(p, g)
