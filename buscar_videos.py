"""
Busca 4 videos candidatos de YouTube para cada lección (sin API de YouTube, sin costo)
y los guarda en la tabla video_candidatos de Supabase (proyecto Wave Academy).

Variables de entorno necesarias:
  SUPABASE_URL          https://ndglmonqpqpfgeoxatcb.supabase.co
  SUPABASE_SERVICE_KEY  clave service_role (se carga como Secret en GitHub)
Opcionales:
  LOTE                  cuántas lecciones buscar por corrida (por defecto 250)
  PAUSA_MIN / PAUSA_MAX segundos de espera entre búsquedas (por defecto 4 y 8)
"""
import os
import sys
import time
import random
import requests
import yt_dlp

URL = os.environ["SUPABASE_URL"].rstrip("/")
KEY = os.environ["SUPABASE_SERVICE_KEY"].strip()
LOTE = int(os.environ.get("LOTE", "250"))
PAUSA_MIN = float(os.environ.get("PAUSA_MIN", "4"))
PAUSA_MAX = float(os.environ.get("PAUSA_MAX", "8"))
CANDIDATOS_POR_LECCION = 4
ERRORES_SEGUIDOS_MAX = 3

HEADERS = {
    "apikey": KEY,
    "Content-Type": "application/json",
}
if KEY.startswith("eyJ"):  # clave clásica (JWT); las nuevas sb_secret_ van solo en apikey
    HEADERS["Authorization"] = f"Bearer {KEY}"


def pendientes():
    r = requests.get(
        f"{URL}/rest/v1/video_pendientes",
        headers=HEADERS,
        params={"select": "*", "limit": str(LOTE)},
        timeout=60,
    )
    r.raise_for_status()
    return r.json()


def buscar_en_youtube(consulta):
    opciones = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "extract_flat": True,
    }
    with yt_dlp.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(f"ytsearch10:{consulta}", download=False)
    resultado = []
    for e in info.get("entries") or []:
        vid = e.get("id")
        if not vid:
            continue
        dur = e.get("duration")
        if e.get("live_status") in ("is_live", "is_upcoming"):
            continue
        if dur is not None and (dur < 90 or dur > 3600):
            continue
        resultado.append(
            {
                "youtube_id": vid,
                "titulo": e.get("title"),
                "canal": e.get("channel") or e.get("uploader"),
                "duracion_seg": int(dur) if dur else None,
                "miniatura": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
            }
        )
        if len(resultado) >= CANDIDATOS_POR_LECCION:
            break
    return resultado


def guardar(leccion, consulta, videos):
    lesson_id = leccion["lesson_id"]
    if videos:
        filas = [dict(v, lesson_id=lesson_id, orden=i + 1) for i, v in enumerate(videos)]
        r = requests.post(
            f"{URL}/rest/v1/video_candidatos",
            headers=dict(HEADERS, Prefer="resolution=ignore-duplicates,return=minimal"),
            params={"on_conflict": "lesson_id,youtube_id"},
            json=filas,
            timeout=60,
        )
        r.raise_for_status()
    r = requests.post(
        f"{URL}/rest/v1/video_busqueda",
        headers=dict(HEADERS, Prefer="resolution=merge-duplicates,return=minimal"),
        json={
            "lesson_id": lesson_id,
            "consulta": consulta,
            "estado": "buscado" if videos else "sin_resultados",
            "candidatos": len(videos),
        },
        timeout=60,
    )
    r.raise_for_status()


def main():
    lista = pendientes()
    print(f"Lecciones a buscar en esta corrida: {len(lista)}")
    hechas = 0
    errores_seguidos = 0
    for leccion in lista:
        consulta = f'{leccion["leccion"]} {leccion["materia"]} {leccion["anio"]} explicación'
        try:
            videos = buscar_en_youtube(consulta)
            guardar(leccion, consulta, videos)
            errores_seguidos = 0
            hechas += 1
            print(f"[{hechas}/{len(lista)}] {leccion['leccion']} -> {len(videos)} candidatos")
        except Exception as ex:
            errores_seguidos += 1
            print(f"ERROR en '{leccion['leccion']}': {ex}")
            if errores_seguidos >= ERRORES_SEGUIDOS_MAX:
                print("Demasiados errores seguidos (posible bloqueo de YouTube). Se corta la corrida.")
                sys.exit(1)
        time.sleep(random.uniform(PAUSA_MIN, PAUSA_MAX))
    print(f"Listo. Lecciones procesadas: {hechas}")


if __name__ == "__main__":
    main()
