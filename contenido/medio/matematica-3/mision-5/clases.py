# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 5 · Sumar con tres y cuatro cifras: las 4 clases animadas.
Metáfora de toda la misión: la colecta de botellas para reciclar de la escuela de Sofi.
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m5-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '0e37924c-34be-4ca6-903d-adc48bba2af9', 2: '56c3080d-65cd-48c5-bc1a-7f96354be596', 3: 'ec72f326-f881-496f-b8aa-a9699b148baf', 4: '625f8e80-e05f-4c29-bdde-b6e4f1445b6d'}
TIT = {1: 'Sumar centenas y miles', 2: 'Sumar con cuatro cifras descomponiendo', 3: 'Estimar una suma', 4: 'Sumas de memoria con miles'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "reto", "texto": "Juntaron 2.400 botellas. Llegan 1.300 más. ¿Cuántas hay?", "segundos": 8, "respuesta": "¡3.700!", "emoji": "♻️", "titulo": "SUMAR", "sub": "centenas y miles",
  "voz": ["Desafío: la escuela juntó *2.400* botellas.", "Llegan *1.300* más. ¿Cuántas hay?", "¡*3.700*!", "Hoy: *sumar centenas y miles*."]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "2.000 + 3.000", "r": "5.000"}, {"p": "400 + 500", "r": "900"}, {"p": "1.200 + 1.300", "r": "2.500"}],
  "voz": ["¡Ronda rápida para entrar en calor!", "2.000 más 3.000 es *5.000*.", "400 más 500 es *900*.", "1.200 más 1.300 es *2.500*."]},
 {"t": "tabla", "titulo": "MILES CON MILES", "columnas": ["", "M", "C", "D", "U"], "filas": [["2.400", "2", "4", "0", "0"], ["1.300", "1", "3", "0", "0"], ["SUMA", "3", "7", "0", "0"]],
  "voz": ["Ponemos los números en la tabla.", "Cientos con cientos: 4 más 3, *7*.", "Miles con miles: 2 más 1, *3*.", "¡Son *3.700* botellas!"]},
 {"t": "definicion", "palabra": "Sumar redondos", "texto": "Sumamos miles con miles y cientos con cientos.", "emoji": "➕",
  "voz": ["Sumamos *miles con miles*.", "Y *cientos con cientos*."]},
 {"t": "quiz4", "pregunta": "¿Cuánto es 3.000 + 4.000?", "opciones": ["7.000", "700", "34.000"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuánto es 3.000 más 4.000?", "Tres miles más cuatro miles…", "¡*7.000*!"]},
 {"t": "errores", "items": [{"mal": "2.000 + 500 = 7.000", "bien": "2.000 + 500 = 2.500"}],
  "voz": ["Ojo con este error.", "No se suman miles con cientos: es *2.500*."]},
 {"t": "resumen", "items": [["MILES", "con miles"], ["CIENTOS", "con cientos"], ["10 CIENTOS", "un mil"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Sumamos *miles con miles*.", "Y *cientos con cientos*.", "Diez cientos forman *un mil*.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Dos grados juntaron muchas botellas!", "bajada": "Tercero 2.345 y cuarto 1.432", "emoji": "♻️", "titulo": "SUMAR", "sub": "descomponiendo",
  "voz": ["¡Último momento: dos grados juntaron muchas botellas!", "Tercero, *2.345*. Cuarto, *1.432*.", "Hoy: *sumar descomponiendo*."]},
 {"t": "descomponer", "numero": "2.345", "titulo": "DESARMAMOS EL 2.345", "partes": ["2.000", "300", "40", "5"], "resultado": "= 2.345 ✓",
  "voz": ["Primero desarmamos el *2.345*.", "El 2 vale *2.000*.", "El 3 vale *300*.", "El 4 vale 40 y el 5 vale 5.", "¡Así lo desarmamos!"]},
 {"t": "tabla", "titulo": "LUGAR POR LUGAR", "columnas": ["", "M", "C", "D", "U"], "filas": [["2.345", "2.000", "300", "40", "5"], ["1.432", "1.000", "400", "30", "2"], ["SUMA", "3.000", "700", "70", "7"]],
  "voz": ["Desarmamos también el 1.432.", "Sumamos los *miles* y las *centenas*.", "Después, las *decenas* y las *unidades*.", "¡3.000 + 700 + 70 + 7 es *3.777*!"]},
 {"t": "completa", "antes": "2.000 + 1.000 =", "despues": "miles", "opciones": ["3.000", "300", "30"], "correcta": 0,
  "voz": ["Completá: 2.000 más 1.000…", "Miles con miles…", "¡*3.000*!"]},
 {"t": "errores", "items": [{"mal": "2.345 + 1.432 = 3.000", "bien": "2.345 + 1.432 = 3.777"}],
  "voz": ["Ojo con este error.", "Hay que sumar *todos* los lugares, no solo los miles."]},
 {"t": "resumen", "items": [["DESARMAR", "los dos números"], ["SUMAR", "lugar por lugar"], ["JUNTAR", "los resultados"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero *desarmamos* los dos números.", "Sumamos *lugar por lugar*.", "Y al final *juntamos* todo.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Sofi", "emoji": "👧"}, "mensajes": [{"yo": False, "txt": "Tenemos 3.890 y 2.105 botellas"}, {"yo": True, "txt": "¿Llegamos a 6.000?"}, {"yo": False, "txt": "¡Calculemos más o menos!"}], "titulo": "ESTIMAR", "sub": "una suma",
  "voz": ["Sofi escribe: tenemos 3.890 y 2.105 botellas.", "¿Llegamos a *6.000*?", "¡Calculemos *más o menos*!", "Hoy: *estimar una suma*."]},
 {"t": "recta", "min": 3000, "max": 5000, "paso": 1000, "marcas": [{"v": 3890, "txt": "3.890"}, {"v": 4000, "txt": "cerca: 4.000"}],
  "voz": ["Buscamos el mil más cercano en la recta.", "El 3.890 está acá, entre 3.000 y 4.000.", "¡Está muy cerca del *4.000*! Le faltan solo 110."]},
 {"t": "transforma", "titulo": "ESTIMAMOS", "pasos": [{"txt": "3.890 + 2.105"}, {"txt": "4.000 + 2.000", "nota": "redondos"}, {"txt": "CERCA DE 6.000"}],
  "voz": ["Tenemos 3.890 más 2.105.", "Cambiamos por redondos: 4.000 más *2.000*.", "¡Da *cerca de 6.000*!"]},
 {"t": "prediccion", "pregunta": "¿5.120 + 2.940 da cerca de…?", "a": {"txt": "8.000", "emoji": "😎"}, "b": {"txt": "5.000", "emoji": "🤔"}, "correcta": "a", "resultado": "¡Cerca de 8.000!",
  "voz": ["¿Qué creés? 5.120 más 2.940…", "5.000 más 3.000…", "¡Cerca de *8.000*!"]},
 {"t": "errores", "items": [{"mal": "Estimar es hacer la cuenta exacta", "bien": "Estimar es calcular más o menos"}],
  "voz": ["Ojo con este error.", "Estimar es calcular *más o menos*, con redondos.", "La cuenta exacta se hace después, para comparar."]},
 {"t": "resumen", "items": [["ESTIMAR", "más o menos"], ["REDONDEAR", "al mil cercano"], ["SIRVE", "para controlar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Estimar es calcular *más o menos*.", "Redondeamos al *mil más cercano*.", "Sirve para *controlar* la cuenta.", CIERRE]},
]
N4 = [
 {"t": "gancho", "emoji": "🧠", "final": "⚡", "titulo": "DE MEMORIA", "sub": "con miles",
  "voz": ["Sofi suma sin papel y sin calculadora.", "¿Cómo lo hace tan rápido?", "Hoy: *sumas de memoria con miles*."]},
 {"t": "mazo", "titulo": "AMIGOS DEL MIL", "items": [{"frente": "300 + ?", "dorso": "700"}, {"frente": "600 + ?", "dorso": "400"}, {"frente": "800 + ?", "dorso": "200"}],
  "voz": ["300 y *700* forman mil.", "600 y *400* forman mil.", "¡800 y *200* forman mil!"]},
 {"t": "comparar", "a": {"cab": "MILES", "texto": "2.000 + 2.000 = 4.000", "emoji": "♻️"}, "b": {"cab": "CIENTOS", "texto": "500 + 500 = 1.000", "emoji": "♻️"}, "signo": "+",
  "voz": ["Dos bolsas iguales de *2.500*: es un doble.", "El doble de 2.000 es *4.000*.", "Y el doble de 500 es *1.000*.", "¡En total, *5.000*!"]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "3.600 + ? = 4.000", "r": "400"}, {"p": "1.500 + 1.500", "r": "3.000"}, {"p": "4.000 + 3.000", "r": "7.000"}],
  "voz": ["¡Ronda rápida! De memoria.", "A 3.600 le faltan *400* para 4.000.", "1.500 más 1.500 es *3.000*.", "4.000 más 3.000 es *7.000*."]},
 {"t": "errores", "items": [{"mal": "A 3.600 le faltan 600 para 4.000", "bien": "Le faltan 400"}],
  "voz": ["Ojo con este error.", "6 cientos y *4* cientos forman un mil: faltan 400."]},
 {"t": "resumen", "items": [["AMIGOS DEL MIL", "300 y 700"], ["DOBLES", "2.500 + 2.500"], ["MILES", "como unidades"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los *amigos del mil* suman 1.000.", "Los *dobles* son fáciles.", "Los miles se suman *como unidades*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m5-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 5 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
