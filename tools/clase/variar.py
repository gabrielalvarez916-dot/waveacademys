# Variaciones automáticas que se aplican igual al armar la clase y al grabar la voz (para que coincidan).
# - Preguntas: la respuesta correcta no puede quedar siempre en la A. Se la ubica en una posición fija
#   según la clase y la escena (A, B o C), y si la segunda frase de la voz era "¿opción, opción u opción?",
#   se rearma en el orden nuevo.
import hashlib, re

def _lista(ops):
    ops = [re.sub(r'\s+', ' ', o).strip() for o in ops]
    def m(o): return o[0].lower() + o[1:] if o and o[0].isupper() and not o[:2].isupper() else o
    if len(ops) == 2: return '¿' + m(ops[0]) + ', o ' + m(ops[1]) + '?'
    return '¿' + ', '.join(m(o) for o in ops[:-1]) + ', o ' + m(ops[-1]) + '?'

def preparar(L):
    slug = L.get('slug', '')
    for k, e in enumerate(L.get('escenas', [])):
        if e.get('t') != 'pregunta' or e.get('fija') or not isinstance(e.get('opciones'), list): continue
        ops, c = e['opciones'], e.get('correcta', 0)
        if isinstance(c, str):
            if c.strip().isdigit(): c = int(c)
            elif c in ops: c = ops.index(c)
            else: continue
            if not isinstance(e.get('correcta'), int): continue  # formato viejo: no se toca
        n = len(ops)
        if n < 2 or not (0 <= c < n): continue
        dest = int(hashlib.md5(f'{slug}:{k}'.encode()).hexdigest(), 16) % n
        if dest == c: continue
        nuevo = ops[:c] + ops[c + 1:]
        nuevo.insert(dest, ops[c])
        e['opciones'], e['correcta'] = nuevo, dest
        v = e.get('voz') or []
        # rearmar la frase que enumera las opciones, solo si las nombra todas y son texto sin símbolos
        ORD = {0: ('primera', 'primero'), 1: ('segunda', 'segundo'), 2: ('tercera', 'tercero'), 3: ('cuarta', 'cuarto')}
        for i in range(2, len(v)):
            v[i] = re.sub(r'\b(L|l)a (primera|segunda|tercera|cuarta)\b(?! persona| misi| vez| parte)', lambda m: m.group(1) + 'a ' + ORD[dest][0], v[i])
            v[i] = re.sub(r'\b(E|e)l (primero|segundo|tercero|cuarto)\b(?! paso)', lambda m: m.group(1) + 'l ' + ORD[dest][1], v[i])
        if len(v) > 1 and all(not re.search(r'[0-9×⁰¹²³⁴⁵⁶⁷⁸⁹⁻—"«]', o) for o in ops):
            low = v[1].lower()
            if sum(1 for o in ops if o.lower()[:12] in low) >= n - 1:
                v[1] = _lista(nuevo)
    return L
