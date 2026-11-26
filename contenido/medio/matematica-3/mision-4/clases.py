# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 4 · Dinero y números grandes: las 4 clases animadas.
VARIANTE: lo que dice "vuelto" lleva su parte "neutro" ("cambio") para alumnos de otros países; las clases sin palabras regionales van con "sin_variante".
Metáfora de toda la misión: la bicicletería de Don Beto. Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat3-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '2cb62deb-dd54-4e25-b8ac-6b492a9959a9', 2: 'be655e22-9d61-46b6-a229-9d6f21c19308', 3: 'bb190a37-8992-4dff-ad11-24c3027ab7db', 4: '74963e44-2be0-46dd-a84b-8f9e36379e7d'}
TIT = {1: 'Billetes y monedas de uso actual', 2: 'Formar montos grandes', 3: 'Comparar precios de cantidades grandes', 4: 'Pagar y calcular el vuelto'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
BETO = {"nombre": "Don Beto", "emoji": "👴"}

N1 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Abrió la bicicletería de Don Beto!", "bajada": "Todo se paga con billetes", "emoji": "🚲", "titulo": "LOS BILLETES", "sub": "de miles",
  "voz": ["¡Último momento: abrió la *bicicletería* de Don Beto!", "Allá todo se paga con *billetes*.", "Hoy: *los billetes de miles*."]},
 {"t": "zoom", "niveles": [{"emoji": "💵", "txt": "$100"}, {"emoji": "💵", "txt": "$500"}, {"emoji": "💵", "txt": "$1.000"}, {"emoji": "💵", "txt": "$2.000"}],
  "voz": ["Este billete vale *100*.", "Este vale *500*: cinco de cien.", "Este vale *1.000*.", "¡Y este vale *2.000*: dos de mil!"]},
 {"t": "canje", "titulo": "CAMBIAMOS UN BILLETE", "grande": {"n": 1, "txt": "1.000"}, "chico": {"n": 0, "txt": "100"}, "sueltos": 0, "ec1": "1 billete de $1.000", "ec2": "10 billetes de $100",
  "voz": ["Don Beto tiene un billete de *1.000*.", "Lo cambia por billetes de 100.", "Le dan *diez* billetes.", "Cuenta: cien, doscientos… ¡mil!", "Un billete de 1.000 vale *diez* de 100."]},
 {"t": "quiz4", "pregunta": "¿Cuántos billetes de $1.000 forman $2.000?", "opciones": ["2", "20", "1"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuántos de 1.000 forman 2.000?", "Contá de mil en mil…", "¡*Dos* billetes!"]},
 {"t": "errores", "items": [{"mal": "Un billete de $500 vale lo mismo que uno de $1.000", "bien": "Dos billetes de $500 valen $1.000"}],
  "voz": ["Ojo con este error.", "Hacen falta *dos* billetes de 500 para tener 1.000."]},
 {"t": "resumen", "items": [["$1.000", "diez de $100"], ["$2.000", "dos de $1.000"], ["EL NÚMERO", "dice cuánto vale"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un billete de 1.000 vale *diez* de 100.", "Uno de 2.000 vale *dos* de 1.000.", "El número dice *cuánto vale*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Don Beto", "emoji": "👴"}, "mensajes": [{"yo": False, "txt": "El casco cuesta $3.700"}, {"yo": True, "txt": "¿Con qué billetes lo pago?"}, {"yo": False, "txt": "¡Probemos juntos!"}], "titulo": "FORMAR", "sub": "montos grandes",
  "voz": ["Don Beto avisa: el casco cuesta *3.700*.", "¿Con qué billetes lo pagamos?", "¡Probemos juntos!", "Hoy: *formar montos grandes*."]},
 {"t": "descomponer", "numero": "$3.700", "titulo": "SEPARAMOS $3.700", "partes": ["$3.000", "$700"], "resultado": "= $3.700 ✓",
  "voz": ["Queremos juntar *3.700*.", "Lo separamos en dos partes.", "Los miles: *3.000*.", "Los cientos: *700*.", "Tres mil más setecientos: ¡*3.700*!"]},
 {"t": "deslizador", "titulo": "JUNTAMOS BILLETES", "min": 0, "max": 3700, "unidad": "$", "emoji": "💵", "paradas": [{"v": 3000, "txt": "3 de $1.000"}, {"v": 3500, "txt": "+ $500"}, {"v": 3700, "txt": "+ 2 de $100"}],
  "voz": ["Tres billetes de 1.000: *3.000*.", "Uno de 500: *3.500*.", "¡Dos de 100: *3.700*!"]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "2 de $1.000 y 4 de $100", "r": "$2.400"}, {"p": "1 de $2.000 y 1 de $500", "r": "$2.500"}, {"p": "5 de $1.000", "r": "$5.000"}],
  "voz": ["¡Ronda rápida! ¿Cuánto dinero es?", "Dos de mil y cuatro de cien: *2.400*.", "Uno de dos mil y uno de quinientos: *2.500*.", "Cinco de mil: *5.000*."]},
 {"t": "errores", "items": [{"mal": "4 de $1.000 y 3 de $100 son $7.000", "bien": "4 de $1.000 y 3 de $100 son $4.300"}],
  "voz": ["Ojo con este error.", "Miles con miles, cientos con cientos: *4.300*."]},
 {"t": "resumen", "items": [["SEPARAR", "miles y cientos"], ["MILES", "billetes de $1.000"], ["CIENTOS", "de $500 y $100"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Separamos en *miles* y *cientos*.", "Los miles, con billetes de *1.000*.", "Los cientos, con billetes de *500* y *100*.", CIERRE]},
]
N3 = [
 {"t": "gancho", "emoji": "🚲", "final": "🤔", "titulo": "COMPARAR", "sub": "precios grandes",
  "voz": ["Una bici cuesta *4.250*. Un monopatín cuesta *4.520*.", "¿Cuál es más caro?", "Hoy: *comparar precios grandes*."]},
 {"t": "balanza", "izq": {"cab": "BICI", "items": ["$4.250"]}, "der": {"cab": "MONOPATÍN", "items": ["$4.520"]}, "gana": "der",
  "voz": ["Miramos primero los *miles*: 4 y 4. Empatan.", "Después las *centenas*: 2 y 5.", "¡El monopatín es *más caro*!"]},
 {"t": "ranking", "titulo": "DEL MÁS CARO AL MÁS BARATO", "items": [{"txt": "BICI GRANDE", "emoji": "🚲", "dato": "$8.900"}, {"txt": "PATINES", "emoji": "🛼", "dato": "$3.200"}, {"txt": "CASCO", "emoji": "⛑️", "dato": "$1.950"}],
  "voz": ["Ordenamos del más caro al más barato.", "Tercero, el *casco*: 1.950.", "Segundos, los *patines*: 3.200.", "¡Y primera, la *bici grande*: 8.900!"]},
 {"t": "quiz4", "pregunta": "¿Cuál es más barato?", "opciones": ["$6.080", "$6.800", "$6.008"], "correcta": 2,
  "voz": ["Ahora vos: ¿cuál es *más barato*?", "Todos tienen 6 miles. Mirá las centenas y las decenas…", "¡*6.008*!"]},
 {"t": "errores", "items": [{"mal": "$999 es más caro que $1.200", "bien": "$1.200 es más caro que $999"}],
  "voz": ["Ojo con este error.", "1.200 tiene *cuatro cifras*: es más caro."]},
 {"t": "resumen", "items": [["PRIMERO", "los miles"], ["SI EMPATAN", "las centenas"], ["MÁS CARO", "número mayor"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero miramos los *miles*.", "Si empatan, las *centenas*.", "El precio *mayor* es el más caro.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": BETO, "lugar": "🚲", "lineas": ["Tomi compra un timbre de $3.700.", "Paga con $4.000.", "¿Cuánto le devuelve Don Beto?"], "titulo": "PAGAR", "sub": "y el vuelto",
  "voz": ["Tomi compra un timbre de *3.700*.", "Paga con *4.000*.", "¿Cuánto le devuelve Don Beto?", "Hoy: *pagar y calcular el vuelto*."],
  "neutro": {"sub": "y el cambio", "voz": ["Tomi compra un timbre de *3.700*.", "Paga con *4.000*.", "¿Cuánto le devuelve Don Beto?", "Hoy: *pagar y calcular el cambio*."]}},
 {"t": "recta", "min": 3700, "max": 4000, "paso": 100, "marcas": [{"v": 3700, "txt": "precio"}, {"v": 4000, "txt": "paga"}],
  "voz": ["Contamos para adelante desde el precio.", "Empezamos en *3.700*.", "3.800, 3.900, ¡*4.000*! Son tres saltos de 100."]},
 {"t": "definicion", "palabra": "Vuelto", "texto": "Lo que te devuelven cuando pagás de más.", "emoji": "🪙",
  "voz": ["El *vuelto* es lo que te devuelven.", "Pasa cuando pagás *de más*."],
  "neutro": {"palabra": "Cambio", "texto": "Lo que te devuelven cuando pagas de más.", "voz": ["El *cambio* es lo que te devuelven.", "Pasa cuando pagas *de más*."]}},
 {"t": "pistas", "problema": "Un inflador cuesta $7.600. Paga con $10.000.", "pistas": ["De 7.600 a 8.000 hay 400", "De 8.000 a 10.000 hay 2.000"], "respuesta": "$2.400",
  "voz": ["Un inflador cuesta 7.600. Pagan con *10.000*.", "Pista: de 7.600 a 8.000 hay *400*.", "Pista: de 8.000 a 10.000 hay *2.000*.", "¡400 más 2.000: le devuelven *2.400*!"]},
 {"t": "errores", "items": [{"mal": "Cuesta $3.700, paga $4.000: le devuelven $700", "bien": "Le devuelven $300"}],
  "voz": ["Ojo con este error.", "De 3.700 a 4.000 hay *300*, no 700."]},
 {"t": "resumen", "items": [["VUELTO", "lo que sobra"], ["CONTAR", "del precio al pago"], ["SALTOS", "hasta el mil"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *vuelto* es lo que sobra.", "Contamos del *precio* al *pago*.", "Primero saltamos *hasta el mil*.", CIERRE],
  "neutro": {"items": [["CAMBIO", "lo que sobra"], ["CONTAR", "del precio al pago"], ["SALTOS", "hasta el mil"]], "voz": ["Repasemos lo que aprendimos.", "El *cambio* es lo que sobra.", "Contamos del *precio* al *pago*.", "Primero saltamos *hasta el mil*.", CIERRE]}},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m4-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 4 · Nivel {n}", "estilo": "primeros", "escenas": E}
    if n < 4: L["sin_variante"] = True
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
