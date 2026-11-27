# Tipos de pregunta de Wave Academy

Versión del 18/11/2026. Todo lo cerrado se corrige sin IA en la función `corregir` (modos `actividad` y `examen`). Solo `open` y `solve_complete` (o un tipo sin clave cargada) van a la IA, y si no hay ninguna de esas no se la llama.

Dónde vive cada cosa:
- `questions.options` = lo que ve el alumno (estructura).
- `question_rubrics.reference_answer` = la clave de corrección (solo admin y función; el alumno nunca la lee).
- `question_rubrics.explanation` = se muestra después de responder, en actividades (no en el examen).
- `questions.tiempo_seg` = modo Relámpago: si alguna pregunta del set lo tiene, el set se juega de a una pregunta con cronómetro.

Código: `js/wave-calc.js` (números al azar, fórmulas, número argentino, fichas; igual en app y servidor), `js/tipos-nuevos.js` (pantalla de los tipos nuevos), `supabase/functions/_shared/corregir.js` (corrector; la función `corregir` lleva una copia).

## Nivel de cada pregunta (obligatorio desde el 22/11/2026)

Cada pregunta de actividad y de examen lleva `"n"`: `recordar`, `aplicar`, `analizar` o `error`. Lo controla `tools/control_calidad.py` antes de cargar (mínimos y prohibiciones en docs/reglas-fijas-pdf.md, sección "Calidad de carpeta, actividades y examen"). La base no lee este campo: es solo para el control.

## Tipos y claves

| Tipo | Estructura (`options`) | Clave (`reference_answer`) |
|---|---|---|
| `multiple_choice`, `true_false` | lista de opciones | texto de la correcta |
| `odd_one_out` | lista de opciones | texto del intruso |
| `short_answer` | — | `{"acepta":["a","b"]}` (sin clave va a la IA) |
| `numeric` | `{"unidad":"min"}` opcional | `{"acepta":[6000]}`, `{"formula":"a*b"}`, `tolerancia`, `unidad`, `modo:"texto"` (binario) |
| `fill_blank` | el enunciado lleva `___` | `{"huecos":[["2.000","2000"],["400"]]}` |
| `ordering` | lista desordenada | `{"orden":["1","2","3"]}` |
| `matching` | `{"izquierda":[..],"derecha":[..]}` | `{"pares":{"x":"1"}}` |
| `classify` | `{"elementos":[..],"categorias":[..]}` | `{"categorias":{"x":"A"}}` |
| `table_fill` | `{"columnas":[..],"filas":[[..,""]]}` | `{"celdas":{"1|Columna":["200"]}}` |
| `multi_select` | lista de opciones | `{"correctas":[..]}` |
| `tap_text` (tocá el texto, subrayá y clasificá, detective del error) | `{"segmentos":[..],"modo":"palabras"\|"lineas","categorias":[..],"pide_correccion":"texto"}` | `{"tocar":[1,3]}` o `{"categorias":{"1":"Sujeto"},"correccion":["60"]}` (posiciones desde 0) |
| `tokens` (armá con fichas, reto de armado) | en orden: `{"fichas":[..]}`; reto: `{"fichas":["8","8","3","3"],"objetivo":24,"usar_todas":true,"operadores":[..]}` | en orden: `{"soluciones":[[..]]}`; reto: `{"ejemplo":"..."}` (vale cualquier cuenta que dé el objetivo) |
| `keywords` | `{"ayuda":".."}` | `{"grupos":[["lugar","posicion*"],["valor"]],"minimo":2}` (cada grupo son sinónimos; `*` = cualquier terminación) |
| `label_image` | `{"imagen":"data:image/png;base64,..","puntos":[{"id":"1","x":50,"y":50}],"rotulos":[..],"alt":".."}` | `{"puntos":{"1":"Núcleo"}}` |
| `open`, `solve_complete` | — | texto de referencia (lo usa la IA) |

Pregunta al revés = `multiple_choice` con el resultado en el enunciado y las cuentas o causas como opciones.
Asociación = `matching`.

## Cuentas con números al azar

Tipo `numeric` con `options`: `{"vars":{"a":{"min":12,"max":90},"b":{"min":3,"max":9}},"calculadas":{"c":"a*b"},"reglas":["a%10!=0","c<500"]}`. El enunciado usa `{a}` y `{b}`. La clave es `{"formula":"a*b"}`. Cada intento sortea otros números (semilla), se repite hasta cumplir todas las reglas, y el servidor recalcula con la misma semilla. Hay que comprobar siempre que las reglas dejen resultados posibles (si no hay manera, la pregunta queda sin números).

Operadores de las fórmulas y reglas: `+ - * / % ^ == != < > <= >= && ||`, funciones `abs min max floor ceil round sqrt mcd digitos`.

## Modo Relámpago

Se activa poniendo `tiempo_seg` (3 a 300) a las preguntas de un set (actividad o examen). Una pregunta por vez; si se acaba el tiempo pasa sola a la siguiente (cuenta como respondida con lo que haya).

## Examen (nivel jefe): 5 preguntas
- Cada intento sortea **5 preguntas**: 4 del banco del examen de la misión actual + 1 del banco del examen de la misión anterior (misma materia). En la primera misión, las 5 son de la actual.
- Actual: se reparte entre lecciones (`questions.lesson_id`), primero las menos vistas, y deja para el final las que tienen el mismo enunciado que una pregunta de las actividades de esa misión.
- Anterior: prioriza lo que al alumno le fue mal (promedio en exámenes y nota de las actividades de esa lección); si no hay datos, las no vistas.
- `corregir` (modo examen) siempre exige `sorteo_id`; lee las preguntas del sorteo con permisos de servidor.
- Para que el "tema flojo" funcione, cargá `lesson_id` en las preguntas del banco del examen (la lección que evalúa).

## Inglés estilo app de idiomas (marcas en el enunciado)
Se escriben dentro del texto de la pregunta; la corrección no cambia (js/ingles-duo.js, solo en alumno.html).
- `[[audio:Where is the library?]]` → botones 🔊 Escuchar y 🐢 Despacio (voz en inglés del navegador). Con `short_answer` (acepta) = escribí lo que escuchás; con `multiple_choice` = escuchá y elegí.
- `[[hablar:Good morning]]` → lo anterior + 🎤 Hablar; escribe lo que el navegador entendió en el campo. Usar con `short_answer` + `acepta`. Si no hay micrófono, el alumno escribe.
- `[[memorama]]` → en `matching`, se juega con tarjetas. La pareja k de `izquierda` debe ser la k de `derecha` (mismo orden). Sin la marca, las opciones de la derecha se mezclan solas.
- `multiple_choice` con opciones que son todas emojis → se muestran como fichas grandes ("elegí la imagen").

## Actividades-juego (desde 23/11/2026): crucigrama, sopa de letras y escape room
Son marcas en el enunciado (js/juegos-act.js, solo en alumno.html); la corrección no cambia porque usan tipos que ya existen.
Armarlas con `tools/juegos_actividad.py` (no a mano):
- `crucigrama([(respuesta, pista), ...], consigna)` → `fill_blank` con `[[crucigrama:fila,col,h|v,largo;...]]`: la herramienta cruza las palabras sola. Cada palabra es un hueco (acepta con y sin espacios).
- `sopa([palabras], consigna)` → `multi_select` con `[[sopa]]`: todas las opciones son palabras a encontrar (la grilla se arma sola en la pantalla). Encontrar una palabra marca su opción.
- `escape(pregunta)` → agrega `[[escape]]` a la primera pregunta de una ACTIVIDAD (no examen): un candado por pregunta que se abre al comprobarla bien; con todos abiertos, «¡Escapaste!».
Sugerencia: crucigrama y sopa para vocabulario y conceptos clave; escape room para la práctica general o un nivel de cierre.

## Actividades plus (solo actividades, nunca examen)

Se activan con una marca al principio del enunciado. La marca no se ve. Cambian la pantalla, pero la corrección es la del tipo de siempre, con su clave de siempre (tabla de arriba). Una marca por pregunta. Cada actividad tiene que resolverse en uno o dos minutos.

| Marca | Tipo | Qué hace el alumno | Clave |
|---|---|---|---|
| `[[error]]` | `tap_text` modo `lineas` | toca el paso con error de una cuenta o procedimiento (cada segmento es un paso) | `{"tocar":[1]}` |
| `[[secuencia]]` | `fill_blank` | completa los pasos que faltan; los pasos se separan con `→` en el enunciado | `{"huecos":[..]}` |
| `[[comparar]]` | `multiple_choice` | compara 2 o 3 resoluciones lado a lado y elige la correcta (` \| ` = salto de línea dentro de una opción) | texto de la correcta |
| `[[causas]]` | `matching` | une cada causa (izquierda) con su consecuencia (derecha) | `{"pares":{..}}` |
| `[[etapas]]` / `[[linea]]` | `ordering` | ordena etapas de un proceso / hechos en una línea de tiempo | `{"orden":[..]}` |
| `[[oracion:Sujeto,Verbo,Complemento]]` | `tokens` | arma la oración por partes (las partes de la marca guían) | `{"soluciones":[[..]]}` |
| `[[problema]]` | `numeric`, `short_answer`, `solve_complete` | problema verbal: los datos salen resaltados y tiene un borrador que no se entrega | la del tipo |
| `[[piezas:4]]`, `[[piezas:4:circulo]]`, `[[piezas:4:barra:2]]` | `numeric` | pinta piezas de 1 o más enteros partidos en 4 → escribe `3/4` | `{"acepta":[0.75]}` |
| `[[repartir:12:3:🍎]]` | `numeric` | reparte 12 objetos en 3 grupos → escribe cuántos hay en cada grupo (solo si quedaron iguales; puede sobrar) | `{"acepta":[4]}` |
| `[[recta:0:2:1/4]]` | `numeric` | toca la recta (de 0 a 2, de a 1/4) → escribe `5/4` (con paso decimal escribe `1,25`) | `{"acepta":[1.25]}` |
| `[[esquema]]` / `[[esquema:arbol]]` | `matching` o `classify` | completa un esquema tocando nombres (en `arbol` el primer elemento de la izquierda es el de arriba) | la del tipo |
| `[[arrastrar]]` | `label_image` | rotula tocando el nombre y después el punto | `{"puntos":{..}}` |
| `[[geoplano:6:area]]` / `[[geoplano:6:perimetro]]` | `numeric` | construye una figura en una cuadrícula de 6×6 → escribe el área (en cuadraditos) o el perímetro | `{"acepta":[6]}` (con diagonales usar `tolerancia`) |
| `[[funcion]]` / `[[funcion:5]]` | `fill_blank` con 2 huecos: `y = ___x + ___` | marca dos puntos en el plano → completa pendiente y ordenada (enteros o fracción `1/2`) | `{"huecos":[["1/2","0,5"],["1"]]}` |
| `[[molecula:H,O]]` | `short_answer` | arma la molécula con átomos → escribe la fórmula en el orden de la marca (`H2O`) | `{"acepta":["H2O"]}` |
| `[[circuito]]` / `[[sistema]]` | `multi_select` | elige piezas o partes y se van armando en el circuito o el sistema | `{"correctas":[..]}` |
| `[[simulador:Temperatura,0,100,10,°C;Tiempo,120-x,s]]` | cualquiera (casi siempre `multiple_choice` o `numeric`) | mueve el control (de 0 a 100, de a 10) y mira cómo cambian las salidas (fórmula con `x`); después responde | la del tipo |
| `[[capas:Introducción\|Desarrollo\|Cierre]]` | `open` o `keywords` | escribe el texto por partes; se entrega todo junto | la del tipo |


## Actividades de Naturales (solo actividades de nivel y generales, nunca examen) · `js/actividades-nat.js` (27/11/2026)

Mismo mecanismo que las actividades plus: una marca al principio del enunciado cambia la pantalla y lo que arma el alumno se escribe en el campo del tipo de siempre (la corrección y la clave no cambian). Los dibujos se reusan del banco de la lección de Naturales. Prueba: `python3 tools/interactiva/prueba-act-nat.py`.

| Marca | Tipo | Qué hace el alumno | Clave |
|---|---|---|---|
| `[[rotular:celula_animal]]` (también celula_vegetal, flor, planta, ojo, corazon, tierra, neurona, bacteria, virus, suelo) | `matching`: izquierda `"1","2",…` en el orden de las partes del dibujo; derecha, los nombres | toca un nombre y el número del dibujo; el rótulo queda pegado | `{"pares":{"1":"Membrana plasmática",…}}` |
| `[[red:pastizal]]` (laguna, monte) | `classify`: elementos = especies de esa red; categorías = niveles tróficos (de productor hacia arriba) | ubica cada especie en su fila; se dibujan las flechas y la energía | `{"categorias":{..}}` |
| `[[recorrido:digestion]]` (sangre, aire, savia, reflejo, orina) | `ordering` con los nombres de las estaciones | toca las estaciones en orden; la ficha se transforma | `{"orden":[..]}` |
| `[[clave:vertebrados]]` (invertebrados, plantas, reinos) | `multiple_choice` con los grupos | recorre la clave con sí / no; al llegar se marca el grupo | texto del grupo |
| `[[punnett:Aa,Aa]]` | cualquiera (casi siempre `numeric`) | completa el cuadro; se cuentan los genotipos | la del tipo |
| `[[adn:TACGGA]]` / `[[arn:TACGGA]]` | `short_answer` | arma la cadena con fichas de bases | `{"acepta":["ATGCCT"]}` |
| `[[osmosis:0:animal]]` (0 agua destilada, 1 suero, 2 agua salada; animal o vegetal) | `multiple_choice` | mira el medio y la célula antes de predecir | texto de la correcta |
| `[[mezclas]]` | `matching`: izquierda mezclas; derecha Filtración, Evaporación, Imantación, Decantación, Tamización | elige el método y ve el aparato | `{"pares":{..}}` |
| `[[densidad:120:30]]` (masa en g : volumen en cm³, hasta 40) | `numeric` | pesa en la balanza, sumerge en la probeta y calcula | `{"acepta":[4]}` |
| `[[instrumento:termometro:46]]` (probeta, regla en mm, balanza de a 50 g) | `numeric` | lee el instrumento, con lupa | `{"acepta":[46]}` |
| `[[atomo]]` | cualquiera | arma el átomo con protones, neutrones y electrones | la del tipo |
| `[[tabla]]` | `short_answer` (se escribe el símbolo) | toca el elemento en la tabla | `{"acepta":["Mg"]}` |
| `[[balancear:CH4+O2>CO2+H2O]]` | `fill_blank` con un `___` por fórmula | balancea con + y −; los contadores se ponen verdes | `{"huecos":[["1"],["2"],["1"],["2"]]}` |
| `[[ph]]` | `classify`: categorías Ácida, Neutra, Básica | ubica cada sustancia en la zona de la escala | `{"categorias":{..}}` |
| `[[ohm:serie:6:4:2]]` (o paralelo) | cualquiera | mueve las perillas y lee amperímetro y voltímetros | la del tipo |
| `[[pista:mruv:0:2]]` (mru:v o mruv:v0:a) | cualquiera | el auto avanza segundo a segundo con cinta y tabla | la del tipo |
| `[[dcl]]` | `multi_select` con fuerzas que digan «hacia arriba / abajo / la izquierda / la derecha» | marca fuerzas y se dibujan sobre la caja | `{"correctas":[..]}` |
| `[[graficar:0,-20;2,-10;4,0\|tiempo (min)\|temperatura (°C)]]` | cualquiera | ubica los puntos de la tabla y se traza la línea | la del tipo |
| `[[experimento]]` | `classify`: categorías Cambia…, Se mide…, Queda igual… | arma los dos montajes | `{"categorias":{..}}` |
| `[[luna]]` | `matching`: izquierda `"1".."4"` (1 izquierda, 2 abajo, 3 derecha, 4 arriba; el Sol a la izquierda) | ubica cada fase en la órbita | `{"pares":{"1":"Luna nueva",…}}` |
| `[[plato]]` | `classify`: categorías = grupos de alimentos | arma el plato | `{"categorias":{..}}` |
