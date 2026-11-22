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
