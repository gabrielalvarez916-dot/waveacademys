# -*- coding: utf-8 -*-
"""Estilos y piezas visuales comunes de los PDF de lección de Wave Academy."""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                Flowable, KeepTogether, PageBreak, NextPageTemplate, CondPageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit, ImageReader

import os
FD = os.environ.get("WAVE_FONTS", "/usr/share/fonts/truetype/dejavu/")
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DV-I", FD + "DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DV-BI", FD + "DejaVuSans-BoldOblique.ttf"))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV-I", boldItalic="DV-BI")

DARK = HexColor("#243b3f"); TEAL = HexColor("#0e7c7b"); MINT = HexColor("#7fd1c2")
LIGHT = HexColor("#eaf6f3"); LIGHT2 = HexColor("#d8f0ea"); TEXT = HexColor("#2b2b2b")
GRAY = HexColor("#707f82"); AMBER = HexColor("#F4B63F"); CREAM = HexColor("#fff4d6"); AMBERD = HexColor("#9a6a00")
PW, PH = A4
LM = RM = 54
W = PW - LM - RM  # ancho útil

# ---------------- estilos ----------------
def S(name, **kw):
    base = dict(fontName="DV", fontSize=8.8, leading=13.2, textColor=TEXT, alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(name, **base)

body = S("body", spaceAfter=5)
bodyc = S("bodyc", spaceAfter=0)
small = S("small", fontSize=7.8, leading=11)
cap = S("cap", fontName="DV-I", fontSize=6.8, leading=9, textColor=GRAY, alignment=TA_CENTER, spaceBefore=3, spaceAfter=7)
bul = S("bul", leftIndent=12, bulletIndent=2, spaceAfter=3)
defin = S("defin", fontName="DV-I", textColor=white, fontSize=9, leading=14)
h1 = S("h1", fontName="DV-B", fontSize=19, leading=24, textColor=DARK, spaceAfter=8)
h2 = S("h2", fontName="DV-B", fontSize=10, leading=13, textColor=TEAL, spaceBefore=8, spaceAfter=5)
cellb = S("cellb", fontName="DV-B", fontSize=7.8, leading=10.5, textColor=DARK)
cell = S("cell", fontSize=7.8, leading=10.5)
cellc = S("cellc", fontSize=7.8, leading=10.5, alignment=TA_CENTER)
cellcb = S("cellcb", fontName="DV-B", fontSize=7.8, leading=10.5, alignment=TA_CENTER, textColor=DARK)
stepn = S("stepn", leftIndent=14, bulletIndent=0, spaceAfter=3)
ex = S("ex", fontName="DV-B", fontSize=9.5, leading=13, textColor=TEAL, spaceBefore=9, spaceAfter=5)


class Label(Flowable):
    """Texto en mayúsculas con espaciado entre letras (como en el modelo)."""
    def __init__(self, text, color=MINT, size=6, font="DV-B", space=1.9, align="left"):
        super().__init__(); self.t, self.c, self.s, self.f, self.sp, self.al = text, color, size, font, space, align
    def wrap(self, aw, ah):
        self.aw = aw; return aw, self.s + 5
    def draw(self):
        c = self.canv; t = c.beginText()
        tw = pdfmetrics.stringWidth(self.t, self.f, self.s) + self.sp * (len(self.t) - 1)
        x = 0 if self.al == "left" else (self.aw - tw) / 2
        t.setTextOrigin(x, 2); t.setFont(self.f, self.s); t.setFillColor(self.c); t.setCharSpace(self.sp); t.textOut(self.t)
        c.drawText(t)

def P(t, st=body): return Paragraph(t, st)
def spc(h=6): return Spacer(1, h)
def bullets(items): return [Paragraph(t, bul, bulletText="•") for t in items]

def box_dark(label, html):
    t = Table([[[Label(label), spc(2), P(html, defin)]]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), DARK), ("ROUNDEDCORNERS", [9, 9, 9, 9]),
                           ("LEFTPADDING", (0, 0), (-1, -1), 16), ("RIGHTPADDING", (0, 0), (-1, -1), 16),
                           ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 11)]))
    return t

def box_note(label, html, kind="tip"):
    bar, bg, lc = (TEAL, LIGHT, TEAL) if kind == "tip" else (AMBER, CREAM, AMBERD)
    inner = Table([[[Label(label, color=lc), spc(2), P(html, bodyc)]]], colWidths=[W - 4])
    inner.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), 12),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 12), ("TOPPADDING", (0, 0), (-1, -1), 8),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
    t = Table([["", inner]], colWidths=[4, W - 4])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), bar), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return t

def bar(num, title):
    t = Table([["", Paragraph(f'<font color="#7fd1c2">{num}.</font> {title}', S("bt", fontName="DV-B", fontSize=12.5, leading=16, textColor=white))]],
              colWidths=[8, W - 8])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), MINT), ("BACKGROUND", (1, 0), (1, 0), DARK),
                           ("ROUNDEDCORNERS", [7, 7, 7, 7]), ("LEFTPADDING", (1, 0), (1, 0), 14),
                           ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    t.keepWithNext = True; t.spaceAfter = 6
    return t

def subbar(title):
    t = Table([["", Paragraph(title, S("sb", fontName="DV-B", fontSize=9.5, leading=12, textColor=TEAL))]], colWidths=[4, W - 4])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), TEAL), ("BACKGROUND", (1, 0), (1, 0), LIGHT2),
                           ("ROUNDEDCORNERS", [5, 5, 5, 5]), ("LEFTPADDING", (1, 0), (1, 0), 12),
                           ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    t.keepWithNext = True; t.spaceBefore = 4; t.spaceAfter = 6
    return t

def table(head, rows, widths, align_first_bold=True, center_cols=()):
    data = [[Label(h, color=white, size=5.8, space=1.6, align=('center' if (j in center_cols and j > 0) else 'left')) for j, h in enumerate(head)]]
    for r in rows:
        line = []
        for j, c in enumerate(r):
            if isinstance(c, str):
                st = cellcb if (j in center_cols and j == 0) else cellc if j in center_cols else cellb if (j == 0 and align_first_bold) else cell
                line.append(Paragraph(c, st))
            else:
                line.append(c)
        data.append(line)
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [("BACKGROUND", (0, 0), (-1, 0), DARK), ("ROUNDEDCORNERS", [6, 6, 6, 6]),
          ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
          ("TOPPADDING", (0, 0), (-1, 0), 7), ("BOTTOMPADDING", (0, 0), (-1, 0), 4),
          ("TOPPADDING", (0, 1), (-1, -1), 5), ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
          ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]
    for i in range(1, len(data)):
        if i % 2 == 1: st.append(("BACKGROUND", (0, i), (-1, i), LIGHT))
    t.setStyle(TableStyle(st))
    return t



def spaced(c, x, y, txt, font, size, color, sp):
    t = c.beginText(x, y); t.setFont(font, size); t.setFillColor(color); t.setCharSpace(sp); t.textOut(txt); c.drawText(t)
    t0 = c.beginText(0, 0); t0.setCharSpace(0); c.drawText(t0)

