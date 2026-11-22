# -*- coding: utf-8 -*-
# MÁQUINA DEL NIVEL MEDIO · diccionario neutro PROPIO (copia independiente de tools/neutro.py del Avanzado, que no se toca).
# Las palabras nuevas del Medio se suman acá (MAPA si es voseo, OK si no lo es).
# -*- coding: utf-8 -*-
"""Voseo rioplatense -> español neutro latinoamericano (tuteo), con diccionario cerrado.
Lo usan tools/medio/clase (armar.py, voz_edge.py, revisar_contenido.py) y tools/medio/pdf para producir la versión neutra.
- neutro(texto): convierte un texto.
- convertir(obj): convierte todos los textos de una lección o de un contenido de PDF (no toca ids, colores, emojis, imágenes).
- revisar(obj): lista palabras que parecen voseo y no están en el diccionario (el control avisa antes de subir).
Para sumar una forma nueva: agregarla a MAPA (si es voseo) o a OK (si no lo es)."""
import re

MAPA = {
 # imperativos y presentes de voseo -> tuteo
 'abrí': 'abre', 'abrís': 'abres', 'acabás': 'acabas', 'acercás': 'acercas', 'acordate': 'acuérdate', 'acordás': 'acuerdas',
 'agregá': 'agrega', 'agregás': 'agregas', 'agrupá': 'agrupa', 'agrupás': 'agrupas', 'ajustás': 'ajustas', 'analizá': 'analiza', 'anotá': 'anota',
 'anotalo': 'anótalo', 'aplicá': 'aplica', 'aplicás': 'aplicas', 'apoyá': 'apoya', 'aprendés': 'aprendes', 'armá': 'arma', 'armás': 'armas',
 'arrancás': 'arrancas', 'arrancá': 'arranca', 'asocialos': 'asócialos', 'avanzás': 'avanzas', 'averiguá': 'averigua', 'avisale': 'avísale',
 'buscá': 'busca', 'buscás': 'buscas', 'calculalas': 'calcúlalas', 'calculalo': 'calcúlalo', 'calculá': 'calcula', 'calculás': 'calculas',
 'cambiá': 'cambia', 'cambiás': 'cambias', 'canjeás': 'canjeas', 'cazás': 'cazas', 'cerrá': 'cierra', 'cerrás': 'cierras', 'chequeá': 'revisa',
 'clasificalo': 'clasifícalo', 'clasificá': 'clasifica', 'comparalas': 'compáralas', 'compará': 'compara', 'comparás': 'comparas',
 'compensá': 'compensa', 'completá': 'completa', 'comprobala': 'compruébala', 'comprobalo': 'compruébalo', 'comprobá': 'comprueba',
 'comprobás': 'compruebas', 'comprás': 'compras', 'comés': 'comes', 'concluí': 'concluye', 'conjugá': 'conjuga', 'conocés': 'conoces',
 'contalo': 'cuéntalo', 'contalos': 'cuéntalos', 'contame': 'cuéntame', 'controlá': 'controla', 'contá': 'cuenta', 'contás': 'cuentas',
 'convertís': 'conviertes', 'copiá': 'copia', 'copiás': 'copias', 'corregí': 'corrige', 'corregís': 'corriges', 'corré': 'corre', 'cruzás': 'cruzas',
 'creés': 'crees', 'debés': 'debes', 'decidí': 'decide', 'decidís': 'decides', 'decí': 'di', 'decime': 'dime', 'decís': 'dices', 'dedicale': 'dedícale',
 'deducís': 'deduces', 'dejás': 'dejas', 'dejá': 'deja', 'depositás': 'depositas', 'desarmás': 'desarmas', 'descomponé': 'descompón',
 'desconfiá': 'desconfía', 'describí': 'describe', 'deshacés': 'deshaces', 'deslizala': 'deslízala', 'deslizá': 'desliza', 'detectás': 'detectas',
 'devolvés': 'devuelves', 'dibujá': 'dibuja', 'dibujás': 'dibujas', 'distribuí': 'distribuye', 'dividí': 'divide', 'dividís': 'divides', 'dudás': 'dudas',
 'duplicás': 'duplicas', 'dá': 'da', 'elegí': 'elige', 'elegís': 'eliges', 'elevá': 'eleva', 'elevás': 'elevas', 'empezá': 'empieza', 'empezás': 'empiezas',
 'encontrá': 'encuentra', 'encontrás': 'encuentras', 'entregalas': 'entrégalas', 'entregalo': 'entrégalo', 'entregá': 'entrega', 'entregás': 'entregas',
 'entrás': 'entras', 'escondé': 'esconde', 'escribila': 'escríbela', 'escribilo': 'escríbelo', 'escribí': 'escribe', 'escribís': 'escribes',
 'estimá': 'estima', 'estimás': 'estimas', 'evitá': 'evita', 'expandí': 'expande', 'explicá': 'explica', 'fijate': 'fíjate', 'formás': 'formas',
 'hacé': 'haz', 'hacés': 'haces', 'hallás': 'hallas', 'identificá': 'identifica', 'imaginá': 'imagina', 'imaginate': 'imagínate', 'inferís': 'infieres',
 'interpretá': 'interpreta', 'inventá': 'inventa', 'juntá': 'junta', 'juntás': 'juntas', 'justificá': 'justifica', 'lastimás': 'lastimas',
 'leelo': 'léelo', 'leé': 'lee', 'leés': 'lees', 'listá': 'enumera', 'llegás': 'llegas', 'mandame': 'mándame', 'mantené': 'mantén', 'marcá': 'marca',
 'marcás': 'marcas', 'medí': 'mide', 'medís': 'mides', 'mirá': 'mira', 'mirás': 'miras', 'mostrá': 'muestra', 'mostrás': 'muestras', 'mové': 'mueve',
 'muestrales': 'muéstrales', 'multiplicá': 'multiplica', 'multiplicás': 'multiplicas', 'necesitás': 'necesitas', 'nombrá': 'nombra',
 'observá': 'observa', 'olvidás': 'olvidas', 'ordená': 'ordena', 'pagás': 'pagas', 'partilo': 'pártelo', 'partí': 'parte', 'partís': 'partes',
 'pará': 'para', 'pasalo': 'pásalo', 'pasá': 'pasa', 'pedile': 'pídele', 'pedís': 'pides', 'pensalo': 'piénsalo', 'pensá': 'piensa', 'pensás': 'piensas',
 'pintás': 'pintas', 'planificá': 'planifica', 'planteá': 'plantea', 'podés': 'puedes', 'poné': 'pon', 'ponés': 'pones', 'practicá': 'practica',
 'practicás': 'practicas', 'preguntale': 'pregúntale', 'preguntate': 'pregúntate', 'preguntá': 'pregunta', 'probá': 'prueba', 'probás': 'pruebas',
 'prolongás': 'prolongas', 'protegé': 'protege', 'quedás': 'quedas', 'querés': 'quieres', 'quitás': 'quitas', 'recibís': 'recibes',
 'recomendame': 'recomiéndame', 'recordá': 'recuerda', 'recordás': 'recuerdas', 'recorré': 'recorre', 'recortás': 'recortas', 'redondeá': 'redondea',
 'redondeás': 'redondeas', 'reemplazá': 'reemplaza', 'reemplazás': 'reemplazas', 'reescribí': 'reescribe', 'releé': 'relee', 'repartí': 'reparte',
 'repartís': 'repartes', 'repasá': 'repasa', 'resolvé': 'resuelve', 'resolvés': 'resuelves', 'respondé': 'responde', 'restale': 'réstale',
 'restá': 'resta', 'restás': 'restas', 'revisá': 'revisa', 'sabés': 'sabes', 'sacás': 'sacas', 'salteás': 'saltas', 'seguí': 'sigue', 'señalá': 'señala',
 'simplificá': 'simplifica', 'subrayá': 'subraya', 'subí': 'sube', 'subís': 'subes', 'sumale': 'súmale', 'sumá': 'suma', 'sumás': 'sumas',
 'tachás': 'tachas', 'tapá': 'tapa', 'tené': 'ten', 'tenés': 'tienes', 'tipealos': 'escríbelos', 'tipeá': 'escribe', 'tipeás': 'escribes', 'tirás': 'tiras',
 'tocá': 'toca', 'tomá': 'toma', 'traducí': 'traduce', 'transpirás': 'sudas', 'trasladás': 'trasladas', 'trazá': 'traza', 'trazás': 'trazas',
 'ubicá': 'ubica', 'uní': 'une', 'unís': 'unes', 'usá': 'usa', 'usás': 'usas', 'verificá': 'verifica', 'verificás': 'verificas', 'volvé': 'vuelve',
 'vivís': 'vives', 'viví': 'vive', 'vení': 'ven', 'venís': 'vienes', 'sentís': 'sientes', 'jugás': 'juegas', 'jugá': 'juega', 'entendés': 'entiendes',
 'tomás': 'tomas', 'guardás': 'guardas', 'sos': 'eres', 'vos': 'tú', 'acá': 'aquí',
 # palabras rioplatenses
 'campera': 'chaqueta', 'camperas': 'chaquetas', 'ojotas': 'sandalias', 'remera': 'camiseta', 'remeras': 'camisetas', 'pileta': 'piscina',
 'heladera': 'refrigerador', 'frutilla': 'fresa', 'frutillas': 'fresas', 'manteca': 'mantequilla', 'hacelo': 'hazlo', 'completalo': 'complétalo', 'resolvelo': 'resuélvelo', 'comparala': 'compárala', 'comparalo': 'compáralo', 'abonás': 'abonas', 'conocé': 'conoce', 'guardá': 'guarda', 'hablá': 'habla', 'intentá': 'intenta', 'programá': 'programa', 'superá': 'supera', 'terminá': 'termina', 'terminás': 'terminas', 'elegilo': 'elígelo', 'preguntame': 'pregúntame', 'dale': 'vamos', 'che': 'oye',
}
FRASES = [(r'\bcon vos\b', 'contigo'), (r'\b(a|para|de|por) vos\b', r'\1 ti')]
OK = set('''abuela abuelo además allá allí ahí así atrás billete busqué caminé canadá capitales caramelos chile chocolate cocinaré cociné comerciales
compás comí corchete corrí culturales dé demás después detrás decimales diagonales diecisiete digitales dársela elo eme encontré equivale escala escalas
escuela especiales está estás esté estudié fila gemelos glaciales granos habrá hielo huele huelo humanos iguales internacionales interés intervalo
intervalos jacarandás kilo leí limite llame llegué límite mala manos mate materiales meridianos mete minerales miré modelos mundiales más mí naturales
nile novela novelas océanos ojalá omite orales originales pagué papá paquete paralela paralelas paralelo paralelos paraná parcela parcelas pastizales
país pasará pelo penales perdí permite pesame principales proporcionales puntuales qué quizás racionales reales regionales regué repite rete revés
romanos sabérselos sale sé será señales siete sí sociales subsuelo subsuelos suele suelo suelos tala tela temporales terminé titila tomate totales
tradicionales tropicales té vale vegetales veintisiete veintitrés vela venezuela veranos verbales vitales vuela yaguareté zócalo órganos apela
animales estará guardé quedé clásica mamá jamás perú bebé café panamá bogotá josé maní aquí allá ahí sofá bambú menú también sabés'''.split()) - set(MAPA)

PAL = re.compile(r"[A-Za-zÁÉÍÓÚáéíóúñÑüÜ]+")
SOSPECHA = re.compile(r'(ás|és|ís|á|é|í)$|^(vos|sos)$|[^aeiouáéíóú](ate|ame|alo|ala|alos|alas|ale|ales|elo|ela|ele|ilo|ila|ile)$')


def _caso(orig, nuevo):
    if orig.isupper() and len(orig) > 1: return nuevo.upper()
    return nuevo[0].upper() + nuevo[1:] if orig[0].isupper() else nuevo


def neutro(s):
    if not isinstance(s, str) or not s: return s
    for a, b in FRASES: s = re.sub(a, b, s)
    s = re.sub(r'\b(Con|A|Para|De|Por) vos\b', lambda m: 'Contigo' if m.group(1) == 'Con' else m.group(1) + ' ti', s)
    s = re.sub(r'\bpará\b(?=\s+(?:que|el|la|los|las|un|una)\b)', 'para', s)  # "pará" imperativo vs. error de tipeo de "para"
    return PAL.sub(lambda m: _caso(m.group(0), MAPA[m.group(0).lower()]) if m.group(0).lower() in MAPA and not (m.group(0) == 'Tomás') else m.group(0), s)


NO_TOCAR = {'t', 'slug', 'step_id', 'subject_id', 'emoji', 'final', 'color', 'zona', 'resaltar', 'tipo', 'id', 'png', 'png_base64', 'img', 'imagen', 'archivo', 'src',
            'b64', 'voz_id', 'lugar', 'icono', 'materia'}


def convertir(o, clave=None):
    """Versión neutra. En las misiones VARIANTE, cualquier bloque puede traer "neutro": {...} con lo que cambia para
    alumnos de otros países (se escribe ya en neutro); acá reemplaza a lo argentino."""
    if isinstance(o, str):
        return o if clave in NO_TOCAR or o.startswith('data:') or (len(o) > 3000 and ' ' not in o[:200]) else neutro(o)
    if isinstance(o, list): return [convertir(x, clave) for x in o]
    if isinstance(o, dict):
        r = {k: convertir(v, k) for k, v in o.items() if k != 'neutro'}
        if isinstance(o.get('neutro'), dict): r.update(convertir(o['neutro']))
        return r
    return o


def argentino(o):
    """Versión argentina: se sacan los bloques "neutro"."""
    if isinstance(o, list): return [argentino(x) for x in o]
    if isinstance(o, dict): return {k: argentino(v) for k, v in o.items() if k != 'neutro'}
    return o


def tiene_neutro(o):
    if isinstance(o, list): return any(tiene_neutro(x) for x in o)
    if isinstance(o, dict): return 'neutro' in o or any(tiene_neutro(v) for v in o.values())
    return False


def textos(o, clave=None):
    if isinstance(o, str):
        if not (clave in NO_TOCAR or o.startswith('data:') or (len(o) > 3000 and ' ' not in o[:200])): yield o
    elif isinstance(o, list):
        for x in o: yield from textos(x, clave)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k != 'neutro': yield from textos(v, k)


def revisar(o):
    """Palabras que parecen voseo y no están en el diccionario (ni en MAPA ni en OK)."""
    raras = set()
    for s in textos(o):
        for w in PAL.findall(s.replace('*', '')):
            lw = w.lower()
            if len(lw) > 2 and lw not in MAPA and lw not in OK and SOSPECHA.search(lw) and w != 'Tomás': raras.add(lw)
    return sorted(raras)



# ---- palabras que aparecieron en el Nivel Medio ----
MAPA.update({'igualá': 'iguala', 'igualás': 'igualas', 'quitá': 'quita', 'contalas': 'cuéntalas', 'levantá': 'levanta', 'ordenalos': 'ordénalos', 'ponelo': 'ponlo', 'seguís': 'sigues', 'saltás': 'saltas', 'volvés': 'vuelves'})
MAPA.update({'tachá': 'tacha', 'perdés': 'pierdes', 'prestás': 'prestas', 'regalás': 'regalas', 'usalos': 'úsalos', 'dalo': 'voltéalo', 'decilo': 'dilo', 'saltá': 'salta', 'escuchá': 'escucha', 'apretá': 'aprieta', 'apretás': 'aprietas', 'equivocás': 'equivocas', 'descubrí': 'descubre', 'tapalo': 'tápalo', 'seño': 'maestra'})  # Matemática 1 · Misión 9
OK |= {'regalos', 'caramelo', 'regala', 'regalo'}
OK -= set(MAPA)
