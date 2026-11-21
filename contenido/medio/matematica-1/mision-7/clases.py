# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 7 · Dinero y números (VARIANTE: pesos para Argentina; dinero sin nombre de moneda para otros países).
Metáfora: el kiosco de la escuela de Sofi. Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat1-m7-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'fb7c3aed-d805-4941-8f09-3c6e7193d989', 2: '5dbb9363-036b-4396-b501-0f541aeb3c02', 3: 'd3e93bda-076c-461b-a864-5678f5b95633', 4: '912800e8-76cc-4a36-9e18-e08de60d211b'}
TIT = {1: 'Monedas y billetes', 2: 'Contar dinero', 3: 'Pagar justo', 4: 'Comparar precios'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍬", "lineas": ["Sofi atiende el kiosco.", "Los chicos pagan con pesos.", "¡Hay monedas y billetes!"], "titulo": "MONEDAS", "sub": "y billetes",
  "voz": ["Sofi atiende el *kiosco* de la escuela.", "Los chicos pagan con *pesos*.", "Hay monedas y billetes.", "Hoy: *monedas y billetes*."],
  "neutro": {"lineas": ["Sofi atiende el kiosco.", "Los chicos pagan con dinero.", "¡Hay monedas y billetes!"],
             "voz": ["Sofi atiende el *kiosco* de la escuela.", "Los chicos pagan con *dinero*.", "Hay monedas y billetes.", "Hoy: *monedas y billetes*."]}},
 {"t": "comparar", "a": {"cab": "MONEDA", "texto": "redonda, de metal", "emoji": "🪙"}, "b": {"cab": "BILLETE", "texto": "de papel", "emoji": "💵"}, "signo": "y",
  "voz": ["La *moneda* es redonda y de metal.", "El *billete* es de papel.", "¡Los dos sirven para pagar!"]},
 {"t": "monedas", "titulo": "MONEDAS DE 10", "items": [10, 10, 10], "texto": "$30",
  "voz": ["Sofi tiene tres monedas de 10.", "10, 20, 30.", "¡*30 pesos*!"],
  "neutro": {"voz": ["Sofi tiene tres monedas de 10.", "10, 20, 30.", "¡Tiene *30*!"]}},
 {"t": "monedas", "titulo": "UN BILLETE", "items": [20, 10], "texto": "$30",
  "voz": ["Un billete de 20 y una moneda de 10.", "20, 30.", "¡También son *30*!"]},
 {"t": "consejo", "titulo": "MIRÁ EL NÚMERO", "texto": "El número dice cuánto vale", "emoji": "🔍",
  "voz": ["Truco: el *número* dice cuánto vale."]},
 {"t": "pregunta", "pregunta": "¿Cuánto vale esta moneda: $5?", "opciones": ["1", "5", "10"], "correcta": 1,
  "voz": ["Ahora vos. Mirá la moneda.", "¿Cuánto vale?", "¡*5*! Lo dice su número."]},
 {"t": "resumen", "items": [["MONEDA", "de metal"], ["BILLETE", "de papel"], ["EL NÚMERO", "dice cuánto vale"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *moneda* es de metal.", "El *billete* es de papel.", "El *número* dice cuánto vale.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Cuánto son 2 monedas de 10?", "segundos": 6, "respuesta": "¡20!", "emoji": "🪙", "titulo": "CONTAR", "sub": "dinero",
  "voz": ["Desafío: ¿cuánto son dos monedas de 10?", "¡*20*! 10, 20.", "Hoy: *contar dinero*."]},
 {"t": "monedas", "titulo": "LA CAJA DE SOFI", "items": [10, 10, 5, 1, 1], "texto": "$27",
  "voz": ["Sofi cuenta la plata de la caja.", "10, 20, 25, 26, 27.", "¡Hay *27 pesos*!"],
  "neutro": {"voz": ["Sofi cuenta el dinero de la caja.", "10, 20, 25, 26, 27.", "¡Hay *27*!"]}},
 {"t": "monedas", "titulo": "OTRA CUENTA", "items": [20, 10, 5], "texto": "$35",
  "voz": ["Ahora un billete y dos monedas.", "20, 30, 35.", "¡Son *35*!"]},
 {"t": "consejo", "titulo": "PRIMERO LO GRANDE", "texto": "Empezá por el que más vale", "emoji": "💵",
  "voz": ["Truco: empezá a contar por el que *más vale*."]},
 {"t": "pregunta", "pregunta": "$10 + $10 + $2, ¿cuánto es?", "opciones": ["12", "22", "30"], "correcta": 1,
  "voz": ["Ahora vos. Dos de 10 y uno de 2.", "¿Cuánto es todo?", "¡*22*! 10, 20, 22."]},
 {"t": "errores", "items": [{"mal": "Contar monedas: 3 monedas = 3", "bien": "Sumar lo que vale cada una"}],
  "voz": ["Ojo con este error.", "No contamos monedas: *sumamos lo que valen*."]},
 {"t": "resumen", "items": [["CONTAR", "sumando lo que vale"], ["EMPEZAR", "por lo que más vale"], ["TOTAL", "10, 20, 25…"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Contamos *sumando* lo que vale cada una.", "Empezamos por lo que *más vale*.", "Y llegamos al *total*.", CIERRE],
  "neutro": {"voz": ["Repasemos lo que aprendimos.", "Contamos *sumando* lo que vale cada una.", "Empezamos por lo que *más vale*.", "Y llegamos al *total*.", "¡Muy bien! Ahora, *a practicar*."]}},
]
N3 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍬", "lineas": ["Tomi quiere un alfajor.", "Cuesta $15.", "¿Con qué monedas paga justo?"], "titulo": "PAGAR", "sub": "justo",
  "voz": ["Tomi quiere comprar un *alfajor*.", "El alfajor cuesta *15 pesos*.", "¿Con qué monedas paga justo?", "Hoy: *pagar justo*."],
  "neutro": {"lineas": ["Tomi quiere una galleta.", "Cuesta $15.", "¿Con qué monedas paga justo?"],
             "voz": ["Tomi quiere comprar una *galleta*.", "La galleta cuesta *15*.", "¿Con qué monedas paga justo?", "Hoy: *pagar justo*."]}},
 {"t": "monedas", "titulo": "PAGA $15", "items": [10, 5], "texto": "¡JUSTO! $15",
  "voz": ["Tomi da una moneda de 10 y una de 5.", "10, 15.", "¡Pagó *justo*! No sobra nada."]},
 {"t": "monedas", "titulo": "PAGA $20", "items": [10, 5, 5], "texto": "¡JUSTO! $20",
  "voz": ["Lola compra una pelotita de 20.", "10, 15, 20.", "¡También pagó *justo*!"]},
 {"t": "errores", "items": [{"mal": "Dar $10 para algo de $15", "bien": "Falta: hay que llegar a 15"}],
  "voz": ["Ojo con este error.", "Con 10 *no alcanza*: hay que llegar a 15."]},
 {"t": "pregunta", "pregunta": "Algo cuesta $12. ¿Qué das?", "opciones": ["$10 + $2", "$10 + $5", "$5 + $5"], "correcta": 0,
  "voz": ["Ahora vos. Algo cuesta 12.", "¿Qué monedas das para pagar justo?", "¡*10 y 2*! 10, 12."]},
 {"t": "consejo", "titulo": "CONTÁ HASTA EL PRECIO", "texto": "Pagar justo es llegar al precio", "emoji": "🎯",
  "voz": ["Truco: contá hasta llegar *al precio*."]},
 {"t": "resumen", "items": [["PAGAR JUSTO", "ni más ni menos"], ["CONTAR", "hasta el precio"], ["SI FALTA", "no alcanza"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Pagar justo es *ni más ni menos*.", "Contamos hasta *el precio*.", "Si falta, *no alcanza*.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍬", "lineas": ["En el kiosco todo tiene precio.", "Un chupetín: $5.", "Un jugo: $20."], "titulo": "COMPARAR", "sub": "precios",
  "voz": ["En el kiosco todo tiene *precio*.", "Un chupetín cuesta *5 pesos*.", "Un jugo cuesta *20 pesos*.", "Hoy: *comparar precios*."],
  "neutro": {"lineas": ["En el kiosco todo tiene precio.", "Una paleta: $5.", "Un jugo: $20."],
             "voz": ["En el kiosco todo tiene *precio*.", "Una paleta cuesta *5*.", "Un jugo cuesta *20*.", "Hoy: *comparar precios*."]}},
 {"t": "comparar", "a": {"cab": "$20", "texto": "jugo", "emoji": "🧃"}, "b": {"cab": "$5", "texto": "chupetín", "emoji": "🍭"}, "signo": ">",
  "voz": ["El jugo cuesta 20.", "El chupetín cuesta 5.", "20 es *más* que 5: ¡el jugo es *más caro*!"],
  "neutro": {"b": {"cab": "$5", "texto": "paleta", "emoji": "🍭"}, "voz": ["El jugo cuesta 20.", "La paleta cuesta 5.", "20 es *más* que 5: ¡el jugo es *más caro*!"]}},
 {"t": "comparar", "a": {"cab": "$10", "texto": "manzana", "emoji": "🍎"}, "b": {"cab": "$30", "texto": "pelota", "emoji": "⚽"}, "signo": "<",
  "voz": ["La manzana cuesta 10.", "La pelota cuesta 30.", "10 es *menos* que 30: ¡la manzana es *más barata*!"]},
 {"t": "pregunta", "pregunta": "¿Qué es más caro?", "opciones": ["🍪 $8", "🧃 $18"], "correcta": 1,
  "voz": ["Ahora vos. Galletita de 8, jugo de 18.", "¿Qué es *más caro*?", "¡El jugo! 18 es más que 8."],
  "neutro": {"voz": ["Ahora tú. Galleta de 8, jugo de 18.", "¿Qué es *más caro*?", "¡El jugo! 18 es más que 8."]}},
 {"t": "pregunta", "pregunta": "¿Qué es más barato?", "opciones": ["🍭 $5", "🍎 $10"], "correcta": 0,
  "voz": ["Otra más.", "¿Qué es *más barato*?", "¡El de 5! 5 es menos que 10."]},
 {"t": "consejo", "titulo": "MÁS CARO, MÁS BARATO", "texto": "El número más grande es el más caro", "emoji": "🏷️",
  "voz": ["Truco: el número más grande es el *más caro*."]},
 {"t": "resumen", "items": [["MÁS CARO", "número más grande"], ["MÁS BARATO", "número más chico"], ["PRECIO", "lo que cuesta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Más caro*: el número más grande.", "*Más barato*: el número más chico.", "El *precio* es lo que cuesta.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m7-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 7 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
