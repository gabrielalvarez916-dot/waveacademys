# -*- coding: utf-8 -*-
"""Voseo rioplatense -> español neutro latinoamericano (tuteo), con diccionario cerrado.
Lo usan armar.py y voz_edge.py (clases) y tools/pdf/generar.py (PDF) para producir la versión neutra de todo.
- neutro(texto): convierte un texto.
- convertir(obj): convierte todos los textos de una lección o de un contenido de PDF (no toca ids, colores, emojis, imágenes).
- revisar(obj): lista palabras que parecen voseo y no están en el diccionario (el control avisa antes de subir).
Para sumar una forma nueva: agregarla a MAPA (si es voseo) o a OK (si no lo es)."""
import re

MAPA = {'asegurate':'asegúrate','explicalo':'explícalo','andás':'andas','avisame':'avísame','bancame':'espérame','contestame':'contéstame','guardame':'guárdame','cantás':'cantas','llevá':'lleva','traé':'trae','felicitás':'felicitas','descubrís':'descubres','bajá':'baja','mantenés':'mantienes','indicá':'indica','parodiá':'parodia','satirizá':'satiriza','distinguís':'distingues','reconocés':'reconoces','concluís':'concluyes','contestás':'contestas','prestás':'prestas','votá':'vota','abrigate':'abrígate','apagá':'apaga','aclaralo':'acláralo','mandás':'mandas',
 'burlás': 'burlas', 'exagerás': 'exageras', 'abandonás': 'abandonas', 'cumplís': 'cumples', 'transformá': 'transforma',
 'comé': 'come', 'aconsejale': 'aconséjale', 'decila': 'dila', 'dormís': 'duermes', 'aconsejás': 'aconsejas', 'doblá': 'dobla', 'llamás': 'llamas', 'recomendá': 'recomienda', 'pedí': 'pide',
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
 'tachá': 'tacha', 'agachás': 'agachas', 'amasá': 'amasa', 'decoralo': 'decóralo', 'modelá': 'modela', 'ponele': 'ponle', 'transformalo': 'transfórmalo', 'acercate': 'acércate', 'describís': 'describes', 'planeás': 'planeas', 'mezclá': 'mezcla', 'probala': 'pruébala', 'pintá': 'pinta', 'dibujalo': 'dibújalo', 'oscurecé': 'oscurece', 'invertí': 'invierte', 'miralo': 'míralo', 'pasás': 'pasas', 'contrastá': 'contrasta', 'obtenés': 'obtienes', 'cociná': 'cocina', 'desparasitá': 'desparasita', 'ensayá': 'ensaya', 'evaluá': 'evalúa', 'ahorrá': 'ahorra', 'escuchás': 'escuchas', 'esperá': 'espera', 'evaluás': 'evalúas', 'respondés': 'respondes', 'reescribilo': 'reescríbelo', 'hablás': 'hablas', 'puntuá': 'puntúa', 'usalos': 'úsalos', 'variá': 'varía', 'repetís': 'repites', 'preguntás': 'preguntas', 'argumentá': 'argumenta', 'discrepá': 'discrepa', 'discrepás': 'discrepas', 'reconocé': 'reconoce', 'discutí': 'discute', 'completé': 'completé', 'definí': 'define', 'entregué': 'entregué', 'firmé': 'firmé', 'incluí': 'incluye', 'pasame': 'pásame', 'releí': 'relee', 'respetá': 'respeta', 'mostrala': 'muéstrala', 'ordenalas': 'ordénalas', 'quedate': 'quédate', 'sentí': 'sentí', 'cuidá': 'cuida', 'mejorá': 'mejora', 'olés': 'hueles', 'reemplazalas': 'reemplázalas', 'tocás': 'tocas', 'comparé': 'compara', 'defendés': 'defiendes', 'distinguí': 'distingue', 'escuchá': 'escucha', 'oís': 'oyes', 'aprendé': 'aprende', 'revisalas': 'revísalas', 'separá': 'separa', 'usala': 'úsala', 'agradecés': 'agradeces', 'explicás': 'explicas', 'resumís': 'resumes', 'resumí': 'resume', 'generalizá': 'generaliza', 'sacá': 'saca', 'perdés': 'pierdes', 'trabás': 'trabas', 'rotulá': 'rotula', 'conocelo': 'conócelo', 'esperás': 'esperas', 'presentalo': 'preséntalo', 'reuní': 'reúne', 'reunís': 'reúnes', 'detectá': 'detecta', 'presentás': 'presentas', 'proponés': 'propones',
 'actuá': 'actúa', 'proponé': 'propón', 'estudiá': 'estudia', 'mezclás': 'mezclas', 'repetí': 'repite', 'ubicás': 'ubicas',
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
OK = set('''congela bala francés usará camila caerá podrá velo morirá recordará regalos tendrá cantaré canté gramaticales anoté arreglé esperé mortales combate ponérmela revela sala animé entendí gemelo jubila pala rechacé rescate volví descortés tele empate tomé exprés olvidé desayuné inés levanté salí biogás cerré pascales pascal conocí literales aprendí while late name profile cortés estilo relé relés pila pilas emocionales moví corté hilo laterales llamé agregué armé pegué usé sobresale dejé mezclé pinté probé rotulé acuarela afiné degradé encajé horizontales marqué sumé verticales óvalo dibujé cambié legales universales centrales comité comités quitárselo constitucionales reclame vigila electorales canales ilegales tribunales mochila morales hospitales prevé modelo humedales derrame arbustales carayá corales valdés escuché respeté aprobé cansé compré debate formales informales opcionales personales finales completé entregué firmé sentí inglés señala generales vocales porqué visité malos metales yangtsé bebés mudé rurales arrozales estrés guaraní globales locales malo ambientales nacionales parís organela sales través filo yacaré abuela abuelo además allá allí ahí así atrás billete busqué caminé canadá capitales caramelos chile chocolate cocinaré cociné comerciales
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


JS = r"""/* GENERADO por tools/neutro.py --js (no editar a mano: el diccionario vive en tools/neutro.py).
   Interfaz en español neutro para alumnos de otros países: si el alumno (o todos los hijos de la familia) no es de la Argentina,
   convierte en el momento los textos de la pantalla (voseo -> tuteo). Los argentinos ven todo igual que siempre.
   No toca valores de formularios ni datos: solo lo que se lee (textos, placeholder, title, aria-label). */
(function () {
  var M = __MAPA__;
  var PAL = /[A-Za-zÁÉÍÓÚáéíóúñÑüÜ]+/g;
  function caso(o, n) { return (o.length > 1 && o === o.toUpperCase()) ? n.toUpperCase() : (o.charAt(0) !== o.charAt(0).toLowerCase() ? n.charAt(0).toUpperCase() + n.slice(1) : n); }
  function neutro(s) {
    if (!s || typeof s !== 'string') return s;
    s = s.replace(/\b([Cc])on vos\b/g, function (m, c) { return c === 'C' ? 'Contigo' : 'contigo'; })
         .replace(/\b([AaPpDd]\w*|[Pp]or) vos\b/g, function (m, w) { return /^(a|para|de|por)$/i.test(w) ? w + ' ti' : m; });
    return s.replace(PAL, function (w) { var k = w.toLowerCase(); return (M.hasOwnProperty(k) && w !== 'Tomás') ? caso(w, M[k]) : w; });
  }
  window.WaveNeutro = { neutro: neutro, activo: false, activar: function () { activar(); } };
  var ATR = ['placeholder', 'title', 'aria-label'];
  function pasar(n) {
    if (n.nodeType === 3) { var v = n.nodeValue, w = neutro(v); if (w !== v) n.nodeValue = w; return; }
    if (n.nodeType !== 1 || /^(SCRIPT|STYLE|TEXTAREA|IFRAME|CODE)$/.test(n.nodeName) || n.isContentEditable) return;
    ATR.forEach(function (a) { var v = n.getAttribute && n.getAttribute(a); if (v) { var w = neutro(v); if (w !== v) n.setAttribute(a, w); } });
    for (var c = n.firstChild; c; c = c.nextSibling) pasar(c);
  }
  function activar() {
    if (window.WaveNeutro.activo) return; window.WaveNeutro.activo = true;
    document.title = neutro(document.title); pasar(document.body);
    new MutationObserver(function (ms) { ms.forEach(function (m) {
      if (m.type === 'characterData') pasar(m.target);
      else if (m.type === 'attributes') pasar(m.target);
      else m.addedNodes.forEach(pasar);
    }); }).observe(document.body, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ATR });
    var al = window.alert, cf = window.confirm;
    window.alert = function (t) { return al.call(window, neutro(String(t))); };
    window.confirm = function (t) { return cf.call(window, neutro(String(t))); };
  }
  var K = 'wave_neutro';
  try { if (localStorage.getItem(K) === '1') document.addEventListener('DOMContentLoaded', activar); } catch (e) {}
  async function decidir() {
    try {
      var sb = window.Wave && Wave.sb; if (!sb) return;
      var ses = await sb.auth.getSession(); var u = ses.data.session && ses.data.session.user; if (!u) return;
      var r = await sb.from('students').select('pais').eq('profile_id', u.id).maybeSingle();
      var paises = r.data ? [r.data.pais] : [];
      if (!r.data) {
        var f = await sb.from('families').select('id, pais').eq('profile_id', u.id).maybeSingle();
        if (f.data && f.data.pais) paises = [f.data.pais]; // el país que eligió la familia manda
        else if (f.data) { var h = await sb.from('students').select('pais').eq('family_id', f.data.id); paises = (h.data || []).map(function (x) { return x.pais; }); }
      }
      var si = paises.length > 0 && paises.every(function (p) { return p && p !== 'Argentina'; });
      try { localStorage.setItem(K, si ? '1' : '0'); } catch (e) {}
      if (si) activar();
    } catch (e) {}
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', decidir); else decidir();
})();
"""

if __name__ == '__main__' and '--js' in __import__('sys').argv:
    import json, os
    destino = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'js', 'neutro.js')
    open(destino, 'w', encoding='utf-8').write(JS.replace('__MAPA__', json.dumps(MAPA, ensure_ascii=False, sort_keys=True)))
    print('js/neutro.js:', len(MAPA), 'palabras')
elif __name__ == '__main__':
    import sys, json, glob
    fs = sys.argv[1:] or glob.glob('tools/clase/lecciones/*.json') + glob.glob('contenido/*/mision-*/mision-*.json')
    malas = {}
    for f in fs:
        r = revisar(json.load(open(f, encoding='utf-8')))
        if r: malas[f] = r
    for f, r in malas.items(): print(f, ':', ' '.join(r))
    print('neutro:', 'OK' if not malas else f'{sum(map(len, malas.values()))} palabra(s) sin clasificar')
    sys.exit(1 if malas else 0)
