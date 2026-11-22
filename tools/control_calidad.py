# -*- coding: utf-8 -*-
"""CONTROL DE CALIDAD de una misión (Avanzado y Medio), ANTES de cargarla. Si algo no cumple, frena la carga
y explica qué arreglar. Sin IA. Reglas: docs/reglas-fijas-pdf.md (sección "Calidad de carpeta, actividades y examen").

Uso: python tools/control_calidad.py contenido/<materia>/mision-N/mision-N.json [...]
     python tools/control_calidad.py --todas      (revisa todas, sin frenar: solo informa)

Etiqueta de nivel que pide cada consigna o pregunta (obligatoria en misiones nuevas):
- carpeta: en cada nivel, "carpeta_nivel": ["recordar", "aplicar", "analizar", "error"], paralela a "carpeta".
- actividades y examen: en cada pregunta, "n": "recordar" | "aplicar" | "analizar" | "error".
  aplicar = usar lo aprendido en un caso nuevo · analizar = comparar, explicar causas, justificar ·
  error = encontrar y corregir un error típico ("un compañero dice…"). Las tres cuentan como "pensadas".
Las misiones que ya estaban en el repo al poner esta regla (tools/calidad_existentes.txt) no se revisan."""
import json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, 'medio'))
try:
    from primeros_anios import es_primeros
except Exception:
    def es_primeros(materia=None, subject_id=None, contenido=None): return False

NIVELES = {'recordar', 'aplicar', 'analizar', 'error'}
PENSADAS = {'aplicar', 'analizar', 'error'}
CON_IA = {'open', 'solve_complete'}
ELECCION = {'multiple_choice', 'true_false'}

# Mínimos por tipo de nivel. carpeta = pensadas por nivel (PDF); act = pensadas en las actividades de los niveles 1 a 4
# (el Relámpago no cuenta: es velocidad a propósito); examen = pensadas en el banco y tope de opción múltiple + V/F.
REGLAS = {
    'avanzado': {'carpeta': 2, 'act': 3, 'examen': 5, 'eleccion_max': 0.60, 'examen_no_eleccion_pensada': 1},
    'medio':    {'carpeta': 1, 'act': 2, 'examen': 4, 'eleccion_max': 0.70, 'examen_no_eleccion_pensada': 1},
    'primeros': {'carpeta': 1, 'act': 2, 'examen': 3, 'eleccion_max': 0.80, 'examen_no_eleccion_pensada': 0},
}

# Consignas que piden solo recordar: no pueden ir etiquetadas como pensadas.
MEMORIA = re.compile(r'^\W*(¿\s*)?(c[oó]mo se llama|c[oó]mo se llaman|qu[eé] (es|son|se llama)\b|cu[aá]l es el nombre|c[oó]mo se denomina)'
                     r'|respond[eé] (s[ií] o no|solo s[ií] o no)', re.I)
# Distractores de relleno: se descartan solos y regalan la respuesta.
RELLENO = re.compile(r'^\W*(todas las anteriores|ninguna de las anteriores|no s[eé]|cualquiera|agua sucia|son lindas?|no importa|nada que ver)\W*$', re.I)
ABSOLUTOS = re.compile(r'^\W*(nada|nunca|ninguno|ninguna|siempre|solo en .+|nadie)\W*$', re.I)

def norm(s): return re.sub(r'\s+', ' ', re.sub(r'[^\wñáéíóúü%° ]', ' ', str(s).lower())).strip()

def existentes():
    ruta = os.path.join(AQUI, 'calidad_existentes.txt')
    if not os.path.exists(ruta): return set()
    return {l.strip() for l in open(ruta, encoding='utf-8') if l.strip() and not l.startswith('#')}

def tipo_nivel(ruta, M):
    if '/medio/' in ruta.replace('\\', '/'):
        return 'primeros' if es_primeros(subject_id=M.get('subject_id'), contenido=M) or M.get('estilo') == 'primeros' else 'medio'
    return 'avanzado'

def revisar_pregunta(q, donde, nivel, err, avi):
    t = q.get('t'); p = str(q.get('p') or ''); o = q.get('o'); r = q.get('r') or {}
    n = str(q.get('n') or '').lower().strip()
    if n not in NIVELES: err.append(f'{donde}: falta "n" (recordar, aplicar, analizar o error)')
    if t in CON_IA: err.append(f'{donde}: tipo "{t}" llama a la IA; usá keywords, short_answer o numeric (sin IA)')
    if n in PENSADAS and MEMORIA.search(p): err.append(f'{donde}: está como "{n}" pero pide recordar un nombre o un sí/no: «{p[:70]}»')
    if t in ('multiple_choice', 'multi_select', 'odd_one_out') and isinstance(o, list):
        ops = [str(x) for x in o]
        if len({norm(x) for x in ops}) < len(ops): err.append(f'{donde}: opciones repetidas')
        if nivel != 'primeros' and t == 'multiple_choice' and len(ops) < 3 and {norm(x) for x in ops} != {'sí', 'no'}:
            err.append(f'{donde}: menos de 3 opciones')
        corr = r.get('correcta') if isinstance(r, dict) else r
        correctas = [corr] if t != 'multi_select' else list((r or {}).get('correctas') or [])
        if t == 'multiple_choice' and corr is not None and corr not in ops: err.append(f'{donde}: la correcta no está entre las opciones')
        distr = [x for x in ops if x not in correctas]
        for x in distr:
            if RELLENO.match(x): err.append(f'{donde}: distractor de relleno «{x}»: usá un error típico (lo de "ojo" del PDF)')
            elif ABSOLUTOS.match(x) and nivel != 'primeros': avi.append(f'{donde}: distractor absoluto «{x}»: suele descartarse solo')
        if t == 'multiple_choice' and corr and distr:
            largo, mayor = len(str(corr)), max(len(x) for x in distr)
            if largo > 25 and largo > 2 * mayor: err.append(f'{donde}: la correcta es mucho más larga que las demás y se delata: igualá el largo')
    return n

def revisar(ruta, forzar=False):
    M = json.load(open(ruta, encoding='utf-8'))
    nivel = tipo_nivel(ruta, M); R = REGLAS[nivel]
    err, avi = [], []
    # Carpeta de cada nivel (PDF)
    for k, N in sorted((M.get('niveles') or {}).items(), key=lambda x: int(x[0]) if str(x[0]).isdigit() else 0):
        cons = N.get('carpeta') or []; tags = [str(x).lower().strip() for x in (N.get('carpeta_nivel') or [])]
        resp = N.get('respuestas_carpeta') or []
        d = f'nivel {k} · carpeta'
        if len(tags) != len(cons): err.append(f'{d}: "carpeta_nivel" tiene que tener una etiqueta por consigna ({len(cons)})'); continue
        if any(x not in NIVELES for x in tags): err.append(f'{d}: etiqueta inválida (vale recordar, aplicar, analizar o error)')
        for i, (c, tg) in enumerate(zip(cons, tags)):
            texto = c if isinstance(c, str) else (c or {}).get('consigna', '')
            if tg in PENSADAS and MEMORIA.search(texto): err.append(f'{d} {i + 1}: está como "{tg}" pero pide recordar un nombre o un sí/no')
            acepta = resp[i] if i < len(resp) else []
            acepta = acepta if isinstance(acepta, list) else [acepta]
            if not [a for a in acepta if str(a).strip()]: err.append(f'{d} {i + 1}: sin respuesta válida en respuestas_carpeta')
            elif any(len(str(a).split()) > 6 for a in acepta): err.append(f'{d} {i + 1}: respuesta válida de más de 6 palabras: la app la compara letra por letra; reformulá para que la respuesta sea corta')
        p = sum(t in PENSADAS for t in tags)
        if p < R['carpeta']: err.append(f'{d}: {p} consigna(s) pensada(s); el mínimo es {R["carpeta"]} (caso nuevo, causa y consecuencia, comparar o error típico, con respuesta corta)')
        if nivel != 'primeros' and 'error' not in tags: avi.append(f'{d}: ninguna consigna apunta a un error típico (regla del PDF)')
    # Actividades (niveles 1 a 4; el 5 es Relámpago)
    pens = 0
    for k, lista in (M.get('act') or {}).items():
        for j, q in enumerate(lista or []):
            n = revisar_pregunta(q, f'actividad {k}.{j + 1}', nivel, err, avi)
            if str(k) != '5' and n in PENSADAS: pens += 1
    if M.get('act') and pens < R['act']: err.append(f'actividades: {pens} pensada(s) en los niveles 1 a 4; el mínimo es {R["act"]}')
    # Examen (banco del nivel jefe)
    ex = M.get('examen') or []
    if ex:
        pens = elec = no_elec_pens = 0
        for j, it in enumerate(ex):
            q = it[1] if isinstance(it, list) and len(it) > 1 else it
            n = revisar_pregunta(q, f'examen {j + 1}', nivel, err, avi)
            pens += n in PENSADAS; elec += q.get('t') in ELECCION
            no_elec_pens += (n in PENSADAS and q.get('t') not in ELECCION)
        if pens < R['examen']: err.append(f'examen: {pens} pregunta(s) pensada(s) de {len(ex)}; el mínimo es {R["examen"]}')
        if elec > R['eleccion_max'] * len(ex): err.append(f'examen: {elec} de {len(ex)} son opción múltiple o V/F; el tope es {int(R["eleccion_max"] * 100)} %')
        if no_elec_pens < R['examen_no_eleccion_pensada']: err.append('examen: falta al menos 1 pregunta pensada que no sea de elegir (keywords, numeric, short_answer, classify, ordering…)')
    return nivel, err, avi

def main():
    args = sys.argv[1:]
    informe = '--todas' in args
    if informe:
        base = os.path.join(os.path.dirname(AQUI), 'contenido')
        args = sorted(os.path.relpath(os.path.join(r, f), os.path.dirname(AQUI)) for r, _, fs in os.walk(base) for f in fs if re.fullmatch(r'mision-\d+\.json', f))
    viejas = set() if informe else existentes()
    frenar = False
    for ruta in args:
        rel = ruta.replace('\\', '/')
        if rel in viejas: print(f'{rel}: misión anterior a la regla, no se revisa'); continue
        nivel, err, avi = revisar(ruta)
        if err:
            frenar = True
            print(f'\n✗ {rel} ({nivel}): {len(err)} problema(s) — NO se carga')
            for e in err: print('   -', e)
        else:
            print(f'✓ {rel} ({nivel}): cumple la regla de calidad')
        for a in avi: print('   (aviso)', a)
    sys.exit(1 if frenar and not informe else 0)

if __name__ == '__main__':
    main()
