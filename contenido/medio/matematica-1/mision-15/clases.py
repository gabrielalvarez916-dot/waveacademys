# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 15 · Sumar y restar con calculadora: las 4 clases animadas.
Metáfora: la calculadora del kiosco de Sofi. Plantilla nueva: `calculadora` (tools/medio/clase/motor/t-mate.js).
Genera tools/medio/clase/lecciones/medio-mat1-m15-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'dc0cbb8e-985a-4558-9c62-794e7f55ca1b', 2: '5babb0c2-1dc6-4215-b54e-fe5cca3c3874', 3: '72822d33-d452-4196-8f82-3d7b7e4d7d29', 4: '0edad486-fc1f-4ea2-a233-539185842eb6'}
TIT = {1: 'Conocer la calculadora', 2: 'Sumar y restar con teclas', 3: 'Controlar resultados', 4: 'Descubrir regularidades'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍬", "lineas": ["En el kiosco hay mucha gente.", "Sofi tiene que sumar rápido.", "¡Usa una calculadora!"], "titulo": "LA CALCULADORA", "sub": "conocerla",
  "voz": ["En el kiosco hay *mucha gente*.", "Sofi tiene que sumar muy rápido.", "¡Usa una *calculadora*!", "Hoy: *conocer la calculadora*."]},
 {"t": "calculadora", "titulo": "LA CALCULADORA DE SOFI", "teclas": ["2", "5"], "resultado": "25", "texto": "APRETÁ 2 Y 5",
  "voz": ["Esta es la *calculadora* de Sofi.", "Aprieta el 2 y después el 5.", "¡En la pantalla dice *25*!"]},
 {"t": "matriz", "titulo": "SUS PARTES", "celdas": [{"cab": "PANTALLA", "txt": "muestra los números"}, {"cab": "NÚMEROS", "txt": "del 0 al 9"}, {"cab": "+ Y −", "txt": "sumar y restar"}, {"cab": "= Y C", "txt": "resultado y borrar"}],
  "voz": ["La calculadora tiene *cuatro partes*.", "La *pantalla* muestra los números.", "Las teclas de *números*, del 0 al 9.", "El *más* y el *menos*.", "El *igual* y la *C* para borrar."]},
 {"t": "consejo", "titulo": "LA C BORRA", "texto": "Si te equivocás, apretá la C", "emoji": "🧽",
  "voz": ["Truco: si te equivocás, apretá la *C*."]},
 {"t": "pregunta", "pregunta": "¿Dónde se ve el resultado?", "opciones": ["En las teclas", "En la pantalla", "En la C"], "correcta": 1,
  "voz": ["Ahora vos. Mirá la calculadora.", "¿Dónde se ve el resultado?", "¡En la *pantalla*!"]},
 {"t": "resumen", "items": [["PANTALLA", "muestra los números"], ["NÚMEROS", "del 0 al 9"], ["SIGNOS", "+, − e ="]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *pantalla* muestra los números.", "Hay teclas de *números*.", "Y teclas de *signos*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué teclas apretás para hacer 7 + 5?", "segundos": 6, "respuesta": "7, +, 5, =", "emoji": "🧮", "titulo": "SUMAR Y RESTAR", "sub": "con teclas",
  "voz": ["Desafío: ¿qué teclas apretás para 7 más 5?", "¡7, más, 5 e *igual*!", "Hoy: *sumar y restar con teclas*."]},
 {"t": "flujo", "titulo": "EL ORDEN", "items": [{"txt": "Número", "emoji": "7️⃣"}, {"txt": "Signo", "emoji": "➕"}, {"txt": "Número", "emoji": "5️⃣"}, {"txt": "Igual", "emoji": "🟰"}],
  "voz": ["Primero, un *número*.", "Después, el *signo*.", "Después, otro *número*.", "Y al final, el *igual*."]},
 {"t": "calculadora", "teclas": ["7", "+", "5"], "resultado": "12", "texto": "7 + 5 = 12",
  "voz": ["Sumamos 7 más 5.", "Apretamos 7, más y 5.", "Apretamos igual: ¡*12*!"]},
 {"t": "calculadora", "teclas": ["1", "5", "−", "4"], "resultado": "11", "texto": "15 − 4 = 11",
  "voz": ["Ahora restamos 15 menos 4.", "Apretamos 1, 5, menos y 4.", "Apretamos igual: ¡*11*!"]},
 {"t": "pregunta", "pregunta": "¿Qué tecla va al final?", "opciones": ["+", "C", "="], "correcta": 2,
  "voz": ["Ahora vos. Pensá en el orden.", "¿Qué tecla va al final?", "¡El *igual*!"]},
 {"t": "errores", "items": [{"mal": "Olvidar el =", "bien": "Apretar = para ver el resultado"}],
  "voz": ["Ojo con este error.", "Sin el *igual*, no sale el resultado."]},
 {"t": "resumen", "items": [["ORDEN", "número, signo, número, ="], ["SUMAR", "tecla +"], ["RESTAR", "tecla −"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *orden*: número, signo, número, igual.", "Para *sumar*, la tecla más.", "Para *restar*, la tecla menos.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Hice 20 + 3 y me dio 50"}, {"yo": True, "txt": "¡Eso no puede ser!"}, {"yo": False, "txt": "¿Qué hice mal?"}], "titulo": "CONTROLAR", "sub": "resultados",
  "voz": ["Tomi le escribe a Sofi.", "Hizo 20 más 3 y le dio 50.", "¡Eso no puede ser!", "Hoy: *controlar resultados*."]},
 {"t": "calculadora", "teclas": ["2", "0", "+", "3", "0"], "resultado": "50", "texto": "¡APRETÓ 30, NO 3!",
  "voz": ["Mirá lo que apretó Tomi.", "Apretó 20, más y… ¡30!", "Por eso le dio *50*."]},
 {"t": "corrige", "titulo": "LO ARREGLAMOS", "cambios": [{"antes": "20 + 3 = 50", "despues": "20 + 3 = 23", "motivo": "apretó 30 en vez de 3"}],
  "voz": ["Corregimos la cuenta de Tomi.", "20 más 3 es *23*."]},
 {"t": "calculadora", "teclas": ["2", "0", "+", "3"], "resultado": "23", "texto": "¡AHORA SÍ: 23!",
  "voz": ["Tomi lo hace otra vez.", "Aprieta 20, más y 3.", "¡Ahora sí: *23*!"]},
 {"t": "pregunta", "pregunta": "La calculadora dice 6 + 2 = 62. ¿Está bien?", "opciones": ["Sí", "No"], "correcta": 1,
  "voz": ["Ahora vos. Pensá antes de mirar.", "6 más 2… ¿da 62?", "¡*No*! Da 8."]},
 {"t": "consejo", "titulo": "PENSÁ PRIMERO", "texto": "Si el resultado es raro, volvé a apretar", "emoji": "🤔",
  "voz": ["Truco: *pensá* el resultado antes de apretar."]},
 {"t": "resumen", "items": [["PENSAR", "antes de apretar"], ["MIRAR", "la pantalla"], ["COMPARAR", "¿dice lo mismo?"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero *pensamos*.", "Después *miramos* la pantalla.", "Y *comparamos*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "DESCUBRIMIENTO", "titular": "¡LA CALCULADORA TIENE UN SECRETO!", "bajada": "Sofi lo encontró sumando 10", "emoji": "🔍", "titulo": "DESCUBRIR", "sub": "regularidades",
  "voz": ["¡Último momento! Sofi hizo un *descubrimiento*.", "La calculadora tiene un *secreto*.", "Hoy: *descubrir regularidades*."]},
 {"t": "tren", "titulo": "SUMAR 1", "desde": 5, "hasta": 12,
  "voz": ["Sofi aprieta más 1, una y otra vez.", "5, 6, 7, 8, 9, 10, 11, 12.", "¡Va de *uno en uno*!"]},
 {"t": "tren", "titulo": "SUMAR 10", "desde": 3, "hasta": 93, "paso": 10,
  "voz": ["Ahora aprieta más 10, desde el 3.", "3, 13, 23, 33, 43, 53, 63, 73, 83, 93.", "¡El *3* del final no cambia nunca!"]},
 {"t": "cuadro", "titulo": "RESTAR 10", "hasta": 50, "desde": 1, "faltan": [17, 27, 37],
  "voz": ["Restar 10 es subir una fila del cuadro.", "47, 37, 27, 17.", "¡Cambia el *primer número*!"]},
 {"t": "pregunta", "pregunta": "4, 14, 24… ¿qué sigue?", "opciones": ["25", "34", "44"], "correcta": 1,
  "voz": ["Ahora vos. Sumamos 10 cada vez.", "4, 14, 24… ¿qué sigue?", "¡*34*!"]},
 {"t": "resumen", "items": [["+ 1", "cambia el último"], ["+ 10", "cambia el primero"], ["− 10", "baja una decena"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Más 1 cambia *el último* número.", "Más 10 cambia *el primero*.", "Menos 10 *baja una decena*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m15-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 15 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
