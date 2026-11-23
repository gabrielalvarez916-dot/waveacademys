# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 6 · Dinero hasta 1.000: las 4 clases animadas.
VARIANTE: lo que nombra los pesos (o el vuelto) lleva su parte "neutro" para alumnos de otros países.
Metáfora: el kiosco de alfajores de la abuela Rosa. Regla de primeros años (tools/medio/primeros_anios.py).
Genera tools/medio/clase/lecciones/medio-mat2-m6-n<N>.json.
Plantillas de plataformas de la misión (distintas de la misión 5): escala, memoria, completa, contrarreloj, personaje, prediccion, dilema, logro."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '88c8a4da-6933-47c5-8121-c91903a69764', 2: 'fb8ec094-ba9f-4077-b86e-95cc06acb2b1', 3: 'e7f49b6c-02ce-4734-b38a-a8abbbd01fde', 4: '64dee40e-c6d2-45b7-baa5-a02fa247c211'}
TIT = {1: 'Billetes y monedas', 2: 'Formar un monto', 3: 'Calcular el vuelto', 4: 'Comprar y comparar precios'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
CIERRE_N = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏪", "lineas": ["Rosa abrió un kiosco.", "Vende alfajores.", "Le pagan con pesos."], "titulo": "BILLETES", "sub": "y monedas",
  "voz": ["La abuela Rosa abrió un *kiosco*.", "Vende sus alfajores.", "Los chicos le pagan con *pesos*.", "Hoy: *billetes y monedas*."],
  "neutro": {"lineas": ["Rosa abrió un kiosco.", "Vende alfajores.", "Le pagan con dinero."],
             "voz": ["La abuela Rosa abrió un *kiosco*.", "Vende sus alfajores.", "Los chicos le pagan con *dinero*.", "Hoy: *billetes y monedas*."]}},
 {"t": "comparar", "a": {"cab": "BILLETE", "texto": "de papel", "emoji": "💵"}, "b": {"cab": "MONEDA", "texto": "de metal", "emoji": "🪙"}, "signo": "y",
  "voz": ["El *billete* es de papel.", "La *moneda* es de metal.", "¡Los dos sirven para pagar!"]},
 {"t": "monedas", "titulo": "BILLETES DE 100", "items": [100, 100, 100], "texto": "$300",
  "voz": ["Tomi tiene tres billetes de 100.", "100, 200, 300.", "¡Tiene *300 pesos*!"],
  "neutro": {"voz": ["Tomi tiene tres billetes de 100.", "100, 200, 300.", "¡Tiene *300*!"]}},
 {"t": "escala", "titulo": "¿CUÁL VALE MÁS?", "items": [{"txt": "$10", "emoji": "🪙", "valor": 10}, {"txt": "$100", "emoji": "💵", "valor": 100}, {"txt": "$500", "emoji": "💵", "valor": 500}],
  "voz": ["Una moneda de *10*.", "Un billete de *100*: vale más.", "Un billete de *500*: ¡vale mucho más!"]},
 {"t": "memoria", "titulo": "LA CAJA DE ROSA", "items": ["$10", "$50", "$100", "$500"], "falta": 3,
  "voz": ["Mirá la caja de Rosa.", "Se tapa… ¡y falta uno!", "¡Faltaba el billete de *500*!"]},
 {"t": "pregunta", "pregunta": "¿Cuánto son 2 billetes de $200?", "opciones": ["$400", "$4", "$2200"], "correcta": 0,
  "voz": ["Ahora vos. Dos billetes de 200.", "¿Cuánto dinero es?", "¡*400*! 200, 400."]},
 {"t": "resumen", "items": [["BILLETE", "de papel"], ["MONEDA", "de metal"], ["EL NÚMERO", "dice cuánto vale"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *billete* es de papel.", "La *moneda* es de metal.", "El *número* dice cuánto vale.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "Formá $350 con billetes", "segundos": 8, "respuesta": "$200 + $100 + $50", "emoji": "💵", "titulo": "FORMAR", "sub": "un monto",
  "voz": ["Desafío: juntá *350 pesos* con billetes.", "¡200, más 100, más 50!", "Hoy: *formar un monto*."],
  "neutro": {"voz": ["Desafío: junta *350* con billetes.", "¡200, más 100, más 50!", "Hoy: *formar un monto*."]}},
 {"t": "monedas", "titulo": "PRIMERO EL GRANDE", "items": [200, 100, 50], "texto": "$350",
  "voz": ["Rosa empieza por el billete más grande.", "200, 300, 350.", "¡Son *350*!"]},
 {"t": "consejo", "titulo": "DEL MÁS GRANDE", "texto": "Al más chico", "emoji": "💡",
  "voz": ["Truco: contá del billete *más grande* al más chico."]},
 {"t": "completa", "antes": "$500 + $200 + $20 =", "despues": "", "opciones": ["$720", "$5220", "$270"], "correcta": 0,
  "voz": ["Completá: 500, más 200, más 20.", "¿Cuánto es?", "¡*720*! 500, 700, 720."]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "$100 + $100", "r": "$200"}, {"p": "$200 + $50", "r": "$250"}, {"p": "$500 + $500", "r": "$1.000"}],
  "voz": ["¡Ronda rápida de billetes!", "100 más 100: *200*.", "200 más 50: *250*.", "500 más 500: ¡*1.000*!"]},
 {"t": "errores", "items": [{"mal": "$200 + $50 = $20050", "bien": "$200 + $50 = $250"}],
  "voz": ["Ojo con este error.", "200 más 50 es *250*."]},
 {"t": "resumen", "items": [["MONTO", "dinero en total"], ["CONTAR", "del más grande"], ["FORMAS", "hay más de una"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *monto* es el dinero en total.", "Contamos del billete *más grande*.", "Hay *más de una forma* de formarlo.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, quiero un alfajor de $80"}, {"yo": True, "txt": "¿Con cuánto pagás?"}, {"yo": False, "txt": "¡Con $100!"}], "titulo": "EL VUELTO", "sub": "lo que te devuelven",
  "voz": ["Tomi quiere un alfajor de 80.", "Rosa le pregunta: ¿con cuánto pagás?", "¡Con un billete de 100!", "Hoy: *calcular el vuelto*."],
  "neutro": {"titulo": "EL CAMBIO", "mensajes": [{"yo": False, "txt": "Abu, quiero un alfajor de $80"}, {"yo": True, "txt": "¿Con cuánto pagas?"}, {"yo": False, "txt": "¡Con $100!"}],
             "voz": ["Tomi quiere un alfajor de 80.", "Rosa le pregunta: ¿con cuánto pagas?", "¡Con un billete de 100!", "Hoy: *calcular el cambio*."]}},
 {"t": "personaje", "personaje": ROSA, "lineas": [{"txt": "Te devuelvo lo que sobra", "animo": "feliz"}, {"txt": "Contá desde 80 hasta 100", "animo": "piensa"}],
  "voz": ["Rosa explica: te devuelvo *lo que sobra*.", "Contá desde el precio hasta lo que pagaste."]},
 {"t": "saltos", "titulo": "DE 80 A 100", "min": 70, "max": 100, "cada": 10, "inicio": 80, "saltos": [{"a": 10, "txt": "+10"}, {"a": 10, "txt": "+10"}],
  "voz": ["Empezamos en el precio: 80.", "Un salto: *90*.", "Otro salto: *100*. ¡Dos saltos de 10 son *20*!"]},
 {"t": "prediccion", "pregunta": "Pagás $500 por algo de $300. ¿Cuánto te devuelven?", "a": {"txt": "$200", "emoji": "💵"}, "b": {"txt": "$800", "emoji": "🤔"}, "correcta": "a", "resultado": "¡$200! 400, 500",
  "voz": ["¿Qué creés? Pagás 500 por algo de 300.", "¿Te devuelven 200 u 800?", "¡*200*! De 300 a 500 hay 200."],
  "neutro": {"pregunta": "Pagas $500 por algo de $300. ¿Cuánto te devuelven?"}},
 {"t": "calculadora", "teclas": ["1", "0", "0", "−", "7", "0"], "resultado": "30", "texto": "100 − 70 = 30", "titulo": "CON RESTA",
  "voz": ["También se puede *restar*.", "Pagás 100, cuesta 70: 100 menos 70.", "¡Te devuelven *30*!"],
  "neutro": {"voz": ["También se puede *restar*.", "Pagas 100, cuesta 70: 100 menos 70.", "¡Te devuelven *30*!"]}},
 {"t": "errores", "items": [{"mal": "Devolver lo que pagaste", "bien": "Devolver lo que sobra"}],
  "voz": ["Ojo con este error.", "Te devuelven *lo que sobra*, no lo que pagaste."]},
 {"t": "resumen", "items": [["VUELTO", "lo que sobra"], ["CONTAR", "del precio al pago"], ["JUSTO", "sin vuelto"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *vuelto* es lo que sobra.", "Contamos desde el precio hasta el pago.", "Si pagás justo, no hay vuelto.", CIERRE],
  "neutro": {"items": [["CAMBIO", "lo que sobra"], ["CONTAR", "del precio al pago"], ["JUSTO", "sin cambio"]],
             "voz": ["Repasemos lo que aprendimos.", "El *cambio* es lo que sobra.", "Contamos desde el precio hasta el pago.", "Si pagas justo, no hay cambio.", CIERRE_N]}},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Ofertas en el kiosco!", "bajada": "Rosa cambió los precios", "emoji": "🏷️", "titulo": "COMPRAR", "sub": "y comparar",
  "voz": ["¡Último momento: ofertas en el kiosco de Rosa!", "Tomi tiene *500 pesos* para gastar.", "Hoy: *comprar y comparar precios*."],
  "neutro": {"voz": ["¡Último momento: ofertas en el kiosco de Rosa!", "Tomi tiene *500* para gastar.", "Hoy: *comprar y comparar precios*."]}},
 {"t": "balanza", "izq": {"cab": "$450", "items": ["4 de 100", "1 de 50"]}, "der": {"cab": "$540", "items": ["5 de 100", "2 de 20"]}, "gana": "der",
  "voz": ["Un jugo cuesta 450. Una galletita, 540.", "Miramos las centenas: 5 es más que 4.", "¡540 es *más caro*!"]},
 {"t": "escala", "titulo": "DEL MÁS BARATO", "items": [{"txt": "$150", "emoji": "🍬", "valor": 150}, {"txt": "$300", "emoji": "🍫", "valor": 300}, {"txt": "$900", "emoji": "🎂", "valor": 900}],
  "voz": ["Un caramelo: *150*. Es el más barato.", "Un alfajor: *300*.", "Una torta: *900*. ¡La más cara!"]},
 {"t": "dilema", "situacion": "Tomi tiene $500. ¿Qué compra?", "emoji": "🤔", "a": {"txt": "Alfajor $300 y caramelo $150", "consecuencia": "Gasta $450: ¡le alcanza!", "emoji": "✅"}, "b": {"txt": "Alfajor $300 y jugo $250", "consecuencia": "Son $550: ¡no le alcanza!", "emoji": "❌"},
  "voz": ["Tomi tiene 500. ¿Qué puede comprar?", "Alfajor y caramelo: 450. ¡Le alcanza!", "Alfajor y jugo: 550. ¡No le alcanza!"]},
 {"t": "pregunta", "pregunta": "¿Cuál es más barato?", "opciones": ["$270", "$720", "$702"], "correcta": 0,
  "voz": ["Ahora vos. 270, 720 o 702.", "¿Cuál es el *más barato*?", "¡*270*! Tiene menos centenas."]},
 {"t": "logro", "titulo": "¡NIVEL SUPERADO!", "items": ["Comparo precios", "Sumo antes de pagar", "Sé si me alcanza"], "xp": 30,
  "voz": ["Comparamos precios mirando las *centenas*.", "Sumamos los precios *antes de pagar*.", "Así sabemos si nos *alcanza*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m6-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 6 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
