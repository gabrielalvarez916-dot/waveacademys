# -*- coding: utf-8 -*-
"""Generador genérico de PDF de lección (Wave Academy).
Entrada: un JSON con {"meta": {...}, "contenido": {...}} (el borrador que arma la fábrica en lesson_drafts.contenido).
Uso: python3 render_leccion.py entrada.json salida.pdf
meta: materia, anio, tema_num, tema, leccion_num, titulo, minutos (opcional), video_titulo (opcional), video_min (opcional)
"""
import sys, os, json, re, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wavepdf import *  # estilos, colores y piezas visuales ya aprobados

ENT = re.compile(r"&(?!(amp|lt|gt|quot|#\d+);)")

def limpio(t):
    """Texto de la IA -> mini-HTML seguro para ReportLab: solo <b> permitido."""
    t = str(t or "")
    t = ENT.sub("&amp;", t)
    t = re.sub(r"<(?!/?b>)", "&lt;", t)
    return t.strip()

PREF = re.compile(r"^\s*(ojo con esto|importante|tip|ojo)\s*[:\-–]\s*", re.I)
def sin_prefijo(t):
    t = PREF.sub("", limpio(t))
    return t[:1].upper() + t[1:] if t else t

def barra(num, title):
    """Barra de sección: número con punto, o un símbolo sin punto."""
    return bar(num, title) if isinstance(num, int) else _bar_sim(num, title)

def _bar_sim(sym, title):
    t = Table([["", Paragraph(f'<font color="#7fd1c2">{sym}</font>  {title}', S("bt2", fontName="DV-B", fontSize=12.5, leading=16, textColor=white))]], colWidths=[8, W - 8])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), MINT), ("BACKGROUND", (1, 0), (1, 0), DARK), ("ROUNDEDCORNERS", [7, 7, 7, 7]),
                           ("LEFTPADDING", (1, 0), (1, 0), 14), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    t.keepWithNext = True; t.spaceAfter = 6
    return t

def words(c):
    out = [c.get("objetivo", "")] + list(c.get("vas_a_ver", []))
    for s in c.get("secciones", []):
        for b in s.get("bloques", []):
            out += [b.get("titulo", ""), b.get("texto", "")] + list(b.get("items", []) or [])
            for f in b.get("filas", []) or []: out += f
    for k in ("ejemplo_completo", "ejemplo_incompleto", "ejemplo_solo"):
        e = c.get(k) or {}
        out += [e.get("titulo", ""), e.get("planteo", "")] + list(e.get("pasos", []) or [])
    t = c.get("tip") or {}
    out += [t.get("titulo", ""), t.get("texto", "")] + list(c.get("ojo", []) or []) + list(c.get("carpeta", []) or [])
    return len(re.findall(r"\w+", " ".join(map(str, out))))

def wrap_lines(text, font, size, maxw, maxlines):
    ls = simpleSplit(text, font, size, maxw)
    return ls[:maxlines]

# ---------------- portada y páginas ----------------
META = {}
LOGO = os.environ.get("WAVE_LOGO", os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png"))

def cover(c, doc):
    m = META
    c.saveState()
    n = 220; top, bot = (0x0b, 0x5e, 0x61), (0x14, 0x92, 0x8a)
    for i in range(n):
        f = i / (n - 1)
        c.setFillColorRGB(*[(top[k] + (bot[k] - top[k]) * f) / 255 for k in range(3)])
        c.rect(0, PH - (i + 1) * PH / n - 0.6, PW, PH / n + 1.2, stroke=0, fill=1)
    c.setFillColor(MINT); c.setFillAlpha(0.13); c.setFont("DV-B", 158); c.drawString(300, PH - 432, f"{int(m['tema_num']):02d}"); c.setFillAlpha(1)
    spaced(c, 62, PH - 95, f"{m['materia'].upper()} · {m['anio']}.º AÑO", "DV-B", 7.4, MINT, 2.4)
    spaced(c, 62, PH - 111, f"TEMA {m['tema_num']} · {m['tema'].upper()}"[:58], "DV-B", 7.4, MINT, 2.4)
    c.setFillColor(white); c.roundRect(426, PH - 124, 112, 72, 14, stroke=0, fill=1)
    c.drawImage(ImageReader(LOGO), 432, PH - 119, width=100, height=60, mask="auto", preserveAspectRatio=True, anchor="c")
    spaced(c, 62, PH - 238, "LECCIÓN", "DV-B", 7, MINT, 2.6)
    c.setFillColor(MINT); c.setFont("DV-B", 124); c.drawString(58, PH - 333, f"{int(m['leccion_num']):02d}")
    # título: tamaño que entre en 2 líneas
    c.setFillColor(white)
    size = 26.5
    while size > 17 and len(simpleSplit(m["titulo"], "DV-B", size, 440)) > 2: size -= 1.5
    y = PH - 379
    for ln in simpleSplit(m["titulo"], "DV-B", size, 440)[:2]:
        c.setFont("DV-B", size); c.drawString(62, y, ln); y -= size * 1.28
    ybar = y - 4
    c.setStrokeColor(AMBER); c.setLineWidth(4); c.setLineCap(1); c.line(64, ybar, 134, ybar)
    c.setFillColor(white); c.setFont("DV-I", 10.5)
    for i, ln in enumerate(wrap_lines(m["subtitulo"], "DV-I", 10.5, 400, 4)):
        c.drawString(62, ybar - 36 - i * 18.5, ln)
    vv = [limpio(x) for x in (META.get("_vas_a_ver") or [])][:6]
    if vv:
        y0 = ybar - 36 - 18.5 * min(4, len(wrap_lines(m["subtitulo"], "DV-I", 10.5, 400, 4))) - 26
        spaced(c, 62, y0, "LO QUE VAS A VER", "DV-B", 7, MINT, 2.6); y0 -= 20
        for x in vv:
            ls = simpleSplit(x, "DV", 9.6, 420)[:2]
            c.setFillColor(AMBER); c.circle(66, y0 + 3, 2.2, stroke=0, fill=1)
            c.setFillColor(white); c.setFont("DV", 9.6)
            for ln in ls:
                c.drawString(78, y0, ln); y0 -= 13
            y0 -= 5
    for txt, x in (("LECTURA", 62), ("INCLUYE", 145)):
        spaced(c, x, PH - 726, txt, "DV-B", 5.8, MINT, 2)
    c.setFillColor(white); c.setFont("DV-B", 8.2)
    c.drawString(62, PH - 741, f"{m['minutos']} minutos"); c.drawString(145, PH - 741, "Ejemplos · Carpeta · Resumen · Glosario")
    def wave(color, y0, a, ph):
        c.setFillColor(color); p = c.beginPath(); p.moveTo(0, 0); p.lineTo(0, y0)
        p.curveTo(PW * 0.22, y0 + a, PW * 0.38, y0 - a * 0.9, PW * 0.58, y0 + a * 0.2 + ph)
        p.curveTo(PW * 0.76, y0 + a * 1.1 + ph, PW * 0.88, y0 + a * 1.0 + ph, PW, y0 + a * 1.5 + ph)
        p.lineTo(PW, 0); p.close(); c.drawPath(p, stroke=0, fill=1)
    wave(HexColor("#3aaca6"), 78, 8, 14); wave(HexColor("#2f6b67"), 52, 6, 8); wave(HexColor("#263a3d"), 26, 4, 3)
    c.restoreState()

def page(c, doc):
    m = META
    c.saveState()
    spaced(c, LM, PH - 40, f"WAVE ACADEMY · {m['materia'].upper()} · {m['anio']}.º AÑO", "DV-B", 6.4, DARK, 1.9)
    txt = f"LECCIÓN {m['leccion_num']} · {m['titulo'].upper()}"
    while pdfmetrics.stringWidth(txt, "DV-B", 6.4) + 1.9 * len(txt) > 260 and len(txt) > 12: txt = txt[:-2]
    tw = pdfmetrics.stringWidth(txt, "DV-B", 6.4) + 1.9 * (len(txt) - 1)
    spaced(c, PW - RM - tw, PH - 40, txt, "DV-B", 6.4, TEAL, 1.9)
    c.setStrokeColor(TEAL); c.setLineWidth(1); c.line(LM, PH - 48, PW - RM, PH - 48)
    c.setFillColor(GRAY); c.setFont("DV-B", 6.4)
    c.drawString(LM, 36, "Material de estudio · Uso exclusivo de estudiantes de Wave Academy")
    c.setFillColor(TEAL); c.roundRect(PW - RM - 20, 30, 20, 13, 5, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("DV-B", 7); c.drawCentredString(PW - RM - 10, 34, str(doc.page))
    c.restoreState()

# ---------------- imágenes ----------------
TIPOS_IMG = {"mapa": "MAPA", "foto": "FOTO", "ilustracion": "ILUSTRACIÓN", "diagrama": "DIAGRAMA", "esquema": "ESQUEMA",
             "grafico": "GRÁFICO", "linea_de_tiempo": "LÍNEA DE TIEMPO", "figura_geometrica": "FIGURA", "obra_de_arte": "OBRA DE ARTE", "otro": "IMAGEN"}
FIG = [0]

def _archivo_imagen(b):
    """Devuelve la ruta de una imagen real si el bloque trae 'archivo' (ruta local) o 'url' descargable; si no, None."""
    ruta = b.get("archivo")
    if ruta and os.path.isfile(ruta): return ruta
    b64 = b.get("png_base64")  # figura creada por Claude en sesión y guardada dentro del propio borrador
    if b64:
        try:
            import base64, tempfile
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
            tmp.write(base64.b64decode(b64)); tmp.close(); return tmp.name
        except Exception:
            return None
    url = b.get("url")
    if url and str(url).startswith("https://"):
        try:
            import urllib.request, tempfile
            ext = os.path.splitext(str(url).split("?")[0])[1].lower()
            if ext not in (".png", ".jpg", ".jpeg"): return None
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
            with urllib.request.urlopen(url, timeout=20) as r: tmp.write(r.read())
            tmp.close(); return tmp.name
        except Exception:
            return None
    return None

def imagen_bloque(b):
    """Bloque de imagen. Si hay archivo o url, la inserta; si no, deja un recuadro con la descripción EXACTA de la imagen que falta."""
    FIG[0] += 1
    n = FIG[0]
    tipo = TIPOS_IMG.get(b.get("imagen_tipo"), "IMAGEN")
    titulo = limpio(b.get("titulo")); pie = limpio(b.get("texto"))
    desc = limpio(b.get("imagen_descripcion")); fuente = limpio(b.get("imagen_fuente"))
    cab = P(f"<b>Figura {n}</b>" + (f" · {titulo}" if titulo else ""), S("fg", fontName="DV-B", fontSize=8.8, textColor=TEAL, spaceAfter=3))
    real = _archivo_imagen(b)
    if real:
        try:
            from reportlab.platypus import Image as RLImage
            iw, ih = ImageReader(real).getSize()
            w = min(W * 0.8, iw); h = w * ih / iw
            if h > 300: h = 300; w = h * iw / ih
            im = RLImage(real, width=w, height=h); im.hAlign = "CENTER"
            out = [cab, im] + ([P(pie, cap)] if pie else [spc(6)])
            return [KeepTogether(out)]
        except Exception:
            pass
    cuerpo = [Label(f"{tipo} A INSERTAR", color=AMBERD, size=5.8), spc(3), P(f"<b>Qué tiene que mostrar:</b> {desc}", bodyc)]
    if fuente: cuerpo += [spc(3), P(f"<b>Dónde conseguirla:</b> {fuente}", small)]
    caja = Table([[cuerpo]], colWidths=[W])
    caja.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), CREAM), ("BOX", (0, 0), (-1, -1), 0.8, AMBER, None, (3, 2)),
                              ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                              ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 10)]))
    return [KeepTogether([cab, caja] + ([P(pie, cap)] if pie else [spc(6)]))]

# ---------------- bloques ----------------
def tabla_bloque(b):
    cols = [limpio(x) for x in b.get("columnas", [])]
    filas = [[limpio(x) for x in f] for f in b.get("filas", [])]
    n = max(len(cols), 1)
    # primera columna un poco más angosta si hay 3 o más
    if n >= 3 and not b.get("iguales"): widths = [W * 0.26] + [W * 0.74 / (n - 1)] * (n - 1)
    else: widths = [W / n] * n
    out = []
    if b.get("titulo"): out.append(P(f"<b>{limpio(b['titulo'])}</b>", S("tt", fontName="DV-B", fontSize=8.8, textColor=TEAL, spaceAfter=3)))
    out.append(table([x.upper() for x in cols], [r + [""] * (n - len(r)) for r in filas], widths))
    if b.get("texto"): out.append(P(limpio(b["texto"]), cap))
    else: out.append(spc(6))
    return [KeepTogether(out)]

def bloque(b):
    t = b.get("tipo"); tx = limpio(b.get("texto")); ti = sin_prefijo(b.get("titulo")) if t in ("importante", "tip", "ojo") else limpio(b.get("titulo")); items = [limpio(x) for x in (b.get("items") or [])]
    if t == "parrafo": return [P(tx)]
    if t == "definicion": return [box_dark(ti.upper() if ti else "DEFINICIÓN", tx), spc(8)]
    if t == "importante": return [box_note("✦ IMPORTANTE" + (": " + ti.upper() if ti else ""), tx), spc(8)]
    if t == "tip": return [box_note("TIP" + (": " + ti.upper() if ti else ""), tx, "tip"), spc(8)]
    if t == "ojo": return [box_note("OJO CON ESTO" + (": " + ti.upper() if ti else ""), tx, "ojo"), spc(8)]
    if t == "lista": return bullets(items) + [spc(4)]
    if t == "pasos":
        out = ([P(tx)] if tx else []) + [Paragraph(x, stepn, bulletText=f"{i + 1}.") for i, x in enumerate(items)]
        return out + [spc(4)]
    if t == "ejemplo":
        out = [subbar("Ejemplo" + (": " + ti if ti else ""))]
        if tx: out.append(P(tx))
        out += [Paragraph(x, stepn, bulletText=f"{i + 1}.") for i, x in enumerate(items)]
        return [KeepTogether(out), spc(6)]
    if t == "tabla": return tabla_bloque(b)
    if t == "imagen": return imagen_bloque(b)
    return [P(tx)] if tx else []

# ---------------- bloques fijos (etapas, ejemplos, carpeta, soluciones) ----------------
ETAPAS = {1: "Etapa 1 · Los conceptos principales", 2: "Etapa 2 · Profundizamos"}

def etapa_banner(n):
    return subbar(ETAPAS.get(n, f"Etapa {n}"))

def _pasos(items):
    return [Paragraph(limpio(x), stepn, bulletText=f"{i + 1}.") for i, x in enumerate(items or [])]

def ejemplos_fijos(c):
    """Ejemplo completo, incompleto y 'hacelo solo'. Devuelve [] si el borrador no los trae (borradores viejos)."""
    comp, inc, solo = c.get("ejemplo_completo"), c.get("ejemplo_incompleto"), c.get("ejemplo_solo")
    if not (comp or inc or solo): return []
    cab = barra("▶", "Ejemplos: mirá, completá y hacelo solo")
    s = []
    if comp:
        o = [subbar("Ejemplo completo" + (": " + limpio(comp.get("titulo")) if comp.get("titulo") else ""))]
        if comp.get("planteo"): o.append(P(limpio(comp["planteo"])))
        if comp.get("columnas"): o += tabla_bloque({**comp, "titulo": None, "texto": None})
        o += _pasos(comp.get("pasos"))
        s += [KeepTogether([cab] + o), spc(8)]; cab = None
    if inc:
        o = [subbar("Ejemplo incompleto: completalo vos" + (" · " + limpio(inc.get("titulo")) if inc.get("titulo") else ""))]
        if inc.get("planteo"): o.append(P(limpio(inc["planteo"])))
        if inc.get("columnas"): o += tabla_bloque({**inc, "titulo": None, "texto": None})
        o += _pasos(inc.get("pasos"))
        o.append(P("Completá los espacios ___ en tu carpeta. Después entregá tu respuesta en la app.", cap))
        s += [KeepTogether(([cab] if cab else []) + o), spc(8)]; cab = None
    if solo:
        o = [subbar("Hacelo solo" + (": " + limpio(solo.get("titulo")) if solo.get("titulo") else ""))]
        if solo.get("planteo"): o.append(P(limpio(solo["planteo"])))
        o += _pasos(solo.get("pasos"))
        o.append(P("Resolvelo en tu carpeta. Después entregá tu respuesta en la app.", cap))
        s += [KeepTogether(([cab] if cab else []) + o), spc(8)]; cab = None
    return s

def tip_y_ojo(c):
    s = []
    t = c.get("tip")
    if t and (t.get("texto") or t.get("titulo")):
        s += [box_note("TIP" + (": " + sin_prefijo(t.get("titulo")).upper() if t.get("titulo") else ""), limpio(t.get("texto")), "tip"), spc(8)]
    ojo = [limpio(x) for x in (c.get("ojo") or [])]
    if ojo:
        html = "<br/>".join(f"• {x}" for x in ojo)
        s += [box_note("OJO CON ESTO", html, "ojo"), spc(8)]
    return s

def carpeta_fija(c):
    items = [limpio(x) for x in (c.get("carpeta") or [])]
    if not items: return []
    s = [barra("✎", "Actividad de carpeta"),
         P("Hacé estas consignas en tu carpeta. Cuando termines, entregá tus respuestas en la app: ahí las revisamos y recién después ves las soluciones.")]
    s += [Paragraph(x, stepn, bulletText=f"{i + 1}.") for i, x in enumerate(items)]
    return [KeepTogether(s), spc(10)]

def soluciones_fijas(c):
    sol = c.get("soluciones")
    if not sol: return []
    sm = S("solp", fontSize=7.4, leading=10, textColor=GRAY)
    smb = S("solb", fontName="DV-B", fontSize=7.4, leading=10, textColor=DARK)
    rows = []
    if sol.get("incompleto"): rows.append([Paragraph("Ejemplo incompleto", smb), Paragraph(limpio(sol["incompleto"]), sm)])
    if sol.get("solo"): rows.append([Paragraph("Hacelo solo", smb), Paragraph(limpio(sol["solo"]), sm)])
    for i, x in enumerate(sol.get("carpeta") or [], 1): rows.append([Paragraph(f"Carpeta, consigna {i}", smb), Paragraph(limpio(x), sm)])
    if not rows: return []
    return [KeepTogether([barra("✓", "Soluciones"),
            P("Mirá esto recién cuando hayas terminado.", S("solnota", fontName="DV-I", fontSize=7.4, leading=10, textColor=GRAY, spaceAfter=4)),
            table(["ACTIVIDAD", "RESPUESTA"], rows, [W * 0.27, W * 0.73])])]

# ---------------- documento ----------------
def story(c, nivel="full"):
    """nivel: full | sin_glosario | sin_resumen (se omite lo que no entre en 4 hojas)."""
    s = [NextPageTemplate("main"), PageBreak()]
    etapa_actual = None
    for i, sec in enumerate(c["secciones"], 1):
        if sec.get("etapa") and sec.get("etapa") != etapa_actual:
            etapa_actual = sec["etapa"]; s += [CondPageBreak(120), etapa_banner(etapa_actual)]
        s.append(bar(i, limpio(sec["titulo"])))
        for b in sec.get("bloques", []): s += bloque(b)
        s.append(spc(8))
    s += ejemplos_fijos(c) + tip_y_ojo(c)
    if nivel in ("full", "sin_glosario") and c.get("resumen"):
        s += [CondPageBreak(120), barra("★", "Resumen")]
        cards = []
        for r in c["resumen"]:
            cards.append([Label(limpio(r["titulo"]).upper()[:40], color=TEAL, size=5.8, space=1.2), spc(1), P(limpio(r["texto"]), small)])
        rows = []
        for i in range(0, len(cards), 2):
            pair = cards[i:i + 2]
            if len(pair) < 2: pair.append("")
            rows.append(pair)
        span = [("SPAN", (0, len(rows) - 1), (1, len(rows) - 1))] if len(cards) % 2 else []
        rt = Table(rows, colWidths=[W / 2, W / 2])
        rt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), LIGHT), ("ROUNDEDCORNERS", [8, 8, 8, 8]),
                                ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                                ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                                ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -2), 3, white),
                                ("LINEAFTER", (0, 0), (0, -1), 3, white)] + span))
        s += [rt, spc(8)]
    if nivel == "full" and c.get("glosario"):
        s += [CondPageBreak(100), barra("Aa", "Glosario")]
        s += [table(["PALABRA", "QUÉ SIGNIFICA"], [[limpio(g["palabra"]), limpio(g["significado"])] for g in c["glosario"]], [W * 0.26, W * 0.74])]
    # las soluciones NO se imprimen: la app las valida y las muestra después de entregar
    s += [spc(8)] + carpeta_fija(c)
    return s

MAX_HOJAS_CONTENIDO = 4

def _construir(c, m, salida, nivel):
    FIG[0] = 0
    doc = BaseDocTemplate(salida, pagesize=A4, title=f"{m['materia']} · Lección {m['leccion_num']} · {m['titulo']}", author="Wave Academy",
                          leftMargin=LM, rightMargin=RM, topMargin=64, bottomMargin=56)
    cv = PageTemplate(id="cover", frames=[Frame(0, 0, 40, 40, id="c0", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)], onPage=cover)
    mn = PageTemplate(id="main", frames=[Frame(LM, 56, W, PH - 56 - 64, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)], onPage=page)
    doc.addPageTemplates([cv, mn])
    doc.build([Spacer(1, 1)] + story(c, nivel))
    return doc.page

def render(entrada, salida):
    data = json.load(open(entrada, encoding="utf8"))
    c = data["contenido"]; m = data["meta"]
    m["minutos"] = m.get("minutos") or max(10, 5 * round(words(c) / 110 / 5))
    m["subtitulo"] = m.get("subtitulo") or c["objetivo"]
    META.clear(); META.update(m); META["_vas_a_ver"] = c.get("vas_a_ver") or []
    # portada (1 hoja) + hasta 4 hojas de contenido; si no entra, se omite glosario y luego resumen. Nunca se recorta contenido.
    for nivel in ("full", "sin_glosario", "sin_resumen"):
        paginas = _construir(c, m, salida, nivel)
        if paginas - 1 <= MAX_HOJAS_CONTENIDO: break
    aviso = "" if nivel == "full" else f" (omitido para entrar en {MAX_HOJAS_CONTENIDO} hojas: {'glosario' if nivel == 'sin_glosario' else 'glosario y resumen'})"
    if paginas - 1 > MAX_HOJAS_CONTENIDO:
        aviso += f" ATENCIÓN: el contenido ocupa {paginas - 1} hojas; hay que acortarlo"
    print(f"páginas: {paginas} (portada + {paginas - 1}){aviso}")

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2]); print("ok")
