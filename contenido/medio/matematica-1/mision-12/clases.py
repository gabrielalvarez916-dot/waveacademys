# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 12 · Sumar y restar decenas enteras: las 4 clases animadas.
Metáfora: el kiosco de Sofi con bolsitas de 10 caramelos (🛍️). Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat1-m12-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'f517e08c-77e1-4cf6-80c2-da7c3d03d246', 2: '615375b1-8f2b-4292-984c-ffc13a379f5d', 3: '5c177431-710f-48c2-a86a-7990c016a001', 4: 'ca664d4f-cebb-4cd2-80d9-d79e496460f9'}
TIT = {1: 'Sumar decenas', 2: 'Restar decenas', 3: 'Contar de a diez', 4: 'Cálculos con decenas'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
R = lambda saltos, inicio, titulo: {"t": "saltos", "titulo": titulo, "min": 0, "max": 100, "cada": 10, "inicio": inicio, "saltos": saltos}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍬", "lineas": ["Sofi vuelve al kiosco.", "Guarda caramelos en bolsitas de 10.", "¡Llega un pedido nuevo!"], "titulo": "SUMAR", "sub": "decenas",
  "voz": ["Sofi vuelve al *kiosco* de la escuela.", "Guarda los caramelos en bolsitas de 10.", "¡Y llega un pedido nuevo!", "Hoy: *sumar decenas*."]},
 {"t": "juntar", "a": {"emoji": "🛍️", "n": 2}, "b": {"emoji": "🛍️", "n": 3}, "texto": "20 + 30 = 50",
  "voz": ["Sofi tiene *2* bolsitas. Le traen *3* más.", "Juntamos todas las bolsitas.", "¡5 bolsitas son *50* caramelos!"]},
 {"t": "definicion", "palabra": "DECENA ENTERA", "texto": "Termina en 0: 10, 20, 30…", "emoji": "🛍️",
  "voz": ["Una *decena entera* termina en cero.", "Son bolsitas *sin sueltos*."]},
 R([{"a": 10, "txt": "+10"}, {"a": 10, "txt": "+10"}, {"a": 10, "txt": "+10"}], 20, "20 + 30"),
 {"t": "consejo", "titulo": "SUMÁ LAS BOLSITAS", "texto": "20 + 30 es como 2 + 3", "emoji": "🛍️",
  "voz": ["Truco: sumá las *bolsitas*, como 2 más 3."]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 40 + 20?", "opciones": ["42", "60", "6"], "correcta": 1,
  "voz": ["Ahora vos. 4 bolsitas y 2 bolsitas.", "¿Cuánto es 40 más 20?", "¡*60*! Seis bolsitas."]},
 {"t": "resumen", "items": [["BOLSITA", "vale 10"], ["JUNTAR", "2 + 3 bolsitas"], ["SUMA", "20 + 30 = 50"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cada *bolsita* vale 10.", "*Juntamos* las bolsitas.", "20 más 30 es *50*.", CIERRE]},
]
N1[3]["voz"] = ["Empezamos en el 20 y sumamos 30.", "Primer salto: ¡30!", "Segundo salto: ¡40!", "Tercer salto: ¡llegamos al *50*!"]

N2 = [
 {"t": "reto", "texto": "Sofi tiene 7 bolsitas y vende 2. ¿Cuántas quedan?", "segundos": 6, "respuesta": "¡5!", "emoji": "🛍️", "titulo": "RESTAR", "sub": "decenas",
  "voz": ["Desafío: Sofi tiene 7 bolsitas y vende 2.", "¡Le quedan *5*!", "Hoy: *restar decenas*."]},
 {"t": "sacar", "emoji": "🛍️", "n": 7, "menos": 2, "texto": "70 − 20 = 50",
  "voz": ["Sofi tiene *70* caramelos: 7 bolsitas.", "Vende 2 bolsitas.", "¡Le quedan *50* caramelos!"]},
 {"t": "definicion", "palabra": "RESTAR DECENAS", "texto": "Sacar bolsitas enteras", "emoji": "➖",
  "voz": ["*Restar decenas* es sacar bolsitas enteras.", "Como 7 menos 2, ¡pero con bolsitas!"]},
 R([{"a": -10, "txt": "−10"}, {"a": -10, "txt": "−10"}], 70, "70 − 20"),
 {"t": "pregunta", "pregunta": "¿Cuánto es 80 − 30?", "opciones": ["50", "11", "5"], "correcta": 0,
  "voz": ["Ahora vos. 8 bolsitas, vendemos 3.", "¿Cuánto es 80 menos 30?", "¡*50*! Cinco bolsitas."]},
 {"t": "errores", "items": [{"mal": "Olvidar el 0: 70 − 20 = 5", "bien": "70 − 20 = 50"}],
  "voz": ["Ojo con este error.", "¡No te olvides del *cero*! Son 50."]},
 {"t": "resumen", "items": [["VENDER", "sacar bolsitas"], ["RESTAR", "7 − 2 bolsitas"], ["RESTA", "70 − 20 = 50"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Vender* es sacar bolsitas.", "Restamos *como con números chicos*.", "70 menos 20 es *50*.", CIERRE]},
]
N2[3]["voz"] = ["Empezamos en el 70 y restamos 20.", "Un salto para atrás: ¡60!", "Otro salto: ¡llegamos al *50*!"]

N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Cuántos caramelos hay?"}, {"yo": True, "txt": "Muchas bolsitas de 10"}, {"yo": False, "txt": "¡Contalas rápido!"}], "titulo": "CONTAR", "sub": "de a diez",
  "voz": ["Tomi le escribe a Sofi.", "¿Cuántos caramelos hay en el kiosco?", "¡Hay muchas bolsitas de 10!", "Hoy: *contar de a diez*."]},
 {"t": "tren", "titulo": "DE 10 EN 10", "desde": 10, "hasta": 100, "paso": 10,
  "voz": ["Llega el tren de las *decenas*.", "10, 20, 30, 40, 50, 60, 70, 80, 90, 100.", "¡Llegamos a *100*!"]},
 {"t": "tren", "titulo": "¿QUÉ FALTA?", "desde": 10, "hasta": 100, "paso": 10, "faltan": [30, 60, 90],
  "voz": ["¡Se borraron algunos vagones!", "10, 20, 30, 40, 50, 60, 70, 80, 90, 100.", "Faltaban el *30*, el *60* y el *90*."]},
 R([{"a": -10, "txt": "−10"}, {"a": -10, "txt": "−10"}, {"a": -10, "txt": "−10"}], 100, "PARA ATRÁS"),
 {"t": "pregunta", "pregunta": "100, 90, 80… ¿qué sigue?", "opciones": ["79", "70", "60"], "correcta": 1,
  "voz": ["Ahora vos. Contamos para atrás.", "100, 90, 80… ¿qué sigue?", "¡*70*!"]},
 {"t": "consejo", "titulo": "MIRÁ EL PRIMER NÚMERO", "texto": "30, 40, 50: cambia el primero", "emoji": "👀",
  "voz": ["Truco: de 10 en 10, cambia *el primer número*."]},
 {"t": "resumen", "items": [["ADELANTE", "10, 20, 30…"], ["ATRÁS", "100, 90, 80…"], ["TRUCO", "cambia el primero"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Para *adelante*: 10, 20, 30.", "Para *atrás*: 100, 90, 80.", "Cambia *el primer número*.", CIERRE]},
]
N3[3]["voz"] = ["Ahora contamos *para atrás*.", "Desde 100: ¡90!", "Otro salto: ¡80!", "Y otro más: ¡*70*!"]

N4 = [
 {"t": "noticia", "cinta": "KIOSCO DE SOFI", "titular": "¡GRAN VENTA DE CARAMELOS!", "bajada": "Llegan y se van bolsitas", "emoji": "🍬", "titulo": "CÁLCULOS", "sub": "con decenas",
  "voz": ["¡Gran venta en el kiosco de Sofi!", "Llegan y se van *bolsitas*.", "Hoy: *cálculos con decenas*."]},
 {"t": "agregar", "emoji": "🛍️", "n": 3, "mas": 4, "texto": "30 + 40 = 70",
  "voz": ["Sofi tiene *30* caramelos: 3 bolsitas.", "Compra 4 bolsitas más: 4, 5, 6, 7.", "¡Tiene *70* caramelos!"]},
 {"t": "sacar", "emoji": "🛍️", "n": 10, "menos": 3, "texto": "100 − 30 = 70",
  "voz": ["Ahora hay *100* caramelos: 10 bolsitas.", "Se venden 3 bolsitas.", "¡Quedan *70* caramelos!"]},
 {"t": "comparar", "a": {"cab": "LLEGAN", "texto": "sumamos +", "emoji": "📦"}, "b": {"cab": "SE VAN", "texto": "restamos −", "emoji": "👋"}, "signo": "o",
  "voz": ["Si *llegan* caramelos, sumamos.", "Si *se van*, restamos.", "¡Leé bien el problema!"]},
 {"t": "pregunta", "pregunta": "Hay 50. Llegan 20. ¿Qué cuenta hacemos?", "opciones": ["50 + 20", "50 − 20", "20 − 50"], "correcta": 0,
  "voz": ["Ahora vos. Hay 50 y llegan 20.", "¿Qué cuenta hacemos?", "¡*50 más 20*! Llegan, sumamos."]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 60 + 40?", "opciones": ["100", "64", "20"], "correcta": 0,
  "voz": ["La última, bien rápido.", "¿Cuánto es 60 más 40?", "¡*100*! Diez bolsitas."]},
 {"t": "resumen", "items": [["SUMAR", "50 + 40 = 90"], ["RESTAR", "80 − 50 = 30"], ["PROBLEMAS", "¿llegan o se van?"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Sumamos* cuando llegan.", "*Restamos* cuando se van.", "¡Y pensamos en *bolsitas*!", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m12-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 12 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
