"""
Busca videos candidatos de YouTube para cada lección (método v2, sin IA y sin API de YouTube).

Qué mejora respecto del método viejo:
  - La consulta usa lección + tema + materia + nivel (inicial / primaria / secundaria).
  - Descarta videos en otros idiomas, de otro nivel (infantiles en secundaria, universitarios
    en primaria, etc.) y contenido que no es educativo.
  - Prioriza videos de Argentina y España, pero acepta cualquier país si está en español.
  - Busca varias lecciones a la vez y sin pausas largas.
  - No busca oficios ni lecciones sin nombre real (la cola ya viene filtrada: video_pendientes_v2).

Variables de entorno:
  SUPABASE_URL, SUPABASE_SERVICE_KEY   (obligatorias)
  LOTE        lecciones por corrida (por defecto 1200)
  HILOS       búsquedas en paralelo (por defecto 6)
  MAX_MIN     minutos máximos antes de cortar limpio (por defecto 40)
  DRY_RUN     "1" = prueba: muestra resultados y NO guarda nada
"""
import math
import os
import random
import re
import sys
import threading
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

CANDIDATOS_POR_LECCION = 4
RESULTADOS_POR_BUSQUEDA = 15

# ---------------------------------------------------------------- niveles
# En la base: Nivel Inicial / Nivel Medio / Nivel Avanzado.
# Para buscar usamos los nombres conocidos: inicial / primaria / secundaria.
NIVEL_TXT = {
    "inicial": "nivel inicial jardín de infantes",
    "medio": "primaria",
    "avanzado": "secundaria",
}
# (duración mínima, duración máxima) en segundos
DURACION = {"inicial": (45, 600), "medio": (90, 1200), "avanzado": (180, 1800)}

# ---------------------------------------------------------------- listas de reglas
ES = set(
    "el la los las de del que y en un una para con por como es se al lo su sus mas cual cuando "
    "donde son este esta estos estas clase explicacion ejemplos ejercicios facil tema ejemplo "
    "aprende aprender entender resumen".split()
)
EN = set(
    "the of and to how what is for with in you your this that from explained learn beginners "
    "course lesson introduction why are vs free guide tutorial class lecture".split()
)
PT = set("voce nao uma aula exercicios ensino fundamental explicacao".split())
ES_EXCLUSIVAS = {"el", "los", "las", "del", "un"}

NO_LATINO = re.compile(r"[\u0400-\u04FF\u0590-\u06FF\u0900-\u0DFF\u3040-\u30FF\u4E00-\u9FFF\uAC00-\uD7AF]")
TILDES_ES = re.compile(r"[áéíóúñ¿¡]", re.I)

# contenido infantil: se descarta en secundaria
INFANTIL = re.compile(
    r"\b(para ninos|ninos|ninas|infantil|infantiles|kids|preescolar|jardin de infantes|"
    r"dibujos animados|cantajuego|pocoyo|peppa|primer grado|segundo grado|tercer grado|"
    r"cuarto grado|quinto grado|sexto grado|primaria|aprende jugando|smile and learn|"
    r"aula365|flexflix|peques)\b"
)
# contenido de nivel superior: se descarta en inicial y en primaria
SUPERIOR = re.compile(
    r"\b(secundaria|bachillerato|universidad|universitario|preparatoria|selectividad|ebau|"
    r"licenciatura|facultad|cbc|ingreso a la universidad|ingenieria|calculo diferencial)\b"
)
# solo para inicial: también se descarta lo de primaria en adelante
PRIMARIA = re.compile(r"\b(primer grado|segundo grado|tercer grado|cuarto grado|quinto grado|sexto grado|primaria)\b")
# no educativo (todos los niveles)
RUIDO = re.compile(
    r"\b(predica|predicacion|sermon|estudio biblico|estudios biblicos|reaccion|reaccionando|"
    r"shorts|tiktok|memes|trailer|pelicula completa|capitulo completo|telediario|sorteo|"
    r"unboxing|asmr|karaoke)\b"
)
# bonus Argentina / España
AR_ES = re.compile(
    r"\b(argentina|argentino|argentinos|argentinas|educ ar|educar|canal encuentro|encuentro|"
    r"paka paka|espana|espanol de espana|unicoos|aprendemos juntos)\b"
)
# canales educativos conocidos (bonus chico); se puede editar libremente
CANALES_BUENOS = [
    "canal encuentro", "educ.ar", "unicoos", "khan academy", "julioprofe", "profe alex",
    "academia internet", "math2me", "derivando", "quantumfracture", "date un vlog",
    "educatina", "happy learning", "aprendemos juntos", "paka paka",
]

STOP = set(
    "para como cual cuales cuando donde desde hasta entre sobre segun tambien porque pero sino "
    "esta este estos estas esas esos aquel aquella clase explicacion tema temas leccion video "
    "ejemplos ejercicios facil resumen completo basico".split()
)


# ---------------------------------------------------------------- utilidades de texto
def norm(s):
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9ñ]+", " ", s.lower()).strip()


def tokens(s):
    """Palabras significativas, recortadas a 5 letras para que 'plazos' ~ 'plazo'."""
    return {t[:5] for t in norm(s).split() if len(t) >= 4 and t not in STOP}


def materia_base(materia):
    """'Matemática IV' / 'Lengua 3' -> 'Matemática' / 'Lengua'."""
    return re.sub(r"\s+(?:[IVX]{1,4}|\d+)(?=\s|$)", "", materia or "").strip()


def es_generico(s):
    return bool(re.match(r"^\s*(lecci[oó]n|tema)\s*\d+\s*$", s or "", re.I))


# ---------------------------------------------------------------- consultas
def consulta_principal(l):
    nivel = NIVEL_TXT.get(l["nivel"], "")
    partes = [l["leccion"]]
    if l.get("tema") and not es_generico(l["tema"]):
        partes.append(l["tema"])
    partes += [materia_base(l["materia"]), nivel, "explicación"]
    return re.sub(r"\s+", " ", " ".join(partes)).strip()


def consulta_alternativa(l):
    nivel = NIVEL_TXT.get(l["nivel"], "")
    base = l["tema"] if l.get("tema") and not es_generico(l["tema"]) else l["leccion"]
    return re.sub(r"\s+", " ", f"{base} {materia_base(l['materia'])} {nivel} clase").strip()


# ---------------------------------------------------------------- filtros y puntaje
def es_espanol(titulo, canal):
    """Devuelve (ok, penalizacion). Lenient: sin pistas claras no se descarta, solo penaliza."""
    if NO_LATINO.search(titulo or ""):
        return False, 0
    pal = set(norm(titulo).split())
    en = len(pal & EN)
    es = len(pal & ES) + (1 if TILDES_ES.search(titulo or "") else 0)
    pt = len(pal & PT)
    if pt >= 1 and not (pal & ES_EXCLUSIVAS) and "ñ" not in (titulo or "").lower():
        return False, 0
    if en > es or (en > 0 and es == 0):
        return False, 0
    if es == 0 and en == 0:
        return True, 1.0
    return True, 0.0


def evaluar(video, l):
    """Devuelve (puntaje, motivo_descarte). puntaje None = descartado."""
    titulo = video.get("title") or ""
    canal = video.get("channel") or video.get("uploader") or ""
    desc = (video.get("description") or "")[:300]
    dur = video.get("duration")
    nivel = l["nivel"]

    if video.get("live_status") in ("is_live", "is_upcoming"):
        return None, "en vivo"
    dmin, dmax = DURACION.get(nivel, (90, 1800))
    if dur is not None and not (dmin <= dur <= dmax):
        return None, "duración"

    texto = norm(f"{titulo} {canal}")
    if RUIDO.search(texto):
        return None, "no educativo"
    if nivel == "avanzado" and INFANTIL.search(texto):
        return None, "infantil en secundaria"
    if nivel == "medio" and SUPERIOR.search(texto):
        return None, "nivel superior en primaria"
    if nivel == "inicial" and (SUPERIOR.search(texto) or PRIMARIA.search(texto)):
        return None, "nivel superior en inicial"

    ok, penal = es_espanol(titulo, canal)
    if not ok:
        return None, "idioma"

    # relevancia: tiene que compartir palabras con la lección / el tema / los contenidos
    v = tokens(f"{titulo} {desc}")
    tl = tokens(l["leccion"])
    tt = tokens(l["tema"]) if l.get("tema") and not es_generico(l["tema"]) else set()
    tc = tokens(" ".join(l.get("contenidos") or []))
    ol, ot, oc = len(tl & v), len(tt & v), len(tc & v)
    # tiene que coincidir con el título de la lección, o con al menos 2 palabras del tema/contenidos
    if not (ol >= 1 or ot + oc >= 2):
        return None, "no se relaciona con la lección"

    puntaje = 3.0 * ol + 2.0 * ot + 1.5 * oc - penal
    if AR_ES.search(norm(f"{titulo} {canal} {desc}")):
        puntaje += 2.0
    if any(c in canal.lower() for c in CANALES_BUENOS):
        puntaje += 1.5
    vistas = video.get("view_count") or 0
    puntaje += 0.3 * math.log10(vistas + 1)
    return puntaje, None


def elegir(entradas, l):
    ranking = []
    for e in entradas:
        if not e.get("id"):
            continue
        p, _ = evaluar(e, l)
        if p is not None:
            ranking.append((p, e))
    ranking.sort(key=lambda x: -x[0])
    out, vistos = [], set()
    for _, e in ranking:
        if e["id"] in vistos:
            continue
        vistos.add(e["id"])
        dur = e.get("duration")
        out.append(
            {
                "youtube_id": e["id"],
                "titulo": e.get("title"),
                "canal": e.get("channel") or e.get("uploader"),
                "duracion_seg": int(dur) if dur else None,
                "miniatura": f"https://i.ytimg.com/vi/{e['id']}/hqdefault.jpg",
            }
        )
        if len(out) >= CANDIDATOS_POR_LECCION:
            break
    return out


# ---------------------------------------------------------------- YouTube y Supabase
def buscar_en_youtube(consulta):
    import yt_dlp

    opciones = {"quiet": True, "no_warnings": True, "skip_download": True, "extract_flat": True}
    with yt_dlp.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(f"ytsearch{RESULTADOS_POR_BUSQUEDA}:{consulta}", download=False)
    return info.get("entries") or []


def buscar_leccion(l):
    q1 = consulta_principal(l)
    videos = elegir(buscar_en_youtube(q1), l)
    consulta = q1
    if len(videos) < 2:  # poca cosa: segunda búsqueda con otra redacción
        q2 = consulta_alternativa(l)
        extra = elegir(buscar_en_youtube(q2), l)
        ids = {v["youtube_id"] for v in videos}
        for v in extra:
            if v["youtube_id"] not in ids and len(videos) < CANDIDATOS_POR_LECCION:
                videos.append(v)
        consulta = f"{q1} || {q2}"
    return consulta, videos


def main():
    import requests

    url = os.environ["SUPABASE_URL"].rstrip("/")
    key = os.environ["SUPABASE_SERVICE_KEY"].strip()
    lote = int(os.environ.get("LOTE", "1200"))
    hilos = int(os.environ.get("HILOS", "6"))
    max_seg = int(os.environ.get("MAX_MIN", "40")) * 60
    dry = os.environ.get("DRY_RUN", "0") == "1"

    headers = {"apikey": key, "Content-Type": "application/json"}
    if key.startswith("eyJ"):
        headers["Authorization"] = f"Bearer {key}"

    r = requests.get(
        f"{url}/rest/v1/video_pendientes_v2",
        headers=headers,
        params={"select": "*", "limit": str(lote)},
        timeout=60,
    )
    r.raise_for_status()
    lista = r.json()
    print(f"Lecciones a buscar en esta corrida: {len(lista)} (hilos: {hilos}, prueba: {dry})")

    def guardar(l, consulta, videos):
        lid = l["lesson_id"]
        # se reemplazan los candidatos viejos que nadie eligió; los elegidos no se tocan
        requests.delete(
            f"{url}/rest/v1/video_candidatos",
            headers=headers,
            params={"lesson_id": f"eq.{lid}", "elegido": "eq.false"},
            timeout=60,
        ).raise_for_status()
        if videos:
            filas = [dict(v, lesson_id=lid, orden=i + 1) for i, v in enumerate(videos)]
            requests.post(
                f"{url}/rest/v1/video_candidatos",
                headers=dict(headers, Prefer="resolution=ignore-duplicates,return=minimal"),
                params={"on_conflict": "lesson_id,youtube_id"},
                json=filas,
                timeout=60,
            ).raise_for_status()
        requests.post(
            f"{url}/rest/v1/video_busqueda",
            headers=dict(headers, Prefer="resolution=merge-duplicates,return=minimal"),
            json={
                "lesson_id": lid,
                "consulta": consulta,
                "estado": "buscado" if videos else "sin_resultados",
                "candidatos": len(videos),
                "version": 2,
                "buscado_at": datetime.now(timezone.utc).isoformat(),
            },
            timeout=60,
        ).raise_for_status()

    lock = threading.Lock()
    estado = {"hechas": 0, "con": 0, "sin": 0, "errores": 0, "seguidos": 0, "corte": False}
    inicio = time.time()

    def trabajo(l):
        if estado["corte"] or time.time() - inicio > max_seg:
            return None
        time.sleep(random.uniform(0.2, 0.8))
        try:
            consulta, videos = buscar_leccion(l)
            if not dry:
                guardar(l, consulta, videos)
            with lock:
                estado["hechas"] += 1
                estado["seguidos"] = 0
                estado["con" if videos else "sin"] += 1
                n = estado["hechas"]
            top = videos[0]["titulo"][:70] if videos else "-"
            print(f"[{n}/{len(lista)}] {l['materia']} · {l['leccion'][:45]} -> {len(videos)} | {top}")
            if dry:
                for v in videos:
                    print(f"      · {v['titulo'][:80]} [{v['canal']}]")
        except Exception as ex:  # noqa: BLE001
            with lock:
                estado["errores"] += 1
                estado["seguidos"] += 1
                if estado["seguidos"] >= max(8, hilos * 2):
                    estado["corte"] = True
            print(f"ERROR en '{l['leccion'][:45]}': {ex}")
        return None

    with ThreadPoolExecutor(max_workers=hilos) as ex:
        futs = [ex.submit(trabajo, l) for l in lista]
        for _ in as_completed(futs):
            pass

    print(
        f"Listo. Procesadas: {estado['hechas']} | con videos: {estado['con']} | "
        f"sin resultados: {estado['sin']} | errores: {estado['errores']} | "
        f"minutos: {(time.time() - inicio) / 60:.1f}"
    )
    if estado["corte"]:
        print("Se cortó por demasiados errores seguidos (posible bloqueo de YouTube).")
        sys.exit(1)


if __name__ == "__main__":
    main()
