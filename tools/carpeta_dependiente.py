# -*- coding: utf-8 -*-
"""26/11/2026 · Detecta consignas de carpeta que no se entienden solas (dependen del PDF, de un dibujo,
una tabla, una historia o un texto que no está en la consigna).
Regla de Gabriel: la carpeta son actividades sobre el tema, sin contexto externo: cada consigna trae
adentro el caso o los datos (números, emojis, palabras citadas, la historia en una línea)."""
import re

# Siempre remiten a algo de afuera (salvo que la consigna traiga los datos)
FUERTE = re.compile(
    r"\b(del dibujo|de la imagen|la figura|la l[aá]mina|pdf|de la p[aá]gina|recuadro|la foto|que ves|"
    r"del texto|el texto anterior|la historia de arriba|del cuento|de arriba|de abajo|del otro lado|"
    r"ese pedido|esa lista|ese cuadro|esa tabla|el ejemplo|del ejemplo|el resultado de arriba|de un lado|ese grupo|el grupo [A-Z]\b|"
    r"la primera palabra|los dos t[ií]tulos|qu[eé] d[ií]a)\b", re.I)
# Referencias numeradas a un material (lugar 2, pista 1, tarjeta 1): los números no cuentan como datos
NUMERADA = re.compile(r"\b(el lugar \d|la pista \d|la tarjeta \d|las tarjetas|la escena|el cartel|marcad[oa]|el verso \d)\b", re.I)
# Remiten a algo de afuera si la consigna no trae datos propios
DEBIL = re.compile(
    r"\b(tablas?|cuadros?(?! (comparativo|sin[oó]ptico))|gr[aá]ficos?|esquemas?|mapas?|planos?|carteles?|"
    r"la historia|el cuento|la receta|la lista|la tarjeta|la nota|la carta|el pedido|va primero|va segunda|"
    r"va al final|mir[aá]|observ[aá]|cont[aá] (los|las)|seg[uú]n|ese|esa|esos|esas|aquel|aquella|"
    r"la caja de|la fila|la columna|la recta|anterior|el monto|el precio final|la oferta|la compra|"
    r"se forma|el recorrido)\b", re.I)
CONTEO = re.compile(r"¿\s*(cu[aá]nt[oa]s?)\b[^?]*\?", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⬀-⯿]")
NUM = re.compile(r"\d|\b(un[oa]?|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|doble|mitad)\b", re.I)
LISTA = re.compile(r"[A-ZÁÉÍÓÚÑÜ] _|_ [A-ZÁÉÍÓÚÑÜ]|\b[A-ZÁÉÍÓÚÑ] [A-ZÁÉÍÓÚÑ] [A-ZÁÉÍÓÚÑ]\b|\S\s*\+\s*\S|(\b[A-ZÁÉÍÓÚÑÜ]{2,}\b.*){2,}|:\s*\S+.*[,·→/]|\(\s*\S+[-,]")
# Personajes de las historias del PDF: preguntar un hecho suyo sin contarlo en la consigna
PERSONAJE = re.compile(
    r"\b(Sofi|Tomi|Lola|Dani|Wilson|Holmes|abuela|abuelo|sapo|patito|beb[eé]|jirafa|detective|"
    r"ladrones|liga)\b", re.I)
AFIRMA = re.compile(r"\b(dice|dijo|escribi[oó]|puso|cree|piensa|pregunta|hizo|riega)\b", re.I)
SABER = re.compile(r"\b(semana|a[nñ]o|mes|alfabeto|abecedario|vocales)\b", re.I)


def _con_datos(t):
    return bool(NUM.search(t) or EMOJI.search(t) or re.search(r"[«\"“].{3,}[»\"”]", t) or LISTA.search(t))


def depende(t):
    t = re.sub(r'\[\[[^\]]*\]\]', ' ', str(t or ''))
    caso_largo = bool(re.search(r"[.:]\s*¿", t)) and len(t.split()) >= 12
    if NUMERADA.search(t) and not re.search(r"\bdice que\b", t) and not (EMOJI.search(t) or re.search(r"[«\"“].{3,}[»\"”]", t) or LISTA.search(t)): return True
    if FUERTE.search(t) and not _con_datos(t): return True
    if DEBIL.search(t) and not _con_datos(t) and not caso_largo: return True
    if CONTEO.search(t) and not _con_datos(t) and not SABER.search(t): return True
    # "Tomi se toca la nariz. ¿Qué orden escuchó?" trae el caso; "¿Qué hace Tomi?" no
    caso = bool(re.search(r"[.:]\s*¿", t)) or bool(re.search(r"\b[A-ZÁÉÍÓÚÑÜ]{2,}\b", t))
    if PERSONAJE.search(t) and not AFIRMA.search(t) and not caso and len(t.split()) < 12 and not _con_datos(t): return True
    return False
