# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 10 · Cuidamos nuestro entorno. Genera mision-10.json.
Regla de primeros años. Metáfora: los guardianes del patio. Cierre del año: repaso de lo aprendido.
Niveles: 1 observo el patio de la escuela · 2 qué cuida y qué daña a un ambiente · 3 armamos carteles de cuidado · 4 mostramos lo que aprendimos."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
import figuras as FG

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
P = lambda x: {"tipo": "parrafo", "texto": x}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
SA = lambda p, acepta, e, **k: {"t": "short_answer", "p": p, "o": {}, "r": {"acepta": acepta}, "e": e, **k}
ORD = lambda p, desorden, orden, e, **k: {"t": "ordering", "p": p, "o": desorden, "r": {"orden": orden}, "e": e, **k}
ESTILO = {"estilo": "primeros"}
low = lambda w: [w, w.lower(), w.capitalize()]
def acepta(*ws):
    out = []
    for w in ws: out += [w, w.lower(), w.capitalize()]
    return out

N1 = {**ESTILO,
"objetivo": "Vas a observar el patio de tu escuela.",
"vas_a_ver": ["Qué hay en el patio", "Seres vivos y cosas", "Contar y anotar"],
"secciones": [
 S(1, "El patio", [
  P("En el patio hay <b>árboles</b>, <b>plantas</b>, <b>bichitos</b>, bancos y tachos."),
  IMG("Mi patio", "Qué hay.", FG.tiras(["ÁRBOLES", "PLANTAS", "BICHITOS", "BANCOS", "TACHOS"], numeros=False, cols=3)),
 ]),
 S(1, "Vivos y no vivos", [
  D("Entorno", "Todo lo que está a nuestro alrededor."),
  P("Los árboles y los bichitos son <b>seres vivos</b>. Los bancos, <b>no</b>."),
  IMG("Separamos", "Vivos y no vivos.", FG.tiras(["VIVOS: ÁRBOL, HORMIGA", "NO VIVOS: BANCO, TACHO"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que contó Sofi. Lo vas a usar en la carpeta."),
  IMG("Registro de Sofi", "En el patio.", FG.tiras(["ÁRBOLES: 3", "TACHOS: 2", "PAPELES EN EL PISO: 8"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Observo", "planteo": "Sofi sale al patio.", "pasos": ["Mira con atención.", "Cuenta los árboles: 3.", "Lo anota."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El árbol…", "pasos": ["El árbol es un ser ___."]},
"ejemplo_solo": {"titulo": "Tu patio", "planteo": "Dibujá el patio de tu escuela con lo que tiene."},
"tip": {"titulo": "Usá los sentidos", "texto": "Mirá y escuchá con cuidado."},
"ojo": ["No toques bichitos que pican.", "Observar es mirar sin romper nada."],
"resumen": [{"titulo": "Entorno", "texto": "Lo que nos rodea."}, {"titulo": "Vivos", "texto": "Árboles, bichitos."}, {"titulo": "Registrar", "texto": "Contar y anotar."}],
"glosario": [{"palabra": "Entorno", "significado": "Lo que está a nuestro alrededor."}, {"palabra": "Cantero", "significado": "Lugar con tierra para plantas."}],
"carpeta": ["¿Cuántos árboles contó Sofi?", "¿Qué había más: tachos o papeles en el piso?", "¿El banco es un ser vivo?"],
"respuestas_carpeta": [["3", "tres", "TRES", "Tres"], acepta("PAPELES", "PAPELES EN EL PISO", "LOS PAPELES"), acepta("NO")],
"carpeta_nivel": ["aplicar", "analizar", "aplicar"],
"soluciones": {"incompleto": "VIVO.", "solo": "Tu dibujo.", "carpeta": ["3.", "PAPELES.", "NO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver qué cuida y qué daña al ambiente.",
"vas_a_ver": ["Lo que daña", "Lo que cuida", "Qué podemos hacer"],
"secciones": [
 S(1, "Lo que daña", [
  P("Tirar <b>basura</b> al piso, romper ramas y gastar agua <b>dañan</b> el ambiente."),
  IMG("Daña", "No lo hagas.", FG.tiras(["TIRAR BASURA", "ROMPER RAMAS", "DEJAR LA CANILLA ABIERTA"], numeros=False, cols=1)),
 ]),
 S(1, "Lo que cuida", [
  D("Cuidar", "Hacer cosas para que algo esté bien."),
  P("Usar el <b>tacho</b>, regar plantas y cerrar la canilla <b>cuidan</b> el ambiente."),
  IMG("Cuida", "¡Hacelo!", FG.tiras(["USAR EL TACHO", "REGAR PLANTAS", "CERRAR LA CANILLA"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las acciones. Las vas a usar en la carpeta."),
  IMG("¿Cuida o daña?", "Pensá.", FG.tiras(["PISAR EL CANTERO", "JUNTAR PAPELES", "APAGAR LA LUZ"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "En el recreo", "planteo": "Tomi termina su galletita.", "pasos": ["Tiene el papel en la mano.", "Busca el tacho.", "Lo tira ahí: ¡cuida!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La basura va…", "pasos": ["La basura va en el ___."]},
"ejemplo_solo": {"titulo": "En tu casa", "planteo": "Pensá algo que podés hacer en tu casa para cuidar."},
"tip": {"titulo": "Pensá en los animales", "texto": "La basura puede lastimar a pájaros y bichitos."},
"ojo": ["Juntá papeles con un adulto y lavate las manos.", "No juntes vidrios rotos."],
"resumen": [{"titulo": "Daña", "texto": "Basura, romper, gastar."}, {"titulo": "Cuida", "texto": "Tacho, regar, cerrar."}, {"titulo": "Vos", "texto": "Podés ayudar."}],
"glosario": [{"palabra": "Dañar", "significado": "Hacer mal."}, {"palabra": "Canilla", "significado": "Por donde sale el agua."}],
"carpeta": ["Pisar el cantero, ¿cuida o daña?", "Juntar papeles, ¿cuida o daña?", "¿Por qué apagar la luz cuida?"],
"respuestas_carpeta": [acepta("DAÑA"), acepta("CUIDA"), acepta("NO GASTA", "AHORRA", "AHORRA LUZ", "NO SE GASTA", "PARA NO GASTAR")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "TACHO.", "solo": "Por ejemplo: cerrar la canilla.", "carpeta": ["DAÑA.", "CUIDA.", "PORQUE NO SE GASTA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a armar un cartel para cuidar el ambiente.",
"vas_a_ver": ["Partes del cartel", "Escribir el mensaje", "Revisar"],
"secciones": [
 S(1, "Partes del cartel", [
  D("Cartel", "Papel grande con un mensaje para todos."),
  P("Tiene un <b>título</b>, un <b>dibujo</b> y un <b>mensaje</b> corto."),
  IMG("El cartel", "Tres partes.", FG.tiras(["TÍTULO", "DIBUJO", "MENSAJE"], numeros=True, cols=3)),
 ]),
 S(1, "El mensaje", [
  P("El mensaje es <b>corto</b> y dice qué hacer: <b>USÁ EL TACHO</b>."),
  IMG("Mensajes", "Cortos y claros.", FG.tiras(["USÁ EL TACHO", "CERRÁ LA CANILLA", "CUIDÁ LAS PLANTAS"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cartel de Tomi. Lo vas a usar en la carpeta."),
  IMG("Cartel de Tomi", "¿Está bien escrito?", FG.tiras(["CUIDÁ LAS PLANTA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Mi cartel", "planteo": "Sofi arma su cartel.", "pasos": ["Título: EL PATIO.", "Dibuja un tacho.", "Mensaje: USÁ EL TACHO."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Mensaje para el agua…", "pasos": ["CERRÁ LA ___."]},
"ejemplo_solo": {"titulo": "Tu cartel", "planteo": "Armá un cartel con título, dibujo y mensaje."},
"tip": {"titulo": "Letras grandes", "texto": "Escribí grande para que se lea de lejos."},
"ojo": ["Revisá que se entienda.", "Pocas palabras: el mensaje es corto."],
"resumen": [{"titulo": "Título", "texto": "Arriba."}, {"titulo": "Dibujo", "texto": "Ayuda a entender."}, {"titulo": "Mensaje", "texto": "Corto y claro."}],
"glosario": [{"palabra": "Mensaje", "significado": "Lo que queremos decir."}, {"palabra": "Título", "significado": "Nombre del cartel."}],
"carpeta": ["¿Qué palabra está mal escrita en el cartel de Tomi?", "¿Cómo se escribe bien?", "¿Qué partes tiene un cartel?"],
"respuestas_carpeta": [acepta("PLANTA"), acepta("PLANTAS"), acepta("TÍTULO, DIBUJO Y MENSAJE", "TITULO, DIBUJO Y MENSAJE", "TÍTULO DIBUJO MENSAJE", "TITULO DIBUJO MENSAJE")],
"carpeta_nivel": ["error", "error", "recordar"],
"soluciones": {"incompleto": "CANILLA.", "solo": "Tu cartel.", "carpeta": ["PLANTA.", "PLANTAS.", "TÍTULO, DIBUJO Y MENSAJE."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a mostrar lo que aprendiste este año.",
"vas_a_ver": ["Lo que aprendimos", "Cuidar siempre", "Contarlo a otros"],
"secciones": [
 S(1, "Lo que aprendimos", [
  P("Aprendiste sobre tu <b>cuerpo</b>, <b>animales</b>, <b>plantas</b> y el <b>cielo</b>."),
  IMG("Mi año", "Todo lo que vimos.", FG.tiras(["MI CUERPO", "ANIMALES", "PLANTAS", "EL CIELO"], numeros=False, cols=2)),
 ]),
 S(1, "Cuidar siempre", [
  D("Reutilizar", "Usar algo otra vez en vez de tirarlo."),
  P("Podemos <b>usar menos</b>, <b>reutilizar</b> y <b>separar</b> la basura."),
  IMG("Tres ideas", "Para cuidar.", FG.tiras(["USAR MENOS", "REUTILIZAR", "SEPARAR"], numeros=True, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Pensá qué vas a contar en la muestra."),
  IMG("En la muestra", "Elegí uno.", FG.tiras(["MI CARTEL", "MI CUADERNO DE CAMPO", "MI CALENDARIO DEL TIEMPO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La muestra", "planteo": "Sofi muestra su cartel.", "pasos": ["Lo levanta bien alto.", "Lee el mensaje.", "Cuenta por qué es importante."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Una botella vacía…", "pasos": ["La puedo ___ como maceta."]},
"ejemplo_solo": {"titulo": "Contalo", "planteo": "Contale a tu familia algo que aprendiste este año."},
"tip": {"titulo": "Hablá fuerte y claro", "texto": "Mirá a los que te escuchan."},
"ojo": ["Esperá tu turno para hablar.", "Escuchá a tus compañeros."],
"resumen": [{"titulo": "Aprendimos", "texto": "Cuerpo, animales, plantas, cielo."}, {"titulo": "Cuidar", "texto": "Usar menos, reutilizar."}, {"titulo": "Mostrar", "texto": "Contar a otros."}],
"glosario": [{"palabra": "Muestra", "significado": "Cuando enseñamos lo que hicimos."}, {"palabra": "Reutilizar", "significado": "Usar otra vez."}],
"carpeta": ["Nombrá algo que aprendiste este año.", "¿Qué podés hacer con una botella vacía?", "¿Qué vas a mostrar en la muestra?"],
"respuestas_carpeta": [acepta("MI CUERPO", "CUERPO", "ANIMALES", "PLANTAS", "EL CIELO", "CIELO", "LA LUNA", "EL SOL", "LAS MEZCLAS", "MATERIALES"), acepta("REUTILIZARLA", "REUTILIZAR", "UNA MACETA", "MACETA", "SEPARARLA", "RECICLARLA"), acepta("MI CARTEL", "CARTEL", "MI CUADERNO DE CAMPO", "CUADERNO", "MI CALENDARIO", "CALENDARIO")],
"carpeta_nivel": ["recordar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "REUTILIZAR.", "solo": "Lo contaste en tu casa.", "carpeta": ["Por ejemplo: LAS PLANTAS.", "UNA MACETA.", "Por ejemplo: MI CARTEL."]},
}

ACT = {
"1": [MC("EN EL PATIO, ¿CUÁL ES UN SER VIVO?", ["EL ÁRBOL", "EL BANCO", "EL TACHO"], "EL ÁRBOL", "NACE Y CRECE.", n="aplicar"),
      SA("SOFI CONTÓ 3 ÁRBOLES Y 2 TACHOS. ¿CUÁNTAS COSAS CONTÓ?", ["5", "cinco", "CINCO"], "3 + 2 = 5.", n="aplicar")],
"2": [MC("¿QUÉ CUIDA EL AMBIENTE?", ["USAR EL TACHO", "TIRAR PAPELES", "ROMPER RAMAS"], "USAR EL TACHO", "LA BASURA VA AL TACHO.", n="recordar"),
      MC("TOMI DEJA LA CANILLA ABIERTA. ¿QUÉ PASA?", ["SE GASTA AGUA", "SE CUIDA EL AGUA", "NO PASA NADA"], "SE GASTA AGUA", "HAY QUE CERRARLA.", n="error")],
"3": [MC("¿QUÉ PARTES TIENE UN CARTEL?", ["TÍTULO, DIBUJO Y MENSAJE", "SOLO UN NÚMERO", "UNA PELOTA"], "TÍTULO, DIBUJO Y MENSAJE", "TRES PARTES.", n="recordar"),
      MC("¿CUÁL ES UN BUEN MENSAJE PARA UN CARTEL?", ["USÁ EL TACHO", "HOLA", "MI PERRO SE LLAMA TOBI"], "USÁ EL TACHO", "CORTO Y DICE QUÉ HACER.", n="analizar")],
"4": [MC("¿QUÉ ES REUTILIZAR?", ["USAR OTRA VEZ", "TIRAR TODO", "ROMPER"], "USAR OTRA VEZ", "COMO UNA BOTELLA MACETA.", n="recordar"),
      MC("UNA BOTELLA VACÍA, ¿CÓMO LA REUTILIZÁS?", ["COMO MACETA", "LA TIRO AL PISO", "LA ROMPO"], "COMO MACETA", "REUTILIZAR.", n="aplicar")],
"5": [MC("RELÁMPAGO. LA BASURA VA EN EL…", ["TACHO", "PISO", "CANTERO"], "TACHO", "TACHO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ DAÑA?", ["ROMPER RAMAS", "REGAR", "JUNTAR PAPELES"], "ROMPER RAMAS", "LASTIMA AL ÁRBOL.", tiempo=30, n="aplicar"),
      SA("RELÁMPAGO. ¿QUÉ HACÉS CON LA CANILLA AL TERMINAR?", acepta("CERRARLA", "LA CIERRO", "CERRAR", "CIERRO"), "CERRARLA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL ÁRBOL ES UN…", ["SER VIVO", "OBJETO", "MATERIAL"], "SER VIVO", "NACE Y CRECE.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES EL ENTORNO?", ["LO QUE NOS RODEA", "UN JUGUETE", "UN NÚMERO"], "LO QUE NOS RODEA", "EL PATIO, LA PLAZA.", n="recordar")],
 [1, MC("EN EL PATIO, ¿CUÁL NO ES UN SER VIVO?", ["EL BANCO", "LA HORMIGA", "EL ÁRBOL"], "EL BANCO", "NO NACE NI CRECE.", n="aplicar")],
 [1, SA("HAY 8 PAPELES EN EL PISO. SOFI JUNTA 8. ¿CUÁNTOS QUEDAN?", ["0", "cero", "CERO", "NINGUNO", "ninguno"], "8 − 8 = 0.", n="aplicar")],
 [2, MC("¿QUÉ DAÑA AL AMBIENTE?", ["TIRAR BASURA AL PISO", "REGAR PLANTAS", "CERRAR LA CANILLA"], "TIRAR BASURA AL PISO", "ENSUCIA Y LASTIMA ANIMALES.", n="recordar")],
 [2, MC("¿POR QUÉ LA BASURA DAÑA A LOS PÁJAROS?", ["PUEDE LASTIMARLOS", "LOS HACE VOLAR", "LES DA COMIDA RICA"], "PUEDE LASTIMARLOS", "SE LA PUEDEN COMER.", n="analizar")],
 [2, MC("SOFI PISA EL CANTERO PARA IR MÁS RÁPIDO. ¿QUÉ PASA?", ["DAÑA LAS PLANTAS", "CUIDA LAS PLANTAS", "NADA"], "DAÑA LAS PLANTAS", "HAY QUE IR POR EL CAMINO.", n="error")],
 [3, MC("EL MENSAJE DE UN CARTEL TIENE QUE SER…", ["CORTO Y CLARO", "LARGUÍSIMO", "SIN LETRAS"], "CORTO Y CLARO", "PARA QUE TODOS LO LEAN.", n="recordar")],
 [3, ORD("ORDENÁ LAS PARTES DEL CARTEL DE ARRIBA HACIA ABAJO.", ["MENSAJE", "TÍTULO", "DIBUJO"], ["TÍTULO", "DIBUJO", "MENSAJE"], "TÍTULO, DIBUJO, MENSAJE.", n="aplicar")],
 [3, SA("COMPLETÁ EL MENSAJE: CERRÁ LA ___", acepta("CANILLA"), "CERRÁ LA CANILLA.", n="aplicar")],
 [4, MC("¿QUÉ PODÉS HACER CON UNA BOTELLA VACÍA?", ["UNA MACETA", "TIRARLA AL PISO", "ROMPERLA"], "UNA MACETA", "REUTILIZAR.", n="aplicar")],
 [4, MC("¿CUÁL ES UNA IDEA PARA CUIDAR?", ["USAR MENOS", "GASTAR MÁS", "ROMPER TODO"], "USAR MENOS", "USAR MENOS, REUTILIZAR, SEPARAR.", n="recordar")],
 [4, MC("TOMI HABLA MIENTRAS SOFI MUESTRA SU CARTEL. ¿QUÉ CONVIENE?", ["ESPERAR SU TURNO", "GRITAR MÁS", "IRSE"], "ESPERAR SU TURNO", "ESCUCHAMOS A LOS COMPAÑEROS.", n="error")],
 [4, SA("NOMBRÁ UN SER VIVO QUE ESTUDIASTE ESTE AÑO.", acepta("PLANTA", "ÁRBOL", "ARBOL", "PERRO", "GATO", "PEZ", "RANA", "PATO", "VACA", "LEÓN", "LEON", "CONEJO", "PERSONA", "YO"), "POR EJEMPLO: LA RANA.", n="aplicar")],
]
M = {"subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "tema": 10, "estilo": "primeros",
     "practica": "Práctica general: cuidamos nuestro entorno", "examen_titulo": "Nivel jefe: cuidamos nuestro entorno",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-10.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
