# -*- coding: utf-8 -*-
"""Agrega escenas que ENSEÑAN a una clase animada ya hecha, usando el PDF de la MISMA lección (misión + nivel).
Nunca borra ni cambia escenas existentes: inserta las nuevas justo antes de la primera pregunta.
Uso: python tools/clase/enriquecer.py leng2-m6-n1 [slug ...]   (escribe en tools/clase/lecciones/; revertible con git)
Escenas que arma (en este orden, hasta el tope): definición del concepto central -> ejemplo resuelto (pasos) -> consejo -> error típico.
Reglas: solo entra lo relacionado con la clase (título, preguntas, resumen); si la clase ya enseña, no se toca."""
import json, os, re, sys, glob
AQUI = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, 'tools')); sys.path.insert(0, AQUI)
import control_calidad as C
ENS = {'definicion', 'comparar', 'pasos', 'tabla', 'flujo', 'causas', 'ecuacion', 'antesdespues', 'bloques', 'ciclo', 'partes', 'venn', 'balanza', 'recta', 'texto', 'zoom', 'pizarra',
       'chat', 'geo', 'vocab', 'fichas', 'tren', 'linea', 'saltos', 'frase', 'errores', 'matriz', 'consejo'}
TOPE = {'avanzado': 5, 'medio': 3, 'primeros': 3}           # escenas nuevas como máximo
ESC_MAX = {'avanzado': 11, 'medio': 8, 'primeros': 8}        # escenas totales de la clase como máximo
NUM = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']

def plano(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', str(s or ''))).strip()
def voz(s): return re.sub(r'\s+', ' ', re.sub(r'</?b>', '*', re.sub(r'<(?!/?b>)[^>]+>', '', str(s or '')))).strip()
def vz(e):
    v = e.get('voz'); return ' '.join(v) if isinstance(v, list) else str(v or '')
def primera_oracion(s, tope=130):
    s = plano(s); m = re.match(r'(.{20,%d}?[.!?])(\s|$)' % tope, s)
    return m.group(1) if m else s[:tope]
def pal(s): return {w for w in C.norm_t(plano(s)).split() if len(w) > 3 and w not in C.STOP}

def escenas_de(N, L):
    """Escenas candidatas a partir del contenido del PDF, relacionadas con lo que la clase ya dice."""
    E = L['escenas']; tema = pal(' '.join([L.get('titulo', '')] + [vz(e) for e in E] + [str(e.get('pregunta', '')) + ' '.join(map(str, e.get('opciones', []))) for e in E]))
    out = []
    # 1) definición: el concepto del PDF más relacionado con la clase
    defs = []
    for s in N.get('secciones') or []:
        for b in s.get('bloques') or []:
            if b.get('tipo') == 'definicion' and b.get('titulo') and b.get('texto'):
                rel = len(pal(b['titulo']) & tema) / max(1, len(pal(b['titulo'])))
                if rel > 0: defs.append((rel, b))
    for _, b in sorted(defs, key=lambda x: -x[0])[:2]:
        t = primera_oracion(b['texto']); v = primera_oracion(voz(b['texto']), 170)
        out.append(('definicion', {'t': 'definicion', 'palabra': plano(b['titulo']), 'texto': t, 'emoji': '📘', 'voz': [f'Veamos *{plano(b["titulo"])}*.', v]}))
    # 2) ejemplo resuelto
    ec = N.get('ejemplo_completo') or {}
    pasos = [plano(p) for p in ec.get('pasos') or []]
    if 3 <= len(pasos) <= 5:
        out.append(('pasos', {'t': 'pasos', 'titulo': plano(ec.get('titulo', 'Ejemplo')).upper(), 'items': [{'txt': p, 'emoji': NUM[i]} for i, p in enumerate(pasos)],
                              'voz': ['Resolvamos un caso: ' + voz(ec.get('planteo', '')) ] + [voz(p) for p in pasos]}))
    # 3) consejo
    tip = N.get('tip') or {}
    if tip.get('texto'):
        out.append(('consejo', {'t': 'consejo', 'texto': plano(tip['texto']), 'emoji': '💡', 'voz': [f'Un consejo: {voz(tip["texto"])}']}))
    # 4) error típico: solo si hay una consigna de tipo error con respuesta para decir el "bien"
    ojo = [plano(x) for x in N.get('ojo') or []]; tags = [str(x).lower() for x in N.get('carpeta_nivel') or []]; sol = (N.get('soluciones') or {}).get('carpeta') or []
    items = []
    for i, tg in enumerate(tags):
        if tg == 'error' and i < len(sol) and i < len(N.get('carpeta') or []):
            cons = plano((N['carpeta'][i] if isinstance(N['carpeta'][i], str) else N['carpeta'][i].get('consigna', '')))
            m = max(ojo, key=lambda o: len(pal(o) & pal(cons)), default=None)
            if m and len(pal(m) & pal(cons)) >= 1: items.append({'mal': m.rstrip('.'), 'bien': 'Lo correcto: ' + plano(sol[i]).rstrip('.')})
    if items:
        out.append(('errores', {'t': 'errores', 'items': items, 'voz': ['Errores típicos.'] + [f'Ojo: {i["mal"]}. {i["bien"]}.' for i in items]}))
    return out

def enriquecer(slug, M, N, L, nivel):
    E = L['escenas']
    if len(E) >= ESC_MAX[nivel]: return 0, 'ya tiene el tope de escenas'
    ya = {e.get('t') for e in E}
    nuevas = [s for t, s in escenas_de(N, L) if t not in ya or t in ('definicion',) and s['palabra'].lower() not in ' '.join(vz(e).lower() for e in E)]
    nuevas = nuevas[:min(TOPE[nivel], ESC_MAX[nivel] - len(E))]
    if not nuevas: return 0, 'el PDF no aporta nada relacionado'
    k = next((i for i, e in enumerate(E) if e.get('t') == 'pregunta'), len(E) - 1)
    L['escenas'] = E[:k] + nuevas + E[k:]
    return len(nuevas), 'ok'

def main(slugs):
    idx = {}
    for p in glob.glob(os.path.join(RAIZ, 'contenido', '**', 'mision-*.json'), recursive=True):
        try: M = json.load(open(p, encoding='utf-8'))
        except Exception: continue
        nivel = C.tipo_nivel(p, M)
        for pc, L in C._clases_de(p, M)[1]: idx[L['slug']] = (p, M, pc, nivel)
    for s in slugs:
        if s not in idx: print(s, '→ no encontré su PDF'); continue
        p, M, pc, nivel = idx[s]; L = json.load(open(pc, encoding='utf-8')); n = int(re.search(r'-n(\d)$', s).group(1))
        N = (M.get('niveles') or {}).get(str(n)); antes = len(L['escenas'])
        k, msg = enriquecer(s, M, N, L, nivel) if N else (0, 'sin nivel en el PDF')
        if k: json.dump(L, open(pc, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'{s}: {antes} → {len(L["escenas"])} escenas ({msg})')

if __name__ == '__main__': main(sys.argv[1:])
